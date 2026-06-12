# Awesome Hard-Constrained Machine Learning

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Survey paper preprint available soon.**

**We welcome missed papers and will keep this repository updated.**

> A reader-facing paper list and guide for hard-constrained machine learning, organized by the logic of the companion survey.

This README follows the survey's structure: preliminaries and evaluation terminology first, then hard-constrained predictive models, hard-constrained generative models, applications and benchmarks, and finally cross-cutting reading guides.

## Contents

- [Awesome Hard-Constrained Machine Learning](#awesome-hard-constrained-machine-learning)
  - [Contents](#contents)
  - [Survey Logic](#survey-logic)
  - [Reading Lens](#reading-lens)
  - [Related Surveys and Foundations](#related-surveys-and-foundations)
    - [Related Surveys](#related-surveys)
    - [Foundations and Preliminaries](#foundations-and-preliminaries)
  - [Part I: Hard-Constrained Predictive Models](#part-i-hard-constrained-predictive-models)
    - [Training-Based Approaches](#training-based-approaches)
    - [Post-Processing and Repair](#post-processing-and-repair)
    - [Structured NN Layers](#structured-nn-layers)
    - [Constraint Parameterization](#constraint-parameterization)
  - [Part II: Hard-Constrained Generative Models](#part-ii-hard-constrained-generative-models)
    - [Push-Forward Generators](#push-forward-generators)
    - [Autoregressive Models](#autoregressive-models)
    - [Diffusion and Flow-Matching Models](#diffusion-and-flow-matching-models)
  - [Applications and Benchmarks](#applications-and-benchmarks)
    - [AI for Optimization](#ai-for-optimization)
    - [AI for Science](#ai-for-science)
    - [Constrained Synthesis](#constrained-synthesis)
  - [Reader Guides and Data](#reader-guides-and-data)
  - [Citation](#citation)
  - [Contributing](#contributing)

## Survey Logic

| Survey section | Reader question | README role |
|---|---|---|
| Preliminaries | What are the model and constraint settings? | Foundation papers and evaluation terminology. |
| Hard-constrained predictive models | How can predictions or decisions be made feasible? | Four method families following Part I of the survey. |
| Hard-constrained generative models | How can valid samples be generated? | Push-forward, autoregressive, and diffusion/flow families. |
| Applications and benchmarks | Where do the claims matter in practice? | Optimization, science, and constrained synthesis examples. |
| Discussion | How should claims be interpreted? | Reading guides for guarantees, trade-offs, and failure modes. |

## Reading Lens

Every paper is easier to compare through four questions.

| Angle | Reader question | What to check |
|---|---|---|
| Constraint satisfaction | What supports feasibility? | Guarantee type, residuals, tolerances, certificates, validity rates. |
| Output utility | Is the constrained output useful? | Accuracy, objective gap, reward, sample quality, diversity, downstream utility. |
| Cost | What is paid for enforcement? | Training overhead, solver calls, repair iterations, sampler steps, latency, memory. |
| Scope and assumptions | Where does the claim apply? | Constraint class, domain, oracle, map validity, solver assumptions, discretization. |

![Evaluation dimensions](figures/evaluation.png)

## Related Surveys and Foundations

### Related Surveys

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| Related surveys and background | <a href="https://doi.org/10.1109/MSP.2017.2693418">Geometric deep learning: going beyond euclidean data</a> | IEEE Signal Processing Magazine | 2017 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2103.16378">End-to-end constrained optimization learning: A survey</a> | arXiv | 2021 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2104.13478">Geometric deep learning: Grids, groups, graphs, geodesics, and gauges</a> | arXiv | 2021 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2103.12828">Learning to optimize: A primer and a benchmark</a> | arXiv | 2021 |
| Related surveys and background | <a href="https://doi.org/10.1016/j.ejor.2020.07.063">Machine learning for combinatorial optimization: a methodological tour d’horizon</a> | EJOR | 2021 |
| Related surveys and background | <a href="https://doi.org/10.1038/s42254-021-00314-5">Physics-informed machine learning</a> | Nat. Rev. Phys. | 2021 |
| Related surveys and background | <a href="https://doi.org/10.1016/j.cor.2021.105400">Reinforcement learning for combinatorial optimization: A survey</a> | COR | 2021 |
| Related surveys and background | <a href="https://doi.org/10.1016/j.ejor.2021.04.032">Machine learning at the service of meta-heuristics for solving combinatorial optimization problems: A state-of-the-art</a> | EJOR | 2022 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2211.08064">Physics-informed machine learning: A survey on problems, methods and applications</a> | arXiv | 2022 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2202.00665">Tutorial on amortized optimization for learning to optimize over continuous domains</a> | arXiv | 2022 |
| Related surveys and background | <a href="https://arxiv.org/pdf/2408.12599">Controllable text generation for large language models: A survey</a> | arXiv | 2024 |
| Related surveys and background | <a href="https://doi.org/10.1613/jair.1.15320">Decision-focused learning: Foundations, state of the art, benchmark and future opportunities</a> | JAIR | 2024 |
| Related surveys and background | <a href="https://dl.acm.org/doi/10.1145/3689037">Physics-informed computer vision: A review and perspectives</a> | ACM CSUR | 2024 |
| Related surveys and background | <a href="https://doi.org/10.3390/ai5030074">Understanding physics-informed neural networks: techniques, applications, trends, and challenges</a> | AI | 2024 |
| Related surveys and background | <a href="https://doi.org/10.1016/j.ejor.2024.03.020">A survey of contextual optimization methods for decision-making under uncertainty</a> | EJOR | 2025 |
| Related surveys and background | <a href="https://doi.org/10.1515/9783111376776-009">Trustworthy optimization learning: a brief overview</a> | Mathematical Optimization for… | 2025 |
| Related surveys and background | <a href="https://doi.org/10.1007/s44379-025-00016-0">When physics meets machine learning: A survey of physics-informed machine learning</a> | Machine Learning for… | 2025 |

### Foundations and Preliminaries

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| neural networks and model foundations | <a href="https://doi.org/10.1016/0893-6080(89)90020-8">Multilayer feedforward networks are universal approximators</a> | Neural networks | 1989 |
| neural networks and model foundations | <a href="https://doi.org/10.1016/S0893-6080(05)80131-5">Multilayer feedforward networks with a nonpolynomial activation function can approximate any function</a> | Neural networks | 1993 |
| constraint classes and optimization theory | Convex optimization | Cambridge university press | 2004 |
| generative/discriminative model foundations | Pattern recognition and machine learning | Springer | 2006 |
| neural networks and model foundations | <a href="https://doi.org/10.1007/11840817_66">Recurrent neural networks are universal approximators</a> | International conference on… | 2006 |
| generative/discriminative model foundations | Probabilistic graphical models: principles and techniques | MIT press | 2009 |
| generative/discriminative model foundations | <a href="https://arxiv.org/pdf/1312.6114">Auto-encoding variational bayes</a> | arXiv | 2013 |
| generative/discriminative model foundations | <a href="https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html">Generative adversarial nets</a> | NeurIPS | 2014 |
| generative/discriminative model foundations | <a href="https://proceedings.mlr.press/v37/rezende15.html">Variational inference with normalizing flows</a> | ICML | 2015 |
| neural networks and model foundations | <a href="https://dl.acm.org/doi/10.1145/3065386">ImageNet classification with deep convolutional neural networks</a> | CACM | 2017 |
| neural networks and model foundations | <a href="https://arxiv.org/pdf/1912.10077">Are transformers universal approximators of sequence-to-sequence functions?</a> | arXiv | 2019 |
| generative/discriminative model foundations | <a href="https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html">Denoising diffusion probabilistic models</a> | NeurIPS | 2020 |
| generative/discriminative model foundations | <a href="https://arxiv.org/pdf/2011.13456">Score-based generative modeling through stochastic differential equations</a> | arXiv | 2020 |
| neural networks and model foundations | <a href="https://proceedings.mlr.press/v125/kidger20a.html">Universal approximation with deep narrow networks</a> | COLT | 2020 |
| neural networks and model foundations | <a href="https://doi.org/10.1016/j.acha.2019.06.004">Universality of deep convolutional neural networks</a> | Applied and computational… | 2020 |
| generative/discriminative model foundations | <a href="https://arxiv.org/pdf/2210.02747">Flow matching for generative modeling</a> | arXiv | 2022 |
| generative/discriminative model foundations | <a href="https://arxiv.org/pdf/2209.03003">Flow straight and fast: Learning to generate and transfer data with rectified flow</a> | arXiv | 2022 |
| neural networks and model foundations | <a href="https://jmlr.org/papers/v23/21-0730.html">Universal approximation of functions on sets</a> | JMLR | 2022 |
| neural networks and model foundations | <a href="https://jmlr.org/papers/v23/21-0716.html">Universal approximation theorems for differentiable geometric deep learning</a> | JMLR | 2022 |
<!-- | ResNet universal approximation | <a href="https://proceedings.mlr.press/v235/liu24am.html">Characterizing ResNet’s Universal Approximation Capability</a> | Proceedings of the Forty-first… | 2024 | -->

## Part I: Hard-Constrained Predictive Models

Predictive methods return decisions, labels, controls, trajectories, or optimization variables that should satisfy constraints.

| Family | Core mechanism | Typical guarantee basis | Main trade-off |
|---|---|---|---|
| Training-based approaches | Put feasibility pressure into training through penalties, barriers, Lagrangians, or safe updates. | Empirical residuals, dual/convergence statements, or safe-update assumptions. | Low inference cost but feasibility may depend on training coverage and assumptions. |
| Post-processing and repair | Correct raw predictions after inference through projection, repair, warm starts, or projection-analogous correction. | Solver tolerance, repair success, correction geometry, or empirical residual checks. | Stronger feasibility evidence but extra inference or correction cost. |
| Structured NN layers | Embed differentiable solvers, completion layers, or fixed-point operators. | KKT/solver conditions, layer validity, tolerance, differentiability assumptions. | Clear mechanism but can be solver-heavy or problem-specific. |
| Constraint parameterization | Parameterize outputs so feasible points are produced directly. | By-construction feasibility under valid parameterization or map assumptions. | Fast inference but coverage and geometry assumptions matter. |

### Training-Based Approaches

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| provable guarantees and verification | <a href="https://arxiv.org/pdf/1711.07356">Evaluating robustness of neural networks with mixed integer programming</a> | arXiv | 2017 |
| provable guarantees and verification | <a href="https://arxiv.org/pdf/1809.03008">Training for faster adversarial robustness verification via inducing relu stability</a> | arXiv | 2018 |
| penalty/adversarial training | <a href="https://doi.org/10.1109/SmartGridComm.2019.8909795">Deepopf: A deep neural network approach for security-constrained dc optimal power flow</a> | 2019 IEEE International… | 2019 |
| RL-CBF. | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/4213">End-to-end safe reinforcement learning through barrier functions for safety-critical continuous control tasks</a> | AAAI | 2019 |
| provable guarantees and verification | <a href="https://arxiv.org/pdf/1902.09592">Verification of non-linear specifications for neural networks</a> | arXiv | 2019 |
| constraint-limit calibration. | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9303017">DeepOPF+: A deep neural network approach for DC optimal power flow for ensuring feasibility</a> | 2020 IEEE International… | 2020 |
| predict-and-reconstruct. | <a href="https://doi.org/10.1109/TPWRS.2020.3026379">Deepopf: A deep neural network approach for security-constrained dc optimal power flow</a> | IEEE TPS | 2020 |
| provable guarantees and verification | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9302963">Learning optimal power flow: Worst-case guarantees for neural networks</a> | 2020 IEEE International… | 2020 |
| penalty/adversarial training | <a href="https://doi.org/10.1109/SmartGridComm47815.2020.9303008">Learning optimal solutions for extremely fast AC optimal power flow</a> | 2020 IEEE International… | 2020 |
| penalty/adversarial training | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/5403">Predicting ac optimal power flows: Combining deep learning and lagrangian dual methods</a> | AAAI | 2020 |
| provable guarantees and verification | <a href="https://doi.org/10.1109/TAC.2020.3046193">Safety verification and robustness analysis of neural networks via quadratic constraints and semidefinite programming</a> | IEEE TAC | 2020 |
| provable guarantees and verification | <a href="https://doi.org/10.1109/TSG.2020.3009401">Verification of neural network behaviour: Formal guarantees for power system applications</a> | IEEE TSG | 2020 |
| penalty/adversarial training | <a href="https://doi.org/10.1109/TCNS.2021.3124283">A convex neural network solver for dcopf with generalization guarantees</a> | IEEE TCNS | 2021 |
| provable guarantees and verification | <a href="https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html">Beta-CROWN: Efficient bound propagation with per-neuron split constraints for complete and incomplete neural network verification</a> | NeurIPS | 2021 |
| provable guarantees and verification | <a href="https://arxiv.org/pdf/2112.08091">Ensuring DNN solution feasibility for optimization problems with convex constraints and its application to DC optimal power flow problems</a> | arXiv | 2021 |
| penalty/adversarial training | <a href="https://arxiv.org/pdf/2110.02672">Physics-Informed Neural Networks for AC Optimal Power Flow</a> | arXiv | 2021 |
| penalty/adversarial training | <a href="https://doi.org/10.1109/SmartGridComm51999.2021.9632308">Physics-informed neural networks for minimising worst-case violations in dc optimal power flow</a> | 2021 IEEE International… | 2021 |
| constraint-aware background. | <a href="https://dl.acm.org/doi/10.1145/3453483.3454064">Provable repair of deep neural networks</a> | Proceedings of the 42nd ACM… | 2021 |
| penalty/adversarial training | <a href="https://doi.org/10.23919/EUSIPCO55093.2022.9909927">Constrained deep networks: Lagrangian optimization via log-barrier extensions</a> | 2022 30th European Signal… | 2022 |
| constrained non-convex learning. | <a href="https://doi.org/10.1109/TIT.2022.3187948">Constrained learning with non-convex losses</a> | IEEE Transactions on Information… | 2022 |
| provable guarantees and verification | <a href="https://doi.org/10.23919/ACC53348.2022.9867571">Learning neural networks under input-output specifications</a> | 2022 American Control Conference… | 2022 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2110.01653">Learning to solve the AC optimal power flow via a lagrangian approach</a> | arXiv | 2022 |
| penalty/adversarial training | <a href="https://arxiv.org/pdf/2212.10930">Minimizing worst-case violations of neural networks</a> | arXiv | 2022 |
| provable guarantees and verification | <a href="https://dl.acm.org/doi/10.1145/3591238">Architecture-preserving provable repair of deep neural networks</a> | Proceedings of the ACM on… | 2023 |
| penalty/adversarial training | <a href="https://doi.org/10.1109/PowerTech55446.2023.10202770">Enriching neural network training dataset to improve worst-case performance guarantees</a> | 2023 IEEE Belgrade PowerTech | 2023 |
| provable guarantees and verification | <a href="https://doi.org/10.1109/ICASSP49357.2023.10096520">POLICE: Provably optimal linear constraint enforcement for deep neural networks</a> | ICASSP 2023-2023 IEEE… | 2023 |
| Lagrangian and primal-dual training | <a href="https://openreview.net/forum?id=h0RVoZuUl6">Resilient constrained learning</a> | NeurIPS | 2023 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2306.06674">Self-supervised equality embedded deep lagrange dual for approximate constrained optimization</a> | arXiv | 2023 |
| self-supervised primal-dual learning. | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/25520">Self-supervised primal-dual learning for constrained optimization</a> | AAAI | 2023 |
| Lagrangian and primal-dual training | <a href="https://hdl.handle.net/1866/33886">Constrained optimization for machine learning: algorithms and applications</a> | PhD thesis | 2024 |
| dual-feasible completion. | <a href="https://openreview.net/forum?id=gN1iKwxlL5">Dual lagrangian learning for conic optimization</a> | NeurIPS | 2024 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2403.03454">Learning constrained optimization with deep augmented lagrangian methods</a> | arXiv | 2024 |
| Lagrangian and primal-dual training | <a href="https://openreview.net/forum?id=fDaLmkdSKU">Near-Optimal Solutions of Constrained Learning Problems</a> | ICLR | 2024 |
| provable guarantees and verification | <a href="https://arxiv.org/pdf/2403.13297">POLICEd RL: Learning closed-loop robot control policies with provable satisfaction of hard constraints</a> | arXiv | 2024 |
| provable parameter editing. | <a href="https://openreview.net/forum?id=IGhpUd496D">Provable Editing of Deep Neural Networks using Parametric Linear Relaxation</a> | NeurIPS | 2024 |
| Lagrangian and primal-dual training | <a href="https://doi.org/10.1109/TPWRS.2024.3498705">Self-supervised learning for large-scale preventive security constrained dc optimal power flow</a> | IEEE TPS | 2024 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2510.20995">AL-CoLe: Augmented Lagrangian for Constrained Learning</a> | arXiv | 2025 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2505.19387">Alignment of large language models with constrained learning</a> | arXiv | 2025 |
| learned constraints and feasibility guarantees | <a href="https://openreview.net/forum?id=ZvUZvT8tgg">Conformal Mixed-Integer Constraint Learning with Feasibility Guarantees</a> | NeurIPS | 2025 |
| decision-focused feasibility | <a href="https://openreview.net/forum?id=eTmvwxohRx">Feasibility-Aware Decision-Focused Learning for Predicting Parameters in the Constraints</a> | NeurIPS | 2025 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2505.13631">Learning (approximately) equivariant networks via constrained optimization</a> | arXiv | 2025 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2510.20777">Learning Optimal Power Flow with Pointwise Constraints</a> | arXiv | 2025 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2511.14320">Learning with Statistical Equality Constraints</a> | arXiv | 2025 |
| penalty/adversarial training | <a href="https://arxiv.org/pdf/2510.23196">Neural Networks for AC Optimal Power Flow: Improving Worst-Case Guarantees during Training</a> | arXiv | 2025 |
| provable guarantees and verification | <a href="https://openreview.net/forum?id=1ffIkWo0yq">Provable Gradient Editing of Deep Neural Networks</a> | NeurIPS | 2025 |
| provable guarantees and verification | <a href="https://doi.org/10.1109/CDC57313.2025.11312423">Provably-safe neural network training using hybrid zonotope reachability analysis</a> | 2025 IEEE 64th Conference on… | 2025 |
| provable guarantees and verification | <a href="https://arxiv.org/pdf/2502.02434">mPOLICE: Provable Enforcement of Multi-Region Affine Constraints in Deep Neural Networks</a> | arXiv | 2025 |
| Lagrangian and primal-dual training | <a href="https://openreview.net/forum?id=BHSSV1nHvU">Breaking Safety Paradox with Feasible Dual Policy Iteration</a> | ICLR | 2026 |
| SCPO weight-space projection. | <a href="https://arxiv.org/pdf/2512.13788">Constrained Policy Optimization via Sampling-Based Weight-Space Projection</a> | arXiv | 2026 |
| Lagrangian and primal-dual training | <a href="https://arxiv.org/pdf/2601.17274">Unrolled Neural Networks for Constrained Optimization</a> | arXiv | 2026 |

### Post-Processing and Repair

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| post-processing and projection | <a href="https://doi.org/10.1109/MLSP.2019.8918690">Learning warm-start points for AC optimal power flow</a> | 2019 IEEE 29th International… | 2019 |
| learning-to-warm-start. | <a href="https://www.climatechange.ai/papers/neurips2019/1">Warm-starting AC optimal power flow with graph neural networks</a> | 33rd Conference on Neural… | 2019 |
| predict-and-reconstruct. | <a href="https://doi.org/10.1109/TPWRS.2020.3026379">Deepopf: A deep neural network approach for security-constrained dc optimal power flow</a> | IEEE TPS | 2020 |
| post-processing and projection | <a href="https://proceedings.mlr.press/v211/sambharya23a.html">End-to-end learning to warm-start for real-time quadratic optimization</a> | L4DC | 2023 |
| homeomorphic projection. | <a href="https://proceedings.mlr.press/v202/liang23a.html">Low complexity homeomorphic projection to ensure neural-network Solution feasibility for optimization over (non-) convex set</a> | ICML | 2023 |
| INN-based homeomorphic projection. | <a href="https://jmlr.org/papers/v25/23-1577.html">Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization</a> | JMLR | 2024 |
| fixed-point residual warm start. | <a href="https://jmlr.org/papers/v25/23-1174.html">Learning to warm-start fixed-point optimization algorithms</a> | JMLR | 2024 |
| bisection projection. | <a href="https://openreview.net/forum?id=HWN9CAfcav">Efficient Bisection Projection to Ensure Neural-Network Solution Feasibility for Optimization over General Set</a> | Proceedings of the Forty-second… | 2025 |
| bisection-based projection. | <a href="https://doi.org/10.1145/3679240.3734656">Solving Chance-Constrained AC-OPF Problem by Neural Network with Bisection-based Projection</a> | The 16th ACM International… | 2025 |
| autoencoder-based projection. | <a href="https://openreview.net/forum?id=dVlkUtsyg7">Improving Feasibility via Fast Autoencoder-Based Projections</a> | ICLR | 2026 |

### Structured NN Layers

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| differentiable QP layer. | <a href="https://proceedings.mlr.press/v70/amos17a.html">Optnet: Differentiable optimization as a layer in neural networks</a> | ICML | 2017 |
| DC3 completion-correction. | <a href="https://arxiv.org/pdf/2104.12225">DC3: A learning method for optimization with hard constraints</a> | arXiv | 2020 |
| PROF differentiable projection. | <a href="https://dl.acm.org/doi/10.1145/3447555.3464874">Enforcing policy feasibility constraints through differentiable projection for energy optimization</a> | Proceedings of the Twelfth ACM… | 2021 |
| F-FPN nonexpansive fixed points. | <a href="https://doi.org/10.1186/s13663-021-00706-3">Feasibility-based fixed point networks</a> | Fixed Point Theory and… | 2021 |
| structured feasibility layers | <a href="https://arxiv.org/pdf/2210.01802">Alternating differentiation for optimization layers</a> | arXiv | 2022 |
| AC predict-and-reconstruct with penalty training. | <a href="https://doi.org/10.1109/JSYST.2022.3201041">DeepOPF: A feasibility-optimized deep neural network approach for AC optimal power flow problems</a> | IEEE Systems Journal | 2022 |
| structured feasibility layers | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html">Efficient and modular implicit differentiation</a> | NeurIPS | 2022 |
| Gauge NN / interior-point gauge map. | <a href="https://arxiv.org/pdf/2203.12196">Safe and efficient model predictive control using neural networks: An interior point approach</a> | arXiv | 2022 |
| Wasserstein-based projection. | <a href="https://doi.org/10.1137/20M1376790">Wasserstein-Based Projections with Applications to Inverse Problems</a> | SIAM Journal on Mathematics of… | 2022 |
| computationally simple feasible mapping. | <a href="https://doi.org/10.1134/S1064562423701077">A new computationally simple approach for implementing neural networks with output hard constraints</a> | Doklady Mathematics | 2023 |
| structured feasibility layers | <a href="https://openreview.net/forum?id=oO1IreC6Sd">Neural Fields with Hard Constraints of Arbitrary Differential Order</a> | NeurIPS | 2023 |
| structured feasibility layers | <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/f3716db40060004d0629d4051b2c57ab-Abstract-Conference.html">One-step differentiation of iterative algorithms</a> | NeurIPS | 2023 |
| hard convex constraint imposition. | <a href="https://arxiv.org/pdf/2307.08336">RAYEN: Imposition of Hard Convex Constraints on Neural Networks</a> | arXiv | 2023 |
| LOOP-LC 2.0 generalized gauge map. | <a href="https://arxiv.org/pdf/2311.04838">Toward Rapid, Optimal, and Feasible Power Dispatch through Generalized Neural Mapping</a> | arXiv | 2023 |
| dual completion. | <a href="https://arxiv.org/pdf/2402.02596">Dual interior point optimization learning</a> | arXiv | 2024 |
| GLinSAT accelerated linear satisfiability. | <a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/dd73f39426a03131c38c8d943153d44b-Paper-Conference.pdf">GLinSAT: The general linear satisfiability neural network layer by accelerated gradient descent</a> | NeurIPS | 2024 |
| Hard affine enforcement layer | <a href="https://arxiv.org/pdf/2410.10807">Hardnet: Hard-constrained neural networks with universal approximation guarantees</a> | arXiv | 2024 |
| star-shaped ray marching. | <a href="https://doi.org/10.3390/math12233788">Imposing Star-Shaped Hard Constraints on the Neural Network Output</a> | Mathematics | 2024 |
| integer correction plus projection. | <a href="https://arxiv.org/pdf/2410.11061">Learning to optimize for mixed-integer non-linear programming with feasibility guarantees</a> | arXiv | 2024 |
| infeasible-QP differentiation. | <a href="https://openreview.net/forum?id=YCPDFfmkFr">Leveraging Augmented-Lagrangian Techniques for Differentiating over Infeasible Quadratic Programs in Machine Learning</a> | ICLR | 2024 |
| QCQP activation. | <a href="https://arxiv.org/pdf/2401.06820">QCQP-Net: Reliably Learning Feasible Alternating Current Optimal Power Flow Solutions Under Constraints</a> | arXiv | 2024 |
| PI-HC-MoE local hard constraints. | <a href="https://openreview.net/forum?id=u3dX2CEIZb">Scaling physics-informed hard constraints with mixture-of-experts</a> | ICLR | 2024 |
| constraint boundary wandering. | <a href="https://doi.org/10.1109/TPAMI.2025.3560762">Constraint boundary wandering framework: Enhancing constrained optimization with deep neural networks</a> | IEEE Transactions on Pattern… | 2025 |
| ENFORCE AdaNP projection. | <a href="https://arxiv.org/pdf/2502.06774">ENFORCE: Nonlinear constrained learning with adaptive-depth neural projection</a> | arXiv | 2025 |
| ProbHardE2E DPPL. | <a href="https://arxiv.org/pdf/2506.07003">End-to-end probabilistic framework for learning with hard constraints</a> | arXiv | 2025 |
| safe-network decision rules. | <a href="https://openreview.net/forum?id=gjiCml2CNG">Enforcing Hard Linear Constraints in Deep Learning Models with Decision Rules</a> | NeurIPS | 2025 |
| ProjNet CAD projection. | <a href="https://arxiv.org/pdf/2510.11227">Enforcing convex constraints in Graph Neural Networks</a> | arXiv | 2025 |
| feasibility-seeking step. | <a href="https://openreview.net/forum?id=oum1txoy1D">FSNet: Feasibility-Seeking Neural Network for Constrained Optimization with Guarantees</a> | NeurIPS | 2025 |
| T-SKM iterative post-processing. | <a href="https://arxiv.org/pdf/2512.10461">T-SKM-Net: Trainable Neural Network Framework for Linear Constraint Satisfaction via Sampling Kaczmarz-Motzkin Method</a> | arXiv | 2025 |
| CAffNet / CAffine layer. | <a href="https://arxiv.org/pdf/2605.24437">CAffNet: Hard Constraint-Affine Neural Networks</a> | arXiv | 2026 |
| Deep FlexQP. | <a href="https://openreview.net/forum?id=HL3TvE4Afm">Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding</a> | ICLR | 2026 |
| HardNet++. | <a href="https://arxiv.org/pdf/2604.19669">HardNet++: Nonlinear Constraint Enforcement in Neural Networks</a> | arXiv | 2026 |
| LMI-Net. | <a href="https://arxiv.org/pdf/2604.05374">LMI-Net: Linear Matrix Inequality-Constrained Neural Networks via Differentiable Projection Layers</a> | arXiv | 2026 |
| PiNet orthogonal projection. | <a href="https://openreview.net/forum?id=EJ680UQeZG">Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers</a> | ICLR | 2026 |
| SnareNet repair layer. | <a href="https://arxiv.org/pdf/2602.09317">SnareNet: Flexible Repair Layers for Neural Networks with Hard Constraints</a> | arXiv | 2026 |

### Constraint Parameterization

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| activation-space parameterization. | <a href="https://openaccess.thecvf.com/content_CVPRW_2020/html/w45/Frerix_Homogeneous_Linear_Inequality_Constraints_for_Neural_Network_Activations_CVPRW_2020_paper.html">Homogeneous linear inequality constraints for neural network activations</a> | CVPRW | 2020 |
| Vertex Network. | <a href="https://proceedings.mlr.press/v144/zheng21a.html">Safe reinforcement learning of control-affine systems with vertex networks</a> | L4DC | 2021 |
| gauge map from virtual action to safe action. | <a href="https://doi.org/10.23919/ACC53348.2022.9867652">Computationally efficient safe reinforcement learning for power systems</a> | 2022 American Control Conference… | 2022 |
| gauge map from unit ball. | <a href="https://doi.org/10.1109/ACCESS.2023.3285199">Learning to solve optimization problems with hard linear constraints</a> | IEEE Access | 2023 |
| Hom-PGD. | <a href="https://openreview.net/forum?id=bP5cU0OYSn">Fast Projection-Free Approach (without Optimization Oracle) for Optimization over Compact Convex Set</a> | NeurIPS | 2025 |
| Caratheodory-style feasible decomposition. | <a href="https://openreview.net/forum?id=EPDLFWyNnF">Geometric Algorithms for Neural Combinatorial Optimization with Constraints</a> | NeurIPS | 2025 |
| HoP polar homeomorphism. | <a href="https://arxiv.org/pdf/2502.00304">HoP: Homeomorphic Polar Learning for Hard Constrained Optimization</a> | arXiv | 2025 |
| soft-radial projection. | <a href="https://arxiv.org/pdf/2602.03461">Soft-Radial Projection for Constrained End-to-End Learning</a> | arXiv | 2026 |

## Part II: Hard-Constrained Generative Models

Generative methods produce samples that must remain valid under explicit structural, physical, geometric, or logical constraints.

| Family | Core mechanism | Typical guarantee basis | Main trade-off |
|---|---|---|---|
| Push-forward generators | Transform latent variables into a constrained domain. | Map validity, support inclusion, manifold or geometry assumptions. | Clean feasibility story but map design and coverage can be difficult. |
| Autoregressive models | Restrict generation step by step through constrained decoding or construction rules. | Grammar, automaton, decoder, or search validity. | Good for symbolic/discrete domains but may reduce diversity or increase search cost. |
| Diffusion and flow-matching models | Modify dynamics, sampling domain, guidance, or training to respect constraints. | Boundary behavior, constrained sampler validity, guidance success, discretization assumptions. | Flexible and high quality but feasibility, utility, and sampling cost must be reported together. |

### Push-Forward Generators

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| one-step consistency map | <a href="https://proceedings.mlr.press/v202/song23a.html">Consistency Models</a> | ICML | 2023 |
| push-forward and normalizing-flow maps | <a href="https://openreview.net/forum?id=p1gzxzJ4Y5">FlowPG: Action-Constrained Policy Gradient with Normalizing Flows</a> | NeurIPS | 2023 |
| mean-flow one-step generator | <a href="https://openreview.net/forum?id=uWj4s7rMnR">Mean Flows for One-step Generative Modeling</a> | NeurIPS | 2025 |
| shortcut one-step diffusion | <a href="https://openreview.net/forum?id=OlzB6LnXcS">One Step Diffusion via Shortcut Models</a> | The Thirteenth International… | 2025 |

### Autoregressive Models

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| constrained beam search | <a href="https://aclanthology.org/D17-1098/">Guided open vocabulary image captioning with constrained beam search</a> | Proceedings of the 2017… | 2017 |
| lexically constrained decoding | <a href="https://aclanthology.org/N18-1119/">Fast lexically constrained decoding with dynamic beam allocation for neural machine translation</a> | Proceedings of the 2018… | 2018 |
| Metropolis-Hastings constrained text sampling | <a href="https://arxiv.org/abs/1811.10996">CGMH: Constrained Sentence Generation by Metropolis-Hastings Sampling</a> | AAAI | 2019 |
| gradient-guided language generation | <a href="https://arxiv.org/pdf/1912.02164">Plug and play language models: A simple approach to controlled text generation</a> | arXiv | 2019 |
| predicate-logic constrained decoding | <a href="https://arxiv.org/abs/2010.12884">NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints</a> | Proceedings of the 2021… | 2021 |
| gradient-based constrained LM sampling | <a href="https://arxiv.org/abs/2205.12558">Gradient-Based Constrained Sampling from Language Models</a> | arXiv | 2022 |
| grammar-constrained decoding | <a href="https://arxiv.org/abs/2305.13971">Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning</a> | Proceedings of the 2023… | 2023 |

### Diffusion and Flow-Matching Models

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| manifold constraint correction. | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/a48e5877c7bf86a513950ab23b360498-Abstract-Conference.html">Improving diffusion models for inverse problems using manifold constraints</a> | NeurIPS | 2022 |
| manifold and geometric modeling | <a href="https://arxiv.org/pdf/2207.03024">Riemannian diffusion Schrodinger bridge</a> | arXiv | 2022 |
| Riemannian score/diffusion modeling. | <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/123d3e814e257e0781e5d328232ead9b-Abstract-Conference.html">Riemannian diffusion models</a> | NeurIPS | 2022 |
| barrier/reflected diffusion. | <a href="https://arxiv.org/pdf/2304.05364">Diffusion models for constrained domains</a> | arXiv | 2023 |
| constrained diffusion bridge. | <a href="https://openreview.net/forum?id=WH1yCa0TbB">Learning Diffusion Bridges on Constrained Domains</a> | The Eleventh International… | 2023 |
| training and fine-tuning | <a href="https://arxiv.org/pdf/2301.13362">Optimizing ddpm sampling with shortcut fine-tuning</a> | arXiv | 2023 |
| reflection-based diffusion. | <a href="https://proceedings.mlr.press/v202/lou23a.html">Reflected diffusion models</a> | ICML | 2023 |
| manifold and geometric modeling | <a href="https://arxiv.org/pdf/2302.02277">SE (3) diffusion model with application to protein backbone generation</a> | arXiv | 2023 |
| manifold and geometric modeling | <a href="https://openreview.net/forum?id=FLTg8uA5xI">Scaling riemannian diffusion models</a> | NeurIPS | 2023 |
| manifold and geometric modeling | <a href="https://doi.org/10.1109/ICRA48891.2023.10161569">Se (3)-diffusionfields: Learning smooth cost functions for joint grasp and motion optimization through diffusion</a> | 2023 IEEE international… | 2023 |
| training and fine-tuning | <a href="https://arxiv.org/pdf/2409.08861">Adjoint matching: Fine-tuning flow and diffusion generative models with memoryless stochastic optimal control</a> | arXiv | 2024 |
| categorical statistical-manifold flow | <a href="https://openreview.net/forum?id=5fybcQZ0g4">Categorical flow matching on statistical manifolds</a> | NeurIPS | 2024 |
| trust sampling. | <a href="https://openreview.net/forum?id=dJUb9XRoZI">Constrained Diffusion with Trust Sampling</a> | NeurIPS | 2024 |
| projected diffusion sampling. | <a href="https://openreview.net/forum?id=FsdB3I9Y24">Constrained Synthesis with Projected Diffusion Models</a> | NeurIPS | 2024 |
| dual constrained training. | <a href="https://openreview.net/forum?id=Es2Ey2tGmM">Constrained diffusion models via dual training</a> | NeurIPS | 2024 |
| constrained diffusion solver warm start. | <a href="https://arxiv.org/pdf/2403.05571">Efficient and Guaranteed-Safe Non-Convex Trajectory Optimization with Constrained Diffusion Model</a> | arXiv | 2024 |
| training and fine-tuning | <a href="https://arxiv.org/pdf/2402.15194">Fine-tuning of continuous-time diffusion models as entropy-regularized control</a> | arXiv | 2024 |
| Fisher-geometric flow matching | <a href="https://arxiv.org/pdf/2405.14664">Fisher flow matching for generative modeling over discrete data</a> | arXiv | 2024 |
| Riemannian / general-geometry flow matching | <a href="https://openreview.net/forum?id=g7ohDlTITL">Flow Matching on General Geometries</a> | ICLR | 2024 |
| reflected or constrained-domain sampling | <a href="https://proceedings.mlr.press/v247/kook24b.html">Gaussian cooling and dikin walks: The interior-point method for logconcave sampling</a> | The Thirty Seventh Annual… | 2024 |
| ECI sampling. | <a href="https://arxiv.org/pdf/2412.01786">Gradient-free generation for hard-constrained systems</a> | arXiv | 2024 |
| Metric / geodesic flow matching | <a href="https://openreview.net/forum?id=fE3RqiF4Nx">Metric flow matching for smooth interpolations on the data manifold</a> | NeurIPS | 2024 |
| Metropolis constrained sampling. | <a href="https://openreview.net/forum?id=jzseUq55eP">Metropolis sampling for constrained diffusion models</a> | NeurIPS | 2024 |
| mirror diffusion. | <a href="https://openreview.net/forum?id=XPWEtXzlLy">Mirror diffusion models for constrained and watermarked generation</a> | NeurIPS | 2024 |
| NAMM learned mirror map. | <a href="https://arxiv.org/pdf/2406.12816">Neural Approximate Mirror Maps for Constrained Diffusion Models</a> | arXiv | 2024 |
| Reflected flow matching | <a href="https://arxiv.org/pdf/2405.16577">Reflected Flow Matching</a> | arXiv | 2024 |
| reflected Schrodinger bridge. | <a href="https://arxiv.org/pdf/2401.03228">Reflected Schrodinger Bridge for Constrained Generative Modeling</a> | arXiv | 2024 |
| Variational flow matching for graphs | <a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/15b780350b302a1bf9a3bd273f5c15a4-Abstract-Conference.html">Variational flow matching for graph generation</a> | NeurIPS | 2024 |
| training and fine-tuning | <a href="https://arxiv.org/pdf/2510.10020">Calibrating Generative Models</a> | arXiv | 2025 |
| training and fine-tuning | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/1af991de2d4c4e679bcc5d9e23ac6bae-Paper-Conference.pdf">Composition and alignment of diffusion models using constrained learning</a> | NeurIPS | 2025 |
| proximal ADMM constrained diffusion. | <a href="https://arxiv.org/pdf/2510.14989">Constrained Diffusion for Protein Design with Hard Structural Constraints</a> | arXiv | 2025 |
| CPS posterior-mean projection. | <a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/9b01c4a7d3fc49875dad3c13848bcd9e-Paper-Conference.pdf">Constrained Posterior Sampling: Time Series Generation with Hard Constraints</a> | NeurIPS | 2025 |
| CDD constrained discrete sampling. | <a href="https://arxiv.org/pdf/2503.09790">Constrained discrete diffusion</a> | arXiv | 2025 |
| manually bridged diffusion. | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/34159">Constrained generative modeling with manually bridged diffusion models</a> | AAAI | 2025 |
| guided generation and correction | <a href="https://arxiv.org/pdf/2505.13131">Constraint-Aware Diffusion Guidance for Robotics: Real-Time Obstacle Avoidance for Autonomous Racing</a> | arXiv | 2025 |
| OLLA constrained Langevin. | <a href="https://arxiv.org/pdf/2510.22044">Fast Non-Log-Concave Sampling under Nonconvex Equality and Inequality Constraints with Landing</a> | arXiv | 2025 |
| fast constrained sampling. | <a href="https://openreview.net/forum?id=3kVM0m60Q5">Fast constrained sampling in pre-trained diffusion models</a> | NeurIPS | 2025 |
| polytope flow via ball homeomorphism. | <a href="https://arxiv.org/pdf/2503.10232">Flows on convex polytopes</a> | arXiv | 2025 |
| gauge flow matching | <a href="https://iclr.cc/virtual/2025/35307">Gauge flow matching for efficient constrained generative modeling over general convex set</a> | ICLR 2025 Workshop on Deep… | 2025 |
| terminal constrained trajectory optimization. | <a href="https://arxiv.org/pdf/2511.08425">HardFlow: Hard-Constrained Sampling for Flow-Matching Models via Trajectory Optimization</a> | arXiv | 2025 |
| LLE inverse-algorithm extrapolation. | <a href="https://openreview.net/forum?id=EGYwfs4XhI">Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Linear Extrapolation</a> | NeurIPS | 2025 |
| CDIM constrained update. | <a href="https://openreview.net/forum?id=TYGDG9zEML">Linearly Constrained Diffusion Implicit Models</a> | NeurIPS | 2025 |
| LoMAP local projection. | <a href="https://openreview.net/forum?id=EHG5Iv1mmb">Local Manifold Approximation and Projection for Manifold-Aware Diffusion Planning</a> | Forty-second International… | 2025 |
| heavy-tailed mirror flow | <a href="https://arxiv.org/pdf/2510.08929">Mirror flow matching with heavy-tailed priors for generative modeling on convex domains</a> | arXiv | 2025 |
| training and fine-tuning | <a href="https://arxiv.org/pdf/2508.09156">Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems</a> | arXiv | 2025 |
| simplex-to-Euclidean map | <a href="https://arxiv.org/pdf/2510.27480">Simplex-to-Euclidean Bijections for Categorical Flow Matching</a> | arXiv | 2025 |
| softly constrained denoiser. | <a href="https://arxiv.org/pdf/2512.14980">Softly Constrained Denoisers for Diffusion Models</a> | arXiv | 2025 |
| latent proximal correction. | <a href="https://openreview.net/forum?id=TrNB08KuHK">Training-Free Constrained Generation With Stable Diffusion Models</a> | NeurIPS | 2025 |
| guided generation and correction | <a href="https://arxiv.org/pdf/2502.05749">UniDB: A Unified Diffusion Bridge Framework via Stochastic Optimal Control</a> | arXiv | 2025 |
| feasible-set parameterization | <a href="https://arxiv.org/pdf/2602.12233">Categorical Flow Maps</a> | arXiv | 2026 |
| Constraint-Aware Flow Matching. | <a href="https://arxiv.org/pdf/2605.12754">Constraint-Aware Flow Matching: Decision Aligned End-to-End Training for Constrained Sampling</a> | arXiv | 2026 |
| landing mechanism. | <a href="https://arxiv.org/pdf/2604.17838">Efficient Diffusion Models under Nonconvex Equality and Inequality Constraints via Landing</a> | Proceedings of the 43rd… | 2026 |
| FAST-DIPS measurement correction. | <a href="https://openreview.net/forum?id=voMeZVAkKL">FAST-DIPS: Adjoint-Free Analytic Steps and Hard-Constrained Likelihood Correction for Diffusion-Prior Inverse Problems</a> | ICLR | 2026 |
| gauge flow matching | <a href="https://openreview.net/forum?id=vxq1OnaAMq">Gauge Flow Matching: Efficient Constrained Generative Modeling over General Convex Set and Beyond</a> | ICLR | 2026 |
| SafeFlowMatcher CBF correction. | <a href="https://openreview.net/forum?id=refcXHU1Nh">SafeFlowMatcher: Safe and Fast Planning Using Flow Matching with Control Barrier Functions</a> | ICLR | 2026 |
| TOCFlow terminal optimal control. | <a href="https://arxiv.org/pdf/2601.09474">Terminally constrained flow-based generative models from an optimal control perspective</a> | arXiv | 2026 |

## Applications and Benchmarks

The application section uses the same evaluation lens across domains: feasibility evidence, output utility, enforcement cost, and assumption scope.

| Application group | Typical constraints | Useful reporting dimensions |
|---|---|---|
| AI for optimization | Network, resource, safety, optimality, integer, and feasibility constraints. | Feasibility residuals, objective gap, solver calls, latency. |
| AI for science | Physical laws, geometry, chemistry, material, simulation, and inverse-design constraints. | Physical validity, residuals, sample quality, downstream screening. |
| Constrained synthesis | Grammar, trajectory, safety, logic, and design validity constraints. | Validity rate, diversity, task success, guidance or decoding overhead. |

### AI for Optimization

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| optimal power flow and power systems | <a href="https://doi.org/10.1109/TPEC48276.2020.9042547">A survey on applications of machine learning for optimal power flow</a> | 2020 IEEE Texas Power and Energy… | 2020 |
| optimal power flow and power systems | <a href="https://doi.org/10.1287/educ.2021.0234">Machine learning for optimal power flows</a> | Tutorials in Operations… | 2021 |
| OPF proxy/background. | <a href="https://doi.org/10.1109/TPWRS.2022.3212925">Fast optimal power flow with guarantees via an unsupervised generative model</a> | IEEE TPS | 2022 |
| optimal power flow and power systems | <a href="https://doi.org/10.1109/SmartGridComm52983.2022.9961047">Projection-aware Deep Neural Network for DC Optimal Power Flow Without Constraint Violations</a> | 2022 IEEE International… | 2022 |
| optimal power flow and power systems | <a href="https://doi.org/10.3390/en17061381">Advancements and future directions in the application of machine learning to AC optimal power flow: A critical review</a> | Energies | 2024 |
| optimal power flow and power systems | <a href="https://doi.org/10.1049/rpg2.13048">Equality-embedded augmented Lagrangian neural network for DC optimal power flow</a> | IET Renewable Power Generation | 2024 |
| optimal power flow and power systems | <a href="https://doi.org/10.1109/TPWRS.2024.3354733">FRMNet: A Feasibility Restoration Mapping Deep Neural Network for AC Optimal Power Flow</a> | IEEE TPS | 2024 |
| optimal power flow and power systems | <a href="https://doi.org/10.1109/TPWRS.2024.3373399">Unsupervised Learning for Solving AC Optimal Power Flows: Design, Analysis, and Experiment</a> | IEEE TPS | 2024 |
| optimal power flow and power systems | <a href="https://arxiv.org/pdf/2506.11281">Constrained diffusion models for synthesizing representative power flow datasets</a> | arXiv | 2025 |
| optimal power flow and power systems | <a href="https://arxiv.org/pdf/2510.14075">DiffOPF: Diffusion Solver for Optimal Power Flow</a> | arXiv | 2025 |
| bisection-based projection. | <a href="https://doi.org/10.1145/3679240.3734656">Solving Chance-Constrained AC-OPF Problem by Neural Network with Bisection-based Projection</a> | The 16th ACM International… | 2025 |
| optimal power flow and power systems | <a href="https://ssrn.com/abstract=5854385">Towards Trustworthy Learning for Optimal Power Flow: A Physics-informed Diffusion Model</a> | Available at SSRN 5854385 | 2025 |
| optimal power flow and power systems | <a href="https://arxiv.org/pdf/2602.06255">A hard-constrained NN learning framework for rapidly restoring AC-OPF from DC-OPF</a> | arXiv | 2026 |
| trajectory optimization and manipulation | <a href="https://openreview.net/forum?id=bGPDviEtZ1">MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation</a> | ICLR | 2026 |
| combinatorial optimization and exact solvers | <a href="https://arxiv.org/pdf/2605.07113">Solving Max-Cut to Global Optimality via Feasibility-Preserving Graph Neural Networks</a> | arXiv | 2026 |

### AI for Science

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| physics-constrained learning and generation | <a href="https://arxiv.org/pdf/2204.06125">Hierarchical text-conditional image generation with clip latents</a> | arXiv | 2022 |
| physics-constrained learning and generation | <a href="https://arxiv.org/pdf/2302.08224">DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization</a> | arXiv | 2023 |
| physics-constrained learning and generation | <a href="https://doi.org/10.1177/02783649241273668">Diffusion policy: Visuomotor policy learning via action diffusion</a> | The International Journal of… | 2023 |
| physics-constrained learning and generation | <a href="https://cdn.openai.com/papers/dall-e-3.pdf">Improving image generation with better captions</a> | Computer Science. https://cdn.… | 2023 |
| physics-constrained learning and generation | <a href="https://arxiv.org/pdf/2307.08123">Solving inverse problems with latent diffusion models via hard data consistency</a> | arXiv | 2023 |
| physics-constrained learning and generation | <a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/9c93b3cd3bc60c0fe7b0c2d74a2da966-Abstract-Conference.html">T2t: From distribution learning in training to gradient search in testing for combinatorial optimization</a> | NeurIPS | 2023 |
| physics-constrained learning and generation | <a href="https://doi.org/10.1038/s41586-024-07487-w">Accurate structure prediction of biomolecular interactions with AlphaFold 3</a> | Nature | 2024 |
| Riemannian flow matching for materials | <a href="https://arxiv.org/pdf/2406.04713">Flowmm: Generating materials with riemannian flow matching</a> | arXiv | 2024 |
| physics-constrained learning and generation | <a href="https://openreview.net/forum?id=8mMqlab1pn">Generative Learning for Solving Non-Convex Problem with Multi-Valued Input-Solution Mapping</a> | 12th International Conference on… | 2024 |
| physics-constrained learning and generation | <a href="https://doi.org/10.1038/s41586-025-08628-5">A generative model for inorganic materials design</a> | Nature | 2025 |
| molecule, material, and protein generation | <a href="https://arxiv.org/pdf/2602.19153">Constrained Diffusion for Accelerated Structure Relaxation of Inorganic Solids with Point Defects</a> | NeurIPS 2025 AI4Mat Workshop | 2026 |
| molecule, material, and protein generation | <a href="https://openreview.net/forum?id=sJABnBEYeh">Physically Valid Biomolecular Interaction Modeling with Gauss-Seidel Projection</a> | ICLR | 2026 |

### Constrained Synthesis

| Keywords | Paper | Venue | Year |
|---|---|---|---:|
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2310.09574">Reduced Policy Optimization for Continuous Control with Hard Constraints</a> | NeurIPS | 2023 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2412.09342">Diffusion predictive control with constraints</a> | arXiv | 2024 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2412.17993">Multi-Agent Path Finding in Continuous Spaces with Projected Diffusion Models</a> | arXiv | 2024 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2504.00342">Aligning diffusion model with problem constraints for trajectory optimization</a> | arXiv | 2025 |
| Constrained Diffusers. | <a href="https://arxiv.org/pdf/2506.12544">Constrained diffusers for safe planning and control</a> | arXiv | 2025 |
| trajectory optimization and safe control | <a href="https://doi.org/10.23919/ACC63710.2025.11108080">Equality constrained diffusion for direct trajectory optimization</a> | 2025 American Control Conference… | 2025 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2509.08775">Joint Model-based Model-free Diffusion for Planning with Constraints</a> | arXiv | 2025 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2502.03607">Simultaneous multi-robot motion planning with projected diffusion models</a> | arXiv | 2025 |
| trajectory optimization and safe control | <a href="https://arxiv.org/pdf/2506.02955">UniConFlow: A Unified Constrained Flow-Matching Framework for Certified Motion Planning</a> | arXiv | 2025 |
| trajectory optimization and safe control | <a href="https://ojs.aaai.org/index.php/AAAI/article/download/39512/43473">Discrete-guided diffusion for scalable and safe multi-robot motion planning</a> | AAAI | 2026 |
| trajectory optimization and safe control | <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GuideFlow_Constraint-Guided_Flow_Matching_for_Planning_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.pdf">GuideFlow: Constraint-guided flow matching for planning in end-to-end autonomous driving</a> | Proceedings of the IEEE/CVF… | 2026 |

## Reader Guides and Data

- [Start Here](docs/start-here.md)
- [How to Read a Hard-Constraint Claim](docs/reader-guide/how-to-read-a-hard-constraint-claim.md)
- [Which Method Family?](docs/reader-guide/which-method-family.md)
- [Common Failure Modes](docs/reader-guide/common-failure-modes.md)
- [Guarantee Terminology](docs/evaluation/guarantee-terminology.md)
- [Reporting Dimensions](docs/evaluation/reporting-dimensions.md)
- [Public paper index](data/papers.csv)
- [Method timeline](data/method_timeline.csv)
- [BibTeX snapshot](data/references.bib)

## Citation

If this repository helps your work, please cite the companion survey and this repository.

```bibtex
@misc{HardConstrainedMLSurveyRepo,
  title        = {Awesome Hard-Constrained Machine Learning},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/lem/Hard-Constrained-ML-Survey}
}
```

## Contributing

Suggestions and pull requests are welcome. Please add papers with a clear method family, guarantee basis, and link to the original source when available.
