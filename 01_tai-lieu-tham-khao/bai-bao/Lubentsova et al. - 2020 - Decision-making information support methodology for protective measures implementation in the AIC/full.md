PAPER • OPEN ACCESS

# Decision-making information support methodology for protective measures implementation in the AIC

To cite this article: E V Lubentsova 2020 613 012073

View the article online for updates and enhancements.

## You may also like

GIS-based Industrial Land Suitability-Analysis for locating Industrial Parks in Raipur and Nava Raipur Ankur Baghel

Modeling of an intellectual system forassessing the environmental safety o irrigated lands using fuzzy logic methods V A Kuzmin, K E Tokarev, A Yu Rudenko et al.

Development of Evaluation System for-Rural Planting Adaptability Based on Computer Technology Zhiyi Xu

# Decision-making information support methodology for protective measures implementation in the AIC

E V Lubentsova<sup>1</sup>, G V Masyutina<sup>2</sup>, V F Lubentsov<sup>1</sup>, A V Permyakov<sup>3</sup> and M S Kozlova<sup>3</sup>

<sup>1</sup>Kuban State Technological University, 2 Moskovskaya str., Krasnodar, Russian Federation

<sup>2</sup>North-Caucasus Federal University, 56 ave. 40 Let Oktyabrya, Pyatigorsk, Russian Federation

<sup>3</sup>Yaroslav-the-Wise Novgorod State University, 41, ul. B. St. Petersburgskaya, Veliky Novgorod, Russian Federation

E-mail: elena-v-l@mail.ru

Abstract. The article describes the methodology of decision-making information support for protective measures implementation in the agro-industrial complex (AIC). The aim is to determine the rational area of treated land plots for protective measures implementation as components of cultivated crop area-based industrial technology. The methodology is based on the method of analytic hierarchy process (AHP) constructing and analyzing of multicriteria decision-making task solving in the selection of a rational land plot area for protection treatment. The following selection criteria are used: land plots route survey results giving the information about crops diseases throughout the area under study; affected plant damage degree; diseases harmfulness; environmental conditions (air temperature, precipitation (humidity)); probable losses. A hierarchical estimation of the used criteria importance is obtained, and an information model is formed. The model made it possible to establish a rational land plot option recommended for treatment. The novelty of the proposed methodology for solving the task is the following: the rationale for information technology (IT) application for a new class of tasks dealt with by the AIC and the technology practical focus on environmental friendliness ensuring and resources saving; on the basis of the methodology, the scientifically-based method, that does not require the involvement of a large number of experts, is used; the software implementation of the methodology on a PC does not impose special requirements for computing resources.

## 1. Introduction

The implementation of a set of measures aimed at plant protection against diseases with the use of decision-making support information technologies is a topical issue. A related problem is an environmental deterioration throughout the world and the legitimate pursuit of ecologically safe agricultural products and environment preservation. The analysis showed that, in the market, there are no ready-made domestic solutions that provide the necessary level of computerization and automation with reference to industry requirements [1]. Therefore, the decision to introduce a new information system in order to better the management, introduce international agricultural practices and the principles of “precision agriculture” is timely [2].

To provide the increasingly growing population with food, agricultural production needs to be raised by 70% [3]. This necessitates the modernization of information technology-based agricultural production processes, and it will make the processes as efficient as possible. The introduction of digital technologies and automation in the AIC is a recognised need for further agricultural production development in the world [4].

In the integrated plant protection management, protected crops state, disease development stage, and its harmfulness are taken into account and the application of such methods and means of control which would contribute to the reduction of the risks associated with pesticides use is included. In addition to this, plant protection is conducted taking into account environmental management, beneficial species preservation, and human and domestic animal health protection.

