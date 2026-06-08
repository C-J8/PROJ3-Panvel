-- Monthly Sales aggregation by Category
SELECT 
    date_trunc('month', data_emissao) as mes,
    categoria_gerencial,
    sum(faturamento) as faturamento_total,
    sum(quantidade) as quantidade_total,
    sum(faturamento) / sum(quantidade) as ticket_medio
FROM panvel__vendas
GROUP BY 1, 2
ORDER BY 1, 2;
