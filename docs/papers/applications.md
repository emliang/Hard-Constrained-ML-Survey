# 4. Applications and Evaluation

[Home](../../README.md#browse-papers) · [Related Surveys](surveys.md) · [Hard-Constrained Prediction](prediction.md) · [Hard-Constrained Generation](generation.md)

Paper lists follow the companion survey. Papers may appear in multiple categories.

## Contents

- [4.1 AI for Optimization and Control](#41-ai-for-optimization-and-control)
  - [4.1.1 Optimal Power Flow](#411-optimal-power-flow)
  - [4.1.2 Trajectory Optimization](#412-trajectory-optimization)
- [4.2 Scientific Computing and Discovery](#42-scientific-computing-and-discovery)
  - [4.2.1 Physics-Informed Learning](#421-physics-informed-learning)
  - [4.2.2 Molecular and Material Design](#422-molecular-and-material-design)
- [4.3 Evaluator-Guided Generation](#43-evaluator-guided-generation)

## 4.1 AI for Optimization and Control

### 4.1.1 Optimal Power Flow

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | ML-for-OPF survey | <a href="https://doi.org/10.1109/TPEC48276.2020.9042547">A survey on applications of machine learning for optimal power flow</a> | TPEC | 2020 |
| 2 | fast AC-OPF penalty learning | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9303008">Learning optimal solutions for extremely fast AC optimal power flow</a> | SmartGridComm | 2020 |
| 3 | ML for optimal power flows | <a href="https://doi.org/10.1287/educ.2021.0234">Machine learning for optimal power flows</a> | INFORMS Tutorials | 2021 |
| 4 | projection-aware DC-OPF | <a href="https://doi.org/10.1109/SmartGridComm52983.2022.9961047">Projection-aware Deep Neural Network for DC Optimal Power Flow Without Constraint Violations</a> | SmartGridComm | 2022 |
| 5 | bounded AC-OPF prediction; power-flow completion | <a href="https://doi.org/10.1109/JSYST.2022.3201041">DeepOPF: A feasibility-optimized deep neural network approach for AC optimal power flow problems</a> | IEEE Systems Journal | 2023 |
| 6 | dual-feasible SOC-relaxation proxy | <a href="https://arxiv.org/abs/2310.02969">Dual Conic Proxies for AC Optimal Power Flow</a> | arXiv | 2023 |
| 7 | generative OPF with guarantees | <a href="https://doi.org/10.1109/TPWRS.2022.3212925">Fast optimal power flow with guarantees via an unsupervised generative model</a> | IEEE TPS | 2023 |
| 8 | AC-OPF ML critical review | <a href="https://doi.org/10.3390/en17061381">Advancements and future directions in the application of machine learning to AC optimal power flow: A critical review</a> | Energies | 2024 |
| 9 | OPF state-of-the-art review | <a href="https://doi.org/10.1109/ACCESS.2025.3556168">Optimal Power Flow: A Review of State-of-the-Art Techniques and Future Perspectives</a> | IEEE Access | 2025 |
| 10 | OptNet-embedded OPF proxy | <a href="http://hub.hku.hk/bitstream/10722/350203/1/content.pdf">OptNet-Embedded Data-Driven Approach for Optimal Power Flow Proxy</a> | IEEE TIA | 2025 |
| 11 | bisection-based projection | <a href="https://doi.org/10.1145/3679240.3734656">Solving Chance-Constrained AC-OPF Problem by Neural Network with Bisection-Based Projection</a> | e-Energy | 2025 |
| 12 | LUMINA cross-topology OPF benchmark | <a href="https://arxiv.org/abs/2605.02133">LUMINA: A Grid Foundation Model for Benchmarking AC Optimal Power Flow Surrogate Learning</a> | arXiv | 2026 |
| 13 | projection-aware differentiable layer | <a href="https://doi.org/10.1109/PESIM67009.2026.11438430">MPA-DNN: Projection-Aware Unsupervised Learning for Multi-period DC-OPF</a> | IEEE PES IM | 2026 |

### 4.1.2 Trajectory Optimization

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | training-accounted invariant-set projection | <a href="https://erl.ucsd.edu/ref/Chen_DeepMPC_ACC18.pdf">Approximating Explicit Model Predictive Control Using Constrained Neural Networks</a> | ACC | 2018 |
| 2 | adaptive CBF-QP safety filter | <a href="https://arxiv.org/pdf/1910.00555">Adaptive Safety with Control Barrier Functions</a> | ACC | 2020 |
| 3 | differentiable CBF-QP safety layer | <a href="https://arxiv.org/abs/2111.11277">BarrierNet: A Safety-Guaranteed Layer for Neural Networks</a> | arXiv | 2021 |
| 4 | SCPO weight-space projection | <a href="https://arxiv.org/abs/2512.13788">Constrained Policy Optimization via Sampling-Based Weight-Space Projection</a> | arXiv | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 4.2 Scientific Computing and Discovery

### 4.2.1 Physics-Informed Learning

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | analytic conservation completion layer | <a href="https://arxiv.org/abs/1909.00912">Enforcing Analytic Constraints in Neural Networks Emulating Physical Systems</a> | arXiv | 2019 |
| 2 | linear-operator parameterization | <a href="https://arxiv.org/abs/2002.01600">Linearly Constrained Neural Networks</a> | arXiv | 2020 |
| 3 | training-side constrained optimization | <a href="https://arxiv.org/abs/2102.04626">Physics-Informed Neural Networks with Hard Constraints for Inverse Design</a> | arXiv | 2021 |
| 4 | distance-function boundary construction | <a href="https://doi.org/10.1016/j.cma.2021.114333">Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks</a> | Comput. Methods Appl. Mech. Eng. | 2022 |
| 5 | space-time divergence-free parameterization | <a href="https://arxiv.org/abs/2210.01741">Neural Conservation Laws: A Divergence-Free Perspective</a> | NeurIPS | 2022 |
| 6 | hard-constrained neural fields | <a href="https://openreview.net/forum?id=oO1IreC6Sd">Neural Fields with Hard Constraints of Arbitrary Differential Order</a> | NeurIPS | 2023 |
| 7 | KKT-hPINN closed-form equality projection | <a href="https://arxiv.org/abs/2402.07251">Physics-Informed Neural Networks with Hard Linear Equality Constraints</a> | arXiv | 2024 |
| 8 | flux-divergence conservation architecture | <a href="https://arxiv.org/abs/2608.18148">Flux-form Spatiotemporal Neural Operators for Coarse-Grained Dynamics of Multiscale PDEs</a> | arXiv | 2026 |

### 4.2.2 Molecular and Material Design

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | Riemannian diffusion | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/123d3e814e257e0781e5d328232ead9b-Abstract-Conference.html">Riemannian diffusion models</a> | NeurIPS | 2022 |
| 2 | Riemannian Schrodinger bridge | <a href="https://arxiv.org/pdf/2207.03024">Riemannian Diffusion Schrödinger Bridge</a> | arXiv | 2022 |
| 3 | manifold score model | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/105112d52254f86d5854f3da734a52b4-Abstract-Conference.html">Riemannian score-based generative modelling</a> | NeurIPS | 2022 |
| 4 | scalable Riemannian diffusion | <a href="https://openreview.net/forum?id=FLTg8uA5xI">Scaling riemannian diffusion models</a> | NeurIPS | 2023 |
| 5 | SE(3) protein diffusion | <a href="https://arxiv.org/pdf/2302.02277">SE(3) diffusion model with application to protein backbone generation</a> | arXiv | 2023 |
| 6 | AlphaFold 3 structure prediction | <a href="https://doi.org/10.1038/s41586-024-07487-w">Accurate structure prediction of biomolecular interactions with AlphaFold 3</a> | Nature | 2024 |
| 7 | Riemannian / general-geometry flow matching | <a href="https://openreview.net/forum?id=g7ohDlTITL">Flow Matching on General Geometries</a> | ICLR | 2024 |
| 8 | Riemannian flow matching for materials | <a href="https://arxiv.org/pdf/2406.04713">FlowMM: Generating materials with Riemannian flow matching</a> | arXiv | 2024 |
| 9 | Metric / geodesic flow matching | <a href="https://openreview.net/forum?id=fE3RqiF4Nx">Metric flow matching for smooth interpolations on the data manifold</a> | NeurIPS | 2024 |
| 10 | inorganic material generation | <a href="https://doi.org/10.1038/s41586-025-08628-5">A generative model for inorganic materials design</a> | Nature | 2025 |
| 11 | defect-structure relaxation | <a href="https://openreview.net/forum?id=L3LYjJJoL5">Constrained Diffusion for Accelerated Structure Relaxation of Inorganic Solids with Point Defects</a> | NeurIPS AI4Mat Workshop | 2025 |
| 12 | Neural SHAKE manifold projection | <a href="https://jcheminf.biomedcentral.com/counter/pdf/10.1186/s13321-025-01053-w">Neural SHAKE: Geometric Constraints in Neural Differential Equations</a> | Journal of Cheminformatics | 2025 |
| 13 | stochastic proximal constrained diffusion with consensus ADMM | <a href="https://openreview.net/forum?id=kkvqVRu2Zy">Constrained Diffusion for Protein Design with Hard Structural Constraints</a> | ICLR | 2026 |
| 14 | Gauss-Seidel biomolecular projection | <a href="https://openreview.net/forum?id=sJABnBEYeh">Physically Valid Biomolecular Interaction Modeling with Gauss-Seidel Projection</a> | ICLR | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 4.3 Evaluator-Guided Generation

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | shortcut DDPM fine-tuning | <a href="https://arxiv.org/pdf/2301.13362">Optimizing ddpm sampling with shortcut fine-tuning</a> | arXiv | 2023 |
| 2 | adjoint-matching fine-tuning | <a href="https://arxiv.org/pdf/2409.08861">Adjoint matching: Fine-tuning flow and diffusion generative models with memoryless stochastic optimal control</a> | arXiv | 2024 |
| 3 | entropy-regularized diffusion control | <a href="https://arxiv.org/pdf/2402.15194">Fine-tuning of continuous-time diffusion models as entropy-regularized control</a> | arXiv | 2024 |
| 4 | generative calibration | <a href="https://arxiv.org/pdf/2510.10020">Calibrating Generative Models</a> | arXiv | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

[Back to top](#4-applications-and-evaluation) · [All categories](../../README.md#browse-papers)
