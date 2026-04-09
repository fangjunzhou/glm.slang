from pathlib import Path
import logging
import slangpy as spy
from pyglm import glm

from math_slang import SHADER_PATH as MATH_SHADER_PATH
from math_slang import load_module_from_file as load_math_module_from_file
from math_slang.quaternion import to_slang, from_slang

logger = logging.getLogger(__name__)

TEST_SHADER_PATH = Path(__file__).parent / "slang"

SHADER_PATHS = [
    MATH_SHADER_PATH,
    TEST_SHADER_PATH,
]

device = spy.create_device(
    type=spy.DeviceType.automatic,
    include_paths=SHADER_PATHS,
)

logger.info(f"Device created: {device}")

math_module = load_math_module_from_file(device=device)
test_module = spy.Module.load_from_file(
    device=device,
    path="test_quaternion.slang",
    link=[math_module],
)
logger.info(f"Modules loaded: {math_module}, {test_module}")


# Test conversion between glm.quat and math.quat.quat
def test_conversion():
    q_py = glm.quat(1.0, 2.0, 3.0, 4.0)
    q_slang = test_module.test_conversion(to_slang(q_py))
    q_py_converted = from_slang(q_slang)
    assert q_py == q_py_converted, f"Expected {q_py}, got {q_py_converted}"


# Test cases for quaternion functions
def test_identity():
    q = test_module.test_identity()
    logger.info(f"Identity quaternion: {q}")
