## Determination of Interaction Between Criteria and the Criteria Priorities in Laptop Selection Problem

<!-- image -->

Fatma So ¨nmez C ¸ ak ı r 1 · Mehmet Pekkaya 2

Received: 6 February 2020 / Revised: 19 March 2020 / Accepted: 6 April 2020 / Published online: 2 May 2020 Ó Taiwan Fuzzy Systems Association 2020

Abstract The statistic of global laptop shipment showed that 161.6 million laptops were sold, 65.23% more than desktop-PCs, and almost the same quantity as tablets in 2017. So, laptop demand is quite high and needs to be researched on what kind of criteria (properties) are crucial. Since there are more than one criteria, this study focuses on multi-criteria decision-making (MCDM) methods in selecting laptops. This study aims to determine the interaction between criteria, and the criteria priorities in laptop selection problem that can be added/changing new features every day and to present the findings/results to the researcher/decision-makers. DEMATEL method is used for determining the interactions which are not observed in laptop literature, and fuzzy AHP is for criteria priorities. The price and brand image of a laptop have more interrelated action than the other main criteria. According to results, the brand image is determined as the most important criteria. Along with the brand image, other/peripheral properties and price criteria have totally two-thirds priority among six main criteria. The brand image along with the price had a dominant effect on other criteria according to the interaction matrices/diagrams. This study also shows that criteria priority results should be considered along with interaction matrices/diagrams that may produce such following information: speed, storage, monitor and other/peripheral properties criteria have overall effecting feature but not strongly, while brand image is a transition criterion along with having the highest priority, and the price criterion is obviously being affected by all criteria.

&amp; Mehmet Pekkaya mehmet.pekkaya@beun.edu.tr

1 Management Information Systems, Bart ı n University, Ag ˘dac ı , Bart ı n, Turkey

2 Business Administration, Z. Bu ¨lent, Ecevit University (ZBEU), I ˙ ncivez, Zonguldak, Turkey

Keywords MCDM  AHP  Fuzzy AHP  DEMATEL  Laptop selection

## 1 Introduction

Due to technological developments, computer usage is becoming more common every year. At the same time, there are continuous improvements in computer models and features produced every year.

Computers can be examined under three main titles: desktop-PC, laptops, and tablets. Figure 1 shows net computer sales from 2010 to 2017 and estimated sales volumes from 2018 to 2023. Figure 1 shows that desktop and PC sales have been declining, but laptop and tablet sales have declined for a short time, laptop sales have increased again. Considering that the life expectancy of a computer is 5 years, it can be seen how widespread computer sales are. New properties are added to a product that is in such high demand in the market every year and this situation forces the decision-makers. The difficulty of this selection process stems from the existence of alternative brands, models and integrated features.

The main motivation of the study is to contribute to the solution of the problem of laptop selection in individual or institutional terms within the laptop demand, which maintains its importance throughout the world. In this study, it is desired to determine the effective criteria for the laptop selection problem and to evaluate the criteria. Thus, by determining the priorities of these criteria with an analytical approach and revealing the interaction between the criteria, we have conducted these analyses to try to give information on the selection problem. There are three main research gaps in the related literature. Firstly, AHP/ANP methods are commonly used in determining criteria priority, but no research using DEMATEL is observed to determine interactions between criteria in related literature. Secondly, in the related studies reviewed, it is observed that the main/sub-criteria expressions/concepts considered are not in accordance. Thirdly, it is observed that there is no compliance in the criteria priorities obtained as a result of the analyses in the related literature. Accordingly, the aim of this study is focused on determining interactions and analyzing these two fuzzy environments related to the concepts and priorities.

<!-- image -->

<!-- image -->

Fig. 1 Shipment (2010-2017) and forecast (2018-2023) of laptops, desktop-PCs and tablets worldwide (in million units); (www.statista. com; 04.11.2019)

<!-- image -->

As it is known, people make many decisions for themselves, their families or professions in their daily lives. These decisions can sometimes be about whether or not to select an option, or as a decision among multiple options. Decision-making and analysis of decisions are as old as human history and new ones are added every day [1]. The choice of options or alternatives for decision-making makes it difficult to decide. Previously, individuals used their own knowledge to make decisions with different characteristics and many alternative options. Due to advancing technology, increasing business relationships, and the surplus of similar products, these decisions have become difficult. Models have been developed to make decisions among alternatives. These models are differentiated by different approaches and analysis algorithms. In this selection process, which has different alternatives and different models, there may be difficulty in making decisions and there are several methods developed to overcome this difficulty.

The steps in decision-making using alternatives can be listed as follows [1]:

- (i) Determination of relevant criteria and alternatives;
- (ii) Quantitative measurements on the relative importance of the criteria and the impact of alternatives on these criteria;
- (iii) It is the selection/sorting and/or grouping of alternatives as a result of calculating the index score or relative position for each alternative.

<!-- image -->

In particular, this study was conducted by (i) and (ii) concentrated on the steps.

Multi-criteria decision-making (MCDM) techniques are widely used because of their ability to solve multidimensional information problems, is a well-known issue of decision-making, and MCDM is a modeling tool used to deal with complex engineering problems [2]. When the literature is examined, many studies with different MCDM techniques can be found. Although there are many MCDMs, each has different and distinctive characteristics [3].

Since there are many criteria in laptop selection problem and the fuzzy environment in views of experts' criteria priorities as mentioned in paragraph of motivation/research gaps, we used MCDM methods which have some advantages for solving such problems. These advantages can be summarized as follows: (1) multi-criteria/variable can be used; (2) MCDM methods may have more sensitivity in the measurement of taking views of experts, for example as the Likert scale has 3, 5, 7 or 9 points, AHP scale has a doublesided 9-point scale and also contains consistency measurement; (3) alternative statistical methods for conducting such analysis, need so many assumptions and so need bigger sample volume. Although obtaining several experts' views are enough in MCDM, some alternative statistical methods (covariance based/partial least squares structural equation modeling, instead of DEMATEL) may need at least more than 100 sample volume of experts.

The name, developer(s) and development year of some of these methods are given in Table 1. PROMETHEE allows preference functions to be used in the comparison of alternatives according to the criteria; MACBETH provides a different and easier-to-understand view of the comparison of decision criteria; COPRAS treats the criteria as useful or useless without using a comparison matrix; ANP decides with the idea of the interaction of these components in a decision environment consisting of criteria and alternatives; VIKOR can be used for selection and ranking problems as well as for evaluation of decision performances where there are conflicting criteria (max-min); MOORA, the calculation time is very short according to some methods is simple to understand and apply. In essence, AHP, DEMATEL, Entropy, CRITIC can be used for determining the priority of the criteria in MCDM problems; DEMATEL can be used for determining the inter-criteria interaction, and alongside AHP other MCDM

Table 1 Some multiple criteria decision-making models

| Method                                                                        | Study   |
|-------------------------------------------------------------------------------|---------|
| DEMATEL, Decision-Making Trial and Evaluation Laboratory Method               | [4]     |
| AHP, Analytic Hierarchy Process                                               | [5]     |
| TOPSIS, Technique for Order Preference by Similarity to Ideal Solution        | [6]     |
| GRA, Grey Relational Analysis                                                 | [7]     |
| PROMETHEE, Preference Ranking Organization Method for Enrichment Evaluation   | [8]     |
| MACBETH, Measuring Attractiveness by a Categorical Based Evaluation Technique | [9]     |
| COPRAS, Complex Proportional Assessment                                       | [10]    |
| ANP, Analytic Network Process                                                 | [11]    |
| VIKOR, Vise Kriterijumska Optimizacija I Kompromisno Resenje                  | [12]    |
| MOORA, Multi-Objective Optimization on basis of Ratio Analysis                | [13]    |
| ARAS, Additive Ratio Assessment                                               | [14]    |
| MOOSRA, Multi-Objective Optimization On The Basis Of Simple Ratio Analysis    | [15]    |
| ENTROPI                                                                       | [16]    |
| F-AHP, Fuzzy AHP                                                              | [17]    |
| CRITIC, CRiteria Importance Through Inter-criteria Correlation                | [18]    |

