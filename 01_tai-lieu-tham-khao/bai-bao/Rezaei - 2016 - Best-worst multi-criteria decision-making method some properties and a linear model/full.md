# Best-worst multi-criteria decision-making method: Some properties and a linear model<sup>\$</sup>

Jafar Rezaei <sup>n</sup>

Transport and Logistics Group, Faculty of Technology Policy and Management, Delft University of Technology, Delft, The Netherland

a r t i c l e i n f o

Article history: Received 2 April 2015 Accepted 3 December 2015 Available online 12 December 2015

Keywords: Best worst method (BWM) Multi-criteria decision-making (MCDM) Interval analysis

## a b s t r a c t

The Best Worst Method (BWM) is a multi-criteria decision-making method that uses two vectors of pairwise comparisons to determine the weights of criteria. First, the best (e.g. most desirable, most important), and the worst (e.g. least desirable, least important) criteria are identi<sup>fi</sup>ed by the decisionmaker, after which the best criterion is compared to the other criteria, and the other criteria to the worst criterion. A non-linear minmax model is then used to identify the weights such that the maximum absolute difference between the weight ratios and their corresponding comparisons is minimized. The minmax model may result in multiple optimal solutions. Although, in some cases, decision-makers prefer to have multiple optimal solutions, in other cases they prefer to have a unique solution. The aim of this paper is twofold: <sup>fi</sup>rstly, we propose using interval analysis for the case of multiple optimal solutions, in which we show how the criteria can be weighed and ranked. Secondly, we propose a linear model for BWM, which is based on the same philosophy, but yields a unique solution.

& 2015 Elsevier Ltd. All rights reserved.

## 1. Introduction

In general, decision-making can be de<sup>fi</sup>ned as identifying and selecting an alternative from a set of alternatives based on the preferences of the decision-maker(s). In most cases, several criteria are involved in this identi<sup>fi</sup>cation and selection process, which is why these problems are called multi-criteria decision-making problems. Different decision-makers value the criteria involved differently. In the past decades, several multi-criteria decision-making methods have been proposed to help decision-makers <sup>fi</sup>nd the values of the criteria and the alternatives based on their preferences. As the aim of this paper is not to review these methods, we refer the readers to some textbooks that cover the most commonly used MCDM methods [1–3], and some review papers [4,5]. One of the most recently developed methods is the best worst method (BWM) [6], which is a comparison-based method that conducts the comparisons in a particularly structured way, such that not only is less information is required, but the comparisons are also more consistent. In some cases, BWM results in multioptimality, which means that solving the problem results in different sets of weights for the criteria. This feature of the method may be desirable in some cases. For instance, when debating has an important role in the decision-making process [7] (e.g. political decision-making), multi-optimality provides the decision-makers with the freedom to incorporate higher-level information (information that cannot be modeled) into their decision-making process. In other cases, however, the decision-maker may prefer a unique solution (e.g. when there is no debating or when there is no higherlevel information that needs to be considered). The main contribution of this paper is twofold. We <sup>fi</sup>rst ascertain some solution properties of BWM and show how we can determine the ranges of the weights of different criteria in the case of multi-optimality. We then use interval analysis as a way to analyze such cases and to determine the ranking of the criteria. Secondly, we propose a linear BWM, based on the same philosophy of BWM, that always results in unique solution.

In the next section, we provide an overview of the BWM, after which we discuss the multi-optimality property of this method in Section 3. Next, we describe the interval analysis and incorporate it in the method. Numerical examples are used to illustrate the procedure we propose to rank the interval weights. In Section 4, we propose a linear model of BWM and also solve some examples for this model. The conclusions are presented in Section 5.

## 2. Best worst method

Here, we brie<sup>fl</sup>y describe the steps of BWM that can be used to derive the weights of the criteria [6].

Step 1. Determine a set of decision criteria.

In this step, the decision-maker identi<sup>fi</sup>es n criteria $\{ c _ { 1 } , c _ { 2 } , \cdots , c _ { n } \}$ that are used to make a decision.

Step 2. Determine the best (e.g. most desirable, most important) and the worst (e.g. least desirable, least important) criteria.

Step 3. Determine the preference of the best criterion over all the other criteria, using a number between 1 and 9. The resulting best-to-others (BO) vector would be:

$$
A _ {B} = (a _ {B 1}, a _ {B 2}, \dots , a _ {B n}),
$$

where $a _ { B j }$ indicates the preference of the best criterion B over criterion j. It is clear that $a _ { B B } = 1$

<sup>¼</sup>Step 4. Determine the preference of all the criteria over the worst criterion, using a number between 1 and 9. The resulting others-to-worst (OW) vector would be:

