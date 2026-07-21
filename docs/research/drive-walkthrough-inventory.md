# Drive Walkthrough Inventory — Sprint 0

Operational inventory of walkthrough/guide assets already located in the user's private Google Drive. These sources are used for story navigation and access-path construction; they are not, by themselves, authoritative evidence for RNG mechanics, shiny locks, generation timing, or emulator behavior.

## Located walkthroughs
- Pokémon Emerald — `Detonado Emerald.pdf`
- Pokémon FireRed / LeafGreen — `Detonado FireRed_LeafGreen.pdf`
- Pokémon Diamond / Pearl — `Detonado de Pokémon Diamond_Pearl.pdf`
- Pokémon Platinum — `Detonado de Pokémon Platinum.pdf`
- Pokémon HeartGold / SoulSilver — `Detonado de Pokémon HeartGold_SoulSilver.pdf`
- Pokémon Black / White — `Detonado de Pokémon Black_White.pdf`
- Pokémon Black 2 / White 2 — `Detonado de Pokémon Black 2 _ White 2.pdf`

## Additional guide assets located
- Pokémon Emerald Prima guide (2005)
- Pokémon Diamond & Pearl official/Prima guides
- Pokémon HeartGold & SoulSilver Prima/Johto guides
- Pokémon Black & White Prima guides
- `Pokemon Locations.pdf` and related collection/reference material

## Usage policy
For each protected legendary/static/roamer target, construct a `LegendaryAccessPath` containing:
1. minimum story milestone;
2. badges/flags/key items/HMs or equivalent traversal requirements;
3. required NPC/event interactions;
4. navigation path;
5. encounter classification (static, roamer, one-time, event, etc.);
6. trigger safety classification;
7. recommended `MASTER_PRE_HUNT_SAVE` boundary;
8. Capture Readiness requirements;
9. RNG/generation method reference;
10. shiny-lock eligibility status;
11. source provenance and evidence status.

## Evidence separation
- Walkthrough/guide: progression and navigation evidence.
- Decompilation/reverse engineering/technical research: mechanics evidence.
- Emulator documentation: emulator API/behavior evidence.
- Experiment: required to promote emulator-dependent behavior to `TESTED`.

## Safety invariant
Generic story automation must never cross a protected encounter trigger solely because a walkthrough says to continue. `PRE_HUNT_STOP` and critical/irreversible triggers require the project safety gates first.
