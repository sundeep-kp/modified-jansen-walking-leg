Full document here-- https://docs.google.com/document/d/1wQWvOZNvA1PLT6YzGUdqtGpzAtf10ug7fWzOEEy77QI/

preview (does not include assets for now, refer above document as recommended):

# Modified Jansen Walking Mechanism Report

![alt text](<demo/Screencast from 2026-09-18 23-34-17.gif>)

## Abstract
Theo Jansen's linkage is a well-known single-degree-of-freedom, eight-bar planar mechanism that converts rotary input into a leg-like walking trajectory. The objective of this project was to reduce the visual and part-count complexity of the standard Jansen leg — consolidating links where they do not affect the underlying kinematics — while keeping the mechanism at one degree of freedom and retaining a Jansen-like foot trajectory that closely matched human gait.

The design was carried out in SolidWorks, using its Motion Study add-in to verify the trajectory and animate the assembled mechanism, and later reconstructed in MuJoCo to evaluate contact dynamics and inform a physical build.

This reduced mechanism is a compact re-interpretation of the standard Jansen leg, in which several links were merged or removed for compactness without altering the underlying kinematic behaviour.

## 1. Introduction

Theo Jansen's linkage is a well-known single-degree-of-freedom, eight-bar planar mechanism that converts rotary input into a leg-like walking trajectory. The objective of this project was to reduce the visual and part-count complexity of the standard Jansen leg — consolidating links where they do not affect the underlying kinematics — while keeping the mechanism at one degree of freedom and retaining a Jansen-like foot trajectory that closely matched human gait. The design was carried out in SolidWorks, using its Motion Study add-in to verify the trajectory and animate the assembled mechanism, and later reconstructed in MuJoCo to evaluate contact dynamics and inform a physical build.

## 2. Mechanism Overview

The design is a reduced re-interpretation of the standard Jansen leg (Fig. 1), in which several links were merged or removed for compactness without altering the underlying kinematic behaviour.

Figure 1. The reduced mechanism (left) alongside the reference eight-bar Jansen linkage it is derived from (right).

### 2.1 Topology Reduction

The bottom horizontal link was removed and the two lower-left links were straightened into a single rigid link.

The upper-right horizontal link and the middle-right link were removed and replaced with one rigid bent link (shown in yellow in Fig. 3), which is a compaction choice rather than a kinematic change.

Ignoring the foot and the outermost link that drives it, the crank disk becomes the effective ground-mounted driver.

Figure 2. Before (left) and after (right) consolidating the lower-leg links into a single rigid member.

This reduction is visual rather than kinematic: the point where the lower right link meets the ternary (triangular) link is still pinned to the ground in the underlying sketch, even though this is not obvious from the solid geometry alone. The mechanism therefore reduces, functionally, to the same four-bar linkage present in the upper-right portion of the standard Jansen leg.

### 2.2 The Driving Four-Bar Subsystem

Colour-coding the assembly makes the reduction explicit (Fig. 3): the crank disk (black) rotates about the fixed ground pivot, driving the coupler link (blue), which in turn drives the ternary link (red). The ternary link is itself pinned to ground at a second, fixed point — completing the crank-rocker four-bar. The bent link (yellow) is an output link riding on the ternary link, carrying motion down to the lower leg (grey).

Figure 3. Colour-coded four-bar subsystem — crank (black), coupler (blue), ternary/rocker link (red), and the output bent link (yellow).

## 3. Methodology

The mechanism was built up incrementally in SolidWorks, verifying at each stage that the added constraints produced the intended single-degree-of-freedom behaviour before proceeding.

### 3.1 Ground Link and Ternary Link Placement

A disk was used as the ground link. One corner of the ternary link was pinned to this ground link at a separation of 15.8 mm (Fig. 4). The ternary link was chosen as the member fixed to ground because it plays the same structural role as the corresponding rocker link in the upper four-bar of the standard Jansen leg (Section 2.2); the 15.8 mm separation itself was arrived at empirically, by sweeping the dimension and observing its effect on the foot trajectory — this trade-off is examined in Section 4.2.

Figure 4. Ternary link sketch showing the fixed-pivot separation and hole geometry.

### 3.2 Crank–Coupler Assembly