It should be noted that there are no universal recommendations on the use of plant protection products because particular crops protection measures have been developed for specific ecological-geographical areas. At the same time, measures that limit the spread of infection from plant to plant are relevant. This is a prerequisite for the rapid identification of dangerous focuses of diseases on a certain site in a specific ecological-geographical area. In constructing integrated plant protection management, an important role is played by modern protective measures, which are designed for specific areas, directed simultaneously against the complex of all harmful objects (pests, diseases, weeds), and which take into account rational areas of treated land plots, as components of cultivated crop area-based industrial technology. The application of active plant protection products should take into consideration the economic threshold of harmfulness. In carrying out integrated protection activities based on various qualitative and quantitative criteria for specific areas, economic-organizational, soil, climatic, and other conditions are taken into account. Difficulties of taking all the information into consideration in decision-making lead to significant crop losses. Therefore, the task of protective measures implementation should be regarded as multicriterion one, which requires rational cultivated land plot determining methodology development and implementation.

For a long time, agricultural production was not an attractive area for information technology (IT) due to the impossibility of using qualitative information and the paucity of quantitative information for operational decision-making. The use of IT in the agricultural sector was limited to the application of computers and software only in finance and commercial transactions [5]. The use of digital technologies to monitor crops and cultivated farmlands was started relatively recently. To date, agribusiness in Russia has made considerable progress, as evidenced by a stable level of investments in agricultural production and increased competition among agricultural producers. In the agro-industrial complex, the volume and quality of the use of modern technologies for the collection, storage, and processing of data go up. However, the need for effective data processing, its integration with quantitative data and credible conclusions that you can rely on when making decisions at the stage of crop cultivation, is highly insufficient. As a result, IT-based decision-making support is relevant.

The use of the technology with automated decision-making support for protective measures set development in a similar economy sector (science) of other countries is not known. The current trend in plant protection development is integrated management which combines processing operations in a single technological cycle. A very important requirement for the under-development methodology of rational treated land plot determining for protective measures implementation is the possibility for embedding it into the schemes of existing technologies. A large number of open problems in the industry, the solution of which is possible with the help of information technologies, is one of the main arguments for the relevance of this work, and one of the information technologies application elements, contributing to an increase in agricultural productivity by 70% by 2050.

The purpose of the developed methodology is to determine rational areas of treated land plots for the implementation of protective measures as components of cultivated crop area-based industrial technology.

However, despite the fact that land plots and areas can be considered as autonomous nodes in agrotechnological systems with complex material and energy linkages, it is difficult to divide them into rational treated areas. One of the reasons for this is that there are currently no clear recommendations and rules, the use of which would make it possible to reasonably estimate a potentially particularly important land plot for primary cultivation while taking into account several criteria. If necessary, each expert makes that estimation in accordance with their knowledge and experience. The task of making a high-priority land plot and its boundaries selection, which may become the root cause of a critical situation in the AIC, should be considered as a multicriteria decision-making task.

## 2. The rationale of the chosen task-solving method

The proposed methodology is based on the method of analytic hierarchy process (AHP) constructing and analyzing [6, 7, 8]. AHP is a systematic procedure that allows to solve multicriteria tasks, including qualitative and quantitative factors, using simple and well-founded rules. In scientific literature, the application of this method in various fields is discussed in detail. Thus, for example, the application of the pairwise comparisons method main results to the AHP analysis method is presented in [9]. In the study [10], an extension of the pairwise comparison method in computer implementation with fuzzy numbers is proposed, and the study [11] presents a fuzzy modeling device in the environment of MATLAB and fuzzyTECH. In [12], the solution to the task of priority vector finding in the analytic hierarchy process method as a nonlinear optimization task is presented. The above-mentioned works show that the decision-making processes both in the task of allocating a rational land plot for various crops cultivation and in other areas are largely similar. Therefore, the proposed methodology can be related to diversified use solutions. The following criteria can be used for the estimation of the choice of a high-priority land plot or area for its protection treatment:

 land plots route survey results that show the extent of crops diseases throughout the entire ecological-geographical area;

 affected plants damage degree, which is estimated on special scales and expressed as a percentage or in points;

 diseases harmfulness, i.e. diseases spread and development information, which determines the possible extent of damage;

 growing conditions (air temperature, precipitation), probable losses, and other indicators.

## 3. The methodology of a decision-making support information technology when choosing a rational treatment area

