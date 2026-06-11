# Literature Map

## Scope

- Landscape sweep: 1000 ranked entries written to `docs/related_work_matrix.csv`.
- Serious skim: top 300 entries written to `docs/serious_skim_300.csv`.
- Deep read set: top 230 entries written to `docs/deep_read_230.csv`.
- Hostile prior-work set: top 100 entries written to `docs/hostile_prior_work.csv` and summarized in `docs/hostile_prior_work.md`.
- Year range in matrix: 1985-2026; median citation count: 34.0.

The sweep is centered on robot manipulation, tactile sensing, pre-touch/proximity sensing, grasp strategy selection, and contact-rich control. The extraction is metadata/abstract based unless a source provided more detail through its scholarly record; the paper claims are therefore restricted to mechanisms visible from those records and to the runnable evidence in this repository.

## Field Box

The field box is robot manipulation under partial precontact state: a robot hand approaches an object whose local geometry, material, compliance, or friction may require a different discrete grasp/contact strategy than the nominal one. The contested decision is not only what the robot believes, but when the belief must become an active controller mode before first contact.

## High-Pressure Clusters

- `tactile manipulation`: 263 entries. Examples: Development of Intelligent Robot Hand Using Proximity, Contact and Slip Sensing; Implementing tactile behaviors using FingerVision; Soft-smart robotic end effectors with sensing, actuation, and gripping capabilities.
- `pretouch proximity`: 239 entries. Examples: Multi-Modal Sensor for Fingertips of Anthropomorphic Grippers; Adding Proximity Sensing Capability to Tactile Array Based on Off-the-Shelf FSR and PSoC; Grasp Motion Planning by Non-contact Groping based on Proximity Sensors on Robot Fingertips.
- `tactile grasping`: 231 entries. Examples: Multifunctional Tactile Feedbacks Towards Compliant Robot Manipulations via 3D-Shaped Electronic Skin; Experimental Evaluation of Tactile Sensors for Compliant Robotic Hands; A Novel Tactile Sensor with Electromagnetic Induction and Its Application on Stick-Slip Interaction Detection.
- `proximity sensing`: 120 entries. Examples: Toward a New Generation of Electrically Controllable Hygromorphic Soft Actuators; A robust tactile sensor matrix for intelligent grasping of objects using robotic grippers; MagicGripper: A Mini-MagicTac Integrated Gripper Enabling Multimodal Perception in Contact-Rich Manipulation.
- `contact-rich control`: 52 entries. Examples: Sim-to-Real Transfer for Robotic Manipulation with Tactile Sensory; Improved Learning of Robot Manipulation Tasks Via Tactile Intrinsic Motivation; Minsight: A Fingertip‐Sized Vision‐Based Tactile Sensor for Robotic Manipulation.
- `visuotactile manipulation`: 44 entries. Examples: Cable manipulation with a tactile-reactive gripper; E-Skin: From Humanoids to Humans [Point of View]; TacRot: A Parallel-Jaw Gripper with Rotatable Tactile Sensors for In-Hand Manipulation.
- `hybrid force control`: 30 entries. Examples: Development of Sensory-Motor Fusion-Based Manipulation and Grasping Control for a Robotic Hand-Eye System; Robot-assisted Tactile Sensing for Minimally Invasive Tumor Localization; A Sensor-Based Dual-Arm Tele-Robotic System.
- `precontact grasping`: 21 entries. Examples: A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control; An AI‐Enabled All‐In‐One Visual, Proximity, and Tactile Perception Multimodal Sensor; Gentle Grasping: A Method With Low-Cost Magnetic Tactile Sensors.

## Mechanism Clusters

- `tactile`: 845 entries.
- `grasp_planning`: 628 entries.
- `vision`: 550 entries.
- `precontact`: 401 entries.
- `reactive`: 304 entries.
- `learning`: 298 entries.
- `deformable`: 272 entries.
- `slip`: 202 entries.
- `contact_control`: 182 entries.
- `dexterous`: 154 entries.

## Hidden Assumptions That May Be False

1. First contact is an acceptable time to decide the manipulation mode.
2. Discrete strategy switching latency is negligible relative to the approach time.
3. The preshape or grasp family can be corrected after tactile evidence arrives.
4. Precontact signals are perception features, not control guard conditions.
5. The cost of an exploratory touch is small enough to ignore.
6. Contact force transients do not change the feasible strategy set.
7. Object pose, compliance, friction, and local geometry stay fixed while the hand approaches.
8. The robot can recover from a bad initial contact without irreversible slip or damage.
9. A single nominal approach speed is safe across hidden contact modes.
10. Tactile classification accuracy is the bottleneck, not decision timing.
11. Vision or depth provides enough state before contact for selecting the grasp family.
12. A planner can commit to a grasp and leave contact handling to a low-level controller.
13. Failure labels after contact are sufficient supervision for precontact policy design.
14. The same end-effector compliance is appropriate before and after contact.
15. The surface cue distribution is stationary across lighting, material, and distance.
16. Cue confidence can be thresholded without accounting for remaining stopping distance.
17. Proximity and tactile pipelines can be evaluated independently from mode-switch dynamics.
18. A missed precontact cue only delays perception rather than changing the contact event.
19. Hybrid guards should be placed at contact boundaries rather than before them.
20. Benchmark success/failure metrics capture harmful first-contact impulses.
21. The controller's discrete mode is less important than the continuous force trajectory.
22. Grasp strategy is a label predicted once, rather than a contract that must become active before contact.
23. Manipulation policies can ignore the asymmetric cost of false early switches versus late switches.
24. Precontact information is too weak to justify changing the central control mechanism.

