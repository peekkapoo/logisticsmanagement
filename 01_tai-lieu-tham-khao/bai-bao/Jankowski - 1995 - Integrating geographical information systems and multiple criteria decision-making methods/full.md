# Integrating geographical information systems and multiple criteria decision-making methods

Piotr Jankowski

To cite this article: Piotr Jankowski (1995) Integrating geographical information systems and multiple criteria decision-making methods, International Journal of Geographical Information Systems, 9:3, 251-273, DOI: 10.1080/02693799508902036

To link to this article: https://doi.org/10.1080/02693799508902036

![](images/e63cdd071270210d075ee8e99d82c4d23f759b363f62539245872e0ed86b7d92.jpg)

Published online: 05 Feb 2007.

![](images/fdea6d4ed095e5dabd6872eaa2e759def4b868e6523b4b047da6eef1ae327ffe.jpg)

Submit your article to this journal ↗

![](images/891660491d32bc9abcb892f3c3c8d1517d44a173e93e143026a7128502bfa822.jpg)

Article views: 11806

![](images/ccca8f60afaacc4d71f862d230a958686d365a1f971e5b812d32553e42dd6583.jpg)

View related articles ↗

![](images/ee75b08de96d8f3c6180c32b3cb8894b0fca1d6ce5024a940055afcf261ffa83.jpg)

Citing articles: 38 View citing articles ↗

# Integrating geographical information systems and multiple criteria decision-making methods

PIOTR JANKOWSKI

Department of Geography, University of Idaho, Moscow, Idaho 83844-3021 U.S.A.

(Received 15 December 1992; accepted 7 January 1994)

Abstract. Many spatial decision-making problems, such as site selection or land use allocation require the decision-maker to consider the impacts of choice-alternatives along multiple dimensions in order to choose the best alternative. The decision-making process, involving policy priorities, trade-offs, and uncertainties, can be aided by Multiple Criteria Decision making (MCDM) methods. This paper presents a framework for integrating geographical information systems (GIS) and MCDM methods. In this framework the MCDM methods are classified and matched with choice heuristics used by the decision-makers in the presence of competing alternatives and multiple evaluation criteria. Two strategies for integrating GIS with MCDM are proposed. The first strategy suggests linking GIS and MCDM techniques using a file exchange mechanism. The second strategy suggests integrating GIS and MCDM functions using a common database. The paper presents the implementation of the first strategy using PC-ARC/INFO, a file exchange module, and four different MCDM computer programs.

## 1. Introduction

In the early 1980s geographical information system (GIS) software emerged commercially as a new information processing technology offering unique capabilities of automating, managing, and analysing a variety of spatial data. From the early beginnings, dating back to the development of the Canadian Geographic Information System (CGIS) in the 1960s (Tomlinson 1988), GIS has been depicted as a decision support technology. Many applications of GIS developed over the last decade provided information necessary for the decision-making in diverse areas including natural resources management, environmental pollution and hazard control, regional planning, urban development planning, and utilities management. Cowen (1988) underscored the decision support function of GIS by describing it as a ‘decision support system’. This notion of GIS was disputed, however, by other researchers who argued that the current GIS technology does not offer sufficient decision support capabilities (Densham and Rushton, 1988, Goodchild 1989, Densham and Goodchild 1989, Harris and Batty 1991).

Two perspectives on developing better decision support capabilities of GIS can be identified, one based on analytical problem solving as a centrepiece of Spatial Decision Support System (SDSS) and another based on integration of GIS and specialized analytical models. According to the first perspective, SDSS should offer modelling, optimization, and simulation functions required to generate, evaluate, recommend, and test the sensitivity or problem solution strategies. These capabilities are essential to solving semi- or poorly structured spatial decision-making problems. The model-based approach of SDSS represents an alternative and an extension of a toolkit approach embodied in the current generation of GIS software offering enough flexibility to accommodate a wide range of geometric operations at the expense of modelling, optimization, and dynamic simulation functions. The second perspective on improving the decision support capabilities focuses on the expansion of GIS descriptive, prescriptive, and predictive capabilities by integrating GIS software with other general software packages (e.g., statistical software) and with specialized analytical models such as environmental and socio-economic models (Goodchild 1987, Dangermond 1987, Burrough et al. 1989, Birkin et al. 1990, Nyerges 1993, Maidment 1993). According to this view, mapping, query, and spatial modelling functions of GIS can provide data display at different scales, preprocessing, and data input for environmental and statistical models. Different levels of integration between GIS and analytical models can be considered, starting from a loose integration where GIS and models are linked using a file exchange mechanism, through a tighter integration with a common user interface and user-transparent file exchange process, to a fully integrated GIS modelling system with shared memory and a common file structure (Fedra 1993).

Both perspectives share a common concern for providing better procedures for spatial decision-making support. Within this framework, Multiple Criteria Decision-Making (MCDM) methods received in the past little attention despite their ample potential as spatial decision support tools. A few but notable contributions on integrating of GIS and multiple criteria evaluation techniques can be found in the papers by Janssen and Rietveld (1990), Janssen and van Herwijnen (1991), and Carver (1991). A more recent and concentrated research effort at integrating GIS and MCDM methods has been undertaken by the IDRISI Project team at Clark University (Eastman et al. 1993).

The general objective of MCDM is to assist the decision-maker (DM) in selecting the 'best' alternative from the number of feasible choice-alternatives under the presence of multiple choice criteria and diverse criterion priorities. The problem of multicriterion (multi-objective) choice in decision making is the paramount challenge faced by individuals, public, and private corporations. The nature of the challenge is two-fold;

1. How to identify choice alternatives satisfying the objectives of parties involved in the decision-making process.

2. How to reduce/order the set of feasible choice alternatives to identify the most preferred alternative.

The challenge of multicriterion choice can be attributed to many spatial decision-making problems involving search and location/allocation of resources (for applications of MCDM in spatial decision-making problems see Massam 1980, and Voogd 1983). These problems, often analysed in GIS, include location/site selection for: service facilities, recreational activities, retail outlets, hazardous waste disposal sites, and critical areas for specific resource management and control practices. Other examples include the selection of optimal utility routes in urban/rural areas such as powerline routes (Harris 1992), or the selection of water pipeline routes (Jankowski and Richard 1994), and land use decision-making involving trade-offs among conflicting land uses at individual parcel locations (Berry 1992).

The purpose of this paper is twofold: (1) to clarify the role of GIS and multicriteria decision-making methods in supporting spatial decision-making, and (2) to present a framework for integrating GIS with MCDM. The rest of the paper proceeds as follows. A brief exposition of the rational model of the decision-making process and the role of GIS are discussed in section two. Section three presents an overview and classification of multiple criteria decision-making techniques. The choice heuristics used by the decision-makers in the presence of competing alternatives and evaluation criteria are presented in section four. A few of these heuristics can be implemented directly in GIS using the database processing capabilities of commercial GIS software. Others, that cannot be implemented directly in GIS, can be matched with the selected MCDM techniques. The recommendations for the effective integration of GIS and MCDM are provided in section five followed by an implementation example.

