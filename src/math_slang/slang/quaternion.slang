implementing math;

namespace math.quat {

// Quaternions in math.slang are defined as float4(x, y, z, w).
public typealias quat = float4;

// Returns the identity quaternion (1, 0, 0, 0).
public quat identity() { return quat(0, 0, 0, 1); }

}

