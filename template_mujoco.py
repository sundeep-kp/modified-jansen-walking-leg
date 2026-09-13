import mujoco
import mujoco.viewer
import time
from pathlib import Path

xml_path = Path(__file__).parent / "modified_jansen_leg.xml"

model = mujoco.MjModel.from_xml_path(str(xml_path))
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)
