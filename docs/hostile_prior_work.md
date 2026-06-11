# Hostile Prior Work

This set intentionally over-includes papers that could make the contribution look incremental: pre-touch/proximity sensing, tactile feedback, grasp selection, contact-rich control, and learned manipulation. Each entry records what it already covers and what it leaves open for a latency-aware precontact guard.

## 1. Multifunctional Tactile Feedbacks Towards Compliant Robot Manipulations via 3D-Shaped Electronic Skin

- Year/venue: 2022; IEEE Sensors Journal
- Authors: Wennan Xiong; Hui Feng; Haosen Liwang; Dan Li; Wanbing Yao; Dilinazha Duolikun; Yunlei Zhou; YongAn Huang
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/jsen.2022.3162914

## 2. Toward a New Generation of Electrically Controllable Hygromorphic Soft Actuators

- Year/venue: 2015; Advanced Materials
- Authors: Silvia Taccola; Francesco Greco; Edoardo Sinibaldi; Alessio Mondini; Barbara Mazzolai; Virgilio Mattoli
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1002/adma.201404772

## 3. A robust tactile sensor matrix for intelligent grasping of objects using robotic grippers

- Year/venue: 2021; 
- Authors: T Prabhu; P. V. Manivannan; Debanik Roy; Yathishkumar
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iria53009.2021.9588669

## 4. A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control

- Year/venue: 2026; Discover Mechanical Engineering
- Authors: Mohammed R. Ahmed; Sadeq H. Bakhy; Ihsan A. Baqer
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1007/s44245-026-00275-y

## 5. Multi-Modal Sensor for Fingertips of Anthropomorphic Grippers

- Year/venue: 2024; 
- Authors: Tanzeel Ahmad Fazal; Gianluca Laudante; Michele Mirto; Olga Pennacchio; Salvatore Pirozzi
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/mesa61532.2024.10704824

## 6. MagicGripper: A Mini-MagicTac Integrated Gripper Enabling Multimodal Perception in Contact-Rich Manipulation

- Year/venue: 2025; IEEE Transactions on Automation Science and Engineering
- Authors: Wen Fan; Haoran Li; Qingzheng Cong; Dandan Zhang
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/tase.2025.3631485

## 7. Development of Intelligent Robot Hand Using Proximity, Contact and Slip Sensing

- Year/venue: 2010; Transactions of the Society of Instrument and Control Engineers
- Authors: Yoshitomo Mizoguchi; Kenjiro Tadakuma; Hiroaki HASEGAWA; Aiguo Ming; Masatoshi Ishikawa; Makoto Shimojo
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.9746/sicetr.46.632

## 8. Implementing tactile behaviors using FingerVision

- Year/venue: 2017; 
- Authors: Akihiko Yamaguchi; Christopher G. Atkeson
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/humanoids.2017.8246881

## 9. Soft-smart robotic end effectors with sensing, actuation, and gripping capabilities

- Year/venue: 2019; Smart Materials and Structures
- Authors: Chaoqun Xiang; Jianglong Guo; Jonathan Rossiter
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1088/1361-665x/ab1176

## 10. Experimental Evaluation of Tactile Sensors for Compliant Robotic Hands

- Year/venue: 2021; Frontiers in Robotics and AI
- Authors: Werner Friedl; Maximo A. Roa
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3389/frobt.2021.704416

## 11. Adding Proximity Sensing Capability to Tactile Array Based on Off-the-Shelf FSR and PSoC

- Year/venue: 2019; IEEE Transactions on Instrumentation and Measurement
- Authors: Julian Castellanos-Ramos; Andres Trujillo-Leon; Rafael Navas‐Gonzalez; Francisco Barbero-Recio; Jose A. Sanchez-Duran; Oscar Oballe-Peinado; Fernando Vidal‐Verdu
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tim.2019.2944555

## 12. Force and proximity fingertip sensor to enhance grasping perception

- Year/venue: 2015; 
- Authors: Jelizaveta Konstantinova; Agostino Stilli; Kaspar Althoefer
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros.2015.7353659

## 13. A Dexterous Gripper for Space Robotics

- Year/venue: 1999; Virtual Community of Pathological Anatomy (University of Castilla La Mancha)
- Authors: Claudio Bonivento; Claudio Melchiorri; Gabriele Vassura; Gianni Ferretti; C. Maffezzoni; G. Magnani; G. Beccari; Stefano Caselli; et al.
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://hdl.handle.net/11311/563831

