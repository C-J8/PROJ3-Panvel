-- Monthly Performance (Sales vs Targets) by Category
-- Achievement % = (Actual Sales / Goal) * 100
WITH metas_unpivoted AS (
    SELECT 
        date_trunc('month', data_meta_venda) as mes,
        CASE 
            WHEN categoria_meta = 'meta_n_med' THEN 'N-MED'
            WHEN categoria_meta = 'meta_med' THEN 'MED'
        END as categoria_gerencial,
        sum(valor_meta) as meta_total
    FROM (
        SELECT data_meta_venda, meta_n_med, meta_med 
        FROM panvel__metas
    )
    UNPIVOT (
        valor_meta FOR categoria_meta IN (meta_n_med, meta_med)
    )
    GROUP BY 1, 2
),
vendas_agg AS (
    SELECT 
        date_trunc('month', data_emissao) as mes,
        categoria_gerencial,
        sum(faturamento) as faturamento_total
    FROM panvel__vendas
    GROUP BY 1, 2
)
SELECT 
    v.mes,
    v.categoria_gerencial,
    v.faturamento_total,
    m.meta_total,
    (v.faturamento_total / m.meta_total) * 100 as percentual_atingimento
FROM vendas_agg v
INNER JOIN metas_unpivoted m 
    ON v.mes = m.mes 
   AND v.categoria_gerencial = m.categoria_gerencial
ORDER BY 1, 2;
