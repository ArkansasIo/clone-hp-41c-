# Source Completion and Verification Roadmap

This roadmap separates repository hygiene from emulator feature work. A file being present does not mean the feature is implemented or validated.

## Phase 1 — Reproducible baseline

- Record host OS, compiler, SCons, Flex, Bison, GTK/GLib, libxml2, SDL and image-tool versions.
- Build the unmodified tree and preserve the complete build log.
- Identify warnings and failures separately from missing optional dependencies.
- Run repository-integrity tests and retain results with the commit.

## Phase 2 — Build graph and source inventory

- Review every `SConscript` and map source files to built targets.
- Identify generated versus authored files and document generation commands.
- Audit target coverage against `all_calcs` and the NCD/NUI directories.
- Add explicit tests for broken or stale paths; do not manufacture placeholder ROMs or claim unsupported models work.

## Phase 3 — HP-41C-family fidelity

- Trace the Nut processor execution loop, register/state representation, memory and module-port mapping.
- Verify HP-41C/41CV/41CX configuration, ROM/module loading, keyboard scanning, display rendering and state persistence.
- Add regression tests for module insertion/removal, peripheral recognition, and save/restore.
- Use documented, legally distributable test fixtures; record any differences from physical hardware.

## Phase 4 — Stability and maintainability

- Add automated tests around deterministic, non-GUI processor operations where the current design permits.
- Improve error messages for malformed model definitions and unavailable resources.
- Add sanitizer or static-analysis jobs only after the supported compiler/toolchain is established.
- Keep GUI modernization separate from CPU fidelity changes to make regressions diagnosable.

## Phase 5 — Optional modernization

A port to newer C standards, a different GUI toolkit, or a new build system should be proposed as a separate migration. Preserve a working legacy build until feature parity and model-specific tests demonstrate that the replacement is reliable.

## Current verification status

The repository-integrity tests validate expected source-tree entries and build references. They do not compile the C application, run SCons, or execute calculator microcode. Those checks require a suitable native environment and legacy dependencies.
