WITH
base AS (
  SELECT DISTINCT codigo_filial, 'vendas' AS origem FROM panvel__vendas
  UNION ALL 
  SELECT DISTINCT codigo_filial, 'metas' AS origem FROM panvel__metas
  UNION ALL 
  SELECT DISTINCT codigo_filial, 'filiais' AS origem FROM panvel__filiais
  UNION ALL 
  SELECT DISTINCT codigo_filial, 'devolucoes' AS origem FROM panvel__devolucoes
),

contagem AS (
  SELECT
    codigo_filial,
    COUNT(*) as nr_origens
  FROM base
  GROUP BY codigo_filial
),

top_2 AS (
  SELECT 'Mais aparicoes' AS categoria, codigo_filial, nr_origens
  FROM contagem
  ORDER BY nr_origens DESC
  LIMIT 2
),

bottom_2 AS (
  SELECT 'Menos aparicoes' AS categoria, codigo_filial, nr_origens
  FROM contagem
  ORDER BY nr_origens ASC
  LIMIT 2
)

SELECT * FROM top_2
UNION ALL
SELECT * FROM bottom_2