$$
A _ {W} = (a _ {1 W}, a _ {2 W}, \dots , a _ {n W}) ^ {T},
$$

where $a _ { j W }$ indicates the preference of the criterion j over the worst criterion W. It is clear that $a _ { W W } = 1$

<sup>¼</sup>Step 5. Find the optimal weights $\left( W _ { 1 } ^ { * } , W _ { 2 } ^ { * } , . . . , W _ { n } ^ { * } \right)$

The aim is to determine the optimal weights of the criteria, such that the maximum absolute differences $\left| { \frac { w _ { B } } { w _ { j } } } - a _ { B j } \right|$ and $\left| \frac { w _ { j } } { w _ { W } } - a _ { j W } \right|$ for all $j$ is minimized, which is translated to the fol-<sup> </sup>lowing minmax model:

$$
\begin{array}{l} \min \max _ {j} \left\{\left| \frac {w _ {B}}{w _ {j}} - a _ {B j} \right|, \left| \frac {w _ {j}}{w _ {W}} - a _ {j W} \right| \right\} \\ \text { s.t. } \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text {   for   all   } j \end{array}\tag{1}
$$

Model (1) is equivalent to the following model:

min $\xi$

$$
\begin{array}{l} \text {   s.t.   } \\ \left| \frac {w _ {B}}{w _ {j}} - a _ {B j} \right| \leq \xi , \text {   for   all   } j \\ \left| \frac {w _ {j}}{w _ {W}} - a _ {j W} \right| \leq \xi , \text {   for   all   } j \\ \sum_ {j} w _ {j} = 1 \end{array}\tag{2}
$$

For any value of $\xi ,$ multiplying the <sup>fi</sup>rst set of the constraints of model (2) by $w _ { j }$ and the second set of constraints by $w _ { W }$ , it can be seen that the solution space of model (2) is an intersection of 4n 5 linear constraints (2(2n 3) comparison constraints and one <sup> </sup>constraint for the weights sum), thus given a large enough $\xi$ that the solution space is non-empty. Solving model $( 2 ) ,$ , the optimal weights $\left( w _ { 1 } ^ { * } , w _ { 2 } ^ { * } , . . . , w _ { n } ^ { * } \right)$ and $\xi ^ { * }$ are obtained.

According to [6], a consistent comparison is de<sup>fi</sup>ned as follows:

De<sup>fi</sup>nition 1. A comparison is fully consistent when $a _ { B j } \times a _ { j W } = a _ { B W } ,$ for all j, where $a _ { B j } , a _ { j W }$ and $a _ { B W }$ <sup> ¼</sup>are respectively the preference of the best criterion over the criterion $j ,$ the preference of criterion j over the worst criterion, and the preference of the best criterion over the worst criterion.

Table 1 shows the maximum values of $\xi ($ (consistency index) for different values of $a _ { B W }$

Consistency Index (CI) Table [6].

<table><tr><td> $a_{BW}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>Consistency Index (max  $\xi$ )</td><td>0.00</td><td>0.44</td><td>1.00</td><td>1.63</td><td>2.30</td><td>3.00</td><td>3.73</td><td>4.47</td><td>5.23</td></tr></table>

Best-to-others (BO) and others-to-worst (OW) pairwise comparison vectors: Example 1.

<table><tr><td>BO</td><td>Quality</td><td>Price</td><td>Comfort</td><td>Safety</td><td>Style</td></tr><tr><td>Best criterion: price</td><td>2</td><td>1</td><td>4</td><td>2</td><td>8</td></tr><tr><td>OW</td><td></td><td></td><td></td><td colspan="2">Worst criterion: style</td></tr><tr><td>Quality</td><td></td><td></td><td></td><td>4</td><td></td></tr><tr><td>Price</td><td></td><td></td><td></td><td>8</td><td></td></tr><tr><td>Comfort</td><td></td><td></td><td></td><td>2</td><td></td></tr><tr><td>Safety</td><td></td><td></td><td></td><td>4</td><td></td></tr><tr><td>Style</td><td></td><td></td><td></td><td>1</td><td></td></tr></table>

Best-to-others (BO) and others-to-worst (OW) pairwise comparison vectors: Example 2.

<table><tr><td>BO</td><td>Quality</td><td>Price</td><td>Comfort</td><td>Safety</td><td>Style</td></tr><tr><td>Best criterion: price</td><td>2</td><td>1</td><td>4</td><td>3</td><td>8</td></tr><tr><td>OW</td><td></td><td></td><td></td><td colspan="2">Worst criterion: style</td></tr><tr><td>Quality</td><td></td><td></td><td></td><td>4</td><td></td></tr><tr><td>Price</td><td></td><td></td><td></td><td>8</td><td></td></tr><tr><td>Comfort</td><td></td><td></td><td></td><td>2</td><td></td></tr><tr><td>Safety</td><td></td><td></td><td></td><td>3</td><td></td></tr><tr><td>Style</td><td></td><td></td><td></td><td>1</td><td></td></tr></table>

Best-to-others (BO) and others-to-worst (OW) pairwise comparison vectors: Example 3.

<table><tr><td>BO</td><td>Quality</td><td>Price</td><td>Comfort</td><td>Safety</td><td>Style</td></tr><tr><td>Best criterion: price</td><td>2</td><td>1</td><td>4</td><td>3</td><td>8</td></tr><tr><td>OW</td><td></td><td></td><td></td><td colspan="2">Worst criterion: style</td></tr><tr><td>Quality</td><td></td><td></td><td></td><td>4</td><td></td></tr><tr><td>Price</td><td></td><td></td><td></td><td>8</td><td></td></tr><tr><td>Comfort</td><td></td><td></td><td></td><td>4</td><td></td></tr><tr><td>Safety</td><td></td><td></td><td></td><td>2</td><td></td></tr><tr><td>Style</td><td></td><td></td><td></td><td>1</td><td></td></tr></table>

Considering the consistency index (Table 1), the consistency ratio is calculated as follows:

$$
\text { Consistency   Ratio } = \frac {\xi^ {*}}{\text { Consistency   Index }}\tag{3}
$$

Consistency Ratio 0; 1 , values close to 0 show more con-<sup>½ </sup>sistency, while values close to 1 show less consistency.

The solution space of (2) includes all the positive values for $w _ { j } , j = 1 , . . . , n ,$ such that the sum of weights be 1 and the violation <sup>¼</sup>of all the weight ratios from their corresponding comparison be at most $\xi .$ Here we show that model (2) might result in multiple optimal solutions for problems with more than three criteria.

Suppose that for a problem with n criteria (weight variables), we have $\xi ^ { * }$ . Replacing $\xi$ by $\xi ^ { * }$ in the right-hand side of the constraints of (2), the optimal solution would be the results of the following linear system:

$$
\left\{ \begin{array}{l} \left| w _ {B} - a _ {B j} w _ {j} \right| \leq \xi^ {*} w _ {j}, \text {   for   all   } j \\ \left| w _ {j} - a _ {j W} w _ {W} \right| \leq \xi^ {*} w _ {W}, \text {   for   all   } j \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text {   for   all   } j \end{array} \right.\tag{4}
$$

For fully consistent problems $( \xi ^ { * } = 0 )$ , each constraint $| w _ { B } - a _ { B j }$ $w _ { j } | \leq \xi ^ { * } w _ { j }$ <sup>¼</sup>is converted to one constraint $w _ { B } - a _ { B j } w _ { j } = 0$ <sup>j </sup>(similarly $\big | \dot { w } _ { j } - a _ { j W } \dot { w } _ { W } \big | \le \xi ^ { * } w _ { W }$ is converted to $w _ { j } - a _ { j W } w _ { W } = 0 )$ , while for <sup></sup>not-fully consistent problems $( \xi ^ { * } > 0 )$ <sup> ¼</sup>, each constraint $\left| w _ { B } - a _ { B j } w _ { j } \right|$ $\leq \xi ^ { * } w _ { j }$ is converted to two constraints w ${ \cdot } a _ { B j } w _ { j } \le \xi ^ { * } w _ { j }$ <sup></sup>and a<sub>Bj</sub>w<sub>j</sub> $- w _ { B } \leq \xi ^ { * } w _ { j }$ (similarly $\left| w _ { j } - a _ { j W } w _ { W } \right| \le \xi ^ { * } w _ { W }$ is converted to $w _ { j } -$ $a _ { j W } w _ { W } \leq \xi ^ { * } w _ { W }$ and $a _ { j W } \dot { w } _ { W } - { w } _ { j } \le \dot { \xi } ^ { * } w _ { W } )$ <sup></sup>. So for fully consistent problems we have $_ { 2 n - 3 }$ equality constraints, and for not-fully consistent we have 2(2n 3) inequality constraints. Furthermore, for fully consistent problems (because of the equality in the chain relations extracted from the consistency de<sup>fi</sup>nition, $a _ { B j } \times a _ { j W } = a _ { B W } ) ,$ the number of independent constraints become n (n 1 comparison <sup></sup>constraints one weights sum constraint). So for a fully consistent problem we have a nonhomogeneous linear system with n weight variables and n constraints, so we have a unique optimal solution. It is also obvious based on the relation chains in the consistency de<sup>fi</sup>nition, $a _ { B j } \times a _ { j W } = a _ { B W }$ , that a problem with two criteria $( n { = } 2 )$ is always consistent, hence, with a unique solution. For not-fully consistent problems $\left( n \geq 3 \right)$ we have $4 n - 5$ constraints (at least two of which are equality, the rest are inequality), 5n-8 variables (n weight variables 4n 8 slack variables), so we have a nonhomogeneous linear system for which:

The number of variables the number of constraints (or: $5 n - 8 = 4 n - 5 ) ,$ , if n 3;

<sup> ¼  ¼</sup>The number of variables4the number of constraints (or: $5 n - 8 > 4 n - 5 ) , { \mathrm { i f ~ } } n > 3$

<sup> </sup>So for not-fully consistent problems with three criteria we always have a unique optimal solution, while for not-fully consistent problems with more than three criteria we might have multiple optimal solutions.

The following section proposes a way to rank the criteria in the case of multi-optimality.

## 3. Interval weights

In this section, we propose the following two models to calculate the lower and upper bounds of the weight of criterion j. These models are solved after solving model (2) and <sup>fi</sup>nding $\xi ^ { * }$

min w<sub>j</sub>

$$
\begin{array}{l} \text { s.t. } \\ \left| \frac {w _ {B}}{w _ {j}} - a _ {B j} \right| \leq \xi^ {*}, \text {   for   all   } j \\ \left| \frac {w _ {j}}{w _ {W}} - a _ {j W} \right| \leq \xi^ {*}, \text {   for   all   } j \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text {   for   all   } j \end{array}\tag{5}
$$

$$
\begin{array}{l} \max w _ {j} \\ \text { s.t. } \\ \left| \frac {w _ {B}}{w _ {j}} - a _ {B j} \right| \leq \xi^ {*}, \text { for   all } j \\ \left| \frac {w _ {j}}{w _ {W}} - a _ {j W} \right| \leq \xi^ {*}, \text { for   all } j \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text { for   all } j \end{array}\tag{6}
$$

By solving these two models for all the criteria, we can determine the optimal weights of the criteria as intervals. The center of intervals can be used to rank the criteria or alternatives [8]. However, another option is to rank the criteria or alternatives based on the interval weights. In order to do that, we suggest using matrix of degree of preference and matrix of preferences. In the next section, we present interval analysis that is used to compare and rank the interval weights.

## 3.1. Interval analysis

Here, we <sup>fi</sup>rst introduce some basic de<sup>fi</sup>nitions and operations of interval numbers, interval arithmetic, and comparing interval numbers [9,10].

De<sup>fi</sup>nition 2. A closed interval is an ordered pair in a bracket as: $A = [ a _ { L } , a _ { R } ] = \{ x : a _ { L } \leq x \leq a _ { R } , x \in R \} ,$ 7

where a and $a _ { R }$ are the left limit and the right limit of A, respectively. The closed interval can also be de<sup>fi</sup>ned by its center and width as:

$$
A = \left\langle a _ {C}, a _ {W} \right\rangle = \{x: a _ {C} - a _ {W} \leq x \leq a _ {C} + a _ {W}, x \in R \},\tag{8}
$$

where $a _ { C }$ and $a _ { W }$ are the center and width of A, respectively.

De<sup>fi</sup>nition 3. Let $\ast \in \{ + , ~ - , ~ \times , ~ / \} \mathrm { b e }$ a binary operation on two <sup>- fþ </sup>closed intervals A and B, then

$$
A * B = \{x * y: x \in A, y \in B \}\tag{9}
$$

de<sup>fi</sup>nes a binary operation on the set of closed intervals. It is assumed that, in the case of division, $0 \notin B .$

<sup>2</sup>The operations on closed intervals used in this paper are as follows:

$$
A + B = [ a _ {L} + b _ {L}, a _ {R} + b _ {R} ]\tag{10}
$$

$$
\begin{array}{c} A \times B = [ \min (a _ {L} \times b _ {L}, a _ {L} \times b _ {R}, a _ {R} \times b _ {L}, a _ {R} \times b _ {R}), \\ \max (a _ {L} \times b _ {L}, a _ {L} \times b _ {R}, a _ {R} \times b _ {L}, a _ {R} \times b _ {R}) ] \end{array}\tag{11}
$$

$$
\begin{array}{c} A / B = [ \min {(a _ {L} / b _ {L}, a _ {L} / b _ {R}, a _ {R} / b _ {L}, a _ {R} / b _ {R})}, \\ \max {(a _ {L} / b _ {L}, a _ {L} / b _ {R}, a _ {R} / b _ {L}, a _ {R} / b _ {R})}, \text {   if   } 0 \notin [ b _ {L}, b _ {R} ] \end{array}\tag{12}
$$

$$
k A = \left\{ \begin{array}{l l} \left[ k a _ {L}, k a _ {R} \right], & \text { for } k \geq 0 \\ \left[ k a _ {R}, k a _ {L} \right], & \text { for } k <   0 \end{array} \right.
$$

where k is a real number.

13

Here we describe some de<sup>fi</sup>nition for comparing interval numbers [11].

Let $A = [ a _ { L } , ~ a _ { R } ]$ and $B = \left[ b _ { L } , \ b _ { R } \right]$ be two interval numbers.

De<sup>fi</sup>nition 4. The degree of preference of A over B (or $A > B )$ is de<sup>fi</sup>ned as:

$$
P (A > B) = \frac {\max (0 , a _ {R} - b _ {L}) - \max (0 , a _ {L} - b _ {R})}{(a _ {R} - a _ {L}) + (b _ {R} - b _ {L})}\tag{14}
$$

The degree of preference of B over A is calculated similarly as:

$$
P (B > A) = \frac {\max (0 , b _ {R} - a _ {L}) - \max (0 , b _ {L} - a _ {R})}{(a _ {R} - a _ {L}) + (b _ {R} - b _ {L})}\tag{15}
$$

It is clear that $P ( A > B ) + P ( B > A ) = 1$ and $P ( A > B ) = P ( B > A ) =$ 0:5 when $A = B ,$ <sup>ð Þþ ð</sup>, which means when $a _ { L } = b _ { L }$ <sup>ð</sup>and $a _ { R } = b _ { R }$

De<sup>fi</sup>nition 5. ${ \mathrm { ~ f ~ } } P ( A > B ) > P ( B > A )$ (or equivalently $P ( A > B ) > 0 . 5 ) $ <sup>ð Þ ð Þ</sup>then A is said to be superior to B to the degree of $P ( A > B )$ <sup>Þ</sup>, denoted by $A \stackrel { P ( A > B ) } { \sim } B ;$ if $P ( A > B ) = P ( B > A ) = 0 . 5$ then A is said to be <sup>g ð Þ ¼ ð</sup>indifferent to B; denoted by $A \sim B ;$ if $P ( B > A ) > P ( A > B )$ (or equivalently $P ( B > A ) > 0 . 5 )$ <sup> ð Þ ð Þ</sup>, then A is said to be inferior to B to the grade of $P ( B > A )$ denoted by $\stackrel { P ( B > A ) } { A } { } ^ { ~ } \stackrel { } { _ { \prec } } { } ^ { ~ }$

As we discussed before, for a not-fully-consistent comparison system with more than three criteria we have interval weights. The lower and upper limits of these intervals are obtained using (5) and (6), respectively. To compare the interval weights we calculate the 'matrix of degree of preference' $D P _ { i j } ,$ and ‘matrix of preferences’ $P _ { i j } ,$ respectively, as follows:

$$
D P _ {i j} = \begin{array}{c c c c} A & B & \dots & N \\ A & P (A > A) & P (A > B) & \dots & P (A > N) \\ B & P (B > A) & P (B > B) & \dots & P (B > N) \\ \vdots & \vdots & \ddots & \vdots \\ N & P (N > A) & P (N > B) & \dots & P (N > N) \end{array}\tag{16}
$$

$$
P _ {i j} = \begin{array}{c c c c} & A & B & \dots & N \\ A & p _ {A A} & p _ {A B} & \dots & p _ {A N} \\ B & p _ {B A} & p _ {B B} & \dots & p _ {B N} \\ \vdots & \vdots & \ddots & \vdots \\ N & p _ {N A} & p _ {N B} & \dots & p _ {N N} \end{array}\tag{17}
$$

Where:

$$
p _ {i j} = \left\{ \begin{array}{l l} 1, & \text { if } \quad P (i > j) > 0. 5, \\ 0, & \text { if } \quad P (i > j) \leq 0. 5, \quad i, j = A, \ldots , N. \end{array} \right.
$$

Then, we simply calculate the sum of the elements in each row of the matrix $P _ { i j } ,$ , and rank the criteria based on their sum values.

So, as discussed above, we can determine the weight of criterion j in the form of an interval like: $w _ { j } = \langle w _ { j C } , w _ { j W } \rangle =$ $\{ x : \ w _ { j C } - w _ { j W } \leq x \leq w _ { j C } + w _ { j W } , \ x \in R \}$ <sup>¼ ¼</sup> After determining the <sup>f  þ g</sup>weights as intervals, equations (14)–(17) can be used to rank them. Alternatively, as mentioned before, this range can be used as an input for debating and making an agreement on a set of weights within the ranges. In these cases, one alternative is to consider w (the center value) as a representative.

## 3.1.1. Numerical examples

Example 1. When buying a car, a buyer considers <sup>fi</sup>ve criteria quality (c ), price $( c _ { 2 } ) ,$ , comfort (c ), safety (c ), and style (c ). The buyer provides the pairwise comparison vectors as shown in Table 2.

Solving this problem using model (2) results in $w _ { 1 } ^ { * } = 0 . 2 1 0 5$ $w _ { 2 } ^ { * } = 0 . 4 2 1 1 , \ w _ { 3 } ^ { * } = 0 . 1 0 5 3 , \ w _ { 4 } ^ { * } = 0 . 2 1 0 5 , \ w _ { 5 } ^ { * } = 0 . 0 5 2 6 ,$ <sup>¼</sup>and $\xi ^ { * } = 0 .$ <sup>¼ ¼ ¼ ¼ ¼</sup>This comparison system is fully consistent and we have a single solution.

![](images/02644209f09251e867a5481fd77cc37a2a573c3306b72bb1aa2df3d858b68b12.jpg)  
Fig. 1. Optimal interval weights of example 2.

Example 2. Consider the example presented above, with the BO and OW comparison vectors as shown in Table 3.

Solving this problem using model (2) yields $\xi ^ { * } = 0 . 1 4 5 9$ , which <sup>¼</sup>implies that the pairwise comparison system is not-fullyconsistent and we may have multi-optimality. We used models (5) and (6) and found the following optimal intervals for the weights of the criteria (and their centers and width), with the optimal value of $\xi ^ { * } = 0 . 1 4 5 9$ (see also Fig. 1).

$$
\begin{array}{l} w _ {1} ^ {*} = [ 0. 2 1 4 5, 0. 2 2 8 9 ], w _ {1} ^ {*} (c e n t e r) = 0. 2 2 1 7, w _ {1} ^ {*} (w i d t h) = 0. 0 0 7 2 \\ w _ {2} ^ {*} = [ 0. 4 4 6 1, 0. 4 5 7 1 ], w _ {2} ^ {*} (c e n t e r) = 0. 4 5 1 6, w _ {2} ^ {*} (w i d t h) = 0. 0 0 5 5 \\ w _ {3} ^ {*} = [ 0. 1 0 8 5, 0. 1 1 7 6 ], w _ {3} ^ {*} (c e n t e r) = 0. 1 1 3 1, w _ {3} ^ {*} (w i d t h) = 0. 0 0 4 6 \\ w _ {4} ^ {*} = [ 0. 1 5 6 3, 0. 1 6 0 2 ], w _ {4} ^ {*} (c e n t e r) = 0. 1 5 8 2, w _ {4} ^ {*} (w i d t h) = 0. 0 0 1 9 \\ w _ {5} ^ {*} = [ 0. 0 5 4 8, 0. 0 5 6 1 ], w _ {5} ^ {*} (c e n t e r) = 0. 0 5 5 4, w _ {5} ^ {*} (w i d t h) = 0. 0 0 0 7 \end{array}
$$

Looking at the intervals and Fig. 1, because there is no overlap between the interval numbers, for the ranking involved, it is obvious that price quality safety comfort style.

<sup>g g g g</sup>If we calculate the degree of preference matrix (16) and preference matrix (17), we arrive at the same conclusion.

$$
D P _ {i j} = \left( \begin{array}{c c c c c} 0. 5 & 0 & 1 & 1 & 1 \\ 1 & 0. 5 & 1 & 1 & 1 \\ 0 & 0 & 0. 5 & 0 & 1 \\ 0 & 0 & 1 & 0. 5 & 1 \\ 0 & 0 & 0 & 0 & 0. 5 \end{array} \right) \Rightarrow P _ {i j} = \left( \begin{array}{c c c c c} 0 & 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right) \begin{array}{c} s u m \\ 3 \\ 4 \\ 1 \\ 2 \\ 0 \end{array}
$$

The sum of each row is used to rank the criteria, which means that price $\succ$ quality safety comfort style.

Example 3. Now suppose that the DM has provided the pairwise comparison vectors BO and OW as shown in Table 4.

Solving this problem using model (2), we <sup>fi</sup>nd $\xi ^ { * } = 1$ , which <sup>¼</sup>shows the problem may have multiple optimal solutions. Using models (5) and (6), we <sup>fi</sup>nd the following optimal intervals for the weights for the criteria (and their centers and width), with the optimal value of $\xi ^ { * } = 1$ (see also Fig. 2).

$$
\begin{array}{l} w _ {1} ^ {*} = [ 0. 1 5 7 9, 0. 2 4 6 9 ], w _ {1} ^ {*} (c e n t e r) = 0. 2 0 2 4, w _ {1} ^ {*} (w i d t h) = 0. 0 4 4 5 \\ w _ {2} ^ {*} = [ 0. 4 2 8 6, 0. 4 9 3 2 ], w _ {2} ^ {*} (c e n t e r) = 0. 4 6 0 9, w _ {2} ^ {*} (w i d t h) = 0. 0 3 2 3 \\ w _ {3} ^ {*} = [ 0. 1 4 2 9, 0. 1 6 4 4 ], w _ {3} ^ {*} (c e n t e r) = 0. 1 5 3 6, w _ {3} ^ {*} (w i d t h) = 0. 0 1 0 8 \\ w _ {4} ^ {*} = [ 0. 1 1 1 1, 0. 1 5 7 9 ], w _ {4} ^ {*} (c e n t e r) = 0. 1 3 4 5, w _ {4} ^ {*} (w i d t h) = 0. 0 2 3 4 \\ w _ {5} ^ {*} = [ 0. 0 4 7 6, 0. 0 5 4 8 ], w _ {5} ^ {*} (c e n t e r) = 0. 0 5 1 2, w _ {5} ^ {*} (w i d t h) = 0. 0 0 3 6 \end{array}
$$

![](images/94b35983edaa38ea6fbca6511d17be7a3bf05456d01e0aa49c711bb2951af22f.jpg)  
Fig. 2. Optimal interval weights of example 3.

For this example, it is not easy to visually rank the interval weights, as some of them overlap.

If we calculate the degree of preference matrix (16) and preference matrix (17), we have:

$$
D P _ {i j} = \left( \begin{array}{c c c c c} 0. 5 & 0 & 0. 9 4 1 3 & 1 & 1 \\ 1 & 0. 5 & 1 & 1 & 1 \\ 0. 0 5 8 7 & 0 & 0. 5 & 0. 7 7 9 9 & 1 \\ 0 & 0 & 0. 2 2 0 1 & 0. 5 & 1 \\ 0 & 0 & 0 & 0 & 0. 5 \end{array} \right) \Rightarrow P _ {i j} = \left( \begin{array}{c c c c c} 0 & 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right) \quad \begin{array}{l} s u m \\ 3 \\ 4 \\ 2 \\ 1 \\ 0 \end{array}
$$

Based on the sum of the rows, the following ranking emerges: price quality comfort safety style.

## 4. A linear model of BWM

As discussed in the previous section, model (2) could result in multiple optimal solutions. If, instead of minimizing the maximum value among the set of $\begin{array} { r } { \left\{ \bigg | \frac { w _ { B } } { w _ { j } } - a _ { B j } \bigg | , \ : \bigg | \frac { w _ { j } } { w _ { W } } - a _ { j W } \bigg | \right\} } \end{array}$ , we minimize the maximum among the set of $\big \{ \dot { \big | w _ { B } } - a _ { B j } w _ { j } \big | , \big | w _ { j } - a _ { j W } w _ { W } \big | \big \}$ , the problem can be formulated as follows.

$$
\begin{array}{l} \min \max _ {j} \left\{\left| w _ {B} - a _ {B j} w _ {j} \right|, \left| w _ {j} - a _ {j W} w _ {W} \right| \right\} \\ \text { s.t. } \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text {   for   all   } j \end{array}\tag{18}
$$

Problem (18) can be transferred to the following linear programming problem:

$$
\begin{array}{l} \min \xi^ {L} \\ \text { s.t. } \\ \left| w _ {B} - a _ {B j} w _ {j} \right| \leq \xi^ {L}, \text { for   all } j \\ | w _ {j} - a _ {j W} w _ {W} | \leq \xi^ {L}, \text { for   all } j \\ \sum_ {j} w _ {j} = 1 \\ w _ {j} \geq 0, \text { for   all } j \end{array}\tag{19}
$$

Problem (19) is a linear problem, which has a unique solution. Solving Problem (19), the optimal weights $\left( W _ { 1 } ^ { * } , W _ { 2 } ^ { * } , . . . , W _ { n } ^ { * } \right)$ and $\xi ^ { L * }$ are obtained.

For this model, $\xi ^ { L * }$ can be directly considered as an indicator of the consistency of the comparisons (here we do not use Consistency Index, Eq. 3). Values of $\xi ^ { L * }$ close to zero show a high level of consistency.

## 4.1. Numerical examples

Example 1. We use the same data that was used for Example 1 in section 3 for buying a car. Using model (19), we have:

$w _ { 1 } ^ { * } = 0 . 2 1 0 5 , w _ { 2 } ^ { * } = 0 . 4 2 1 1 , w _ { 3 } ^ { * } = 0 . 1 0 5 3 , w _ { 4 } ^ { * } = 0 . 2 1 0 5 , w _ { 5 } ^ { * } =$ <sup>¼</sup>0:0526; and $\xi ^ { L * } = 0 .$

<sup>¼</sup>The comparison system is fully consistent and we have a unique solution. As can also be seen in case of consistency, both models result in the same weights.

Example 2. Here, we use the same data that was used for Example 2 in section 3 for buying a car. While, due to the inconsistency of the problem and the non-linearity of model (2), there were multiple optimal solutions, applying model (19), we <sup>fi</sup>nd the following unique solution.

$$
w _ {1} ^ {*} = 0. 2 2 9 5, w _ {2} ^ {*} = 0. 4 4 8 1, w _ {3} ^ {*} = 0. 1 1 4 8, w _ {4} ^ {*} = 0. 1 5 3 0,
$$

w 0:0546; and $\xi ^ { L * } = 0 . 0 1 0 9 $

As can be seen the unique solution found by this model is very close to the center of intervals we found from the non-linear model is Section 3.

## 5. Conclusion and future research

The best worst method (BWM) results in a single solution for problems with two or three criteria and when the comparisons system is fully consistent with any number of criteria. For notfully-consistent comparison systems with more than three criteria, where there may be multiple optimal solutions, we can <sup>fi</sup>nd the weights as intervals. This feature of the BWM in fact provides more information about the optimal solution. The center of intervals can be used to rank the criteria or alternatives. However, another option is to rank the criteria or alternatives based on the interval weights. In order to do that, we suggested using matrix of degree of preference and matrix of preferences. Although multioptimality may be desirable in some cases, in other cases, a unique solution is preferred, which is why we also proposed a linear BWM, the philosophy behind which is very close to the initial BWM model, but, due to its linearity results in a unique solution. Interesting future research directions are to use the method in real-world cases and to extend the method for group-decisionmaking problems [12].

## References

[1] Triantaphyllou E. Multi-criteria decision making methods a comparative study. USA: Springer; 2000.

[2] Ishizaka A, Nemery P. Multi-criteria decision analysis: methods and software. West Sussex, UK: John Wiley & Sons; 2013.

[3] Köksalan MM, Wallenius J, Zionts S. Multiple criteria decision making: from early history to the 21st century, Singapore: World Scientific: 2011

[4] Govindan K, Rajendran S, Sarkis J, Murugesan P. Multi criteria decision making approaches for green supplier evaluation and selection: a literature review. Journal of Cleaner Production 2013.

[5] Ho W, Xu X, Dey PK. Multi-criteria decision making approaches for supplier evaluation and selection: a literature review. European Journal of Operational Research 2010;202:16–24.

[6] Rezaei J. Best-worst multi-criteria decision-making method. Omega 2015:53:49-57

[7] Simons T, Pelled LH, Smith KA. Making use of difference: diversity, debate, and decision comprehensiveness in top management teams. Academy of Management Journal 1999;42:662–673.

[8] Rezaei J, Wang J, Tavasszy L. Linking supplier development to supplier segmentation using Best Worst Method. Expert Systems with Applications 2015;42:9152–9164.

[9] Alefeld G, Herzberger J. Introduction to interval computation. New York, USA: Academic press; 1983.

[10] Moore RE, Kearfott RB, Cloud MJ. Introduction to interval analysis. PA, USA: Siam; 2009.

[11] Wang Y-M, Yang J-B, Xu D-L. A preference aggregation method through the estimation of utility intervals. Computers & Operations Research 2005;32:2027–2049.

[12] Sun B, Ma W. An approach to consensus measurement of linguistic preference relations in multi-attribute group decision making and application. Omega 2015;51:83–92.

Jafar Rezaei is an assistant professor of operations and supply chain management at Delft University of Technology, the Netherlands, where he also obtained his Ph.D. One of his main research interests is in the area of multi-criteria decision-making (MCDM). He has published in various academic journals, including International Journal of Production Economics, International Journal of Production Research, International Journal of Systems Science, Industrial Marketing Management, Expert Systems with Applications, Applied Soft Computing, Applied Mathematical Modeling, IEEE Transactions on Engineering Management, European Journal of Opera tional Research, and Omega.