methods in Table 1 can be used for selection, sorting or grouping alternatives

The study aims to determine the criteria priorities in laptop selection, the impact levels of criteria with using a diagram of these criteria via MCDM methods and present the findings to the decision-makers/researchers. Another aim of this study is to show that the interaction between the criteria taken into consideration in the laptop selection process can be modeled by DEMATEL approach. In academic studies on laptop selection, it is seen that AHP method is the most preferred among the MCDM methods in determining criteria priorities, and ANN, CRITIC methods are also commonly used.

In the laptop/computer selection problem, DEMATEL or Fuzzy AHP-DEMATEL model application is not encountered in related literature, for such evaluations of criteria used in the present study in the selection of computers. With this aspect, it can be said that the study findings and approach will contribute especially with DEMATEL modeling.

Within the scope of the aim of the study, a literature study was conducted and the criteria that could affect the selection of the laptop were listed especially based on the study of Pekkaya and Aktogan [19]. Subsequently, the main/sub-criteria to be used in the analyses were clarified by considering the opinions of the related academicians. It was ensured that these criteria were graded with paircomparisons by expert views. AHP and fuzzy AHP methods were used for determining the criteria priorities and DEMATEL method was used to determine the interactions of each criteria with the other criteria.

The highlights of the study can be expressed for especially laptop selection problem as based on the views of 23 experts: (1) by applying two separate scenarios, in order to determine the importance levels of each criterion influencing/being influenced by other criteria, the net effects of the criterion, and the total interactions; (2) to show drawing and presenting the diagrams for inter-criteria interaction model, thus showing that the inter-criteria interaction model can be revealed in a more understandable/descriptive way; (3) determining the 6 main criteria priorities via fuzzy AHP and 20 sub-criteria; (4) the views obtained from 23 computer experts were figured out by using fuzzy logic approach and then obtained the group judgments which are used in AHP-DEMATEL calculations as data.

The remaining part of this paper is structured as follows: in Sect. 2 of the study, a literature review of academic studies in the field is reported. In the third section, DEMATEL method, in the fourth section AHP, in the fifth section fuzzy AHP methods are explained. The sixth section is where criterion significance ratings and analysis of interactions with the criterion are reported. In the last section findings are evaluated by comparing them with the related literature.

## 2 Literature Summary on Computer Selection

The AHP and DEMATEL methods have been used alone or in combination with other models in the solution of many decision problems since the years of participating in the literature. Table 2 presents some models used for computer selection and some work done by leaning or hybridizing with DEMATEL and AHP.

In Table 2, some examples of MCDM methods usage in computer selection in the literature and the main criteria used in these methods are presented.

Table 2 MCDM methods usage in computer selection problem

| Method                     | Main criteria and research                                                                                                 |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|
| AHP; PC                    | Memory Capacity, Graphics Capacity, Size, Weight, and Price, [20]                                                          |
| AHP; PC                    | Concurrent Capacity, Execution Speed, Maximum I/O Configuration, [24]                                                      |
| DEA; PC                    | Memory, Processor, Hdd, display card, [25]                                                                                 |
| ANN; PC                    | Speed, RAM, Display, Price, [26]                                                                                           |
| ELECTRE & F-AHP; PC        | Speed, Graphics Card, System Memory, Hdd, Battery Life, Weight, Brand, Price, [27]                                         |
| AHP, DEA, TOPSIS, VIKOR; L | Speed, Brand, Capacity, Screen, External hardware, Price, [19]                                                             |
| TOPSIS; L                  | Warranty, size, battery life, specification, and others, [28]                                                              |
| MULTI MOORA and MOOSRA; L  | Speed, cache memory, storage, display card memory, memory, screen resolution/size, brand reliability weight and cost, [29] |
| CRITIC and EVAMIX; L       | Service, Brand Reliability, Design, CPU Speed, Cache, Graphics Card Size, RAM, Screen Resolution, Hdd, Weight, Price [30]  |
| FAHP, TOPSIS               | Hdd and RAM capacity, speed, Screen, Brand, Warranty, Weight, and Price [21]                                               |
| PIPRECIA, EDAS             | Hdd, screen, Processor type/tact, Cache memory, RAM, Graphics, Weight, Battery, Price [22]                                 |
| ANP                        | Hdd, Processor, Graphics and design, Warranty, portability, Battery [23]                                                   |

L laptop, PC personnel computer, Hdd hard disk

It can be seen in Table 2 that there are different categories for Price, Speed categories, Storage/Memory/Memory categories, Brand categories, Size and Other features in the selection of Laptop or Personnel Computer. Main and sub-criteria are created with the information obtained. The most important criteria are determined as memory (0.430) [20], processing speed (0.2742) [19], brand and warranty (0.22) [21], Hdd/Ram/cache memory (0.28) [22], speed (0.22) [23]. The determined most important criteria show that memory, speed, brand image must be taken into consideration. AHP/ANP methods are commonly used in criteria priority calculations, but no research using DEMATEL has been encountered to determine interactions between criteria in related literature.

In the application part of the study, while the main and sub-criteria are formed, expert opinions are taken for the whole criterion in the table. The main criteria and subcriteria, which are found to be the most important, have been applied. This process allows the study to perform repeated checks.

## 3 DEMATEL Method

The DEMATEL is a method by Battelle Memorial Institute developed to solve problems related to technological development and human activity, enabling to analyze and simplify the relationship between complex management problems or criteria [4, 31]. The DEMATEL method can also examine the problems and complex relationships between each part of a community [32]. DEMATEL can place criteria in order of priority according to the effects of the relations according to type and other criteria [33]. In the method, the criteria that have a higher impact on other criteria and are assumed to have high priority are called cause criteria, whereas those that are influenced and assumed to have low priority are called outcome criteria. Along with determining the priorities, Paksoy [39] declares the output of DEMATEL as follows:

<!-- image -->

- Identification of criteria clusters that affect other criteria for all criteria,
- Determination of cause criteria that most affect other criteria,
- Determination of the most affected result criteria from the other criteria,
- Identification of the relationship between each of the criteria,
- Determination of the influence power of cause-effect relations between criteria. The operation of the method is carried out in the following five steps [34-39].

Step 1: Obtaining a matrix, which shows the relation of criteria to each other.

The DEMATEL pair-comparison scale to be used in this step is given in Table 3.

With the use of this measurement scale, the goal is to reveal the causality relationship between each criterion. Brainstorm, expert opinion and literature search, etc., methods and criteria can be compared.

Table 3 Point values of paircomparisons for DEMATEL

|   Value | Meaning                                                                                       |
|---------|-----------------------------------------------------------------------------------------------|
|       0 | Ineffective: used when a criterion is compared with itself                                    |
|       1 | Low impact: the criterion is a low impact on the other criterion compared                     |
|       2 | Medium impact: the criterion is moderate on the other criterion to which it is compared       |
|       3 | High impact: the criterion is highly effective on the other criterion to which it is compared |
|       4 | Very high impact: the criterion is very high on the other criterion to which it is compared   |

Table 4 DEMATEL calculation process (from step 2 onwards)

