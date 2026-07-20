# StarkStormShinyHunter

Projeto de automação e assistência para shiny hunting em jogos Pokémon, com foco em arquitetura modular, segurança operacional, reprodutibilidade e pesquisa documentada.

## Status

Fase inicial de estruturação e Research Sprint 0.

## Governança

- **Google Drive:** fonte oficial de documentação extensa, pesquisa, decisões e relatórios.
- **GitHub:** fonte oficial de código, configurações versionáveis, testes, README e CHANGELOG.
- ROMs, saves pessoais, credenciais, tokens, webhooks e outros segredos **não devem ser versionados**.
- Mudanças relevantes devem ser persistidas e versionadas; decisões importantes não devem existir apenas em conversas.

## Estrutura prevista

- `src/` — código-fonte
- `tests/` — testes automatizados
- `config/` — exemplos e schemas de configuração sem segredos
- `docs/` — documentação técnica curta vinculada ao código
- `scripts/` — utilitários operacionais e de pesquisa

## Frentes técnicas iniciais

1. Research Sprint 0 e validação de premissas.
2. RNG e identificação de métodos de shiny hunting por jogo/geração.
3. Save Factory e checkpoints seguros.
4. Regras de shiny lock e elegibilidade.
5. Política de Poké Balls e Capture Assurance.
6. Time de captura, sobrevivência e mitigação de falhas.
7. Integrações externas, incluindo Discord, sem versionar segredos.
8. Testes, double-check e validação reversa antes de considerar etapas concluídas.

## Princípio de validação

Toda implementação relevante deve passar por validação direta e por uma segunda checagem orientada a encontrar gaps, contradições, falsos positivos, condições de borda e premissas não demonstradas.
