# Codigo Fonte

Esta pasta vai receber a versao modular da pipeline que hoje esta nos notebooks.

## Modulos planejados

- `data/`: leitura, download e validacao das bases.
- `preparation/`: construcao da `Base_V1`.
- `features/`: construcao da `Base_V2` e features de modelagem.
- `clustering/`: rotinas de clusterizacao e perfis.
- `modeling/`: treino, validacao e avaliacao de modelos.
- `utils/`: caminhos, formatacao e utilitarios compartilhados.

## Regra

Primeiro manteremos os notebooks oficiais funcionando. Depois, a logica estabilizada deve ser migrada para estes modulos.
