<div align="center">

# Towards Human-Centered Safety in Vision-Language-Action Policies for Robotics: A Survey and Outlook

</div>

## Overview

This is the Github link to organize papers in the survey.

<details open>
<summary><b>Related papers</b></summary>

- [A Pathway Study for Future Humanoid Standards](https://www.therobotreport.com/wp-content/uploads/2025/09/IEEE-Humanoid-Report-of-Future-Standards-Development.pdf). *IEEE Robotics and Automation Society*, 2025.  

- [Human-AI Safety: A Descendant of Generative AI and Control Systems Safety](https://arxiv.org/abs/2405.09794). *arXiv 2405.09794*, 2024.  

- [Perceived Safety in Physical Human-Robot Interaction – A Survey](https://arxiv.org/abs/2009.07217). *ACM Computing Surveys*, 2021.  

- [Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems](https://arxiv.org/abs/2405.06624). *arXiv 2405.06624*, 2024. 

- [Action Hallucination in Generative Visual-Language-Action Models](https://arxiv.org/abs/2602.06339). *arXiv 2602.06339*, 2026.  

- [Position: Good Embodied Reward Models Need Bad Behavior Data](https://arxiv.org/abs/2406.06087). *arXiv 2406.06087*, 2024.  

</details>


## Surveyed Papers


<details open>
<summary><b>I. Design-Time Safety</b></summary>

<details open>
<summary><i>A. Learning-based Alignment</i></summary>

<details open>
<summary>Direct Control Alignment</summary>

<p>
These methods characterize reactive control safety strategies typically identified as System 1.
</p>

<summary>Imitation-Driven Safety</summary>

- [ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846). CoRL, 2023.

- [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896). ICRA, 2024.

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.


<summary>Control-Constrained Safety</summary>

- [Human-Guided Reinforcement Learning With Sim-to-Real Transfer for Autonomous Navigation](https://ieeexplore.ieee.org/document/10250993). TPAMI, 2023.

- [From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning](https://arxiv.org/abs/2507.22028). ICLR Poster, 2026.

- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480). NeurIPS Spotlight, 2025.

</details>


<details open>
<summary>Reasoning-Augmented Control Alignment</summary>
<p>
These models augment reactive (System 1) policies with reasoning (System 2) to infer actions based on safety factors and/or predicted outcomes.
</p>

<summary>Reasoning-Constrained Safety</summary>

- [Tokenize the World into Object-level Knowledge to Address Long-tail Events in Autonomous Driving](https://arxiv.org/abs/2407.00959). CoRL, 2024.

- [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757). NeurIPS, 2025.

- [Poutine: Vision-Language-Trajectory Pre-Training and Reinforcement Learning Post-Training Enable Robust End-to-End Autonomous Driving](https://arxiv.org/abs/2506.11234). *arXiv 2506.11234*, 2025.

- [StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving](https://arxiv.org/abs/2603.09482). *arXiv 2603.09482*, 2026.

- [SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model](https://arxiv.org/abs/2604.19710). *arXiv 2604.19710*, 2026.

- [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167). *arXiv 2602.08167*, 2026.

- [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://arxiv.org/abs/2602.02459). ICML, 2026.

- [RationalVLA: A Rational Vision-Language-Action Model with Dual System](https://arxiv.org/abs/2506.10826). *arXiv 2506.10826*, 2025.

- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020). *arXiv 2503.20020*, 2025.

<summary>World-Model-Based Safety</summary>

- [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720). ECCV, 2024.

- [IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model](https://arxiv.org/abs/2508.06571). *arXiv 2508.06571*, 2025.

- [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063). *arXiv 2603.01063*, 2026.

- [Learning from Mistakes: Post-Training for Driving VLA with Takeover Data](https://arxiv.org/abs/2603.14972). *arXiv 2603.14972*, 2026.

- [Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models](https://arxiv.org/abs/2603.06049). *CVPR Findings*, 2026.

- [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2512.24426). CVPR, 2026.


<summary>Hybrid</summary>

- [Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail](https://arxiv.org/abs/2511.00088). *arXiv 2511.00088*, 2025.

- [Latent Chain-of-Thought World Modeling for End-to-End Driving](https://arxiv.org/abs/2512.10226). *arXiv 2512.10226*, 2025.

</details>

<details open>
<summary>Agentic Action Alignment</summary>
<p>
These models relie on safety-aligned LLMs/VLMs to select and sequence actions via planners or action APIs that directly interface with robotic systems, enabling agentic System 2 control.
</p>

These are susceptible to risks such as,

- [Safety Not Found (404): Hidden Risks of LLM-Based Robotics Decision Making](https://arxiv.org/abs/2407.09179). *arXiv 2407.09179*, 2024.  

- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691). ICRA, 2025.

- [BadRobot: Jailbreaking Embodied LLMs in the Physical World](https://arxiv.org/abs/2407.20242). ICLR, 2025.

- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.


Meanwhile, defenses are reliant on the base MLLM,

- [HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal](https://arxiv.org/abs/2402.04249). ICML, 2024.

- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663). *arXiv 2503.08663*, 2025.

- [Can AI Perceive Physical Danger and Intervene?](https://arxiv.org/abs/2509.21651). *arXiv 2509.21651*, 2025.



</details>
</details>


<details open>
<summary><i>B. Safety Data Scaling</i></summary>

<details open>
<summary>Safety-Critical Data Sampling</summary>

- [SSE: Multimodal Semantic Data Selection and Enrichment for Industrial-scale Data Assimilation](https://arxiv.org/abs/2409.13860). KDD, 2025.

- [Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems](https://arxiv.org/abs/2604.08366). *arXiv 2604.08366*, 2026.

- [Unsupervised Discovery of Failure Taxonomies from Deployment Logs](https://arxiv.org/abs/2506.06570). *arXiv 2506.06570*, 2025.

</details>

<details open>
<summary>Safety-Critical Data Generation</summary>

Simulation-based strategies have been proposed to collect data via scripted motions,

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.

- [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642). *arXiv 2510.01642*, 2025.

- [Avoid Everything: Model-Free Collision Avoidance with Expert-Guided Fine-Tuning](https://proceedings.mlr.press/v270/fishman25a.html). CoRL, 2025.

Others constructs augmented environments that expose models to rare but physically plausible hazards with neural world modeling,

- [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080). *arXiv 2309.17080*, 2023.

- [GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving](https://arxiv.org/abs/2503.20523). *arXiv 2503.20523*, 2025.

- [Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control](https://arxiv.org/abs/2503.14492). *arXiv 2503.14492*, 2025. 

- [Cosmos-Drive-Dreams: Scalable Synthetic Driving Data Generation with World Foundation Models](https://arxiv.org/abs/2506.09042). *arXiv 2506.09042*, 2025.

- [Evaluating Gemini Robotics Policies in a Veo World Simulator](https://arxiv.org/abs/2512.10675). *arXiv 2512.10675*, 2025.

</details>

</details>
</details>

---

<details open>
<summary><b>Deployment-Time Safety</b></summary>

<details open>
<summary><i>A. Safe Action Guardrail</i></summary>

<details open>
<summary>1) Control-Level Guardrail</summary>

The set of safety filters that check robot predicted controls against explicit constraints, applies corrections if needed, and selects safely executable actions.

<details open>
<summary>(a) Control-Theoretic Filters</summary>

<summary>Reachability-based filters</summary>

- [From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies](https://arxiv.org/abs/2511.06385). *arXiv 2511.06385*, 2025.  

- [Robots That Suggest Safe Alternatives](https://arxiv.org/abs/2409.09883). *arXiv 2409.09883*, 2024.  

- [Generalizing Safety Beyond Collision-Avoidance via Latent-Space Reachability Analysis](https://arxiv.org/abs/2502.00935). *arXiv 2502.00935*, 2025.  

- [Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures](https://arxiv.org/abs/2505.00779). *arXiv 2505.00779*, 2025.  

- [AnySafe: Adapting Latent Safety Filters at Runtime via Safety Constraint Parameterization in the Latent Space](https://arxiv.org/abs/2509.19555). *arXiv 2509.19555*, 2025.  

- [What You Don't Know Can Hurt You: How Well do Latent Safety Filters Understand Partially Observable Safety Constraints?](https://arxiv.org/abs/2510.06492). *arXiv 2510.06492*, 2025.  

- [How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints](https://arxiv.org/abs/2511.18606). *arXiv 2511.18606*, 2025.  


<summary>Control-barrier function filters</summary>

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891). *arXiv 2512.11891*, 2025.  

- [Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation](https://arxiv.org/abs/2603.05754). *arXiv 2603.05754*, 2026.
Handling perceptual blind spots (e.g., is that stove hot? is that a reflection or a real object?) with safety constraints and runtime safety filter.

</details>

<details open>
<summary>(b) Model Predictive Filters</summary>

<summary>Value estimation</summary>

- [Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification](https://arxiv.org/abs/2510.16281). *arXiv 2510.16281*, 2025.  

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.  

- [From Obstacles to Etiquette: Robot Social Navigation with VLM-Informed Path Selection](https://arxiv.org/abs/2602.09002). *arXiv 2602.09002*, 2026.

<!-- - [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281). *arXiv 2602.12281*, 2026.   -->

<summary>Neural world modeling</summary>

- [From Foresight to Forethought: VLM-in-the-Loop Policy Steering via Latent Alignment](https://arxiv.org/abs/2502.01828). *arXiv 2502.01828*, 2025.  

- [Reimagination with Test-time Observation Interventions: Distractor-Robust World Model Predictions for Visual Model Predictive Control](https://arxiv.org/abs/2506.16565). *arXiv 2506.16565*, 2025.  

- [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918). *arXiv 2311.17918*, 2023.  

</details>
</details>

<details open>
<summary>2) Task-Level Guardrail</summary>

<summary>Formal runtime verification</summary>

<!-- 104 130-139 148-149 -->

- [How to Raise a Robot -- A Case for Neuro-Symbolic AI in Constrained Task Planning for Humanoid Assistive Robots](https://arxiv.org/abs/2312.08820). SACMAT 2023

- [Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents](https://arxiv.org/abs/2309.09919). *arXiv 2309.09919*, 2023. 

- [SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models](https://arxiv.org/abs/2409.19471). *arXiv 2409.19471*, 2024.  

- [Ensuring Safety in LLM-Driven Robotics: A Cross-Layer Sequence Supervision Mechanism](https://doi.org/10.1109/IROS58592.2024.10801576). IROS, 2024. 

- [Subtle Risks, Critical Failures: A Framework for Diagnosing Physical Safety of LLMs for Embodied Decision Making](https://aclanthology.org/2025.emnlp-main.1305.pdf). EMNLP, 2025.

- [SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning](https://arxiv.org/abs/2503.06892). *arXiv 2503.06892*, 2025.  

- [IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402). *arXiv 2506.16402*, 2025. 

- [Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis](https://arxiv.org/abs/2503.03911). *arXiv 2503.03911*, 2025.  

- [Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885). *arXiv 2503.07885*, 2025.  

- [RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic](https://arxiv.org/abs/2512.21220). *arXiv 2512.21220*, 2025.  

- [Ask, Reason, Assist: Decentralized Robot Collaboration via Language and Logic](https://arxiv.org/abs/2509.23506). *arXiv 2509.23506*, 2025.

<summary>Semantic verification</summary>

- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.

- [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963). *arXiv 2401.12963*, 2024.  


- [Don't Let Your Robot Be Harmful: Responsible Robotic Manipulation](https://arxiv.org/abs/2411.18289). *arXiv 2411.18289*, 2024.  


</details>

</details>

<details open>
<summary><i>B. Safety against OOD</i></summary>

<summary>OOD detection</summary>

- [Semantic Anomaly Detection with Large Language Models](https://arxiv.org/abs/2305.11307). *Autonomous Robots*, 2023.  

- [Robots That Ask for Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928). *arXiv 2307.01928*, 2023.  

- [Real-Time Anomaly Detection and Reactive Planning with Large Language Models](https://arxiv.org/abs/2407.08735). *arXiv 2407.08735*, 2024.  

<summary>OOD-aware control prediction</summary>

- [Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning](https://arxiv.org/abs/2505.10547). *arXiv 2505.10547*, 2025.  

- [Uncertainty-Aware Latent Safety Filters for Avoiding Out-of-Distribution Failures](https://arxiv.org/abs/2505.00779). *arXiv 2505.00779*, 2025.  

- [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474). *arXiv 2602.22474*, 2026.  


</details>

<details open>
<summary><i>C. Safety against Attacks</i></summary>

<details open>
<summary>1) Control-Level Defense</summary>

<details open>
<summary>(a) Adversarial attack risks & defenses</summary>

<summary>Attack risks</summary>

- [AdvDO: Realistic Adversarial Attacks for Trajectory Prediction](https://arxiv.org/abs/2209.08744). *arXiv 2209.08744*, 2022.  

- [BadNAVer: Exploring Jailbreak Attacks on Vision-and-Language Navigation](https://arxiv.org/abs/2505.12443). *arXiv 2505.12443*, 2025.  

- [Malicious Path Manipulations via Exploitation of Representation Vulnerabilities of Vision-Language Navigation Systems](https://arxiv.org/abs/2407.07392). IROS, 2024.  

- [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587). *ICCV*, 2025.  

- [AdvGrasp: Adversarial Attacks on Robotic Grasping from a Physical Perspective](https://arxiv.org/abs/2507.09857). *arXiv 2507.09857*, 2025.  

- [Adversarial Attacks on Robotic Vision-Language-Action Models](https://arxiv.org/abs/2506.03350). *arXiv 2506.03350*, 2025.  

- [Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21663). *arXiv 2511.21663*, 2025.  

- [When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203). *arXiv 2511.16203*, 2025.  

- [Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237). *arXiv 2510.13237*, 2025.  

- [FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models](https://arxiv.org/abs/2509.19870). *arXiv 2509.19870*, 2025.  

- [RedVLA: Physical Red Teaming for Vision-Language-Action Models](https://arxiv.org/abs/2604.22591). *arXiv 2604.22591*, 2026.

- [When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192). CVPR 2026.


<!-- with additional risks to perception

- [Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos](https://arxiv.org/abs/2502.06789). *arXiv 2502.06789*, 2025.  

- [Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation](https://arxiv.org/abs/2503.04261). *arXiv 2503.04261*, 2025.  

- [Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches](https://arxiv.org/abs/2108.13162). *arXiv 2108.13162*, 2021.  

- [3D Gaussian Splatting-Driven Multi-View Robust Physical Adversarial Camouflage Generation](https://arxiv.org/abs/2409.10574). *arXiv 2409.10574*, 2024.  

- [CP-Freezer: Latency Attacks against Vehicular Cooperative Perception](https://arxiv.org/abs/2401.04577). *arXiv 2401.04577*, 2024.  

- [Towards Powerful and Practical Patch Attacks for 2D Object Detection in Autonomous Driving](https://arxiv.org/abs/2508.10600). *arXiv 2508.10600*, 2025.  

- [MAGIC: Mastering Physical Adversarial Generation in Context through Collaborative LLM Agents](https://arxiv.org/abs/2507.08009). *arXiv 2507.08009*, 2025.  

- [Securing the Lane: Defences against Patch Attacks on Autonomous Vehicle’s Lane Detection](https://doi.org/10.1109/EuroSPW67616.2025.00039). *IEEE EuroS&P Workshops*, 2025.  

- [DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches](https://arxiv.org/abs/2506.16690). *arXiv 2506.16690*, 2025.   -->

<summary>Defenses</summary>

- [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587). *ICCV*, 2025.  

- [Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237). *arXiv 2510.13237*, 2025.  

- [RedVLA: Physical Red Teaming for Vision-Language-Action Models](https://arxiv.org/abs/2604.22591). *arXiv 2604.22591*, 2026.

- [When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192). CVPR 2026.

</details>

<details open>
<summary>(b) Backdoor attack risks & defenses</summary>

<summary>Attack risks</summary>

- [Everyday Object Meets Vision-and-Language Navigation Agent via Backdoor](https://proceedings.neurips.cc/paper_files/paper/2024/hash/58e6c003c9fb3992265005ff6aef1913-Abstract-Conference.html). *NeurIPS*, 2024.  

- [AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149). *arXiv 2511.12149*, 2025.  

- [Goal-Oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269). *arXiv 2510.09269*, 2025.  

- [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640). *arXiv 2505.16640*, 2025.  

- [DropVLA: An Action-Level Backdoor Attack on Vision–Language–Action Models](https://arxiv.org/abs/2510.10932). *arXiv 2510.10932*, 2025.

<!-- with additional risks to perception

- [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858). *arXiv 2203.00858*, 2022.  

-->

<summary>Defenses</summary>

- [AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149). *arXiv 2511.12149*, 2025.  

- [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640). *arXiv 2505.16640*, 2025.  


</details>
</details>

<details open>
<summary>2) Plan-Level Defense</summary>

</details>

<summary>Attack risks</summary>

May include semantic jailbreaking,

- [SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments](https://arxiv.org/abs/2412.00114). *arXiv 2412.00114*, 2024.

- [Towards Transferable Attacks Against Vision-LLMs in Autonomous Driving with Typography](https://arxiv.org/abs/2405.14169). *arXiv 2405.14169*, 2024.  

- [Exploring the Robustness of Decision-Level through Adversarial Attacks on LLM-Based Embodied Models](https://arxiv.org/abs/2405.19802). *arXiv 2405.19802*, 2024.  

- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691). *arXiv 2410.13691*, 2024.  

- [BadRobot: Jailbreaking Embodied LLMs in the Physical World](https://arxiv.org/abs/2407.20242). *arXiv 2407.20242*, 2024.

- [PhysPatch: A Physically Realizable and Transferable Adversarial Patch Attack for Multimodal Large Language Models-based Autonomous Driving Systems](https://arxiv.org/abs/2508.05167). *arXiv 2508.05167*, 2025.  

or backdooring,

- [Physical Backdoor Attack Can Jeopardize Driving with Vision-Large-Language Models](https://arxiv.org/abs/2404.12916). *arXiv 2404.12916*, 2024.  

- [Compromising Embodied Agents with Contextual Backdoor Attacks](https://arxiv.org/abs/2408.02882). *arXiv 2408.02882*, 2024.  

- [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774). *arXiv 2405.20774*, 2024.  

- [TrojanRobot: Physical-World Backdoor Attacks Against VLM-based Robotic Manipulation](https://arxiv.org/abs/2411.11683). *arXiv 2411.11683*, 2024.  

<summary>Defenses</summary>

- [SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments](https://arxiv.org/abs/2412.00114). *arXiv 2412.00114*, 2024.

- [Preventing Robotic Jailbreaking via Multimodal Domain Adaptation](https://arxiv.org/abs/2509.23281). arXiv, 2025.

- [TrojanRobot: Physical-World Backdoor Attacks Against VLM-based Robotic Manipulation](https://arxiv.org/abs/2411.11683). *arXiv 2411.11683*, 2024.  

- [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774). ICLR, 2025.  

</details>


</details>

---

<details open>
<summary><b>Validation-Time Safety</b></summary>

<details open>
<summary><i>A. General Safety Benchmarks</i></summary>

Evaluate general unsafe action recognition and avoidance (top-down).

- [WaymoQA: A Multi-View Visual Question Answering Dataset for Safety-Critical Reasoning in Autonomous Driving](https://arxiv.org/abs/2511.20022). *arXiv 2511.20022*, 2025.  

- [WOMD-Reasoning: A Large-Scale Dataset and Benchmark for Interaction and Intention Reasoning in Driving](https://arxiv.org/abs/2407.04281). *arXiv 2407.04281*, 2024.  

- [Can AI Perceive Physical Danger and Intervene?](https://arxiv.org/abs/2509.21651). *arXiv 2509.21651*, 2025.  

- [SciFi-Benchmark: Leveraging Science Fiction to Improve Robot Behavior](https://arxiv.org/abs/2503.10706). *arXiv 2503.10706*, 2025.  

- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663). *arXiv 2503.08663*, 2025.  

- [WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-Tail Scenarios](https://arxiv.org/abs/2406.14547). *arXiv 2406.14547*, 2024.  

- [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-to-End Autonomous Driving](https://arxiv.org/abs/2406.03877). *arXiv 2406.03877*, 2024.  

- [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349). *arXiv 2406.15349*, 2024.  

- [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535). *arXiv 2604.08535*, 2026.

- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480). NeurIPS Spotlight, 2025.

- [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2510.13412). *arXiv 2510.13412*, 2025.  

- [Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models](https://arxiv.org/abs/2409.13174). *arXiv 2409.13174*, 2024.  

- [SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-Based Robotic Task Planning](https://arxiv.org/abs/2503.06892). *arXiv 2503.06892*, 2025.  

- [ANNIE: Be Careful of Your Robots](https://arxiv.org/abs/2509.03383). *arXiv 2509.03383*, 2025.  

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891). *arXiv 2512.11891*, 2025.  

- [AgentSafe: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.  

- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178). *arXiv 2412.13178*, 2024.  

- [Social-LLaVA: Enhancing Social Robot Navigation through Human-Language Reasoning](https://arxiv.org/abs/2501.09024). *arXiv 2501.09024*, 2025.  

</details>

<details open>
<summary><i>B. Robustness Benchmarks</i></summary>

Evaluate resilience to perturbed inputs and reasoning failures (stress-test).

- [Embodied Red Teaming for Auditing Robotic Foundation Models](https://arxiv.org/abs/2411.18676). *arXiv 2411.18676*, 2024.  

- [Predictive Red Teaming: Breaking Policies Without Breaking Robots](https://arxiv.org/abs/2502.06575). *arXiv 2502.06575*, 2025.  

- [Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities](https://arxiv.org/abs/2507.13019). *ICCV*, 2025.  

- [Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies](https://arxiv.org/abs/2603.12510). *arXiv 2603.12510*, 2026.  

</details>

<details open>
<summary><i>C. Situational Benchmarks</i></summary>

Evaluate safety under context-dependent and embodied scenarios (bottom-up).

- [FREA: Feasibility-Guided Generation of Safety-Critical Scenarios with Reasonable Adversariality](https://arxiv.org/abs/2406.02983). *arXiv 2406.02983*, 2024.  


- [DiffScene: Diffusion-Based Safety-Critical Scenario Generation for Autonomous Vehicles](https://ojs.aaai.org/index.php/AAAI/article/view/30364). *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)*, 2025.  

- [Learning to Collide: An Adaptive Safety-Critical Scenarios Generating Method](https://arxiv.org/abs/2003.01197). *arXiv 2003.01197*, 2020.  

- [Evaluating Gemini Robotics Policies in a Veo World Simulator](https://arxiv.org/abs/2512.10675). *arXiv 2512.10675*, 2025.  

</details>


</details>


## Related Projects

- [Awesome-Large-Model-Safety](https://github.com/xingjunm/Awesome-Large-Model-Safety) -- Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety


