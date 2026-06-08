WITH
source AS (
  SELECT
    codigo_filial,
    faixa_vida,
    localidade,
    tipo_estabelecimento,
    delivery,
    metragem_area_venda,
    panvel_clinic,
    estacionamento,
    atendimento_24_horas
  FROM panvel__filiais
),

total_filiais AS (
  SELECT
    localidade,
    COUNT(codigo_filial) AS total_filiais
  FROM source
  GROUP BY 1
  HAVING total_filiais = 1
),

filial_unica AS (
  SELECT
    s.*
  FROM source s
  INNER JOIN total_filiais tf
    ON s.localidade = tf.localidade
),

final AS (
  SELECT
    AVG(metragem_area_venda) AS avg_metragem_area_venda,
    COUNT(*) AS nr_filiais,
    COUNT(
      CASE
        WHEN tipo_estabelecimento = 'BAIRRO' THEN 1
      END
    ) AS nr_tipo_bairro,
    COUNT(
      CASE
        WHEN tipo_estabelecimento = 'CENTRO' THEN 1
      END
    ) AS nr_tipo_centro,
    COUNT(
      CASE
        WHEN faixa_vida = 'MENOS DE 1 ANO' THEN 1
      END
    ) AS nr_faixa_menos_1_ano,
    COUNT(
      CASE
        WHEN faixa_vida = 'ENTRE 1-2 ANOS' THEN 1
      END
    ) AS nr_faixa_1_2_anos,
    COUNT(
      CASE
        WHEN faixa_vida = 'ENTRE 2-3 ANOS' THEN 1
      END
    ) AS nr_faixa_2_3_anos,
    COUNT(
      CASE
        WHEN faixa_vida = 'MAIS DE 3 ANOS' THEN 1
      END
    ) AS nr_faixa_mais_3_anos
  FROM filial_unica
)

SELECT
  avg_metragem_area_venda,
  nr_filiais,
  nr_tipo_bairro / CAST(nr_filiais AS FLOAT) AS tx_tipo_bairro,
  nr_tipo_centro / CAST(nr_filiais AS FLOAT) AS tx_tipo_centro,
  
  nr_faixa_menos_1_ano,
  nr_faixa_menos_1_ano / CAST(nr_filiais AS FLOAT) AS tx_faixa_menos_1_ano,
  
  nr_faixa_1_2_anos,
  nr_faixa_1_2_anos / CAST(nr_filiais AS FLOAT) AS tx_faixa_1_2_anos,
  
  nr_faixa_2_3_anos,
  nr_faixa_2_3_anos / CAST(nr_filiais AS FLOAT) AS tx_faixa_2_3_anos,
  
  nr_faixa_mais_3_anos,
  nr_faixa_mais_3_anos / CAST(nr_filiais AS FLOAT) AS tx_faixa_mais_3_anos
FROM final