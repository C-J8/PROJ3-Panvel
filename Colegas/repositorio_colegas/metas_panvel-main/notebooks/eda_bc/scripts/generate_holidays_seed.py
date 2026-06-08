import os
import datetime

def get_easter_date(year):
    # Butcher's Gregorian Easter Algorithm (exact)
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    month = (h + L - 7 * m + 114) // 31
    day = ((h + L - 7 * m + 114) % 31) + 1
    return datetime.date(year, month, day)

def get_holidays_for_year(year):
    easter = get_easter_date(year)
    
    # Mobile Holidays
    carnival_monday = easter - datetime.timedelta(days=48)
    carnival_tuesday = easter - datetime.timedelta(days=47)
    good_friday = easter - datetime.timedelta(days=2)
    corpus_christi = easter + datetime.timedelta(days=60)
    
    # Last bank business day of the year (Dec 31, unless it's a weekend, then the preceding Friday)
    dec31 = datetime.date(year, 12, 31)
    if dec31.weekday() == 5:    # Saturday
        last_bank_day = dec31 - datetime.timedelta(days=1)
    elif dec31.weekday() == 6:  # Sunday
        last_bank_day = dec31 - datetime.timedelta(days=2)
    else:
        last_bank_day = dec31

    fixed_holidays = [
        (datetime.date(year, 1, 1), "Ano Novo"),
        (datetime.date(year, 4, 21), "Tiradentes"),
        (datetime.date(year, 5, 1), "Dia do Trabalho"),
        (datetime.date(year, 9, 7), "Independência do Brasil"),
        (datetime.date(year, 10, 12), "Nossa Senhora Aparecida"),
        (datetime.date(year, 11, 2), "Finados"),
        (datetime.date(year, 11, 15), "Proclamação da República"),
        (datetime.date(year, 11, 20), "Dia da Consciência Negra"),
        (datetime.date(year, 12, 25), "Natal")
    ]
    
    mobile_holidays = [
        (carnival_monday, "Segunda de Carnaval"),
        (carnival_tuesday, "Terça de Carnaval"),
        (good_friday, "Sexta-feira Santa"),
        (corpus_christi, "Corpus Christi"),
        (last_bank_day, "Último dia útil bancário")
    ]
    
    all_holidays = fixed_holidays + mobile_holidays
    all_holidays.sort(key=lambda x: x[0])
    
    # De-duplicate
    unique_holidays = []
    seen_dates = set()
    for dt, name in all_holidays:
        if dt not in seen_dates:
            unique_holidays.append((dt, name))
            seen_dates.add(dt)
            
    return unique_holidays

def main():
    years = [2023, 2024, 2025, 2026]
    records = []
    for yr in years:
        hols = get_holidays_for_year(yr)
        records.extend(hols)
        
    base_dir = os.path.dirname(os.path.dirname(__file__))
    seeds_dir = os.path.join(base_dir, "seeds")
    os.makedirs(seeds_dir, exist_ok=True)
    csv_file = os.path.join(seeds_dir, "feriados.csv")
    
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write('"feriado_data";"feriado_nome"\n')
        for dt, name in records:
            f.write(f'"{dt.isoformat()}";"{name}"\n')
            
    print(f"Successfully generated {csv_file}")

if __name__ == "__main__":
    main()