## 2. GIS and the rational model of the decision-making process

The fundamental concept of various models of individual and organizational decision-making behaviour is rationality. The conceptual origins of the term rationality can be traced back to the philosophy of Rationalism which asserts the superiority of intellect over empirical experience (Encyclopaedia Britannica 1974). Simon (1957) argued for replacing the concept of rationality, built into the classical model of decision-making, with the principle of bounded rationality. According to this principle, individuals and organizations follow a satisficing decision-making behaviour, based on search activity, to meet certain aspiration levels rather than the optimizing behaviour aimed at finding the best decision alternative. In his more contemporary work Simon (1978, 1979) presented the concept of procedural rationality which means the effectiveness of decision support procedures in search of the relevant decision alternatives. The procedurally rational model of decision-making process distinguishes the following four steps that are generally appropriate for a structured approach to decision situations (McKenna 1980):

1. Problem definition: a discrepancy between the present state and the desired state is recognized as a need. That need is formulated as a problem calling for decision.

2. Search for alternatives and selection criteria: the feasible alternatives (potential problem solutions) and criteria for evaluating the alternatives are established.

3. Evaluation of alternatives: the impacts of each alternative on every evaluation criterion are assessed.

4. Selection of alternatives: alternatives are ordered from the most desirable to the least desirable and either the top alternative is selected or the group of more desirable alternatives is retained for further evaluation.

The role of GIS in implementing this model in spatial decision-making has been the search for feasible alternatives (step 2). The search for feasible sites, routes, and land use allocations has been traditionally carried out using manual map overlays as part of suitability analysis. The basic tenants of this approach involved the specification of physical, economic, and environmental criteria important in determining the technical and social feasibilities of the project, and next the cartographical representation of these criteria on map layers. All of the layers were then overlaid using transparencies and the lightest areas represented the most desirable decision alternatives (McHarg 1969). With the advent of GIS and its capability to overlay digital maps, land suitability studies became more sophisticated. For example, Harris (1992) reported a powerline siting study that included 40 various physical, environmental, and socio-economic suitability factors.

Suitability analysis often results in generating a number of feasible alternatives. This can be due not only to more than one alternative satisfying technical suitability criteria but also due to political context of the decision making process that requires taking into account additional social and environmental criteria. Different strategies can be applied to reduce/order the set of feasible alternatives and hence, to facilitate the choice. One possible strategy suggests introducing for every decision criterion a threshold value that must be passed by an alternative in order to qualify. The threshold values can be gradually tightened until only one alternative is left. This approach, called the reduced processing strategy (Hong and Vogel 1991), does not set a high cognitive demand before the decision-maker since it does not require the evaluation of trade-offs among the alternatives. The reduced processing strategy can be implemented in GIS by an iterative suitability analysis resulting in step-by-step reduction of feasible alternatives. Such a procedure is, however, time consuming when the number of alternatives is large. A faster approach is to apply GIS in conjunction with one of the reduced processing MCDM techniques. In this approach the initial set of feasible alternatives is still generated in GIS but the reduction process is carried out using a MCDM technique. The final result may be visualized using the GIS display capabilities. This approach can be enhanced by integrating MCDM techniques with GIS.

Another strategy to reduce and/or order the set of GIS-generated, feasible alternatives is to include in the analysis the DM's preferences. These preferences may concern the decision criteria and performance levels of alternatives on every decision criterion. The process of quantifying the DM's preferences requires making trade-offs among the criteria and it is cognitively demanding, especially if the number of criteria is large. This strategy, called full processing, can also be implemented by integrating the processing capabilities of GIS with the structured decision-making approach featured by MCDM techniques.

In many instances the decision-making process involves a group of decision-makers representing different, often conflicting interests. Examples of such decision-making problems include many environmental dilemmas, such as, selection of habitat restoration sites, land use allocation, or siting of utility line corridors. In these problems, choice strategies aimed at reducing/ordering the set of GIS-generated feasible alternatives should include the consideration of multiple and conflicting viewpoints, and facilitate a movement towards consensus. These capabilities, lacking in the current GIS software, can be created by integrating GIS with MCDM techniques useful in the group decision making context (Hwang and Lin 1987).

The following section provides a brief overview and classification of MCDM techniques that can be potentially useful for integrating with GIS.

## 3. Multiple criteria decision—making-an overview of the methodology

It is a widely accepted notion in the literature that MCDM consists of two categories: multiple attribute decision making MADM and multiple objective decision-making MODM (Cohon 1978, Hwang and Masud 1979, Hwang and Yoon 1981). MADM is concerned with choice from a moderate/small size set of discrete actions (feasible alternatives), while MODM deals with the problem of design (finding a Pareto-optimal solution) in a feasible solution space bounded by the set of constraints (Colson and De Bruyn 1989). MADM is often referred to as multicriteria analysis (Teghem et al. 1989) or multicriteria evaluation (Nijkamp et al. 1990, Voogd 1983), whereas MODM is viewed as a natural extension of mathematical programming, where multiple objectives are considered simultaneously. This paper deals with MADM which involves choosing, based on the decision criteria and criterion priorities, from a moderate/small size set of alternatives; hence the term multiple criteria decision-making (MCDM) will be used in reference to MADM.

![](images/d235579acab47984751344c8588491d05ff4ec8acec4245ad9ff22f177288a89.jpg)  
Figure 1. A general model of MCDM.

## 3.1. A general model of MCDM

The point of departure for any MCDM technique is the generation of the discrete set of alternatives, the formulation of the set of criteria, and the evaluation of the impact of each alternative on every criterion. Every MCDM technique shares a common approach called here a general model of MCDM (figure 1).

The estimated impacts of alternatives on every criterion, called criterion scores, are organized into a decision matrix C:

$$
C = \left[ \begin{array}{c} c _ {1 1} \dots c _ {1 I} \\ \vdots \qquad \vdots \\ c _ {J 1} \dots c _ {J I} \end{array} \right]\tag{1}
$$

where:

$c_{Jl}$ is the criterion score,

$J =$ represents criteria.

I = represents alternatives.

Depending on the MCDM technique the criterion scores may be aggregated in a nonstandardized format (raw scores) or in standardized format (standardized score).

Various linear and nonlinear standardization procedures exist that normalize the criterion scores so that $0 < = c_{JI} < = 1$ (Hwang and Yoon 1981, Voogd 1983, Jankowski 1989).

The second element of MCDM techniques, besides the criterion scores, is the DM's preferences. The preferences may be formulated in regard to criterion scores taking the form of cut-off values (minimum or maximum threshold) or the desired aspiration levels (Lotfi et al. 1992). They may also be formulated in regard to decision criteria and expressed in a cardinal vector of normalized criterion preference weights w where:

$$
\mathbf {w} = (w _ {1}, w _ {2}, \dots , w _ {J}), \quad \text { and } \quad 0 <   = w _ {J} <   = 1\tag{2}
$$

The criterion scores and the DM's preferences are processed using single or multiple aggregation functions that return a solution in the form of either:

1. One recommended alternative.

2. Reduced decision space consisting of several 'good alternatives'.

3. Ranking of alternatives from best to worst.

In many real world decision-making problems, criterion scores express predictions of impacts likely to be caused by the adoption of a given alternative and as such are prone to imprecisions of forecast and uncertainties of the future. In addition, the DM's preferences are often inconsistent, subject to shifting, and inaccuracies in determination (Bouyssou 1991). The problems of imprecision, uncertainty, and inaccurate determination are addressed in MCDM techniques by the sensitivity analysis of decision recommendations. There are two common approaches to sensitivity analysis in MCDM techniques:

1. Considering two alternatives at a time by calculating changes in weight values and changes in criterion scores required to bring the two alternatives to an equal position in the final ranking (Nagel and Long 1989).

2. Considering all alternatives taking part in the evaluation process and calculating changes in their ranking positions as the result of changing criterion scores and criterion weights.

## 3.2. Classification of MCDM techniques

The MCDM techniques can be classified according to the level of cognitive processing demanded from the DM and the method of aggregating criterion scores and the DM's priorities (figure 2).

According to the cognitive processing level two classes of MCDM techniques can be distinguished: compensatory and noncompensatory (Hwang and Yoon 1981). The compensatory approach is based on the assumption that the high performance of an alternative achieved on one or more criteria can compensate for the weak performance of the same alternative on other criteria. In a compensatory MCDM technique the high score of an alternative achieved on one criterion is traded off, according to the DM's preference structure, for the low score received on another criterion. This means that a low score of a given alternative on a high-preference criterion may be compensated by a high score on another high preference criterion, or it may require high scores on two low-preference criteria to offset a low score on one high-preference criterion. The compensatory approach is cognitively demanding since it requires the DM to specify criterion priorities expressed as cardinal weights or priority functions.

![](images/eee911c2c03dafd606ae1fc68c36bbd278c628d2557b61b63e9e5a277c4c7bd4.jpg)  
Figure 2. Classification of MCDM techniques. The superscripts denote criteria priorities (CP) and criterion score priorities (CSP). The techniques listed in the figure constitute a limited representation of the full set of MCDM techniques. For a more complete account of MCDM techniques see Ozernoy (1992).

Under the noncompensatory approach a low criterion score for an alternative cannot be offset by another criterion's high score. The alternatives are compared along the set of criteria without making intra-criterion trade-offs. The noncompensatory approach is cognitively less demanding than the compensatory approach since it requires, at the most, the ordinal ranking of criteria based on the DM's priorities.

## 3.2.1. Compensatory MCDM techniques

The class of compensatory MCDM techniques can be divided further, according to the method of aggregating criterion scores and the DM's priorities, into two subclasses;

1. Additive techniques.

2. Techniques based on the ideal point approach.

Within both subclasses the MCDM techniques can be further distinguished based on the approach to formulating the DM's priorities. The two approaches included in figure 2 are: priorities regarding the decision criteria (criteria priorities or CP) and priorities regarding the value levels of criterion scores (criterion score priorities or CSP).

In the additive techniques the criterion scores are standardized to enable the inter-criterion trade-offs and to allow the comparison of the alternative performance on a common scale. The total score for each alternative is calculated by multiplying the criterion weight by the criterion performance score. The alternative with the highest score is recommended as the top choice. Weighted Summation (Voogd 1983) is probably the best known representative of the subclass. The basic form of the weighted summation technique can be depicted in this matrix notation:

$$
\left[ \begin{array}{c} s _ {1} \\ \vdots \\ s _ {I} \end{array} \right] = \left[ \begin{array}{c} c _ {1 1} \dots c _ {J 1} \\ \vdots \qquad \vdots \\ c _ {1 I} \dots c _ {J I} \end{array} \right] \times \left[ \begin{array}{c} w _ {1} \\ \vdots \\ w _ {J} \end{array} \right]\tag{3}
$$

where:

$s_{I} =$ appraisal score for alternative $I$ , and the criterion scores matrix is the transpose of the decision matrix $C$

The assumptions behind this technique are that the weights are cardinal, the criterion scores are determined on the interval/ratio scale, and data is aggregated by addition.

The Concordance Analysis, which is the most common technique based on pairwise comparison, determines the ranking of alternatives by means of pairwise comparison of alternatives. The comparison is based on calculating the concordance measure which represents the degree of dominance of alternative i over alternative $i'$ for all the criteria for which i is equal or better than $i'$ , and the discordance measure which represents the degree of dominance of alternative $i'$ over alternative i for all the criteria for which $i'$ is better than i (Nijkamp and van Delft 1977, Nijkamp et al. 1990). The calculations of concordance and discordance measures are carried out in concordance analysis for every pair of alternatives,. Based on these measures the differences between alternatives are quantified and a final score is calculated for every alternative. The final score is then used to rank the alternatives from best to worst.

Other MCDM techniques belonging to this subclass include the Analytical Hierarchy Process–AHP (Saaty 1980) which uses a hierarchical structure of criteria and both additive transformation function and pairwise comparison of criteria to establish criterion weights, and the Multi-Attribute Tradeoff System–MATS (Brown et al. 1986) in which the DM's utility functions are derived for every criterion and criterion weights are calculated based on inter-criteria trade-offs. The utility functions are used to derive utility values for every criterion score. The utility values are then combined with criterion weights, using the additive function, to obtain the total score for every alternative.

In the techniques based on the concept of an ideal point the DM is asked to locate in n-dimensional space his/her ideal solution, i.e., to specify the most desirable value for each decision criterion. Then, the distance between the ideal solution and each considered alternative is measured using a Euclidean or a non-linear distance measure in order to arrive at the ranking of alternatives.

Technique for Order Preference by Similarity to Ideal Solution—TOPSIS (Hwang and Yoon 1981), Aspiration-level Interactive Method—AIM (Lotfi et al. 1992), and Multi-Dimensional Scaling—MDS (Voogd 1983) are three examples of techniques based on the intuitive concept that the chosen alternative should be as close as possible to the ideal solution and as far away as possible from the worst solution. The two techniques: TOPSIS and MDS use the criterion preference approach to representing the DM's preferences. The AIM technique uses the criterion score preferences approach in which the DM determines his/her levels of aspiration for different criterion score values.

## 3.2.2. Noncompensatory MCDM techniques

A common facet of the noncompensatory techniques is the stepwise reduction of the set of alternatives without trading off their deficiencies along some evaluation criteria for their strengths along other criteria (Hwang and Yoon 1981, Minch and Sanders 1986). The differences among these techniques result from the following different rules of elimination:

(a) The Dominance technique: the elimination is based entirely on criterion scores; an alternative is dominated, and hence eliminated from further consideration, if there is another alternative which is better on one or more criteria and is equal on the remaining criteria.

(b) The Conjunctive method: every criterion has a minimum cut-off value specified by the DM. Those alternatives that fail a cut-off value on any of the evaluation criteria are eliminated.

(c) The Disjunctive method: also uses cut-off values but in this method an alternative is eliminated if it fails to exceed a minimum cut-off value on at least one of the evaluation criteria.

(d) The Lexicographic method: requires that the evaluation criteria be ranked from the most important to the least important. The alternatives are compared first on the most important criterion and the alternative with the highest criterion performance score wins; all the other alternatives are eliminated. If more than one alternative is left the evaluation continues on the second most important criterion, third, etc. The lexicographic technique uses both the DM's criterion score preferences (CP) to rank the criteria and the DM's criterion score preferences (CSP) to compare the alternatives

In general, the noncompensatory MCDM techniques require from the DM the reduced level of cognitive processing and hence, can be useful in decision making situations where the DM cannot or is unwilling to formulate his/her preferences. The disadvantage of these techniques is a potential for recommending an inferior alternative due to their reduced processing strategy.

## 4. Choice strategies and selection of MCDM techniques

Hong and Vogel (1991) identified five different choice strategies used by decision-makers that can be matched with characteristics of different MCDM techniques. These choice strategies include:

1. Screening of absolute rejects: elimination of clearly dominated alternatives as the first step before any further choice deliberation,

2. Satisficing principle: the DM will consider all the alternatives that satisfy conjunctively or disjunctively the minimum performance levels,

3. First-reject: the DM wants to use exclusively the conjunctive elimination rule to reject all the alternatives that do not pass minimum threshold values,

4. Stepwise elimination: The DM narrows down the choice re-evaluating the set of remaining alternatives every time one of the alternatives is eliminated,

5. Generation of linear ordering: the DM wants to generate a ranking of alternatives from the most preferred to the least preferred one.

The first four choice strategies can be implemented using exclusively the noncompensatory MCDM techniques. The last strategy (generation of linear ordering)

requires the full processing approach and hence, can be implemented using the compensatory MCDM techniques.

Below, the five choice strategies are matched with the MCDM techniques presented in figure 2.

```ini
absolute rejects = => [dominance]
satisfying principle = => [Conjunctive, Disjunctive]
first-reject = => [Conjunctive]
stepwise elimination = => [Lexicographic]
generation of linear orderings:
with criteria = => [Weighted Summation, Concordance
preferences Analysis, AHP, TOPSIS, MDS]
with criterion = => [AIM]
score preferences
with criterion preferences = => [MATS]
and criterion score preferences
```

The three variants of the ‘generation of linear orderings’ choice strategy were distinguished based on three different approaches to representing the DM’s priorities in the MCDM techniques represented in figure 2.

There exists empirical evidence that decision-makers use different choice strategies at different stages of the decision-making process (Wright and Barbour 1977). Hence, one can assume that different sequences of choice strategies can be used in decision-making situations concerning spatial decision-making problems. For example, the sequence of {first-reject, generation of linear orderings} could be used in a site selection problem if the DM desires first to drop the clearly inferior alternatives and next to rank the 'good' alternatives from most to least desirable. This situation is illustrated with the following route selection problem described in Jankowski and Richard (1994).

The Seattle Water Department (SWD 1988) studied various alternatives for selecting a route for a new section of a primary water transmission line for the City of Seattle and its purveyors in King Country, Washington (figure 3).

The proposed alternatives were all located within the environmentally sensitive Snoqualmie River Valley region, making this an appropriate example of the multicriteria decision problem. In the initial study, conducted by the Seattle Water Department, the alternatives were identified with a manual, suitability mapping approach. In the verification study conducted by Richard (1992) a GIS-based approach was used. The decision criteria included: total cost (TOTALCOST) estimated for each route alternative, the amount of public right-of-way (ROWACRES) falling within the alternative right-of-way, the reliability criteria including the normal daily traffic volume of roads (VEH\_DAY) which fall with and parallel the alternatives' rights-of-way, erosion hazard areas (ERSACRES), landslide hazard areas (LNDACRES), seismic hazard areas (SEIACRES), and the environmental criteria including the area of wetlands (WETACRES) and the length of stream segments (STRMLEN) falling within the alternatives' rights-of-way. The additional criterion included in the analysis was the length of alternative (ALTLEN).

The conjunctive selection rule, representing the ‘first reject’ strategy, was applied to reduce the initial set of pipeline route alternatives. The choice rule included a combination of technical, land use, topographic, geological, and economic constraints that had to be satisfied by the alternatives. The six alternatives that passed the conjunctive selection rule are listed in table 1 together with the decision criteria and criterion scores.

![](images/4d7c3187715ddcea5a8c6d21638249f303f854dc2e8b6ef1378cf3d17f158d81.jpg)  
Figure 3. Study area for a water transmission line in King County, Washington.

The six pipeline route alternatives can be ordered from best to worst applying the choice strategy ‘generation of linear orderings’. One variant of this strategy, that uses criterion utility functions for expressing criterion score preferences and weights for representing preferences on criteria can be implemented by the Multi-Attribute Utility Tradeoff System technique—MATS.

MATS, implemented as a stand-alone, interactive computer program that runs on DOS-based microcomputers (Brown et al. 1986), requires the DM to enter first decision criteria and to define a numeric scale for every criterion by entering a maximum and minimum values. Next, with the help of program's interrogation/specification mode, the utility functions are derived by the user for every criterion. A criterion utility function describes how much utility is received from each value of the criterion score. The utility values are normalized and range in the interval $\langle 0,1\rangle$ .

Following the specification of criterion score preferences through the criterion utility functions the user is asked to define the preferences regarding the decision criteria. The decision criteria preferences are derived through the series of trade-off questions in which the user is asked to evaluate the relative importance of one criterion versus the other criterion. The decision criteria preferences are then quantified into standardized weights that sum to 1.0. In the next step the user enters the names of decision alternatives and the criterion scores. MATS uses the following aggregation function to calculate the final score for each decision alternative:

$$
S _ {i} = \sum_ {j = 1} ^ {J} U f _ {j} (c _ {j i}) w _ {j}\tag{4}
$$

where:

$S_{i} =$ final score for alternative $i$ .

$c_{ji} =$ criterion score for criterion $j$ and alternative $i$

$Uf_{j} =$ utility function of criterion $j$

$w_{j} =$ cardinal weight of criterion $j$ .

Table 1. Six conjunctively selected alternatives with the decision criteria and criterion scores.

<table><tr><td>ALT.NAME</td><td>ROWACRES [acres]</td><td>ERSACRES [acres]</td><td>SEIACRES [acres]</td><td>LNDACRES [acres]</td><td>WETACRES [acres]</td><td>STRMLEN (m)</td><td>VEH_DAY (cars)</td><td>ALTLEN (km)</td><td>TOTALCOST [$ millions]</td></tr><tr><td>ALT1</td><td>70.27</td><td>6.24</td><td>15.7</td><td>4.91</td><td>5.71</td><td>502</td><td>8200</td><td>12.38</td><td>27.1</td></tr><tr><td>ALT2</td><td>53.25</td><td>10.05</td><td>12.76</td><td>4.03</td><td>5.07</td><td>206</td><td>8200</td><td>11.83</td><td>25.2</td></tr><tr><td>ALT3</td><td>15.28</td><td>13.76</td><td>15.00</td><td>5.22</td><td>1.09</td><td>1347</td><td>4900</td><td>25.57</td><td>23.6</td></tr><tr><td>ALT4</td><td>34.54</td><td>13.53</td><td>16.12</td><td>4.78</td><td>0.86</td><td>883</td><td>6300</td><td>9.88</td><td>24.4</td></tr><tr><td>ALT5</td><td>35.85</td><td>12.03</td><td>22.93</td><td>13.85</td><td>6.52</td><td>675</td><td>7240</td><td>37.05</td><td>24.7</td></tr><tr><td>ALT6</td><td>29.78</td><td>9.36</td><td>16.28</td><td>3.44</td><td>6.91</td><td>191</td><td>8200</td><td>8.1</td><td>15.6</td></tr></table>

In the water pipeline route selection problem the following criterion weights, consistent with preferences stated by a citizen advisory committee (Richard 1992), were used:

<table><tr><td>Criterion</td><td>Weight</td></tr><tr><td>ROWACRES</td><td>0·130</td></tr><tr><td>ERSACRES</td><td>0·057</td></tr><tr><td>SEIACRES</td><td>0·057</td></tr><tr><td>LNDACRES</td><td>0·057</td></tr><tr><td>WETACRES</td><td>0·053</td></tr><tr><td>STRMLEN</td><td>0·027</td></tr><tr><td>VEH_DAY</td><td>0·053</td></tr><tr><td>ALTLEN</td><td>0·284</td></tr><tr><td>TOTALCOST</td><td>0·284</td></tr></table>

The ranking of six alternatives based on standardized final score values calculated by MATS is presented below:

<table><tr><td>Alternative</td><td>Final score</td></tr><tr><td>ALT6</td><td>0.821</td></tr><tr><td>ALT4</td><td>0.638</td></tr><tr><td>ALT2</td><td>0.572</td></tr><tr><td>ALT3</td><td>0.543</td></tr><tr><td>ALT1</td><td>0.478</td></tr><tr><td>ALT5</td><td>0.270</td></tr></table>

The sensitivity analysis of the solution, facilitated by MATS, revealed that the alternative route ALT6 was firm in the first position. It would take a significant improvement in the total cost of the second-ranked route (ALT4), or a simultaneous improvement in values of at least four other criteria, in order for ALT4 to tie ALT6.

Another variant of the decision strategy ‘generation of linear orderings’ incorporates the DM’s priorities only in regard to decision criteria. This variant can be implemented using, among others, a MCDM Weighted Summation technique. In this example the Best Choice program (Nagel and Long 1989) was used to rank the alternatives ALT1 through ALT6. Best Choice requires the user to enter names of alternatives, decision criteria, the measurement units of criteria, and weights for each criterion. The criterion scores for each alternative are then entered into a decision matrix with alternatives represented by rows and criteria by columns. The program analyzes data by converting scores to percentages in order to deal with the multidimensionality of data, and a summary score is computed for each alternative. Negative (cost) criteria are handled simply by placing a negative sign in front of the criterion scores, or by taking the reciprocal of the criterion scores. The sensitivity analysis in Best Choice allows the user to see how much the criterion score or the criterion weight must change to alter the results of the analysis.

The ranking of six alternatives based on final score values calculated by Best Choice, using the same criterion weights as in MATS, is presented on top of the next page.

<table><tr><td>Alternative</td><td>Final Score (%)</td></tr><tr><td>ALT6</td><td>25·27</td></tr><tr><td>ALT4</td><td>18·03</td></tr><tr><td>ALT3</td><td>16·59</td></tr><tr><td>ALT2</td><td>15·26</td></tr><tr><td>ALT1</td><td>14·17</td></tr><tr><td>ALT5</td><td>10·90</td></tr></table>

The final ranking obtained from Best Choice is very similar to the ranking obtained from MATS. This can be explained by the same type of aggregation function used in both programs, and by the fact that utility functions derived in MATS were nearly linear. The final ranking might have been quite different if the utility functions were concave or convex.

## 5. Strategies for integrating GIS and MCDM

The choice of MCDM techniques and an approach to integration with GIS depends on the type of data model used in GIS. In a raster-based GIS each individual cell is regarded as a choice alternative and hence, it is a candidate for evaluation. The number of cells, in the majority of raster maps, makes it impractical to use computationally intensive MCDM techniques based on pairwise comparisons of all alternatives (i.e., concordance analysis). In this case one can advocate weighted summation as the useful and practical MCDM technique for raster GIS. The multiple criteria evaluation, with weighted summation integrated into a raster GIS, becomes then a two-step procedure where a suitability map is developed first, followed by the rank-ordering of cells.

In a vector-based GIS the multiple criteria evaluation can also be carried out as a two-step procedure, where the first step involves creating a suitability map and the second step rank-ordering the alternatives represented by points, lines, or polygons. The difference between the multiple criteria evaluation in vector GIS and raster GIS is a relatively small number of suitable alternatives obtained from step one in a vector system in comparison to a number of raster cells. This makes possible integrating vector-based GIS and MCDM techniques other than weighted summation.

Nyerges (1993) distinguished loose and tight coupling as two approaches to interfacing GIS and computer environmental models. These two approaches can be followed when integrating GIS with MCDM techniques. In the remainder of this section the conceptual basis of loose and tight coupling of GIS and MCDM are outlined followed by an example of implementing the loose coupling approach in a vector-based GIS.

## 5.1. The loose coupling strategy

The main idea of loose coupling approach is to facilitate to integration of GIS and MCDM techniques using a file exchange mechanism. The assumption behind this strategy is that MCDM techniques already exist in the form of stand alone computer programs, which is true for many of the techniques reviewed in §3 (Lotfi and Teich 1991, Radcliff 1986). Each of these programs comes with its customized interface and the user is faced with different interfaces when running a sequence of different MCDM techniques. The results of the decision analysis may be sent to GIS for display and spatial visualization.

The integration of GIS and MCDM in the loose coupling architecture is based on linking three modules:

— GIS module

— MCDM techniques module, and

— File Exchange Module (see figure 4).

The GIS module is used for generating the set of spatial decision alternatives (e.g., sites, routes, land uses) in the course of performing land suitability analysis. The alternatives can be represented in two different ways: (1) each alternative is represented by a separate GIS map coverage, (2) each alternative is represented by one record or multiple records in one composite coverage. The set of decision criteria consists of map coverage attributes. The coverage attribute values serve as the criterion scores.

