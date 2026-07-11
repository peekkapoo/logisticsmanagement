# Extensions of the TOPSIS for group decision-making under fuzzy environment

Chen-Tung Chen<sup>∗</sup>

Department of Information Management, The Overseas Chinese College of Commerce, 100, Chiao Kwang Road, Taichung, Taiwan, ROC

Received June 1997; received in revised form October 1997

## Abstract

The aim of this paper is to extend the TOPSIS to the fuzzy environment. Owing to vague concepts frequently represented in decision data, the crisp value are inadequate to model real-life situations. In this paper, the rating of each alternative and the weight of each criterion are described by linguistic terms which can be expressed in triangular fuzzy numbers. Then, a vertex method is proposed to calculate the distance between two triangular fuzzy numbers. According to the concept of the TOPSIS, a closeness coecient is dened to determine the ranking order of all alternatives by calculating the distances to both the fuzzy positive-ideal solution (FPIS) and fuzzy negative-ideal solution (FNIS) simultaneously. Finally, an example is shown to highlight the procedure of the proposed method at the end of this paper. c 2000 Elsevier Science B.V. All rights reserved.

Keywords: TOPSIS; Linguistic variables; Triangular fuzzy number; MCDM

## 1. Introduction

Decision-making problems is the process of nding the best option from all of the feasible alternatives. In almost all such problems the multiplicity of criteria for judging the alternatives is pervasive. That is, for many such problems, the decision maker wants to solve a multiple criteria decision making (MCDM) problem. A MCDM problem can be concisely expressed in matrix format as

$$
\boldsymbol {D} = \begin{array}{c} A _ {1} \\ A _ {2} \\ \vdots \\ A _ {m} \end{array} \left[ \begin{array}{c c c c} C _ {1} & C _ {2} & \dots & C _ {n} \\ x _ {1 1} & x _ {1 2} & \dots & x _ {1 n} \\ x _ {2 1} & x _ {2 2} & \dots & x _ {2 n} \\ \vdots & \vdots & \vdots & \vdots \\ x _ {m 1} & x _ {m 2} & \dots & x _ {m n} \end{array} \right],
$$

$$
W = [ w _ {1} w _ {2} \dots w _ {n} ],
$$

where $A _ { 1 } , A _ { 2 } , \ldots , A _ { m }$ are possible alternatives among which decision makers have to choose, $C _ { 1 } , C _ { 2 } , \ldots , C _ { n }$ are criteria with which alternative performance are measured, $x _ { i j }$ is the rating of alternative $A _ { i }$ with respect to criterion $C _ { j } , \ w _ { j }$ is the weight of criterion $C _ { j }$

In classical MCMD methods, the ratings and the weights of the criteria are known precisely [5, 10, 13]. A survey of the methods has been presented in Hwang and Yoon [10]. Technique for order performance by similarity to ideal solution (TOPSIS), one of the known classical MCDM method, was rst developed by Hwang and Yoon [10] for solving a MCDM problem. It bases upon the concept that the chosen alternative should have the shortest distance from the positive ideal solution (PIS) and the farthest from the negative ideal solution (NIS). In the process of TOPSIS, the performance ratings and the weights of the criteria are given as crisp values.

Under many conditions, crisp data are inadequate to model real-life situations. Since human judgements including preferences are often vague and cannot estimate his preference with an exact numerical value. A more realistic approach may be to use linguistic assessments instead of numerical values, that is, to suppose that the ratings and weights of the criteria in the problem are assessed by means of linguistic variables [1, 3, 4, 6, 9, 15]. In this paper, we further extended the concept of TOPSIS to develop a methodology for solving multi-person multi-criteria decision-making problems in fuzzy environment. Considering the fuzziness in the decision data and group decision-making process, linguistic variables are used to assess the weights of all criteria and the ratings of each alternative with respect to each criterion. We can convert the decision matrix into a fuzzy decision matrix and construct a weighted normalized fuzzy decision matrix once the decision makers’ fuzzy ratings have been pooled. According to the concept of TOP-SIS, we dene the fuzzy positive ideal solution (FPIS) and the fuzzy negative ideal solution (FNIS). And then, a vertex method is proposed in this paper to calculate the distance between two triangular fuzzy ratings. Using the vertex method, we can calculate the distance of each alternative from FPIS and FNIS, respectively. Finally, a closeness coecient of each alternative is dened to determine the ranking order of all alternatives. The higher value of closeness coe- cient indicates that an alternative is closer to FPIS and farther from FNIS simultaneously.

In order to develop the linguistic TOPSIS method, the paper is organized as follows. Next section introduces the basic denitions and notations of the fuzzy number and linguistic variable. Section 3 presents the linguistic TOPSIS method in group decision making and the choice process. And then, the proposed method is illustrated with an example. Finally, some conclusions are pointed out in the end of this paper.

![](images/d7f15aaf44c0ea51438fc3a9468adb181f954f5eb417b291944b5e557e4e2128.jpg)  
Fig. 1. A fuzzy number ˜n.

## 2. Preliminaries

In the following, we brie y review some basic definitions of fuzzy sets from [2, 11, 12, 14–16]. These basic denitions and notations below will be used throughout the paper until otherwise stated.

Denition 2.1. A fuzzy set $\tilde { A }$ in a universe of discourse X is characterized by a membership function $\mu _ { \tilde { A } } ( x )$ which associates with each element x in X a real number in the interval [0; 1]. The function value $\mu _ { \tilde { A } } ( x )$ is termed the grade of membership of x in A<sup>˜</sup> [14].

Denition 2.2. A fuzzy set $\tilde { A }$ of the universe of discourse X is convex if and only if for all $x _ { 1 } , x _ { 2 }$ in X ,

$$
\mu_ {\tilde {A}} (\lambda x _ {1} + (1 - \lambda) x _ {2}) \geqslant \operatorname{Min} \left(\mu_ {\tilde {A}} \left(x _ {1}\right), \mu_ {\tilde {A}} \left(x _ {2}\right)\right),\tag{1}
$$

where $\lambda \in [ 0 , 1 ]$

Denition 2.3. A fuzzy set $\tilde { A }$ of the universe of discourse X is called a normal fuzzy set implying that $\exists x _ { i } \in X , ~ \mu _ { \tilde { A } } ( x _ { i } ) = 1$

Denition 2.4. A fuzzy number is a fuzzy subset in the universe of discourse X that is both convex and normal. Fig. 1 shows a fuzzy number ˜n of the universe of discourse X which is both convex and normal.

Denition 2.5. The -cut of fuzzy number ˜n is dened

$$
\tilde {n} ^ {\alpha} = \left\{x _ {i}: \mu_ {\tilde {n}} (x _ {i}) \geqslant \alpha , x _ {i} \in X \right\},\tag{2}
$$

where $\alpha \in [ 0 , 1 ]$

$\tilde { n } ^ { \alpha }$ is a non-empty bounded closed interval contained in X and it can be denoted by $\tilde { n } ^ { \alpha } = [ n _ { \ell } ^ { \alpha } , n _ { \mathrm { u } } ^ { \alpha } ]$ $n _ { \ell } ^ { \alpha }$ and $n _ { \mathrm { u } } ^ { \alpha }$ are the lower and upper bounds of the closed interval, respectively [11, 16]. Fig. 2 shows a fuzzy number ˜n with -cuts, where

![](images/ec94d3ea3d88963f5c8d3f2a8c58aa4e8d20717fbdca5f0a473d18dc74a1caeb.jpg)

Fig. 2. Fuzzy number ˜n with -cuts.  
![](images/6179da6baf9b58f6888b799ca7b4ec550af1f48875f391228e449a67fa1de568.jpg)  
Fig. 3. A triangular fuzzy number ˜n.

$$
\tilde {n} ^ {\alpha_ {1}} = \left[ n _ {\ell} ^ {\alpha_ {1}}, n _ {\mathrm{u}} ^ {\alpha_ {1}} \right], \quad \tilde {n} ^ {\alpha_ {2}} = \left[ n _ {\ell} ^ {\alpha_ {2}}, n _ {\mathrm{u}} ^ {\alpha_ {2}} \right].\tag{3}
$$

From Fig. 2, we can see that if $\alpha _ { 2 } \geqslant \alpha _ { 1 }$ , then $n _ { \ell } ^ { \alpha _ { 2 } } \geqslant n _ { \ell } ^ { \alpha _ { 1 } }$ and $n _ { \mathrm { u } } ^ { \alpha _ { 1 } } \geqslant n _ { \mathrm { u } } ^ { \alpha _ { 2 } }$

Denition 2.6. A triangular fuzzy number $\tilde { n }$ can be dened by a triplet $( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ shown in Fig. 3. The membership function $\mu _ { \tilde { n } } ( x )$ is dened as [11]:

$$
\mu_ {\tilde {n}} (x) = \left\{ \begin{array}{l l} 0, & x <   n _ {1}, \\ \frac {x - n _ {1}}{n _ {2} - n _ {1}}, & n _ {1} \leqslant x \leqslant n _ {2}, \\ \frac {x - n _ {3}}{n _ {2} - n _ {3}}, & n _ {2} \leqslant x \leqslant n _ {3}, \\ 0, & x > n _ {3}. \end{array} \right.\tag{4}
$$

Denition 2.7. If ˜n is a fuzzy number and $n _ { \ell } ^ { \alpha } > 0$ for $\alpha \in [ 0 , 1 ]$ , then $\tilde { n }$ is called a positive fuzzy number [2, 9].

Given any two positive fuzzy numbers $\tilde { m } , \tilde { n }$ and a positive real number r, the -cut of two fuzzy numbers are $\tilde { m } ^ { \alpha } = [ m _ { \ell } ^ { \alpha } , m _ { \mathrm { u } } ^ { \alpha } ]$ and $\tilde { n } ^ { \alpha } { = } [ n _ { \ell } ^ { \alpha } , n _ { \mathrm { u } } ^ { \alpha } ] ~ ( \alpha { \in } [ 0 , 1 ] )$ , respectively. According to the interval of condence [11], some main operations of positive fuzzy numbers m˜ and $\tilde { n }$ can be expressed as follows:

$$
(\tilde {m} (+) \tilde {n}) ^ {\alpha} = [ m _ {\ell} ^ {\alpha} + n _ {\ell} ^ {\alpha}, m _ {\mathrm{u}} ^ {\alpha} + n _ {\mathrm{u}} ^ {\alpha} ],\tag{5}
$$

$$
(\tilde {m} (-) \tilde {n}) ^ {\alpha} = [ m _ {\ell} ^ {\alpha} - n _ {\mathrm{u}} ^ {\alpha}, m _ {\mathrm{u}} ^ {\alpha} - n _ {\ell} ^ {\alpha} ],\tag{6}
$$

$$
(\tilde {m} (\cdot) \tilde {n}) ^ {\alpha} = [ m _ {\ell} ^ {\alpha} \cdot n _ {\ell} ^ {\alpha}, m _ {\mathrm{u}} ^ {\alpha} \cdot n _ {\mathrm{u}} ^ {\alpha} ],\tag{7}
$$

$$
(\tilde {m} (:) \tilde {n}) ^ {\alpha} = \left[ \frac {m _ {\ell} ^ {\alpha}}{n _ {\mathrm{u}} ^ {\alpha}}, \frac {m _ {\mathrm{u}} ^ {\alpha}}{n _ {\ell} ^ {\alpha}} \right],\tag{8}
$$

$$
(\tilde {m} ^ {\alpha}) ^ {- 1} = \left[ \frac {1}{m _ {\mathrm{u}} ^ {\alpha}}, \frac {1}{m _ {\ell} ^ {\alpha}} \right],\tag{9}
$$

$$
(\tilde {m} (\cdot) r) ^ {\alpha} = [ m _ {\ell} ^ {\alpha} \cdot r, m _ {\mathrm{u}} ^ {\alpha} \cdot r ],\tag{10}
$$

$$
(\tilde {m} (:) r) ^ {\alpha} = \left[ \frac {m _ {\ell} ^ {\alpha}}{r}, \frac {m _ {\mathrm{u}} ^ {\alpha}}{r} \right].\tag{11}
$$

Denition 2.8. Let $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ and $\tilde { n } = ( n _ { 1 }$ $n _ { 2 } , n _ { 3 } )$ be two triangular fuzzy numbers. If $\tilde { m } = \tilde { n } ,$ then $m _ { 1 } = n _ { 1 } , m _ { 2 } = n _ { 2 }$ and $m _ { 3 } = n _ { 3 }$

Denition 2.9. If ˜n is a triangular fuzzy number and $n _ { \ell } ^ { \alpha } { > } 0 , ~ n _ { \mathrm { u } } ^ { \alpha } { \leqslant } 1$ for $\alpha \in [ 0 , 1 ]$ , then $\tilde { n }$ is called a normalized positive triangular fuzzy number [12].

Denition 2.10. $\tilde { D }$ is called a fuzzy matrix, if at least an entry in $\tilde { D }$ is a fuzzy number [2].

Denition 2.11. A linguistic variable is a variable whose values are linguistic terms [15].

The concept of linguistic variable is very useful in dealing with situations which are too complex or too ill-dened to be reasonably described in conventional quantitative expressions [15]. For example, “weight” is a linguistic variable, its values are very low, low, medium, high, very high, etc. These linguistic values can also be represented by fuzzy numbers.

Denition 2.12. Let $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ and $\tilde { n } =$ $\left( n _ { 1 } , n _ { 2 } , n _ { 3 } \right)$ be two triangular fuzzy numbers, then the vertex method is dened to calculate the distance between them as

$$
d (\tilde {m}, \tilde {n}) = \sqrt {\frac {1}{3} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} ]}.\tag{12}
$$

Denition 2.13. Let $\tilde { A }$ and $\tilde { B }$ be two triangular fuzzy numbers. The fuzzy number $\tilde { A }$ is closer to fuzzy number $\tilde { B }$ as $d ( \tilde { A } , \tilde { B } )$ approaches 0.

Many distance measurement functions are proposed in [17], but here the vertex method is an eective and simple method to calculate the distance between two triangular fuzzy numbers. Some important properties of the vertex method are described as follows:

Property 1. If both m˜ and n˜ are real numbers; then the distance measurement $d ( \tilde { m } , \tilde { n } )$ is identical to the Euclidean distance.

Proof. Suppose that both $\tilde { m } { = } ( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ and $\tilde { n } =$ $( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ are two real numbers; then let $m _ { 1 } = m _ { 2 }$ $= m _ { 3 } = m$ and $n _ { 1 } = n _ { 2 } = n _ { 3 } = n$ . The distance measurement $( d ( \tilde { m } , \tilde { n } ) )$ can be calculated as

$$
\begin{array}{l} d (\tilde {m}, \tilde {n}) \\ = \sqrt {\frac {1}{3} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} ]} \\ = \sqrt {\frac {1}{3} [ (m - n) ^ {2} + (m - n) ^ {2} + (m - n) ^ {2} ]} \\ = \sqrt {(m - n) ^ {2}} \\ = | m - n |. \end{array}
$$

Property 2. Two triangular fuzzy numbers m˜ and n˜ are identical if and only if $d ( \tilde { m } , \tilde { n } ) = 0 .$

Proof. Let $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ and $\tilde { n } = ( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ be two triangular fuzzy numbers.

(I) If ˜m and ˜n are identical, then $m _ { 1 } = n _ { 1 } , ~ m _ { 2 } = n _ { 2 }$ and $m _ { 3 } = n _ { 3 }$ . The distance between ˜m and ˜n is

$$
\begin{array}{l} a (m, n) \\ = \sqrt {\frac {1}{3} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} ]} \\ = \sqrt {\frac {1}{3} [ (0) ^ {2} + (0) ^ {2} + (0) ^ {2} ]} \\ = 0. \end{array}
$$

$$
\begin{array}{l} d (\tilde {m}, \tilde {n}) \\ = \sqrt {\frac {1}{3} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} ]} \\ = 0. \end{array}
$$

Implies that $m _ { 1 } = n _ { 1 } , m _ { 2 } = n _ { 2 }$ and $m _ { 3 } = n _ { 3 }$ . Therefore, two triangular fuzzy numbers $\tilde { m }$ and $\tilde { n }$ are identical and the property has been proved.

![](images/75a73881d93b8f78ee82fa4f257f6a2b2c102d763fca9af460e7ccde8c4e496f.jpg)  
Fig. 4. Three triangular fuzzy numbers.

Property 3. Let $\tilde { A } , \tilde { B }$ and C˜ be three triangular fuzzy numbers. The fuzzy number $\tilde { B }$ is closer to fuzzy number $\tilde { A }$ than the other fuzzy number $\tilde { C }$ if and only if $d ( \tilde { A } , \tilde { B } ) < d ( \tilde { A } , \tilde { C } )$

This property is trivial. For example, Fig. 4 shows three fuzzy numbers $\tilde { A } = ( 1 , 3 , 5 ) , \ \tilde { B } = ( 2 , 4 , 7 )$ and $\tilde { C } = ( 5 , 7 , 9 )$ . From Fig. 4, we can easily see that the fuzzy number $\tilde { B }$ is closer to fuzzy number $\tilde { A }$ than the other fuzzy number ${ \tilde { C } } .$ According to the vertex method, the distance measurement is calculated as

$$
\begin{array}{l} d (\tilde {A}, \tilde {B}) = \sqrt {\frac {1}{3} [ (1 - 2) ^ {2} + (3 - 4) ^ {2} + (5 - 7) ^ {2} ]} \\ \qquad = \sqrt {2}, \\ d (\tilde {A}, \tilde {C}) = \sqrt {\frac {1}{3} [ (1 - 5) ^ {2} + (3 - 7) ^ {2} + (5 - 9) ^ {2} ]} = 4. \end{array}
$$

According to the distance measurement and De- nition 2.13, we conclude that the fuzzy number $\tilde { B }$ is closer to fuzzy number $\tilde { A }$ than the other fuzzy number ${ \tilde { C } } .$

Property 4. Let $\tilde { O } = ( 0 , 0 , 0 )$ be original. $I f d ( \tilde { A } , \tilde { O } ) <$ $d ( \tilde { B } , \tilde { O } )$ ; then fuzzy number $\tilde { A }$ is closer to original than the other fuzzy number B˜.

According to the Property 3, this property is trivial and easily proved.

## 3. The proposed method

A systematic approach to extend the TOPSIS to the fuzzy environment is proposed in this section. This method is very suitable for solving the group decision-making problem under fuzzy environment. In this paper, the importance weights of various criteria and the ratings of qualitative criteria are considered as linguistic variables. These linguistic variables can be expressed in positive triangular fuzzy numbers as Tables 1 and 2.

Table 1  
Linguistic variables for the importance weight of each criterion

<table><tr><td>Very low (VL)</td><td>(0,0,0.1)</td></tr><tr><td>Low (L)</td><td>(0,0.1,0.3)</td></tr><tr><td>Medium low (ML)</td><td>(0.1,0.3,0.5)</td></tr><tr><td>Medium (M)</td><td>(0.3,0.5,0.7)</td></tr><tr><td>Medium high (MH)</td><td>(0.5,0.7,0.9)</td></tr><tr><td>High (H)</td><td>(0.7,0.9,1.0)</td></tr><tr><td>Very high (VH)</td><td>(0.9,1.0,1.0)</td></tr></table>

