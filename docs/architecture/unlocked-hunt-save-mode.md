# Unlocked Hunt Save Mode

## Objetivo

Permitir saves alternativos, separados dos saves canônicos, para caçar Pokémon shiny que possuem shiny lock em sua própria geração/jogo, preservando a experiência de captura no jogo original sempre que tecnicamente viável.

## Princípios

1. Nunca alterar silenciosamente um save canônico.
2. Todo save desbloqueado deve ser derivado de uma cópia e ter identidade própria.
3. A remoção do shiny lock deve ser mínima, localizada e documentada.
4. O restante da lógica do encontro deve permanecer original sempre que possível: espécie, local, nível, moveset, método de encontro e progressão.
5. O sistema deve registrar ROM/revisão, patch aplicado, hash antes/depois, save de origem e target desbloqueado.
6. A Living Dex deve marcar a origem como `UNLOCKED_HUNT` para diferenciar de hunts canônicas.
7. Um shiny só pode ser marcado como `SHINY_SECURED` após captura real, save válido e backup confirmado.

## Perfis de save

- `CANONICAL`: jogo sem alteração de shiny lock.
- `UNLOCKED_HUNT`: save/ROM alternativo usado exclusivamente para targets originalmente shiny-locked.
- `RNG_OPTIMIZED`: save preparado para manipulação RNG sem remover locks.
- `CUTE_CHARM`: save com TID/SID planejado para Cute Charm Glitch onde aplicável.

## Fluxo

1. Identificar target e confirmar se há shiny lock na versão/região exata.
2. Mapear o mecanismo do lock no código/ROM.
3. Criar cópia isolada da ROM/save.
4. Aplicar patch mínimo para remover apenas o lock necessário.
5. Recalcular/validar integridade quando necessário.
6. Criar save alternativo com treinador `diego`, masculino.
7. Progredir a história normalmente até o ponto do encontro.
8. Executar Capture Readiness e checkpoint pré-hunt.
9. Caçar/capturar o shiny normalmente.
10. Registrar no tracker como `UNLOCKED_HUNT`, incluindo geração, jogo, target, patch e save.

## Gates de segurança

- Nenhum patch sem identificar hash e revisão exatos.
- Nenhum patch genérico aplicado a ROM de revisão desconhecida.
- Nenhuma alteração de odds, espécie ou encontro além do necessário para remover o lock, salvo modo explicitamente separado.
- Nenhum arquivo de ROM, save pessoal ou credencial versionado no GitHub.
- Toda mudança precisa de validação reversa e teste de que o encontro permanece funcional e capturável.

## Research backlog

Criar registry por jogo/versão com:

- Pokémon locked.
- Tipo do lock (PID reroll, forced non-shiny, fixed PID, script/event gate etc.).
- Local exato do mecanismo.
- Estratégia de patch mínima.
- Compatibilidade com RNG manipulation.
- Efeitos colaterais conhecidos.
- Evidência/fonte.
- Status: CONFIRMED / PARTIAL / PENDING / TESTED.