According to the loose coupling strategy the land suitability analysis is run through the GIS user interface. The results of analysis including the set of alternatives, the set of decision criteria, and criterion scores can be represented in a two-dimensional decision table with criteria in rows, decision alternatives in columns, and table elements as criterion scores. The decision table is generated as an ASCII-format file in the File Exchange module. The File Exchange module consists of programs that extract the GIS coverage attributes, create the decision table, and change its format to different input file formats required by MCDM programs.

## 5.2. The tight coupling strategy

The tight coupling strategy differs from the loose coupling by using multiple criteria evaluation functions fully integrated into GIS, a shared data base, and a common user interface (figure 5)

Under this approach the GIS evaluation functions facilitate the spatial decision-making with multiple criteria. The functions include: generation of decision table, enumeration of decision-maker's preferences, selection of aggregation function, and sensitivity analysis. These functions represent operations common to many MCDM techniques. However, instead of accessing a specific MCDM technique, like in the loose coupling approach one can select a function from a common GIS user interface. This makes the multiple criteria evaluation functions a part of the GIS tool box.

The evaluation functions contain specific operations that can be selected by the user. For example, the function enumerating DM's preferences can be carried out by: (1) rating (Voogd 1983), (2) pairwise comparison of criteria using a 9-point scale (Saaty 1980), and (3) inter-criteria trade-offs based on attribute values (Brown et al. 1986). The function ‘select aggregation function’ offers the selection of: (1) weighted summation, (2) outranking based on pairwise comparison, (3) additive utility function, and (4) ideal point distance function. The function ‘sensitivity analysis’ allows one to select: (1) dynamic sensitivity option in which the user can see the change in final scores of alternatives as one increases and decreases the weight of any criterion, and (2) threshold analysis option which calculates new values for criterion scores and weights that would have to be adopted in order to rank any two selected alternatives (e.g., the winner and the runner-up) equally.

The GIS database module serves as the repository of choice alternatives (sites, routes, land use areas) whose spatial features are represented by points, lines, and areas. The specification of alternatives and evaluation criteria is made by the user from the system's interface. The data extraction into the decision table is performed transparently.

![](images/362d59633aed720f45454abf5a7f946bb7fd60eae147b18e076ca7dee2e00ea1.jpg)  
Figure 4. The loose coupling architecture for linking GIS and MCDM.

![](images/6aef418d6de4f4117b70ac8e8e8348c5afb73897ede35fc2454eacf8a6dca2d3.jpg)  
Figure 5. The tight coupling architecture for linking GIS and MCDM.

![](images/19c1253aa239c334d4be4ccbe4b9c1fa09a50f0a1f926924dee23592dd24c543.jpg)  
Figure 6. The directory structure of the prototype implementation of loose coupling strategy.

The GIS interface, under the proposed design, will facilitate the map views of alternatives and their criteria. The user will be able to select any number of criteria and up to two alternatives that will be displayed in two simultaneous map views. In the case of selecting two alternatives the monitor's display will be split into two halves facilitating the pairwise comparison of alternatives on selected criteria. The quantitative comparisons can be further enhanced by displaying tables with criterion scores representing the performance of alternatives on selected criteria, and charts (pie, bar, line and spider web charts). The qualitative comparisons can be facilitated by changing the scale of a map view to better assess spatial relationships, combining map views with hypertext, photographic images, sound, and video animation. The comparative mode of visualizing the spatial properties of alternatives can help in formulating the decision-maker's preferences and trade-offs articulated in criterion weights.

## 5.3. Implementation of the loose coupling strategy

The integration of a vector-based GIS and MCDM was developed using the loose coupling strategy outlined in § 5.1. The integrated system has three components: a GIS module, MCDM module, and file exchange module (figure 6).

The GIS module is comprised of the PC-ARC/INFO $^{®}$ 3.4D (commercial GIS software from ESRI, Redlands, CA) that runs on DOS-based microcomputers. PC-ARC/INFO is used for land suitability analysis that results in generating feasible alternatives. These are the alternatives satisfying physical and technical constraints imposed on ARC/INFO coverage attributes. The current implementation requires that every alternative be represented by one ARC/INFO coverage.

The MCDM module is a collection of four stand-alone DOS-based computer programs implementing different MCDM techniques included in figure 1. These programs are:

1 Best Choice: the interactive computer program based on the weighted summation technique (Nagel and Long 1989). Best Choice can accept up to 15 alternatives and 15 decision criteria. The DM's preferences on decision criteria are represented by cardinal weights.

2 Aspiration-Level Interactive Method—AIM 3.0: the interactive computer program based on the ideal-point approach (Lotfi et al. 1992). The maximum size of the decision table accepted by AIM is 50 alternatives and 10 criteria. The DM's preferences are represented in AIM by the aspiration levels on criterion scores.

3 Expert Choice 8.0: the interactive computer program based on Analytic Hierarchy Process—AHP (Saaty 1990). The program uses the hierarchical structure of criteria and pairwise comparisons among the criteria to establish criterion weights. The additive transformation function of the weighted summation approach is used to calculate a final score for each alternative. There is no limit on the size of decision problem accepted by Expert Choice. The DM's preferences on criteria are represented by cardinal weights.

4 MCDM-Windows: the interactive computer program that includes three different MCDM techniques: Conjunctive, Disjunctive, and TOPSIS. The conjunctive and disjunctive techniques are based on cutoff values as the decision rule for eliminating inferior alternatives, and TOPSIS is based on the ideal point approach. The program was developed by the author and his students as part of the GIS-MCDM integration project. There is no limit on the size of the decision table accepted by MCDM-Windows. In conjunctive and disjunctive techniques the DM's preferences on criterion scores are represented explicitly by cutoff values. The TOPSIS technique represents the DM's preferences on criteria in the form of cardinal weights.

The file exchange module is comprised of two programs: one that generates the decision table and the other that changes its format to input file formats of the four MCDM programs. An input file containing the decision table can then be opened from a selected MCDM program by the user. The generation of a decision table is carried out by an interactive program written in SML (Simple Macro Language of PC-ARC/INFO). The formatting of the decision table file is carried out by a program written in Turbo PASCAL version 6.0.

## 5.3.1. Operation of the file exchange module

After preparing the decision alternatives in PC-ARC/INFO and storing them in separate coverages the user can access the file exchange module. The user is presented first with a dialogue menu asking for the name of a file that will store the decision table and then with another menu asking to select the decision alternatives from the PC-ARC/INFO coverage list (figure 7).

In response to the selected alternatives the SML program presents the user with another menu containing the choice of three different formats for attributes (figure 8).

Under this specification an attribute value extracted from a coverage is the sum of all record values for this attribute. If an alternative is represented by a point coverage then the extracted attribute value will be represented only by one record since one point represents one alternative. If an alternative is represented by either a line or a polygon coverage then the extracted attribute value will be represented by the sum of line or polygon records, since a line or an area may be comprised of multiple line segments or multiple polygons. The choice of formats for the extracted attribute values include: (1) the sum of all records for a given attribute, (2) the percentage ratio of two attributes, and (3) the product of attribute value and the user-specified constant value.

Following the selection of the format for the first attribute the program extracts and displays the attribute names of the selected alternatives. It is assumed that all attributes representing the decision criteria are shared by the alternatives. After the user selects

Selecting the coverages to be used as alternatives ...

Coverage Number: 1

![](images/6222032cf3b26575209661c3f0ee483d5f48f2bbe1d6966f260d6e2ac80b004b.jpg)  
Figure 7. Menu with the example selection of decision alternatives.

Formatting the attribute information ...

![](images/216028ed2e74e4af3cc884f773092d0070f9370a23b1cef3389a7a1080afe010.jpg)  
Figure 8. Menu with the attribute formats.

one attribute its values are extracted from the selected alternatives (coverages) and written into an ASCII file representing the decision table. This step, including the selection of the attribute format, is then repeated for other attributes chosen by the user as the decision criteria.

After the decision table is completed the user is presented with the final selection menu (figure 9).

The selection made in this menu is carried out by the PASCAL program that changes the original format of the decision table to the input file format of the selected MCDM program. The decision table can then be accessed from the given MCDM program as its input file.

Selecting the MCDM file format ...

![](images/4916e4f919567f70d991d1a8b1c8c5e4ac91ed26422c35ed2122673853854cd2.jpg)  
Figure 9. Menu with the MCDM file formats.

## 6. Summary and conclusion

Two perspectives on developing better decision support capabilities of GIS have been identified in this paper: one based on analytical problem solving as a central function of a Spatial Decision Support System (SDSS) and another based on the integration of GIS and other specialized software. Both perspectives share a common goal of providing better procedures for spatial decision-making support. Within this framework, multiple criteria decision-making (MCDM) techniques offer ample potential as spatial decision support tools. The purpose of using MCDM is to assist the decision maker in selecting the best alternative from the number of feasible choice-alternatives under the presence of multiple choice criteria and diverse criterion priorities.

Every MCDM technique shares a common approach called a general model of MCDM. According to this model the decision-making problem is structured into the set of alternative and the set of criteria. The performance of each alternative on every criterion is represented in the two-dimensional decision table by evaluation scores. These scores combined with the decision maker's preferences are processed by aggregation functions that return a solution in the form of either one recommended alternative, or a reduced decision space consisting of several good alternatives, or a ranking of alternatives from best to worst. The general model of MCDM parallels the procedurally rational model of decision making. The four steps of the procedurally rational model: problem definition, search for alternatives and selection criteria, evaluation of alternatives, and selecting an alternative, correspond to the following steps in the general model of MCDM: deriving the set of alternatives and the set of criteria, formulating the decision table, aggregating the data in the decision table and performing sensitivity analysis, and making the final recommendation.

The role of GIS in implementing the procedurally-rational model of decision making in land use allocation, site, and route selection problems is foremost the search for suitable alternatives, but also helping the decision makers to assign priority weights to decision criteria, evaluate the suitable alternatives, and visualize the results of choice. The search often results in the selection of a number of alternatives that satisfy the minimum threshold values. Further reduction of the set of admissible alternatives and the selection of the best alternative often requires the use of MCDM techniques. Hence, the improvement of GIS decision support capabilities can be achieved by introducing the multiple criteria decision-making techniques into the GIS context.

The MCDM can be classified according the level of cognitive processing required from the DM into compensatory and noncompensatory techniques, and according to the method of aggregating criterion scores and the DM's priorities into additive, based on the ideal point approach, pairwise comparison, and sequential elimination techniques.

The multiple criteria evaluation in raster GIS involves evaluating a large number of individual cells. This makes the integration of some computationally more intensive MCDM techniques with raster GIS impractical. In vector-based GIS the multiple criteria evaluation results in a relatively small number of suitable alternatives, in comparison to a number of raster cells. This makes feasible integrating a number of different MCDM techniques, besides the weighted summation technique, with vector-based GIS.

A few of the MCDM techniques can be implemented directly in GIS using the operators of the database query language. Others, however, can be implemented more efficiently using external programs and integrating these programs with GIS. Two strategies for integrating GIS and MCDM are proposed. The first strategy called here the loose coupling strategy suggests linking GIS and MCDM techniques using a file exchange mechanism. The second strategy called the tight coupling strategy suggests linking GIS and MCDM techniques using a shared database.

The framework presented in this paper provides guidelines for implementing the loose coupling of a vector-based GIS and MCDM. The implementation of the tight coupling strategy requires further work. More research is also needed on the topics of sensitivity analysis in an integrated GIS—MCDM system and facilitating group decision making in the GIS—MCDM context.

## Acknowledgments

The author would like to thank two anonymous reviewers for their thoughtful comments and suggestions in preparing the final version of the paper.

## References

BERRY, J. K., 1992, GIS resolves land use conflicts: A case study. 1993 International GIS Sourcebook (Fort Collins, CO: GIS World), pp. 248–253.

BIRKIN, M., CLARKE, G., and WILSON, A., 1990, Elements of a model-based GIS for the evaluation of urban policy. In Geographic Information Systems: Developments and Applications, edited by L. Worrall (London: Belhaven Press), pp. 133–162.

BOUYSSOU, D., 1991, Modelling inaccurate determination, uncertainty, imprecision using multiple criteria. In Multiple criteria decision support. Proceedings of the International Workshop held in Helsinki, Finland, 7–11 August 1989, edited by P. Korhonen, A. Lewandowski and J. Wallenius (Berlin: Springer-Verlag), pp. 78–87.

BROWN, C. A., STINSON, D. P., and GRANT, R. W., 1986. Multi-attribute tradeoff system: Personal computer version user's manual. (Denver: Public and Social Evaluation Office, Division of Planning Technical Services, Engineering Research Center, Bureau of Reclamation).

BURROUGH, P. A., VAN DEURSEN, W., and HEUVELINK, G., 1988, Linking spatial process models and GIS: a marriage of convenience of a blossoming partnership? In Proceedings, GIS/LIS '88, vol. 2, San Antonio, TX (Bethesda, MD: American Congress on Surveying and Mapping), pp. 598–607.

CARVER, S. J., 1991, Integrating multi-criteria evaluation with geographical information systems. International Journal of Geographical Information Systems, 5, 321–339.

COHON, J. L., 1978, Multiobjective programming and planning. (New York: Academic Press).

COLSON, G., and DE BRUYN, C., 1989, Models and methods in multiple objectives decision making. Mathematical and Computer Modelling, 12, 1201–1211.

COWEN, D., 1988, GIS versus CAD versus DBMS: what are the differences? Photogrammetric Engineering and Remote Sensing, 54, 1551–1555.

DANGERMOND, J., 1987, The maturing of GIS and a new age for geographic information modelling systems (GIMS), In Proceedings, International Geographic Information Systems Symposium: The Research Agenda, vol. 2 (Arlington, VA: NASA), pp. 55–66.

DENSHAM, P. J., and GOODCHILD, M. F., 1989, Spatial decision support systems: a research agenda. In Proceedings, GIS/LIS '89, Orlando, FL, vol. 2 (Bethesda, MD: American Congress on Surveying and Mapping), pp. 707–716.

