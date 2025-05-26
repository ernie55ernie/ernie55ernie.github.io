---
layout: post
title: "Positive Semidefiniteness of a 3×3 Correlation Matrix"
date: 2025-05-26
category: quantitative interview
---

We are given the symmetric matrix:

\\[
\Sigma =
\begin{pmatrix}
1 & 0.6 & -0.3 \\
0.6 & 1 & \rho \\
-0.3 & \rho & 1
\end{pmatrix}
\\]

We are to find all real values of \\( \rho \\) for which this matrix is a **valid correlation matrix**, i.e., **positive semidefinite (PSD)**.

---

### Step 1: Symmetry and Unit Diagonal

The matrix is symmetric and has 1's on the diagonal, satisfying basic properties of correlation matrices.

---

### Step 2: Leading Principal Minors

To be PSD, **all leading principal minors** must be nonnegative.

#### First minor (top-left entry):

\\[
1 \geq 0 \quad \text{(True)}
\\]

#### Second-order minor:

\\[
\begin{vmatrix}
1 & 0.6 \\
0.6 & 1
\end{vmatrix}
= 1 - 0.6^2 = 1 - 0.36 = 0.64 > 0
\\]

#### Full determinant:

\\[
\det(\Sigma) =
1(1 \cdot 1 - \rho^2)
- 0.6(0.6 \cdot 1 - \rho \cdot (-0.3))
+ (-0.3)(0.6 \cdot \rho - 1 \cdot (-0.3))
\\]

Expanding and simplifying:

\\[
= 1(1 - \rho^2) - 0.6(0.6 + 0.3\rho) - 0.3(0.6\rho + 0.3)
\\]
\\[
= 1 - \rho^2 - 0.36 - 0.18\rho - 0.18\rho - 0.09
\\]
\\[
= (1 - 0.36 - 0.09) - \rho^2 - 0.36\rho = 0.55 - \rho^2 - 0.36\rho
\\]

So the condition is:

\\[
\det(\Sigma) = 0.55 - \rho^2 - 0.36\rho \geq 0
\\]

---

### Step 3: Solve the Inequality

Solve:

\\[
-\rho^2 - 0.36\rho + 0.55 \geq 0
\\]

Multiply by -1 (flip the inequality):

\\[
\rho^2 + 0.36\rho - 0.55 \leq 0
\\]

Solve the quadratic:

\\[
\rho = \frac{-0.36 \pm \sqrt{0.36^2 + 4 \cdot 0.55}}{2}
= \frac{-0.36 \pm \sqrt{0.1296 + 2.2}}{2}
= \frac{-0.36 \pm \sqrt{2.3296}}{2}
\\]

\\[
\sqrt{2.3296} \approx 1.525 \Rightarrow \rho \in \left[ \frac{-0.36 - 1.525}{2}, \frac{-0.36 + 1.525}{2} \right]
= [-0.9425, 0.5825]
\\]

---

### Conclusion

The matrix is a valid correlation matrix **if and only if**:

\\[
\rho \in [-0.9425, 0.5825]
\\]

This is the full set of real values for \\( \rho \\) making the matrix positive semidefinite.

# Reference

* [1] [Linear Algebra and Its Applications (Fourth Edition)](https://dn720003.ca.archive.org/0/items/linear-algebra-by-strang-4-th-edition/linear%20algebra%20by%20strang%204%20th%20edition.pdf)
