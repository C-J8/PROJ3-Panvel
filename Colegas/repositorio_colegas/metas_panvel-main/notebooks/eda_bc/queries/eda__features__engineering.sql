-- Feature Engineering: Flag dia útil, Mortalidade, Natalidade e Ticket Médio por filial
WITH calendar AS (
    SELECT DISTINCT CAST(data_emissao AS DATE) AS data
    FROM panvel__vendas
),
working_days AS (
    SELECT
        data,
        ROW_NUMBER() OVER (
            PARTITION BY date_trunc('month', data)
            ORDER BY data
        ) AS rn
    FROM calendar
    WHERE dayofweek(data) NOT IN (0, 6)
      AND data NOT IN (SELECT CAST(feriado_data AS DATE) FROM seed__feriados)
),
working_days_flags AS (
    SELECT
        data,
        CASE WHEN rn = 1 THEN 1 ELSE 0 END AS fl_primeiro_dia_util,
        CASE WHEN rn = 5 THEN 1 ELSE 0 END AS fl_quinto_dia_util
    FROM working_days
),
filial_ticket_medio AS (
    SELECT
        codigo_filial,
        SUM(faturamento) / COUNT(DISTINCT codigo_documento_saida) AS ticket_medio_filial
    FROM panvel__vendas
    GROUP BY codigo_filial
),
daily_vendas AS (
    SELECT
        codigo_filial,
        CAST(data_emissao AS DATE) AS data,
        categoria_gerencial,
        SUM(faturamento) AS faturamento_total,
        SUM(quantidade) AS quantidade_total
    FROM panvel__vendas
    GROUP BY codigo_filial, data, categoria_gerencial
)
SELECT
    dv.codigo_filial,
    f.localidade,
    f.uf,
    dv.data,
    dv.categoria_gerencial,
    dv.faturamento_total,
    dv.quantidade_total,
    COALESCE(wdf.fl_primeiro_dia_util, 0) AS fl_primeiro_dia_util,
    COALESCE(wdf.fl_quinto_dia_util, 0) AS fl_quinto_dia_util,
    COALESCE(dc.taxa_mortalidade_cidade, 0.0) AS taxa_mortalidade_cidade,
    COALESCE(dc.taxa_natalidade_cidade, 0.0) AS taxa_natalidade_cidade,
    ROUND(ftm.ticket_medio_filial, 2) AS ticket_medio_filial
FROM daily_vendas dv
LEFT JOIN panvel__filiais f
  ON dv.codigo_filial = f.codigo_filial
LEFT JOIN working_days_flags wdf
  ON dv.data = wdf.data
LEFT JOIN seed__dados_cidades dc
  ON f.localidade = dc.localidade
  AND YEAR(dv.data) = dc.ano
LEFT JOIN filial_ticket_medio ftm
  ON dv.codigo_filial = ftm.codigo_filial
ORDER BY dv.codigo_filial, dv.data, dv.categoria_gerencial;
