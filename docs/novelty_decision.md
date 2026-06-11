# Novelty Decision

## Decision

Proceed with a paper titled **Precontact Cue Control: Latency-Aware Guards for Switching Grasp Strategy Before Touch**.

## Thesis

In manipulation tasks where a hidden local contact condition determines the safe grasp strategy, the first tactile contact is often too late to decide. A precontact cue should be used as a latency-aware hybrid guard: switch only when the cue is informative enough and arrives far enough before contact for the new strategy to become active.

## Why This Is The Strongest Direction

- It changes which mechanism is central: the paper is about guard placement and activation deadlines, not bigger perception or more data.
- It yields a falsifiable formal condition: if switch distance exceeds remaining distance, contact-reactive strategies incur unavoidable late-mode failures.
- It creates evidence that existing success metrics hide: first-contact impulse and late-switch probability.
- It has a clean hostile boundary against pre-touch sensing and tactile feedback papers.

## Rejected Directions

- Bigger visuotactile models: too close to better data/model capacity.
- New benchmark only: forbidden unless paired with a new mechanism.
- Generic uncertainty-aware switching: too broad and already covered by active perception/control literature.
- Reinforcement learning policy: could learn the behavior but would obscure the physical timing claim.

## Closest Prior Work To Beat

- Multifunctional Tactile Feedbacks Towards Compliant Robot Manipulations via 3D-Shaped Electronic Skin (2022): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Toward a New Generation of Electrically Controllable Hygromorphic Soft Actuators (2015): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- A robust tactile sensor matrix for intelligent grasping of objects using robotic grippers (2021): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control (2026): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Multi-Modal Sensor for Fingertips of Anthropomorphic Grippers (2024): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- MagicGripper: A Mini-MagicTac Integrated Gripper Enabling Multimodal Perception in Contact-Rich Manipulation (2025): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Development of Intelligent Robot Hand Using Proximity, Contact and Slip Sensing (2010): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Implementing tactile behaviors using FingerVision (2017): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Soft-smart robotic end effectors with sensing, actuation, and gripping capabilities (2019): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Experimental Evaluation of Tactile Sensors for Compliant Robotic Hands (2021): Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
