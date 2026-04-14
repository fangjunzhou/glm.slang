# Developer Guide

## Project layout

- `libs/`
  - `glm_slang/`
    - `src/glm_slang/` Python package
    - `src/glm_slang/slang/` Slang sources (`glm.slang`, `quaternion.slang`)
    - `src/glm_slang/conversion.py` pyglm to Slang conversions
- `tests/`
  - `glm_slang/`
    - `src/glm_slang_test/` pytest tests and Slang test shaders

## Slang package integration

`glm.slang` is registered as a `SlangPackage` via `GlmSlang` and built by the
`SlangPackageManager` from `spm.slang`. Dependencies are declared via
`dependencies()` and the manager builds packages in topological order while
collecting include paths. See the
[`spm.slang` docs](https://fangjunzhou.github.io/spm.slang/index.html).

Relevant files:

- `libs/glm_slang/src/glm_slang/__init__.py`
- `external/spm.slang/libs/spm_slang/src/spm_slang/package.py`
- `external/spm.slang/libs/spm_slang/src/spm_slang/package_manager.py`

## Adding a new feature

1. Add new Slang code under `libs/glm_slang/src/glm_slang/slang/`.
2. Include it from `glm.slang` so it is part of the module.
3. If you need Python conversions, extend `to_slang`/`from_slang` in
   `libs/glm_slang/src/glm_slang/conversion.py`.
4. Expose any additional Python helpers from the package `__init__.py`.

## Adding tests

1. Add Slang test entry points under
   `tests/glm_slang/src/glm_slang_test/slang/` and include them from
   `glm_test.slang`.
2. Add pytest coverage in `tests/glm_slang/src/glm_slang_test/test_*.py`,
   using `SlangPackageManager` to load the test module and the conversion
   helpers to bridge types.

## Running tests

Run the test suite from the repo root:

`pytest tests/glm_slang`

To run a single test file or test case, pass a path or node id, for example:

- `pytest tests/glm_slang/src/glm_slang_test/test_conversion.py`
- `pytest tests/glm_slang/src/glm_slang_test/test_conversion.py::test_float3`

For more options, see the
[pytest usage docs](https://docs.pytest.org/en/stable/how-to/usage.html).

## Building documentation

Build the docs from the repo root:

`sphinx-build -b html docs docs/_build`

For a clean rebuild, remove the build directory and rebuild with a fresh
environment:

- `rm -rf docs/_build`
- `sphinx-build -b html -E -a docs docs/_build`