| Step   | Calculation                                                                           | Explanation                                                                                                                                                                                                                                                                                                                                                                                      |
|--------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S2     | k ¼ 1 Max 1  i  n P n j ¼ 1 x ij N ¼ k  A                                                                                       | All direct relation matrix elements are multiplied by the k value created using the maximum values of the rows and columns. The creation of the k value and the normalized matrix is done in this step                                                                                                                                                                                           |
| S3     | T ¼ lim k !1 ð N þþ N k Þ T ¼ N ð 1   N Þ   1 P                                                                                       | The normalized N matrix is multiplied by the inverse of the unit matrix normalized matrix                                                                                                                                                                                                                                                                                                        |
| S4     | D i ¼ n j ¼ 1 t ij i ¼ 1 ; 2 ; . . . ; n R i ¼ P n j ¼ 1 t ij ; j ¼ 1 ; 2 ; . . . ; n | After obtaining the full interactions matrix ( T ), it is necessary to calculate the effect of a criterion on the other criteria, and the extent to which it is influenced by other features. D i in equations, the sum of the T matrix line, which indicates the direct effect of a factor on other factors, R i : column sums that indicate the degree to which a factor is affected by others |

- S5 A threshold value is set by the decision-maker for the effect grades that are thought to be meaningless or to be ignored. An effect matrix is created by writing ''0'' instead of the influence grades that are less than the specified equal value. All the causal results can be seen by drawing the graph of this arranged T

2

3

<!-- formula-not-decoded -->

The values on the diagonal values of the matrix are 0 because they are ''ineffective'' if the criteria are compared with each other. Other process steps are summarized in Table 4.

The main advantage of the DEMATEL method is including indirect relationships with a conciliatory cause and effect model [38]. The threshold value is determined by the decision-makers or experts. The effect direction graph diagram is obtained by showing the points in a coordinate plane (D ? R, D -R) with the horizontal axis D ? R and the vertical axis D -R [34].

## 4 Analytic Hierarchy Process (AHP) Method

AHP is a method developed by Saaty in 1980 for solving problems with a large number of criteria and alternatives, which are used to determine the criteria priorities or to conduct selecting/sorting of alternatives using pair-comparisons. AHP can be considered as the most widely used MCDM method for solving MCDM problems in almost every aspect of life decision-making for especially determining priorities of the existing criteria in such a process.

The usage of tolerated consistent AHP and fuzzy AHP methodology is one of the highlights of this study.

AHP allows determining the priorities of the criteria over the pair-comparison matrix of experts' views and is advantageous in comparison to the other MCDM methods in terms of calculating a single number of cross-consistencies of all pair-comparisons used in determining calculations of the criteria priorities. One-side scale values of two-way pair-comparisons in AHP are listed in Table 5.

AHP has been widely used in recent years to determine the criteria priorities with pair-comparisons, especially generating criteria priorities for selecting/sorting of proper alternatives in MCDM calculations. The AHP calculation process is an eigenvalue approach to the pair-wise comparisons [40] and its calculation stages are summarized in Table 6. This calculation can be thought as getting the weight vector W by solving '' B * W = k max* W ' ', where k max is the largest eigenvector of B matrix. As it is seen at the table, in addition to determining the criteria priorities in the problem over the pair-comparison matrix at steps 1-3, the cross-consistency confirmed pair-comparisons represented as a single number (CR, at stages 4-5) is evaluated as the advantageous face of AHP. The most important advantage of the AHP method over the other methods is the paircomparison matrices which are made to determine the relative importance of the criteria at the same level in the hierarchical structure.

<!-- image -->

Table 5 Scale values of pair-comparisons in AHP Source: Hamzacebi and Pekkaya [40]

| Value      | Category     | Explanation                                                                        |
|------------|--------------|------------------------------------------------------------------------------------|
| 1          | Equal        | Two activities contribute to the objective equally                                 |
| 3          | Moderate     | Experience and judgment slightly favor one activity over another                   |
| 5          | Strong       | Experience and judgment strongly favor one activity over another                   |
| 7          | Very strong  | An activity is favored very strongly over another                                  |
| 9          | Extreme      | Favoring one activity over another is of the highest possible order of affirmation |
| 2, 4, 6, 8 | Intermediate | Intermediate values of neighbor values                                             |

Table 6 The stages of AHP calculations for criteria priorities Source: Pekkaya and Aktogan [19]

| Step   | Calculation/explanation                                                                                                             | Calculation/explanation                                                                                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S1     | B = [ b ij ] matrix is constructed by getting the pair-compared (consisting of 1/9, 1/8, … , 8, 9 values of 17 scales) expert views | B = [ b ij ] matrix is constructed by getting the pair-compared (consisting of 1/9, 1/8, … , 8, 9 values of 17 scales) expert views                                                                           |
| S2     | c ij ¼ b ij P n i ¼ 1 b ij P                                                                                                        | By normalizing B matrix with respect to its column total values, matrix [ c ij ] is obtained                                                                                                                  |
| S3     | w i ¼ n j ¼ 1 c ij n P                                                                                                              | The priority values ( W column matrix) for each criteria in the research are calculated by dividing the sum of the row values of the C matrix by the number of criteria ( n ). The sum of the priorities is 1 |
| S4     | k ¼ d i w i n D = B * W                                                                                                             | The column matrix of D is formed by matrix multiplication of B and W . The mean of the values of ' ' D matrix scores to their own priority'', k is calculated                                                 |
| S5     | CR ¼ k   n n   1 RI                                                                                                                   | The CR is the consistency ratio of the pair-comparisons in matrix B . RI is random index value as below n : 3 4 5 6 7 8                                                                                       |

8

<!-- formula-not-decoded -->

Function l lower, m mean and u upper shows the value. Two fuzzy numbers can be added and subtracted, multiplied and divided, and reversed [44]. Nine linguistic expressions are used in AHP as shown in Table 5. Triangular fuzzy number equivalents of these expressions are given in Table 7.

Table 8 shows the fuzzy AHP steps. Existing data will be made unfuzzy and processed by following these steps.

Table 7 Fuzzy triangle scale

| Value      | Definition             | Fuzzy triangle scale               |
|------------|------------------------|------------------------------------|
| 1          | Equal importance       | (1,1,1)                            |
| 3          | Moderate importance    | (2,3,4)                            |
| 5          | Strong importance      | (4,5,6)                            |
| 7          | Very strong importance | (6,7,8)                            |
| 9          | Extreme importance     | (9,9,9)                            |
| 2; 4; 6; 8 | Intermediate values    | (1,2,3); (3,4,5); (5,6,7); (8,8,9) |

## 5 Fuzzy Analytic Hierarchy Process Method

Fuzzy AHP (FAHP) is a modified basic of the AHP method. FAHP used in MCDM problems such as AHP and is a synthetic extension of the classical AHP method [41]. The main difference between AHP and FAHP can be declared as follows. FAHP uses fuzzy numbers or linguistic expressions for calculations instead of real numbers. These linguistic expressions are equally important, absolute important, etc. [42]. In obtaining fuzzy numbers, Zadeh [17] introduced the fuzzy clustering process and this triangular fuzzy process has been widely adopted due to its simplicity in the calculation and its advantages such as the ability to produce solutions to fuzzy data [43]. Pair-comparisons are made using fuzzy numbers and it can be thought that linguistic expressions can be better represented. Fuzzy sets are real numbers drawn in the range 0 to 1.

The membership function is defined as follows with the fuzzy number N ^ ve and the triangular fuzzy number TFN [44]:

<!-- image -->

Table 8 The fuzzy AHP calculation stages for criteria priorities

| Step   | Calculation Explanation                                                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| S1     | ~ d k 11 ~ d k 12    ~ d k 1 n Pair-comparison matrices are created                                                                                                                                                       |
| S2     | ~ d ij ¼ n k ¼ 1 ~ d k ij K If there is more than one decision-maker, the average of the values taken from each decision-maker is calculated 2 3      |
| S3     | ~ d 11 ~ d 12    ~ d 1 n Matrix elements are updated based on average values                                                                                                                                                       |
| S4     | ~ r i ¼ n j ¼ 1 ~ d ij 1 = n i ¼ 1 ; 2 ; . . . ; n The geometric mean method is used to define the fuzzy geometric mean and weights of each criterion |
| S5     | ~ w i ¼ ~ r i ð ~ r i  ~ r n Þ   1 The fuzzy weights of the criteria are defined                                                                                                                                                       |
| S6     | M i ¼ ð ~ w 1  ~ w n Þ = n Calculate the average and normalized weight criteria                                                                                                                                                       |

The table is adapted from Chou et al. [42]. Many fuzzy AHP applications can be seen in the literature. The method has been used effectively in decision-making problems in many areas. Various methods have been presented by various researchers to determine the best option or to sort the options in a multi-criteria environment by using fuzzy sets theory and hierarchical structure [45]. In this study, Chou procedure is used for removing blurriness.

## 6 Determining the Interaction Between Criteria and the Criteria Priorities in Laptop Selection

The application purpose of this study is to determine the interaction/causal relationship between criteria via DEMATEL, and the criteria priorities via AHP in the laptop selection problem. In order to carry out these purposes, 23 experts' views were gathered using pair-comparisons of main criteria. Acquired values from 23 experts for so many criteria are not the same, then, in general, we take into account a fuzzy approach practically to get clear values from fuzzy views. In laptop selection problem, six main criteria and 21 sub-criteria are specified according to the study of Pekkaya and Aktogan [19] and then pre-survey to some academicians. Afterward, a questionnaire is constructed. The questionnaire consists of one-way 5 point (0-4) scaled 30 pair-comparisons of main criteria on effecting direction for DEMATEL calculations, and twoway 9 point scaled 15 pair-comparisons of main criteria for AHP calculations. Moreover, five-point scaled (1-least important to 5-extreme important) 20 sub-criteria questions exist in the questionnaire for priority calculations via reciprocal approach [46, 47].

The reciprocal approach is preferred for being less tired of the experts in the questionnaire process and more reliable measurement after 45 pair-comparisons conduction, since no pair-comparison which consists of only scaling importance. This method has a simple calculation formula with ' ' wi = (1/ r i )/(Sum(1/ r i ))' '. 20 sub-criteria questions exist since one of the main criteria (M1-price of the product) has no sub-criteria. Along with their bold abbreviations, all the main/sub-criteria of the study in laptop selection problems are listed in Table 9.

The questionnaire is applied to 23 experts who are computer software programmers or engineers. The experts who are willing and available, have selected via the convenience sampling method. They have knowledge/experience on computer features, and some are related to purchase/sale, as eight of the experts are academicians, the rest of them are working in this industry. Most of them are male (65.2%, 15 people), have more than 5 years of experience (73.9%), and work in private industry (65.2%).

The DEMATEL literature is becoming vast and growing and has received a great deal of attention in the past decade and many researchers have applied it for solving different complicated system problems in various areas due to its advantages/capabilities, even in many real-world systems that include imprecise and uncertain information. The DEMATEL technique produces an interaction table that allows observing causal relationships, effects, net effects, and total interactions separately in even ranking form for criteria/factors. And also the DEMATEL technique converts the interrelations between criteria/factors into an intelligible systematic structural model which allows an impact relation (interactions) diagram, both of these opportunities are usable for long-term strategic decisionmaking and indicating improvement scopes [48]. Accordingly, the DEMATEL technique is used for determining the intelligible systematic structural model for main criteria/factors in the laptop selection problem.

<!-- image -->

| Table 9 The main and sub- criteria names in laptop   | Main criteria                              | Sub-criteria                                           |
|------------------------------------------------------|--------------------------------------------|--------------------------------------------------------|
| selection                                            | M1-Price of the product                    | S1-Price                                               |
|                                                      | M2-Running speed                           | S2-Proc-speed                                          |
|                                                      |                                            | S3-RAM-speed                                           |
|                                                      |                                            | S4-Card-speed                                          |
|                                                      | M3-Storage capacity                        | S5-RAM-capacity                                        |
|                                                      |                                            | S6-HDD/SDD-capacity                                    |
|                                                      |                                            | S7-Graphics card-memory                                |
|                                                      |                                            | S8-Proc-cache                                          |
|                                                      | M4-Monitor properties                      | S9-Resolution                                          |
|                                                      |                                            | S10-Size                                               |
|                                                      |                                            | S11-Touch screen                                       |
|                                                      |                                            | S12-Other (usage advantages)                           |
|                                                      | M5-Other properties and laptop peripherals | S13-Ports (USB, HDMI, etc.)                            |
|                                                      |                                            | S14-Weight                                             |
|                                                      |                                            | S15-Battery properties                                 |
|                                                      |                                            | S16-Drivers (CD/DVD/Blu-ray)                           |
|                                                      | M6-Brand image                             | S17-Service quality                                    |
|                                                      |                                            | S18-Design (keyboard, ports, etc.)                     |
|                                                      |                                            | S19-Eco-friendly (radiation, energy consumption, etc.) |
|                                                      |                                            | S20-Hardware Quality                                   |
|                                                      |                                            | S21-Durability (impact, drop, etc.)                    |

The interaction between main criteria is determined via DEMATEL using 5-point scaled 30 pair-comparisons of the main criteria conducted in two main scenarios. Construction procedure of interaction matrix in terms of these two scenarios, totally four scenarios can be counted using two different approaches to threshold value [49]. The scenario properties are summarized in Table 10. For example, in the first DEMATEL scenario (DSen-1a), separately 23 interaction matrices are constructed according to 23 exert views, then the ultimate interaction matrix is calculated by taking the arithmetic mean of each interaction between criteria by using these 23 matrices. Accordingly, the magnitude of total effects, being totally affected, being net influencing/influenced, and transactions are calculated by using this ultimate interaction matrix. However, in the third DEMATEL scenario (DSen-2b), after taking mean values all pair-comparisons of 23 experts, only one interaction matrix is calculated by using these pair-comparison values.

Table 10 Interaction matrix formation scenarios via DEMATEL

| Scenario   | Construction of the interaction matrix                                                     | Threshold value                 |
|------------|--------------------------------------------------------------------------------------------|---------------------------------|
| DSen-1a    | Mean of separately constructed interaction matrices according to 23 views                  | 0.4160; maximum diagonal value  |
| DSen-1b    | Using the same matrix as DSen-1a                                                           | 0.3683; mean of all cell values |
| DSen-2a    | One interaction matrix is constructed using mean values of the pair-comparison of views 23 | 0.5894; maximum diagonal value  |
| DSen-2b    | Using same matrix as DSen-2a                                                               | 0.4868; mean of all cell values |

<!-- image -->

The constructed interaction matrix in terms of DSen-1a is reported in Table 11 and an impact relation diagram is drawn as in Fig. 2. The bold values in the matrix are significant effecting values according to the threshold approach of maximum diagonal value on the matrix which is 0.4160. The significant effecting values are represented in the diagrams shown in bold. According to Table 11 (for DSen-1a/b), M1 and M6 have totally highly effecting values to the other criteria (D values), M1 and M6 have totally highly been effected values from the other criteria (R values), and then these criteria are more interactive (or relationship) criteria than others (D ? R values). Relatively net effecting criteria are M2 and M3 with having positively highest D -R values, and relatively net being effected criteria are M1 and partly M6 with having negative highest D -R values.

Table 11 Interaction matrix and affecting/ed sums for Scenario 1a