## 14. A Sensory Soft Robotic Gripper Capable of Learning-Based Object Recognition and Force-Controlled Grasping

- Year/venue: 2022; IEEE Transactions on Automation Science and Engineering
- Authors: Zhanfeng Zhou; Runze Zuo; Binbin Ying; Junhui Zhu; Yong Wang; Xin Wang; Xinyu Liu
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/tase.2022.3228255

## 15. Blocks World of Touch: Exploiting the Advantages of All-Around Finger Sensing in Robot Grasping

- Year/venue: 2020; Frontiers in Robotics and AI
- Authors: Daniel Fernandes Gomes; Zhonglin Lin; Shan Luo
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3389/frobt.2020.541661

## 16. Fingertip proximity sensor with realtime visual-based calibration

- Year/venue: 2016; 
- Authors: Jelizaveta Konstantinova; Agostino Stilli; Angela Faragasso; Kaspar Althoefer
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros.2016.7759051

## 17. Shape Deposition Manufacturing of a Soft, Atraumatic, Deployable Surgical Grasper1

- Year/venue: 2014; Journal of Medical Devices
- Authors: Joshua B. Gafford; Ye Ding; Andrew P. Harris; Terrence McKenna; Panagiotis Polygerinos; Donal Holland; Arthur Moser; Conor J. Walsh
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1115/1.4027048

## 18. A Novel Tactile Sensor with Electromagnetic Induction and Its Application on Stick-Slip Interaction Detection

- Year/venue: 2016; Sensors
- Authors: Yanjie Liu; Haijun Han; Tao Liu; Jingang Yi; Qingguo Li; Yoshio INOUE
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3390/s16040430

## 19. Grasp Motion Planning by Non-contact Groping based on Proximity Sensors on Robot Fingertips

- Year/venue: 2017; Journal of the Robotics Society of Japan
- Authors: Yosuke Suzuki; Masao Setogawa; Aiguo Ming; Makoto Shimojo
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.7210/jrsj.35.135

## 20. Teleoperation with Tactile Feedback based on a Capacitive Proximity Sensor Array

- Year/venue: 2020; 
- Authors: Hosam Alagi; Stefan Escaida Navarro; Jan Hergenhan; Selma Music; Bjorn Hein
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Near-field sensing estimates surface/object state before touch, usually as an input feature.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/i2mtc43012.2020.9128701

## 21. Development of a Two-Finger Haptic Robotic Hand with Novel Stiffness Detection and Impedance Control

- Year/venue: 2024; Sensors
- Authors: Vahid Mohammadi; Ramin Shahbad; Mojtaba Hosseini; Mohammad Hossein Gholampour; Saeed Shiry Ghidary; F T Najafi; Ahad Behboodi
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.3390/s24082585

## 22. A Nonarray Soft Capacitive Tactile Sensor With Simultaneous Contact Force and Location Measurement for Intelligent Robotic Grippers

- Year/venue: 2023; IEEE Transactions on Instrumentation and Measurement
- Authors: Chao Tang; Xinxin Chang; Jinxing Wang; Yulian Peng; Houping Wu; Hongbo Wang
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tim.2023.3343795

## 23. U-TAG: Electromagnetic Wireless Sensing System for Robotic Hand Pre-Grasping

- Year/venue: 2024; Sensors
- Authors: Armin Gharibi; Filippo Costa; Simone Genovesi
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.3390/s24165340

## 24. Grip Stabilization through Independent Finger Tactile Feedback Control

- Year/venue: 2020; Sensors
- Authors: Filipe Veiga; Benoni B. Edin; Jan Peters
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.3390/s20061748

## 25. Sim-to-Real Transfer for Robotic Manipulation with Tactile Sensory

- Year/venue: 2021; 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Authors: Zihan Ding; Ya-Yen Tsai; Wang Wei Lee; Bidan Huang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/iros51168.2021.9636259

## 26. Soft-bubble grippers for robust and perceptive manipulation

- Year/venue: 2020; 
- Authors: Naveen Kuppuswamy; Alex Alspach; Avinash Uttamchandani; Sam Creasey; Takuya Ikeda; Russ Tedrake
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros45743.2020.9341534

## 27. Maximizing manipulation capabilities of persons with disabilities using a smart 9-degree-of-freedom wheelchair-mounted robotic arm system

