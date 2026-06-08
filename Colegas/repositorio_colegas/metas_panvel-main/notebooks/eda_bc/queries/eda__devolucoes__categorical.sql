-- Monthly Returns aggregation by Category
SELECT 
    date_trunc('month', data_devolucao) as mes,
    categoria_gerencial,
    sum(valor_devolucao) as valor_devolucao_total,
    sum(quantidade) as quantidade_devolvida
FROM panvel__devolucoes
GROUP BY 1, 2
ORDER BY 1, 2;
