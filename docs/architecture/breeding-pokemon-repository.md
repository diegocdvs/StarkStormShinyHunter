# Breeding Pokémon Repository

## Objetivo

Manter um repositório lógico de Pokémon-base disponíveis em saves especializados para acelerar breeding entre gerações, evitando reconstruir manualmente pais, espécies raras ou Pokémon que exigem transferência entre jogos.

## Conceito

O sistema deve manter um catálogo de saves contendo Pokémon úteis para breeding. Quando uma hunt por ovos exigir uma espécie que não existe naturalmente naquele jogo/geração, o agente consulta esse catálogo, localiza um save-fonte compatível, realiza a troca/transferência necessária e usa o Pokémon recebido como parent.

Exemplo operacional:

- Target: Bulbasaur shiny via breeding na Gen II.
- Bulbasaur não é obtido normalmente em Gold/Silver/Crystal.
- O agente consulta o `Breeding Pokémon Repository`.
- Localiza um save de Gen I contendo Bulbasaur.
- No save de Gen II, captura/seleciona um Pokémon descartável para a troca.
- Executa a transferência Gen I → Gen II via mecanismo compatível (ex.: Time Capsule quando aplicável).
- Valida espécie, OT, DVs e integridade pós-transferência.
- Registra o Bulbasaur transferido como parent disponível no `GEN2_BREEDING_FARM`.
- Inicia breeding com o Shiny Ditto preparado para o protocolo Gen II.

## Estrutura lógica do catálogo

Cada entrada deve registrar:

- `species`
- `form` quando aplicável
- `gender`
- `generation_origin`
- `game_origin`
- `language`
- `trainer_name`
- `trainer_gender`
- `save_id`
- `save_profile`
- `box`
- `slot`
- `breeding_compatible_generations`
- `transfer_paths`
- `special_flags`
- `is_shiny`
- `ivs_or_dvs` quando disponíveis
- `nature` quando aplicável
- `ability` quando aplicável
- `egg_moves` quando relevantes
- `provenance_status`

## Perfis de save

- `BREEDING_SOURCE_SAVE`: save-fonte que contém espécies/pais úteis.
- `BREEDING_FARM_SAVE`: save de destino usado para breeding ativo.
- `TRANSFER_STAGING_SAVE`: save intermediário para preparar e validar trocas.
- `MASTER_ARCHIVE_SAVE`: cópia imutável preservada; nunca usada diretamente.

## Política de transferência

1. Nunca operar diretamente sobre `MASTER_ARCHIVE_SAVE`.
2. Criar working copy antes de qualquer troca.
3. Validar compatibilidade entre geração, jogo, idioma e método de transferência.
4. Selecionar automaticamente um Pokémon descartável no save de destino quando uma troca exigir contraparte.
5. Nunca usar como descartável um shiny, lendário, evento, parent especial, Pokémon necessário à Living Dex ou recurso marcado como protegido.
6. Criar checkpoint/save state em ambos os lados antes da troca quando o ambiente suportar.
7. Validar o Pokémon recebido após a troca.
8. Atualizar o catálogo imediatamente após mudança de box/slot/save.
9. Registrar origem e cadeia de transferências para provenance.

## Protected Pokémon Policy

O agente deve manter uma denylist dinâmica de Pokémon que nunca podem ser usados como moeda de troca automática:

- qualquer shiny;
- qualquer Pokémon marcado `LIVING_DEX_REQUIRED`;
- lendários/míticos/eventos;
- breeding parents raros ou com DVs/IVs úteis;
- Pokémon com moves/event flags especiais;
- qualquer Pokémon explicitamente protegido pelo usuário.

## Seleção de Pokémon descartável

Quando for necessário trocar um Pokémon aleatório, o agente deve preferir:

1. captura comum e facilmente repetível;
2. espécie abundante na área atual;
3. baixo valor estratégico;
4. sem item equipado relevante;
5. sem flags especiais;
6. não shiny;
7. não necessário a outras hunts em andamento.

Se não houver candidato seguro, o agente deve capturar um novo Pokémon especificamente para servir como trade fodder.

## Integração com o Save Orchestrator

O `Save Orchestrator` deve oferecer:

- busca por espécie/atributo;
- resolução automática de save-fonte;
- cálculo da rota de transferência;
- montagem de cadeia de working copies;
- checkpoints antes/depois;
- verificação de integridade;
- atualização do catálogo após cada operação.

## Integração com Gen II Shiny Ditto Breeding

O fluxo preferencial para espécies de Gen I que serão breedadas em Gen II é:

`BREEDING_SOURCE_SAVE (Gen I)`
→ selecionar parent alvo
→ `TRANSFER_STAGING_SAVE`
→ troca via método compatível
→ `GEN2_BREEDING_FARM`
→ validar parent
→ cruzar com Shiny Ditto
→ produzir ovos em volume
→ registrar shinies obtidos

## Persistência

O catálogo deve ser armazenado em formato machine-readable no GitHub apenas como metadados e schema. Saves reais permanecem fora do GitHub, em armazenamento privado. Nenhum `.sav`, ROM, state ou credencial deve ser versionado.

## Futuro

Criar um índice HTML no Shiny Living Dex Tracker mostrando também:

- quais espécies já possuem parent disponível;
- em qual save estão;
- idiomas disponíveis;
- compatibilidade com Masuda;
- compatibilidade com Gen II Shiny Ditto breeding;
- rotas de transferência possíveis;
- quantidade de parents redundantes.