|    |   M1 |   M2 |   M3 |   M4 |   M5 |   M6 |    D |    R |   D ? R | D - R   |
|----|------|------|------|------|------|------|------|------|---------|---------|
| M1 | .416 | .449 | .444 | .419 | .406 | .524 | 2.66 | 2.82 |    5.48 | - .18   |
| M2 | .494 | .268 | .345 | .328 | .300 | .448 | 2.18 | 2.10 |    4.29 | .08     |
| M3 | .479 | .352 | .237 | .302 | .267 | .415 | 2.05 | 1.96 |    4.01 | .09     |
| M4 | .444 | .315 | .284 | .217 | .261 | .415 | 1.94 | 1.94 |    3.88 | - .01   |
| M5 | .440 | .293 | .266 | .278 | .206 | .411 | 1.89 | 1.84 |    3.73 | .05     |
| M6 | .552 | .427 | .382 | .399 | .400 | .377 | 2.54 | 2.59 |    5.13 | - .05   |

Fig. 2 Interaction diagram for Scenario 1a via DEMATEL. The values of two directional arrows calculated by taking the mean of both values in that direction. The more interrelation level degrees are represented as darker drawings

<!-- image -->

These consequences can also be partly observed in Fig. 2, since only the significant impacts which are at a higher level than the threshold value are represented on the diagram. According to Fig. 2, the main criteria of M1-Price have interactions with each criteria, especially at a high level with M6-Brand, and then M2-Speed and M3-Storage. As the laptop ' 'Price' ' dominantly affects the criteria of ' 'Brand'', ' 'Speed'' and ''Storage'', also laptop ''Price'' is dominantly affected by the same three criteria. In terms of comparisons, since M1-Price's affecting values are clearly at a lower level then being effected values, in general, M1Price criteria can be named as being effected criteria which can be observed in Fig. 2.

Table 12 Interaction matrix and affecting/ed sums for Scenario 2a

Fig. 3 Interaction diagram for Scenario 2a via DEMATEL

<!-- image -->

Constructed interaction matrix in terms of DSen-2b is reported in Table 12 and the interaction diagram is given in Fig. 3. The threshold approach of maximum diagonal value

|    |   M1 |   M2 |   M3 |   M4 |   M5 |   M6 |    D |    R |   D ? R | D - R   |
|----|------|------|------|------|------|------|------|------|---------|---------|
| M1 | .589 | .578 | .566 | .542 | .527 | .716 | 3.52 | 3.77 |    7.29 | - .25   |
| M2 | .646 | .353 | .441 | .428 | .394 | .607 | 2.87 | 2.73 |    5.60 | .14     |
| M3 | .628 | .452 | .314 | .394 | .356 | .566 | 2.71 | 2.54 |    5.25 | .17     |
| M4 | .584 | .408 | .370 | .295 | .344 | .554 | 2.55 | 2.55 |    5.10 | .01     |
| M5 | .577 | .380 | .349 | .362 | .277 | .544 | 2.49 | 2.42 |    4.91 | .07     |
| M6 | .746 | .560 | .503 | .525 | .521 | .529 | 3.38 | 3.53 |    6.90 | - .13   |

Bold values indicate significant effecting values according to the threshold approach of maximum diagonal value on the matrix and represented in the related diagrams on the matrix is 0.5894. According to Table 12 (for DSen2a/b), M1 and M6 have totally highly affecting/being affected values to/from the other criteria, and then more interactive criteria than others. Relatively net effecting criteria are M2 and M3, and relatively net effected criteria are M1 and M6. Then all these relatively effecting/being affected results of these four DEMATEL scenarios produced mainly the same results. However, because of the differences in interaction values and basic threshold values, we obtained different interaction diagrams. Since DSen-1b and DSen-2b produced almost the same diagram, only DSen-2b diagram is reported along with diagrams of DSen1a/2a.

<!-- image -->

Fig. 4 Interaction diagram for Scenario 2b via DEMATEL

<!-- image -->

The main consequences of Figs. 2 and 3 are almost the same. Since the threshold value of Fig. 3 is higher than that of Fig. 2, comparatively fewer interactions are represented in Fig. 3. Mainly, the same results can be derived from Fig. 3 as from Fig. 2. Since interaction matrices of Figs. 3 and 4 are the same, consequences from Tables 12, 13 are the same as expected. Since the threshold value of Fig. 4 is lower than that of Fig. 3, comparatively more interactions are represented in Fig. 4.

Accordingly, Fig. 4 can be thought more complicated with having many more drawings that have significantly affecting values. Pekkaya and Aslan [49] also preferred the ' 'maximum diagonal threshold value approach'' because of the more simple, clear and significant drawings as in Figs. 2 and 3. However, preponderance observability of M1 and M6 criteria having more distinct interrelations in Fig. 3 can be stated as the advantage of Fig. 3. Diagram of Scenario 1b is not reported because of the almost the same complicated interaction drawing with Fig. 4 of Scenario 2b, then the Scenario 1b results of Fig. 4 expressed are almost the same for the Scenario 1b diagram. The main difference between Fig. 4 and Figs. 2, 3 can be stated as M6-Brand criteria has a cumulative inter-reaction with other criteria in order to foster the M1-Price criteria. From another perspective, M1-Price and M6-Brand have almost the same image according to interaction drawings among other criteria in terms of experts' views. This image is powered by having the highest double-side interaction value and almost the same positioning in the diagram with respect to D ? R and D -R values.

Table 13 Interaction matrix and affecting/ed sums for Scenario 2b

<!-- image -->

The main criteria priority calculations are conducted according to four AHP scenarios and two main DEMATEL scenarios. AHP scenarios are summarized in Table 14. In the calculation processes of AHP scenarios, most of the consistencies of experts' pair-comparisons are not proper according to Saaty's consistency boundary which is at CR = 0.1000, accepted as too rigid, and consistency tolerated Dodd et al.'s boundary which is at CR = 0.4113 for six criteria [24, 50, 51] is accepted. By accepting Dodd et al. approach, we can use much more experts' views in the priority calculations, less loss of information, that let us to have more representing the views of experts when limitations exist in applying re-survey for inconsistent ones. In AHP scenarios, two of the experts' views out of 23 experts were not taken into account, since their pair-comparison constancies were higher than the CR = 0.4113 boundary.

For scenario-AHPa, in terms of each exerts' pair-comparison views, separately AHP methodology is carried out, and the main criteria priorities are calculated by using views of each expert. Then, priority series are generated for six main criteria. The priorities are determined by

|    |   M1 |   M2 |   M3 |   M4 |   M5 |   M6 |    D |    R |   D ? R | D - R   |
|----|------|------|------|------|------|------|------|------|---------|---------|
| M1 | .589 | .578 | .566 | .542 | .527 | .716 | 3.52 | 3.77 |    7.29 | - .25   |
| M2 | .646 | .353 | .441 | .428 | .394 | .607 | 2.87 | 2.73 |    5.60 | .14     |
| M3 | .628 | .452 | .314 | .394 | .356 | .566 | 2.71 | 2.54 |    5.25 | .17     |
| M4 | .584 | .408 | .370 | .295 | .344 | .554 | 2.55 | 2.55 |    5.10 | .01     |
| M5 | .577 | .380 | .349 | .362 | .277 | .544 | 2.49 | 2.42 |    4.91 | .07     |
| M6 | .746 | .560 | .503 | .525 | .521 | .529 | 3.39 | 3.52 |    6.90 | - .13   |

Bold values indicate significant effecting values according to the threshold approach of maximum diagonal value on the matrix and represented in the related diagrams Generated priority series are tested whether it is equal to reference priority of [19], via one-sample t test (if normally distributed via SW, Shapiro-Wilk test) or W test (Wilcoxon signed rank test)

Table 14 Scenarios for main criteria priority calculations via AHP

| Scenario   | Sample                                | Explanation                                                              |
|------------|---------------------------------------|--------------------------------------------------------------------------|
| AHPa       | 21                                    | Arithmetic means are calculated using the generated priority series      |
| AHPw       | 5 ? 2*16; 16 units' views are doubled | Arithmetic means are calculated using the generated priority series      |
| FAHP       | 21                                    | Geometric means are calculated using two-way pair-comparisons of experts |
| FAHPw      | 5 ? 2*16; 16 units' views are doubled | Geometric means are calculated using two-way pair-comparisons of experts |

