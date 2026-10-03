# 2. Hard-Constrained Prediction

[Home](../../README.md#browse-papers) · [Related Surveys](surveys.md) · [Hard-Constrained Generation](generation.md) · [Applications and Evaluation](applications.md)

Paper lists follow the companion survey. Papers may appear in multiple categories.

## Contents

- [2.1 Training-Based Approaches](#21-training-based-approaches)
  - [2.1.1 Soft-Penalty Training](#211-soft-penalty-training)
  - [2.1.2 Lagrangian-Based Training](#212-lagrangian-based-training)
  - [2.1.3 Verification-Guided Training](#213-verification-guided-training)
- [2.2 Structured NN Layers](#22-structured-nn-layers)
  - [2.2.1 Explicit Feasibility Layers](#221-explicit-feasibility-layers)
  - [2.2.2 Equality Completion Layers](#222-equality-completion-layers)
  - [2.2.3 Optimization-Based Layers](#223-optimization-based-layers)
- [2.3 Constraint Parameterization](#23-constraint-parameterization)
  - [2.3.1 Feasible Combinations](#231-feasible-combinations)
  - [2.3.2 Feasible Distributions](#232-feasible-distributions)
  - [2.3.3 Global Feasible-Set Maps](#233-global-feasible-set-maps)
- [2.4 Post-Processing Approaches](#24-post-processing-approaches)
  - [2.4.1 Warm-Start Methods](#241-warm-start-methods)
  - [2.4.2 Projection-Based Correction](#242-projection-based-correction)
  - [2.4.3 Projection-Analogous Correction](#243-projection-analogous-correction)
- [2.5 Hybrid Pipelines](#25-hybrid-pipelines)

## 2.1 Training-Based Approaches

### 2.1.1 Soft-Penalty Training

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | differentiable logical-violation loss | <a href="https://proceedings.mlr.press/v97/fischer19a.html">DL2: Training and Querying Neural Networks with Logic</a> | ICML | 2019 |
| 2 | AC-OPF physics-informed residuals | <a href="https://arxiv.org/pdf/2110.02672">Physics-Informed Neural Networks for AC Optimal Power Flow</a> | arXiv | 2021 |
| 3 | DC-OPF worst-case PINN | <a href="https://doi.org/10.1109/SmartGridComm51999.2021.9632308">Physics-informed neural networks for minimising worst-case violations in DC optimal power flow</a> | SmartGridComm | 2021 |
| 4 | worst-case violation training | <a href="https://arxiv.org/pdf/2212.10930">Minimizing worst-case violations of neural networks</a> | arXiv | 2022 |
| 5 | violation-driven data enrichment | <a href="https://doi.org/10.1109/PowerTech55446.2023.10202770">Enriching neural network training dataset to improve worst-case performance guarantees</a> | PowerTech | 2023 |
| 6 | worst-case AC-OPF guarantees | <a href="https://arxiv.org/pdf/2510.23196">Neural Networks for AC Optimal Power Flow: Improving Worst-Case Guarantees during Training</a> | arXiv | 2025 |

### 2.1.2 Lagrangian-Based Training

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | Lagrangian-dual OPF prediction | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/5403">Predicting AC optimal power flows: Combining deep learning and Lagrangian dual methods</a> | AAAI | 2020 |
| 2 | stochastic augmented-Lagrangian training | <a href="https://arxiv.org/abs/2009.07330">Training Neural Networks under Physical Constraints Using a Stochastic Augmented Lagrangian Approach</a> | arXiv | 2020 |
| 3 | log-barrier constrained training | <a href="https://doi.org/10.23919/EUSIPCO55093.2022.9909927">Constrained deep networks: Lagrangian optimization via log-barrier extensions</a> | EUSIPCO | 2022 |
| 4 | nonconvex constrained learning | <a href="https://doi.org/10.1109/TIT.2022.3187948">Constrained learning with non-convex losses</a> | IEEE TIT | 2023 |
| 5 | resilient constrained learning | <a href="https://openreview.net/forum?id=h0RVoZuUl6">Resilient constrained learning</a> | NeurIPS | 2023 |
| 6 | self-supervised primal-dual learning | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/25520">Self-supervised primal-dual learning for constrained optimization</a> | AAAI | 2023 |
| 7 | near-optimal constrained learning | <a href="https://openreview.net/forum?id=fDaLmkdSKU">Near-Optimal Solutions of Constrained Learning Problems</a> | ICLR | 2024 |
| 8 | functional risk-constrained duality | <a href="https://arxiv.org/pdf/2312.01110">Strong Duality Relations in Nonconvex Risk-Constrained Learning</a> | arXiv | 2024 |
| 9 | augmented-Lagrangian constrained learning | <a href="https://arxiv.org/pdf/2510.20995">AL-CoLe: Augmented Lagrangian for Constrained Learning</a> | arXiv | 2025 |
| 10 | pointwise-constrained OPF learning | <a href="https://arxiv.org/pdf/2510.20777">Learning Optimal Power Flow with Pointwise Constraints</a> | arXiv | 2025 |
| 11 | statistical equality constraints | <a href="https://arxiv.org/pdf/2511.14320">Learning with Statistical Equality Constraints</a> | arXiv | 2025 |
| 12 | Lagrangian-augmented neural network | <a href="https://link.springer.com/content/pdf/10.1007/s00521-026-11880-z.pdf">Enforcing Domain Constraints Through Lagrangian Primal-Dual Learning</a> | Neural Comput. Appl. | 2026 |

### 2.1.3 Verification-Guided Training

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | MIP neural verification | <a href="https://arxiv.org/pdf/1711.07356">Evaluating robustness of neural networks with mixed integer programming</a> | arXiv | 2017 |
| 2 | ReLU stability for verification | <a href="https://arxiv.org/pdf/1809.03008">Training for faster adversarial robustness verification via inducing ReLU stability</a> | arXiv | 2018 |
| 3 | nonlinear-spec verification | <a href="https://arxiv.org/pdf/1902.09592">Verification of non-linear specifications for neural networks</a> | arXiv | 2019 |
| 4 | constraint-limit calibration | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9303017">DeepOPF+: A deep neural network approach for DC optimal power flow for ensuring feasibility</a> | SmartGridComm | 2020 |
| 5 | OPF worst-case certificates | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9302963">Learning optimal power flow: Worst-case guarantees for neural networks</a> | SmartGridComm | 2020 |
| 6 | Beta-CROWN bound propagation | <a href="https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html">Beta-CROWN: Efficient bound propagation with per-neuron split constraints for complete and incomplete neural network verification</a> | NeurIPS | 2021 |
| 7 | offline parameter repair | <a href="https://dl.acm.org/doi/10.1145/3453483.3454064">Provable repair of deep neural networks</a> | PLDI | 2021 |
| 8 | power-system NN verification | <a href="https://doi.org/10.1109/TSG.2020.3009401">Verification of neural network behaviour: Formal guarantees for power system applications</a> | IEEE TSG | 2021 |
| 9 | input-output specification training | <a href="https://doi.org/10.23919/ACC53348.2022.9867571">Learning neural networks under input-output specifications</a> | ACC | 2022 |
| 10 | parameter-level SDP certificate | <a href="https://arxiv.org/abs/2201.00632">Neural Network Training under Semidefinite Constraints</a> | arXiv | 2022 |
| 11 | SDP robustness certificate | <a href="https://doi.org/10.1109/TAC.2020.3046193">Safety verification and robustness analysis of neural networks via quadratic constraints and semidefinite programming</a> | IEEE TAC | 2022 |
| 12 | REASSURE localized patch networks | <a href="https://openreview.net/forum?id=xS8AMYiEav3">Sound and Complete Neural Network Repair with Minimality and Locality Guarantees</a> | ICLR | 2022 |
| 13 | counterexample-guided network repair | <a href="https://proceedings.mlr.press/v202/boetius23a.html">A Robust Optimisation Perspective on Counterexample-Guided Repair of Neural Networks</a> | ICML | 2023 |
| 14 | architecture-preserving repair | <a href="https://dl.acm.org/doi/10.1145/3591238">Architecture-preserving provable repair of deep neural networks</a> | POPL | 2023 |
| 15 | verified preventive constraint tightening | <a href="https://openreview.net/forum?id=QVcDQJdFTG">Ensuring DNN Solution Feasibility for Optimization Problems with Linear Constraints</a> | ICLR | 2023 |
| 16 | POLICE linear enforcement | <a href="https://doi.org/10.1109/ICASSP49357.2023.10096520">POLICE: Provably optimal linear constraint enforcement for deep neural networks</a> | ICASSP | 2023 |
| 17 | provable parameter editing | <a href="https://openreview.net/forum?id=IGhpUd496D">Provable Editing of Deep Neural Networks using Parametric Linear Relaxation</a> | NeurIPS | 2024 |
| 18 | multi-region affine enforcement | <a href="https://arxiv.org/pdf/2502.02434">mPOLICE: Provable Enforcement of Multi-Region Affine Constraints in Deep Neural Networks</a> | arXiv | 2025 |
| 19 | provable input-output specification repair | <a href="https://arxiv.org/abs/2511.07741">Provable Repair of Deep Neural Network Defects by Preimage Synthesis and Property Refinement</a> | CCS | 2025 |
| 20 | hybrid-zonotope safe training | <a href="https://doi.org/10.1109/CDC57313.2025.11312423">Provably-safe neural network training using hybrid zonotope reachability analysis</a> | CDC | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 2.2 Structured NN Layers

### 2.2.1 Explicit Feasibility Layers

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | safe predictor mixture | <a href="https://arxiv.org/abs/2001.11062">Safe predictors for enforcing input-output specifications</a> | arXiv | 2020 |
| 2 | hierarchical label consistency | <a href="https://doi.org/10.1613/jair.1.12850">Multi-Label Classification Neural Networks with Hard Logical Constraints</a> | JAIR | 2021 |
| 3 | forward-pass theory-guided projection | <a href="https://doi.org/10.1016/j.jcp.2021.110624">Theory-Guided Hard Constraint Projection (HCP): A Knowledge-Based Data-Driven Scientific Machine Learning Method</a> | J. Comput. Phys. | 2021 |
| 4 | convex ray-and-scale feasibility layer | <a href="https://doi.org/10.1134/S1064562423701077">A new computationally simple approach for implementing neural networks with output hard constraints</a> | Doklady Mathematics | 2023 |
| 5 | renormalizing constraint layer | <a href="https://jmlr.org/papers/v24/23-0158.html">Hard-constrained deep learning for climate downscaling</a> | JMLR | 2023 |
| 6 | LOOP-LC 2.0 generalized gauge map | <a href="https://arxiv.org/pdf/2311.04838">Toward Rapid, Optimal, and Feasible Power Dispatch through Generalized Neural Mapping</a> | arXiv | 2023 |
| 7 | power-balance and reserve repair layers | <a href="https://doi.org/10.1109/TPWRS.2023.3317352">End-to-end feasible optimization proxies for large-scale economic dispatch</a> | IEEE TPS | 2024 |
| 8 | Hard affine enforcement layer | <a href="https://arxiv.org/pdf/2410.10807">HardNet: Hard-constrained neural networks with universal approximation guarantees</a> | arXiv | 2024 |
| 9 | compiled linear-constraint correction | <a href="https://proceedings.iclr.cc/paper_files/paper/2024/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf">How Realistic Is Your Synthetic Data? Constraining Deep Generative Models for Tabular Data</a> | ICLR | 2024 |
| 10 | star-shaped ray-and-scale feasibility layer | <a href="https://doi.org/10.3390/math12233788">Imposing Star-Shaped Hard Constraints on the Neural Network Output</a> | Mathematics | 2024 |
| 11 | integer rounding and continuous correction | <a href="https://arxiv.org/pdf/2410.11061">Learning to optimize for mixed-integer non-linear programming with feasibility guarantees</a> | arXiv | 2024 |
| 12 | KKT-hPINN closed-form equality projection | <a href="https://arxiv.org/abs/2402.07251">Physics-Informed Neural Networks with Hard Linear Equality Constraints</a> | arXiv | 2024 |
| 13 | adaptive constraint correction | <a href="https://arxiv.org/abs/2505.24579v2">Adaptive Correction for Ensuring Conservation Laws in Neural Operators</a> | arXiv | 2025 |
| 14 | compiled disjunctive-constraint correction | <a href="https://proceedings.iclr.cc/paper_files/paper/2025/hash/47360925c45a166c96f652589265dee9-Abstract-Conference.html">Beyond the Convexity Assumption: Realistic Tabular Data Generation under Quantifier-Free Real Linear Constraints</a> | ICLR | 2025 |
| 15 | safe-network decision rules | <a href="https://papers.neurips.cc/paper_files/paper/2025/hash/975a1a8e86e72c148aa2152243953064-Abstract-Conference.html">Enforcing Hard Linear Constraints in Deep Learning Models with Decision Rules</a> | NeurIPS | 2025 |
| 16 | CAffNet / CAffine layer | <a href="https://arxiv.org/pdf/2605.24437">CAffNet: Hard Constraint-Affine Neural Networks</a> | arXiv | 2026 |
| 17 | autoencoder-based projection | <a href="https://openreview.net/forum?id=dVlkUtsyg7">Improving Feasibility via Fast Autoencoder-Based Projections</a> | ICLR | 2026 |
| 18 | CAffNet-Lite CBF-by-construction controller | <a href="https://arxiv.org/abs/2605.26534">Learning Safe-by-Design Neural Network Controllers</a> | arXiv | 2026 |
| 19 | hard convex constraint imposition | <a href="https://arxiv.org/abs/2307.08336v2">RAYEN: Imposition of Hard Convex Constraints on Neural Networks</a> | arXiv | 2026 |
| 20 | soft-radial candidate transformation | <a href="https://arxiv.org/pdf/2602.03461">Soft-Radial Projection for Constrained End-to-End Learning</a> | arXiv | 2026 |

### 2.2.2 Equality Completion Layers

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | DC-OPF equality reconstruction; optional LP repair | <a href="https://doi.org/10.1109/SmartGridComm.2019.8909795">DeepOPF: Deep neural network for DC optimal power flow</a> | SmartGridComm | 2019 |
| 2 | DC3 completion-correction | <a href="https://openreview.net/forum?id=V1ZHVxJ6dSS">DC3: A learning method for optimization with hard constraints</a> | ICLR | 2021 |
| 3 | bounded AC-OPF prediction; power-flow completion | <a href="https://doi.org/10.1109/JSYST.2022.3201041">DeepOPF: A feasibility-optimized deep neural network approach for AC optimal power flow problems</a> | IEEE Systems Journal | 2023 |
| 4 | reduced-policy hard constraints | <a href="https://arxiv.org/abs/2310.09574">Reduced Policy Optimization for Continuous Control with Hard Constraints</a> | NeurIPS | 2023 |
| 5 | equality-embedded dual OPF | <a href="https://arxiv.org/pdf/2306.06674">Self-supervised equality embedded deep Lagrange dual for approximate constrained optimization</a> | arXiv | 2023 |
| 6 | equality-embedded AL OPF | <a href="https://doi.org/10.1049/rpg2.13048">Equality-embedded Augmented Lagrangian Neural Network for DC Optimal Power Flow</a> | IET RPG | 2024 |

### 2.2.3 Optimization-Based Layers

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | differentiable QP layer | <a href="https://proceedings.mlr.press/v70/amos17a.html">OptNet: Differentiable optimization as a layer in neural networks</a> | ICML | 2017 |
| 2 | declarative optimization layer | <a href="https://arxiv.org/abs/1909.04866">Deep Declarative Networks: A New Hope</a> | arXiv | 2019 |
| 3 | differentiable convex layers | <a href="https://proceedings.neurips.cc/paper/2019/hash/9ce3c52fc54362e22053399d3181c638-Abstract.html">Differentiable convex optimization layers</a> | NeurIPS | 2019 |
| 4 | differentiable SAT-relaxation layer | <a href="https://proceedings.mlr.press/v97/wang19e.html">SATNet: Bridging deep learning and logical reasoning using a differentiable satisfiability solver</a> | ICML | 2019 |
| 5 | MIP-as-layer | <a href="https://doi.org/10.1609/aaai.v34i02.5509">MIPaaL: Mixed Integer Program as a Layer</a> | AAAI | 2020 |
| 6 | DC3 completion-correction | <a href="https://openreview.net/forum?id=V1ZHVxJ6dSS">DC3: A learning method for optimization with hard constraints</a> | ICLR | 2021 |
| 7 | forward-pass differentiable projection | <a href="https://arxiv.org/abs/2111.10785">Differentiable Projection for Constrained Deep Learning</a> | arXiv | 2021 |
| 8 | PROF differentiable projection | <a href="https://dl.acm.org/doi/10.1145/3447555.3464874">Enforcing policy feasibility constraints through differentiable projection for energy optimization</a> | e-Energy | 2021 |
| 9 | F-FPN implicit fixed-point layer | <a href="https://doi.org/10.1186/s13663-021-00706-3">Feasibility-based fixed point networks</a> | Fixed Point Theory Algorithms | 2021 |
| 10 | alternating differentiation | <a href="https://arxiv.org/pdf/2210.01802">Alternating differentiation for optimization layers</a> | arXiv | 2022 |
| 11 | modular implicit differentiation | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html">Efficient and modular implicit differentiation</a> | NeurIPS | 2022 |
| 12 | ProjectNet learned updates with finite Dykstra projection | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/25884">End-to-End Learning for Optimization via Constraint-Enforcing Approximators</a> | AAAI | 2023 |
| 13 | QP warm-start learning | <a href="https://proceedings.mlr.press/v211/sambharya23a.html">End-to-end learning to warm-start for real-time quadratic optimization</a> | L4DC | 2023 |
| 14 | PDE-Constrained-Layer (PDE-CL) | <a href="https://arxiv.org/abs/2207.08675">Learning Differentiable Solvers for Systems with Hard Constraints</a> | ICLR | 2023 |
| 15 | LinSATNet extended Sinkhorn scaling | <a href="https://proceedings.mlr.press/v202/wang23at.html">LinSATNet: The Positive Linear Satisfiability Neural Networks</a> | ICML | 2023 |
| 16 | one-step differentiation | <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/f3716db40060004d0629d4051b2c57ab-Abstract-Conference.html">One-step differentiation of iterative algorithms</a> | NeurIPS | 2023 |
| 17 | differentiable Frank-Wolfe layer | <a href="https://arxiv.org/abs/2308.10806">DFWLayer: Differentiable Frank-Wolfe Optimization Layer</a> | ICLR | 2024 |
| 18 | GLinSAT explicit-autodiff / implicit-differentiation variants | <a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/dd73f39426a03131c38c8d943153d44b-Paper-Conference.pdf">GLinSAT: The general linear satisfiability neural network layer by accelerated gradient descent</a> | NeurIPS | 2024 |
| 19 | learned fixed-point warm start and unrolled rollout | <a href="https://jmlr.org/papers/v25/23-1174.html">Learning to warm-start fixed-point optimization algorithms</a> | JMLR | 2024 |
| 20 | PI-HC-MoE local hard constraints | <a href="https://openreview.net/forum?id=u3dX2CEIZb">Scaling physics-informed hard constraints with mixture-of-experts</a> | ICLR | 2024 |
| 21 | constraint boundary wandering | <a href="https://doi.org/10.1109/TPAMI.2025.3560762">Constraint boundary wandering framework: Enhancing constrained optimization with deep neural networks</a> | IEEE TPAMI | 2025 |
| 22 | DAE-HardNet algebraized constraint projection | <a href="https://arxiv.org/abs/2512.05881">DAE-HardNet: A Physics Constrained Neural Network Enforcing Differential-Algebraic Hard Constraints</a> | arXiv | 2025 |
| 23 | ENFORCE AdaNP projection | <a href="https://arxiv.org/abs/2502.06774">ENFORCE: Nonlinear constrained learning with adaptive-depth neural projection</a> | arXiv | 2025 |
| 24 | ProjNet encapsulated CAD projection with surrogate gradient | <a href="https://arxiv.org/pdf/2510.11227">Enforcing convex constraints in Graph Neural Networks</a> | arXiv | 2025 |
| 25 | feasibility-seeking step | <a href="https://openreview.net/forum?id=oum1txoy1D">FSNet: Feasibility-Seeking Neural Network for Constrained Optimization with Guarantees</a> | NeurIPS | 2025 |
| 26 | T-SKM-Net joint-training unrolling / post-processing variants | <a href="https://arxiv.org/pdf/2512.10461">T-SKM-Net: Trainable Neural Network Framework for Linear Constraint Satisfaction via Sampling Kaczmarz-Motzkin Method</a> | arXiv | 2025 |
| 27 | first-order optimization-layer training | <a href="https://arxiv.org/abs/2512.02494v2">A Fully First-Order Layer for Differentiable Optimization</a> | ICML | 2026 |
| 28 | Deep FlexQP unfolded quadratic subproblems | <a href="https://openreview.net/forum?id=HL3TvE4Afm">Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding</a> | ICLR | 2026 |
| 29 | DisjunctiveNet DNF projection | <a href="https://arxiv.org/abs/2605.30456">DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers</a> | ICML | 2026 |
| 30 | HS-Jacobian projection training | <a href="https://arxiv.org/abs/2605.11526">Efficient and Provably Convergent End-to-End Training of Deep Neural Networks with Linear Constraints</a> | arXiv | 2026 |
| 31 | HardNet++ local-linearization correction | <a href="https://arxiv.org/pdf/2604.19669">HardNet++: Nonlinear Constraint Enforcement in Neural Networks</a> | arXiv | 2026 |
| 32 | LMI-Net differentiable matrix-inequality projection | <a href="https://arxiv.org/pdf/2604.05374">LMI-Net: Linear Matrix Inequality-Constrained Neural Networks via Differentiable Projection Layers</a> | arXiv | 2026 |
| 33 | physics-constrained correction layer | <a href="https://doi.org/10.1016/j.compchemeng.2025.109418">Physics-Informed Neural Networks with Hard Nonlinear Equality and Inequality Constraints</a> | Comput. Chem. Eng. | 2026 |
| 34 | PiNet implicit projection layer | <a href="https://openreview.net/forum?id=EJ680UQeZG">Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers</a> | ICLR | 2026 |
| 35 | ShardNet branch selection and QP projection | <a href="https://arxiv.org/abs/2606.30935">ShardNet: Training Neural Controllers with Hard, Non-Convex Constraints</a> | arXiv | 2026 |
| 36 | SnareNet repair layer | <a href="https://arxiv.org/pdf/2602.09317">SnareNet: Flexible Repair Layers for Neural Networks with Hard Constraints</a> | arXiv | 2026 |
| 37 | unrolled constrained optimization | <a href="https://arxiv.org/pdf/2601.17274">Unrolled Neural Networks for Constrained Optimization</a> | arXiv | 2026 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 2.3 Constraint Parameterization

### 2.3.1 Feasible Combinations

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | activation-space parameterization | <a href="https://openaccess.thecvf.com/content_CVPRW_2020/html/w45/Frerix_Homogeneous_Linear_Inequality_Constraints_for_Neural_Network_Activations_CVPRW_2020_paper.html">Homogeneous linear inequality constraints for neural network activations</a> | CVPRW | 2020 |
| 2 | sample-specific barycentric-coordinate parameterization | <a href="https://arxiv.org/abs/2003.10258">Sample-Specific Output Constraints for Neural Networks</a> | arXiv | 2020 |
| 3 | Vertex Network | <a href="https://proceedings.mlr.press/v144/zheng21a.html">Safe reinforcement learning of control-affine systems with vertex networks</a> | L4DC | 2021 |

### 2.3.2 Feasible Distributions

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | probability-support parameterization | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/c182ec594f38926b7fcb827635b9a8f4-Abstract-Conference.html">Semantic Probabilistic Layers for Neuro-Symbolic Learning</a> | NeurIPS | 2022 |
| 2 | distributions over feasible particles | <a href="https://openreview.net/forum?id=JGO8CvG5S9">Universal Approximation Under Constraints is Possible with Transformers</a> | ICLR | 2022 |
| 3 | PAL constrained polynomial densities | <a href="https://proceedings.mlr.press/v286/kurscheidt25a.html">A Probabilistic Neuro-symbolic Layer for Algebraic Constraint Satisfaction</a> | UAI | 2025 |

### 2.3.3 Global Feasible-Set Maps

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | gauge map from virtual action to safe action | <a href="https://doi.org/10.23919/ACC53348.2022.9867652">Computationally efficient safe reinforcement learning for power systems</a> | ACC | 2022 |
| 2 | Gauge NN / interior-point gauge map | <a href="https://ieeexplore.ieee.org/document/9992871">Safe and efficient model predictive control using neural networks: An interior point approach</a> | CDC | 2022 |
| 3 | gauge map from unit ball | <a href="https://doi.org/10.1109/ACCESS.2023.3285199">Learning to solve optimization problems with hard linear constraints</a> | IEEE Access | 2023 |
| 4 | HoP polar homeomorphism | <a href="https://arxiv.org/pdf/2502.00304">HoP: Homeomorphic Polar Learning for Hard Constrained Optimization</a> | arXiv | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 2.4 Post-Processing Approaches

### 2.4.1 Warm-Start Methods

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | AC-OPF warm start | <a href="https://doi.org/10.1109/MLSP.2019.8918690">Learning warm-start points for AC optimal power flow</a> | MLSP | 2019 |
| 2 | learning-to-warm-start | <a href="https://www.climatechange.ai/papers/neurips2019/1">Warm-starting AC optimal power flow with graph neural networks</a> | NeurIPS Climate Workshop | 2019 |
| 3 | AC-OPF Lagrangian learning | <a href="https://arxiv.org/pdf/2110.01653">Learning to solve the AC optimal power flow via a Lagrangian approach</a> | NAPS | 2022 |
| 4 | QP warm-start learning | <a href="https://proceedings.mlr.press/v211/sambharya23a.html">End-to-end learning to warm-start for real-time quadratic optimization</a> | L4DC | 2023 |
| 5 | learned fixed-point warm start and unrolled rollout | <a href="https://jmlr.org/papers/v25/23-1174.html">Learning to warm-start fixed-point optimization algorithms</a> | JMLR | 2024 |
| 6 | dual-feasible neural warm start | <a href="https://arxiv.org/abs/2605.09382">Learning-Augmented Scalable Linear Assignment Problem Optimization via Neural Dual Warm-Starts</a> | ICML | 2026 |
| 7 | iteration-count-aware warm-start fine-tuning | <a href="https://arxiv.org/abs/2605.11102">Newton&#x27;s Lantern: A Reinforcement Learning Framework for Finetuning AC Power Flow Warm Start Models</a> | arXiv | 2026 |

### 2.4.2 Projection-Based Correction

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | RL-CBF action filtering | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/4213">End-to-end safe reinforcement learning through barrier functions for safety-critical continuous control tasks</a> | AAAI | 2019 |
| 2 | equality reconstruction and LP recovery | <a href="https://doi.org/10.1109/TPWRS.2020.3026379">DeepOPF: A deep neural network approach for security-constrained DC optimal power flow</a> | IEEE TPS | 2021 |

### 2.4.3 Projection-Analogous Correction

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | Wasserstein-based projection | <a href="https://doi.org/10.1137/20M1376790">Wasserstein-Based Projections with Applications to Inverse Problems</a> | SIAM J. Math. Data Sci. | 2022 |
| 2 | homeomorphic projection | <a href="https://proceedings.mlr.press/v202/liang23a.html">Low complexity homeomorphic projection to ensure neural-network Solution feasibility for optimization over (non-) convex set</a> | ICML | 2023 |
| 3 | INN-based homeomorphic projection | <a href="https://jmlr.org/papers/v25/23-1577.html">Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization</a> | JMLR | 2024 |
| 4 | bisection projection | <a href="https://openreview.net/forum?id=HWN9CAfcav">Efficient Bisection Projection to Ensure Neural-Network Solution Feasibility for Optimization over General Set</a> | ICML | 2025 |
| 5 | bisection-based projection | <a href="https://doi.org/10.1145/3679240.3734656">Solving Chance-Constrained AC-OPF Problem by Neural Network with Bisection-Based Projection</a> | e-Energy | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

## 2.5 Hybrid Pipelines

| # | Keywords | Paper | Venue | Year |
|---:|---|---|---|---:|
| 1 | DC3 completion-correction | <a href="https://openreview.net/forum?id=V1ZHVxJ6dSS">DC3: A learning method for optimization with hard constraints</a> | ICLR | 2021 |
| 2 | equality reconstruction and LP recovery | <a href="https://doi.org/10.1109/TPWRS.2020.3026379">DeepOPF: A deep neural network approach for security-constrained DC optimal power flow</a> | IEEE TPS | 2021 |
| 3 | equality-embedded dual OPF | <a href="https://arxiv.org/pdf/2306.06674">Self-supervised equality embedded deep Lagrange dual for approximate constrained optimization</a> | arXiv | 2023 |
| 4 | equality-embedded AL OPF | <a href="https://doi.org/10.1049/rpg2.13048">Equality-embedded Augmented Lagrangian Neural Network for DC Optimal Power Flow</a> | IET RPG | 2024 |
| 5 | AC-OPF feasibility restoration map | <a href="https://doi.org/10.1109/TPWRS.2024.3354733">FRMNet: A Feasibility Restoration Mapping Deep Neural Network for AC Optimal Power Flow</a> | IEEE TPS | 2024 |
| 6 | learned fixed-point warm start and unrolled rollout | <a href="https://jmlr.org/papers/v25/23-1174.html">Learning to warm-start fixed-point optimization algorithms</a> | JMLR | 2024 |
| 7 | ProbHardE2E DPPL | <a href="https://arxiv.org/pdf/2506.07003">End-to-end probabilistic framework for learning with hard constraints</a> | arXiv | 2025 |
| 8 | Caratheodory-style feasible decomposition | <a href="https://openreview.net/forum?id=EPDLFWyNnF">Geometric Algorithms for Neural Combinatorial Optimization with Constraints</a> | NeurIPS | 2025 |

[Back to contents](#contents) · [All categories](../../README.md#browse-papers)

[Back to top](#2-hard-constrained-prediction) · [All categories](../../README.md#browse-papers)