In this study, we offer an information technology for solving the task of choosing a rational treatment area using an integral estimate, which allows one to compare different land plot treatment area options, taking into account the totality of their characteristics and properties. The task of choosing the best option is difficult to formalize since high-priority land plot selection object characteristics contradict each other, i.e. when one of the characteristics gets better, another often deteriorates, which means that formalization of the choosing a rational treatment area option task solution is required. To do this, decomposition of the task is carried out, and, in the initial solution finding phase, the task of choosing a rational land plot is presented in the form of a hierarchical structure with a peak (target), intermediate levels-criteria and the lowest level, which includes a set of alternatives. In the next phase, priority is given to the criteria by which each of the alternatives is estimated. The method under consideration allows to pairwise compare the rational treated area option choosing task elements with respect to their effect on their common characteristic. The method of alternatives pairwise comparison makes it possible to obtain a result in the form of an inverse symmetric matrix, the elements of which are the intensities of the activities of the i-th hierarchy components in relation to the j-th hierarchy components, which take an estimate in the intensity scale of 1 to 9 [9]. A useful outcome in the alternatives pairwise comparison is the consistency index $\mathrm { { C I } = \left( \mathrm { { L } _ { m a x } - n } \right) / \left( n - 1 \right) }$ , which shows the magnitude of experts’ judgments consistency violation. Along with the pairwise comparisons matrix, an estimation measure of the degree of deviation from consistency is determined. If the established limits are exceeded, it is necessary to recheck experts’ judgments. In the work, CI minimizing by criteria priorities adjustment is proposed.

Further, a comparison is made between the CI and the value that would have been obtained by a random selection of quantitative judgments from the scale [9], and by inverse symmetric matrix formation. Dividing the CI by the value, corresponding to the same order matrix random consistency, we obtain a number called consistency ratio (CR). The CR value should be no more than 0.1. In this case, experts’ judgements are accepted as consistent, otherwise, it is necessary to double-check their judgments.

Consider the application of decision-making information technology on specific data. Based on the requirements for a cultivated crop, a pre-selection of several options of land plots and their adjacent territories is made, from which then the final choice of the best option will be made. These options are presented in table 1. The influence degree estimate of each of the criteria is summarized in table 2.

Table 1. Alternatives.

<table><tr><td>No</td><td>Option (alternative) name</td></tr><tr><td>1</td><td>the maximum possible treatment area is infected ( $A_1$ )</td></tr><tr><td>2</td><td>the land plot with the maximum degree of infection ( $A_2$ )</td></tr><tr><td>3</td><td>25% of the maximum possible treatment area is not infected ( $A_3$ )</td></tr><tr><td>4</td><td>50% of the maximum possible treatment area is not infected ( $A_4$ )</td></tr><tr><td>5</td><td>the land plot with the maximum possible infection probability ( $A_5$ )</td></tr></table>

Table 2. Selection criteria and alternatives.

<table><tr><td rowspan="2">Selection criteria</td><td colspan="5">Alternatives</td></tr><tr><td>the maximum possible treatment area is infected</td><td>the land plot with the maximum degree of infection</td><td>25% of the maximum possible treatment area is not infected</td><td>50% of the maximum possible treatment area is not infected</td><td>the land plot with the maximum possible infection probability</td></tr><tr><td>Land plots route survey results (C1)</td><td>available in full</td><td>available in full</td><td>available partially</td><td>available partially</td><td>not available</td></tr><tr><td>Damage degree (C2)</td><td>&lt; 2%</td><td>2-5%</td><td>5-10%</td><td>10-20%</td><td>≥ 20%</td></tr><tr><td>Disease harmfulness (C3)</td><td>0.5%</td><td>1%</td><td>3%</td><td>5%</td><td>&gt; 5%</td></tr><tr><td>Growing conditions (air temperature, precipitation) (humidity)) (C4)</td><td>favourable</td><td>moderate</td><td>satisfactory</td><td>satisfactory</td><td>satisfactory</td></tr><tr><td>Probable harmfulness or losses ( $C_5$ )</td><td>&gt;75%</td><td>75%</td><td>25%</td><td>50%</td><td>10%</td></tr></table>