Table 15 Main criteria priorities according to methods/ scenarios

| Scenario        |    M1 |    M2 |    M3 |    M4 |    M5 |    M6 | Cont.   |
|-----------------|-------|-------|-------|-------|-------|-------|---------|
| AHPa            | .1903 | .1079 | .0855 | .1450 | .2152 | .2561 | .2724   |
| AHPw            | .1963 | .1138 | .0849 | .1419 | .2061 | .2570 | .2747   |
| FAHP            | .1736 | .0867 | .0868 | .1553 | .2077 | .2899 | .0359   |
| FAHPw           | .1813 | .0920 | .0860 | .1508 | .1964 | .2934 | .0382   |
| DSen-1a         | .2067 | .1617 | .1512 | .1463 | .1408 | .1933 |         |
| DSen-2a         | .2080 | .1597 | .1499 | .1455 | .1400 | .1969 |         |
| Mean of all     | .1927 | .1203 | .1074 | .1475 | .1844 | .2478 |         |
| Mean of AHP     | .1854 | .1001 | .0858 | .1482 | .2063 | .2741 |         |
| [19]            | .2082 | .2742 | .1480 | .1366 | .1005 | .1325 | Other   |
| [20]            |  .275 |       |  .430 |  .235 |  .060 |       |         |
| [21]            |   .11 |   .18 |   .12 |       |   .12 |   .22 | ( .25 ) |
| [22]            |   .12 |   .18 |   .28 |   .17 |   .18 |   .06 |         |
| [23]            |       |  .338 |  .128 |  .066 |  .194 |  .274 |         |
| SW, p value     |  .073 |  .004 |  .547 |  .310 |  .108 |  .731 |         |
| t test, p value |  .499 |       |  .000 |  .416 |  .000 |  .000 |         |
| W test, p value |       |  .000 |       |       |       |       |         |

obtaining arithmetic means of each generated priority series which is the scenario-AHPa. AHPw is conducted similar to AHPa, but experts who have higher experience than 5 years, are accepted as having more reliable views, and hencetheir views are counted as doubled. For scenario FAHP and FAHPw, a simple fuzzy AHP approach is conducted, general views of experts for criteria priorities are calculated by using geometric mean. In FAHP, geometric means of each main criteria are calculated by using two-way pair-comparison scores of experts. In FAHPw, the geometric means are calculated by using the same paircomparison scores but 16 experts' views are doubled because of their experience as in AHPw.

The priorities obtained from AHP method can be accepted as being more appropriate in evaluating than the DEMATEL method; DEMATEL can be used especially in analyzing the interaction and interrelations between the criteria [49]. In most cases, DEMATEL-priorities have a tendency to have equal priorities, maybe because of the common usage of rationally close magnitudes of total interaction values. In this study, DEMATEL-priorities are calculated by using the vector sum of D ? R and D -R as in the study of Pekkaya and Aslan [49]. Thus, DEMATELpriorities are reported only to compare with AHP-priorities, since DEMATEL-priorities represent interaction weights which are calculated from interaction volumes. High interaction volumes may not always mean high priority. Interaction values should be taken into consideration, but in alternative decision priorities maybe be different than in highly interactive criteria.

According to AHP-priorities in terms of the scenario in Table 15, the main criteria priorities are almost the same and the most important main criteria in laptop selection are decided as M6-Brand, then M5-Other and M1-Price. M3 priority relatively has the least score. According to DEMATEL-priorities the most important criteria are decided as M1-Price and then M6-Brand and M5 priorities relatively have the least score. So, these results can be interpreted as follows. AHP-priorities represent a more valid importance degree in laptop selection, DEMATEL- R priority rank in main criteria or all in group, w criteria priorities priorities represent especially interaction degrees of criteria in laptop selection. For example, as M1-Price has the highest degree of interaction with other criteria ranking at 1 out of 6, M1-Price has a priority of about 17.36% ranking at 3 out of 6. In general representation, FAHP scenario priorities are selected because of both its common usages of related AHP literature and almost the same priorities determined in AHP scenarios. According to FAHP priorities, M6, M5 and M1 totally have 67.11% priority in laptop selection. These priorities are statistically compared with the results of the study Pekkaya and Aktogan [19], since generated priority series allow such statistical tests, namely t test, Wilcoxon tests. According to these tests and new findings, as M2 and M3 priorities are radically decreasing, M5 and M6 priorities are radically increasing, and M1 and M4 priorities are conserving their importance. The results can also be compared to the accepted priorities of some studies [20-23] in Table 15.

<!-- image -->

Table 16 Main and sub-criteria priorities via FAHP

| Main criteria; its priority   | Sub-criteria   | In group   | In group   | All in   | All in   |
|-------------------------------|----------------|------------|------------|----------|----------|
|                               |                | w          | R          | w        | R        |
| M1-Price; .1736               | S1-Price       | 1.000      | 1          | .1736    | 1        |
| M2-Speed; .0867               | S2-Proc-sp     | .3071      | 2          | .0266    | 16       |
|                               | S3-RAM-sp      | .3071      | 2          | .0266    | 16       |
|                               | S4-Card-sp     | .3858      | 1          | .0335    | 14       |
| M3-Storage; .0868             | S5-RAM-cap     | .2212      | 4          | .0192    | 21       |
|                               | S6-HDD/SDD     | .2584      | 2          | .0224    | 19       |
|                               | S7-Gr Card     | .2949      | 1          | .0256    | 18       |
|                               | S8-Proc-cache  | .2255      | 3          | .0196    | 20       |
| M4-Monitor; .1553             | S9-Resolution  | .1922      | 4          | .0298    | 15       |
|                               | S10-Size       | .2446      | 3          | .0380    | 13       |
|                               | S11-Touch scr  | .3087      | 1          | .0479    | 10       |
|                               | S12-Other      | .2545      | 2          | .0395    | 12       |
| M5-Other; .2077               | S13-Ports      | .2598      | 3          | .0539    | 8        |
|                               | S14-Weight     | .2630      | 2          | .0546    | 6        |
|                               | S15-Battery    | .1967      | 4          | .0408    | 11       |
|                               | S16-Drivers    | .2806      | 1          | .0583    | 4        |
| M6-Brand; .2899               | S17-Service    | .1809      | 5          | .0524    | 9        |
|                               | S18-Design     | .2140      | 2          | .0620    | 3        |
|                               | S19-Eco-fri    | .2261      | 1          | .0655    | 2        |
|                               | S20-Hardware   | .1877      | 4          | .0544    | 7        |
|                               | S21-Durability | .1913      | 3          | .0555    | 5        |

The determined sub-criteria priorities are listed in Table 16. S1-Price (17.36%) has the highest priorities mainly because of being also main criteria and having no other sub-criteria. Then S19-Eco-fri (6.55%) and S18-Design (6.20%) sub-criteria of M6-Brand have quite high priorities. However, RAM-cap (1.92%) and S8-Proc-cache (1.96%) sub-criteria of M3-Storage have quite low priorities. The other 15 sub-criteria have priority scores between 2.24% and 5.83%.

<!-- image -->

## 7 Conclusion

The evaluation of the alternatives can be accepted as one of the most important stages of the purchase decision of a product. In daily life, while instant decisions can be made, quantitative/analytical decision processes especially MCDM methods are preferred for important individual or company/institution decisions. Many decision-making models have been developed to make this important analytical approach easy. This study can be accepted as an application of what kind of useful information produced via the AHP and DEMATEL method, which are widely preferred among MCDM methods, can be used in choosing a laptop. The main purpose of this study is to determine the interaction between criteria, and the criteria priorities in the laptop selection problem.