Table 2  
Linguistic variables for the ratings

<table><tr><td>Very poor (VP)</td><td>(0,0,1)</td></tr><tr><td>Poor (P)</td><td>(0,1,3)</td></tr><tr><td>Medium poor (MP)</td><td>(1,3,5)</td></tr><tr><td>Fair (F)</td><td>(3,5,7)</td></tr><tr><td>Medium good (MG)</td><td>(5,7,9)</td></tr><tr><td>Good (G)</td><td>(7,9,10)</td></tr><tr><td>Very good (VG)</td><td>(9,10,10)</td></tr></table>

The importance weight of each criterion can be obtained by either directly assign or indirectly using pairwise comparisons [7]. In here, it is suggested that the decision makers use the linguistic variables (shown as Tables 1 and 2) to evaluate the importance of the criteria and the ratings of alternatives with respect to various criteria.

Assume that a decision group has K persons, then the importance of the criteria and the rating of alternatives with respect to each criterion can be calculated as

$$
\tilde {x} _ {i j} = \frac {1}{K} [ \tilde {x} _ {i j} ^ {1} (+) \tilde {x} _ {i j} ^ {2} (+) \cdot \cdot \cdot (+) \tilde {x} _ {i j} ^ {K} ]\tag{13}
$$

$$
\tilde {w} _ {j} = \frac {1}{K} [ \tilde {w} _ {j} ^ {1} (+) \tilde {w} _ {j} ^ {2} (+) \dots (+) \tilde {w} _ {j} ^ {K} ]\tag{14}
$$

where $\tilde { x } _ { i j } ^ { K }$ and $\tilde { w } _ { j } ^ { K }$ are the rating and the importance weight of the Kth decision maker.

As stated above, a fuzzy multicriteria group decision-making problem which can be concisely expressed in matrix format as

$$
\begin{array}{l} \tilde {\boldsymbol {D}} = \left[ \begin{array}{c c c c} \tilde {x} _ {1 1} & \tilde {x} _ {1 1} & \ldots & \tilde {x} _ {1 1} \\ \tilde {x} _ {2 1} & \tilde {x} _ {2 2} & \ldots & \tilde {x} _ {2 n} \\ \vdots & \vdots & \ldots & \vdots \\ \tilde {x} _ {m 1} & \tilde {x} _ {m 2} & \ldots & \tilde {x} _ {m n} \end{array} \right], \\ \tilde {W} = [ \tilde {w} _ {1}, \tilde {w} _ {2}, \ldots , \tilde {w} _ {n} ] \end{array}
$$

where $\tilde { x } _ { i j } , \quad \forall i , j$ and $\tilde { w } _ { j } , \ j = 1 , 2 , \ldots , n$ are linguistic variables. These linguistic variables can be described by triangular fuzzy numbers, $\boldsymbol { \tilde { x } } _ { i j } = ( a _ { i j } , b _ { i j } , c _ { i j } )$ and $\tilde { w } _ { j } = ( w _ { j 1 } , w _ { j 2 } , w _ { j 3 } )$

To avoid the complicated normalization formula used in classical TOPSIS, the linear scale transformation is used here to transform the various criteria scales into a comparable scale. Therefore, we can obtain the normalized fuzzy decision matrix denoted by R<sup>˜</sup>.

$$
\tilde {\pmb {R}} = [ \tilde {r} _ {i j} ] _ {m \times n},\tag{15}
$$

where B and C are the set of benet criteria and cost criteria, respectively, and

$$
\begin{array}{l} \tilde {r} _ {i j} = \left(\frac {a _ {i j}}{c _ {j} ^ {*}}, \frac {b _ {i j}}{c _ {j} ^ {*}}, \frac {c _ {i j}}{c _ {j} ^ {*}}\right), \quad j \in B; \\ \tilde {r} _ {i j} = \left(\frac {a _ {j} ^ {-}}{c _ {i j}}, \frac {a _ {j} ^ {-}}{b _ {i j}}, \frac {a _ {j} ^ {-}}{a _ {i j}}\right), \quad j \in C; \\ c _ {j} ^ {*} = \underset {i} {\max} c _ {i j} \quad \text { if } j \in B; \\ a _ {j} ^ {-} = \underset {i} {\min} a _ {i j} \quad \text { if } j \in C. \end{array}
$$

The normalization method mentioned above is to preserve the property that the ranges of normalized triangular fuzzy numbers belong to [0; 1].

Considering the dierent importance of each criterion, we can construct the weighted normalized fuzzy decision matrix as

$$
\tilde {V} = \left[ \tilde {v} _ {i j} \right] _ {m \times n}, \quad i = 1, 2, \dots , m, \quad j = 1, 2, \dots , n,\tag{16}
$$

where $\tilde { v } _ { i j } = \tilde { r } _ { i j } ( \cdot ) \tilde { w } _ { j }$

According to the weighted normalized fuzzy decision matrix, we know that the elements $\tilde { v } _ { i j } , \ \forall i , j$ are normalized positive triangular fuzzy numbers and their ranges belong to the closed interval [0; 1]. Then, we can dene the fuzzy positive-ideal solution (FPIS, A∗) and fuzzy negative-ideal solution

(FNIS, A−) as

$$
A ^ {*} = (\tilde {v} _ {1} ^ {*}, \tilde {v} _ {2} ^ {*}, \dots , \tilde {v} _ {n} ^ {*}),
$$

$$
A ^ {-} = (\tilde {v} _ {1} ^ {-}, \tilde {v} _ {2} ^ {-}, \dots , \tilde {v} _ {n} ^ {-}),
$$

where $\tilde { v } _ { j } ^ { * } = ( 1 , 1 , 1 )$ and $\tilde { v } _ { j } ^ { - } = ( 0 , 0 , 0 ) , j = 1 , 2 , \ldots , n .$

The distance of each alternative from $A ^ { * }$ and $A ^ { - }$ can be currently calculated as

$$
d _ {i} ^ {*} = \sum_ {j = 1} ^ {n} d (\tilde {v} _ {i j}, \tilde {v} _ {j} ^ {*}), \quad i = 1, 2, \dots , m,\tag{17}
$$

$$
d _ {i} ^ {-} = \sum_ {j = 1} ^ {n} d (\tilde {v} _ {i j}, \tilde {v} _ {j} ^ {-}), \quad i = 1, 2, \dots , m,\tag{18}
$$

where $d ( \cdot , \cdot )$ is the distance measurement between two fuzzy numbers.

A closeness coecient is dened to determine the ranking order of all alternatives once the $d _ { i } ^ { * }$ and $d _ { i } ^ { - }$ of each alternative $A _ { i } ( i = 1 , 2 , \dots , m )$ has been calculated. The closeness coecient of each alternative is calculated as

$$
C C _ {i} = \frac {d _ {i} ^ {-}}{d _ {i} ^ {*} + d _ {i} ^ {-}}, \quad i = 1, 2, \dots , m.\tag{19}
$$

Obviously, an alternative $A _ { i }$ is closer to the FPIS $( A ^ { * } )$ and farther from $\mathrm { F N I S } ( A ^ { - } )$ as $C C _ { i }$ approaches to 1. Therefore, according to the closeness coecient, we can determine the ranking order of all alternatives and select the best one from among a set of feasible alternatives.

In sum, an algorithm of the multi-person multicriteria decision making with fuzzy set approach is given in the following.

Step 1: Form a committee of decision-makers, then identify the evaluation criteria.

Step 2: Choose the appropriate linguistic variables for the importance weight of the criteria and the linguistic ratings for alternatives with respect to criteria.

Step 3: Aggregate the weight of criteria to get the aggregated fuzzy weight $\tilde { w } _ { j }$ of criterion $C _ { j } ,$ , and pool the decision makers’ opinions to get the aggregated fuzzy rating $\tilde { x } _ { i j }$ of alternative $A _ { i }$ under criterion $C _ { j }$

Step 4: Construct the fuzzy decision matrix and the normalized fuzzy decision matrix.

Step 5: Construct the weighted normalized fuzzy decision matrix.

Step 6: Determine FPIS and FNIS.

Step 7: Calculate the distance of each alternative from FPIS and FNIS, respectively.

Step 8: Calculate the closeness coecient of each alternative.

Step 9: According to the closeness coecient, the ranking order of all alternatives can be determined.

## 4. Numerical example

Suppose that a software company desires to hire a system analysis engineer. After preliminary screening, three candidates $A _ { 1 } , A _ { 2 }$ and $A _ { 3 }$ remain for further evaluation. A committee of three decision-makers, $D _ { 1 } , D _ { 2 }$ and $D _ { 3 }$ has been formed to conduct the interview and to select the most suitable candidate. Five benet criteria are considered:

(1) emotional steadiness $( C _ { 1 } ) _ { : }$

(2) oral communication skill $( C _ { 2 } )$

(3) personality $\left( C _ { 3 } \right)$

(4) past experience $( C _ { 4 } ) _ { : }$

(5) self-condence $\left( C _ { 5 } \right)$

The hierarchical structure of this decision problem is shown as Fig. 5. The proposed method is currently applied to solve this problem and the computational procedure is summarized as follows:

Step 1: The decision-makers use the linguistic weighting variables (shown in Table 1) to assess the importance of the criteria and present it in Table 3.

Step 2: The decision-makers use the linguistic rating variables (shown in Table 2) to evaluate the rating of alternatives with respect to each criterion and present it in Table 4.

Step 3: Converting the linguistic evaluation (shown in Tables 3 and 4) into triangular fuzzy numbers to construct the fuzzy decision matrix and determine the fuzzy weight of each criterion as Table 5.

Table 3  
The importance weight of the criteria