A second disk was added as the crank, driven by a protruding input shaft, and connected to the ternary link through a coupler link (Fig. 5). This sub-assembly is a crank-rocker four-bar mechanism [1], with the crank providing continuous rotary input and the ternary link rocking in response.

Figure 5. Crank–coupler–ternary link four-bar sub-assembly.

### 3.3 Constraining the Lower Leg

With only the four-bar and the lower leg links connected, the assembly was under-constrained: each crank angle admitted multiple valid positions for the lower leg. An additional bent link, dimensioned as shown in Fig. 6 (9.86 mm and 12.83 mm segments at 139.31°), was introduced to remove this ambiguity and fully constrain the leg to a single configuration per input angle. The remaining sketch dimensions for this stage of the assembly are given in Fig. 7.

Figure 6. Bent-link geometry added to remove the residual assembly ambiguity.

Figure 7. Fully dimensioned four-bar and lower-leg sketch after the additional constraint was applied.

### 3.4 Leg Assembly, Mirroring, and Coupling

The completed leg was assembled and mirrored using SolidWorks' “create opposite hand components” option, and the mirrored files were saved and reassembled independently. Both legs were then joined by a connecting link (highlighted in blue in Fig. 8), which mechanically couples them to a single common input — keeping the overall mechanism at one degree of freedom while the two legs remain permanently offset by a phase difference. This offset was set experimentally (matching the legs at their extremum positions) to give a more natural walking gait.

Figure 8. Both legs coupled through a common connecting link (blue), sharing a single driven input.

### 3.5 Padding and Animation

Foot padding was added to each leg, and the assembly was driven with a simple rotary motor input in a SolidWorks Motion Study to animate the complete walking cycle (see Fig. 10, Section 5).

## 4. Kinematic Analysis

The modified mechanism retains several dimensional characteristics of the conventional Jansen linkage. Table 1 compares the measured link dimensions of this design against the closest corresponding dimensions of the standard Jansen linkage.

Table 1. Measured link dimensions versus standard Jansen proportions.

| Mechanism feature | Measured value (mm) | Closest Jansen value (mm) | Difference |
| --- | ---: | ---: | ---: |
| Upper crank / ternary-link connection | 23.24 | 15.0 | +54.9% |
| Upper fixed-pivot separation | 24.19 | 15.0 | +61.3% |
| Upper (major) coupler link | 44.02 | 41.5 | +6.1% |
| Major lower-leg link | 37.92 | 38.0 | −0.2% |
| Short lower connector | 14.58 | 15.0 | −2.8% |
| Small connector | 7.39 | 7.8 | −5.3% |
| Bent-link segment (short arm) | 9.86 | 7.8 | +26.4% |
| Bent-link segment (long arm) | 12.83 | 15.0 | −14.5% |
| Long lower-leg dimension | 61.08 | 61.9 | −1.3% |
| Upper positional dimension | 13.00 | 15.0 | −13.3% |
| Component offset | 43.17 | 41.5 | +4.0% |

The lower-leg dimensions (37.92 mm, 14.58 mm, 61.08 mm) track the standard Jansen values (38 mm, 15 mm, 61.9 mm) closely, to within about 3%. The upper four-bar dimensions, by contrast, deviate substantially — in places by more than 50% — reflecting the deliberate re-proportioning of this stage to accommodate the reduced topology and a more compact envelope.

### 4.1 Foot Trajectory

The traced path of a point at the centre of the foot's bottom face (Fig. 9) depends on both the input crank angle and the link dimensions and separations described above. To evaluate how human-like the resulting gait is, the traced path is compared directly against a reference human walking trajectory [7] and against the standard Jansen trajectory [6].

Figure 9a. Traced trajectory of the foot contact point of this mechanism, over one input revolution. (mirrored during simulation)

Figure 9b. Reference human walker gait trajectory [7].

Figure 9c. Reference standard Jansen mechanism gait trajectory [6].

### 4.2 Effect of the 15.8 mm Pivot Separation

The separation between the ground pivot and the ternary link (Section 3.1) was found to directly shape the trajectory:

- At 15.8 mm, the trajectory is somewhat front-heavy.
- Increasing the separation moves the path closer to the stretched-D shape of the standard Jansen trajectory.
- Increasing it further makes the trajectory back-heavy.
- Decreasing it too far causes the four-bar to lose continuous rotary motion — consistent with the mechanism moving out of a Grashof-satisfying link proportion, though this was not formally verified against Grashof's condition in this iteration.

The final value of 15.8 mm was retained because it produces a trajectory whose apex sits slightly forward of centre, relative to the standard Jansen path. This was a deliberate design choice, motivated by three considerations: it mimics human stride, where the apex of foot motion typically sits ahead of the body rather than at its midpoint; it reduces the stride length, improving stability and reliability; and it produces a smoother displacement curve, with a more gradual transition from the rising to the falling phase of the stride.

### 4.3 Results

The completed assembly was driven with a simple rotary motor input and animated in SolidWorks Motion Study (Fig. 10), confirming that the coupled two-leg mechanism produces continuous, single-DOF walking motion with the intended phase offset between legs.

Figure 10. Animated mechanism during a Motion Study walking-cycle simulation.

![Animated mechanism during Motion Study](Screencast%20from%202026-09-12%2021-03-46.gif)

Simulation video: https://youtu.be/PFEDmKlTlRk?si=vWkerZGaBaEz1gjp

## 5. Simulation

To evaluate contact dynamics that are not readily accessible in the SolidWorks Motion Study — in particular, foot–ground contact forces through a compliant shoe — the mechanism was reconstructed as a physics simulation in MuJoCo.

### 5.1 Link Naming and Digitised Geometry

Before reconstructing the mechanism outside SolidWorks, every link and joint was given a consistent name, and every relevant dimension was measured directly from the CAD model. This naming convention (Fig. 11) was used throughout the MuJoCo model and its XML description.

Figure 11. Link and joint naming convention used for the MuJoCo reconstruction.

The corresponding measured dimensions are summarised in Table 2, with the upper ternary link's sketch dimensions shown as a representative example in Fig. 12. The foot outline was digitised as a series of edge lengths in the same way — Fig. 13 shows one representative measurement — in order to reproduce the exact collision geometry of the physical foot in simulation.

Table 2. Named-link dimensions used for the MuJoCo reconstruction.

| Named link | Feature | Value |
| --- | --- | --- |
| Upper ternary link | joint_3–joint_4 | 21.00 mm |
| Upper ternary link | joint_4–joint_5 | 12.00 mm |
| Upper ternary link | joint_3–joint_5 | 24.19 mm |
| Upper ternary link | Enclosed area / perimeter | 146.87 mm² / 53.41 mm |
| Straight link (upper ternary → lower ternary) | Length | 15.80 mm |
| Bent link (upper ternary → lower ternary) | Segments / angle | see Fig. 6–7 |
| Lower ternary link | Long edge | 37.72 mm |
| Lower ternary link | Offset / short edge | 2.50 mm |
| Lower ternary link | Included angle | 153.74° |
| Lower ternary link | Third edge | 11.33 mm |
| Foot link | Main structural dims | 13.00 mm, 61.08 mm (R1.00 fillet) |
| Foot link | Digitised outline segments | 14.69, 22.66, 25.48, 2.3, 20.7, 15.33, 7.28, 3.12 mm |

Figure 12. Upper ternary link sketch dimensions (joint_3–joint_4–joint_5), representative of the dimensioning pass summarised in Table 2.

Figure 13. Representative foot-outline edge measurement; the full outline was digitised edge-by-edge in the same way for the simulation collision mesh.

### 5.2 MJCF Reconstruction and Closing Kinematic Loops

The mechanism was recreated by importing meshes extracted from the SolidWorks assembly, one link at a time, into the MuJoCo viewer using the native MJCF format. A closed-loop four-bar linkage example [8] was used as a reference for handling kinematic loops in MuJoCo, since MJCF natively describes open kinematic trees.

A joint was defined for each parent–child link pair. To close the two kinematic loops (the driving four-bar, and the lower-leg loop), equality constraints were used to connect pairs of defined sites — specifically, coincident points on the “straight link” and “base link” bodies that should stay joined during motion.

Figure 14. Initial four-bar sub-mechanism reconstructed in the MuJoCo viewer.