According to results, price and other/peripheral properties of a laptop have more interrelated action with criteria than other main criteria. The brand image is determined as the most important main criteria in the laptop selection problem. Along with the brand image, other/peripheral properties and price criteria have a totally two-thirds (67.11%) priority among six main criteria. In the related literature, it is not appropriate to compare the findings with the literature, since both the focus is mainly on the selection processes of the alternatives and the criteria cannot usually be examined with such a rigorous base. The most important criterion may be determined as storage capacity [20], running speed [19], brand and warranty [21], Hdd/ Ram/cache memory [22], speed [23], while in this study, the brand image, the reason of which can be examined from different perspectives, is determined as the most important criteria. The experts in this study thought that the brand image, along with the price, had a dominant effect on other criteria according to interaction matrices/diagrams. When the results of AHP and DEMATEL are considered together, the brand image and price criteria can be considered as the most important criteria in the laptop selection problem. The interaction matrices/diagrams acquired from the DEMATEL method transmits lots of information about criteria and their interaction directions and magnitudes. For example, speed, storage, monitor and other/peripheral properties criteria have overall effecting feature but not strongly, while brand image which stands in the center of the interactions is transition criterion along with having the highest priority, and the price criterion is obviously being affected by all criteria. The results of the analysis are also re-interviewed with some of the experts, then they emphasized that the brand criterion has the structure that contains the importance of other criteria. This thought can be partially explained as the rationale for the analysis results obtained.

The lack of researching interaction models especially with DEMATEL in the relevant literature increases the originality of this study. This study also shows that criteria priorities should be researched along with their interactions for a fair investigation, since understanding the reasons of some priority scores may be explained by observing interaction matrices/diagrams. The results of this study can be assumed/considered to report remarkable findings in criteria investigations for decision-makers of the laptop, PC and tablet selection.

The following studies may concentrate on determining the objective criteria determining methods which use market data, in order to compare the criteria priorities, or laptops selection.

## References

1. Triantaphyllou, E.: Multi-criteria decision making methods. In: Multi-Criteria Decision Making Methods: A Comparative Study. Applied Optimization, vol. 44, pp. 1-4. Springer, Boston (2000). https://doi.org/10.1007/978-1-4757-3157-6\_2
2. Kahraman, C.: Fuzzy multi-criteria decision making: theory and applications with recent developments. Springer, Berlin (2008)
3. Chen, S.J., Hwang, C.L.: Fuzzy multiple attribute decision making methods. In: Fuzzy Multiple Attribute Decision Making. Lecture Notes in Economics and Mathematical Systems, vol. 375, pp. 289-486. Springer, Berlin (1992). https://doi.org/10.1007/ 978-3-642-46768-4\_5
4. Gabus, A., Fontela, E.: World problems an invitation to further thought within the framework of DEMATEL. Battelle Geneva Research Centre, Geneva (1972)
5. Saaty, T.: The analytic hierarchy process: Planning, priority setting, resource allocation. McGraw-Hill, New York (1980)
6. Hwang, C.L., Yoon, K.: Methods for multiple attribute decision making. In: Multiple Attribute Decision Making. Lecture Notes in Economics and Mathematical Systems, vol. 186, pp. 58-191. Springer, Berlin (1981). https://doi.org/10.1007/978-3-64248318-9\_3
7. Deng, J.L.: Control problems of grey systems. Sys. Contr. Lett. 1 (5), 288-294 (1982)
8. Brans, J.P., Vincke, P.: Note-A Preference Ranking Organisation Method: The PROMETHEE Method for Multiple Criteria Decision-Making. Manage. Sci. 31 (6), 647-656 (1985)
9. Costa, C.A.B., Vansnick, J.C.: MACBETH-An interactive path towards the construction of cardinal value functions. Int. Trans. Oper. Res. 1 (4), 489-500 (1994)
10. Zavadskas, E.K., Kaklauskas, A., Turskis, Z., Tamos ˇaitien, J.: Selection of the effective dwelling house walls by applying attributes values determined at intervals. J. Civil. Eng. Manage 14 (2), 85-93 (2008)
11. Saaty, T.L.: Fundamentals of the analytic network process, proceedings of ISAHP, Kobe, Japan, 48-63 (1999)
12. Trajcovic, S., Avakumovic, D., Opricovic, S.: Multi criteria optimization of an irrigation system. Archit. Civ. Eng. 1 (4), 547-552 (1997)
13. Brauers, W.K., Zavadskas, E.K.: The MOORA method and its application to privatization in a transition economy. Control Cybern 35 (2), 445-469 (2006)
14. Zavadskas, E.K., Turskis, Z.: A new additive ratio assessment (ARAS) method in multicriteria decision-making. Technol. Econ. Dev. Econ. 16 (2), 159-172 (2010)
15. Das, M.C., Sarkar, B., Ray, S.: Decision making under conflicting environment: a new MCDM method. Int. J. Appl. Decis. Sci. 5 (2), 142-162 (2012)
16. Shannon, C.E., Weaver, W.: The mathematical theory of communication, vol. 27, pp. 379-423. University of Illinois Press, Urbana (1949)
17. Zadeh, L.A.: Fuzzy sets. Inf. Control 8 (3), 338-353 (1965)
18. Diakoulaki, D., Mavrotas, G., Papayannakis, L.: Determining objective weights in multiple criteria problems: The critic method. Comput. Oper. Res. 22 (7), 763-770 (1995)
19. Pekkaya, M., Aktogan, M.: Dizu ¨stu ¨ Bilgisayar Sec ¸imi: DEA. TOPSIS ve VIKOR ile Kars ¸ ı las ¸t ı rmal ı Bir Analiz, Ekonomik ve Sosyal Aras ¸t ı rmalar Dergisi 10 (1), 157-178 (2014)
20. Sumi, R.S., Kabir, G.: Analytical hierarchy process for higher effectiveness of buyer decision process. Global J. Manage. Bus. Res 10 (2), 2-9 (2010)
21. Wichapa, N., Khokhajaikiat, P., Sarawan, K., Gonwirat, S.: Selection of the best laptop for educational purposes using hybrid decision making technique. 10 (3), 368 (2019)
22. Stanujkic ´, D., Jevtic ´, M., Ivanov, B.: An approach for laptop computers evaluation using multiple-criteria decision analysis. In Proc. of International Scientific Conference UNITECH, 263-267 (2018)
23. Rayhan, D.S.A.: Selection of best laptop for educational purpose by using ANP. World J. Soc. Sci. 6 (2), 167-181 (2016)
24. Borthick, A.F., Scheiner, J.H.: Selection of small business computer systems: Structuring a multi-criteria approach. J. Inf. Sys. 3 (2), 10-29 (1998)
25. Du ¨zak ı n, E., Demirtas ¸, S.: En uygun performansa sahip kis ¸isel bilgisayarlar ı n olus ¸turulmas ı nda veri zarflama analizinin kullan ı m ı . C ¸ ukurova U ¨ niversitesi Sosyal Bilimler Enstitu ¨su ¨ Dergisi 14 (2), 265-280 (2005)
26. Gal, T., Hanne, T.: Nonessential objectives within network approaches for MCDM. Eur. J. Oper. Res. 168 (2), 584-592 (2006)
27. Ertug ˘rul, I ˙ ., Karakas ¸og ˘lu, N.: Electre ve bulan ı k ahp yo ¨ntemleri ile bir is ¸letme ic ¸in bilgisayar sec ¸imi. Dokuz Eylu ¨l U ¨ nv I ˙ ktisadi ve I ˙ dari Bilimler Faku ¨ltesi Dergisi 25 (2), 23-41 (2013)
28. Lakshmi, T.M., Venkatesan, V.P., Martin, A.: Identification of a better laptop with conflicting criteria using TOPSIS. Int. J. Inf. Eng. Elect. Bus. 7 (6), 28-36 (2015)
29. Adal ı , E.A., Is ¸ ı k, A.T.: The multi-objective decision making methods based on MULTIMOORA and MOOSRA for the laptop selection problem. J. Ind. Eng. Int. 13 (2), 229-237 (2017)
30. Ulutas ¸, A., Cengiz, E.: CRITIC ve EVAMIX yo ¨ntemleri ile bir is ¸letme ic ¸in dizu ¨stu ¨ bilgisayar sec ¸imi. J. Int. Soc. Res. 11 (55), 881-887 (2018)
31. Hu, H.Y., Lee, Y.C., Yen, T.M., Tsai, C.H.: Using BPNN and DEMATEL to modify importance-performance analysis model-a study of the computer industry. Expert Syst. Appl. 36 (6), 9969-9979 (2009)
32. Tsai, S.B.: Using the DEMATEL model to explore the job satisfaction of research and development professionals in china's photovoltaic cell industry. Renew. Sustain. Energy Rev. 81 (1), 62-68 (2018)
33. Tseng, M.L., Lin, Y.H.: Application of fuzzy DEMATEL to develop a cause and effect model of municipal solid waste. Environ. Monit. Assess. 158 (1-4), 519-533 (2009)