- Year/venue: 2007; 
- Authors: Rajiv Dubey; Redwan Alqasemi
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=1598&context=etd

## 28. A Fingertip Sensor and Algorithms for Pre-touch Distance Ranging and Material Detection in Robotic Grasping

- Year/venue: 2023; arXiv (Cornell University)
- Authors: Cheng Fang; Wang Di; Fengzhi Guo; Jun Zou; Dezhen Song
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://arxiv.org/abs/2311.10453

## 29. Development of an Integrated Tactile Sensor System for Clothes Manipulation and Classification Using Industrial Grippers

- Year/venue: 2017; IEEE Sensors Journal
- Authors: Simone Denei; Perla Maiolino; Emanuele Baglini; Giorgio Cannata
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jsen.2017.2743065

## 30. Design and integration of a multi-axial tactile sensor for dexterous manipulation by humanoid robots for industrial applications

- Year/venue: 2025; Results in Engineering
- Authors: Aida Ali; Miral Y. Selim
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1016/j.rineng.2025.108494

## 31. Tactile Sensing for Minimally Invasive Surgery: Conventional Methods and Potential Emerging Tactile Technologies

- Year/venue: 2022; Frontiers in Robotics and AI
- Authors: Wael Othman; Zhi-Han A. Lai; Carlos Abril; Juan S. Barajas-Gamboa; Ricard Corcelles; Matthew Kroh; Mohammad A. Qasaimeh
- Problem claimed: Select or plan a feasible grasp from exteroceptive object state before execution.
- Actual mechanism introduced: Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3389/frobt.2021.705662

## 32. An AI‐Enabled All‐In‐One Visual, Proximity, and Tactile Perception Multimodal Sensor

- Year/venue: 2025; Advanced Robotics Research
- Authors: Menghao Pu; Tiyong Zhao; Lingxi Zhang; Chaoqun Han; Zhiping Chai; Yifan Zhou; Han‐Fei Ding; Zhigang Wu
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1002/adrr.202500062

## 33. Gentle Grasping: A Method With Low-Cost Magnetic Tactile Sensors

- Year/venue: 2025; IEEE Access
- Authors: Yi Liu; Remko Proesmans; Andreas Verleysen; Francis wyffels
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/access.2025.3628903

## 34. Innovative Design of a Soft Robotic Gripper for In-hand Manipulation

- Year/venue: 2021; HAL (Le Centre pour la Communication Scientifique Directe)
- Authors: Amir Pagoli
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://theses.hal.science/tel-03813576

## 35. Multimodal Human Hand Motion Sensing and Analysis-A Review

- Year/venue: 2018; IEEE Transactions on Cognitive and Developmental Systems
- Authors: Yaxu Xue; Zhaojie Ju; Kui Xiang; Jing Chen; Honghai Liu
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tcds.2018.2800167

## 36. Robust bionic distributed multimodal flexible sensor for extreme-condition sensing and intelligent operation

- Year/venue: 2026; Communications Engineering
- Authors: Baijin Mao; Yedong Huang; Yuyaocen Xiang; Wenbo Liu; Xunlong Shi; Xiang Qian; Juntian Qu
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1038/s44172-026-00653-0

## 37. Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization

- Year/venue: 2020; Sensors
- Authors: Zhen Deng; Yannick Jonetzko; Liwei Zhang; Jianwei Zhang
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.3390/s20041050

## 38. Sim-to-Real Transfer for Robotic Manipulation with Tactile Sensory

- Year/venue: 2021; arXiv (Cornell University)
- Authors: Zihan Ding; Ya-Yen Tsai; Wang Wei Lee; Bidan Huang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: http://arxiv.org/abs/2103.00410

## 39. AMADEUS: advanced manipulation for deep underwater sampling

- Year/venue: 1997; IEEE Robotics & Automation Magazine
- Authors: David M. Lane; J.B.C. Davies; Giuseppe Casalino; G. Bartolini; Giorgio Cannata; G. Veruggio; Miquel Canals; Chris Smith; et al.
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/100.637804

## 40. Integrated force and distance sensing using elastomer-embedded commodity proximity sensors

- Year/venue: 2016; 
- Authors: Radhen Patel; Nikolaus Correll
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://doi.org/10.15607/rss.2016.xii.035

## 41. Finger‐Skin‐Inspired Flexible Optical Sensor for Force Sensing and Slip Detection in Robotic Grasping

