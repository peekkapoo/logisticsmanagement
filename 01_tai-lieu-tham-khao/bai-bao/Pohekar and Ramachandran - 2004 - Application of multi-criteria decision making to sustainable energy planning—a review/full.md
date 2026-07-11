# Application of multi-criteria decision making to sustainable energy planning—A review

S.D. Pohekar <sup></sup>, M. Ramachandran

Birla Institute of Technology and Science (BITS), Pilani 333 031, India Received 1 December 2003; accepted 19 December 2003

## Abstract

Multi-Criteria Decision Making (MCDM) techniques are gaining popularity in sustainable energy management. The techniques provide solutions to the problems involving conflicting and multiple objectives. Several methods based on weighted averages, priority setting, outranking, fuzzy principles and their combinations are employed for energy planning decisions. A review of more than 90 published papers is presented here to analyze the applicability of various methods discussed. A classification on application areas and the year of application is presented to highlight the trends. It is observed that Analytical Hierarchy Process is the most popular technique followed by outranking techniques PROMETHEE and ELECTRE. Validation of results with multiple methods, development of interactive decision support systems and application of fuzzy methods to tackle uncertainties in the data is observed in the published literature. © 2004 Elsevier Ltd. All rights reserved

Keywords: Multi-objective optimization; Multi-criteria decision making; Decision support systems; Sustainable energy planning

## Contents

1. Introduction . . . . . . . . . . . . . . 366

2. Overview of multi-criteria decision making (MCDM) methods . . 367 2.1. Weighted sum method (WSM) 368 2.2. Weighted product method (WPM) 369 2.3. Analytical hierarchy process (AHP) . 369

2.4. Preference ranking organization method for enrichment evaluation (PROMETHEE) 370  
2.5. The elimination and choice translating reality (ELECTRE) 371  
2.6. The technique for order preference by similarity to ideal solutions (TOPSIS) 372  
2.7. Compromise programming (CP) 372  
2.8. Multi-attribute utility theory (MAUT) 372  
3. Multi-criteria decision making applications in energy planning 373  
3.1. Multi-objective optimization 374  
3.2. Decision Support System (DSS) 374  
3.3. Multi-criteria decision making methods 375  
4. Conclusion 377

## 1. Introduction

Energy planning using multi-criteria analysis has attracted the attention of decision makers for a long time. The methods can provide solutions to increasing complex energy management problems. Traditional single criteria decision making is normally aimed at maximization of benefits with minimization of costs. These methods provide better understanding of inherent features of decision problem, promote the role of participants in decision making processes, facilitate compromise and collective decisions and provide a good platform to understanding the perception of models’ and analysts’ in a realistic scenario. The methods help to improve quality of decisions by making them more explicit, rational and eficient. Negotiating, quantifying and communicating the priorities are also facilitated with the use of these methods.

During the 1970s, energy planning eforts were directed primarily towards energy models aimed at exploring the energy–economy relationships established in the energy sector. The main objectives followed were to accurately estimate future energy demand. A single criteria approach aimed at identifying the most eficient supply options at a low cost was popular [1,2]. In the 1980s, growing environmental awareness has slightly modified the above decision framework [3]. The need to incorporate environmental and social considerations in energy planning resulted in the increasing use of multicriteria approaches.

Multi-objective linear programming is another planning methodology used for illustrating the trade-of between environmental and economic parameters and for assisting in the selection of a compromise solution [4,5]. It was popular in energy planning with conventional fuels in the 1970s. However, after the oil shock of 1973, a thought was given for energy conservation and energy substitution. Renewable energy sources are being promoted for a wide variety of applications worldwide. They are free from any form of pollution and are capable of substituting for conventional fuels in most of the applications. However, the contribution of these sources is very low, despite considerable technological development and their increasing competitiveness with respect to conventional fuels. This compels the planners and decision makers to identify the barriers for penetration and suggest interventions to overcome them. It is therefore felt that, along with the necessary policy measures, the wide exploitation of sustainable energy should be based on a completely diferent conception of energy planning procedure. The role of diferent actors in decision making thus becomes important. Methods of group decision are therefore of primary interest for the implementation of decision sciences in real-life problems.

Multi-criteria decision making (MCDM) methods deal with the process of making decisions in the presence of multiple objectives. A decision-maker is required to choose among quantifiable or non-quantifiable and multiple criteria. The objectives are usually conflicting and therefore, the solution is highly dependent on the preferences of the decision-maker and must be a compromise. In most of the cases, diferent groups of decision-makers are involved in the process. Each group brings along diferent criteria and points of view, which must be resolved within a framework of understanding and mutual compromise. Applications of MCDM include areas such as integrated manufacturing systems [6], evaluations of technology investment [7], water and agriculture management [8,9] in addition to energy planning [10–12].

## 2. Overview of multi-criteria decision making (MCDM) methods

Multi-Criteria Decision Making is a well known branch of decision making. It is a branch of a general class of operations research models which deal with decision problems under the presence of a number of decision criteria. This major class of models is very often called MCDM. This class is further divided into multiobjective decision making (MODM) and multi-attribute decision making (MADM) [13]. There are several methods in each of the above categories. Priority based, outranking, distance based and mixed methods are also applied to various problems. Each method has its own characteristics and the methods can also be classified as deterministic, stochastic and fuzzy methods. There may be combinations of the above methods. Depending upon the number of decision makers, the methods can be classified as single or group decision making methods. Decision making under uncertainty and decision support systems are also prominent decision making techniques [14].

These methodologies share common characteristics of conflict among criteria, incomparable units, and dificulties in selection of alternatives. In multiple objective decision making, the alternatives are not predetermined but instead a set of objective functions is optimized subject to a set of constraints. The most satisfactory and eficient solution is sought. In this identified eficient solution it is not possible to improve the performance of any objective without degrading the performance of at least one other objective. In multiple attribute decision making, a small number of alternatives are to be evaluated against a set of attributes which are often hard to quantify. The best alternative is usually selected by making comparisons between alternatives with respect to each attribute. The multicriteria decision process is as shown in Fig. 1. The diferent methods are described as follows.

![](images/8b666e15124576d63a1192e18b8bb437f351d687bf6ad6d614550cbbfc396069.jpg)  
Fig. 1. Multicriteria decision process.

## 2.1. Weighted sum method (WSM)

The WSM is the most commonly used approach, especially in single dimensional problems. If there are M alternatives and N criteria then the best alternative is the

S.D. Pohekar, M. Ramachandran / Renewable and Sustainable Energy Reviews 8 (2004) 365–381 369

one that satisfies the following expression:

$$
A _ {W S M} ^ {*} = \operatorname{Max} \sum_ {i} ^ {j} a _ {i j} w _ {j} \quad \text { for } \quad i = 1, 2, 3,... M\tag{1}
$$

where $A _ { \mathrm { ~ } W S M } ^ { * }$ is the WSM score of the best alternative, N is the number of decision criteria, $a _ { i j }$ is the actual value of the $i ^ { \mathrm { { t h } } }$ alternative in terms of the $j ^ { \mathrm { t h } }$ criterion, and $w _ { j }$ is the weight of importance of the $j ^ { \mathrm { t h } }$ criterion. The total value of each alternative is equal to the sum of products. Dificulty with this method emerges when it is applied to multi-dimensional decision-making problems. In combining diferent dimensions, and consequently diferent units, the additive utility assumption is violated [15].

## 2.2. Weighted product method (WPM)

The WPM is very similar to WSM. The main diference is that instead of addition in the model there is multiplication. Each alternative is compared with the others by multiplying a number of ratios, one for each criterion. Each ratio is raised to the power equivalent to the relative weight of the corresponding criterion. In general, in order to compare the alternatives $A _ { K }$ and $A _ { L }$ the following product is obtained:

$$
R (A _ {K} / A _ {L}) = \sum_ {j = 1} ^ {N} (a _ {k j} / a _ {L j}) ^ {w _ {j}}\tag{2}
$$

where N is the number of criteria, $a _ { i j }$ is the actual value of the $i ^ { \mathrm { t h } }$ alternative in terms of the $j ^ { \mathrm { t h } }$ criterion, and $w _ { j }$ is the weight of importance of the $j ^ { \mathrm { t h } }$ criterion. If $R \ ( A _ { K } / A _ { L } )$ is greater than one, then alternative $A _ { K }$ is more desirable than alternative $A _ { L }$ (in the maximization case). The best alternative is the one that is better than or at least equal to all the other alternatives [16].

## 2.3. Analytical hierarchy process (AHP)

Analytical Hierarchy Process (AHP) is developed by Saaty [17,18]. The essence of the process is decomposition of a complex problem into a hierarchy with goal (objective) at the top of the hierarchy, criterions and sub-criterions at levels and sub-levels of the hierarchy, and decision alternatives at the bottom of the hierarchy. Elements at given hierarchy level are compared in pairs to assess their relative preference with respect to each of the elements at the next higher level. The verbal terms of the Saaty’s fundamental scale of 1–9 is used to assess the intensity of preference between two elements. The value of 1 indicates equal importance, 3 moderately more, 5 strongly more, 7 very strongly and 9 indicates extremely more importance. The values of 2, 4, 6, and 8 are allotted to indicate compromise values of importance. Ratio scale and the use of verbal comparisons are used for weighting of quantifiable and non-quantifiable elements. The method computes and aggregates their eigenvectors until the composite final vector of weight coeficients for alternatives is obtained. The entries of final weight coeficients vector reflect the relative importance (value) of each alternative with respect to the goal stated at the top of hierarchy. A decision maker may use this vector due to his particular needs and interests. To elicit pair wise comparisons performed at a given level, a matrix A is created in turn by putting the result of pair wise comparison of element i with element j into the position $a _ { j i }$ as below.

$$
A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & . & a _ {1 n} \\ a _ {2 1} & a _ {2 1} & . & a _ {2 n} \\ a _ {n 1} & a _ {n 2} & . & a _ {n n} \end{array} \right]\tag{3}
$$

After obtaining the weight vector, it is then multiplied with the weight coeficient of the element at a higher level (that was used as criterion for pair wise comparisons). The procedure is repeated upward for each level, until the top of the hierarchy is reached. The overall weight coeficient, with respect to goal for each decision alternative is then obtained. The alternative with the highest weight coefficient value should be taken as the best alternative. One of the major advantages of AHP is that it calculates the inconsistency index as a ratio of the decision maker’s inconsistency and randomly generated index. This index is important for the decision maker to assure him that his judgments were consistent and that the final decision is made well. The inconsistency index should be lower than 0.10. Although a higher value of inconsistency index requires re-evaluation of pair wise comparisons, decisions obtained in certain cases could also be taken as the best alternative.

## 2.4. Preference ranking organization method for enrichment evaluation (PROMETHEE)

This method uses the outranking principle to rank the alternatives, combined with the ease of use and decreased complexity. It performs a pair-wise comparison of alternatives in order to rank them with respect to a number of criteria. Brans et al. [19] have ofered six generalized criteria functions for reference namely, usual criterion, quasi criterion, criterion with linear preference, level criterion, criterion with linear preference and indiference area, and Gaussian criterion. The method uses preference function $P _ { j } \ ( a , b )$ which is a function of the diference $d _ { j }$ between two alternatives for any criterion $j ,$ i. e. $d _ { j } = f ( a , j ) - f ( b , j )$ , where $f ( a , j )$ and $f ( b , j )$ are values of two alternatives a and b for criterion $j .$ The indiference and preference thresholds $q ^ { , }$ and $p '$ are also defined depending upon the type of criterion function. Two alternatives are indiferent for criterion $j$ as long as $d _ { j }$ does not exceed the indiference threshold $q ^ { , }$ . If $d _ { j }$ becomes greater than $p '$ , there is a strict preference. Multi-criteria preference index, $\pi ( \boldsymbol { a } , \boldsymbol { b } )$ a weighted average of the

S.D. Pohekar, M. Ramachandran / Renewable and Sustainable Energy Reviews 8 (2004) 365–381 371 preference functions $P _ { j } \left( a , b \right)$ for all the criteria is defined as

$$
\pi (a, b) = \frac {\sum_ {j = 1} ^ {J} w _ {j} P _ {j} (a , b)}{\sum_ {j = 1} ^ {J} w _ {j}}\tag{4}
$$

$$
\phi^ {+} (a) = \sum_ {A} \pi (a, b)\tag{5}
$$

$$
\phi^ {-} (a) = \sum_ {A} \pi (b, a)\tag{6}
$$

$$
\phi (a) = \phi^ {+} (a) - \phi^ {-} (a)\tag{7}
$$

where $w _ { j }$ is the weight assigned to the criterion j; $\phi ^ { + } ( a )$ is the outranking index of $a$ in the alternative set $\mathbf { A } ; \phi ^ { - } ( a )$ is the outranked index of a in the alternative set A; $\phi ( a )$ is the net ranking of a in the alternative set A. The value having maximum $\phi ( a )$ is considered as the best.

a outranks b iff $\phi ( a ) > \phi ( b )$ ; a is indifferent to b iff $\phi ( a ) = \phi ( b )$

## 2.5. The elimination and choice translating reality (ELECTRE)

This method is capable of handling discrete criteria of both quantitative and qualitative in nature and provides complete ordering of the alternatives. The problem is to be so formulated that it chooses alternatives that are preferred over most of the criteria and that do not cause an unacceptable level of discontent for any of the criteria. The concordance, discordance indices and threshold values are used in this technique. Based on these indices, graphs for strong and weak relationships are developed. These graphs are used in an iterative procedure to obtain the ranking of alternatives [20]. This index is defined in the range (0–1), provides a judgment on degree of credibility of each outranking relation and represents a test to verify the performance of each alternative. The index of global concordance $C _ { i k }$ represents the amount of evidence to support the concordance among all criteria, under the hypothesis that $A _ { i }$ outranks $A _ { k }$ . It is defined as follows.

$$
C _ {i k} = \sum_ {j = 1} ^ {m} W _ {j} c _ {j} (A _ {i} A _ {k}) / \sum_ {j = 1} ^ {m} W _ {j}\tag{8}
$$

where $W _ { j }$ is the weight associated with $j ^ { \mathrm { t h } }$ criteria. Finally, the ELECTRE method yields a whole system of binary outranking relations between the alternatives. Because the system is not necessarily complete, the ELECTRE method is sometimes unable to identify the preferred alternative. It only produces a core of leading alternatives. This method has a clearer view of alternatives by eliminating less favorable ones, especially convenient while encountering a few criteria with a large number of alternatives in a decision making problem [21].

## 2.6. The technique for order preference by similarity to ideal solutions (TOPSIS)

This method is developed by Huang and Yoon [22] as an alternative to ELEC-TRE. The basic concept of this method is that the selected alternative should have the shortest distance from the negative ideal solution in geometrical sense. The method assumes that each attribute has a monotonically increasing or decreasing utility. This makes it easy to locate the ideal and negative ideal solutions. Thus, the preference order of alternatives is yielded through comparing the Euclidean distances. A decision matrix of M alternatives and N criteria is formulated firstly. The normalized decision matrix and construction of the weighted decision matrix is carried out. This is followed by the ideal and negative-ideal solutions. For benefit criteria the decision maker wants to have maximum value among the alternatives and for cost criteria he wants minimum values amongst alternatives. This is followed by separation measure and calculating relative closeness to the ideal solution. The best alternative is one which has the shortest distance to the ideal solution and longest distance to negative ideal solution.

## 2.7. Compromise programming (CP)

Compromise Programming defines the best solution as the one in the set of eficient solutions whose point is the least distance from an ideal point [23].The aim is to obtain a solution that is as close as possible to ideal. The distance measure used in CP is the family of $L _ { p }$ -metrics and is given as

$$
L _ {p} (a) = \sum_ {j = 1} ^ {j} w _ {j} ^ {p} \left| f _ {j} ^ {*} - f (a) \right| / \left| M _ {j} - m _ {j} \right|\tag{9}
$$

where $L _ { p } \ ( a )$ is the $L _ { p }$ metric for alternative $a , f \left( a \right)$ is the value of criterion $j$ for alternative $a , ~ M _ { j }$ is the maximum (ideal) value of criterion j in set A, $m _ { j }$ is the minimum (anti ideal) value of criterion $j$ in set $\mathbf { A } , f _ { j } ^ { * }$ is the ideal value of criterion $j , w _ { j }$ is the weight of the criterion $j , p$ is the parameter reflecting the attitude of the decision maker with respect to compensation between deviations. For $p = 1$ , all deviations from $f _ { j ^ { \ast } }$ are taken into account in direct proportion to their magnitudes meaning that there is full (weighted) compensation between deviations

## 2.8. Multi-attribute utility theory (MAUT)

Multi-attribute Utility Theory takes into consideration the decision maker’s preferences in the form of the utility function which is defined over a set of attributes The utility value can be determined by determination of single attribute utility functions followed by verification of preferential and utility independent conditions and derivation of multi-attribute utility functions. The utility functions can be either additively separable or multiplicatively separable with respect to single attribute utility. The multiplicative form of equation for then utility value is defined as

S.D. Pohekar, M. Ramachandran / Renewable and Sustainable Energy Reviews 8 (2004) 365–381 373 follows.

$$
1 + k u \left(x _ {1}, x _ {2}, \dots x _ {n}\right) = \prod_ {j = 1} ^ {n} \left(1 + k k _ {j} u _ {j} \left(x _ {j}\right)\right)\tag{10}
$$

Here j is the index of attribute, k is overall scaling constant (greater than or equal $\mathrm { t o } ~ { - } 1 )$ , $k _ { j }$ is the scaling constant for attribute j, u(.) is the overall utility function operator, $u _ { j } ( . )$ is the utility function operator for each attribute j [24].

## 3. Multi-criteria decision making applications in energy planning

The application areas of MCDM in energy planning presented in this section are renewable energy planning, energy resource allocation, building energy management, transportation energy management, planning for energy projects, electric utility planning and other miscellaneous areas. The comparison of MCDM methods applicable to energy planning are discussed in the literature. Hobbs and Meirer [25] compared the methods with respect to simplicity of applications and feasible expected outcomes, Huang and Poh [26] discussed the methods used in energy and environmental modeling under uncertainties, Lahdelma et al. [27] discussed these methods for environmental planning and management. The commonly applied MCDM methods out of the above are multi-objective optimization, AHP, PRO-METHEE, ELECTRE, MAUT, fuzzy methods and decision support systems (DSS). More than one MCDM method is also applied in many application areas to validate the results [28–30].

A review of the published literature is presented here with a view to highlighting the applications areas and trends. A classification of published literature before 1990 and beyond 1990 is also presented to highlight suitability of the methods in changed global scenario. Six generalized application areas and a miscellaneous area presented here have common features of minimization of cost benefit ratios, high degrees of uncertainties in formulating the problems, incommensurable units and the need to handle socio-economic aspects in planning. Renewable energy planning and energy resource allocation refers to compilation of feasible energy plan and dissemination of various renewable energy options. The key factors applicable are investment planning, energy capacity expansion planning and evaluation of alternative energies. Building energy management refers to design, selection, installation and building energy management options in a multi-criteria environment. The application normally deals with quantitative issues. Transportation system applications include evaluation of alternative strategies for pollution control, elimination of old polluting vehicles, choosing between private and public transport etc. The key features of transportation applications are of a high concern for socioeconomic reasons. Project planning refers to site selection, technology selection and decision support in renewable energy harnessing projects. The objectives are arriving at a Pareto optimal solution for technology selection, sizing, execution, investment planning. Optimal electrical dispatch scheduling, deciding power generation mix, optimum electricity supply planning are the applications of electric utility planning using MCDM. Miscellaneous applications include desalination plant selection, solid waste management.

It can be observed from the surveyed literature that AHP is the most popular method for prioritizing the alternatives, followed by PROMETHEE and ELEC-TRE. Multi-objective programming is also very widely used to formulate alternative plans. Fuzzy MCDM methods are also adopted for considering the uncertainties in energy planning. Decision support systems are becoming popular in energy planning and resource allocation with the advent of the latest computational aids.

## 3.1. Multi-objective optimization

This method is very widely used in energy resource allocation, energy planning and electric utility applications. Maximization of cost benefit ratio to arrive at optimum resource allocation in rural areas [31], national level energy planning [32] are amongst a few applications. The application areas have common features of higher investment costs, higher project durations, conflicting objectives and uncertainty. Energy security and social benefits are prominent objectives in energy planning with these methods. These techniques are also used for sustainability evaluation of power plants [33], deciding optimum mix of renewable energy technologies at various sectors [34–37]. Renewable energy planning with energy environment linkages [38], economic constraints, technology limitations etc. are the main features of applications surveyed . Applications to various national level issues [39–42] and household energy issues [43,44] are also among the prominent application areas. Multi-objective optimization also finds applications in building energy management [45]. The issues identified are building material design [46], building performance design [47,48], building arrangement design [49], and building shape design [50,51]. Regional energy supply optimization [52,53], desalination power plant selection [54,55], electricity distribution planning using fuzzy approaches [56,57] are also worth mentioning. Genetic algorithms are also applied to electric utility planning and building energy management problems [46]. An analysis of utilizing multiobjective optimization reveals that the methods are being used for a wide variety of applications after 1990. These may be due to the advent of sophisticated computational aids available and increased need for larger socio-economic considerations in energy planning.

## 3.2. Decision Support System (DSS)

These are sophisticated, interactive and computer aided techniques for aiding the decisions [58]. These can support complex problems that would be otherwise dificult to handle. Knowledge based DSS can support the decision makers in selecting criteria, alternatives and trade-ofs, thus making the energy planning simple. The identified DSS use MCDM methods for arriving at interim results. The applications of DSS in energy planning developed are solid waste management [59], transportation energy management [60], electricity production alternatives [61], building energy management [62] and renewable energy project planning [63].

## 3.3. Multi-criteria decision making methods

The Multi Attribute Utility Theory is developed to help decision makers assign utility values to outcomes by evaluating these in terms of multiple attributes and combining individual assignments to obtain overall utility values. It is observed that MAUT is not very extensively used in energy planning. This may be due to requirements of interactive decision environment required in formulating utility functions, complexity of computing scaling constants using the algorithm [64]. Selecting portfolios for solar energy projects [65], energy policy making [66], environmental impact assessment [67] and electric power system expansion planning [68] are the applications identified in the literature. A few numbers of studies are observed using this method after 1990.

The outranking methods belonging to ELECTRE family are popularly used in energy planning. These methods are also used in renewable energy DSS after 1990 [62,69,70].Other common application areas include electric utility planning, building energy management and project planning. These methods are also applied to selection of thermal power plant location by eliminating certain sites [71], renewable energy plant selection [72,73], selecting pollution control technologies [74] and transportation energy planning [75,76]. Though various versions of ELECTRE are developed ELECTRE III is found to be widely used in energy planning applications.

Outranking methods belonging to PROMETHEE category are also extensively used in energy planning. These methods provide a scientific basis to arrive at multicriteria preference index by calculating the strengths and weaknesses of alternative actions. This method is used in energy project planning and applications to geothermal site selection [77,78] and small hydro site selections [79]. Other application areas are impact analysis of energy alternatives [80,81], old vehicle elimination [75,76] and building product designs [82]. Diferent versions of PROMETHEE are in use and PROMETHEE II has been extensively used after 1990.

Analytical Hierarchy Process is very widely used in energy planning. This may be due to provisions of converting a complex problem into a simple hierarchy, flexibility, intuitive appeal, its ability to mix qualitative as well as quantitative criteria in the same decision framework [83] and use of computational aids leading to successful decisions in many domains [84]. Though a there are number of shortcomings [85], the method is popularly used in renewable energy planning [86–90], energy resource allocation [91], transportation energy planning [92], project planning [93] and electric utility planning [94–96]. The applications surveyed have the main objectives of priority setting and have features such as less number of criteria, interaction with decision makers etc. The correctness of AHP has been established by comparing it with other MCDM methods. The method is used with modifications during post 1990.

In addition to the above discussed methods, preference desegregation method is also used for energy analysis and policy making studies [97]. Fuzzy set programming is used for a variety of applications after 1990. A few of the application areas surveyed are solar system evaluation [98,99], power systems [100–103] and wind site selection [104].

<sub>tion</sub> <sub>of</sub> <sub>MC</sub><sup>DM</sup> <sup>methods</sup> <sup>by</sup> <sup>applicat</sup> <sub>a</sub>b<sup>le</sup>

<table><tr><td rowspan="2">Applications</td><td rowspan="2">Multi-objective</td><td colspan="5">Methods</td><td rowspan="2">Total number</td></tr><tr><td>MAUT</td><td>AHP</td><td>PROMETHEE</td><td>ELECTRE</td><td>Others</td></tr><tr><td>Renewable energy planning</td><td>[2,33–38]</td><td>[65,66]</td><td>[87,90,95,96]</td><td>[70,75,79]</td><td>[69,70]</td><td>[62,97–99,104]</td><td>22</td></tr><tr><td>Energy resource allocation</td><td>[43,88,89,95]</td><td></td><td>[88–91]</td><td></td><td></td><td>[1–32,39]</td><td>10</td></tr><tr><td>Building energy management</td><td>[46,47,49–51]</td><td></td><td></td><td>[82]</td><td>[45,62]</td><td></td><td>8</td></tr><tr><td>Transportation energy systems</td><td></td><td></td><td>[76,92]</td><td>[76]</td><td>[75]</td><td>[60]</td><td>5</td></tr><tr><td>Project planning</td><td></td><td></td><td>[93]</td><td>[77,78]</td><td>[71–74]</td><td></td><td>7</td></tr><tr><td>Electric utility planning</td><td>[4,5,53,101]</td><td>[67,68]</td><td>[94–96]</td><td></td><td></td><td>[59,98,100,102]</td><td>12</td></tr><tr><td>Others</td><td>[56]</td><td></td><td></td><td></td><td>[74]</td><td></td><td>2i</td></tr><tr><td>Total number</td><td>22</td><td>4</td><td>14</td><td>7</td><td>10</td><td>13</td><td></td></tr></table>

<sub>in</sub> <sub>squar</sub><sup>e</sup> <sup>brackets</sup> <sup>refer</sup> <sup>toreference</sup>

Table 2  
Classification of MCDM methods by year of publication

<table><tr><td>Year of Publication</td><td>Upto 1990</td><td>Beyond 1990</td><td>Total Number</td></tr><tr><td>Multi-Objective</td><td>[2,4,5,40,47,53,89]</td><td>[25,33–38,43,46,49–51,56,95,101]</td><td>22</td></tr><tr><td>MAUT</td><td>[65,66]</td><td>[67,68]</td><td>4</td></tr><tr><td>AHP</td><td>[75,76,94]</td><td>[87–93,95,96]</td><td>14</td></tr><tr><td>PROMETHEE</td><td>[75,76,79]</td><td>[70,77,78,82]</td><td>7</td></tr><tr><td>ELECTRE</td><td>[71,79]</td><td>[45,62,69,70,72–75]</td><td>10</td></tr><tr><td>Others</td><td>[31,32]</td><td>[25,39,59–60,62,97]–100, 102,104]</td><td>13</td></tr><tr><td>Total Number</td><td>19</td><td>48</td><td></td></tr></table>

Numbers in square brackets refer to reference numbers.

It can be observed from the studies (Tables 1 and 2) that multi-objective optimization accounts for 29% of the identified studies, followed by AHP (20%), ELEC-TRE (15%), PROMETHEE (10%). Miscellaneous methods including DSS and fuzzy methods account for a share of 20% in energy decision making applications. The number of MCDM applications surveyed upto 1990 is 29% and beyond 1990 is 69% approximately. The methods are observed to be highly popular for renewable energy planning (34%), followed by electric utility planning (19%), energy resource allocation (15%), building energy management (13%) and project planning (12%).

## 4. Conclusion

A feview of the published literature on sustainable energy planning presented here indicates greater applicability of MCDM methods in changed socio-economic scenario. The methods have been very widely used to take care of multiple, conflicting criteria to arrive at better solutions Increasing popularity and applicability of these methods beyond 1990 indicate a paradigm shift in energy planning approaches. The methods are observed to be most popular in renewable energy planning followed by energy resource allocation. It is observed that Analytical Hierarchy Process is the most popular technique followed by outranking techniques PROMETHEE and ELECTRE. Validation of results with multiple methods, development of interactive decision support systems and application of fuzzy methods to tackle uncertainties in the data is observed in the published literature.

## Acknowledgements

The authors gratefully acknowledge the contributions of Dr. K. S. Raju, Group Leader–Civil Engineering of BITS, Pilani for his constructive criticism and support.

## References

[1] Samouilidis J, Mitropoulos C. Energy economy models—a survey. European Journal of Operations Research 1982;25:200–15.

[2] Meirer P, Mubayi V. Modeling energy-economic interactions in developing countries-a linear pro gramming approach. European Journal of Operations Research 1983;13:41–59.

[3] Nijcamp P, Volwahsen A. New directions in integrated energy planning. Energy Policy 1990;18(8):764–73.

[4] Kavrakoglu I. Multi-objective strategies in power system planning. European Journal of Operations Research 1983;12:159–70.

[5] Schulz V, Stehfest H. Regional energy supply optimization with multiple objectives. European Journal of Operations Research 1984;17:302–12.

[6] Putrus P. Accounting for intangibles in integrated manufacturing-non-financial justification based on analytical hierarchy process. Information Strategy 1990;6:25–30.

[7] Boucher TO, McStravic EL. Multi-attribute evaluation within a present value framework and its relation to analytic hierarchy process. The Engineering Economist 1991;37:55–71.

[8] Ozelkan EC, Duckstein L. Analyzing water resources alternatives and handling criteria by multicriterion decision techniques. Journal of Environmental Management 1996;48:69–96.

[9] Raju KS, Pillai CRS. Multicriterion decision making in performance evaluation of irrigation projects. European Journal of Operational Research 1999;112(3):479–88.

[10] Afgan NH, Carvalho MG. Sustainable assessment method for energy systems. Boston: Kluwer Academic Publishers; 2000.

[11] Afgan NH, Gobaisi D, Carvalho MG, Cumo M. Sustainable energy management. Renewable and Sustainable Energy Reviews 1998;2:235–86.

[12] Afgan NH, Carvalho MG, Hovanov NV. Sustainability assessment of renewable energy systems. Energy Policy 2000;28:603–12.

[13] Climaco J, editor. Multicriteria analysis. New York: Springer-Verlag; 1997.

[14] Gal T, Hanne T, editors. Multicriteria decision making: Advances in MCDM models, algorithms, theory, and applications. New York: Kluwer Academic Publishers; 1999.

[15] Solnes J. Environmental quality indexing of large industrial development alternatives using AHP. Environmental Impact Assessment Review 2003;23(3):283–303.

[16] Chang YH, Yeh CH. Evaluating airline competitiveness using multi-attribute decision making. Omega 2001;29(5):405–15.

[17] Saaty TL. The analytic hierarchy process. New York: McGraw-Hill; 1980.

[18] Saaty TL. Decision making for leaders. Pittsburgh: RWS Publications; 1992.

[19] Brans JP, Vincke Ph, Mareschal B. How to select and how to rank projects: the PROMETHEE method. European Journal of Operations Research 1986;24:228–38.

[20] Roy B. Me´todologie multicrite\`re d’aide la de´cision. Collection Gestion, Paris: Economica; 1985.

[21] Goicoechea A, Hansen D, Duckstein L. Introduction to multi objective analysis with engineering and business application. Wiley: New York; 1982.

[22] Huang CL, Yoon K. Multi attribute decision making: methods and applications. New York: Springer-Verlag; 1981.

[23] Zeleny M. Multiple criteria decision making. New York: McGraw-Hill; 1982.

[24] Keeny RL, Raifa H. Decisions with multiple objectives: Preferences and value tradeofs. New York: Wiley; 1976.

[25] Hobbs BF, Meirer PM. Multicrerion methods for resource planning: an experimental comparison. IEEE Transactions on Power Systems 1994;9(4):1811–7.

[26] Huang JP, Poh KL, Ang BW. Decision analysis in energy and environmental modeling. Energy 1995;20(9):843–55.

[27] Lahdelma R, Salminen P, Hokkanen J. Using multicriteria methods in environmental planning and management. Environmental Management 2000;26(6):595–605.

[28] Karni R, Feigin P, Breiner A. Multicriterion issues in energy policy making. European Journal of Operational Research 1992;56:30–40

[29] Mirasgedis S, Diakoulaki D. Multicriteria analysis vs. externalities assessment for the comparative evaluation of electricity generation systems. European Journal of Operational Research.; 1997;102(2):364–79.

[30] Salminen P, Hokkanen J, Lahdelma R. Comparing multicriteria methods in the context of environmental problems. European Journal of Operational Research 1998;104:485–96.

[31] Christensen JM, Vidal R. Project evaluation for energy supply in rural areas of developing countries. European Journal of Operations Research 1990;49:230–46.

[32] Lootsma FA, Boonekamp PGM, Cooke RM, Van Oostvoorn F. Choice of a long term strategy for the national electricity supply via scenario analysis and multi-criteria analysis. European Journal of Operational Research 1990;48:189–203.

[33] Afgan NH, Carvalho MG. Multi-criteria assessment of new and renewable energy power plants. Energy 2002;27:739–55.

[34] Iniyan S, Sumanthy K. An optimal renewable energy model for various end-uses. Energy–The International Journal 2000;25:563–75.

[35] Suganthi L, Williams A. Renewable energy in India—a modeling study for 2020–2021. Energy Policy 2000;28:1095–109.

[36] Sinha CS, Kandpal TC. Optimal mix of technologies in rural area: the cooking sector. Inter national Journal of Energy Research 1991;15:85–100.

[37] Cormico C, Dicorato M, Minoia A, Trovato M. A regional energy planning methodology including renewable energy sources environmental constraints. Renewable and Sustainable Energy Reviews 2003;7:99–130.

[38] Borges AR, Antunes CH. A fuzzy multiple objective decision support model for energy-economy planning. European Journal of Operational Research 2003;145(2):304–16.

[39] Chedid R, Mezher T, Jarrouche C. A fuzzy programming approach to energy resource allocation. International Journal of Energy Research 1999;23:303–17.

[40] Psarras J, Capros P, Samoulidis JE. Multi-criteria analysis using a large scale energy supply LP model. European Journal of Operations Research 1990;44:383–94.

[41] Ramanathan R. A multi-criteria methodology to the global negotiations on climate change. IEEE Transactions on Systems, Man and Cybernetics—Part C: Applications and Reviews 1998;28:541–8.

[42] Ramanathan R. Selection of appropriate greenhouse mitigation options. Global Environmental Change 1999;9:203–10.

[43] Ramanathan R, Ganesh LS. Multi-objective analysis of cooking-energy alternatives. Energy 1994;19(4):469–78.

[44] Ramanathan R, Ganesh LS. Energy alternatives for lighting in households: an evaluation using an integrated goal programming-AHP model. Energy 1995;20(1):63–72.

[45] Blondeau P, Allard F. Multicriteria analysis of ventilation in summer period. Building and Environment 2002;37(2):165–76.

[46] Wright JA, Loosemore HA, Fermani R. Optimization of building thermal design and control by multi-criterion genetic algorithm. Energy and Buildings 2002;34:959–72.

[47] D’Cruz NA, Radford AD. Multi-criteria model for building performance and design. Building and Environment 1987;22(3):167–79.

[48] Flourentzou F, Roulet CA. Elaboration of retrofit scenarios. Energy and Buildings 2002;34(2):185–92.

[49] Klemm K, Marks W, Klemm AJ. Multicriteria optimization of the building arrangement with application of numerical simulation. Building and Environment 2000;35(6):537–44.

[50] Marks WM. ulticriteria optimization of shape of energy-saving buildings. Building and Environ ment 1997;32(4):331–9.

[51] Jedrzejuk H, Marks WO. ptimization of shape and functional structure of buildings as well as heat source utilization-partial problems solution. Building and Environment 2002;379(11):1037–43.

[52] Schulz V, Stehfest H. Regional energy supply optimization with multiple objectives. European Journal of Operational Research 1983;17:302–12.

[53] Amagai H, Leung P. Multiple criteria analysis for Japan’s electric power generation mix. Energy Systems and Policy 1989;13:219–36.

[54] Afgan NH, Darwish M, Carvalho MG. Sustainability assessment of desalination plants for water production. Desalination 1999;124:19–31.

[55] Akash BA, Al-Jayyousi O, Mohsen M. Multi-criteria analysis of non-conventional energy technol ogies for water desalination in Jordan. Desalination 1997;114:1–12.

[56] Matos MA. Fuzzy filtering method applied to power distribution planning. Fuzzy Sets and Systems 1999;102(1):53–8.

[57] Levitin G, Tov SMT, Elmakis D. Genetic algorithm for open-loop distribution system design. Electric Power Systems Research 1995;32(2):81–7.

[58] Turban E. Decision support and expert system. New York: Prentice Hall; 1995.

[59] Fiorucci P, Minciardi R. Solid waste management in urban areas: Development and application of a decision support system. Resources Conservation and Recycling 2003;37(4):301–28.

[60] Brand C, Mattarelli M, Moon D, Calvo RW. STEEDS: A strategic transport-energy-environment decision support. European Journal of Operational Research 2002;139(2):416–35.

[61] Gandibleux X. Interactive multicriteria procedure exploiting a knowledge-based module to select electricity production alternatives: The CASTART system. European Journal of Operational Research 1999;113(2):355–73.

[62] Roulet CA. ORME: A multi-criteria rating methodology for buildings. Building and Environment 2002;37:579–86.

[63] Georgopoulou E, Sarafidis F, Mirasgedis S, Zaimi S, Lalas DP. A multiple criteria decision-aid approach in defining national priorities for greenhouse gases emissions reduction in the energy sector. European Journal of Operational Research 2003;146(1):199–215.

[64] Dyer JS. Remarks on analytical hierarchy process. Management Science 1990;36:249–58.

[65] Golabi K, Kirkwood CW, Sicherman A. Selecting a portfolio of solar energy projects using multiattribute preference theory. Management Science 1981;22(2):174–89.

[66] Jones M, Hope C, Hughes R. Amulti-attribute value model for the study of UK energy policy. Journal of Operations Research Society 1990;41(10):919–29.

[67] McDaniels TL. A multiattribute index for evaluating environmental impact of electric utilities. Journal of Environmental Management 1996;46:57–66.

[68] Voropai NL, Ivanova EY. Multicriteria decision analysis technique in electric power system expansion planning. Electrical Power and Energy Systems 2002;24:71–8.

[69] Beccali M, Cellura M, Mistretta M. Decision-making in energy planning-application of the ELEC-TRE method at regional level for the difusion of renewable energy technology. Renewable Energy 2003;28(13):2063–87.

[70] Georgopoulou E, Sarafidis Y, Diakoulaki D. Design and implementation of a group DSS for sustaining renewable energies exploitation. European Journal of Operational Research 1998;109:483–500.

[71] Barda OH, Dupluis J, Lencoini P. Multicriteria location of thermal power plants. European Journal of Operations Research 1990;45:332–46.

[72] Haralambopoulos DA, Polatidis H. Renewable energy projects: structuring a multi-criteria group decision-making framework. Renewable Energy 2003;28:961–73.

[73] Georgopoulou E, Lalas D, Papagiannakis L. A multicriteria decision aid approach for energy planning problems: the case of renewable energy option. European Journal of Operational Research 1997;3:38–54.

[74] Hokkanen J, Salminen P. Choosing a solid waste management system using multicriteria decision analysis. European Journal of Operational Research 1997;98:19–36.

[75] Tzeng GH, Shiau TA. Energy conservation strategies in urban transportation: application of multi-criteria decision making. Energy Systems and Policy 1987;11:1–19.

[76] Tzeng GH, Tsaur SH. Application of multicriteria decision making to old vehicle elimination in Taiwan. In Proceeding of International Conference on MCDM Taipei. Taiwan, 1990: 4:268–283.

[77] Goumas MG, Lygerou V, Papayannakis LE. Computational methods for planning and evaluatin geothermal energy projects. Energy Policy 1999;27:147–54.

[78] Goumas MG, Lygerou V. An extension of the PROMETHEE method for decision-making in fuzzy environment: ranking of alternative energy exploitation projects. European Journal of Operational Research 2000;123:606–13.

[79] Mladineo N, Margeta J, Brans JP, Mareschal B. Multicriteria ranking of alternative locations for small scale hydro plants. European Journal of Operational Research 1987;31:215–22.

[80] Siskos J, Hubert PH. Multi-criteria analysis of the impacts of energy alternatives: A survey and a comparative approach. European Journal of Operational Research 1983;13:278–99.

[81] Tzeng GH, Shiau TA, Lin CY. Application of multi-criteria decision making to the evaluation of new energy system development in Taiwan. Energy 1992;17(10):983–92.

[82] Teno TFL, Marseschal B. An interval version of PROMETHEE for comparison of building products’ design with ill defined data on environmental quality. European Journal of Operational Research 1998;109:522–9.

[83] Wedley WC. Combining qualitative and quantitative factors -an analytical hierarchy approach. Socio-economic Planning Sciences 1990;24:57–64.

[84] Golden BL, Wasil EA, Harker PT. Analytical hierarchy process. Berlin: Springer-Verlag; 1989.

[85] Dyer JS, Fishburn RE, Steuer RE, Wallenenius J, Zionts S. Multiple criteria decision making, multiattribute utility theory: the next ten years. Management Science 1992;38:645–54.

[86] Mohsen MS, Akash BA. Evaluation of domestic solar water heating system in Jordan using ana lytical hierarchy process. Energy Conversion and Management 1997;38(18):1815–22.

[87] Wang X, Feng Z. Sustainable development of rural energy and its appraisal system in China. Renewable and Sustainable Energy Reviews 2002;6:395–404.

[88] Ramanathan R, Ganesh LS. Energy resource allocation incorporating quantitative and qualitative criteria: an integrated model using goal programming and AHP. Socio Economic Planning Sciences 1995;29:197–218.

[89] Ramanathan R, Ganesh LS. A multi-objective programming approach to energy resource allocation problems. International Journal of Energy Research 1990;17:105–19.

[90] Elkarni F, Mustafa I. Increasing the utilization of solar energy technologies (SET) in Jordan: analytic hierarchy process. Energy Policy 1998;21:978–84.

[91] Hobbs BF, Horn GTF. Building public confidence in energy planning: a multi-method MCDM approach to demand side planning at BC gas. Energy Policy 1997;25(3):357–75.

[92] Yedla S, Shreshtha RM. Multicriteria approach for selection of alternative option for environmentally sustainable transport system in Delhi. Transportation Research part A 2003;37:717–29.

[93] Chattopadhyay D, Ramanathan R. A new approach to evaluate generation capacity bids. IEEE Transactions on Power Systems 1998;13:1232–7.

[94] Rahman S, Frair LC. A hierarchical approach to electric utility planning. International Journal of Energy Research 1984;8:185–96.

[95] Zong W, Zhihong W. Mitigation assessment results and priorities for China’s energy sector. Applied Energy 1997;56(3/4):237–51.

[96] Akash BA, Mamlook R, Mohsen MS. Multi-criteria selection of electric power plants using analytical hierarchy process. Electric Power Systems Research 1999;52:29–35.

[97] Diakoulaki D, Zopounidis DC, Doumpos M. The use of a preference desegregation method in energy analysis and policy making. Energy 1999;24(2):157–66.

[98] Mamlook R, Akash BA, Mohsen MS. A neuro-fuzzy program approach for evaluating electric power generation systems. Energy 2001;26:619–32.

[99] Mamlook R, Akash BA, Nijmeh S. Fuzzy set programming to perform evaluation of solar system in Jordan. Energy Conversion and Management 2001;42:1717–26.

[100] Srinivasan D, Liew AC, Chang CS. Applications of fuzzy systems in power systems. Electric Power Systems Research 1995;35(1):39–43.

[101] Brar YS, Dhillon JS, Kothari DP. Multiobjective load dispatch by fuzzy logic based searching weightage pattern. Electric Power Systems Research 2002;63(2):149–60.

[102] Mills D, Vlacic L, Lowe I. Improving electricity planning—use of a multicriteria decision making model. International Transactions in Operational Research 1996;3(3/4):293–304.

[103] Beccali M, Cellura M, Ardente DD. Decision making in energy planning: the ELECTRE multi criteria analysis approach compared to a fuzzy-sets methodology. Energy Conversion and Management 1998;39(16-18):1869–81.

[104] Skikos GD, Machias AV. Fuzzy multi criteria decision making for evaluation of wind sites. Wind Engineering 1992;6(4):213–28.