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
),

final AS (
  SELECT
    s.*,
    CASE
      WHEN tf.total_filiais = 1 THEN TRUE
      ELSE FALSE
    END AS fl_filial_unica
  FROM source s
  LEFT JOIN total_filiais tf
    ON s.localidade = tf.localidade
)

SELECT
  *
FROM final
WHERE fl_filial_unica = TRUE
ORDER BY
  localidade,
  metragem_area_venda DESC