- Year/venue: 2021; Advanced Materials Technologies
- Authors: Chengpeng Jiang; Zhang Zhang; Jing Pan; Yancheng Wang; Lei Zhang; Liming Tong
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1002/admt.202100285

## 42. TacFR-Gripper: A Reconfigurable Fin-Ray-Based Gripper with Tactile Skin for In-Hand Manipulation

- Year/venue: 2024; Actuators
- Authors: Qingzheng Cong; Wen Fan; Dandan Zhang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3390/act13120521

## 43. Adaptive Grasping of Moving Objects through Tactile Sensing

- Year/venue: 2021; Sensors
- Authors: Patrick Lynch; Michael F. Cullinan; Conor McGinn
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3390/s21248339

## 44. Learning to detect slip through tactile estimation of the contact force field and its entropy properties

- Year/venue: 2024; Mechatronics
- Authors: Xiaohai Hu; Aparajit Venkatesh; Yusen Wan; Guiliang Zheng; Neel Jawale; Navneet Kaur; Xu Chen; Paul Birkmeyer
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1016/j.mechatronics.2024.103258

## 45. Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing

- Year/venue: 2023; IEEE Transactions on Neural Networks and Learning Systems
- Authors: Shaowei Cui; Shuo Wang; Rui Wang; Shaolin Zhang; Chaofan Zhang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tnnls.2023.3270579

## 46. [Paper] Combined Tactile and Proximity Sensor Employing Compound-eye Camera

- Year/venue: 2015; ITE Transactions on Media Technology and Applications
- Authors: Hiroto Nakashima; Keiichiro Kagawa; Kazuhiro Shimonomura
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3169/mta.3.227

## 47. Grasping and tactile servoing of deformable objects

- Year/venue: 2023; theses.fr (ABES)
- Authors: Peng Song
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://www.theses.fr/2023UCFA0082/document

## 48. Quantitative softness and texture bimodal haptic sensors for robotic clinical feature identification and intelligent picking

- Year/venue: 2024; Science Advances
- Authors: Ye Qiu; Fangnan Wang; Zhuang Zhang; Kuanqiang Shi; Yi Song; Jiutian Lu; Minjia Xu; Mengyuan Qian; et al.
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1126/sciadv.adp0348

## 49. Tactile Sensors for Friction Estimation and Incipient Slip Detection-Toward Dexterous Robotic Manipulation: A Review

- Year/venue: 2018; IEEE Sensors Journal
- Authors: Wei Chen; Heba Khamis; Ingvars Birznieks; Nathan F. Lepora; Stephen J. Redmond
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jsen.2018.2868340

## 50. Multimodal tactile sensing fused with vision for dexterous robotic housekeeping

- Year/venue: 2024; Nature Communications
- Authors: Qian Mao; Zijian Liao; Jinfeng Yuan; Rong Zhu
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1038/s41467-024-51261-5

## 51. Tactile-based manipulation of deformable objects with dynamic center of mass

- Year/venue: 2016; 
- Authors: Mohsen Kaboli; Kunpeng Yao; Gordon Cheng
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/humanoids.2016.7803358

## 52. Elongatable Gripper Fingers With Integrated Stretchable Tactile Sensors for Underactuated Grasping and Dexterous Manipulation

- Year/venue: 2022; IEEE Transactions on Robotics
- Authors: Sohee John Yoon; Minsik Choi; Bomin Jeong; Yong‐Lae Park
- Problem claimed: Select or plan a feasible grasp from exteroceptive object state before execution.
- Actual mechanism introduced: Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tro.2022.3144949

## 53. Design and Benchmarking of a Multimodality Sensor for Robotic Manipulation With GAN-Based Cross-Modality Interpretation

- Year/venue: 2025; IEEE Transactions on Robotics
- Authors: Dandan Zhang; Wen Fan; Jialin Lin; Haoran Li; Qingzheng Cong; Weiru Liu; Nathan F. Lepora; Shan Luo
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Near-field sensing estimates surface/object state before touch, usually as an input feature.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tro.2025.3526296

## 54. Slip-actuated bionic tactile sensing system with dynamic DC generator integrated E-textile for dexterous robotic manipulation

- Year/venue: 2025; Nature Communications
- Authors: Vashin Gautham; Ashutosh Panpalia; Hamid Manouchehri; Krushang Gabani; Vinoop Anil; Shakunthala Yerneni; Rohit Thakar; Aayush Nayyar; et al.
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1038/s41467-025-61843-6