DENSHAM, P. J., and RUSHTON, G. R., 1988, Decision support systems for locational planning. In Behavioral Modeling in Geography and Planning, edited by R. G. Colledge, and H. J. P. Timmermans (New York: Croom Helm), pp. 56–90.

EASTMAN, J. R., KYEM, P. A. K., and TOLEDANO, J., 1993, A procedure for multi-objective decision making in GIS under conditions of competing objectives. Proceedings, EGIS '93, pp. 438–447.

ENCYCLOPEDIA BRITANNICA, 1974, vol. 15 (University of Chicago), p. 527.

FEDRA, K., 1993, Environmental modeling and GIS. In Environmental Modeling with GIS, edited by M. Goodchild, B. Parks and L. Steyaert (Oxford: University Press), pp. 35–50.

GOODCHILD, M. F., 1987, A spatial analytical perspective on geographical information systems. International Journal of Geographical Information Systems, 1, 327–334.

GOODCHILD, M. F., 1989, Geographic information systems and market research. In Papers and Proceedings of Applied Geography Conferences, 12, 1–8.

HARRIS, T. M., 1992, Balancing economic and energy development with environmental cost: a GIS approach. Presented at the Association of American Geographers 88th Annual Meeting, 18–22 April, 1992, San Diego, CA. Copy of the abstract available from the Association of American Geographers.

HARRIS, B., and BATTY, M., 1991, Locational models, geographic information and planning support systems. Paper presented at the 38th North American Meeting of the Regional Science Association, 7–10 November, New Orleans, LA. Copy of the abstract available from the Regional Science Association.

HONG, I. B., and VOGEL, D. R., 1991, Data and model management in a generalized MCDM-DSS. Decision Science, 22, 1–25.

HWANG, C. L., and LIN, M. J., 1987, Group decision making under multiple criteria (Berlin, Germany: Springer-Verlag).

HWANG, C. L., and YOON, K., 1981, Multiple attribute decision making methods and applications: A state of the art survey (Berlin: Springer-Verlag).

HWANG, C. L., and MASUD, A. S. M., 1979, Multiple objective decision making methods and applications: a state of the art survey (Berlin: Springer-Verlag).

JANOWSKI, P., 1989, Mixed data multicriteria evaluation for regional planning: A systematic approach to the decisionmaking process. Environment and Planning A, 21, 349–362.

JANKOWSKI, P., and RICHARD, L., 1994, Integration of GIS-based suitability analysis and multicriteria evaluation in a spatial decision support system for route selection. Environment and Planning B, 21, 323–340.

JANSSEN., R., and VAN HERWIJNEN, M., 1991, Graphical decision support applied to decisions changing the use of agricultural land. In Multiple criteria decision support. Proceedings of the International Workshop held in Helsinki, Finland, 7–11 August, 1989, edited by P. Korhonen, A. Lewandowski and J. Wallenius (Berlin: Springer-Verlag), pp. 293–302.

JANSSEN, R., and RIETVELD, P., 1990, Multicriteria analysis and GIS: an application to agricultural land use in The Netherlands. In Geographical Information Systems and Regional Planning, edited by H. J. Scholten and J. C. Stilwell (Dordrecht: Kluwer).

LOTFI, V., STEWART, T. J., and ZIONTS, S., 1992, An aspiration-level interactive model for multiple criteria decision making. Computer Operations Research, 19, 671–681.

LOTFI, V., and TEICH, J. E., 1991, Multicriteria decision making using personal computers. In Multiple criteria decision support. Proceedings of the International Workshop held in Helsinki, Finland, 7–11 August, 1989, edited by P. Korhonen, A. Lewandowski and J. Wallenius (Berlin: Springer-Verlag), pp. 152–158.

MAIDMENT, D., 1993, GIS and hydrological modeling. In Environmental Modeling within GIS, edited by M. Goodchild, B. Parks and L. Steyaert (Oxford: University Press), pp. 147–167.

MASSAM, B. H., 1980, Spatial Search (Oxford: Pergamon Press).

MCHARG, I. L., 1969, Design with nature (Garden City, NJ: John Wiley & Sons).

McKenna, C. K., 1980, Quantitative methods for public decision making (New York: McGraw-Hill).

MINCH, R. P., and SANDERS, G. L., 1986, Computerized information systems supporting multicriteria decision making. Decision Sciences, 17, 395–413.

NAGEL, S. S., and LONG, J., 1989, Evaluation analysis with microcomputers (Greenwich, CN: Jai Press).

NIJKAMP, P., RIETVELD, P., and VOOGD, H., 1990, Multicriteria Evaluation (Amsterdam: North Holland).

NUKAMP, P., and VAN DELFT, A., 1977, Multi-criteria analysis and regional decision-making. Studies in Applied Regional Science, 8 (Amsterdam: Leiden).

NYERGES, T. L., 1993, Understanding the scope of GIS: its relationship to environmental modeling. In Environmental Modeling within GIS, edited by M. Goodchild, B. Parks and L. Steyaert (Oxford: University Press), pp. 75–93.

OZERNOY, V. M., 1992, Choosing the 'best' multiple criteria decision-making method. Information Systems and Operational Research, 30, 159–171.

RADCLIFF, B., 1986, Multi-criteria decision making: a survey of software. Social Science Microcomputer Review, 4, 38–55.

RICHARD, L., 1992, Integration of geographic information system analysis and multicriteria evaluation in a spatial decision support system for a pipeline route selection study in King County, Washington. MSc. Thesis (Moscow: Department of Geography, University of Idaho).

SAATY, T. L., 1990, Multicriteria Decision Making: The Analytic Hierarchy Process, (Pittsburgh: Expert Choice, Inc.).

SAATY, T. L., 1980, The analytic hierarchy process: planning, priority setting, resource allocation (New York: McGraw-Hill).

SEATTLE WATER DEPARTMENT (SWD), 1988, Tolt Eastside Supply No. 2 (TESSL) No. 2, Phase III Draft Route Selection Study (Seattle, WA: Seattle Water Department).

SIMON, H., 1979, Rational decision making in business organizations. American Economic Revue, 69, 493–513.

SIMON, H., 1978, Rationality as process and as product of thought. American Economic Revue, 68, 1–16.

SIMON, H., 1957, Models of economic man (New York: John Wiley & Sons).

TEGHEM, J., DELHAYE, C., and KUNSCH, P. L., 1989, An interactive decision support system (IDSS) for multicriteria decision aid. Mathematical and Computer Modelling, 12, 1311–1320.

TOMLINSON, R. F., 1988, The impact of the transition from analogue to digital cartographic representation. The American Cartographer, 15, 249–261.

Voogd, H., 1983, Multicriteria evaluation for urban and regional planning (London: Pion).

WRIGHT, P., and BARBOUR, F., 1977, Phased decision strategies; sequels to an initial screening. TIMS Studies in the Management Science, 6, 91–109.