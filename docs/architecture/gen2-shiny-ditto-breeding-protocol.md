# Gen II Shiny Ditto Breeding Protocol

Status: DESIGN / RESEARCH-VALIDATED CORE, EMPIRICAL EMULATOR VALIDATION PENDING

## Purpose
Define the mandatory Generation II breeding workflow for the StarkStormShinyHunter agent. The default optimization is to establish a reusable shiny Ditto breeding asset before mass breeding targets.

## Core policy
1. A Gen II breeding campaign MUST first attempt to provision a verified shiny Ditto unless an already verified compatible shiny Ditto exists in the Save Registry / Breeding Donor Registry.
2. The canonical reusable asset is stored only in a working/specialized save; master source saves remain immutable.
3. With the appropriate shiny Ditto breeding setup, the target shiny offspring probability is treated as 1/64 only for combinations for which the Gen II DV inheritance constraints have been validated. The planner MUST NOT blindly apply 1/64 to incompatible pairings.
4. Every egg is tracked with parent provenance, save fingerprint, species target, hatch count and result.
5. For evolutionary families, the planner may continue breeding after the first shiny when multiple specimens are required for a Shiny Living Dex.

## Bootstrap strategies
### A. Existing verified shiny Ditto
Preferred. Load a working clone of the registered donor save and validate the Ditto fingerprint before breeding.

### B. Native Gen II shiny Ditto hunt
Hunt/capture Ditto in Gen II, verify shiny state and DV compatibility, register it as a reusable breeding donor.

### C. Red Gyarados -> Gen I -> Ditto transformation route
This is an optional historical glitch-assisted bootstrap path. The workflow must be documented and empirically reproduced before automation is marked TESTED:
- obtain the guaranteed Red Gyarados in Gen II;
- transfer/trade through a compatible Gen I environment using a reversible working-copy workflow;
- execute the documented transformation/glitch procedure that yields a Ditto carrying the shiny-compatible DV pattern;
- trade the resulting Ditto back to Gen II;
- independently verify species, DVs and shiny status;
- register provenance as GLITCH_ASSISTED_SHINY_DITTO rather than CANONICAL_NATIVE_HUNT.

No master save may be modified during this workflow.

## Breeding loop
TARGET -> resolve donor -> validate compatibility -> deposit parents -> egg generation -> collect -> hatch -> verify shiny -> persist capture/hatch record -> update Living Dex -> continue if family quota not met.

## Safety gates
- fail closed if save/ROM identity is unknown;
- fail closed if donor identity/DVs cannot be verified;
- never overwrite MASTER_SAVE;
- checkpoint before trades and before any glitch-assisted operation;
- preserve before/after hashes for every save crossing Gen I/II boundaries;
- rollback if trade/glitch outcome differs from expected fingerprint.

## Living Dex provenance
Each offspring records method=EGG_HUNT, subtype=GEN2_SHINY_DITTO_BREEDING, parent donor ID, origin game, hatch index, save ID, and whether the Ditto bootstrap was NATIVE or GLITCH_ASSISTED.

## Pending empirical validation
- exact emulator/link-cable stack for Gen I <-> II trading;
- deterministic checkpoint boundaries around trades;
- reproduction of the Red Gyarados-derived shiny Ditto glitch from primary/technical references and the supplied video reference;
- compatibility matrix proving when the 1/64 claim applies;
- automated DV extraction from Gen II save/RAM.
