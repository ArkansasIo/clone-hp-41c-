# Contributing to Nonpareil

Nonpareil is a legacy microcode-level calculator simulator. Keep changes incremental and preserve the historical simulator's architecture unless a change explicitly proposes a migration.

## Before changing code

1. Read [README](README), [INSTALL](INSTALL), [COPYING](COPYING), and the applicable notices under [LICENSES](LICENSES).
2. Identify the target calculator family and inspect its processor implementation, NCD definition, KML UI, and SCons build rules.
3. Do not replace ROM images, microcode, or model-specific resources with invented data. Record provenance and licensing for any new resources.
4. Keep changes compatible with the existing C code and SCons toolchain unless the change explicitly updates the supported toolchain.

## Build and test

The historically supported build is SCons. See [INSTALL](INSTALL) for dependencies and configuration.

```sh
scons -h
scons
```

The repository-integrity checks added under `tests/` use Python's standard library and do not require GTK or a compiler:

```sh
python3 -m unittest discover -s tests -v
```

These checks verify repository structure and selected build inputs; they are not a substitute for compiling the simulator or testing calculator behavior.

## Change requirements

- Keep patches focused and explain user-visible behavior.
- Add regression tests when fixing a reproducible bug.
- Update documentation and TODO entries when scope or support changes.
- Do not commit generated build output, personal configuration, credentials, or copyrighted ROMs without documented permission.
- Preserve existing copyright and license notices. Different files in this repository may have different licenses; do not assume one license applies to everything.

## Pull requests

Include the target calculator model/family, rationale, verification commands and results, known limitations, and any licensing/provenance details for added assets.
