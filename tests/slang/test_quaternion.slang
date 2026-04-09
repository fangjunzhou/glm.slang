import math;

math.quat.quat test_identity()
{
    return math.quat.identity();
}

math.quat.quat test_mul(math.quat.quat a, math.quat.quat b)
{
    return math.quat.mul(a, b);
}

math.quat.quat test_conj(math.quat.quat q)
{
    return math.quat.conj(q);
}

math.quat.quat test_inv(math.quat.quat q)
{
    return math.quat.inv(q);
}

math.quat.quat test_from_axis_angle(float3 axisAngle)
{
    return math.quat.fromAxisAngle(axisAngle);
}

float3 test_as_axis_angle(math.quat.quat q)
{
    return math.quat.asAxisAngle(q);
}

float3 test_rotate(math.quat.quat q, float3 v)
{
    return math.quat.rotate(q, v);
}

float3x3 test_as_mat3(math.quat.quat q)
{
    return math.quat.asMat3(q);
}
