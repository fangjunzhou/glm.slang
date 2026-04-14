# Usage

## Overview

`glm.slang` provides Slang math helpers and Python conversion utilities for
`pyglm` data structures. The Python helpers convert between `pyglm` vectors,
matrices, quaternions and their `slangpy` counterparts, while the Slang module
exposes quaternion math in `glm.quat`.

## Installation

TODO

## Converting `pyglm` values

Use `glm_slang.conversion.to_slang` to convert `pyglm` values to `slangpy`
math types, and `glm_slang.conversion.from_slang` to convert results back.
Matrices are converted between glm's column-major layout and Slang's
row-major layout.

```python
from pyglm import glm
from glm_slang.conversion import to_slang, from_slang

v = glm.vec3(1.0, -2.0, 3.0)
v_slang = to_slang(v)
v_round_trip = from_slang(v_slang)
```

`spy.math.float4` is ambiguous (vector or quaternion). Pass `as_type` when
converting from Slang:

```python
from pyglm import glm
from glm_slang.conversion import from_slang

vec4 = from_slang(v_slang_float4, as_type=glm.vec4)
quat = from_slang(q_slang_float4, as_type=glm.quat)
```

## Slang quaternion math

The Slang module exposes quaternion helpers under `glm.quat` such as
`identity`, `mul`, `conj`, `inv`, `fromAxisAngle`, `asAxisAngle`, `rotate`,
and `asMat3`. Once the package is loaded via `SlangPackageManager`, you can
call these functions through `slangpy` bindings.

```python
from spm_slang.package_manager import SlangPackageManager
from glm_slang import GlmSlang

manager = SlangPackageManager()
module = manager.module_map[GlmSlang.name()]
```

Refer to the API reference for the full conversion surface and quaternion
helpers.