Then, pairwise comparisons matrixes for the criteria are constructed [9]. For example, for the criterion “Land plots route survey results”, the pairwise comparisons matrix estimate numerical value is calculated as follows: (1∙2∙3∙5∙7)<sup>1/5</sup> = 2.91369. Having determined the eigenvector component estimates sum, which is 7.68547, we find normalized estimates of the priority vector for each of the selection criteria by dividing the eigenvector estimates by the component estimates sum. The obtained values are shown in the table 3 last column which indicates that the greatest value when choosing the option belongs to the criterion “Land plots route survey results”.

Table 3. Numerical estimates of the pairwise comparisons matrix for selection criteria.

<table><tr><td>Selection criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td>Eigenvector component estimates</td><td>Priority vector normalized estimates</td></tr><tr><td> $C_1$ </td><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>2.91369</td><td>0.37912</td></tr><tr><td> $C_2$ </td><td>1</td><td>1</td><td>2</td><td>7</td><td>8</td><td>2.56947</td><td>0.33433</td></tr><tr><td> $C_3$ </td><td>1/3</td><td>1/2</td><td>1</td><td>7</td><td>8</td><td>1.56317</td><td>0.20340</td></tr><tr><td> $C_4$ </td><td>1/5</td><td>1/7</td><td>1/7</td><td>1</td><td>2</td><td>0.38227</td><td>0.04974</td></tr><tr><td> $C_5$ </td><td>1/7</td><td>1/8</td><td>1/8</td><td>1/2</td><td>1</td><td>0.25677</td><td>0.03341</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Sum:</td><td>7.68547</td><td>1.00000</td></tr><tr><td colspan="8"> $L_{max} = 5.26095; CI = 0.06524; CR = 5.82 \%$ </td></tr></table>

The consistency of judgments, when constructing the criteria pairwise comparisons matrix, is verified using the consistency ratio (CR). To do so, dividing the CI by a number that corresponds to the random matrix dimension of 5x5 equal to 1.12 [6], we obtained the $\mathrm { C R } = 5 . 8 2 < 1 0 \%$ . Since inequality holds, the experts’ judgments are not reviewed.

Then, the pairwise comparisons matrixes for the remaining rational land plot selection criteria were calculated. For example, table 4 shows the pairwise comparisons matrix for the criterion “Land plots route survey results”.

Table 4. Comparison matrix for the criterion $^ { 6 6 } \mathrm { L }$ and plots route survey results”.

<table><tr><td></td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td><td>Eigenvector component estimates</td><td>Priority vector normalized estimates</td></tr><tr><td> $A_1$ </td><td>1</td><td>2</td><td>3</td><td>5</td><td>8</td><td>2.992556</td><td>0.421861</td></tr><tr><td> $A_2$ </td><td>1/2</td><td>1</td><td>3</td><td>5</td><td>7</td><td>2.208167</td><td>0.311286</td></tr><tr><td> $A_3$ </td><td>1/3</td><td>1/3</td><td>1</td><td>3</td><td>5</td><td>1.107566</td><td>0.156134</td></tr><tr><td> $A_4$ </td><td>1/5</td><td>1/5</td><td>1/3</td><td>1</td><td>3</td><td>0.525306</td><td>0.074052</td></tr><tr><td> $A_5$ </td><td>1/8</td><td>1/7</td><td>1/5</td><td>1/3</td><td>1</td><td>0.260102</td><td>0.036667</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Sum:</td><td>7.093697</td><td>1.000000</td></tr><tr><td colspan="8"> $L_{max} = 5.17249; CI = 0.043123; CR = 3.85 \%$ </td></tr></table>

By analogy, the pairwise comparisons matrixes for the remaining criteria are calculated. The results are presented in Figure 1, a, b, c, d, e.

Given the degree of each land plot selection criteria influence and the options numerical estimates in relation to the criteria, the best option was obtained. The global priorities estimates numerical values are given in table 5 and in figure 2.

![](images/4aa9a1a056d106ddaf7ee84dd7d0817f8533abe1f1d76bd84506962657d5a48f.jpg)

