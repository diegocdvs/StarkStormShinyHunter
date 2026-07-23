# StarkStormShinyHunter

Projeto de automação e assistência para shiny hunting em jogos Pokémon, com foco em arquitetura modular, segurança operacional, reprodutibilidade, progressão autônoma e pesquisa documentada.

## Comece aqui

Para assumir ou continuar o projeto sem acesso ao histórico de conversas, leia primeiro [`HANDOFF.md`](HANDOFF.md). Ele é o ponto canônico de continuidade para outro agente de IA ou desenvolvedor e consolida objetivos, invariantes, subsistemas, protocolos de hunt, regras de saves e ordem de execução.

## Status

Research Sprint 0 / fundação técnica. Escopo de Knowledge Base: Gerações I–V. Primeiro PoC vertical: Pokémon Emerald + mGBA. A estratégia é provar o pipeline completo em Emerald antes de generalizar adapters e automações por geração.

## Governança

- **Google Drive:** fonte oficial de documentação extensa, pesquisa, materiais-fonte, walkthroughs e relatórios.
- **GitHub:** fonte oficial de código, configurações versionáveis, schemas, testes e documentação de continuidade/arquitetura.
- ROMs, saves pessoais, credenciais, tokens, webhooks e outros segredos **não devem ser versionados**.
- Mudanças relevantes devem ser persistidas e versionadas; decisões importantes não devem existir apenas em conversas.
- MASTER_SAVE nunca deve ser modificado diretamente; operações usam cópias controladas.
- Operações dependentes de ROM/revisão devem falhar de forma segura quando a identidade/hash não estiver validada.

## Estrutura

- `src/` — código-fonte
- `tests/` — testes automatizados
- `config/` — exemplos, manifests e schemas sem segredos
- `docs/architecture/` — contratos, arquitetura e protocolos operacionais
- `docs/research/` — Knowledge Base e matrizes de evidência
- `scripts/` — utilitários operacionais e de pesquisa
- `web/` — Shiny Living Dex Tracker e interfaces web
- `HANDOFF.md` — contexto canônico para continuidade por outro agente/desenvolvedor

## Subsistemas principais

1. EmulatorAdapter e ROM Identity Gate.
2. RNG Engine por geração/jogo/método.
3. Save Orchestrator e checkpoints seguros.
4. Story Progression Engine e Hunt Route Planner.
5. Protocolos wild, static/legendary, egg, Masuda, Gen II breeding e Poké Radar.
6. Breeding Pokémon Repository para parents/donor saves e transferências rastreáveis.
7. Shiny Lock Registry e Unlocked Hunt Mode isolado.
8. Capture Assurance e proteção de encontros raros.
9. Shiny Living Dex Tracker com proveniência e duplicatas.
10. Integrações externas, incluindo Discord, sem versionar segredos.

## Escopo por geração

- **Gen I:** fluxos especiais de DV/proveniência retroativa e interoperabilidade Gen I↔II; não possui shiny visível nativo.
- **Gen II:** shininess por DVs, breeding intensivo, estratégia Shiny Ditto, wild/static/egg e transferências.
- **Gen III:** RSE/FRLG; Emerald é o PoC prioritário.
- **Gen IV:** DPPt/HGSS; breeding, Masuda, Poké Radar, Cute Charm/RNG e recursos específicos.
- **Gen V:** BW/B2W2; RNG/Timer0/RTC, shiny locks, Masuda e saves B2W2 especializados com Shiny Charm.

## Estados de evidência

- `CONFIRMED` — sustentado por evidência técnica/primária forte.
- `PARTIAL` — evidência existe, mas limites/contexto permanecem abertos.
- `PENDING` — requer pesquisa ou experimento.
- `TESTED` — reproduzido pelo código/PoC no ambiente declarado.

## Princípio de validação

Toda implementação relevante deve passar por validação direta e por uma segunda checagem orientada a encontrar gaps, contradições, falsos positivos, condições de borda e premissas não demonstradas.

Antes de considerar um marco concluído, aplicar também o teste de continuidade: **um novo agente com acesso autorizado ao repositório e ao Drive conseguiria continuar corretamente sem o histórico do chat?** Se não, a documentação está incompleta.
