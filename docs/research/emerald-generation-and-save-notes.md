# Emerald generation and save notes — Sprint 0

## Status legend
- CONFIRMED: supported by technical/reference evidence.
- PARTIAL: evidence exists but boundaries or version applicability need validation.
- PENDING: requires research or experiment.
- TESTED: reproduced by this project.

## Generation methods

### Static / Method 1
**CONFIRMED.** Emerald Method 1 targets include major static and legendary encounters such as Regirock, Regice, Registeel, Latias/Latios, Kyogre, Groudon, Rayquaza, Lugia, Ho-Oh, Mew and Deoxys, plus starters/gifts and selected statics. The RNG engine must keep Method 1 generation separate from wild generation.

Reference: Smogon, `RNG Manipulation of Method 1 Pokémon`.

### Wild / Method H
**CONFIRMED.** Wild encounters use Method H; H-2 is the primary/common relation described for Emerald wild RNG, while H-1 and H-4 can occur. The implementation must not assume every wild encounter follows one fixed call sequence without context reconciliation.

Reference: Smogon, `Emerald Wild Pokemon`.

## Pokémon runtime structure
**CONFIRMED with version-address caveat.** Gen III party Pokémon use a 100-byte structure. PID is at offset 0x00, OT ID at 0x04, checksum at 0x1C, encrypted data at 0x20, status at 0x50 and level at 0x54. Published references list Emerald wild/opponent party RAM near 0x02024744, but address applicability must be verified against exact ROM revision/region before production use.

Reference: Bulbapedia, `Pokémon data structure (Generation III)`.

## Save integrity
**CONFIRMED at structural level.** Gen III raw saves are 128 KiB. Two 57,344-byte game-save blocks provide current/previous redundancy. Each block has 14 sections of 4 KiB, with section ID, checksum, signature and save index in the footer. Sections rotate physically between saves. Integrity logic must resolve sections by section ID rather than assuming fixed physical order.

Critical implications:
1. A Save Factory must preserve both block semantics and section rotation rules.
2. A save cannot be declared valid merely because its file size is correct.
3. Save validation must check section IDs, signatures, checksums and coherent save indices.
4. Emulator save states and cartridge `.sav` files are distinct artifacts and must never be conflated.
5. Emerald encrypts some sensitive save fields using a security key; direct mutation of inventory/money requires version-aware handling.

Reference: Bulbapedia, `Save data structure (Generation III)`.

## ROM identity gate
**CONFIRMED.** `pret/pokeemerald` builds a reference ROM with SHA-1 `f3ae088181bf583e55daf962a92bb46f4f1d07b7`. This hash is a baseline, not an assumption about the user's dump. Runtime addresses and symbols remain gated on exact dump identity.

Reference: pret/pokeemerald.

## Required experiments before PoC promotion
- PENDING: identify exact ROM SHA-1/region/revision supplied for the PoC.
- PENDING: reconcile runtime RNG address/symbols for that exact build.
- PENDING: prove `ENCOUNTER_RAW -> reload -> identical encounter` for each encounter class used.
- PENDING: test whether save-state restoration also restores all RNG/RTC state relevant to Emerald under the selected mGBA build.
- PENDING: compare predicted vs observed PID/Nature/IV/Ability/Gender/Shiny across repeated Method 1 trials.
- PENDING: repeat separately for Method H; Method 1 success cannot validate wild generation.

## Adversarial check
A major failure mode is treating community RAM addresses, generation methods or emulator behavior as universal. Every address is version-gated; every encounter is method-gated; every rollback guarantee is experiment-gated.