![](images/844031b4b1800573d59468b8777810605b5f456cc2ad7a9a176ceb7a06479e3e.jpg)  
с)  
d)

![](images/1ba50dcd7aade8b38da0f36b76658c73d05b447c9dd6dec00357e808fbd47ddc.jpg)  
e)  
Figure 1. Priority vector normalized estimates graphs: а) for the criterion “Land plots route survey results”; b) for the criterion “Damage degree”; c) for the criterion “Disease harmfulness”; d) for the criterion “Growing conditions”; e) for the criterion “Probable harmfulness or losses”.

Table 5. Results matrix.

<table><tr><td rowspan="4">Alternatives</td><td colspan="5">Criteria</td><td rowspan="4">Global priorities</td></tr><tr><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td colspan="5">Priority vector numerical value</td></tr><tr><td>0.379122</td><td>0.334332</td><td>0.203396</td><td>0.049740</td><td>0.033410</td></tr><tr><td>The maximum possible treatment area is infected</td><td>0.421861</td><td>0.507892</td><td>0.510505</td><td>0.484967</td><td>0.510039</td><td>0.474739</td></tr><tr><td>The land plot with the maximum degree of infection</td><td>0.311286</td><td>0.278283</td><td>0.258568</td><td>0.295037</td><td>0.263834</td><td>0.287136</td></tr><tr><td>25% of the maximum possible treatment area is not infected</td><td>0.156134</td><td>0.112326</td><td>0.122441</td><td>0.111239</td><td>0.129574</td><td>0.131514</td></tr><tr><td>50% of the maximum possible treatment area is not infected</td><td>0.074084</td><td>0.068721</td><td>0.073949</td><td>0.071162</td><td>0.063636</td><td>0.071822</td></tr><tr><td>The land plot with the maximum possible infection probability</td><td>0.035828</td><td>0.032779</td><td>0.034537</td><td>0.037595</td><td>0.032918</td><td>0.034544</td></tr></table>

The graph of the obtained global priorities estimates is presented in figure 2.

![](images/5668a2478cb1add75ffc99827fc5a30f5a1373fbff072d24f8dca3dcbb7efeaf.jpg)  
Figure 2. Obtained global priorities estimates graph.

The information model obtained on the basis of the alternatives pairwise comparison has the form:

$$
A = 0. 4 7 4 7 3 9 \cdot A _ {1} + 0. 2 8 7 1 3 6 \cdot A _ {2} + 0. 1 3 1 5 1 4 \cdot A _ {3} + 0. 0 7 1 8 2 2 \cdot A _ {4} + 0. 0 3 4 5 4 4 \cdot A _ {5}.\tag{1}
$$

The best alternative is considered to be the one with the maximum value of global priority. From (1), it can be seen that the first option surpasses the other analogues in basic characteristics. Therefore, the land plot for a high-priority treatment is the one for which the possible treatment area is maximally infected.

In order to increase the reliability of the decision, a multicriteria estimation was carried out, and the best alternative choice was made on the basis of the fuzzy sets [13, 14, 15]. In this calculation, the following fuzzy sets forms are obtained:

$$
\begin{array}{r} C _ {1} = \left\{\frac {0 . 3 7 8}{A _ {1}}, \frac {0 . 3 7 4}{A _ {2}}, \frac {0 . 1 3 3}{A _ {3}}, \frac {0 . 0 6 9}{A _ {4}}, \frac {0 . 0 4}{A _ {5}} \right\}; C _ {2} = \left\{\frac {0 . 5 5 9}{A _ {1}}, \frac {0 . 2 1 8}{A _ {2}}, \frac {0 . 0 9 3}{A _ {3}}, \frac {0 . 0 6 5}{A _ {4}}, \frac {0 . 0 4}{A _ {5}} \right\}; \\ C _ {3} = \left\{\frac {0 . 5 5 5}{A _ {1}}, \frac {0 . 2 1 1}{A _ {2}}, \frac {0 . 1 0 3}{A _ {3}}, \frac {0 . 0 6 9}{A _ {4}}, \frac {0 . 0 4 2}{A _ {5}} \right\}; C _ {4} = \left\{\frac {0 . 5 1 2}{A _ {1}}, \frac {0 . 2 7 2}{A _ {2}}, \frac {0 . 1 0 2}{A _ {3}}, \frac {0 . 0 6 5}{A _ {4}}, \frac {0 . 0 4 4}{A _ {5}} \right\}; \\ C _ {5} = \left\{\frac {0 . 5 5 9}{A _ {1}}, \frac {0 . 2 1 4}{A _ {2}}, \frac {0 . 1 0 5}{A _ {3}}, \frac {0 . 0 6 1}{A _ {4}}, \frac {0 . 0 4}{A _ {5}} \right\}. \end{array}\tag{2}
$$

