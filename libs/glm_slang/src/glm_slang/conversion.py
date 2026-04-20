from __future__ import annotations

from typing import overload
from pyglm import glm
import slangpy as spy


@overload
def to_slang(v: glm.vec2) -> spy.math.float2:
    """Convert a glm.vec2 to a spy.math.float2 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.float2 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.vec3) -> spy.math.float3:
    """Convert a glm.vec3 to a spy.math.float3 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.float3 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.vec4) -> spy.math.float4:
    """Convert a glm.vec4 to a spy.math.float4 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.float4 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.mat2) -> spy.math.float2x2:
    """Convert a glm.mat2 to a spy.math.float2x2 for use in Slang.

    :param v: The matrix in glm format.
    :return: A spy.math.float2x2 representing the same matrix in Slang format.
    """
    ...


@overload
def to_slang(v: glm.mat3) -> spy.math.float3x3:
    """Convert a glm.mat3 to a spy.math.float3x3 for use in Slang.

    :param v: The matrix in glm format.
    :return: A spy.math.float3x3 representing the same matrix in Slang format.
    """
    ...


@overload
def to_slang(v: glm.mat4) -> spy.math.float4x4:
    """Convert a glm.mat4 to a spy.math.float4x4 for use in Slang.

    :param v: The matrix in glm format.
    :return: A spy.math.float4x4 representing the same matrix in Slang format.
    """
    ...


@overload
def to_slang(v: glm.quat) -> spy.math.float4:
    """Convert a glm.quat to a spy.math.float4 for use in Slang.

    :param v: The quaternion in glm format.
    :return: A spy.math.float4 representing the quaternion in Slang format (x, y, z, w).
    """
    ...


@overload
def to_slang(v: glm.ivec2) -> spy.math.int2:
    """Convert a glm.ivec2 to a spy.math.int2 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.int2 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.ivec3) -> spy.math.int3:
    """Convert a glm.ivec3 to a spy.math.int3 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.int3 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.ivec4) -> spy.math.int4:
    """Convert a glm.ivec4 to a spy.math.int4 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.int4 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.uvec2) -> spy.math.uint2:
    """Convert a glm.uvec2 to a spy.math.uint2 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.uint2 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.uvec3) -> spy.math.uint3:
    """Convert a glm.uvec3 to a spy.math.uint3 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.uint3 representing the same vector in Slang format.
    """
    ...


@overload
def to_slang(v: glm.uvec4) -> spy.math.uint4:
    """Convert a glm.uvec4 to a spy.math.uint4 for use in Slang.

    :param v: The vector in glm format.
    :return: A spy.math.uint4 representing the same vector in Slang format.
    """
    ...


def to_slang(
    v: glm.vec2
    | glm.vec3
    | glm.vec4
    | glm.mat2
    | glm.mat3
    | glm.mat4
    | glm.quat
    | glm.ivec2
    | glm.ivec3
    | glm.ivec4
    | glm.uvec2
    | glm.uvec3
    | glm.uvec4,
) -> (
    spy.math.float2
    | spy.math.float3
    | spy.math.float4
    | spy.math.float2x2
    | spy.math.float3x3
    | spy.math.float4x4
    | spy.math.int2
    | spy.math.int3
    | spy.math.int4
    | spy.math.uint2
    | spy.math.uint3
    | spy.math.uint4
):
    """Convert supported glm types to their Slang vector equivalents."""
    if isinstance(v, glm.vec2):
        return spy.math.float2(v.x, v.y)
    if isinstance(v, glm.vec3):
        return spy.math.float3(v.x, v.y, v.z)
    if isinstance(v, glm.vec4):
        return spy.math.float4(v.x, v.y, v.z, v.w)
    if isinstance(v, glm.mat2):
        # glm matrices are column-major; Slang matrix literals/indexing are row-major.
        return spy.math.float2x2(
            [
                v[0][0],
                v[1][0],
                v[0][1],
                v[1][1],
            ]
        )
    if isinstance(v, glm.mat3):
        return spy.math.float3x3(
            [
                v[0][0],
                v[1][0],
                v[2][0],
                v[0][1],
                v[1][1],
                v[2][1],
                v[0][2],
                v[1][2],
                v[2][2],
            ]
        )
    if isinstance(v, glm.mat4):
        return spy.math.float4x4(
            [
                v[0][0],
                v[1][0],
                v[2][0],
                v[3][0],
                v[0][1],
                v[1][1],
                v[2][1],
                v[3][1],
                v[0][2],
                v[1][2],
                v[2][2],
                v[3][2],
                v[0][3],
                v[1][3],
                v[2][3],
                v[3][3],
            ]
        )
    if isinstance(v, glm.quat):
        return spy.math.float4(v.x, v.y, v.z, v.w)
    if isinstance(v, glm.ivec2):
        return spy.math.int2(v.x, v.y)
    if isinstance(v, glm.ivec3):
        return spy.math.int3(v.x, v.y, v.z)
    if isinstance(v, glm.ivec4):
        return spy.math.int4(v.x, v.y, v.z, v.w)
    if isinstance(v, glm.uvec2):
        return spy.math.uint2(v.x, v.y)
    if isinstance(v, glm.uvec3):
        return spy.math.uint3(v.x, v.y, v.z)
    if isinstance(v, glm.uvec4):
        return spy.math.uint4(v.x, v.y, v.z, v.w)
    raise TypeError(f"Unsupported type for to_slang: {type(v)!r}")


@overload
def from_slang(v: spy.math.float2) -> glm.vec2:
    """Convert a spy.math.float2 representing a vector in Slang format to a glm.vec2.

    :param v: A spy.math.float2 representing the vector in Slang format.
    :return: A glm.vec2 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.float3) -> glm.vec3:
    """Convert a spy.math.float3 representing a vector in Slang format to a glm.vec3.

    :param v: A spy.math.float3 representing the vector in Slang format.
    :return: A glm.vec3 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.float2x2) -> glm.mat2:
    """Convert a spy.math.float2x2 in Slang format to a glm.mat2.

    :param v: The matrix in Slang format.
    :return: A glm.mat2 representing the same matrix.
    """
    ...


@overload
def from_slang(v: spy.math.float3x3) -> glm.mat3:
    """Convert a spy.math.float3x3 in Slang format to a glm.mat3.

    :param v: The matrix in Slang format.
    :return: A glm.mat3 representing the same matrix.
    """
    ...


@overload
def from_slang(v: spy.math.float4x4) -> glm.mat4:
    """Convert a spy.math.float4x4 in Slang format to a glm.mat4.

    :param v: The matrix in Slang format.
    :return: A glm.mat4 representing the same matrix.
    """
    ...


@overload
def from_slang(v: spy.math.float4, as_type: type[glm.vec4]) -> glm.vec4:
    """Convert a spy.math.float4 representing a vector in Slang format to a glm.vec4.

    :param v: A spy.math.float4 representing the vector in Slang format.
    :param as_type: Pass ``glm.vec4`` to interpret the float4 as a vector.
    :return: A glm.vec4 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.float4, as_type: type[glm.quat] = glm.quat) -> glm.quat:
    """Convert a spy.math.float4 representing a quaternion in Slang format to a glm.quat.

    :param v: A spy.math.float4 where (x, y, z) are the vector part and w is the scalar part of the quaternion.
    :param as_type: Pass ``glm.quat`` (default) to interpret the float4 as a quaternion.
    :return: A glm.quat representing the same quaternion.
    """
    ...