<table><tr><td></td><td> $D_1$ </td><td> $D_2$ </td><td> $D_3$ </td></tr><tr><td> $C_1$ </td><td>H</td><td>VH</td><td>MH</td></tr><tr><td> $C_2$ </td><td>VH</td><td>VH</td><td>VH</td></tr><tr><td> $C_3$ </td><td>VH</td><td>H</td><td>H</td></tr><tr><td> $C_4$ </td><td>VH</td><td>VH</td><td>VH</td></tr><tr><td> $C_5$ </td><td>M</td><td>MH</td><td>MH</td></tr></table>

![](images/2aa0cb36830633e98a212fb504643474272881709f9402ede4efb7d3ede88477.jpg)  
Fig. 5. The hierarchical structure.

The ratings of the three candidates by decision makers under all criteria

<table><tr><td rowspan="2">Criteria</td><td rowspan="2">Candidates</td><td colspan="3">Decision-makers</td></tr><tr><td> $D_1$ </td><td> $D_2$ </td><td> $D_3$ </td></tr><tr><td rowspan="3"> $C_1$ </td><td> $A_1$ </td><td>MG</td><td>G</td><td>MG</td></tr><tr><td> $A_2$ </td><td>G</td><td>G</td><td>MG</td></tr><tr><td> $A_3$ </td><td>VG</td><td>G</td><td>F</td></tr><tr><td rowspan="3"> $C_2$ </td><td> $A_1$ </td><td>G</td><td>MG</td><td>F</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>MG</td><td>G</td><td>VG</td></tr><tr><td rowspan="3"> $C_3$ </td><td> $A_1$ </td><td>F</td><td>G</td><td>G</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>G</td></tr><tr><td> $A_3$ </td><td>G</td><td>MG</td><td>VG</td></tr><tr><td rowspan="3"> $C_4$ </td><td> $A_1$ </td><td>VG</td><td>G</td><td>VG</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>G</td><td>VG</td><td>MG</td></tr><tr><td rowspan="3"> $C_5$ </td><td> $A_1$ </td><td>F</td><td>F</td><td>F</td></tr><tr><td> $A_2$ </td><td>VG</td><td>MG</td><td>G</td></tr><tr><td> $A_3$ </td><td>G</td><td>G</td><td>MG</td></tr></table>

Step 4: Constructing the normalized fuzzy decision matrix as Table 6.

Step 5: Constructing the weighted normalized fuzzy decision matrix as Table 7.

Step 6: Determine FPIS and FNIS as

$$
\begin{array}{l} A ^ {*} = [ (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1) ], \\ A ^ {-} = [ (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0) ]. \end{array}
$$

Step 7: Calculate the distance of each candidate from FPIS and FNIS, respectively, as Table 8.

Step 8: Calculate the closeness coecient of each candidate as

$$
C C _ {1} = 0. 6 2, \quad C C _ {2} = 0. 7 7, \quad C C _ {3} = 0. 7 1.
$$

Step 9: According to the closeness coecient, the ranking order of the three candidates is $A _ { 2 } , A _ { 3 }$ and $A _ { 1 }$ . Obviously, the best selection is candidate $A _ { 2 }$

## 5. Conclusion

In general, multicriteria problems adhere to uncertain and imprecise data, and fuzzy set theory is adequate to deal with it. In this paper, a linguistic decision process is proposed to solve the multiple criteria decision-making problem under fuzzy environment.

In decision-making process, very often, the assessment of alternatives with respect to criteria and the importance weight are suitable to use the linguistic variables instead of numerical values. Here, we propose a vertex method which is an eective and simple method to measure the distance between two triangular fuzzy numbers, and extend the TOPSIS procedure to the fuzzy environment. In fact, the vertex method can be easily applied to calculate the distance between any two fuzzy numbers which their membership function are linear. Under group decision-making process, it is not dicult to use other aggregation functions [8] to pool the fuzzy ratings of decision-makers in the proposed method.

Table 5  
The fuzzy decision matrix and fuzzy weights of three alternatives

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(5.7, 7.7, 9.3)</td><td>(5, 7, 9)</td><td>(5.7, 7.7, 9)</td><td>(8.33, 9.67, 10)</td><td>(3, 5, 7)</td></tr><tr><td> $A_2$ </td><td>(6.3, 8.3, 9.7)</td><td>(9, 10, 10)</td><td>(8.3, 9.7, 10)</td><td>(9, 10, 10)</td><td>(7, 9, 10)</td></tr><tr><td> $A_3$ </td><td>(6.3, 8, 9)</td><td>(7, 9, 10)</td><td>(7, 9, 10)</td><td>(7, 9, 10)</td><td>(6.3, 8.3, 9.7)</td></tr><tr><td>Weight</td><td>(0.7, 0.9, 1)</td><td>(0.9, 1, 1)</td><td>(0.77, 0.93, 1)</td><td>(0.9, 1, 1)</td><td>(0.43, 0.63, 0.83)</td></tr></table>