The best solution depends on the importance of the criteria $\mathrm { C } _ { 1 } { \div } \mathrm { C } _ { 5 }$ . For these criteria, the importance factors will be respectively equal: $\mathbf { a } _ { 1 } = 0 . 3 7 1 ; \mathbf { a } _ { 2 } = 0 . 3 5 8 ; \mathbf { a } _ { 3 } = 0 . 1 5 7 ; \mathbf { a } _ { 4 } = 0 . 0 8 3 ; \mathbf { a } _ { 5 } = 0 . 0 4 9$ . Given the importance of the criteria, we will have the following fuzzy sets:

$$
\begin{array}{r} \tilde {C} _ {1} ^ {\alpha_ {1}} = \left\{\frac {0 . 3 7 8 ^ {0 . 3 7 1}}{A _ {1}}, \frac {0 . 3 7 4 ^ {0 . 3 7 1}}{A _ {2}}, \frac {0 . 1 3 3 ^ {0 . 3 7 1}}{A _ {3}}, \frac {0 . 0 6 9 ^ {0 . 3 7 1}}{A _ {4}}, \frac {0 . 0 4 ^ {0 . 3 7 1}}{A _ {5}} \right\} \\ = \left\{\frac {0 . 6 9 7}{A _ {1}}, \frac {0 . 6 9 4}{A _ {2}}, \frac {0 . 4 7 3}{A _ {3}}, \frac {0 . 3 7 1}{A _ {4}}, \frac {0 . 3 0 3}{A _ {5}} \right\} \end{array}
$$

$$
\begin{array}{r} \tilde {C} _ {2} ^ {\alpha_ {2}} = \left\{\frac {0 . 5 5 9 ^ {0 . 3 5 8}}{A _ {1}}, \frac {0 . 2 1 8 ^ {0 . 3 5 8}}{A _ {2}}, \frac {0 . 0 9 3 ^ {0 . 3 5 8}}{A _ {3}}, \frac {0 . 0 6 5 ^ {0 . 3 5 8}}{A _ {4}}, \frac {0 . 4 ^ {0 . 3 5 8}}{A _ {5}} \right\} \\ = \left\{\frac {0 . 8 1 2}{A _ {1}}, \frac {0 . 5 7 9}{A _ {2}}, \frac {0 . 4 7 2}{A _ {3}}, \frac {0 . 3 7 6}{A _ {4}}, \frac {0 . 7 2 0}{A _ {5}} \right\} \end{array}
$$

$$
\begin{array}{r} \tilde {\mathcal {C}} _ {3} ^ {\alpha_ {3}} = \left\{\frac {0 . 5 5 5 ^ {0 . 1 5 7}}{A _ {1}}, \frac {0 . 2 1 1 ^ {0 . 1 5 7}}{A _ {2}}, \frac {0 . 1 0 3 ^ {0 . 1 5 7}}{A _ {3}}, \frac {0 . 0 6 9 ^ {0 . 1 5 7}}{A _ {4}}, \frac {0 . 0 4 2 ^ {0 . 1 5 7}}{A _ {5}} \right\} = \left\{\frac {0 . 9 1 1}{A _ {1}}, \frac {0 . 7 9 3}{A _ {2}}, \frac {0 . 6 1 1}{A _ {3}}, \frac {0 . 6 5 7}{A _ {4}}, \frac {0 . 6 0 8}{A _ {5}} \right\} \tilde {\mathcal {C}} _ {4} ^ {\alpha_ {4}} = \\ \left\{\frac {0 . 5 1 2 ^ {0 . 0 8 3}}{A _ {1}}, \frac {0 . 2 7 2 ^ {0 . 0 8 3}}{A _ {2}}, \frac {0 . 1 0 2 ^ {0 . 0 8 3}}{A _ {3}}, \frac {0 . 0 6 5 ^ {0 . 0 8 3}}{A _ {4}}, \frac {0 . 0 4 4 ^ {0 . 0 8 3}}{A _ {5}} \right\} = \left\{\frac {0 . 9 4 6}{A _ {1}}, \frac {0 . 8 9 8}{A _ {2}}, \frac {0 . 8 2 7}{A _ {3}}, \frac {0 . 7 9 7}{A _ {4}}, \frac {0 . 7 7 1}{A _ {5}} \right\} \end{array}
$$