<!-- image -->

34. Wu, W.W., Lee, Y.T.: Developing global managers' competencies using the fuzzy DEMATEL method. Expert Syst. Appl. 32 (2), 499-507 (2007)
35. Tzeng, G.H., Chiang, C.H., Li, C.W.: Evaluating intertwined effects in e-learning programs: A novel hybrid MCDM model based on factor analysis and DEMATEL. Expert Syst. Appl. 32 (4), 1028-1044 (2007)
36. Yang, Y.P.O., Shieh, H.M., Leu, J.D., Tzeng, G.H.: A novel hybrid MCDM model combined with DEMATEL and ANP with applications. Int. J. Oper. Res 5 (3), 160-168 (2008)
37. Kashi, K.: DEMATEL method in practice: finding the causal relations among key competencies. The 9th International days of statistics and economics, Prague, 2015, 723-732. https://pdfs. semanticscholar.org/, Accessed 08 Oct 2019
38. Aksakal, E., Dag ˘deviren, M.: ANP ve DEMATEL Yo ¨ntemleri I ˙ le Personel Sec ¸imi Problemine Bu ¨tu ¨nles ¸ik Bir Yaklas ¸im. Gazi U ¨ niversitesi Mu ¨hendislik-Mimarl ı k Faku ¨ltesi Dergisi 25 (4), 905-913 (2010)
39. Paksoy, S.: C ¸ ok Kriterli Karar Vermede Gu ¨ncel Yaklas ¸ ı mlar. Karahan Kitabevi, Adana (2017)
40. Hamzac ¸ebi, C., Pekkaya, M.: Determining of stock investments with grey relational analysis. Expert Syst. Appl. 38 (8), 9186-9195 (2011)
41. Kabir, G., Hasin, M.A.A.: Comparative analysis of AHP and fuzzy AHP models for multicriteria inventory classification. Int. J. Fuzzy Log. Syst 1 (1), 1-16 (2011)
42. Chou, Y.C., Sun, C.C., Yen, H.Y.: Evaluating the criteria for human resource for science and technology (HRST) based on an integrated fuzzy AHP and fuzzy DEMATEL approach. Appl. Soft. Comput 12 (1), 64-71 (2012)
43. Hsieh, T.Y., Lu, S.T., Tzeng, G.H.: Fuzzy MCDM approach for planning and design tenders selection in public office buildings. Int. J. Project Manage. 22 (7), 573-584 (2004)
44. Chou, Y.C., Yen, H.Y., Dang, V.T., Sun, C.C.: Assessing the human resource in science and technology for Asian countries: application of fuzzy AHP and fuzzy TOPSIS. Symmetry 11 (2), 251-267 (2019)
45. Akman, G., Alkan, A.: Tedarik Zinciri Yo ¨netiminde Bulan ı k AHP yo ¨ntemi kullan ı larak tedarikc ¸ilerin performans ı n ı n o ¨ lc ¸u ¨ lmesi: Otomotiv Yan Sanayiinde bir uygulama. I ˙ stanbul Ticaret U ¨ niversitesi Fen Bilimleri Dergisi 5 (9), 23-46 (2006)
46. Pekkaya, M.: Hizmet Kalite Standartlar ı Temelli, Hastanelerin C ¸ KKV I ˙ le Deg ˘erlendirilmesi, 17th International Symposium on Econometrics, Operations Research and Statistics (ISEOS 2016), 2-4 June 2016 in Sivas, Turkey. ISEOS 2016 Proceedings, 974-982. ISBN: 978-605-4561-47-6 (2016)
47. Roszkowska, E.: Rank ordering criteria weighting methods-a comparative overview. Optimum Studia Ekonomiczne 5 (65), 14-33 (2013)
48. Si, S.L., You, X.Y., Liu, H.C., Zhang, P.: DEMATEL technique: A systematic review of the state-of-the-art literature on methodologies and applications. Math Probl Eng 2018 , 1-33 (2018). https://doi.org/10.1155/2018/3696457
49. Pekkaya, M., Aslan, B.: OSB Yer Sec ¸iminde Dikkate Al ı nan Kriterler Aras ı Etkiles ¸imin ve Kriter O ¨ nem Derecelerinin Belirlenmesi. Int. J. Econ. Adm. Stud 18 , 293-308 (2018)
50. Pekkaya, M., ErolDemir, F.: Determining the Priorities of CAMELS Dimensions Based on Bank Performance. In: Dincer, H., Hacioglu, U ¨ ., Yu ¨ksel, S. (eds.) Global Approaches in Financial Economics, Banking, and Finance. Contributions to Economics. Springer, Cham (2018)
51. Pekkaya, M., Erol, F.: Generating priority series via AHP for conducting statistical tests on CAMELS dimension priorities in evaluating bank failure risk. J. Intell. Fuzzy Sys 37 (6), 8131-8146 (2019)

<!-- image -->

Fatma So ¨nmez C ¸ akir works as a Lecturer at Bart ı n University, Department of Management Information Systems (2009-2020) in Turkey. Her areas of expertise are Multi-Criteria Decision-Making, Numerical Decision Techniques, Artificial Neural Networks, Statistical Package Programs Applications, and Expert Systems. She completed her Master and Doctorate studies in the field of Numerical Methods. In January 2018, she received the title of doctor with her thesis titled ' 'Financial Time Series Estimation with Model Hybridization'' from Gebze Technical University. She has books on Artificial Neural Networks, Parametric Tests in Social Sciences and Partial Least Squares Structural Equation Modeling (PLS-SEM) SmartPLS 3.2. Applications and many application articles.

Mehmet Pekkaya acquired bachelor's degree both in physics, Bogazic ¸i University, Turkey, Educational Faculty (1990-1995), and in business administration, Anadolu University (Turkey), Business Faculty (2005-2009). He received his master's (2000-2002) and Ph.D. degrees (2006-2011) in business administration, Zonguldak Bu ¨lent Ecevit University (ZBEU), Turkey, Graduate School of Social Sciences. He acquired Associate Professor degree from InterUniversity Council of Turkey in September 2015 on numerical decision methods (specially statistics-operation research). Academic positions held by him are in ZBEU, Business Administration Department (subunit: Numerical Methods) as an instructor (2000-2011), assistant professor (2011-2015) and associate professor (2015-… ). His research interests are multi-criteria decision-making, statistical analysis, survey analysis, time series methods, and portfolio optimization. He took part in different international conferences and several workshops.