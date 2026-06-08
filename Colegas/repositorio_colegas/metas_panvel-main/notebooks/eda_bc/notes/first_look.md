## Filiais


### Menções em outras bases

Uma das filiais apresentadas na base `filiais` não existe nas demais bases fornecidas. O que entendemos com o cliente é que essa filial foi encerrada, e podemos desconsiderá-la para o projeto.

- codigo_filial: `1704`

> eda__filiais__mencoes_bases.sql

### Casos de única filial por localidade

Um total de 12 cidades / localidades possuem somente uma filial. Sendo que:
- Nenhuma delas possui atendimento 24H
- Todas possuem Panvel Clinic e delivery
- Somente duas filiais não possuem estacionamento (`1692` e `1818`).

Concluímo também que a regional parece ser relativamente nova, com cerca de 60% das filiais tendo menos de 2 anos de operação (7/12), sendo a faixa de vida predominante `ENTRE 1-2 ANOS`. As unidades possuem uma metragem média de 526m² e estão equilibradas entre `BAIRRO` e `CENTRO`.

> eda__filiais__unica_localidade.sql  
> eda__filiais__unica_localidade_metrics.sql