Table 6  
The fuzzy normalized decision matrix

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(0.59, 0.79, 0.96)</td><td>(0.5, 0.7, 0.9)</td><td>(0.57, 0.77, 0.9)</td><td>(0.83, 0.97, 1)</td><td>(0.3, 0.5, 0.7)</td></tr><tr><td> $A_2$ </td><td>(0.65, 0.86, 1)</td><td>(0.9, 1, 1)</td><td>(0.83, 0.97, 1)</td><td>(0.9, 1, 1)</td><td>(0.7, 0.9, 1)</td></tr><tr><td> $A_3$ </td><td>(0.65, 0.82, 0.93)</td><td>(0.7, 0.9, 1)</td><td>(0.7, 0.9, 1)</td><td>(0.7, 0.9, 1)</td><td>(0.63, 0.83, 0.97)</td></tr></table>

Table 7  
The fuzzy weighted normalized decision matrix

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(0.41, 0.71, 0.96)</td><td>(0.45, 0.7, 0.9)</td><td>(0.44, 0.72, 0.9)</td><td>(0.75, 0.97, 1)</td><td>(0.13, 0.32, 0.58)</td></tr><tr><td> $A_2$ </td><td>(0.46, 0.77, 1)</td><td>(0.81, 1, 1)</td><td>(0.64, 0.9, 1)</td><td>(0.81, 1, 1)</td><td>(0.3, 0.57, 0.83)</td></tr><tr><td> $A_3$ </td><td>(0.46, 0.74, 0.93)</td><td>(0.63, 0.9, 1)</td><td>(0.54, 0.84, 1)</td><td>(0.63, 0.9, 1)</td><td>(0.27, 0.52, 0.81)</td></tr></table>

Table 8  
The distance measurement

<table><tr><td></td><td> $A^{*}$ </td><td> $A^{-}$ </td></tr><tr><td> $A_{1}$ </td><td>2.10</td><td>3.45</td></tr><tr><td> $A_{2}$ </td><td>1.24</td><td>4.13</td></tr><tr><td> $A_{3}$ </td><td>1.59</td><td>3.85</td></tr></table>

Although the proposed method presented in this paper is illustrated by a personal selection problem, however, it can also be applied to problems such as information project selection, material selection and many other areas of management decision problems.

## Acknowledgements

The author gratefully acknowledges nancial support from the National Science Council, Taiwan, Republic of China, under project NSC 87-2213-E-240-001.

## References

[1] R.E. Bellman, L.A. Zadeh, Decision-making in a fuzzy environment, Management Sci. 17 (4) (1970) 141–164.

[2] J.J. Buckley, Fuzzy hierarchical analysis, Fuzzy Sets and Systems 17 (1985) 233–247.

[3] C.T. Chen, A new decision approach for solving plant location selection problem, Int. J. Prod. Econom. (1997), submitted.

[4] M. Delgado, J.L. Verdegay, M.A. Vila, Linguistic decisionmaking models, Int. J. Intelligent System 7 (1992) 479– 492.

[5] J.S. Dyer, P.C. Fishburn, R.E. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, Multiattribute utility theory: The next ten years, Management Sci. 38 (5) (1992) 645–654.

[6] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73–87.

[7] H.M. Hsu, C.T. Chen, Fuzzy hierarchical weight analysis model for multicriteria decision problem, J. Chinese Inst. Industrial Eng. 11 (3) (1994) 129–136.

[8] H.M. Hsu, C.T. Chen, Aggregation of fuzzy opinions under group decision making, Fuzzy Sets and Systems 79 (1996) 279–285.

[9] H.M. Hsu, C.T. Chen, Fuzzy credibility relation method for multiple criteria decision-making problems, Inform. Sci. 96 (1997) 79–91.

[10] C.L. Hwang, K. Yoon, Multiple Attributes Decision Making Methods and Applications, Springer, Berlin Heidelberg, 1981.

[11] A. Kaufmann, M.M. Gupta, Introduction to Fuzzy Arithmetic: Theory and Applications, Van Nostrand Reinhold, New York, 1985.

[12] D.S. Negi, Fuzzy analysis and optimization, Ph.D. Thesis, Department of Industrial Engineering, Kansas State University, 1989.

[13] J. Teghem, Jr., C. Delhaye, P.L. Kunsch, An interactive decision support system (IDSS) for multicriteria decision aid, Math. Comput. Modeling 12:10=11 (1989) 1311–1320.

[14] L.A. Zadeh, Fuzzy sets, Inform. and Control 8 (1965) 338–353.

[15] L.A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning, Inform. Sci. 8 (1975) 199–249(I), 301–357(II).

[16] H.J. Zimmermann, Fuzzy Set Theory and its Applications, 2nd edn., Kluwer Academic Publishers, Boston=Dordrecht= London, 1991.

[17] R. Zwick, E. Carlstein, D.V. Budescu, Measures of similarity among fuzzy concepts: A comparative analysis, Int. J. Approximate Reasoning 1 (1987) 221–242.