$$
\begin{array}{r} \tilde {C} _ {5} ^ {\alpha_ {5}} = \left\{\frac {0 . 5 5 9 ^ {0 . 0 4 9}}{A _ {1}}, \frac {0 . 2 1 4 ^ {0 . 0 4 9}}{A _ {2}}, \frac {0 . 1 0 5 ^ {0 . 0 4 9}}{A _ {3}}, \frac {0 . 0 6 1 ^ {0 . 0 4 9}}{A _ {4}}, \frac {0 . 0 4 ^ {0 . 0 4 9}}{A _ {5}} \right\} \\ = \left\{\frac {0 . 9 7 2}{A _ {1}}, \frac {0 . 9 2 7}{A _ {2}}, \frac {0 . 8 9 5}{A _ {3}}, \frac {0 . 8 7 1}{A _ {4}}, \frac {0 . 8 5 4}{A _ {5}} \right\} \end{array}
$$

Given the obtained results, the selection rule (4) can be written in the form [16]:

$$
\begin{array}{l} D = \left\{\min (0. 6 9 7; 0. 8 1 2; 0. 9 1 1; 0. 9 4 6; 0. 9 7 2) / A _ {1}; \min (0. 6 9 4; 0. 5 7 9; 0. 7 9 3; 0. 8 9 8; 0. 9 2 7) / A _ {2}; \right. \\ \left. \min (0. 4 7 3; 0. 4 2 7; 0. 6 1 1; 0. 8 2 7; 0. 8 9 5) / A _ {3}; \min (0. 3 7 1; 0. 3 7 5; 0. 6 5 7; 0. 7 9 7; 0. 8 7 1) / A _ {4}; \right. \\ \left. \min (0. 3 0 3; 0. 7 2 0; 0. 6 0 8; 0. 7 7 1; 0. 8 5 4) / A _ {5} \right\}, \end{array} \tag {3}
$$

where D is the resulting solution.

Based on the fuzzy sets (3), we obtain the following fuzzy solution form:

$$
\tilde {D} = \left\{\frac {0 . 6 9 7}{A _ {1}}, \frac {0 . 5 7 9}{A _ {2}}, \frac {0 . 4 2 7}{A _ {3}}, \frac {0 . 3 7 1}{A _ {4}}, \frac {0 . 3 0 3}{A _ {5}} \right\}.\tag{4}
$$

## 4. Results and their analysis

The analysis of the obtained information model (1) based on the AHP and of the solution (4) shows the advantage of option $\mathbf { A } _ { 1 }$ over the others, and also indicates the proximity of options A and ${ \bf A } _ { 2 }$ and the weak advantage of alternative ${ \bf A } _ { 5 }$ over alternatives $\mathbf { A } _ { 1 }$ and ${ \bf A } _ { 2 }$ . The land plot with the maximum possible infection probability (the fifth option) is characterized by a global priority minimum value (0.303) and is not a contender for high-priority treatment.

Analyzing the results of the calculations based on the AHP and fuzzy set methods, the following points can be made:

1. The results obtained using the analytic hierarchy process method and the fuzzy set method do not differ significantly.

2. The estimates received in all cases demonstrate the same studied options rankings obtaining.