## 55. Cable manipulation with a tactile-reactive gripper

- Year/venue: 2021; The International Journal of Robotics Research
- Authors: Yu She; Shaoxiong Wang; Siyuan Dong; Neha Sunil; Alberto Rodriguez; Edward H. Adelson
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1177/02783649211027233

## 56. Harnessing the physical properties of objects for robotic grasping and manipulation

- Year/venue: 2023; Aaltodoc (Aalto University)
- Authors: Tran Nguyen Le
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://aaltodoc.aalto.fi/handle/123456789/125131

## 57. E-Skin: From Humanoids to Humans [Point of View]

- Year/venue: 2019; Proceedings of the IEEE
- Authors: Ravinder Dahiya
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jproc.2018.2890729

## 58. Stabilizing novel objects by learning to predict tactile slip

- Year/venue: 2015; 
- Authors: Filipe Veiga; Herke van Hoof; Jan Peters; Tucker Hermans
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros.2015.7354090

## 59. Visual-Tactile Fusion for 3D Objects Reconstruction from a Single Depth View and a Single Gripper Touch for Robotics Tasks

- Year/venue: 2021; 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Authors: Mohamed Tahoun; Omar Tahri; Juan Antonio Corrales Ramon; Youcef Mezouar
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros51168.2021.9636150

## 60. The role of feed-forward and feedback processes for closed-loop prosthesis control

- Year/venue: 2011; Journal of NeuroEngineering and Rehabilitation
- Authors: Ian Saunders; Sethu Vijayakumar
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1186/1743-0003-8-60

## 61. Control Framework for Dexterous Manipulation Using Dynamic Visual Servoing and Tactile Sensors' Feedback

- Year/venue: 2014; Sensors
- Authors: Carlos A. Jara; Jorge Pomares; Francisco A. Candelas-Herias; Fernando Torres
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.3390/s140101787

## 62. Dynamically Reconfigurable Tactile Sensor for Robotic Manipulation

- Year/venue: 2020; IEEE Robotics and Automation Letters
- Authors: Tae Myung Huh; Hojung Choi; Simone Willcox; Stephanie M. Moon; Mark R. Cutkosky
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/lra.2020.2972881

## 63. HANDdata - first-person dataset including proximity and kinematics measurements from reach-to-grasp actions

- Year/venue: 2023; Scientific Data
- Authors: Enzo Mastinu; Anna Coletti; S. Mohammad; Jasper van den Berg; Christian Cipriani
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1038/s41597-023-02313-w

## 64. Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy Properties

- Year/venue: 2024; IFAC-PapersOnLine
- Authors: Xiaohai Hu; Aparajit Venkatesh; Yusen Wan; Guiliang Zheng; Neel Jawale; Navneet Kaur; Xu Chen; Paul Birkmeyer
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1016/j.ifacol.2025.01.142

## 65. Multi-Modal Haptic Feedback for Grip Force Reduction in Robotic Surgery

- Year/venue: 2019; Scientific Reports
- Authors: Ahmad Abiri; Jake Pensa; Anna Tao; Ji Ma; Yen‐Yi Juo; Syed J. Askari; James W. Bisley; Jacob Rosen; et al.
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1038/s41598-019-40821-1

## 66. Variable-Friction Finger Surfaces to Enable Within-Hand Manipulation via Gripping and Sliding

- Year/venue: 2018; IEEE Robotics and Automation Letters
- Authors: Adam J. Spiers; Berk Callı; Aaron M. Dollar
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/lra.2018.2856398

## 67. Proximity Perception-Based Grasping Intelligence: Toward the Seamless Control of a Dexterous Prosthetic Hand

- Year/venue: 2023; IEEE/ASME Transactions on Mechatronics
- Authors: Si‐Hwan Heo; Hyung‐Soon Park
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tmech.2023.3324051

## 68. UV-laser-machined stretchable multi-modal sensor network for soft robot interaction

- Year/venue: 2022; npj Flexible Electronics
- Authors: Jooyeun Ham; Amy Kyungwon Han; Mark R. Cutkosky; Zhenan Bao
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1038/s41528-022-00225-0

## 69. A Review on Sensor Technologies, Control Approaches, and Emerging Challenges in Soft Robotics

- Year/venue: 2025; Advanced Robotics Research
- Authors: Ean Lovett; Maxwell Hammond; Niloufar Seyfi; Amirreza Fahim Golestaneh; Venanzio Cichella; Caterina Lamuta
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1002/adrr.202500085

