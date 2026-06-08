
# Common Failure Modes

Hard-constrained ML papers are easiest to compare when their claims separate feasibility, utility, cost, and scope. The following failure modes make comparison difficult.

## Treating penalties as guarantees

A penalty can reduce violations without proving that all outputs are feasible. Look for residuals, violation rates, or an additional certificate.

## Reporting validity without utility

A method can make outputs valid by collapsing diversity, becoming conservative, or hurting objective quality. Validity should be read together with task performance.

## Hiding solver dependence

If feasibility depends on a projection, repair, or downstream solver, the paper should report tolerance, termination, runtime, and failure cases.

## Ignoring numerical tolerance

Equality and inequality residuals depend on tolerance choices. A useful comparison states the tolerance and reports both maximum and average residuals.

## Overgeneralizing the constraint class

Some methods work for boxes or affine sets; others require convexity, smooth boundaries, a valid homeomorphism, or an oracle. The claimed scope should match the method assumptions.

## Confusing training-time safety with output feasibility

Safe training updates, constrained losses, and verified output inclusion are different claims. They may be related, but they should not be merged without evidence.