@overload
def from_slang(v: spy.math.int2) -> glm.ivec2:
    """Convert a spy.math.int2 representing a vector in Slang format to a glm.ivec2.

    :param v: A spy.math.int2 representing the vector in Slang format.
    :return: A glm.ivec2 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.int3) -> glm.ivec3:
    """Convert a spy.math.int3 representing a vector in Slang format to a glm.ivec3.

    :param v: A spy.math.int3 representing the vector in Slang format.
    :return: A glm.ivec3 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.int4) -> glm.ivec4:
    """Convert a spy.math.int4 representing a vector in Slang format to a glm.ivec4.

    :param v: A spy.math.int4 representing the vector in Slang format.
    :return: A glm.ivec4 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.uint2) -> glm.uvec2:
    """Convert a spy.math.uint2 representing a vector in Slang format to a glm.uvec2.

    :param v: A spy.math.uint2 representing the vector in Slang format.
    :return: A glm.uvec2 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.uint3) -> glm.uvec3:
    """Convert a spy.math.uint3 representing a vector in Slang format to a glm.uvec3.

    :param v: A spy.math.uint3 representing the vector in Slang format.
    :return: A glm.uvec3 representing the same vector.
    """
    ...


@overload
def from_slang(v: spy.math.uint4) -> glm.uvec4:
    """Convert a spy.math.uint4 representing a vector in Slang format to a glm.uvec4.

    :param v: A spy.math.uint4 representing the vector in Slang format.
    :return: A glm.uvec4 representing the same vector.
    """
    ...


