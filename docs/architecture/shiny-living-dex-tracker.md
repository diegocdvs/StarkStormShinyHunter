# Shiny Living Dex Tracker

## Purpose

The tracker is a first-class subsystem of StarkStormShinyHunter. It records which shiny species/forms are secured, which targets are actively being hunted, duplicates, provenance, capture ball, game/save origin, and audit metadata.

## Core invariants

1. A shiny is counted only after `SHINY_SECURED`, never merely after detection.
2. A slot is complete only when every configured required form for that slot is represented.
3. Species and National Dex number must agree; mismatches fail closed.
4. Duplicates do not inflate Living Dex completion.
5. A completed slot is automatically removed from active-hunt state.
6. Tracker state must be exportable/importable and recoverable independently of browser local storage.
7. The tracker does not own ROMs, saves or savestates. It stores references/identifiers only.

## UI

The first UI is a static HTML dashboard intended to be visually useful without a backend. It supports:

- National Dex progress through Generation V (1–649 baseline for the current project scope)
- filters by generation, status, game and ball
- search by National Dex number/name
- active-hunt state
- duplicate counts
- capture metadata
- JSON import/export
- local browser persistence

The HTML must remain usable even before automated synchronization is implemented.

## Domain model

`ShinyLivingDexTracker` is the canonical application-domain model. The HTML is a presentation layer and must eventually consume/export the same schema rather than become an independent source of truth.

### Specimen fields

- National Dex number
- species
- form
- game
- save identifier
- ball
- method
- capture date
- location
- optional gender/nature/PID
- notes

## Event integration

### `SHINY_FOUND`

Does **not** increment completion. May mark the target as `hunting`/`pending_capture` in a future event projection.

### `SHINY_SECURED`

Registers the specimen and recomputes:

- completed slots
- missing slots/forms
- duplicates
- completion ratio
- most recent capture

### Rollback or invalid save

If post-capture validation fails, no permanent tracker mutation may be committed until save integrity is restored and revalidated.

## Forms policy

Living Dex requirements must be data-driven. Different modes may be supported later:

- `species_only` — one shiny per National Dex species
- `forms_required` — configured distinct forms count as independent completion requirements
- `gender_forms` — configured gender differences may count separately
- `full_variant` — future comprehensive mode

The current engine supports configurable required forms while defaulting to one `default` form per species.

## Source of truth and persistence

- GitHub: code, schema, tests and static HTML UI
- Drive: product/UX decisions, project documentation and exported reports if needed
- Runtime: tracker datastore/JSON, backed up independently

Browser `localStorage` is a convenience cache only, not the final authoritative persistence layer.

## Next integration steps

1. Define versioned JSON schema shared by Python and HTML.
2. Seed canonical species metadata for Gen I–V without relying on network availability at runtime.
3. Project `SHINY_SECURED` events into tracker state.
4. Add route-planner integration so completed targets are skipped and missing targets can be prioritized.
5. Add Discord summary notification after each secured shiny.
6. Add backup/reconciliation command to rebuild tracker state from capture audit events.
