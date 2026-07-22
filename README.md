<div align="center">

# Towards Human-Centered Safety in Vision-Language-Action Robot Control

### A Survey and Outlook

**A curated reading list for semantic action safety in embodied AI**

[Surveyed Papers](#surveyed-papers) · [Taxonomy](#taxonomy-at-a-glance) · [Related Work](#related-papers) · [Contributing](#contributing)

</div>

---

## Overview

This repository accompanies the survey **“Towards Human-Centered Safety in Vision-Language-Action Robot Control: A Survey and Outlook.”** It organizes research on how vision-language-action (VLA) systems can recognize, reason about, and avoid unsafe behavior throughout the robotics lifecycle.

The collection centers on three complementary stages:

- **Design time:** learning alignment and scaling safety-critical data.
- **Deployment time:** runtime guardrails, out-of-distribution handling, and defenses against attacks.
- **Validation time:** safety benchmarks, robustness stress tests, and situational evaluation.

## Taxonomy at a Glance

| Lifecycle stage | Core question | Topics |
| --- | --- | --- |
| **Design time** | How can safety be learned before deployment? | Control and reasoning alignment, world models, safety-critical data |
| **Deployment time** | How can unsafe actions be detected or corrected online? | Control and task guardrails, OOD safety, adversarial and backdoor defenses |
| **Validation time** | How can safety claims be evaluated systematically? | General benchmarks, robustness evaluation, scenario-based stress testing |

## Related Papers

<details open>
<summary><b>Background surveys, perspectives, and standards</b></summary>

- [A Pathway Study for Future Humanoid Standards](https://www.therobotreport.com/wp-content/uploads/2025/09/IEEE-Humanoid-Report-of-Future-Standards-Development.pdf). *IEEE Robotics and Automation Society*, 2025.  

- [Human-AI Safety: A Descendant of Generative AI and Control Systems Safety](https://arxiv.org/abs/2405.09794). *arXiv 2405.09794*, 2024.  

- [Perceived Safety in Physical Human-Robot Interaction – A Survey](https://arxiv.org/abs/2009.07217). *ACM Computing Surveys*, 2021.  

- [Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems](https://arxiv.org/abs/2405.06624). *arXiv 2405.06624*, 2024. 

- [Action Hallucination in Generative Visual-Language-Action Models](https://arxiv.org/abs/2602.06339). *arXiv 2602.06339*, 2026.  

- [Position: Good Embodied Reward Models Need Bad Behavior Data](https://arxiv.org/abs/2406.06087). *arXiv 2406.06087*, 2024.  

- [Embodied AI: Emerging Risks and Opportunities for Policy Action](https://arxiv.org/abs/2509.00117). *arXiv 2509.00117*, 2025.

- [Beyond Alignment: Why Robotic Foundation Models Need Context-Aware Safety](https://doi.org/10.1126/scirobotics.aef2191). *Science Robotics*, 2026.

</details>


## Surveyed Papers

Expand each lifecycle stage to browse its papers. Some papers appear in more than one category when they contribute to multiple parts of the safety lifecycle.


<details open>
<summary><b>I. Design-Time Safety</b> — learning safe behavior and improving data coverage</summary>

<details open>
<summary><b>A. Learning-Based Alignment</b></summary>

<details open>
<summary><b>Direct Control Alignment</b></summary>

<p>
These methods characterize reactive control safety strategies typically identified as System 1.
</p>

#### Imitation-Driven Safety

These methods learn collision avoidance and goal-reaching behavior from demonstrations. ViNT and NoMaD establish broad navigation priors, while NavDP adds safety-oriented trajectory data and a learned critic. Their strength is scalable reactive control; their limitation is that safety remains bounded by what demonstrations cover.

- [ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846). CoRL, 2023.

- [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896). ICRA, 2024.

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.


#### Control-Constrained Safety

Control-constrained methods introduce explicit penalties, rewards, or intervention signals during learning. They move beyond passive imitation by teaching policies to avoid collisions, respect human proximity, and recover from unsafe states, although the learned constraint is only as reliable as its reward and training coverage.

- [Human-Guided Reinforcement Learning With Sim-to-Real Transfer for Autonomous Navigation](https://ieeexplore.ieee.org/document/10250993). TPAMI, 2023.

- [From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning](https://arxiv.org/abs/2507.22028). ICLR Poster, 2026.

- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480). NeurIPS Spotlight, 2025.

</details>


<details open>
<summary><b>Reasoning-Augmented Control Alignment</b></summary>
<p>
These models augment reactive (System 1) policies with reasoning (System 2) to infer actions based on safety factors and/or predicted outcomes.
</p>

#### Reasoning-Constrained Safety

This line of work makes safety-relevant semantics explicit in intermediate reasoning. Driving models ground traffic objects, rules, styles, and possible hazards, while manipulation and navigation models use feasibility reasoning to reject unsafe actions. Explicit reasoning improves interpretability, but plausible explanations do not by themselves guarantee safe control.

- [Tokenize the World into Object-level Knowledge to Address Long-tail Events in Autonomous Driving](https://arxiv.org/abs/2407.00959). CoRL, 2024.

- [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757). NeurIPS, 2025.

- [Poutine: Vision-Language-Trajectory Pre-Training and Reinforcement Learning Post-Training Enable Robust End-to-End Autonomous Driving](https://arxiv.org/abs/2506.11234). *arXiv 2506.11234*, 2025.

- [StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving](https://arxiv.org/abs/2603.09482). *arXiv 2603.09482*, 2026.

- [SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model](https://arxiv.org/abs/2604.19710). *arXiv 2604.19710*, 2026.

- [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167). *arXiv 2602.08167*, 2026.

- [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://arxiv.org/abs/2602.02459). ICML, 2026.

- [RationalVLA: A Rational Vision-Language-Action Model with Dual System](https://arxiv.org/abs/2506.10826). *arXiv 2506.10826*, 2025.

- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020). *arXiv 2503.20020*, 2025.

#### World-Model-Based Safety

World-model approaches train policies against predicted consequences rather than only immediate actions. Failure data, takeover boundaries, counterfactuals, and latent rollouts help models anticipate collisions and recovery needs. Their central bottleneck is prediction fidelity: an imagined future can only support safety when it preserves the relevant physics and semantics.

- [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720). ECCV, 2024.

- [IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model](https://arxiv.org/abs/2508.06571). *arXiv 2508.06571*, 2025.

- [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063). *arXiv 2603.01063*, 2026.

- [Learning from Mistakes: Post-Training for Driving VLA with Takeover Data](https://arxiv.org/abs/2603.14972). *arXiv 2603.14972*, 2026.

- [Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models](https://arxiv.org/abs/2603.06049). *CVPR Findings*, 2026.

- [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2512.24426). CVPR, 2026.


#### Hybrid Approaches

Hybrid methods couple structured reasoning with learned control scores or world models. This combination can connect causal explanations to trajectory selection, but errors may still propagate across the reasoning-to-control interface.

- [Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail](https://arxiv.org/abs/2511.00088). *arXiv 2511.00088*, 2025.

- [Latent Chain-of-Thought World Modeling for End-to-End Driving](https://arxiv.org/abs/2512.10226). *arXiv 2512.10226*, 2025.

</details>

<details open>
<summary><b>Agentic Action Alignment</b></summary>
<p>
These models rely on safety-aligned LLMs or VLMs to select and sequence actions through planners or action APIs that directly interface with robotic systems, enabling agentic System 2 control.
</p>

**Risks**

- [Safety Not Found (404): Hidden Risks of LLM-Based Robotics Decision Making](https://arxiv.org/abs/2407.09179). *arXiv 2407.09179*, 2024.  

- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691). ICRA, 2025.

- [BadRobot: Jailbreaking Embodied LLMs in the Physical World](https://arxiv.org/abs/2407.20242). ICLR, 2025.

- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.


**Alignment and defenses**

Agentic alignment primarily inherits refusal and safety-reasoning capabilities from the underlying multimodal model. Constitutions and physical-danger benchmarks improve high-level judgment, yet reliable deployment still requires verifying that safe reasoning is translated into safe tool calls and robot actions.

- [HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal](https://arxiv.org/abs/2402.04249). ICML, 2024.

- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663). *arXiv 2503.08663*, 2025.

- [Can AI Perceive Physical Danger and Intervene?](https://arxiv.org/abs/2509.21651). *arXiv 2509.21651*, 2025.



</details>
</details>


<details open>
<summary><b>B. Safety Data Coverage</b></summary>

<details open>
<summary><b>Safety-Critical Data Sampling</b></summary>

Sampling methods concentrate limited training and evaluation budgets on rare, diverse, or high-impact events. They improve efficiency near the safety boundary, but cannot recover hazards that were never observed or reliably represented in deployment logs.

- [SSE: Multimodal Semantic Data Selection and Enrichment for Industrial-scale Data Assimilation](https://arxiv.org/abs/2409.13860). KDD, 2025.

- [Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems](https://arxiv.org/abs/2604.08366). *arXiv 2604.08366*, 2026.

- [Unsupervised Discovery of Failure Taxonomies from Deployment Logs](https://arxiv.org/abs/2506.06570). *arXiv 2506.06570*, 2025.

</details>

<details open>
<summary><b>Safety-Critical Data Generation</b></summary>

Generation methods create failures and long-tail hazards that are costly or unsafe to collect in the real world. Scripted simulation offers control, while neural world models offer scale and diversity; both depend on whether the generated scenarios preserve the causal factors that make real behavior unsafe.

Simulation-based strategies collect data through scripted motions:

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.

- [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642). *arXiv 2510.01642*, 2025.

- [Avoid Everything: Model-Free Collision Avoidance with Expert-Guided Fine-Tuning](https://proceedings.mlr.press/v270/fishman25a.html). CoRL, 2025.

Other methods construct augmented environments that expose models to rare but physically plausible hazards through neural world modeling:

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
<summary><b>II. Deployment-Time Safety</b> — monitoring, filtering, and intervention at runtime</summary>

<details open>
<summary><b>A. Action Safeguards</b></summary>

<details open>
<summary><b>1. Control-Level Safeguards</b></summary>

These safety filters check predicted robot controls against explicit constraints, apply corrections when needed, and select safely executable actions.

<details open>
<summary><b>a. Control-Theoretic Filtering</b></summary>

#### Reachability-Based Filters

Reachability filters ask whether a proposed goal, trajectory, or action can remain inside a safe set. The papers progress from geometric collision avoidance toward latent and runtime-parameterized safety concepts, trading stronger coverage for greater dependence on learned state representations.

- [From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies](https://arxiv.org/abs/2511.06385). *arXiv 2511.06385*, 2025.  

- [Robots That Suggest Safe Alternatives](https://arxiv.org/abs/2409.09883). *arXiv 2409.09883*, 2024.  

- [Generalizing Safety Beyond Collision-Avoidance via Latent-Space Reachability Analysis](https://arxiv.org/abs/2502.00935). *arXiv 2502.00935*, 2025.  

- [Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures](https://arxiv.org/abs/2505.00779). *arXiv 2505.00779*, 2025.  

- [AnySafe: Adapting Latent Safety Filters at Runtime via Safety Constraint Parameterization in the Latent Space](https://arxiv.org/abs/2509.19555). *arXiv 2509.19555*, 2025.  

- [What You Don't Know Can Hurt You: How Well do Latent Safety Filters Understand Partially Observable Safety Constraints?](https://arxiv.org/abs/2510.06492). *arXiv 2510.06492*, 2025.  

- [How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints](https://arxiv.org/abs/2511.18606). *arXiv 2511.18606*, 2025.  


#### Control-Barrier Function Filters

Control-barrier methods convert grounded hazards into local action constraints and minimally modify unsafe commands. They are efficient enough for step-level intervention, but contextual or hidden hazards must first be detected and expressed in a control-compatible form.

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891). *arXiv 2512.11891*, 2025.  

- [Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation](https://arxiv.org/abs/2603.05754). *arXiv 2603.05754*, 2026.

  Handles perceptual blind spots—such as hot objects and reflections—using safety constraints and a runtime safety filter.

- [Contextual Safety Reasoning and Grounding for Open-World Robots](https://arxiv.org/abs/2602.19983). *arXiv 2602.19983*, 2026.

</details>

<details open>
<summary><b>b. Predictive Filtering</b></summary>

#### Value Estimation

Value-based filters sample candidate futures and select the one with the best predicted safety and task outcome. This supports geometric, semantic, and social criteria, although it cannot reject an unsafe outcome that is neither sampled nor recognized by the evaluator.

- [Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification](https://arxiv.org/abs/2510.16281). *arXiv 2510.16281*, 2025.  

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712). *arXiv 2505.08712*, 2025.  

- [From Obstacles to Etiquette: Robot Social Navigation with VLM-Informed Path Selection](https://arxiv.org/abs/2602.09002). *arXiv 2602.09002*, 2026.

<!-- - [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281). *arXiv 2602.12281*, 2026.   -->

#### Neural World Modeling

These methods evaluate imagined rollouts before execution. They broaden filtering to delayed and semantic consequences, but hallucinated objects, missing interactions, or inaccurate dynamics can undermine the safety judgment.

- [From Foresight to Forethought: VLM-in-the-Loop Policy Steering via Latent Alignment](https://arxiv.org/abs/2502.01828). *arXiv 2502.01828*, 2025.  

- [Reimagination with Test-time Observation Interventions: Distractor-Robust World Model Predictions for Visual Model Predictive Control](https://arxiv.org/abs/2506.16565). *arXiv 2506.16565*, 2025.  

- [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918). *arXiv 2311.17918*, 2023.  

</details>
</details>

<details open>
<summary><b>2. Task-Level Guardrail</b></summary>

#### Formal Runtime Verification

Runtime-verification methods encode safety as temporal logic, automata, invariants, or executable predicates. Their decisions are inspectable and can trigger blocking or replanning, but open-world safety requirements are difficult to specify and ground completely.

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

#### Semantic Verification

Semantic verifiers use learned reasoning, affordance checks, constitutions, or predicted consequences when hazards cannot be fully formalized. They cover more contextual risks than fixed rules, while offering weaker guarantees and inheriting the evaluator model's failure modes.

- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.

- [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963). *arXiv 2401.12963*, 2024.  


- [Don't Let Your Robot Be Harmful: Responsible Robotic Manipulation](https://arxiv.org/abs/2411.18289). *arXiv 2411.18289*, 2024.  


</details>

</details>

<details open>
<summary><b>B. OOD Safety</b></summary>

#### OOD Detection

Detection methods treat semantic novelty or uncertainty as evidence that the policy may have left its reliable operating regime. Detection alone is insufficient unless it is connected to a timely fallback, clarification, or human handover.

- [Semantic Anomaly Detection with Large Language Models](https://arxiv.org/abs/2305.11307). *Autonomous Robots*, 2023.  

- [Robots That Ask for Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928). *arXiv 2307.01928*, 2023.  

- [Real-Time Anomaly Detection and Reactive Planning with Large Language Models](https://arxiv.org/abs/2407.08735). *arXiv 2407.08735*, 2024.  

#### OOD-Aware Control Prediction

These methods translate uncertainty into action selection, replanning, or deferral. Their shared challenge is calibration: the robot must distinguish harmless novelty from ambiguity, capability mismatch, and imminent physical risk.

- [Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning](https://arxiv.org/abs/2505.10547). *arXiv 2505.10547*, 2025.  

- [Uncertainty-Aware Latent Safety Filters for Avoiding Out-of-Distribution Failures](https://arxiv.org/abs/2505.00779). *arXiv 2505.00779*, 2025.  

- [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474). *arXiv 2602.22474*, 2026.  


</details>

<details open>
<summary><b>C. Adversarial Safety</b></summary>

<details open>
<summary><b>1. Control-Level Defense</b></summary>

<details open>
<summary><b>a. Adversarial Action Risks and Safety</b></summary>

#### Attack Risks

Adversarial attacks perturb observations, prompts, or representations so that perception errors become unsafe motion. The literature demonstrates increasingly physical and transferable attacks, while evaluations still emphasize task failure more often than direct human or cumulative safety harm.

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

#### Defenses

Current defenses combine adversarial training, representation checks, smoothing, and runtime filtering. They improve robustness to known perturbation families, but evidence remains limited for adaptive attacks operating through closed-loop robot–environment interaction.

- [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587). *ICCV*, 2025.  

- [Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237). *arXiv 2510.13237*, 2025.  

- [RedVLA: Physical Red Teaming for Vision-Language-Action Models](https://arxiv.org/abs/2604.22591). *arXiv 2604.22591*, 2026.

- [When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192). CVPR 2026.

</details>

<details open>
<summary><b>b. Backdoor Action Risks and Safety</b></summary>

#### Attack Risks

Backdoor attacks preserve normal behavior until a visual, semantic, or action-level trigger activates a malicious policy. This makes them difficult to detect with ordinary task metrics and especially dangerous when triggers persist across a long-horizon rollout.

- [Everyday Object Meets Vision-and-Language Navigation Agent via Backdoor](https://proceedings.neurips.cc/paper_files/paper/2024/hash/58e6c003c9fb3992265005ff6aef1913-Abstract-Conference.html). *NeurIPS*, 2024.  

- [AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149). *arXiv 2511.12149*, 2025.  

- [Goal-Oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269). *arXiv 2510.09269*, 2025.  

- [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640). *arXiv 2505.16640*, 2025.  

- [DropVLA: An Action-Level Backdoor Attack on Vision–Language–Action Models](https://arxiv.org/abs/2510.10932). *arXiv 2510.10932*, 2025.

<!-- with additional risks to perception

- [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858). *arXiv 2203.00858*, 2022.  

-->

#### Defenses

Backdoor defenses remain less mature than attack methods. Existing work mainly evaluates trigger robustness or adapts generic filtering, leaving a gap in end-to-end guarantees for physically realizable and multimodal triggers.

- [AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149). *arXiv 2511.12149*, 2025.  

- [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640). *arXiv 2505.16640*, 2025.  


</details>
</details>

<details open>
<summary><b>2. Task-Level Defense</b></summary>

#### Attack Risks

Task-level attacks manipulate intent, context, or long-horizon planning rather than a single control output. An unsafe plan may remain locally plausible at every step, so evaluation must connect instruction semantics and hidden triggers to their eventual physical consequences.

Semantic jailbreaking includes:

- [SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments](https://arxiv.org/abs/2412.00114). *arXiv 2412.00114*, 2024.

- [Towards Transferable Attacks Against Vision-LLMs in Autonomous Driving with Typography](https://arxiv.org/abs/2405.14169). *arXiv 2405.14169*, 2024.  

- [Exploring the Robustness of Decision-Level through Adversarial Attacks on LLM-Based Embodied Models](https://arxiv.org/abs/2405.19802). *arXiv 2405.19802*, 2024.  

- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691). *arXiv 2410.13691*, 2024.  

- [BadRobot: Jailbreaking Embodied LLMs in the Physical World](https://arxiv.org/abs/2407.20242). *arXiv 2407.20242*, 2024.

- [PhysPatch: A Physically Realizable and Transferable Adversarial Patch Attack for Multimodal Large Language Models-based Autonomous Driving Systems](https://arxiv.org/abs/2508.05167). *arXiv 2508.05167*, 2025.  

Backdoor attacks include:

- [Physical Backdoor Attack Can Jeopardize Driving with Vision-Large-Language Models](https://arxiv.org/abs/2404.12916). *arXiv 2404.12916*, 2024.  

- [Compromising Embodied Agents with Contextual Backdoor Attacks](https://arxiv.org/abs/2408.02882). *arXiv 2408.02882*, 2024.  

- [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774). *arXiv 2405.20774*, 2024.  

- [TrojanRobot: Physical-World Backdoor Attacks Against VLM-based Robotic Manipulation](https://arxiv.org/abs/2411.11683). *arXiv 2411.11683*, 2024.  

#### Defenses

Task-level defenses use semantic consistency checks, safe prompting, symbolic constraints, and runtime action verification. Their key challenge is cross-layer fidelity: detecting harmful intent early enough to prevent a coherent-looking plan from becoming unsafe embodied action.

- [SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments](https://arxiv.org/abs/2412.00114). *arXiv 2412.00114*, 2024.

- [Preventing Robotic Jailbreaking via Multimodal Domain Adaptation](https://arxiv.org/abs/2509.23281). arXiv, 2025.

- [TrojanRobot: Physical-World Backdoor Attacks Against VLM-based Robotic Manipulation](https://arxiv.org/abs/2411.11683). *arXiv 2411.11683*, 2024.  

- [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774). ICLR, 2025.  

</details>

</details>

</details>

---

<details open>
<summary><b>III. Validation-Time Safety</b> — benchmarking, stress testing, and safety evidence</summary>

<details open>
<summary><b>A. Safety Benchmarking</b></summary>

Safety benchmarking separates **reasoning-centric evaluation**, which asks whether unsafe actions should be proposed at all, from **control-centric evaluation**, which measures what happens after language and perception are grounded into motion.

#### Reasoning-Centric Evaluation

These benchmarks test hazard understanding, refusal, rule following, and multi-step planning before physical execution. They make semantic failures easier to attribute, but many still represent people mainly as labels or hazards rather than interactive agents with intent and preferences.

- [WaymoQA: A Multi-View Visual Question Answering Dataset for Safety-Critical Reasoning in Autonomous Driving](https://arxiv.org/abs/2511.20022). *arXiv 2511.20022*, 2025.  

- [WOMD-Reasoning: A Large-Scale Dataset and Benchmark for Interaction and Intention Reasoning in Driving](https://arxiv.org/abs/2407.04281). *arXiv 2407.04281*, 2024.  

- [Can AI Perceive Physical Danger and Intervene?](https://arxiv.org/abs/2509.21651). *arXiv 2509.21651*, 2025.  

- [SciFi-Benchmark: Leveraging Science Fiction to Improve Robot Behavior](https://arxiv.org/abs/2503.10706). *arXiv 2503.10706*, 2025.  

- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663). *arXiv 2503.08663*, 2025.  

- [SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-Based Robotic Task Planning](https://arxiv.org/abs/2503.06892). *arXiv 2503.06892*, 2025.

- [A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents](https://arxiv.org/abs/2504.14650). *arXiv 2504.14650*, 2025.

- [AgentSafe: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). *arXiv 2506.14697*, 2025.

- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178). *arXiv 2412.13178*, 2024.

#### Control-Centric Evaluation

Control-centric benchmarks expose unsafe trajectories, contact, rule violations, and failures under distribution shift. Their shared contribution is to separate task completion from safety, although metrics beyond collisions and aggregate success remain uneven.

- [WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-Tail Scenarios](https://arxiv.org/abs/2510.26125). *arXiv 2510.26125*, 2025.

- [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-to-End Autonomous Driving](https://arxiv.org/abs/2406.03877). *arXiv 2406.03877*, 2024.  

- [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349). *arXiv 2406.15349*, 2024.  

- [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535). *arXiv 2604.08535*, 2026.

- [SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks](https://arxiv.org/abs/2606.16953). *arXiv 2606.16953*, 2026.

- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480). NeurIPS Spotlight, 2025.

- [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2510.13412). *arXiv 2510.13412*, 2025.  

- [Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models](https://arxiv.org/abs/2409.13174). *arXiv 2409.13174*, 2024.  

- [ANNIE: Be Careful of Your Robots](https://arxiv.org/abs/2509.03383). *arXiv 2509.03383*, 2025.  

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891). *arXiv 2512.11891*, 2025.  

- [Social-LLaVA: Enhancing Social Robot Navigation through Human-Language Reasoning](https://arxiv.org/abs/2501.09024). *arXiv 2501.09024*, 2025.

- [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447). *arXiv 2604.12447*, 2026.

- [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686). *arXiv 2606.23686*, 2026.

</details>

<details open>
<summary><b>B. Robustness Stress-Testing</b></summary>

Robustness stress-testing actively searches for conditions under which safety criteria fail, complementing fixed benchmarks that measure performance on known cases.

#### Perturbation and Adversarial Testing

These studies alter visual inputs, language instructions, or embodiment conditions to expose brittle grounding and control. A useful stress test should isolate a safety-relevant factor without introducing artifacts that would not occur in deployment.

- [Embodied Red Teaming for Auditing Robotic Foundation Models](https://arxiv.org/abs/2411.18676). *arXiv 2411.18676*, 2024.  

- [Predictive Red Teaming: Breaking Policies Without Breaking Robots](https://arxiv.org/abs/2502.06575). *arXiv 2502.06575*, 2025.  

- [Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities](https://arxiv.org/abs/2507.13019). *ICCV*, 2025.  

- [RoboView-Bias: Benchmarking Visual Bias in Embodied Agents for Robotic Manipulation](https://arxiv.org/abs/2509.22356). *arXiv 2509.22356*, 2025.

- [Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies](https://arxiv.org/abs/2603.12510). *arXiv 2603.12510*, 2026.

#### Safety-Critical Scenario Generation

Scenario-generation methods synthesize rare or counterfactual failures that fixed datasets may miss. Simulation offers controlled feasibility, while video world models offer scalable imagined futures; both require strong physical and semantic fidelity for the discovered failures to be meaningful.

- [FREA: Feasibility-Guided Generation of Safety-Critical Scenarios with Reasonable Adversariality](https://arxiv.org/abs/2406.02983). *arXiv 2406.02983*, 2024.  


- [DiffScene: Diffusion-Based Safety-Critical Scenario Generation for Autonomous Vehicles](https://ojs.aaai.org/index.php/AAAI/article/view/30364). *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)*, 2025.  

- [Learning to Collide: An Adaptive Safety-Critical Scenarios Generating Method](https://arxiv.org/abs/2003.01197). *arXiv 2003.01197*, 2020.  

- [Evaluating Gemini Robotics Policies in a Veo World Simulator](https://arxiv.org/abs/2512.10675). *arXiv 2512.10675*, 2025.  

- [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/abs/2606.00267). *arXiv 2606.00267*, 2026.

</details>


</details>


## Related Projects

- [Awesome-Large-Model-Safety](https://github.com/xingjunm/Awesome-Large-Model-Safety) — resources accompanying *Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety*.

## Contributing

Contributions are welcome. When suggesting a paper, please include its title, canonical URL, venue or arXiv identifier, publication year, and the most relevant category in this taxonomy. Please avoid duplicate entries unless a paper genuinely spans multiple lifecycle stages.

---

<div align="center">

If this collection helps your research, consider starring the repository and sharing relevant new work.

</div>