Initially, the constrained bodies did not feel rigidly connected — instead behaving as though attracted like magnets rather than pinned together. Investigating further, this was traced to MuJoCo's equality constraints being soft constraints by default: the solver finds constraint forces parameterised by impedance, stiffness (k), and damping (b), and the solref parameter controls the reference acceleration — i.e. how quickly the constraint tries to correct a violation. Tuning these parameters resolved the apparent “magnetic” behaviour and produced a properly closed kinematic loop.

Figure 15. Equality-constrained sites (labelled) closing the four-bar kinematic loop.

Figure 16. Full single-leg mechanism (“klann_leg”) reconstructed and closed in MuJoCo.

Figure 17. Iterating on the MJCF description (modified_jansen_leg.xml) alongside the live MuJoCo viewer.

### 5.3 Deformable Shoe and Contact Physics

To estimate realistic foot–ground contact behaviour, a deformable shoe body was added at the foot link, modelled as a soft body rather than a rigid one.

Attempt 1: with a low number of mesh nodes, the deformable body was unstable and produced unreliable contact behaviour.

Increasing the node count produced stable results; the overall system was then scaled to match adult foot dimensions.

With most of the system stable, the deformable shoe began passing through the floor plane under load.

Figure 18. Early instability: the deformable shoe penetrating through the floor plane.

This penetration was resolved by tuning the shoe's approximate material properties and the solver's contact-correction behaviour, referring to MuJoCo's contact-physics documentation [9] for the relevant parameters:

```text
young = "8e4"          (Young's modulus, lowered for visualisation purposes)
damping = "0.001"
poisson = "0.2"
solref = "0.003 1"    (controls how quickly the constraint corrects penetration)
solimp = ".95 .99 .0001"
```

The width of the floor plane was also increased to prevent contact “bleeding” under a high node count, following a known issue reported against MuJoCo on GitHub.

Figure 19. Deformable shoe resting stably on the floor plane after parameter tuning.

Figure 20. Shoe visually attached to the foot link of the reconstructed mechanism.

### 5.4 Simulated Contact Loading

With the geometry and contact model in place, the link dimensions and masses were finalised, assuming the links to be aluminium, the shoe to be the mass of a standard adult male shoe (~300 g), and the drive motor's weight to initially be that of a standard 1.7 N motor. Figure 21 shows the theoretical contact force at the FSR location under the base of the big toe, over one walking cycle, at an input torque of 0.08 N·m.

Figure 21. Theoretical contact force at the big-toe FSR location over one walking cycle, at 0.08 N·m input torque.

## 6. Proposed Hardware

Based on the simulated loading in Section 6.4, the following hardware was proposed for a physical build of the mechanism.

### 6.1 Proposed Components

- 12 V OG555 geared motor with encoder — crank drive.
- ESP32 — main microcontroller.
- BTS7960 (or equivalent high-power H-bridge capable of handling the 12 V motor).
- AS5600 — for measuring foot orientation at a given time.
- MPU6050 — standard IMU used for acceleration measurement in this class of project.
- Adafruit Alpha MF01A-N-221-A05 force sensor (rated 1–100 N contact force, <1 ms response, with a mature ESP32-compatible library), used at three standard foot contact points: heel, big toe, and little toe. Alternative: load cell + HX711.
- Mean Well LRS-75-12 power supply — 12 V, 6 A adjustable, providing headroom for future add-ons.

### 6.2 Control Architecture

The proposed control loop drives the crank through a speed/position controller on the ESP32, and closes the loop on foot contact and orientation sensing:

```text
+---------------------------+
|          ESP32 MCU         |
|                             |
Desired crank ---->|  Speed / Position Controller|
speed          |             |               |
+-------------+---------------+
| PWM / DIR
v
+--------------+
| BTS7960 /    |
| H-Bridge     |
+------+-------+
|
+------v-------+
| 12 V OG555   |
| Geared Motor |
+------+-------+
|
CRANK
|
+------v-------+
|   LINKAGE    |
+------+-------+
|
FOOT
|
+-------------------+-------------------+
|                   |                   |
Heel FSR           Big-toe FSR        Little-toe FSR
|                   |                   |
+-------------------+-------------------+
|
v
+--------------+
|    ESP32     |
|  Contact     |
|  detection   |
+--------------+
Motor encoder ------------------------------> ESP32
AS5600 --------------------------------------> ESP32
MPU6050 -------------------------------------> ESP32
```

