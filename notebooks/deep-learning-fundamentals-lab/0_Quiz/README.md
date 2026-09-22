# Ready to get started?
Before you can start the Deep Learning Fundamentals Lab, you need to take an Admissions Quiz.

As a reminder, applicants are expected to have the following prerequisite skills:

- Basic linear algebra (i.e., matrices, vectors, and matrix operations)
- Basic calculus concepts (i.e., function analysis, derivatives, gradients, etc.)
- Basic probability and statistics functions
- Intermediate-level Python programming, including: basic data structures like arrays and dictionaries, the ability to write definitions for functions and classes, and familiarity with data manipulation using libraries like NumPy and Pandas.
- Familiarity with essential machine learning concepts, including supervised and unsupervised learning, overfitting and regularization, and training, validation, and test sets.

The Admissions Quiz is composed of 24 questions, and the minimum passing grade is 70%. The time limit is 45 minutes and it must be completed in one sitting. You have a maximum of two (2) attempts to complete the test.

The Admissions Quiz covers 4 main topics (6 questions for each topic): linear algebra, calculus, probability and statistics. And Python programming.

How can I prepare for the Quiz?
Before you attempt the quiz, we strongly encourage you to consider these highly recommended (and free!) online resources we have curated to help you prepare:

- [Mathematics for Machine Learning](https://mml-book.github.io/): Comprehensive coverage of linear algebra, calculus, and probability.
- [Algebra Basics at Khan Academy](https://www.khanacademy.org/math/algebra-basics): Foundations, algebraic expressions, linear equations and inequalities, graphing lines and slope
- [Statistics and Probability at Khan Academy](https://www.khanacademy.org/math/statistics-probability): Displaying and comparing quantitative data, summarizing quantitative data, modeling data distributions.
- [Python at LearnPython.org](https://www.learnpython.org/): Learn the Basics
- [Applied Data Science Lab](https://www.wqu.edu/adsl): WQU’s own Applied Data Science Lab is free and always available. The Applied Data Science Lab teaches you the Python and Machine Learning skills needed to succeed in the Deep Learning Fundamentals Lab.
Important: Complete this quiz using only your current knowledge

This admissions quiz is designed to assess whether you have the foundational knowledge needed to succeed in the Lab. Please complete it without using any external resources.

Why this matters? The Admissions Quiz difficulty is carefully calibrated to predict your success in the Lab. If you need external help to pass it, you'll likely struggle and may not be able to complete the program successfully.

We want you to succeed! Taking the quiz honestly helps ensure you're ready for the learning journey ahead and will be able to earn your certificate.

Good luck! 🍀
## Preparation notes

The quiz has 24 questions in 45 minutes: 6 questions in each of four areas. A score of 70% means answering at least **17 questions correctly**. Prepare without a calculator or reference material so practice matches the real quiz.

### 1. Linear algebra

Be able to:

- Distinguish scalars, vectors, and matrices and identify their shapes.
- Add and subtract objects of matching shape.
- Compute a dot product: `x . y = sum(x_i * y_i)`.
- Multiply matrices and check compatibility: `(m x n)(n x p) = (m x p)`.
- Transpose a matrix and use `(AB)^T = B^T A^T`.
- Recognize identity matrices, inverses, determinants, singular matrices, vector norms, linear transformations, and small systems of equations.

Common traps: matrix multiplication is generally not commutative; element-wise and matrix multiplication differ; always check dimensions first.

### 2. Calculus

Be able to:

- Interpret a derivative as a rate of change and tangent-line slope.
- Differentiate constants, powers, sums, products, quotients, and compositions.
- Apply the chain rule: if `y = f(g(x))`, then `dy/dx = f'(g(x))g'(x)`.
- Recall derivatives of `x^n`, `e^x`, `ln(x)`, `sin(x)`, and `cos(x)`.
- Find simple critical points, compute partial derivatives, and interpret the gradient.
- Understand gradient descent: `theta_new = theta_old - learning_rate * gradient`.

Common traps: include the inner derivative in the chain rule; gradient descent moves opposite the gradient; a zero derivative alone does not prove a minimum.

### 3. Probability and statistics

Be able to:

- Use `P(not A) = 1 - P(A)`.
- Use `P(A or B) = P(A) + P(B) - P(A and B)`.
- Use `P(A|B) = P(A and B) / P(B)`.
- Distinguish independent from mutually exclusive events and apply Bayes' theorem.
- Calculate and interpret mean, median, mode, range, variance, and standard deviation.
- Explain outliers, population versus sample, expectation, and correlation.
- Recognize Bernoulli, binomial, uniform, and normal distributions.

Common traps: independence does not mean events cannot occur together; read the order in `P(A|B)` carefully; variance uses squared units while standard deviation uses the original units.

### 4. Python programming

Be ready to read a short program and predict its output. Review:

- Core types, zero-based and negative indexing, slicing, and mutability.
- Control flow, functions, return values, default arguments, and scope.
- Comprehensions, exceptions, classes, `__init__`, attributes, and methods.
- NumPy shape, dtype, indexing, vectorization, broadcasting, and `axis`.
- Pandas selection, filtering, missing values, and aggregation.

Examples to evaluate mentally:

```python
[x * x for x in range(5) if x % 2 == 0]  # [0, 4, 16]

import numpy as np
a = np.array([[1, 2], [3, 4]])
a.sum(axis=0)  # array([4, 6])
a.sum(axis=1)  # array([3, 7])
```

Common traps: `=` assigns while `==` compares; `/` is true division while `//` is floor division; `range` excludes its stop value; no explicit `return` means `None`; NumPy arithmetic is normally element-wise while `@` performs matrix multiplication.

## Readiness check

Before using an attempt, confirm that you can:

- Complete 24 mixed questions in no more than 45 minutes.
- Consistently score at least 20/24 in practice, leaving a buffer above the required 17/24.
- Explain every incorrect answer instead of memorizing the correct choice.
- Perform small matrix, derivative, and probability calculations by hand.
- Trace Python code accurately, including NumPy shapes and `axis` behavior.

## Suggested preparation plan

1. Take an untimed diagnostic covering all four topics.
2. Review the weakest topic and work examples by hand.
3. Drill each topic until the main rules and formulas can be recalled unaided.
4. Take a closed-book, 45-minute mock quiz with 6 questions per topic.
5. Review every mistake and consistently exceed the passing score before using an attempt.

During the quiz, average time is about 1 minute 52 seconds per question. Answer quick questions first, mark difficult ones for review, eliminate clearly wrong options, and reserve the final 5 minutes for uncertain answers. Choose a quiet time and confirm that your device, power, and internet connection are reliable before starting.