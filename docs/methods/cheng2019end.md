# `cheng2019end`

**Source Status**: verified_from_source

**Source Pdf File**: cheng2019end__end_to_end_safe_reinforcement_learning_through_barrier_functions_for_safety_critical_continuous_control_tasks.pdf

**Method Family Primary**: control-barrier-function safe reinforcement learning.

**Learning Task**: learn continuous-control policies with safety constraints.

**Model Paradigm**: model-free RL controller coupled with a model-based CBF controller and online dynamics learning.

**Constraint Form**: safety constraints for continuous-control systems.

**Constraint Geometry**: system-dependent safe set.

**Mechanism Label**: RL-CBF.

**Mechanism Summary**: The method combines a model-free RL controller with control-barrier-function controllers and online model learning so that policy exploration is constrained to safe behavior under the paper's stated assumptions.

**Guarantee Target**: safety during control.

**Guarantee Basis**: CBF forward-invariance conditions and probabilistic model-learning assumptions.

**Inference Dependency**: CBF-based controller/QP correction during policy execution and training.

**Main Tradeoff**: stronger safety during learning comes from a model-based CBF controller, so performance and computation depend on the nominal model, online model learning, and CBF feasibility.

**Evidence Note**: PDF text checked around abstract, controller architecture, CBF conditions, and theorem statements.
