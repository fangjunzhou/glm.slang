import glm;

glm.quat.quat test_identity()
{
    return glm.quat.identity();
}

glm.quat.quat test_mul(glm.quat.quat a, glm.quat.quat b)
{
    return glm.quat.mul(a, b);
}

glm.quat.quat test_conj(glm.quat.quat q)
{
    return glm.quat.conj(q);
}

glm.quat.quat test_inv(glm.quat.quat q)
{
    return glm.quat.inv(q);
}

glm.quat.quat test_from_axis_angle(float3 axisAngle)
{
    return glm.quat.fromAxisAngle(axisAngle);
}

float3 test_as_axis_angle(glm.quat.quat q)
{
    return glm.quat.asAxisAngle(q);
}

float3 test_rotate(glm.quat.quat q, float3 v)
{
    return glm.quat.rotate(q, v);
}

float3x3 test_as_mat3(glm.quat.quat q)
{
    return glm.quat.asMat3(q);
}