## 70. Knot-inspired optical sensors for slip detection and friction measurement in dexterous robotic manipulation

- Year/venue: 2023; Opto-Electronic Advances
- Authors: Jing Pan; Qi Wang; Shuaikang Gao; Zhang Zhang; Yu Xie; Longteng Yu; Lei Zhang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.29026/oea.2023.230076

## 71. Nondestructive identification of softness via bioinspired multisensory electronic skins integrated on a robotic hand

- Year/venue: 2022; npj Flexible Electronics
- Authors: Ye Qiu; Shenshen Sun; Xueer Wang; Kuanqiang Shi; Zhiqiang Wang; Xiaolong Ma; Wen‐An Zhang; Guanjun Bao; et al.
- Problem claimed: Maintain object control during dexterous in-hand manipulation under contact uncertainty.
- Actual mechanism introduced: A learned tactile/visuotactile representation maps sensor histories to grasp success or actions.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1038/s41528-022-00181-9

## 72. 2005 IEEE/RSJ International Conference on Intelligent Robots and Systems

- Year/venue: 2005; 
- Authors: Sean Hodgson; Mahdi Tavakoli; Arnaud Leleve; Minh Tu Pham
- Problem claimed: Select or plan a feasible grasp from exteroceptive object state before execution.
- Actual mechanism introduced: Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/iros.2005.1544945

## 73. GTac-Hand: A Robotic Hand With Integrated Tactile Sensing and Extrinsic Contact Sensing Capabilities

- Year/venue: 2023; IEEE/ASME Transactions on Mechatronics
- Authors: Zeyu Lu; Haoyong Yu
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/tmech.2023.3264650

## 74. Design and Calibration of a Force/Tactile Sensor for Dexterous Manipulation

- Year/venue: 2019; Sensors
- Authors: Marco Costanzo; Giuseppe De Maria; Ciro Natale; Salvatore Pirozzi
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3390/s19040966

## 75. Planning Visual-Tactile Precision Grasps via Complementary Use of Vision and Touch

- Year/venue: 2023; IEEE Robotics and Automation Letters
- Authors: Martin Matak; Tucker Hermans
- Problem claimed: Select or plan a feasible grasp from exteroceptive object state before execution.
- Actual mechanism introduced: Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/lra.2022.3231520

## 76. Evetac: An Event-Based Optical Tactile Sensor for Robotic Manipulation

- Year/venue: 2024; IEEE Transactions on Robotics
- Authors: Niklas Funk; Erik Helmut; Georgia Chalvatzaki; Roberto Calandra; Jan Peters
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tro.2024.3428430

## 77. Grasping force control of multi-fingered robot hand based on slip detection using tactile sensor

- Year/venue: 2008; 
- Authors: Daisuke Gunji; Yoshitomo Mizoguchi; Seiichi Teshigawara; Aiguo Ming; Akio Namiki; Masatoshi Ishikawaand; Makoto Shimojo
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/robot.2008.4543605

## 78. Design and Experimental Evaluation of a Sensorimotor-Inspired Grasping Strategy for Dexterous Prosthetic Hands

- Year/venue: 2022; IEEE Transactions on Neural Systems and Rehabilitation Engineering
- Authors: Ting Zhang; Ning Zhang; Yang Li; Bo Zeng; Li Jiang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tnsre.2022.3231972

## 79. TacRot: A Parallel-Jaw Gripper with Rotatable Tactile Sensors for In-Hand Manipulation

- Year/venue: 2022; 2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
- Authors: Wuyi Zhang; Chongkun Xia; Xiaojun Zhu; Houde Liu; Bin Liang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/smc53654.2022.9945388

## 80. Slip Detection with Combined Tactile and Visual Information

- Year/venue: 2018; arXiv (Cornell University)
- Authors: Jianhua Li; Siyuan Dong; Edward H. Adelson
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: http://arxiv.org/abs/1802.10153

## 81. Design and evaluation of a Multi-Finger Skin-Stretch Tactile Interface for Hand Rehabilitation Robots

- Year/venue: 2024; 
- Authors: Alexandre L. Ratschat; Ruben Martin-Rodriguez; Yasemin Vardar; Gerard M. Ribbers; Laura Marchal-Crespo
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/biorob60516.2024.10719873

## 82. Action-Intention-Based Grasp Control With Fine Finger-Force Adjustment Using Combined Optical-Mechanical Tactile Sensor

