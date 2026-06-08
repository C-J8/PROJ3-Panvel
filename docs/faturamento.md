# Convencao de Faturamento

Regra adotada para organizar a pipeline:

- `faturamento` nas bases originais de vendas representa faturamento bruto.
- `faturamento_bruto` e `faturamento_bruto_dia` devem ser tratados como a metrica principal de vendas.
- `valor_devolucao` e `valor_devolucao_dia` sao metricas auxiliares de devolucao.
- `faturamento_liquido` deve ser calculado como `faturamento_bruto - valor_devolucao`, quando fizer sentido.

## Decisao para modelagem

O alvo principal inicial deve ser faturamento bruto.

Motivos:

- os notebooks dos colegas usam `faturamento` diretamente como metrica principal;
- a comparacao com metas foi feita usando faturamento bruto;
- devolucoes podem ocorrer em data, filial ou contexto diferente da venda original;
- usar liquido como alvo sem regra de negocio validada pode introduzir ruido.

## Como usar devolucoes

Devolucoes devem entrar inicialmente como diagnostico ou feature auxiliar:

- `valor_devolucao_dia`;
- `taxa_devolucao`;
- medias moveis de devolucao;
- flags de picos ou janelas operacionais.

Antes de mudar o alvo para faturamento liquido, validar com professor/cliente se a meta oficial e comparada contra bruto ou liquido.
