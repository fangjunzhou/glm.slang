# glm.slang

## Overview

GLM math utilities for Slang.

This library brings GLM into Slang workflows and provides conversion helpers between [pyglm](https://github.com/Zuzu-Typ/PyGLM) and Slang data structures.

## Features

glm.slang provides the following features:
- Quaternion math: Build and manipulate quaternions for 3D rotations.
- Conversion helpers: Move values between pyglm and Slang data structures.

### Quaternion Math

Use the `glm.quat` in Slang to build rotations, compose them, and convert them into vector or matrix forms.

```slang
import glm;

// Build a quaternion representing a 90 degree rotation around the Y axis.
glm.quat.quat q = glm.quat.fromAxisAngle(float3(0, 1, 0) * radians(90));
// Rotate a vector using the quaternion.
float3 rotated = glm.quat.rotate(q, float3(1, 0, 0));
// Convert the quaternion to a rotation matrix.
float3x3 rotation = glm.quat.asMat3(q);
```

### Conversion

Use the conversion helpers to move values between pyglm and Slang data structures.

```python
from pyglm import glm
from glm_slang.conversion import to_slang, from_slang

# Convert a glm vector to Slang and back.
v = glm.vec3(1.0, 2.0, 3.0)
v_slang = to_slang(v)
v_glm = from_slang(v_slang)

# Convert a glm quaternion to Slang and back.
q = glm.angleAxis(glm.radians(90.0), glm.vec3(0.0, 1.0, 0.0))
q_slang = to_slang(q)
q_glm = from_slang(q_slang)
```
