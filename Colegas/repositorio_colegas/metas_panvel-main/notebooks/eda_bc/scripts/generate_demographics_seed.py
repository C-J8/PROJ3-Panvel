import requests
import json
import unicodedata
import os

def normalize_name(name):
    # Remove accents and convert to uppercase
    name = ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')
    return name.strip().upper()

def main():
    target_cities = [
        "APUCARANA", "ARAPONGAS", "ARAUCARIA", "CAMBE", "CAMPO LARGO", "CAMPO MOURAO",
        "CASCAVEL", "CIANORTE", "COLOMBO", "CURITIBA", "FOZ DO IGUACU", "FRANCISCO BELTRAO",
        "GOIOERE", "GUARAPUAVA", "LONDRINA", "MARINGA", "MEDIANEIRA", "PARANAGUA",
        "PARANAVAI", "PATO BRANCO", "PINHAIS", "PIRAQUARA", "PONTA GROSSA",
        "SAO JOSE DOS PINHAIS", "SARANDI", "TELEMACO BORBA", "TOLEDO", "UMUARAMA"
    ]

    print("Fetching PR municipalities from IBGE Localidades...")
    url_mun = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/PR/municipios"
    response = requests.get(url_mun)
    response.raise_for_status()
    mun_list = response.json()

    mun_mapping = {}
    for m in mun_list:
        name_norm = normalize_name(m["nome"])
        mun_mapping[name_norm] = m["id"]

    matched_codes = {}
    for city in target_cities:
        code = mun_mapping.get(city)
        if code:
            matched_codes[city] = str(code)
        else:
            for k, v in mun_mapping.items():
                if city in k or k in city:
                    matched_codes[city] = str(v)
                    break

    print(f"Matched {len(matched_codes)} cities.")

    years_to_build = [2020, 2021, 2022, 2023, 2024, 2025]
    city_yearly_data = []

    for city, code7 in matched_codes.items():
        code6 = code7[:6]
        print(f"Fetching yearly data for {city} ({code7})...")
        
        # 1. Fetch Population (SIDRA Table 6579, Var 9324)
        pop_by_year = {}
        url_pop = f"https://apisidra.ibge.gov.br/values/t/6579/n6/{code7}/v/9324/p/all"
        try:
            res = requests.get(url_pop, timeout=15)
            if res.status_code == 200:
                data = res.json()
                for row in data[1:]:
                    try:
                        yr = int(row["D3C"])
                        val = int(row["V"])
                        pop_by_year[yr] = val
                    except:
                        pass
        except Exception as e:
            print(f"  Error fetching population: {e}")

        # Interpolate / fill population for missing years
        filled_pop = {}
        for yr in years_to_build:
            if yr in pop_by_year:
                filled_pop[yr] = pop_by_year[yr]
            elif yr == 2022:
                filled_pop[yr] = pop_by_year.get(2021, pop_by_year.get(2020))
            elif yr == 2023:
                filled_pop[yr] = pop_by_year.get(2024, pop_by_year.get(2025))
            else:
                closest_year = min(pop_by_year.keys(), key=lambda k: abs(k - yr)) if pop_by_year else None
                filled_pop[yr] = pop_by_year.get(closest_year) if closest_year else 100000

        # 2. Fetch Births (Survey 39, Indicator 78159)
        births_by_year = {}
        url_births = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/39/indicadores/78159/resultados/{code6}"
        try:
            res = requests.get(url_births, timeout=15)
            if res.status_code == 200:
                data = res.json()
                if data and len(data) > 0:
                    res_dict = data[0].get("res", [{}])[0].get("res", {})
                    for yr_str, val_str in res_dict.items():
                        if val_str is not None:
                            try:
                                births_by_year[int(yr_str)] = int(val_str)
                            except ValueError:
                                pass
        except Exception as e:
            print(f"  Error fetching births: {e}")

        filled_births = {}
        latest_birth_yr = max(births_by_year.keys()) if births_by_year else None
        for yr in years_to_build:
            if yr in births_by_year:
                filled_births[yr] = births_by_year[yr]
            else:
                filled_births[yr] = births_by_year[latest_birth_yr] if latest_birth_yr else 0

        # 3. Fetch Infant Mortality Rate (Survey 39, Indicator 30279)
        mort_by_year = {}
        url_mort = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/39/indicadores/30279/resultados/{code6}"
        try:
            res = requests.get(url_mort, timeout=15)
            if res.status_code == 200:
                data = res.json()
                if data and len(data) > 0:
                    res_dict = data[0].get("res", [{}])[0].get("res", {})
                    for yr_str, val_str in res_dict.items():
                        if val_str is not None:
                            try:
                                mort_by_year[int(yr_str)] = float(val_str)
                            except ValueError:
                                pass
        except Exception as e:
            print(f"  Error fetching mortality: {e}")

        filled_mort = {}
        latest_mort_yr = max(mort_by_year.keys()) if mort_by_year else None
        for yr in years_to_build:
            if yr in mort_by_year:
                filled_mort[yr] = mort_by_year[yr]
            else:
                filled_mort[yr] = mort_by_year[latest_mort_yr] if latest_mort_yr else 0.0

        for yr in years_to_build:
            pop = filled_pop[yr]
            births = filled_births[yr]
            mort = filled_mort[yr]
            
            if births and pop:
                birth_rate = round((births / pop) * 1000, 2)
            else:
                birth_rate = 0.0
                
            city_yearly_data.append({
                "localidade": city,
                "ano": yr,
                "taxa_mortalidade": mort,
                "taxa_natalidade": birth_rate
            })

    base_dir = os.path.dirname(os.path.dirname(__file__))
    seeds_dir = os.path.join(base_dir, "seeds")
    os.makedirs(seeds_dir, exist_ok=True)
    csv_file = os.path.join(seeds_dir, "dados_cidades.csv")

    with open(csv_file, "w", encoding="utf-8") as f:
        f.write('"localidade";"ano";"taxa_mortalidade_cidade";"taxa_natalidade_cidade"\n')
        for row in city_yearly_data:
            f.write(f'"{row["localidade"]}";{row["ano"]};{row["taxa_mortalidade"]};{row["taxa_natalidade"]}\n')

    print(f"Successfully generated {csv_file}")

if __name__ == "__main__":
    main()