- Year/venue: 2014; IEEE Sensors Journal
- Authors: Makoto Saen; Kiyoto Ito; Kenichi Osada
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/jsen.2014.2331689

## 83. Integrating and Evaluating Visuo-tactile Sensing with Haptic Feedback for Teleoperated Robot Manipulation

- Year/venue: 2024; arXiv (Cornell University)
- Authors: Noah Becker; Sovailo, Kyrylo; Zhu, Chunyao; Erik Gattung; Kay Hansel; Tim Schneider; Yaonan Zhu; Yasuhisa Hasegawa; et al.
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://arxiv.org/abs/2404.19585

## 84. Pre-touch sensing for sequential manipulation

- Year/venue: 2017; 
- Authors: Boling Yang; Patrick Lancaster; Joshua R. Smith
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Near-field sensing estimates surface/object state before touch, usually as an input feature.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/icra.2017.7989594

## 85. Improved Learning of Robot Manipulation Tasks Via Tactile Intrinsic Motivation

- Year/venue: 2021; IEEE Robotics and Automation Letters
- Authors: Nikola Vulin; Sammy Christen; Stefan Stevsic; Otmar Hilliges
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/lra.2021.3061308

## 86. A Mode-Switching Motion Control System for Reactive Interaction and Surface Following Using Industrial Robots

- Year/venue: 2018; IEEE/CAA Journal of Automatica Sinica
- Authors: Danial Nakhaeinia; Pierre Payeur; Robert Laganiere
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Pre-touch/proximity sensing is fused into perception or grasp selection before execution.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jas.2018.7511069

## 87. A Bio-Inspired Slip Detection and Reflex-Like Suppression Method for Robotic Manipulators

- Year/venue: 2019; IEEE Sensors Journal
- Authors: Andrei Nakagawa-Silva; Nitish V. Thakor; John‐John Cabibihan; Alcimar Barbosa Soares
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jsen.2019.2939506

## 88. Multilevel control of an anthropomorphic prosthetic hand for grasp and slip prevention

- Year/venue: 2016; Advances in Mechanical Engineering
- Authors: Roberto Barone; Anna Lisa Ciancio; Rocco Antonio Romeo; Angelo Davalli; Rinaldo Sacchetti; Eugenio Guglielmelli; Loredana Zollo
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1177/1687814016665082

## 89. Learning Generalizable Vision-Tactile Robotic Grasping Strategy for Deformable Objects via Transformer

- Year/venue: 2024; IEEE/ASME Transactions on Mechatronics
- Authors: Yunhai Han; Kelin Yu; Rahul Batra; Nathan Boyd; C. H. Mehta; Tuo Zhao; Yu She; Seth Hutchinson; et al.
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/tmech.2024.3400789

## 90. Manipulation by Feel: Touch-Based Control with Deep Predictive Models

- Year/venue: 2019; arXiv (Cornell University)
- Authors: Stephen Tian; Frederik Ebert; Dinesh Jayaraman; Mayur Mudigonda; Chelsea Finn; Roberto Calandra; Sergey Levine
- Problem claimed: Select or plan a feasible grasp from exteroceptive object state before execution.
- Actual mechanism introduced: Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections; more data can compensate for a poorly placed decision boundary
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://arxiv.org/abs/1903.04128

## 91. Handheld Micromanipulator for Robot - Assisted Microsurgery

- Year/venue: 2018; Research Showcase @ Carnegie Mellon University (Carnegie Mellon University)
- Authors: Sungwook Yang
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Near-field sensing estimates surface/object state before touch, usually as an input feature.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: http://repository.cmu.edu/cgi/viewcontent.cgi?article=1619&context=dissertations

## 92. Tactile Sensing and Control of Robotic Manipulator Integrating Fiber Bragg Grating Strain-Sensor

- Year/venue: 2019; Frontiers in Neurorobotics
- Authors: Luca Massari; Calogero Maria Oddo; Edoardo Sinibaldi; Renaud Detry; Joseph Bowkett; Kalind Carpenter
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.3389/fnbot.2019.00008

## 93. Making Sense of Vision and Touch: Learning Multimodal Representations for Contact-Rich Tasks