Figure 22. Proposed control architecture: crank speed/position control, closed with foot-contact and orientation sensing.

## 7. Conclusion and Future Work

This project reduced the standard eight-bar Jansen leg to a more compact topology built around a single crank-rocker four-bar, while keeping the mechanism at one degree of freedom and tuning its foot trajectory to sit closer to a human gait than the standard Jansen path. The lower-leg dimensions retained close agreement with the classical Jansen proportions (Section 4), while the upper four-bar was deliberately re-proportioned for the reduced topology and a more compact envelope. Mirroring and coupling the leg into a two-leg, single-input assembly, and animating it in SolidWorks Motion Study, confirmed that the design behaves as intended (Section 5).

The mechanism was then carried substantially further than a CAD exercise: it was reconstructed link-by-link as a physics simulation in MuJoCo, with closed kinematic loops, a deformable contact shoe, and a theoretical contact-force estimate at the big toe (Section 6). That simulated loading, in turn, informed a concrete proposed hardware architecture — drive motor, motor driver, microcontroller, orientation and contact sensing, and power supply — with a defined control loop from desired crank speed through to foot-contact detection (Section 7). Taken together, the project now spans the full path from a first-principles kinematic reduction to a build-ready hardware and control specification.

The most valuable next steps follow directly from where this iteration stopped short:

- Formally verifying the degrees of freedom of the coupled two-leg assembly and the Grashof condition of the driving four-bar using Grübler's equation, rather than relying on the empirical observation in Section 4.2.
- Quantifying the trajectory sweep described in Section 4.2 with a table or plot of pivot separation versus trajectory apex position, instead of the qualitative front-heavy/back-heavy description used here.
- Validating the MuJoCo contact-force estimate (Section 6.4) against the physical prototype once built, and tuning the deformable shoe parameters accordingly.
- Physically fabricating the mechanism and the proposed hardware in Section 7, and closing the control loop on real sensor data rather than simulated values.

## References

- [1] Four bar crank-rocker mechanism demonstration. https://www.youtube.com/watch?v=hrvIBtrDNV0
- [2] Theo Jansen mechanism walking demonstration. https://www.youtube.com/watch?v=clGEbGLUyoQ
- [3] Theo Jansen mechanism build/analysis video. https://www.youtube.com/watch?v=vAEZ4BYAmGE&t=120s
- [4] The Jansen leg: a 1-degree-of-freedom planar linkage of eight links, seven revolute joints. ResearchGate figure. https://www.researchgate.net/figure/The-Jansen-leg-a-1-degree-of-freedom-planar-linkage-of-eight-links-seven-revolute_fig2_277606519
- [5] Educational model of the Theo Jansen mechanism. https://www.printables.com/model/1503557-educational-model-of-theo-jansen-mechanism
- [6] Theo Jansen mechanism reference video. https://www.youtube.com/watch?v=FFuDU1Uiu9k
- [7] Reference human walker gait — acceleration carries the local inversion effect in biological motion perception. https://www.researchgate.net/figure/The-full-gait-trajectory-with-the-10-starting-positions-A-and-the-individual-150-ms_fig1_24187266
- [8] Closed-loop simulation example (four-bar linkage) in MuJoCo, using equality constraints. https://github.com/google-deepmind/mujoco/issues/172
- [9] Reference for deformable-body contact physics parameters used in Section 6.3. https://arxiv.org/html/2411.14701v1



### Project Files

- [modified_jansen_leg.xml](modified_jansen_leg.xml)
- [modified_jansen_leg_adult_male_shoe.xml](modified_jansen_leg_adult_male_shoe.xml)
- [modified_jansen_leg_scaled_4x.xml](modified_jansen_leg_scaled_4x.xml)
- [modified_jansen_leg_visual_shoe.xml](modified_jansen_leg_visual_shoe.xml)
- [reference.xml](reference.xml)
- [template_mujoco.py](template_mujoco.py)

## Appendix: Repository Snapshot

This folder contains the MuJoCo model files, the SolidWorks-derived mesh assets, and the report media used for the walking mechanism design and validation work.
