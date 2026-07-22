# Gen II — Shiny Ditto Breeding Protocol

## Objetivo

Na Geração II, priorizar breeding intensivo usando um **Shiny Ditto** como infraestrutura-base para hunts por ovos. O agente deve obter ou produzir um Shiny Ditto antes de iniciar a fazenda principal de breeding, quando tecnicamente viável.

## Estratégia preferencial

1. Obter o Red Gyarados shiny em Gen II.
2. Preservar um checkpoint canônico antes de qualquer transferência/glitch.
3. Quando compatível com a versão/emulador escolhido, usar uma cópia operacional para executar o procedimento de ida à Gen I via Time Capsule e o glitch de Ditto baseado em Transform/DVs.
4. Retornar o Ditto resultante à Gen II e validar seus DVs/shiny status.
5. Registrar o Ditto validado como `BREEDING_INFRASTRUCTURE_SHINY_DITTO`.
6. Usar esse Ditto como parent padrão para breeding de espécies compatíveis.
7. Rodar breeding em volume, com organização de boxes, contagem de ovos e registro de cada shiny obtido.

## Chance-alvo

A hipótese operacional para o protocolo é **1/64 por offspring** em cruzamentos compatíveis com Shiny Ditto na Gen II. Antes de marcar isso como `TESTED`, o projeto deve validar a derivação pelas regras de herança de DVs do jogo e reproduzir empiricamente o comportamento no ambiente de emulação escolhido.

## Regras de segurança

- Nunca modificar o `MASTER_SAVE` original.
- Criar cópias separadas para Time Capsule/glitch e breeding.
- Hash/fingerprint obrigatório de ROM e save antes/depois.
- Preservar Red Gyarados original em backup.
- Validar que o Ditto retornado possui os DVs esperados e é shiny em Gen II antes de usá-lo.
- Toda transferência entre Gen I/II precisa de save state/checkpoint em ambos os lados quando o emulador suportar.
- Se qualquer passo do glitch divergir do comportamento esperado, falhar fechado e restaurar o checkpoint.

## Integração com o Save Orchestrator

Perfis:

- `GEN2_MASTER_SAVE`
- `GEN2_SHINY_DITTO_FACTORY`
- `GEN1_TIME_CAPSULE_WORKING_SAVE`
- `GEN2_BREEDING_FARM`

O agente deve saber alternar automaticamente entre esses perfis, mantendo provenance completa.

## Living Dex provenance

Cada shiny obtido via breeding deve registrar:

- jogo e versão;
- save de origem;
- parent Shiny Ditto usado;
- espécie do outro parent;
- método `GEN2_SHINY_DITTO_BREEDING`;
- contador de ovos;
- data/hora;
- DV validation quando disponível;
- status `SHINY_SECURED` apenas após save válido + backup.

## Fonte procedural fornecida pelo usuário

Vídeo de referência para o fluxo Red Gyarados → Gen I → Ditto glitch:
`https://youtu.be/-88ZLgzFr_0`

O vídeo é tratado como referência procedural suplementar. A implementação será validada contra comportamento do jogo/disassemblies e testada no emulador antes de automação completa.