- Year/venue: 2020; IEEE Transactions on Robotics
- Authors: Michelle A. Lee; Yuke Zhu; Peter Zachares; Matthew Tan; Krishnan Srinivasan; Silvio Savarese; Li Fei-Fei; Animesh Garg; et al.
- Problem claimed: Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact.
- Actual mechanism introduced: Near-field sensing estimates surface/object state before touch, usually as an input feature.
- Hidden assumptions: cue confidence is enough without modeling switch lead distance; a perception-stage improvement automatically changes the executed contact mode; false early switches and late switches have symmetric cost; the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; cue lead distance; cue dropout; distance-dependent cue informativeness; time from first contact to useful tactile evidence
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; cue appears but is not converted into a hard control guard; ambiguous cue consumes the remaining lead distance; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: precontact/proximity sensing itself; using tactile feedback for grasp stability; hybrid/force control after contact; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how noisy precontact cues become an executable hybrid-control contract; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/tro.2019.2959445

## 94. Design and development of a wearable haptic feedback device to recognize textured surfaces: Preliminary study

- Year/venue: 2017; 
- Authors: Sachille Atapattu; N. M. Senevirathna; Hui Shan; T. B. T. Madusanka; Thilina Dulantha Lalitharatne; Damith Suresh Chathuranga
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/aim.2017.8013988

## 95. Real-Time Intelligent Gripping System for Dexterous Manipulation of Industrial Robots

- Year/venue: 2009; 
- Authors: Abhinav Abhinav; S. Vivekanandan
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: http://www.iaeng.org/publication/WCE2009/WCE2009_pp1747-1752.pdf

## 96. Enhanced Force Estimation and Autonomous Force Tuning Through Fusion of Tactile Sensor and Quasi-Direct Drive Gripper

- Year/venue: 2024; IEEE Sensors Journal
- Authors: Thomas De Clercq; Frederik Ostyn; Guillaume Crevecoeur
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/jsen.2024.3504717

## 97. Fingertip Contact Force Direction Control using Tactile Feedback

- Year/venue: 2024; 
- Authors: Dounia Kitouni; Elie Chelly; Mahdi Khoramshahi; Veronique Perdereau
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/case59546.2024.10711382

## 98. Tactile object class and internal state recognition for mobile manipulation

- Year/venue: 2010; 
- Authors: Sachin Chitta; Matthew Piccoli; Jurgen Sturm
- Problem claimed: Control motion and force once contact constraints are active in contact-rich manipulation.
- Actual mechanism introduced: A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: https://doi.org/10.1109/robot.2010.5509923

## 99. Improving the Representation and Extraction of Contact Information in Vision-Based Tactile Sensors Using Continuous Marker Pattern

- Year/venue: 2023; IEEE Robotics and Automation Letters
- Authors: Mingxuan Li; Yen Hang Zhou; Tiemin Li; Yao Jiang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; grasp family is fixed by pre-execution planning; local geometry uncertainty can be handled by continuous corrections
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; grasp selection and preshaping from perception
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible
- URL/DOI: https://doi.org/10.1109/lra.2023.3303830

## 100. Visuo-Tactile-Based Slip Detection Using A Multi-Scale Temporal Convolution Network

- Year/venue: 2023; arXiv (Cornell University)
- Authors: Junli Gao; Zhaoji Huang; Zhaonian Tang; Haitao Song; Wenyu Liang
- Problem claimed: Detect incipient slip or contact instability after touch so the robot can stabilize a grasp.
- Actual mechanism introduced: Tactile or force signals trigger post-contact slip/stability classification and corrective force.
- Hidden assumptions: the first touch can be used as an information-gathering event; post-contact evidence arrives early enough for correction; hybrid guards belong at contact onset; the discrete strategy is already selected before force control matters; grasp family is fixed by pre-execution planning
- Variables treated as fixed: switching latency; approach speed; first-contact impulse budget; time from first contact to useful tactile evidence; contact-mode transition timing; grasp-family commitment point
- Failure modes ignored: late strategy switch reaches contact in the wrong mode; first-contact transient breaks the object or causes slip before feedback acts; tactile evidence is correct but arrives after the damage/slip event; vision commits to a grasp family despite hidden local surface state
- What it makes less novel: using tactile feedback for grasp stability; hybrid/force control after contact; grasp selection and preshaping from perception; learned manipulation policies or representations
- What it leaves open: where the mode-switch guard should be placed relative to first contact; how remaining lead distance should enter the decision rule; how to avoid failures that happen before tactile correction is physically possible; how to choose the contact strategy before the contact manifold is reached
- URL/DOI: http://arxiv.org/abs/2302.13564
