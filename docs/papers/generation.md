# 3. Hard-Constrained Generation

[Home](../../README.md#browse-papers) · [Related Surveys](surveys.md) · [Hard-Constrained Prediction](prediction.md) · [Applications and Evaluation](applications.md)

Paper lists follow the companion survey. Papers may appear in multiple categories. General one-step model foundations are marked as background.

## Contents

- [3.1 Direct Generation](#31-direct-generation)
- [3.2 Autoregressive Generation](#32-autoregressive-generation)
- [3.3 Diffusion and Flow-Based Generation](#33-diffusion-and-flow-based-generation)
  - [3.3.1 Training-Based Methods](#331-training-based-methods)
  - [3.3.2 Geometry-Aware Sampling](#332-geometry-aware-sampling)
    - [3.3.2.1 Reflected Sampling](#3321-reflected-sampling)
    - [3.3.2.2 Manifold Sampling](#3322-manifold-sampling)
  - [3.3.3 Constraint Parameterization](#333-constraint-parameterization)
  - [3.3.4 Guidance, Correction, and Search](#334-guidance-correction-and-search)
    - [3.3.4.1 Continuous Guidance](#3341-continuous-guidance)
    - [3.3.4.2 Continuous Correction](#3342-continuous-correction)
    - [3.3.4.3 Discrete Guidance, Decoding, and Repair](#3343-discrete-guidance-decoding-and-repair)
    - [3.3.4.4 Candidate and Path Search](#3344-candidate-and-path-search)
    - [3.3.4.5 Bridge-Based Sampling](#3345-bridge-based-sampling)
  - [3.3.5 Combining Mechanisms](#335-combining-mechanisms)

## 3.1 Direct Generation

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | one-step consistency map; background | <a href="https://proceedings.mlr.press/v202/song23a.html">Consistency Models</a> | ICML | 2023 |
| 2 | FlowPG feasible-action normalizing flows | <a href="https://openreview.net/forum?id=p1gzxzJ4Y5">FlowPG: Action-Constrained Policy Gradient with Normalizing Flows</a> | NeurIPS | 2023 |
| 3 | mean-flow one-step generator; background | <a href="https://openreview.net/forum?id=uWj4s7rMnR">Mean Flows for One-step Generative Modeling</a> | NeurIPS | 2025 |
| 4 | shortcut one-step diffusion; background | <a href="https://openreview.net/forum?id=OlzB6LnXcS">One Step Diffusion via Shortcut Models</a> | ICLR | 2025 |
| 5 | physics-informed diffusion distillation | <a href="https://proceedings.mlr.press/v306/zhang26gl.html">Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation</a> | ICML | 2026 |
| 6 | PMosFM one-step feasible-coordinate transport | <a href="https://arxiv.org/abs/2609.40287">PMosFM: Preconditioned Manifold Matching for One-Step Physics-Constrained Generation</a> | arXiv | 2026 |
| 7 | physics-informed generator distillation | <a href="https://arxiv.org/abs/2602.03627">Ultra Fast PDE Solving via Physics Guided Few-step Diffusion</a> | arXiv | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 3.2 Autoregressive Generation

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | constrained beam search | <a href="https://aclanthology.org/D17-1098/">Guided open vocabulary image captioning with constrained beam search</a> | EMNLP | 2017 |
| 2 | lexically constrained decoding | <a href="https://aclanthology.org/N18-1119/">Fast lexically constrained decoding with dynamic beam allocation for neural machine translation</a> | NAACL | 2018 |
| 3 | Metropolis-Hastings constrained text sampling | <a href="https://arxiv.org/abs/1811.10996">CGMH: Constrained Sentence Generation by Metropolis-Hastings Sampling</a> | AAAI | 2019 |
| 4 | gradient-guided language generation | <a href="https://arxiv.org/pdf/1912.02164">Plug and play language models: A simple approach to controlled text generation</a> | arXiv | 2019 |
| 5 | predicate-logic constrained decoding | <a href="https://arxiv.org/abs/2010.12884">NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints</a> | NAACL | 2021 |
| 6 | gradient-based constrained LM sampling | <a href="https://arxiv.org/abs/2205.12558">Gradient-Based Constrained Sampling from Language Models</a> | arXiv | 2022 |
| 7 | grammar-constrained decoding | <a href="https://arxiv.org/abs/2305.13971">Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning</a> | EMNLP | 2023 |
| 8 | logical-circuit constrained resampling | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/d98ce7a82af78cd02968e79ea3fe89e8-Abstract-Conference.html">Controllable Generation via Locally Constrained Resampling</a> | ICLR | 2025 |
| 9 | weighted rejection and sequential Monte Carlo | <a href="https://openreview.net/forum?id=3BmPSFAdq3">Fast Controlled Generation from Language Models with Adaptive Weighted Rejection Sampling</a> | COLM | 2025 |
| 10 | ChopChop semantic prefix pruning | <a href="https://doi.org/10.1145/3776708">ChopChop: A Programmable Framework for Semantically Constraining the Output of Language Models</a> | POPL | 2026 |
| 11 | CARS invalid-prefix adaptive rejection | <a href="https://proceedings.mlr.press/v306/parys26a.html">Constrained Adaptive Rejection Sampling</a> | ICML | 2026 |
| 12 | global decoding with completion probabilities | <a href="https://proceedings.mlr.press/v306/dang26c.html">Mitigating Bias in Locally Constrained Decoding via Tractable Proposals</a> | ICML | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 3.3 Diffusion and Flow-Based Generation

### 3.3.1 Training-Based Methods

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | shortcut DDPM fine-tuning | <a href="https://arxiv.org/pdf/2301.13362">Optimizing ddpm sampling with shortcut fine-tuning</a> | arXiv | 2023 |
| 2 | adjoint-matching fine-tuning | <a href="https://arxiv.org/pdf/2409.08861">Adjoint matching: Fine-tuning flow and diffusion generative models with memoryless stochastic optimal control</a> | arXiv | 2024 |
| 3 | dual constrained training | <a href="https://openreview.net/forum?id=Es2Ey2tGmM">Constrained diffusion models via dual training</a> | NeurIPS | 2024 |
| 4 | entropy-regularized diffusion control | <a href="https://arxiv.org/pdf/2402.15194">Fine-tuning of continuous-time diffusion models as entropy-regularized control</a> | arXiv | 2024 |
| 5 | generative calibration | <a href="https://arxiv.org/pdf/2510.10020">Calibrating Generative Models</a> | arXiv | 2025 |
| 6 | constrained diffusion composition | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/1af991de2d4c4e679bcc5d9e23ac6bae-Paper-Conference.pdf">Composition and alignment of diffusion models using constrained learning</a> | NeurIPS | 2025 |
| 7 | DDAT training / denoising trajectory projection | <a href="https://www.roboticsproceedings.org/rss21/p078.html">DDAT: Diffusion Policies Enforcing Dynamically Admissible Robot Trajectories</a> | RSS | 2025 |
| 8 | hard linear-equality constrained DGM | <a href="https://arxiv.org/abs/2502.05416">Deep Generative Models with Hard Linear Equality Constraints</a> | arXiv | 2025 |
| 9 | physics-constrained flow fine-tuning | <a href="https://arxiv.org/pdf/2508.09156">Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems</a> | arXiv | 2025 |
| 10 | physics-informed diffusion training | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/096347b4efc264ae7f07742fea34af1f-Abstract-Conference.html">Physics-Informed Diffusion Models</a> | ICLR | 2025 |
| 11 | softly constrained denoiser | <a href="https://arxiv.org/pdf/2512.14980">Softly Constrained Denoisers for Diffusion Models</a> | arXiv | 2025 |
| 12 | unified diffusion bridge | <a href="https://arxiv.org/pdf/2502.05749">UniDB: A Unified Diffusion Bridge Framework via Stochastic Optimal Control</a> | arXiv | 2025 |
| 13 | dual-conditioned score model; ensemble inference | <a href="https://arxiv.org/abs/2606.17192">Constrained Diffusion Models with Primal-Dual Inference</a> | arXiv | 2026 |
| 14 | sequential augmented-Lagrangian flow fine-tuning | <a href="https://proceedings.mlr.press/v306/gutjahr26a.html">Constrained Flow Optimization via Sequential Fine-Tuning for Molecular Design</a> | ICML | 2026 |
| 15 | FM-DD endpoint distance; FM-RE membership queries | <a href="https://openreview.net/forum?id=OR4h9WPJhV">Constraint-Aware Flow Matching via Randomized Exploration</a> | TMLR | 2026 |
| 16 | decision-aligned flow training | <a href="https://arxiv.org/pdf/2605.12754">Constraint-Aware Flow Matching: Decision Aligned End-to-End Training for Constrained Sampling</a> | arXiv | 2026 |
| 17 | MBM++ gradient-conditioned residual updates | <a href="https://arxiv.org/abs/2603.06742">Improved Constrained Generation by Bridging Pretrained Generative Models</a> | arXiv | 2026 |
| 18 | rollout-trained sampling guidance | <a href="https://arxiv.org/abs/2607.14398">Integration Matters: Rollout-Based Training for Constrained Diffusion Models</a> | arXiv | 2026 |
| 19 | REPA-P physical supervision of latent features | <a href="https://proceedings.mlr.press/v306/jia26j.html">Learning to Think in Physics: Breaking Shortcut Learning in Scientific Diffusion via Representation Alignment</a> | ICML | 2026 |
| 20 | normal perturbations and final manifold projection | <a href="https://proceedings.mlr.press/v306/keegan26a.html">Manifold-Aware Perturbations for Constrained Generative Modeling</a> | ICML | 2026 |
| 21 | endpoint physics residuals; conflict-free gradients | <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/a57483b394a3654f4317051e4ce3b2b8-Abstract-Conference.html">Physics vs Distributions: Pareto Optimal Flow Matching with Physics Constraints</a> | ICLR | 2026 |
| 22 | physics-informed diffusion distillation | <a href="https://proceedings.mlr.press/v306/zhang26gl.html">Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation</a> | ICML | 2026 |
| 23 | sCM-PINN structure-preserving decoder tuning | <a href="https://doi.org/10.1145/3770855.3819059">Stabilizing Physics-Informed Consistency Models via Structure-Preserving Training</a> | KDD | 2026 |
| 24 | physics-informed generator distillation | <a href="https://arxiv.org/abs/2602.03627">Ultra Fast PDE Solving via Physics Guided Few-step Diffusion</a> | arXiv | 2026 |
| 25 | Flow Expander entropy and verifier fine-tuning | <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/3317577a5bc887afa8bab810bdf31635-Abstract-Conference.html">Verifier-Constrained Flow Expansion for Discovery Beyond the Data</a> | ICLR | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

### 3.3.2 Geometry-Aware Sampling

#### 3.3.2.1 Reflected Sampling

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | barrier/reflected diffusion | <a href="https://arxiv.org/pdf/2304.05364">Diffusion models for constrained domains</a> | arXiv | 2023 |
| 2 | reflection-based diffusion | <a href="https://proceedings.mlr.press/v202/lou23a.html">Reflected diffusion models</a> | ICML | 2023 |
| 3 | Metropolis constrained sampling | <a href="https://openreview.net/forum?id=jzseUq55eP">Metropolis sampling for constrained diffusion models</a> | NeurIPS | 2024 |
| 4 | Reflected flow matching | <a href="https://arxiv.org/pdf/2405.16577">Reflected Flow Matching</a> | arXiv | 2024 |
| 5 | reflected Schrodinger bridge | <a href="https://arxiv.org/pdf/2401.03228">Reflected Schrödinger Bridge for Constrained Generative Modeling</a> | arXiv | 2024 |
| 6 | specular reflected Langevin | <a href="https://arxiv.org/pdf/2510.23985">Score-based constrained generative modeling via Langevin diffusions with boundary conditions</a> | arXiv | 2025 |
| 7 | intrinsic-dimension adaptation in reflected diffusion | <a href="https://arxiv.org/abs/2603.24495">Reflected diffusion models adapt to low-dimensional data</a> | arXiv | 2026 |
| 8 | confined probability-flow ODEs | <a href="https://arxiv.org/abs/2607.28344">Reflected diffusion, no-flux continuity equations and confined Lagrangian flows in bounded domains</a> | arXiv | 2026 |
| 9 | statistical analysis of reflected diffusion | <a href="https://jmlr.org/papers/v27/25-1588.html">Statistical guarantees for denoising reflected diffusion models</a> | JMLR | 2026 |

#### 3.3.2.2 Manifold Sampling

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | Riemannian diffusion | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/123d3e814e257e0781e5d328232ead9b-Abstract-Conference.html">Riemannian diffusion models</a> | NeurIPS | 2022 |
| 2 | Riemannian Schrodinger bridge | <a href="https://arxiv.org/pdf/2207.03024">Riemannian Diffusion Schrödinger Bridge</a> | arXiv | 2022 |
| 3 | manifold score model | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/105112d52254f86d5854f3da734a52b4-Abstract-Conference.html">Riemannian score-based generative modelling</a> | NeurIPS | 2022 |
| 4 | scalable Riemannian diffusion | <a href="https://openreview.net/forum?id=FLTg8uA5xI">Scaling riemannian diffusion models</a> | NeurIPS | 2023 |
| 5 | SE(3) protein diffusion | <a href="https://arxiv.org/pdf/2302.02277">SE(3) diffusion model with application to protein backbone generation</a> | arXiv | 2023 |
| 6 | categorical statistical-manifold flow | <a href="https://openreview.net/forum?id=5fybcQZ0g4">Categorical flow matching on statistical manifolds</a> | NeurIPS | 2024 |
| 7 | Fisher-geometric flow matching | <a href="https://arxiv.org/pdf/2405.14664">Fisher flow matching for generative modeling over discrete data</a> | arXiv | 2024 |
| 8 | Riemannian / general-geometry flow matching | <a href="https://openreview.net/forum?id=g7ohDlTITL">Flow Matching on General Geometries</a> | ICLR | 2024 |
| 9 | Riemannian flow matching for materials | <a href="https://arxiv.org/pdf/2406.04713">FlowMM: Generating materials with Riemannian flow matching</a> | arXiv | 2024 |
| 10 | Metric / geodesic flow matching | <a href="https://openreview.net/forum?id=fE3RqiF4Nx">Metric flow matching for smooth interpolations on the data manifold</a> | NeurIPS | 2024 |
| 11 | manifold diffusion and flow framework | <a href="https://ojs.aaai.org/index.php/AAAI/article/download/29171/30215">Unified Framework for Diffusion Generative Models in SO(3): Applications in Computer Vision and Astrophysics</a> | AAAI | 2024 |
| 12 | Stiefel flow matching for moment constraints | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/35fdecdf8861bc15110d48fbec3193cf-Paper-Conference.pdf">Stiefel Flow Matching for Moment-Constrained Structure Elucidation</a> | ICLR | 2025 |
| 13 | polynomial convergence of Riemannian diffusion | <a href="https://openreview.net/forum?id=lL0FR3UPhZ">Polynomial Convergence of Riemannian Diffusion Models</a> | ICLR | 2026 |
| 14 | total-variation bounds for Riemannian flow matching | <a href="https://arxiv.org/abs/2602.05174">Total Variation Rates for Riemannian Flow Matching</a> | arXiv | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

### 3.3.3 Constraint Parameterization

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | mirror diffusion | <a href="https://openreview.net/forum?id=XPWEtXzlLy">Mirror diffusion models for constrained and watermarked generation</a> | NeurIPS | 2024 |
| 2 | NAMM learned mirror map | <a href="https://arxiv.org/pdf/2406.12816">Neural Approximate Mirror Maps for Constrained Diffusion Models</a> | arXiv | 2024 |
| 3 | Variational flow matching for graphs | <a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/15b780350b302a1bf9a3bd273f5c15a4-Abstract-Conference.html">Variational flow matching for graph generation</a> | NeurIPS | 2024 |
| 4 | polytope flow via ball homeomorphism | <a href="https://arxiv.org/pdf/2503.10232">Flows on convex polytopes</a> | arXiv | 2025 |
| 5 | heavy-tailed mirror flow | <a href="https://arxiv.org/pdf/2510.08929">Mirror flow matching with heavy-tailed priors for generative modeling on convex domains</a> | arXiv | 2025 |
| 6 | DiffeoCFM pullback-metric coordinate transport | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/5616112a0120c15bf7d47a6bccc21bc3-Paper-Conference.pdf">Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry</a> | NeurIPS | 2025 |
| 7 | simplex-to-Euclidean map | <a href="https://arxiv.org/pdf/2510.27480">Simplex-to-Euclidean Bijections for Categorical Flow Matching</a> | arXiv | 2025 |
| 8 | categorical endpoint flow maps | <a href="https://arxiv.org/pdf/2602.12233">Categorical Flow Maps</a> | arXiv | 2026 |
| 9 | gauge flow matching | <a href="https://openreview.net/forum?id=vxq1OnaAMq">Gauge Flow Matching: Efficient Constrained Generative Modeling over General Convex Set and Beyond</a> | ICLR | 2026 |
| 10 | PolyFlow feasible convex-combination updates | <a href="https://proceedings.mlr.press/v306/ma26ar.html">PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update</a> | ICML | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

### 3.3.4 Guidance, Correction, and Search

#### 3.3.4.1 Continuous Guidance

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | MCG manifold-constraint gradient guidance | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/a48e5877c7bf86a513950ab23b360498-Abstract-Conference.html">Improving diffusion models for inverse problems using manifold constraints</a> | NeurIPS | 2022 |
| 2 | FlowGrad generative-ODE gradient control | <a href="https://openaccess.thecvf.com/content/CVPR2023/html/Liu_FlowGrad_Controlling_the_Output_of_Generative_ODEs_With_Gradients_CVPR_2023_paper.html">FlowGrad: Controlling the Output of Generative ODEs with Gradients</a> | CVPR | 2023 |
| 3 | FreeDoM energy-guided conditional sampling | <a href="https://arxiv.org/abs/2303.09833">FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model</a> | arXiv | 2023 |
| 4 | SE(3)-DiffusionFields learned pose costs | <a href="https://doi.org/10.1109/ICRA48891.2023.10161569">Se (3)-diffusionfields: Learning smooth cost functions for joint grasp and motion optimization through diffusion</a> | ICRA | 2023 |
| 5 | universal guidance | <a href="https://arxiv.org/abs/2302.07121">Universal Guidance for Diffusion Models</a> | arXiv | 2023 |
| 6 | trust sampling | <a href="https://openreview.net/forum?id=dJUb9XRoZI">Constrained Diffusion with Trust Sampling</a> | NeurIPS | 2024 |
| 7 | D-Flow differentiation through sampling flows | <a href="https://arxiv.org/abs/2402.14017">D-Flow: Differentiating through Flows for Controlled Generation</a> | ICML | 2024 |
| 8 | gradient guidance for chance-constrained programming | <a href="https://openreview.net/forum?id=Flntl1YwZg">A Gradient Guided Diffusion Framework for Chance Constrained Programming</a> | NeurIPS | 2025 |
| 9 | terminal constrained trajectory optimization | <a href="https://arxiv.org/pdf/2511.08425">HardFlow: Hard-Constrained Sampling for Flow-Matching Models via Trajectory Optimization</a> | arXiv | 2025 |
| 10 | flow-map terminal reward guidance | <a href="https://proceedings.mlr.press/v306/huang26ae.html">How to Guide Your Flow: Few-Step Alignment via Flow Map Reward Guidance</a> | ICML | 2026 |
| 11 | TOCFlow terminal optimal control | <a href="https://arxiv.org/pdf/2601.09474">Terminally constrained flow-based generative models from an optimal control perspective</a> | arXiv | 2026 |

#### 3.3.4.2 Continuous Correction

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | SafeDiffuser barrier constraints during sampling | <a href="https://arxiv.org/abs/2306.00148">SafeDiffuser: Safe Planning with Diffusion Probabilistic Models</a> | arXiv | 2023 |
| 2 | projected diffusion sampling | <a href="https://openreview.net/forum?id=FsdB3I9Y24">Constrained Synthesis with Projected Diffusion Models</a> | NeurIPS | 2024 |
| 3 | ECI extrapolation-correction-interpolation | <a href="https://arxiv.org/pdf/2412.01786">Gradient-free generation for hard-constrained systems</a> | arXiv | 2024 |
| 4 | continuous MAPF projected diffusion | <a href="https://arxiv.org/pdf/2412.17993">Multi-Agent Path Finding in Continuous Spaces with Projected Diffusion Models</a> | arXiv | 2024 |
| 5 | CCFM probabilistic noisy-state correction | <a href="https://arxiv.org/pdf/2509.25157">Chance-constrained Flow Matching for High-Fidelity Constraint-aware Generation</a> | arXiv | 2025 |
| 6 | CoCoGen physical-residual gradient correction | <a href="https://doi.org/10.1137/24m1636071">CoCoGen: Physically Consistent and Conditioned Score-Based Generative Models for Forward and Inverse Problems</a> | SIAM J. Sci. Comput. | 2025 |
| 7 | CPS posterior-mean projection | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/9b01c4a7d3fc49875dad3c13848bcd9e-Paper-Conference.pdf">Constrained Posterior Sampling: Time Series Generation with Hard Constraints</a> | NeurIPS | 2025 |
| 8 | fast constrained sampling | <a href="https://openreview.net/forum?id=3kVM0m60Q5">Fast constrained sampling in pre-trained diffusion models</a> | NeurIPS | 2025 |
| 9 | OLLA constrained Langevin | <a href="https://arxiv.org/pdf/2510.22044">Fast Non-Log-Concave Sampling under Nonconvex Equality and Inequality Constraints with Landing</a> | arXiv | 2025 |
| 10 | LLE inverse-algorithm extrapolation | <a href="https://openreview.net/forum?id=EGYwfs4XhI">Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Linear Extrapolation</a> | NeurIPS | 2025 |
| 11 | CDIM constrained update | <a href="https://openreview.net/forum?id=TYGDG9zEML">Linearly Constrained Diffusion Implicit Models</a> | NeurIPS | 2025 |
| 12 | LoMAP local projection | <a href="https://openreview.net/forum?id=EHG5Iv1mmb">Local Manifold Approximation and Projection for Manifold-Aware Diffusion Planning</a> | ICML | 2025 |
| 13 | Neural SHAKE manifold projection | <a href="https://jcheminf.biomedcentral.com/counter/pdf/10.1186/s13321-025-01053-w">Neural SHAKE: Geometric Constraints in Neural Differential Equations</a> | Journal of Cheminformatics | 2025 |
| 14 | PCFM physics correction | <a href="https://openreview.net/forum?id=cf4etwjY7n">Physics-Constrained Flow Matching: Sampling Generative Models with Hard Constraints</a> | NeurIPS | 2025 |
| 15 | projected multi-robot diffusion | <a href="https://arxiv.org/pdf/2502.03607">Simultaneous multi-robot motion planning with projected diffusion models</a> | arXiv | 2025 |
| 16 | latent proximal correction | <a href="https://openreview.net/forum?id=TrNB08KuHK">Training-Free Constrained Generation With Stable Diffusion Models</a> | NeurIPS | 2025 |
| 17 | collision correction with noise interpolation | <a href="https://eccv.ecva.net/virtual/2026/poster/5969">CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation</a> | ECCV | 2026 |
| 18 | stochastic proximal constrained diffusion with consensus ADMM | <a href="https://openreview.net/forum?id=kkvqVRu2Zy">Constrained Diffusion for Protein Design with Hard Structural Constraints</a> | ICLR | 2026 |
| 19 | Lagrangian dual flows for residual correction | <a href="https://arxiv.org/abs/2607.04513">Constrained Flow Matching via Lagrangian Dual Flows</a> | arXiv | 2026 |
| 20 | DiRecT constrained clean-endpoint solves | <a href="https://arxiv.org/abs/2606.15359">DiRecT: Safe Diffusion-Based Planning via Receding-Horizon Denoising</a> | arXiv | 2026 |
| 21 | landing mechanism | <a href="https://arxiv.org/pdf/2604.17838">Efficient Diffusion Models under Nonconvex Equality and Inequality Constraints via Landing</a> | ICML | 2026 |
| 22 | adaptive projection-budget scheduling | <a href="https://arxiv.org/abs/2605.11214">Enforcing Constraints in Generative Sampling via Adaptive Correction Scheduling</a> | arXiv | 2026 |
| 23 | FAST-DIPS measurement correction | <a href="https://openreview.net/forum?id=voMeZVAkKL">FAST-DIPS: Adjoint-Free Analytic Steps and Hard-Constrained Likelihood Correction for Diffusion-Prior Inverse Problems</a> | ICLR | 2026 |
| 24 | predict-project-renoise sampling | <a href="https://arxiv.org/abs/2601.21033">Predict-Project-Renoise: Sampling Diffusion Models under Hard Constraints</a> | arXiv | 2026 |
| 25 | ProjFlow kinematics-aware endpoint projection | <a href="https://arxiv.org/abs/2602.22742">ProjFlow: Projection Sampling with Flow Matching for Zero-Shot Exact Spatial Motion Control</a> | CVPR | 2026 |
| 26 | constricting barrier-function control | <a href="https://arxiv.org/abs/2602.21429">Provably Safe Generative Sampling with Constricting Barrier Functions</a> | arXiv | 2026 |
| 27 | SafeFlowMatcher CBF correction | <a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning Using Flow Matching with Control Barrier Functions</a> | ICLR | 2026 |
| 28 | split augmented Langevin projection | <a href="https://openreview.net/forum?id=aDJcWNmfce">Strictly Constrained Generative Modeling via Split Augmented Langevin Sampling</a> | ICLR | 2026 |

#### 3.3.4.3 Discrete Guidance, Decoding, and Repair

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | CDD constrained discrete sampling | <a href="https://arxiv.org/pdf/2503.09790">Constrained discrete diffusion</a> | arXiv | 2025 |
| 2 | CTDF mixed-type constraint correction | <a href="https://doi.org/10.1145/3768292.3770358">Constrained Tabular Diffusion for Finance</a> | ICAIF | 2025 |
| 3 | Euclidean / KL neuro-symbolic correction | <a href="https://proceedings.mlr.press/v288/christopher25a.html">Neuro-Symbolic Generative Diffusion Models for Physically Grounded, Robust, and Safe Generation</a> | NeuS | 2025 |
| 4 | discrete diffusion guidance | <a href="https://arxiv.org/abs/2412.10193">Simple Guidance Mechanisms for Discrete Diffusion Models</a> | ICLR | 2025 |
| 5 | TFG-Flow coordinate gradients / categorical Monte Carlo | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/aca042ae71283d25b3d063fc011db9e8-Paper-Conference.pdf">TFG-Flow: Training-free Guidance in Multimodal Generative Flow</a> | ICLR | 2025 |
| 6 | likelihood-ratio discrete jump-rate guidance | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf">Unlocking Guidance for Discrete State-Space Diffusion and Flow Models</a> | ICLR | 2025 |
| 7 | localized feedback for diffusion code repair | <a href="https://arxiv.org/abs/2605.16829">Constrained Code Generation with Discrete Diffusion</a> | arXiv | 2026 |
| 8 | grammar-constrained masked diffusion decoding | <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/a1622fc2f8e37ea5fc696d1c13861c36-Abstract-Conference.html">Constrained Decoding of Diffusion LLMs with Context-Free Grammars</a> | ICLR | 2026 |
| 9 | EPIC memoized grammar completion checks | <a href="https://arxiv.org/abs/2606.00722">EPIC: Efficient and Parallel Inference under CFG Constraints for Diffusion Language Models</a> | arXiv | 2026 |
| 10 | structural-statistic multiplier guidance | <a href="https://arxiv.org/abs/2609.32980">Feasible Flow Matching for Graph Reconstruction via Within-Sampling Primal-Dual Guidance</a> | arXiv | 2026 |
| 11 | MaxSMT graph correction | <a href="https://proceedings.mlr.press/v306/zhang26fh.html">Hard-Constrained Graph Generation with Discrete-Projection Diffusion</a> | ICML | 2026 |
| 12 | LOGDIFF Boolean-circuit score composition | <a href="https://proceedings.mlr.press/v306/alesiani26a.html">Logical Guidance for the Exact Composition of Diffusion Models</a> | ICML | 2026 |
| 13 | primal-dual expected token-budget guidance | <a href="https://arxiv.org/abs/2605.09749">Primal-Dual Guided Decoding for Constrained Discrete Diffusion</a> | arXiv | 2026 |
| 14 | SearchDiff candidate selection and token edits | <a href="https://arxiv.org/abs/2602.02727">Search-Augmented Masked Diffusion Models for Constrained Generation</a> | arXiv | 2026 |

#### 3.3.4.4 Candidate and Path Search

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | SCG rule-loss candidate selection | <a href="https://proceedings.mlr.press/v235/huang24g.html">Symbolic Music Generation with Non-Differentiable Rule Guided Diffusion</a> | ICML | 2024 |
| 2 | SVDD soft value-weighted candidate decoding | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/899af0d66d8850318a20781484416152-Paper-Conference.pdf">Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-based Decoding</a> | NeurIPS | 2025 |
| 3 | TreeG derivative-free sampling-path search | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/6a14c7f9fb3f42645cfa6bd5aa446819-Paper-Conference.pdf">Training-Free Guidance Beyond Differentiability: Scalable Path Steering with Tree Search in Diffusion and Flow Models</a> | NeurIPS | 2025 |

#### 3.3.4.5 Bridge-Based Sampling

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | first-hitting feasible-set absorption | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/ae87d80f5a0f3ee5c5643448f9599d1b-Paper-Conference.pdf">First Hitting Diffusion Models for Generating Manifold, Graph and Categorical Data</a> | NeurIPS | 2022 |
| 2 | constrained diffusion bridge | <a href="https://openreview.net/forum?id=WH1yCa0TbB">Learning Diffusion Bridges on Constrained Domains</a> | ICLR | 2023 |
| 3 | manually bridged diffusion | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/34159">Constrained generative modeling with manually bridged diffusion models</a> | AAAI | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

### 3.3.5 Combining Mechanisms

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | optimization-path-aligned diffusion generation | <a href="https://arxiv.org/abs/2305.18470">Aligning Optimization Trajectories with Diffusion Models for Constrained Design Generation</a> | arXiv | 2023 |
| 2 | constrained diffusion solver warm start | <a href="https://arxiv.org/pdf/2403.05571">Efficient and Guaranteed-Safe Non-Convex Trajectory Optimization with Constrained Diffusion Model</a> | arXiv | 2024 |
| 3 | Constrained Diffusers | <a href="https://arxiv.org/pdf/2506.12544">Constrained diffusers for safe planning and control</a> | arXiv | 2025 |
| 4 | coupled projection for joint diffusion generation | <a href="https://arxiv.org/pdf/2508.10531">Projected Coupled Diffusion for Test-Time Constrained Joint Generation</a> | arXiv | 2025 |
| 5 | endpoint-conditioned GP source; guided flow targets | <a href="https://arxiv.org/abs/2607.14424">ConFlow: Constraints-Guided Learning with Flow Matching for Motion Generation</a> | arXiv | 2026 |
| 6 | decision-aligned flow training | <a href="https://arxiv.org/pdf/2605.12754">Constraint-Aware Flow Matching: Decision Aligned End-to-End Training for Constrained Sampling</a> | arXiv | 2026 |
| 7 | valence generation; charge filter; crystal diffusion | <a href="https://www.nature.com/articles/s43588-026-01037-2">Enhancing materials discovery with valence-constrained design in generative modeling</a> | Nat. Comput. Sci. | 2026 |
| 8 | retrieval-guided diffusion noise optimization | <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Towards_Highly-Constrained_Human_Motion_Generation_with_Retrieval-Guided_Diffusion_Noise_Optimization_CVPR_2026_paper.html">Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization</a> | CVPR | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

[Back to top](#3-hard-constrained-generation) · [All categories](../../README.md#browse-papers)
