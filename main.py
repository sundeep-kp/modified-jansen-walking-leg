import time
from collections import deque

import mujoco
import mujoco.viewer
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Load MuJoCo model
# ============================================================

model = mujoco.MjModel.from_xml_path("scene.xml")
data = mujoco.MjData(model)

ground_id = model.geom("floor").id


# ============================================================
# Live plot configuration
# ============================================================

plt.ion()

fig, ax = plt.subplots()

line, = ax.plot([], [], label="Total contact force")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Force (N)")
ax.set_title("Foot-Ground Contact Force")
ax.grid()
ax.legend()

# Keep only this much history
window = 5.0

times = deque()
forces = deque()

# Update plot at 30 Hz instead of every physics step
plot_interval = 1.0 / 30.0
last_plot_update = 0.0


# ============================================================
# Run simulation
# ============================================================

with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():

        step_start = time.time()

        # ----------------------------------------------------
        # Physics step
        # ----------------------------------------------------

        mujoco.mj_step(model, data)


        # ----------------------------------------------------
        # Calculate total foot-ground contact force
        # ----------------------------------------------------

        total_force = np.zeros(3)

        for i in range(data.ncon):

            contact = data.contact[i]

            # Check whether this contact involves the ground
            if (
                contact.geom[0] == ground_id
                or contact.geom[1] == ground_id
            ):

                wrench = np.zeros(6)

                mujoco.mj_contactForce(
                    model,
                    data,
                    i,
                    wrench
                )

                # Contact frame -> world frame
                R = contact.frame.reshape(3, 3)

                force_world = R.T @ wrench[:3]

                total_force += force_world


        # ----------------------------------------------------
        # Store total force magnitude
        # ----------------------------------------------------

        force_magnitude = np.linalg.norm(total_force)

        times.append(data.time)
        forces.append(force_magnitude)


        # ----------------------------------------------------
        # Remove old data
        # ----------------------------------------------------

        while times and times[0] < data.time - window:

            times.popleft()
            forces.popleft()


        # ----------------------------------------------------
        # Update plot ~30 times/sec
        # ----------------------------------------------------

        if data.time - last_plot_update >= plot_interval:

            line.set_data(times, forces)

            # X-axis follows the rolling time window
            xmin = max(0.0, data.time - window)
            xmax = max(window, data.time)

            ax.set_xlim(xmin, xmax)


            # Y-axis automatically follows force
            if forces:

                ymax = max(forces)

                if ymax > 0:
                    ax.set_ylim(0, ymax * 1.1)
                else:
                    ax.set_ylim(0, 1)


            fig.canvas.draw_idle()
            fig.canvas.flush_events()

            last_plot_update = data.time


        # ----------------------------------------------------
        # Synchronize MuJoCo viewer
        # ----------------------------------------------------

        viewer.sync()


        # ----------------------------------------------------
        # Run simulation in real time
        # ----------------------------------------------------

        elapsed = time.time() - step_start

        remaining = model.opt.timestep - elapsed

        if remaining > 0:
            time.sleep(remaining)


# ============================================================
# Keep plot open after simulation ends
# ============================================================

plt.ioff()
plt.show()