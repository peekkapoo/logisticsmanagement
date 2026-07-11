# A fuzzy approach for supplier evaluation and selection in supply chain management

Chen-Tung Chen<sup>a,</sup>, Ching-Torng Lin<sup>b</sup>, Sue-Fn Huang<sup>b</sup>

<sup>a</sup>Department of Information Management, National United University, 1, Lien Da, Kung-Ching Li, Miao-Li, Taiwan <sup>b</sup>Department of Information Management, Da-Yeh University, 112, Shan-Jiau Road, Da-Tsuen, Changhua, Taiwan

Received 14 April 2003; accepted 29 March 2005 Available online 25 May 2005

## Abstract

This paper is aimed to present a fuzzy decision-making approach to deal with the supplier selection problem in supply chain system. During recent years, how to determine suitable suppliers in the supply chain has become a key strategic consideration. However, the nature of these decisions usually is complex and unstructured. In general, many quantitative and qualitative factors such as quality, price, and flexibility and delivery performance must be considered to determine suitable suppliers. In this paper, linguistic values are used to assess the ratings and weights for these factors. These linguistic ratings can be expressed in trapezoidal or triangular fuzzy numbers. Then, a hierarchy multiple criteria decision-making (MCDM) model based on fuzzy-sets theory is proposed to deal with the supplier selection problems in the supply chain system. According to the concept of the TOPSIS, a closeness coefficient is defined to determine the ranking order of all suppliers by calculating the distances to the both fuzzy positive-ideal solution (FPIS) and fuzzy negative-ideal solution (FNIS) simultaneously. Finally, an example is shown to highlight the procedure of the proposed method at the end of this paper. This paper shows that the proposed model is very well suited as a decision making tool for supplier selection decisions. r 2005 Elsevier B.V. All rights reserved.

Keywords: Supplier selection; Supply chain; Linguistic variables; Fuzzy set theory; MCDM

## 1. Introduction

Recently, supply chain management and the supplier (vendor) selection process have received considerable attention in the business-management literature. During the 1990s, many manufacturers seek to collaborate with their suppliers in order to upgrade their management performance and competitiveness (Ittner et al., 1999; Shin et al., 2000). The material flow in a supply chain is shown in Fig. 1. The purchasing function is increasingly seen as a strategic issue in organizations. Buyer and supplier relationships in manufacturing enterprises have received a great deal of attention. When it is built on long-term relationships, a company’s supply chain creates one of the strongest barriers to entry for competitors (Briggs, 1994; Choi and Hartley, 1996). In other words, once a supplier becomes part of a well-managed and established supply chain, this relationship will have a lasting effect on the competitiveness of the entire supply chain. Therefore, the supplier selection problem has become one of the most important issues for establishing an effective supply chain system. The overall objective of supplier selection process is to reduce purchase risk, maximize overall value to the purchaser, and build the closeness and longterm relationships between buyers and suppliers (Monczka et al., 1998).

![](images/3514074cf06e09180a0e447547e0723c16ee118cd62b4d9fae93db4f554f2761.jpg)  
Fig. 1. Material flow in supply chain.

In supply chains, coordination between a manufacturer and suppliers is typically a difficult and important link in the channel of distribution. Many models have been developed for supplier selection decisions are based on rather simplistic perceptions of decision-making process (Boer et al., 1998; Lee et al., 2001). Most of these methods do not seem to address the complex and unstructured nature and context of many presentday purchasing decisions (Boer et al., 1998). In fact, many existing decision models only quantities criteria are considered for supplier selection. However, several influence factors are often not taken into account in the decision making process, such as incomplete information, additional qualitative criteria and imprecision preferences. According to the vast literature on supplier selection (Boer et al., 1998; Choi and Hartley, 1996; Weber et al., 1991), we conclude that some properties are worth considering when solving the decisionmaking problem for supplier selection. First, the criteria may consider quantitative as well as qualitative dimensions (Choi and Hartley, 1996; Dowlatshahi, 2000; Verma and Pullman, 1998; Weber et al., 1991, 1998). In general, these objectives among these criteria are conflicted. A strategic approach towards supplier selection may further emphasize the need to consider multiple criteria (Donaldson, 1994; Ellram, 1992; Swift, 1995). Second, several decision-makers are very often involved in the decision process for supplier selection (Boer et al., 1998). Third, decisionmaking is often influenced by uncertainty in practice. An increasing number of supplier decisions can be characterized as dynamic and unstructured. Situations are changing rapidly or are uncertain and decision variables are difficult or impossible to quantify (Cook, 1992). Fourth, the types of decision models can be divided into compensatory and non-compensatory methods (Boer et al., 1998; Ghodsypour and O’Brien, 1998; Roodhooft and Konings, 1996). The compensatory decision models leading to an optimal solution for dealing with supplier selection problems. The non-compensatory methods are that use a score of an alternative on a particular criterion can be compensated by high scores on other criteria. From the literature it can be concluded that in supplier selection the classic concept of ‘‘optimality’’ may not always be the most appropriate model (Boer et al., 1998). Overall speaking, we can conclude that supplier selection may involve several and different types of criteria, combination of different decision models, group decision-making and various forms of uncertainty. It is difficult to find the best way to evaluate and select supplier, and companies use a variety of different methods to deal with it. Therefore, the most important issue in the process of supplier selection is to develop a suitable method to select the right supplier.

In essential, the supplier selection problem in supply chain system is a group decision-making under multiple criteria. The degree of uncertainty, the number of decision makers and the nature of the criteria those have to be taken into account in solving this problem. In classical MCDM methods, the ratings and the weights of the criteria are known precisely (Delgado et al., 1992; Hwang and Yoon, 1981; Kaufmann and Gupta, 1991). A survey of the methods has been presented in Hwang and Yoon (1981). Technique for Order Performance by Similarity to Ideal Solution (TOPSIS), one of the known classical MCDM methods, may provide the basis for developing supplier selection models that can effectively deal with these properties. It bases upon the concept that the chosen alternative should have the shortest distance from the Positive Ideal Solution (PIS) and the farthest from the Negative Ideal Solution (NIS).

Under many conditions, crisp data are inadequate to model real-life situations. Since human judgements including preferences are often vague and cannot estimate his preference with an exact numerical value. A more realistic approach may be to use linguistic assessments instead of numerical values. In other words, the ratings and weights of the criteria in the problem are assessed by means of linguistic variables (Bellman and Zadeh, 1970; Chen, 2000; Delgado et al., 1992; Herrera et al., 1996; Herrera and Herrera-Viedma, 2000). In this paper, we further extended to the concept of TOPSIS to develop a methodology for solving supplier selection problems in fuzzy environment (Chen, 2000). Considering the fuzziness in the decision data and group decision-making process, linguistic variables are used to assess the weights of all criteria and the ratings of each alternative with respect to each criterion. We can convert the decision matrix into a fuzzy decision matrix and construct a weighted-normalized fuzzy decision matrix once the decision-makers’ fuzzy ratings have been pooled. According to the concept of TOPSIS, we define the fuzzy positive ideal solution (FPIS) and the fuzzy negative ideal solution (FNIS). And then, a vertex method is applied in this paper to calculate the distance between two fuzzy ratings.

Using the vertex method, we can calculate the distance of each alternative from FPIS and FNIS, respectively. Finally, a closeness coefficient of each alternative is defined to determine the ranking order of all alternatives. The higher value of closeness coefficient indicates that an alternative is closer to FPIS and farther from FNIS simultaneously.

The paper is organized as follows. Next section introduces the basic definitions and notations of the fuzzy numbers and linguistic variables. In Section 3, we present a fuzzy decision-making method to cope with the supplier selection problem. And then, the proposed method is illustrated with an example. Finally, some conclusions are pointed out at the end of this paper.

## 2. Fuzzy numbers and linguistic variables

In this section, some basic definitions of fuzzy sets, fuzzy numbers and linguistic variables are reviewed from Buckley (1985), Kaufmann and Gupta (1991), Negi (1989), Zadeh (1975). The basic definitions and notations below will be used throughout this paper until otherwise stated.

Definition 2.1. A fuzzy set $\tilde { A }$ in a universe of discourse X is characterized by a membership function $\mu _ { \tilde { A } } ( x )$ which associates with each element x in X a real number in the interval [0,1]. The function value $\mu _ { \tilde { A } } ( x )$ is termed the grade of membership of x in A<sup>\~</sup> (Kaufmann and Gupta, 1991).

Definition 2.2. A fuzzy set $\tilde { \boldsymbol { A } }$ in the universe of discourse X is convex if and only if

$$
\mu_ {\tilde {A}} (\lambda x _ {1} + (1 - \lambda) x _ {2}) \geqslant \min (\mu_ {\tilde {A}} (x _ {1}), \mu_ {\tilde {A}} (x _ {2}))\tag{1}
$$

for all $x _ { 1 } , x _ { 2 }$ in X and all $\lambda \in [ 0 , 1 ]$ , where min denotes the minimum operator (Klir and Yuan, 1995).

Definition 2.3. The height of a fuzzy set is the largest membership grade attained by any element in that set. A fuzzy set A<sup>\~</sup> in the universe of discourse X is called normalized when the height of $\tilde { \boldsymbol { A } }$ is equal to 1 (Klir and Yuan, 1995).

Definition 2.4. A fuzzy number is a fuzzy subset in the universe of discourse X that is both convex and normal. Fig. 2 shows a fuzzy number $\tilde { n }$ in the universe of discourse X that conforms to this definition (Kaufmann and Gupta, 1991).

Definition 2.5. The a-cut of fuzzy number n\~ is defined as

$$
\tilde {n} ^ {\alpha} = \{x _ {i}: \mu_ {\tilde {n}} (x _ {i}) \geqslant \alpha , x _ {i} \in X \},\tag{2}
$$

where $\alpha \in [ 0 , 1 ]$

The symbol $\tilde { n } ^ { \alpha }$ represents a non-empty bounded interval contained in X, which can be denoted by $\tilde { n } ^ { \alpha } = [ n _ { l } ^ { \alpha } , n _ { u } ^ { \alpha } ] .$ $n _ { l } ^ { \alpha }$ and $n _ { u } ^ { \alpha }$ are the lower and upper bounds of the closed interval, respectively (Kaufmann and Gupta, 1991; Zimmermann, 1991). For a fuzzy number n\~, if $n _ { l } ^ { \alpha } > 0$ and $n _ { u } ^ { \alpha } \leqslant 1$ for all $\alpha \in [ 0 , 1 ]$ , then n\~ is called a standardized (normalized) positive fuzzy number (Negi, 1989).

Definition 2.6. A positive trapezoidal fuzzy number (PTFN) n\~ can be defined as $( n _ { 1 } , ~ n _ { 2 } , ~ n _ { 3 } , ~ n _ { 4 } )$ 2 shown in Fig. 3. The membership function, $\mu _ { \tilde { n } } ( x )$ is defined as (Kaufmann and Gupta, 1991)

$$
\mu_ {\vec {n}} (x) = \left\{ \begin{array}{l l} 0, & x <   n _ {1}, \\ \frac {x - n _ {1}}{n _ {2} - n _ {1}}, & n _ {1} \leqslant x \leqslant n _ {2}, \\ 1, & n _ {2} \leqslant x \leqslant n _ {3}, \\ \frac {x - n _ {4}}{n _ {3} - n _ {4}}, & n _ {3} \leqslant x \leqslant n _ {4}, \\ 0, & x > n _ {4}. \end{array} \right.\tag{3}
$$

For a trapezoidal fuzzy number $\tilde { n } = ( n _ { 1 } , n _ { 2 } , n _ { 3 } , n _ { 4 } )$ if $n _ { 2 } = n _ { 3 }$ , then n\~ is called a triangular fuzzy number. A non-fuzzy number r can be expressed as $( r , r , r , r )$ . By the extension principle (Dubois and Prade, 1980), the fuzzy sum  and fuzzy subtraction  of any two trapezoidal fuzzy numbers are also trapezoidal fuzzy numbers; but the multiplication $\otimes$ of any two trapezoidal fuzzy numbers is only an approximate trapezoidal fuzzy number. Given any two positive trapezoidal fuzzy numbers, $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } , m _ { 4 } )$ $\tilde { n } = ( n _ { 1 } , n _ { 2 } , n _ { 3 } , n _ { 4 } )$ and a positive real number r, some main operations of fuzzy numbers m\~ and n\~ can be expressed as follows:

![](images/b6210c5b1a2752a5334cc5a438b24a954aa2e1157264739ea068b48ffe161a85.jpg)  
Fig. 2. Fuzzy number n\~.

![](images/2e1f8738cce8eb07a236adfea3e7d7692e55e321f680372036b302260fa898f4.jpg)  
Fig. 3. Trapezoidal fuzzy number n\~.

$$
\tilde {m} \oplus \tilde {n} = [ m _ {1} + n _ {1}, m _ {2} + n _ {2}, m _ {3} + n _ {3}, m _ {4} + n _ {4} ],\tag{4}
$$

$$
\tilde {m} \ominus \tilde {n} = [ m _ {1} - n _ {4}, m _ {2} - n _ {3}, m _ {3} - n _ {2}, m _ {4} - n _ {1} ],\tag{5}
$$

$$
\tilde {m} \otimes r = [ m _ {1} r, m _ {2} r, m _ {3} r, m _ {4} r ],\tag{6}
$$

$$
\tilde {m} \otimes \tilde {n} \cong [ m _ {1} n _ {1}, m _ {2} n _ {2}, m _ {3} n _ {3}, m _ {4} n _ {4} ].\tag{7}
$$

Definition 2.7. A matrix $\tilde { \bf D }$ is called a fuzzy matrix if at least one element is a fuzzy number (Buckley, 1985).

Definition 2.8. A linguistic variable is a variable whose values are expressed in linguistic terms (Zimmermann, 1991).

The concept of a linguistic variable is very useful in dealing with situations, which are too complex or not well defined to be reasonably described in conventional quantitative expressions (Zimmermann, 1991). For example, ‘‘weight’’ is a linguistic variable whose values are very low, low, medium, high, very high, etc. Fuzzy numbers can also represent these linguistic values.

Let $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } , m _ { 4 } )$ and $\tilde { n } = ( n _ { 1 } , n _ { 2 } , n _ { 3 } , n _ { 4 } )$ be two trapezoidal fuzzy numbers. Then the distance between them can be calculated by using the vertex method as (Chen, 2000)

$$
\begin{array}{l} d _ {v} (\tilde {m}, \tilde {n}) \\ = \sqrt {\frac {1}{4} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} + (m _ {4} - n _ {4}) ^ {2} ]}. \end{array}\tag{8}
$$

Let $\tilde { m } = ( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ and $\tilde { n } = ( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ be two triangular fuzzy numbers. Then the distance between them can be calculated by using the vertex method as (Chen, 2000)

$$
\begin{array}{l} d _ {v} (\tilde {m}, \tilde {n}) \\ = \sqrt {\frac {1}{3} [ (m _ {1} - n _ {1}) ^ {2} + (m _ {2} - n _ {2}) ^ {2} + (m _ {3} - n _ {3}) ^ {2} ]}. \end{array}\tag{9}
$$

The vertex method is an effective and simple method to calculate the distance between two trapezoidal fuzzy numbers. According to the vertex method, two trapezoidal fuzzy numbers m\~ and n\~ are identical if and only if $d _ { v } ( \tilde { m } , \tilde { n } ) = 0$ . Let $\tilde { m } ,$ n\~ and $\tilde { p }$ be three trapezoidal fuzzy numbers. Fuzzy number n\~ is closer to fuzzy number m\~ than the other fuzzy number $\tilde { p }$ if and only if $d _ { v } ( \tilde { m } , \tilde { n } ) < d _ { v } ( \tilde { m } , \tilde { p } )$ (Chen, 2000).

## 3. Proposed method for supplier selection

A systematic approach to extend the TOPSIS is proposed to solve the supplier-selection problem under a fuzzy environment in this section. In this paper the importance weights of various criteria and the ratings of qualitative criteria are considered as linguistic variables. Because linguistic assessments merely approximate the subjective judgment of decision-makers, we can consider linear trapezoidal membership functions to be adequate for capturing the vagueness of these linguistic assessments (Delgado et al., 1998; Herrera et al., 1996; Herrera and Herrera-Viedma, 2000). These linguistic variables can be expressed in positive trapezoidal fuzzy numbers, as in Figs. 4 and 5. The importance weight of each criterion can be by either directly assigning or indirectly using pairwise comparison (Cook, 1992). It is suggested in this paper that the decision-makers use the linguistic variables shown in Figs. 4 and 5 to evaluate the importance of the criteria and the ratings of alternatives with respect to qualitative criteria. For example, the linguistic variable ‘‘Medium High (MH)’’ can be represented as ð0:5; 0:6; 0:7; 0:8Þ, the membership function of

![](images/ef5c8ac894d075a30efd99105d9f9215129d376744b078b56d8fbcf190f2534e.jpg)  
Fig. 4. Linguistic variables for importance weight of each criterion.

![](images/589ee567fc21dd567cd11f11fe32a6cffff5f57d8713658237ec884c49d773af.jpg)  
Fig. 5. Linguistic variables for ratings.

which is

$$
\mu_ {\text {Medium High}} (x) = \left\{ \begin{array}{l l} 0, & x <   0. 5, \\ \frac {x - 0 . 5}{0 . 6 - 0 . 5}, & 0. 5 \leqslant x \leqslant 0. 6, \\ 1, & 0. 6 \leqslant x \leqslant 0. 7, \\ \frac {x - 0 . 8}{0 . 7 - 0 . 8}, & 0. 7 \leqslant x \leqslant 0. 8, \\ 0, & x > 0. 8. \end{array} \right.\tag{10}
$$

The linguistic variable ‘‘Very Good $\mathbf { ( V G ) } ^ { \prime }$ can be represented as (8,9,9,10), the membership function of which is

$$
\mu_ {\text { Very   Good }} (x) = \left\{ \begin{array}{l l} 0, & x <   8, \\ \frac {x - 8}{9 - 8}, & 8 \leqslant x \leqslant 9, \\ 1, & 9 \leqslant x \leqslant 1 0. \end{array} \right.\tag{11}
$$

In fact, supplier selection in supply chain system is a group multiple-criteria decision-making (GMCDM) problem, which may be described by means of the following sets:

(i) a set of K decision-makers called $E = \{ D _ { 1 }$ $D _ { 2 } , \ldots , D _ { K } \} ;$

(ii) a set of m possible suppliers called $A = \{ A _ { 1 }$ $A _ { 2 } , \ldots , A _ { m } \} ;$

(iii) a set of n criteria, $C = \{ C _ { 1 } , C _ { 2 } , \ldots , C _ { n } \}$ , with which supplier performances are measured;

(iv) a set of performance ratings of $\begin{array} { r } { A _ { i } ( i = 1 , 2 , . . . , } \end{array}$ mÞ with respect to criteria $C _ { j } ( j = 1 , 2 , \ldots , n )$ called $X = \{ x _ { i j } , i = 1 , 2 , . . . , m , j = 1 , 2 , . . . , n \}$

Assume that a decision group has K decision makers, and the fuzzy rating of each decisionmaker $D _ { k } ( k = 1 , 2 , \ldots , K )$ can be represented as a positive trapezoidal fuzzy number $\tilde { R _ { k } } ( k = 1 , 2 , \ldots$ KÞ with membership function $\mu _ { \tilde { R } _ { k } } ( x )$ . A good aggregation method should be considered the range of fuzzy rating of each decision-maker. It means that the range of aggregated fuzzy rating must include the ranges of all decision-makers fuzzy ratings. Let the fuzzy ratings of all decisionmakers be trapezoidal fuzzy numbers $\tilde { R } _ { k } = ( a _ { k } , b _ { k }$ 4 $c _ { k } , d _ { k } ) , k = 1 , 2 , \ldots , K$ . Then the aggregated fuzzy rating can be defined as

$$
\tilde {R} = (a, b, c, d), \quad k = 1, 2, \ldots , K\tag{12}
$$

where

$$
a = \min _ {k} \{a _ {k} \}, \quad b = \frac {1}{K} \sum_ {k = 1} ^ {K} b _ {k},
$$

$$
c = \frac {1}{K} \sum_ {k = 1} ^ {K} c _ {k}, d = \max _ {k} \{d _ {k} \}.
$$

Let the fuzzy rating and importance weight of the kth decision maker be $\tilde { x } _ { i j k } = ( a _ { i j k } , b _ { i j k } , c _ { i j k } , d _ { i j k } )$ and $\tilde { w } _ { j k } = ( w _ { j k 1 } , w _ { j k 2 } , w _ { j k 3 } , w _ { j k 4 } ) ;$ $i = 1 , 2 , \dots , m ,$ $j = 1 , 2 , \dots , n ,$ , respectively. Hence, the aggregated fuzzy ratings $( \tilde { x } _ { i j } )$ of alternatives with respect to each criterion can be calculated as

$$
\tilde {x} _ {i j} = (a _ {i j}, b _ {i j}, c _ {i j}, d _ {i j})\tag{13}
$$

where

$$
a _ {i j} = \min _ {k} \{a _ {i j k} \}, b _ {i j} = \frac {1}{K} \sum_ {k = 1} ^ {K} b _ {i j k},
$$

$$
c _ {i j} = \frac {1}{K} \sum_ {k = 1} ^ {K} c _ {i j k}, d _ {i j} = \max _ {k} \{d _ {i j k} \}.
$$

The aggregated fuzzy weights $( \tilde { w } _ { j } )$ of each criterion can be calculated as

$$
\tilde {w} _ {j} = (w _ {j 1}, w _ {j 2}, w _ {j 3}, w _ {j 4}),
$$

where

$$
w _ {j 1} = \min _ {k} \{w _ {j k 1} \}, \quad w _ {j 2} = \frac {1}{K} \sum_ {k = 1} ^ {K} w _ {j k 2},\tag{14}
$$

$$
w _ {j 3} = \frac {1}{K} \sum_ {k = 1} ^ {K} w _ {j k 3}, \quad w _ {j 4} = \max _ {k} \{w _ {j k 4} \}.
$$

As stated above, a supplier-selection problem can be concisely expressed in matrix format as follows:

$$
\begin{array}{l} \tilde {\mathbf {D}} = \left[ \begin{array}{c c c c} \tilde {x} _ {1 1} & \tilde {x} _ {1 2} & \ldots .. & \tilde {x} _ {1 n} \\ \tilde {x} _ {2 1} & \tilde {x} _ {2 2} & \ldots .. & \tilde {x} _ {2 n} \\ \vdots & \vdots & \ldots .. & \vdots \\ \tilde {x} _ {m 1} & \tilde {x} _ {m 2} & \ldots .. & \tilde {x} _ {m n} \end{array} \right], \\ \tilde {W} = [ \tilde {w} _ {1},   \tilde {w} _ {2},   \ldots   \tilde {w} _ {n} ], \end{array}
$$

where $\tilde { x } _ { i j } = ( a _ { i j } , b _ { i j } , c _ { i j } , d _ { i j } )$ and $\tilde { w } _ { j } = ( w _ { j 1 } , w _ { j 2 } , w _ { j 3 }$ $w _ { j 4 } ) ; i = 1 , 2 , . . . , m , j = 1 , 2 , . . . , n$ can be approximated by positive trapezoidal fuzzy numbers.

To avoid complexity of mathematical operations in a decision process, the linear scale transformation is used here to transform the various criteria scales into comparable scales. The set of criteria can be divided into benefit criteria (the larger the rating, the greater the preference) and cost criteria (the smaller the rating, the greater the preference). Therefore, the normalized fuzzy-decision matrix can be represented as

$$
\tilde {\mathbf {R}} = [ \tilde {r} _ {i j} ] _ {m \times n},\tag{15}
$$

where B and C are the sets of benefit criteria and cost criteria, respectively, and

$$
\begin{array}{l} \tilde {r} _ {i j} = \left(\frac {a _ {i j}}{d _ {j} ^ {*}}, \frac {b _ {i j}}{d _ {j} ^ {*}}, \frac {c _ {i j}}{d _ {j} ^ {*}}, \frac {d _ {i j}}{d _ {j} ^ {*}}\right), \quad j \in B, \\ \tilde {r} _ {i j} = \left(\frac {a _ {j} ^ {-}}{d _ {i j}}, \frac {a _ {j} ^ {-}}{c _ {i j}}, \frac {a _ {j} ^ {-}}{b _ {i j}}, \frac {a _ {j} ^ {-}}{a _ {i j}}\right), \quad j \in C, \\ d _ {j} ^ {*} = \max _ {i} d _ {i j}, \quad j \in B, \\ a _ {j} ^ {-} = \min _ {i} a _ {i j}, \quad j \in C. \end{array}
$$

The normalization method mentioned above is designed to preserve the property in which the elements $\tilde { r } _ { i j } , \forall i , j$ are standardized (normalized) trapezoidal fuzzy numbers.

Considering the different importance of each criterion, the weighted normalized fuzzy-decision matrix is constructed as

$$
\tilde {V} = [ \tilde {v} _ {i j} ] _ {m \times n}, i = 1, 2, \ldots , m, j = 1, 2, \ldots , n,\tag{16}
$$

where

$$
\tilde {v} _ {i j} = \tilde {r} _ {i j} (\cdot) \tilde {w} _ {j}.
$$

According to the weighted normalized fuzzydecision matrix, normalized positive trapezoidal fuzzy numbers can also approximate the elements $\tilde { v } _ { i j } , \forall i , j .$ . Then, the fuzzy positive-ideal solution (FPIS, A<sup></sup>) and fuzzy negative-ideal solution (FNIS, A<sup></sup>) can be defined as

$$
A ^ {*} = (\tilde {v} _ {1} ^ {*}, \tilde {v} _ {2} ^ {*}, \dots , \tilde {v} _ {n} ^ {*}),\tag{17}
$$

$$
A ^ {-} = (\tilde {v} _ {1} ^ {-}, \tilde {v} _ {2} ^ {-}, \dots , \tilde {v} _ {n} ^ {-}),\tag{18}
$$

where

$$
\begin{array}{c} \tilde {v} _ {j} ^ {*} = \max _ {i} \{v _ {i j 4} \} \quad \text { and } \quad \tilde {v} _ {j} ^ {-} = \min _ {i} \{v _ {i j 1} \}, \\ i = 1, 2, \ldots , m, j = 1, 2, \ldots , n. \end{array}
$$

The distance of each alternative (supplier) from $A ^ { * }$ and $A ^ { - }$ can be currently calculated as

$$
d _ {i} ^ {*} = \sum_ {j = 1} ^ {n} d _ {v} (\tilde {v} _ {i j}, \tilde {v} _ {j} ^ {*}), \quad i = 1, 2, \ldots , m,\tag{19}
$$

$$
d _ {i} ^ {-} = \sum_ {j = 1} ^ {n} d _ {v} (\tilde {v} _ {i j}, \tilde {v} _ {j} ^ {-}), \quad i = 1, 2, \dots , m,\tag{20}
$$

where $d _ { v } ( \cdot , \cdot )$ is the distance measurement between two fuzzy numbers.

A closeness coefficient is defined to determine the ranking order of all possible suppliers once $d _ { i } ^ { * }$ and $d _ { i } ^ { - }$ of each supplier $A _ { i } ( i = 1 , 2 , \dots , m )$ has been calculated. The closeness coefficient represents the distances to the fuzzy positive-ideal solution $( A ^ { * } )$ and the fuzzy negative-ideal solution $( A ^ { - } )$ simultaneously by taking the relative closeness to the fuzzy positive-ideal solution. The closeness coefficient (CC ) of each alternative (supplier) is calculated as

$$
\mathrm{CC} _ {i} = \frac {d _ {i} ^ {-}}{d _ {i} ^ {*} + d _ {i} ^ {-}}, \quad i = 1, 2, \dots , m.\tag{21}
$$

It is clear that $\mathrm { C C } _ { i } = 1$ if $A _ { i } = A ^ { * }$ and $\mathrm { C C } _ { i } = 0$ if $A _ { i } = A ^ { - }$ . In other words, supplier $A _ { i }$ is closer to the FPIS $( A ^ { * } )$ and farther from FNIS (A<sup></sup>) as CC approaches to 1. According to the descending order of $\mathbf { C } \mathbf { C } _ { i }$ , we can determine the ranking order of all suppliers and select the best one from among a set of feasible suppliers. Although we can determine the ranking order of all feasible suppliers, a more realistic approach may be to use a linguistic variable to describe the current assessment status of each supplier in accordance with its closeness coefficient. In order to describe the assessment status of each supplier, we divide the interval [0,1] into five sub-intervals. Five linguistic variables with respect to the sub-intervals are defined to divide the assessment status of supplier into five classes. The decision rules of the

Table 1 Approval status

<table><tr><td>Closeness coefficient (CCi)</td><td>Assessment status</td></tr><tr><td>CCi ∈ [0, 0.2)</td><td>Do not recommend</td></tr><tr><td>CCi ∈ [0.2, 0.4)</td><td>Recommend with high risk</td></tr><tr><td>CCi ∈ [0.4, 0.6)</td><td>Recommend with low risk</td></tr><tr><td>CCi ∈ [0.6, 0.8)</td><td>Approved</td></tr><tr><td>CCi ∈ [0.8, 1.0]</td><td>Approved and preferred</td></tr></table>

five classes are shown in Table 1. According to the Table 1, it means that

If $\mathrm { C C } _ { i } \in [ 0 , 0 . 2 )$ , then supplier $A _ { i }$ belongs to Class I and the assessment status of supplier $A _ { i }$ is ‘‘not recommend’’;

If $\mathbf { C C } _ { i } \in [ 0 . 2 , 0 . 4 )$ , then supplier $A _ { i }$ belongs to Class II and the assessment status of supplier $A _ { i }$ is ‘‘recommend with high risk’’;

If $\mathbf { C C } _ { i } \in [ 0 . 4 , 0 . 6 )$ , then supplier $A _ { i }$ belongs to Class III and the assessment status of supplier $A _ { i }$ is ‘‘recommend with low risk’’;

If $\mathbf { C C } _ { i } \in [ 0 . 6 , 0 . 8 )$ , then supplier $A _ { i }$ belongs to Class IV and the assessment status of supplier $A _ { i }$ is $ { \mathrm { ~  ~ \hat { ~ } { ~ a ~ } p p r o v e d } } ^ { \prime }$ ;

If $\mathbf { C C } _ { i } \in [ 0 . 8 , 1 . 0 ]$ , then supplier $A _ { i }$ belongs to Class V and the assessment status of supplier $A _ { i }$ is ‘‘approved and preferred to recommend.’’

According to Table 1 and decision rules, we can use a linguistic variable to describe the current assessment status of each supplier. In addition, if any two suppliers belong to the same class of assessment status, the closeness coefficient value is used to determine their rank.

In summation, an algorithm of the fuzzy decision-making method for dealing with the supplier selection is given as follows.

Step 1: Form a committee of decision-makers, and then identify the evaluation criteria.

Step 2: Choose the appropriate linguistic variables for the importance weight of the criteria and the linguistic ratings for suppliers.

Step 3: Aggregate the weight of criteria to get the aggregated fuzzy weight $\tilde { w } _ { j }$ of criterion $C _ { j }$ , and pool the decision-makers’ ratings to get the aggregated fuzzy rating $\tilde { x } _ { i j }$ of supplier $A _ { i }$ under criterion $C _ { j }$

Step 4: Construct the fuzzy-decision matrix and the normalized fuzzy-decision matrix.

Step 5: Construct weighted normalized fuzzydecision matrix.

Step 6: Determine FPIS and FNIS.

Step 7: Calculate the distance of each supplier from FPIS and FNIS, respectively.

Step 8: Calculate the closeness coefficient of each supplier.

Step 9: According to the closeness coefficient, we can understand the assessment status of each supplier and determine the ranking order of all suppliers.

## 4. Numerical example

A high-technology manufacturing company desires to select a suitable material supplier to purchase the key components of new products. After preliminary screening, five candidates $( A _ { 1 }$ $A _ { 2 } , A _ { 3 } , A _ { 4 } , A _ { 5 } )$ remain for further evaluation. A committee of three decision-makers, $D _ { 1 } , D _ { 2 }$ and $D _ { 3 }$ , has been formed to select the most suitable supplier. Five benefit criteria are considered:

(1) profitability of supplier $( C _ { 1 } )$

(2) relationship closeness $( C _ { 2 } ) _ { : }$

(3) technological capability $( C _ { 3 } ) _ { : }$

(4) conformance quality $( C _ { 4 } )$

(5) conflict resolution $( C _ { 5 } )$

The hierarchical structure of this decision problem is shown in Fig. 6. The proposed method is currently applied to solve this problem, the computational procedure of which is summarized as follows:

Step 1: Three decision-makers use the linguistic weighting variables shown in Fig. 4 to assess the importance of the criteria. The importance weights of the criteria determined by these three decisionmakers are shown in Table 2.

Step 2: Three decision-makers use the linguistic rating variables shown in Fig. 5 to evaluate the ratings of candidates with respect to each criterion. The ratings of the five candidates by the decisionmakers under the various criteria are shown in Table 3.

Table 2  
![](images/7d7c1a5700670a42651e4caef9b617f50e2c4488590dc04dddd98eb18c6de455.jpg)  
Fig. 6. Hierarchical structure of decision problem.  
Ratings of the five candidates by decision-makers under various criteria

Importance weight of criteria from three decision-makers  
Table 3

<table><tr><td rowspan="2">Criteria</td><td colspan="3">Decision-makers</td></tr><tr><td> $D_1$ </td><td> $D_2$ </td><td> $D_3$ </td></tr><tr><td> $C_1$ </td><td>H</td><td>H</td><td>H</td></tr><tr><td> $C_2$ </td><td>VH</td><td>VH</td><td>VH</td></tr><tr><td> $C_3$ </td><td>VH</td><td>VH</td><td>H</td></tr><tr><td> $C_4$ </td><td>H</td><td>H</td><td>H</td></tr><tr><td> $C_5$ </td><td>H</td><td>H</td><td>H</td></tr></table>

Step 3: Then the linguistic evaluations shown in Tables 2 and 3 are converted into trapezoidal fuzzy numbers to construct the fuzzy-decision matrix and determine the fuzzy weight of each criterion, as in Table 4.

Step 4: The normalized fuzzy-decision matrix is constructed as in Table 5.

Step 5: Weighted normalized fuzzy-decision matrix is constructed as in Table 6.

Step 6: Determine FPIS and FNIS asA<sup></sup> ¼ ½ð0:9; 0:9; 0:9; 0:9Þ; ð1; 1; 1; 1Þ; ð1; 1; 1; 1Þ; ð0:9;0:9; 0:9; 0:9Þ; ð0:9; 0:9; 0:9; 0:9Þ-,A<sup></sup> ¼ ½ð0:35; 0:35; 0:35; 0:35Þ; ð0:4; 0:4; 0:4; 0:4Þ;ð0:35; 0:35; 0:35; 0:35Þ; ð0:35; 0:35; 0:35; 0:35Þ; ð0:35;0:35; 0:35; 0:35Þ-.

<table><tr><td rowspan="2">Criteria</td><td rowspan="2">Suppliers</td><td colspan="3">Decision-makers</td></tr><tr><td> $D_1$ </td><td> $D_2$ </td><td> $D_3$ </td></tr><tr><td rowspan="5"> $C_1$ </td><td> $A_1$ </td><td>MG</td><td>MG</td><td>MG</td></tr><tr><td> $A_2$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_3$ </td><td>VG</td><td>VG</td><td>G</td></tr><tr><td> $A_4$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_5$ </td><td>MG</td><td>MG</td><td>MG</td></tr><tr><td rowspan="5"> $C_2$ </td><td> $A_1$ </td><td>MG</td><td>MG</td><td>VG</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>VG</td><td>G</td><td>G</td></tr><tr><td> $A_4$ </td><td>G</td><td>G</td><td>MG</td></tr><tr><td> $A_5$ </td><td>MG</td><td>G</td><td>G</td></tr><tr><td rowspan="5"> $C_3$ </td><td> $A_1$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>VG</td><td>VG</td><td>G</td></tr><tr><td> $A_4$ </td><td>MG</td><td>MG</td><td>G</td></tr><tr><td> $A_5$ </td><td>MG</td><td>MG</td><td>MG</td></tr><tr><td rowspan="5"> $C_4$ </td><td> $A_1$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_2$ </td><td>G</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_4$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_5$ </td><td>MG</td><td>MG</td><td>G</td></tr><tr><td rowspan="5"> $C_5$ </td><td> $A_1$ </td><td>G</td><td>G</td><td>G</td></tr><tr><td> $A_2$ </td><td>VG</td><td>VG</td><td>VG</td></tr><tr><td> $A_3$ </td><td>G</td><td>VG</td><td>G</td></tr><tr><td> $A_4$ </td><td>G</td><td>G</td><td>VG</td></tr><tr><td> $A_5$ </td><td>MG</td><td>MG</td><td>MG</td></tr></table>

Table 4  
Fuzzy-decision matrix and fuzzy weights of five candidates

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(5,6,7,8)</td><td>(5,7,8,10)</td><td>(7,8,8,9)</td><td>(7,8,8,9)</td><td>(7,8,8,9)</td></tr><tr><td> $A_2$ </td><td>(7,8,8,9)</td><td>(8,9,10,10)</td><td>(8,9,10,10)</td><td>(7,8.7,9.3,10)</td><td>(8,9,10,10)</td></tr><tr><td> $A_3$ </td><td>(7,8.7,9.3,10)</td><td>(7,8.3,8.7,10)</td><td>(7,8.7,9.3,10)</td><td>(8,9,10,10)</td><td>(7,8.3,8.7,10)</td></tr><tr><td> $A_4$ </td><td>(7,8,8,9)</td><td>(5,7.3,7.7,9)</td><td>(5,6.7,7.3,9)</td><td>(7,8,8,9)</td><td>(7,8.3,8.7,10)</td></tr><tr><td> $A_5$ </td><td>(5,6,7,8)</td><td>(5,7.3,7.7,9)</td><td>(5,6,7,8)</td><td>(5,6.7,7.3,9)</td><td>(5,6,7,8)</td></tr><tr><td>Weight</td><td>(0.7,0.8,0.8,0.9)</td><td>(0.8,0.9,1.0,1.0)</td><td>(0.7,0.87,0.93,1.0)</td><td>(0.7,0.8,0.8,0.9)</td><td>(0.7,0.8,0.8,0.9)</td></tr></table>

Table 5  
Normalized fuzzy-decision matrix

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(0.5,0.6,0.7,0.8)</td><td>(0.5,0.7,0.8,1)</td><td>(0.7,0.8,0.8,0.9)</td><td>(0.7,0.8,0.8,0.9)</td><td>(0.7,0.8,0.8,0.9)</td></tr><tr><td> $A_2$ </td><td>(0.7,0.8,0.8,0.9)</td><td>(0.8,0.9,1,1)</td><td>(0.8,0.9,1,1)</td><td>(0.7,0.87,0.93,1)</td><td>(0.8,0.9,1,1)</td></tr><tr><td> $A_3$ </td><td>(0.7,0.87,0.93,1)</td><td>(0.7,0.83,0.87,1)</td><td>(0.7,0.87,0.93,1)</td><td>(0.8,0.9,1,1)</td><td>(0.7,0.83,0.87,1)</td></tr><tr><td> $A_4$ </td><td>(0.7,0.8,0.8,0.9)</td><td>(0.5,0.73,0.77,0.9)</td><td>(0.5,0.67,0.73,0.9)</td><td>(0.7,0.8,0.8,0.9)</td><td>(0.7,0.83,0.87,1)</td></tr><tr><td> $A_5$ </td><td>(0.5,0.6,0.7,0.8)</td><td>(0.5,0.73,0.77,0.9)</td><td>(0.5,0.6,0.7,0.8)</td><td>(0.5,0.67,0.73,0.9)</td><td>(0.5,0.6,0.7,0.8)</td></tr></table>

Table 6  
Weighted normalized fuzzy-decision matrix

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $A_1$ </td><td>(0.35,0.48,0.56,0.72)</td><td>(0.4,0.63,0.8,1)</td><td>(0.49,0.7,0.74,0.9)</td><td>(0.49,0.64,0.64,0.81)</td><td>(0.49,0.64,0.64,0.81)</td></tr><tr><td> $A_2$ </td><td>(0.49,0.64,0.64,0.81)</td><td>(0.64,0.81,1,1)</td><td>(0.56,0.78,0.93,1)</td><td>(0.49,0.7,0.74,0.9)</td><td>(0.56,0.72,0.8,0.9)</td></tr><tr><td> $A_3$ </td><td>(0.49,0.7,0.74,0.9)</td><td>(0.56,0.75,0.87,1)</td><td>(0.49,0.76,0.86,1)</td><td>(0.56,0.72,0.8,0.9)</td><td>(0.49,0.66,0.7,0.9)</td></tr><tr><td> $A_4$ </td><td>(0.49,0.64,0.64,0.81)</td><td>(0.4,0.66,0.77,0.9)</td><td>(0.35,0.58,0.68,0.9)</td><td>(0.49,0.64,0.64,0.81)</td><td>(0.49,0.66,0.7,0.9)</td></tr><tr><td> $A_5$ </td><td>(0.35,0.48,0.56,0.72)</td><td>(0.4,0.66,0.77,0.9)</td><td>(0.35,0.52,0.65,0.8)</td><td>(0.35,0.54,0.58,0.81)</td><td>(0.35,0.48,0.56,0.72)</td></tr></table>

Table 7

Step 7: Calculate the distance of each supplier from FPIS and FNIS with respect to each criterion, respectively, as Tables 7 and 8.

Step 8: Calculate $d _ { i } ^ { * }$ and $d _ { i } ^ { - }$ of five possible suppliers $A _ { i } ( i = 1 , 2 , \dots , 5 )$ as Table 9.

Step 9: Calculate the closeness coefficient of each supplier as

$$
\begin{array}{l l} \mathrm{CC} _ {1} = 0. 5 0, & \mathrm{CC} _ {2} = 0. 6 4, \quad \mathrm{CC} _ {3} = 0. 6 2, \\ \mathrm{CC} _ {4} = 0. 5 1, & \mathrm{CC} _ {5} = 0. 4 0. \end{array}
$$

Step 10: According to the closeness coefficients of five suppliers and the approval status level, we know that suppliers $A _ { 2 }$ and $A _ { 3 }$ belong to Class IV, the assessment status of which are ‘‘Approved’’. Suppliers $A _ { 1 } , A _ { 4 }$ and $A _ { 5 }$ belong to Class III. This means that their assessment status is ‘‘Recommend

Distances between $A _ { i } ( i = 1 , 2 , \dots , 5 )$ and $A ^ { * }$ with respect to each criterion

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $d(A_{1},A^*)$ </td><td>0.4</td><td>0.37</td><td>0.33</td><td>0.28</td><td>0.28</td></tr><tr><td> $d(A_{2},A^*)$ </td><td>0.28</td><td>0.2</td><td>0.25</td><td>0.24</td><td>0.2</td></tr><tr><td> $d(A_{3},A^*)$ </td><td>0.24</td><td>0.26</td><td>0.29</td><td>0.2</td><td>0.26</td></tr><tr><td> $d(A_{4},A^*)$ </td><td>0.28</td><td>0.37</td><td>0.42</td><td>0.28</td><td>0.26</td></tr><tr><td> $d(A_{5},A^*)$ </td><td>0.4</td><td>0.37</td><td>0.45</td><td>0.37</td><td>0.4</td></tr></table>

Table 9

Table 8 Distances between $A _ { i } ( i = 1 , 2 , \dots , 5 )$ and $A ^ { - }$ with respect to each criterion

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $d(A_{1},A^{-})$ </td><td>0.22</td><td>0.38</td><td>0.39</td><td>0.32</td><td>0.32</td></tr><tr><td> $d(A_{2},A^{-})$ </td><td>0.32</td><td>0.49</td><td>0.5</td><td>0.39</td><td>0.41</td></tr><tr><td> $d(A_{3},A^{-})$ </td><td>0.39</td><td>0.43</td><td>0.47</td><td>0.41</td><td>0.37</td></tr><tr><td> $d(A_{4},A^{-})$ </td><td>0.32</td><td>0.34</td><td>0.34</td><td>0.32</td><td>0.37</td></tr><tr><td> $d(A_{5},A^{-})$ </td><td>0.22</td><td>0.34</td><td>0.28</td><td>0.27</td><td>0.22</td></tr></table>

Computations of $d _ { i } ^ { * } , d _ { i } ^ { - }$ and $\mathrm { C C } _ { i }$

<table><tr><td></td><td> $d_{i}^{*}$ </td><td> $d_{i}^{-}$ </td><td> $d_{i}^{*} + d_{i}^{-}$ </td><td> $CC_{i}$ </td></tr><tr><td> $A_{1}$ </td><td>1.66</td><td>1.63</td><td>3.29</td><td>0.5</td></tr><tr><td> $A_{2}$ </td><td>1.17</td><td>2.11</td><td>3.28</td><td>0.64</td></tr><tr><td> $A_{3}$ </td><td>1.25</td><td>2.07</td><td>3.32</td><td>0.62</td></tr><tr><td> $A_{4}$ </td><td>1.61</td><td>1.69</td><td>3.3</td><td>0.51</td></tr><tr><td> $A_{5}$ </td><td>1.99</td><td>1.33</td><td>3.32</td><td>0.4</td></tr></table>

with low $\mathrm { r i s k } ^ { \prime \prime }$ . However, according to the closeness coefficients, supplier $A _ { 2 }$ is preferred to $A _ { 3 }$ because $\mathrm { C C } _ { 2 } { > } \mathrm { C C } _ { 3 }$ in Class IV. In Class III, the preferred order is $A _ { 4 } > A _ { 1 } > A _ { 5 }$ because $\mathrm { C C } _ { 4 } >$ $\mathrm { C C } _ { 1 } { > } \mathrm { C C } _ { 5 }$ . Finally, the ranking order of five suppliers is $\{ A _ { 2 } > A _ { 3 } \} > \{ A _ { 4 } > A _ { 1 } > A _ { 5 } \}$

In the other case, the different membership functions of linguistic variables are used to compare the result of the ranking order. The membership functions of linguistic variables are triangular fuzzy numbers. Three decision-makers use the linguistic variables shown in Figs. 7 and 8 to assess the importance of criteria and evaluate the ratings of candidates with respect to each criterion. Applying the computational procedure of proposed method, the closeness coefficient of each supplier can be calculated as

$$
\begin{array}{l l} \mathrm{CC} _ {1} = 0. 5 0, & \mathrm{CC} _ {2} = 0. 6 4, \quad \mathrm{CC} _ {3} = 0. 6 3, \\ \mathrm{CC} _ {4} = 0. 5 1, & \mathrm{CC} _ {5} = 0. 4 0. \end{array}
$$

According to the closeness coefficients, we know that suppliers $A _ { 2 }$ and $A _ { 3 }$ belong to Class IV. Suppliers $A _ { 1 } , A _ { 4 }$ and $A _ { 5 }$ belong to Class III. The ranking order of five suppliers is $\{ A _ { 2 } > A _ { 3 } \} >$ $\{ A _ { 4 } > A _ { 1 } > A _ { 5 } \}$ . Obviously, the results of ranking order are identical when the different membership functions of linguistic variables are used in the proposed method. Therefore, it can confirm that this proposed method is very effective to deal with the problem of supplier selection.

![](images/366b566c8de57808d117421b0ea8785307105e098e6ede2169b7020fb6ab7e78.jpg)  
Fig. 7. Alterative linguistic variables for importance weight of each criterion.

![](images/e8cfed3c2584ac75c233eec99d3fc14dd6243f9ab5ffda76a6572d0492a64472.jpg)  
Fig. 8. Alterative linguistic variables for ratings.

## 5. Conclusions

Many practitioners and researchers have presented the advantages of supply chain management. In order to increase the competitive advantage, many companies consider that a welldesigned and implemented supply chain system is an important tool. Under this condition, building on the closeness and long-term relationships between buyers and suppliers is critical success factor to establish the supply chain system. Therefore, supplier selection problem becomes the most important issue to implement a successful supply chain system.

In general, supplier selection problems adhere to uncertain and imprecise data, and fuzzy-set theory is adequate to deal with them. In a decisionmaking process, the use of linguistic variables in decision problems is highly beneficial when performance values cannot be expressed by means of numerical values. In other words, very often, in assessing of possible suppliers with respect to criteria and importance weights, it is appropriate to use linguistic variables instead of numerical values. Due to the decision-makers’ experience, feel and subjective estimates often appear in the process of supplier selection problem, an extension version of TOPSIS in a fuzzy environment is proposed in this paper. The fuzzy TOPSIS method can deal with the ratings of both quantitative as well as qualitative criteria and select the suitable supplier effectively. It appears from the foregoing sections that fuzzy TOPSIS method may be a useful additional tool for the problem of supplier selection in supply chain system.

In fact, the fuzzy TOPSIS method is very flexible. According to the closeness coefficient, we can determine not only the ranking order but also the assessment status of all possible suppliers. Significantly, the proposed method provides more objective information for supplier selection and evaluation in supply chain system. The systematic framework for supplier selection in a fuzzy environment presented in this paper can be easily extended to the analysis of other management decision problems. However, improving the approach for solving supplier selection problems more efficiently and developing a group decisionsupport system in a fuzzy environment can be considered as a topic for future research.

## Acknowledgements

The authors gratefully acknowledge the financial support of the National Science Council, Taiwan, under project number NSC 92-2213-E-212-008.

## References

Bellman, B.E., Zadeh, L.A., 1970. Decision-making in a fuzzy environment. Management Science 17 (4), 141–164.

Briggs, P., 1994. Vendor assessment for partners in supply. European Journal of Purchasing & Supply Management 1, 49–59.

Buckley, J.J., 1985. Fuzzy hierarchical analysis. Fuzzy Sets and Systems 17, 233–247.

Chen, C.T., 2000. Extensions of the TOPSIS for group decision-making under fuzzy environment. Fuzzy Sets and Systems 114, 1–9.

Choi, T.Y., Hartley, J.L., 1996. An exploration of supplier selection practices across the supply chain. Journal of Operations Management 14, 333–343.

Cook, R.L., 1992. Expert systems in purchasing applications and development. International Journal of Purchasing and Management 18, 20–27.

de Boer, L., van der Wegen, L., Telgen, J., 1998. Outranking methods in support of supplier selection. European Journal of Purchasing & Supply Management 4, 109–118.

Delgado, M., Verdegay, J.L., Vila, M.A., 1992. Linguistic decision-making models. International Journal of Intelligent Systems 7, 479–492.

Delgado, M., Herrera, F., Herrera-Viedma, E., Martinez, L., 1998. Combining numerical and linguistic information in group decision making. Journal of Information Sciences 107, 177–194.

Donaldson, B., 1994. Supplier selection criteria on the service dimension. European Journal of Purchasing & Supply Management 1, 209–217.

Dowlatshahi, S., 2000. Design–buyer–supplier interface: Theory versus practice. International Journal of Production Economics 63, 111–130.

Dubois, D., Prade, H., 1980. Fuzzy Sets and Systems: Theory and Applications. Academic Press Inc., New York.

Ellram, L.M., 1992. The supplier selection decision in strategic partnerships. International Journal of Purchasing and Management 18, 8–14.

Ghodsypour, S.H., O’Brien, C., 1998. A decision support system for supplier selection using an integrated analytic hierarchy process and linear programming. International Journal of Production Economics 56–57, 199–212.

Herrera, F., Herrera-Viedma, E., 2000. Linguistic decision analysis: Steps for solving decision problems under linguistic information. Fuzzy Sets and Systems 115, 67–82.

Herrera, F., Herrera-Viedma, E., Verdegay, J.L., 1996. A model of consensus in group decision making under linguistic assessments. Fuzzy Sets and Systems 78, 73–87.

Hwang, C.L., Yoon, K., 1981. Multiple Attributes Decision Making Methods and Applications. Springer, New York.

Ittner, C.D., Larcker, D.F., Nagar, V., Rajan, M.V., 1999. Supplier selection, monitoring practices, and firm performance. Journal of Accounting and Public Policy 18, 253–281.

Kaufmann, A., Gupta, M.M., 1991. Introduction to Fuzzy Arithmetic: Theory and Applications. Van Nostrand Reinhold, New York.

Klir, G.J., Yuan, B., 1995. Fuzzy Sets and Fuzzy Logic: Theory and Applications. Prentice-Hall Inc., USA.

Lee, E.K., Ha, S., Kim, S.K., Delgado, M., 2001. Supplier selection and management system considering relationships in supply chain management. IEEE Transactions on Engineering Management 48 (3), 307–318.

Monczka, R., Trent, R., Handfield, R., 1998. Purchasing and Supply Chain Management. South-Western College Publishing, New York.

Negi, D.S., 1989. Fuzzy analysis and optimization. Ph.D. Dissertation, Department of Industrial Engineering, Kansas State University.

Roodhooft, F., Konings, J., 1996. Vendor selection and evaluation—an activity based costing approach. European Journal of Operational Research 96, 97–102.

Shin, H., Collier, D.A., Wilson, D.D., 2000. Supply management orientation and supplier/buyer performance. Journal of Operations Management 18, 317–333.

Swift, C.O., 1995. Preference for single sourcing and supplier selection criteria. Journal of Business Research 32, 105–111.

Verma, R., Pullman, M.E., 1998. An analysis of the supplier selection process. Omega 26, 739–750.

Weber, C.A., Current, J.R., Benton, W.C., 1991. Vendor selection criteria and methods. European Journal of Operational Research 50, 2–18.

Weber, C.A., Current, J.R., Desai, A., 1998. Non-cooperative negotiation strategies for vendor selection. European Journal of Operational Research 108, 208–223.

Zadeh, L.A., 1975. The concept of a linguistic variable and its application to approximate reasoning. Information Sciences 8, 199–249(I) 301–357(II).

Zimmermann, H.J., 1991. Fuzzy Set Theory and its Applications, second ed. Kluwer Academic Publishers, Boston, Dordrecht, London.