SELECT
    data_devolucao::DATE as data,
    codigo_filial,
    categoria_gerencial,
    count(*) as nr_devolucoes_no_dia,
    sum(valor_devolucao) as valor_total_dia,
    sum(valor_devolucao) / sum(quantidade) as ticket_medio_devolucao
FROM panvel__devolucoes
GROUP BY 1, 2, 3
HAVING sum(valor_devolucao) > 50000
ORDER BY valor_total_dia DESC