3. The calculation scheme based on the AHP method is well tested and, along with the fuzzy set method, ensures the stability of the obtained results regarding the baseline data.

4. The fuzzy sets method allows to additionally use interval estimates, which makes it quite promising with a wider scope of application.

## 5. Сonclusion

A common approach to the protection of cultivated crops is this: all areas and land plots, even those adjacent to the infected one, need protection treatment. Therefore, we have redundancy and significant costs. Only then it turns out that the result is far from expected. In practice, it is sufficient to identify a high-priority land plot and to implement protective measures for it, the measures which reduce or completely eliminate precautionary impacts on neighboring land plots. This allows us to reduce costs and improve environmental friendliness.

The presented in the study methodology of decision-making support when carrying out a set of protective measures in the management of the agricultural sector allows to solve the multicriteria task of choosing a rational treated area and eliminate the need for protection treatment of the areas and land plots adjacent to the infected site, thus reducing the costs and improving the environment. In creating the system, the hierarchical approach was applied, which allows to create, expand, and modify the information base when solving the task under consideration and similar tasks of various kinds. The generated information model allows to perform a hierarchical estimation of the used criteria importance. Further researches should focus on the development of models with criteria combining economic and environmental factors, and on the comparative analysis of the hierarchical relationship between introduced new factors and the previously studied factors.

## References

[1] Agriculture and fishery technologies Available at: http://www.tadviser.ru/index.php (accessed: 19.06.2020)

[2] Information technology in the agricultural holding “Kuban” Available at: http://www.tadviser.ru/index.php (accessed: 19.06.2020)

[3] IT in the agro-industrial complex of Russia Available at: http://www.tadviser.ru/index.php (accessed: 19.06.2020)

[4] Overview of digital technologies for the agro-industrial complex: from GIS to the Internet of things Available at: http://integral-russia.ru/2019/10/28/tsifrovaya-platforma-razvitiyaagropromyshlennogo-kompleksa-kontseptsiya-i-osnovnye-tezisy/ (accessed: 19.06.2020)

[5] IT-technologies in agriculture Available at: http://www.controlunion.ru/index.php/11- novosti/425-it-tekhnologii-v-selskom-khozyajstve (accessed: 19.06.2020)

[6] Saati T L 2009 Decision making with dependencies and feedbacks: Analytical networks (Moscow: Knizhnyi dom “LIBROCOM”) p 360

[7] Bin Zhu and Zeshui Xu 2014 Analytic hierarchy process-hesitant group decision making Eur. J. of Oper. Res. 239 (3) 794–801

[8] Saati T L 1972 An eigenvalue allocation model for prioritization and planning (Univercity of Pennsylvania: Energy Management and Policy Center)

[9] David G 2015 Pairwise Comparison Method (Moscow: Statistika) p 144

[10] Alim A, Johora F T, Babu S and Sultana A 2015 Elementary Operations on L-R Fuzzy Number Advances in Pure Mathematics 5 (3) 131–36

[11] Leonenkov A V 2005 Fuzzy modelling using MATLAB and FuzzyTECH environments (St. Petersburg: BHV-St. Petersburg) p 183

[12] Javanbarg M B, Scawthorn C, Kiyono J and Shahbodaghkhan B 2011 Fuzzy AHP-based multicriteria decision making systems using particle swarm optimization Expert Systems with Applications 39 (1) 960–66

[13] Andreychikova O A 2001 Decision making in the conditions of mutual dependence of complex technical systems criteria and alternatives Information technology 11 14–19

[14] Masyutina G V and Lubentsov V F 2009 Methodology for solving the selection multicriteria task for dynamic system management Problems of management, transmission, and processing of information-ATM-TKI-50: materials of the Int. Scientific Conf. (Saratov: State Technical University of Saratov) 128–40

[15] Shtovba S D Introduction to the theory of fuzzy sets and fuzzy logic Available at: http://matlab.exponenta.ru/fuzzylogic/book1/4\_6.php (accessed: 19.06.2020)

[16] Bellman R and Zade L 1976 Decision making in vague terms: Collection book: Questions of analysis and decision-making procedures (Moscow: Mir Publisher) 172–215