## Candidate Directions That Break Assumptions

| Direction | Broken assumptions | Central mechanism | Why it might be strong | Main novelty risk |
| --- | --- | --- | --- | --- |
| Precontact guard contracts | contact is a valid decision boundary; switching latency is negligible | distance-aware hybrid guard that commits a grasp strategy before contact only when the cue has enough lead distance | makes timing, not recognition accuracy, the main mechanism | proximity-sensing papers may already use pre-touch features; must show they do not treat cue lead distance as the control guard |
| Latency-indexed tactile fallback | tactile correction is fast enough | post-contact controller explicitly declares states unrecoverable when latency exceeds impulse budget | clarifies when tactile feedback cannot help | could be viewed as analysis rather than a new method |
| Approach-speed shaping from cue entropy | approach speed is fixed | slow/stop/commit policy coupled to cue entropy and switch distance | converts weak cues into time for strategy selection | may look like generic uncertainty-aware control unless guard is central |
| First-contact impulse benchmark | success metrics capture harmful first contact | metric exposes pre-failure impulse before final grasp success | useful for evaluation | benchmark-only contribution is forbidden without a new mechanism |

## Selected Direction

The strongest direction is **precontact guard contracts**: use precontact cue arrival as a hybrid-control guard whose decision threshold depends on remaining distance, switching latency, and asymmetric costs of early versus late strategy changes. This changes the central mechanism from better tactile/perceptual classification to a latency-aware guard that makes the strategy active before first contact.

## Representative Hostile Papers

| Rank | Year | Title | Venue | Less novel | Leaves open |
| --- | --- | --- | --- | --- | --- |
| 1 | 2022 | Multifunctional Tactile Feedbacks Towards Compliant Robot Manipulations via 3D-Shaped Electronic Skin | IEEE Sensors Journal | precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached |
| 2 | 2015 | Toward a New Generation of Electrically Controllable Hygromorphic Soft Actuators | Advanced Materials | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 3 | 2021 | A robust tactile sensor matrix for intelligent grasping of objects using robotic grippers |  | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 4 | 2026 | A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control | Discover Mechanical Engineering | precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached |
| 5 | 2024 | Multi-Modal Sensor for Fingertips of Anthropomorphic Grippers |  | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 6 | 2025 | MagicGripper: A Mini-MagicTac Integrated Gripper Enabling Multimodal Perception in Contact-Rich Manipulation | IEEE Transactions on Automation Science and Engineering | precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached |
| 7 | 2010 | Development of Intelligent Robot Hand Using Proximity, Contact and Slip Sensing | Transactions of the Society of Instrument and Control Engineers | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 8 | 2017 | Implementing tactile behaviors using FingerVision |  | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 9 | 2019 | Soft-smart robotic end effectors with sensing, actuation, and gripping capabilities | Smart Materials and Structures | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 10 | 2021 | Experimental Evaluation of Tactile Sensors for Compliant Robotic Hands | Frontiers in Robotics and AI | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 11 | 2019 | Adding Proximity Sensing Capability to Tactile Array Based on Off-the-Shelf FSR and PSoC | IEEE Transactions on Instrumentation and Measurement | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 12 | 2015 | Force and proximity fingertip sensor to enhance grasping perception |  | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 13 | 1999 | A Dexterous Gripper for Space Robotics | Virtual Community of Pathological Anatomy (University of Castilla La Mancha) | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 14 | 2022 | A Sensory Soft Robotic Gripper Capable of Learning-Based Object Recognition and Force-Controlled Grasping | IEEE Transactions on Automation Science and Engineering | using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached |
| 15 | 2020 | Blocks World of Touch: Exploiting the Advantages of All-Around Finger Sensing in Robot Grasping | Frontiers in Robotics and AI | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 16 | 2016 | Fingertip proximity sensor with realtime visual-based calibration |  | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 17 | 2014 | Shape Deposition Manufacturing of a Soft, Atraumatic, Deployable Surgical Grasper1 | Journal of Medical Devices | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 18 | 2016 | A Novel Tactile Sensor with Electromagnetic Induction and Its Application on Stick-Slip Interaction Detection | Sensors | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 19 | 2017 | Grasp Motion Planning by Non-contact Groping based on Proximity Sensors on Robot Fingertips | Journal of the Robotics Society of Japan | precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
| 20 | 2020 | Teleoperation with Tactile Feedback based on a Capacitive Proximity Sensor Array |  | precontact/proximity sensing itself; using tactile feedback for grasp stability | where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible |
