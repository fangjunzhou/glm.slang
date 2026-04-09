from typing import List
from pyglm import glm
import slangpy as spy


def to_slang(q: glm.quat) -> spy.math.float4:
    """Convert a glm.quat to a spy.math.float4 for use in Slang.

    :param q: The quaternion in glm format.
    :return: A spy.math.float4 representing the quaternion in Slang format (x, y, z, w).
    """
    return spy.math.float4(q.x, q.y, q.z, q.w)


def from_slang(q: spy.math.float4) -> glm.quat:
    """Convert a spy.math.float4 representing a quaternion in Slang format to a glm.quat.

    :param q: A spy.math.float4 where (x, y, z) are the vector part and w is the scalar part of the quaternion.
    :return: A glm.quat representing the same quaternion.
    """
    return glm.quat(q.w, q.x, q.y, q.z)
