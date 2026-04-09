from pathlib import Path
import slangpy as spy

SHADER_PATH = Path(__file__).parent / "slang"


def load_module_from_file(device: spy.Device) -> spy.Module:
    module = spy.Module.load_from_file(
        device=device,
        path=str(SHADER_PATH / "math.slang"),
    )
    return module
