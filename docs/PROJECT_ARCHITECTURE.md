# Project Architecture and Module Map

## Purpose

Nonpareil is a microcode-level simulator for historical Hewlett-Packard calculator families. It includes simulator code, calculator descriptions and user-interface definitions, microcode sources/objects, sound resources, and build tooling. It is not a generic modern calculator application.

## Existing repository areas

| Path | Responsibility |
| --- | --- |
| `src/` | Simulator, processor-family implementations, application/UI integration, and supporting C code. See `src/SConscript` for the actual build graph. |
| `ncd/` | Calculator definitions and microcode/ROM source assets, organized by model or processor family. SCons rules generate NCD outputs. |
| `nui/` | Keyboard/display layout descriptions (KML) and image resources for calculator interfaces. |
| `dtd/` | XML document type definitions used by supported data formats. |
| `scons/` | Custom SCons builders and rules for assembling microcode, producing calculator definitions, and packaging. |
| `sound/` | Sound resources and their build rules. |
| `win32/` | Windows-specific packaging/installer support. |
| `doc/` | Design diagrams and supporting technical documents. |
| `LICENSES/`, `COPYING`, `CREDITS` | License texts, attribution, and project notices. |

The SCons build scripts are the source of truth for target membership. This table is an orientation aid, not a claim that every calculator target is complete.

## Runtime model

At a high level, the application combines:

1. A processor-family implementation that executes microinstructions.
2. Calculator-specific chip/ROM configuration and state.
3. A model description that selects processor and hardware components.
4. A KML user-interface description and image assets for keyboard/display interaction.
5. Optional peripheral modules such as the HP-41 family printer.
6. A host GUI/event loop and simulator timing.

Classic, Woodstock, Spice, Nut, and Voyager calculators differ in their processor and hardware details. Avoid forcing them into one inaccurate register or instruction model merely to simplify the implementation.

## Data and generated artifacts

- Treat checked-in assembly sources, templates, KML, and other authored definitions as source inputs.
- Treat build outputs under `build/` and generated calculator-definition artifacts as generated unless project history says otherwise.
- Do not infer that an absent ROM dump is safe to recreate. ROM and microcode assets need explicit provenance and license review.
- Keep generated files reproducible from checked-in inputs where the current build system supports it.

## Validation layers

1. **Repository integrity** — required directories, build entry points, licenses, and selected calculator-family inputs exist.
2. **Build validation** — run SCons with the project's actual toolchain and libraries.
3. **Behavioral validation** — smoke-test calculator startup, key input, display updates, state save/restore, and peripheral behavior for the changed model.
4. **Regression validation** — reproduce the original bug and verify the fix across affected models.

The automated repository-integrity workflow does not claim to perform levels 2–4.