def from_slang(
    v: (
        spy.math.float2
        | spy.math.float3
        | spy.math.float4
        | spy.math.float2x2
        | spy.math.float3x3
        | spy.math.float4x4
        | spy.math.int2
        | spy.math.int3
        | spy.math.int4
        | spy.math.uint2
        | spy.math.uint3
        | spy.math.uint4
    ),
    as_type: type[glm.vec4] | type[glm.quat] | None = None,
) -> (
    glm.vec2
    | glm.vec3
    | glm.vec4
    | glm.quat
    | glm.mat2
    | glm.mat3
    | glm.mat4
    | glm.ivec2
    | glm.ivec3
    | glm.ivec4
    | glm.uvec2
    | glm.uvec3
    | glm.uvec4
):
    """Convert supported Slang vector types to glm types.

    For ``spy.math.float4``, pass ``as_type=glm.vec4`` or ``as_type=glm.quat``
    to disambiguate. If omitted, ``glm.quat`` is used for backward compatibility.
    """
    if isinstance(v, spy.math.float2):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.vec2(v.x, v.y)
    if isinstance(v, spy.math.float3):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.vec3(v.x, v.y, v.z)
    if isinstance(v, spy.math.float2x2):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.mat2(
            v[0][0],
            v[1][0],
            v[0][1],
            v[1][1],
        )
    if isinstance(v, spy.math.float3x3):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.mat3(
            v[0][0],
            v[1][0],
            v[2][0],
            v[0][1],
            v[1][1],
            v[2][1],
            v[0][2],
            v[1][2],
            v[2][2],
        )
    if isinstance(v, spy.math.float4x4):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.mat4(
            v[0][0],
            v[1][0],
            v[2][0],
            v[3][0],
            v[0][1],
            v[1][1],
            v[2][1],
            v[3][1],
            v[0][2],
            v[1][2],
            v[2][2],
            v[3][2],
            v[0][3],
            v[1][3],
            v[2][3],
            v[3][3],
        )
    if isinstance(v, spy.math.float4):
        if as_type is None or as_type is glm.quat:
            # glm.quat constructor order is (w, x, y, z).
            return glm.quat(v.w, v.x, v.y, v.z)
        if as_type is glm.vec4:
            return glm.vec4(v.x, v.y, v.z, v.w)
        raise TypeError(f"Unsupported as_type for from_slang(float4): {as_type!r}")
    if isinstance(v, spy.math.int2):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.ivec2(v.x, v.y)
    if isinstance(v, spy.math.int3):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.ivec3(v.x, v.y, v.z)
    if isinstance(v, spy.math.int4):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.ivec4(v.x, v.y, v.z, v.w)
    if isinstance(v, spy.math.uint2):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.uvec2(v.x, v.y)
    if isinstance(v, spy.math.uint3):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.uvec3(v.x, v.y, v.z)
    if isinstance(v, spy.math.uint4):
        if as_type is not None:
            raise TypeError("as_type is only valid for spy.math.float4 inputs")
        return glm.uvec4(v.x, v.y, v.z, v.w)
    raise TypeError(f"Unsupported type for from_slang: {type(v)!r}")
