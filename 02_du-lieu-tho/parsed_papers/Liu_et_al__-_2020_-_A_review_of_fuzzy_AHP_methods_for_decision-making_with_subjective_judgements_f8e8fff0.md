Review

# A review of fuzzy AHP methods for decision-making with subjective judgements

![](images/818ae233b62ad87378ad003b029a35e051a8d109873e419c30196f006263a87a.jpg)

Yan Liu <sup>a,</sup>⇑, Claudia M. Eckert <sup>b</sup>, Christopher Earl <sup>b</sup>

<sup>a</sup> School of Computer Science and Technology, Changchun University of Science and Technology, Changchun 130022, Jilin, China <sup>b</sup> School of Engineering and Innovation, The Open University, Walton Hall, Milton Keynes MK7 6AA, UK

## a r t i c l e i n f o

Article history: Received 26 January 2020 Revised 5 June 2020 Accepted 9 July 2020 Available online 19 July 2020

Keywords: Fuzzy Analytic Hierarchy Process Fuzzy set Multi-criteria decision-making Subjective judgement Selection problem

## a b s t r a c t

Analytic Hierarchy Process (AHP) is a broadly applied multi-criteria decision-making method to determine the weights of criteria and priorities of alternatives in a structured manner based on pairwise comparison. As subjective judgments during comparison might be imprecise, fuzzy sets have been combined with AHP. This is referred to as fuzzy AHP or FAHP. An increasing amount of papers are published which describe different ways to derive the weights/priorities from a fuzzy comparison matrix, but seldomly set out the relative benefits of each approach so that the choice of the approach seems arbitrary. A review of various fuzzy AHP techniques is required to guide both academic and industrial experts to choose suit able techniques for a specific practical context. This paper reviews the literature published since 2008 where fuzzy AHP is applied to decision-making problems in industry, particularly the various selection problems. The techniques are categorised by the four aspects of developing a fuzzy AHP model: (i) representation of the relative importance for pairwise comparison, (ii) aggregation of fuzzy sets for group decisions and weights/priorities, (iii) defuzzification of a fuzzy set to a crisp value for final comparison, and (iv) consistency measurement of the judgements. These techniques are discussed in terms of their underlying principles, origins, strengths and weakness. Summary tables and specification charts are provided to guide the selection of suitable techniques. Tips for building a fuzzy AíP model are also included and six open questions are posed for future work.

 2020 Elsevier Ltd. All rights reserved.

## 1. Introduction

In many professional situations, experts are confronted with a given set of alternatives that they need to choose from, for example when selecting a supplier or a technology. This type of decisionmaking problem is intuitive when considering a single criterion, since experts can choose the alternative of the highest preference. It becomes complicated when there are multiple criteria. These criteria are often not of equal importance and the alternatives have very varied performance. Formal methods are needed to ensure a structured means of making decisions. Many methods are available such as Analytic Hierarchy Process (AHP), Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) and Data Envelopment Analysis (DEA) (see Chai, Liu, and Ngai (2013), Karsak and Dursun (2016) and Zimmer, Fröhling, and Schultmann (2016) for an overview of available decision-making methods). Among them, AHP proposed by Saaty (1980) has been applied extensively to evaluate complex multi-criteria alternatives in a number of fields (Emrouznejad & Marra, 2017; Subramanian & Ramanathan, 2012). It outperforms by ease of use, structuring problems systematically and calculating both criteria weights and alternative priorities. As a popular methodology for handling imprecision, fuzzy sets proposed by Zadeh (1965) are combined with AHP, namely fuzzy AHP or FAHP. This integrated method maintains the advantage of AHP and has been widely applied (Mardani, Jusoh, & Zavadskas, 2015). The procedure of building a fuzzy AHP model follows establishing the comparison matrix, aggregating multiple judgements, measuring the consistency and defuzzifying the fuzzy weights. Various techniques exist for each aspect. However, Little research has examined fuzzy AHP in terms of these aspects and set out the relative benefits of the techniques. This paper reviews the techniques regarding these four aspects, aiming to guide both academics and industrial experts to choose suitable techniques according to their practical context.

AHP structures a problem in a hierarchical way, descending from a goal to criteria, sub-criteria and alternatives in successive levels (Saaty, 1990). The hierarchy provides the experts with an overall view of the complex relationships inherent in the context; and helps them to assess whether the elements of the same level are comparable. Elements are then pairwise compared according to 9 level-scales to derive their weights. However, pairwise comparison, the essence of AHP, introduces imprecision because it requires the judgements of experts. In practical cases, experts might not be able to assign exact numerical values to their preferences due to limited information or capability (Chan & Kumar, 2007; Xu & Liao, 2014).

To handle the imprecision in AHP, exact numbers are replaced with fuzzy numbers representing the linguistic expressions in fuzzy AHP. This tolerates the vague judgements by assigning membership degrees to exact numbers to describe to what extent these numbers belong to an expression. However, introducing fuzzy sets to AHP makes the calculation process less straightforward because different fuzzy sets exist and the associated operations are complex. The techniques for AHP such as eigenvector method and geometric mean cannot directly be used to derive the weights/ priorities from a fuzzy comparison matrix. Many techniques for building a fuzzy AHP model have been proposed. They vary in terms of essential features, strengths and weakness. To the best of our knowledge, limited research has reviewed fuzzy AHP except

Kubler, Robert, Derigent, Voisin, and le Traon (2016) who discuss the application areas.

The earliest reference that we have found dates from 1983 (van Laarhoven & Pedrycz, 1983). Now, fuzzy AHP has become a popular fuzzy multi-criteria decision-making (MCDM) method (Kubler et al., 2016). It is applied in various industries, for example airline retail (Rezaei, Fahim, & Tavasszy, 2014), agriculture (Hashemian, Behzadian, Samizadeh, & Ignatius, 2014; Liu, Eckert, Bris, & Petit, 2019), automobile (Büyüközkan & Güleryüz, 2016; Zimmer, Fröhling, Breun & Schultmann, 2017), logistics (Yayla, Oztekin, Gumus, & Gunasekaran, 2015), manufacturing (Kar, 2014; Ayhan & Kilic, 2015), maritime (Celik & Akyuz, 2018), pharmacy (Alinezad, Seif, & Esfandiari, 2013) and service (Khorasani, 2018), and to solve various problems, for example location selection (Erbas, Kabak, Ozceylan, & Çetinkaya, 2018; Singh, Chaudhary, & Saxena, 2018), machine selection (Nguyen, Md Dawal, Nukman, Aoyama, & Case, 2015; Parameshwaran, Kumar, & Saravanakumar, 2015), supplier selection (Akkaya, Turanog˘lu, & Öztas, 2015; Awasthi, Govindan, & Gold, 2018; Kumar, Rahman, & Chan, 2017; Shakourloo, Kazemi, & Javad, 2016), technique selection (Balusa & Gorai, 2018; Budak & Ustundag, 2015; Naderzadeh, Arabalibeik, Monazzam, & Ghasemi, 2017), sustainability management (Calabrese, Costa, Levialdi & Menichin, 2019, 2016), business impacts assessment (Lee, Cho, & Kim, 2015), risk analysis (Mangla, Kumar, & Barua, 2015), intellectual capital assets management (Calabrese, Costa, & Menichini, 2013) and teaching performance evaluation (Chen, Hsieh, & Do, 2015). These decision problems all deal with the assessment and prioritisation of the alternatives which could be physical entities (e.g. machines, suppliers and locations) or abstract items (e.g. business impact indicators and risk factors). The results are used for selection if a preferred solution is required. The fuzzy AHP models built for the assessment problem in one field are applicable to other fields. This review paper is based on a systematic search of literature published since 2008 where fuzzy AHP is applied to the decision-making problems in industry. Our research originates from supplier selection and then branches out to other topics such as machine selection, location selection, ERP system selection, project selection and technology selection.

![](images/3f5a221315d59b1e9d9887d5c4f505c43c0573b69edd1b273a0c15022d16234e.jpg)  
Fig. 1. The calculation process of fuzzy AHP using triangular fuzzy numbers

The rest of paper is organised as follows. Section 2 explains the principle of fuzzy AHP method. Section 3 shows the research methodology of this study. There are four important aspects to develop a fuzzy AHP model, which are explained in Sections 4–7.

Section 4 explains how different fuzzy numbers, as a special type of fuzzy set, can be defined for judgement representations when establishing the comparison matrix.

Section 5 discusses how these fuzzy numbers are aggregated for group decisions and for deriving the weights.

Section 6 identifies the defuzzification method to obtain a crisp value from a fuzzy value for intuitive comparison.

Section 7 examines the consistency measurement which is an important way to ensure valid pairwise judgements.

To help readers extract quick information, the reviewed techniques are summarised in graphical and tabular forms. Discussions and insights are provided at the end of each section for choosing appropriate techniques. We also point out mistakes in few papers and indicate possible corrections, along with the review. Section 8 concludes this study with open questions for future research and a general guidance for building a fuzzy AHP model.

## 2. Principle of fuzzy AHP

The development of a fuzzy AHP model overall follows the process to develop an AHP model as illustrated in Fig. 1. The white and the light grey boxes show the common steps between AHP and fuzzy AHP but different techniques are applied in the steps of light grey boxes. The dark grey box is the step in fuzzy AHP but not in AHP. We illustrate the process with supplier selection using a special type of fuzzy set, triangular fuzzy number.

Structure the problem: The problem is decomposed in a hierarchy, which includes goal (‘select best suppliers’ in Fig. 1), criteria sub-criteria (Criterion 1 to Criterion 3) and alternatives (Supplier 1 to Supplier 3).

Establish the fuzzy pairwise comparison matrix: Let $\boldsymbol { F } = \left[ \widetilde { c } _ { i j } \right] _ { n \times n }$ be the matrix for n criteria against the goal. $\widetilde { c } _ { i j }$ is a fuzzy <sup></sup>set representing the relative importance of criterion i over j. Its reciprocal, $1 / \widetilde { c } _ { i j } ,$ is equal to the relative importance of criterion j over $i , \widetilde { c } _ { j i } .$ For example, the triangular fuzzy number (2,3,4) in the judgement table of expert 1 is the relative importance of criterion 1 over criterion 2 and thus $( 1 / 4 , 1 / 3 , 1 / 2 )$ is that of criterion 2 over criterion 1. Replacing crisp values with fuzzy sets is the fundamental difference between fuzzy AHP and AHP. It results in that the techniques to derive weights/priorities in AHP cannot directly be used. Several fuzzy sets are applicable to establish the comparison matrix as explained in Section 4.

![](images/bd702ffdbcea9fadcb2961fa6014adc137a292cb83b89d0911b6c16180fd9bee.jpg)  
Fig. 2. Research framework.

Synthesise the judgements: if there are multiple experts, their opinions will be aggregated. As illustrated in Fig. 1, it takes place either before or after calculating the fuzzy weights, i.e. synthesising the pairwise comparisons (as labelled by ① in Fig. 1) or the fuzzy weights (as labelled by ②). In the example, the relative importance of criterion 1 over criterion 2 from the two experts are different, i.e. (2, 3, 4) and (1, 2, 3). They are aggregated first. The techniques are examined in Section 5.

Calculate the fuzzy weights of the criteria: This step aggregates multiple fuzzy sets in the matrix into a single fuzzy set. Some aggregation methods in the previous step are applicable. Specialised methods are presented in Section 5.

Defuzzify the fuzzy weights: This is an extra step compared with AHP which maps a fuzzy set (i.e. fuzzy weight) to a crisp value (i.e. crisp weight) for further comparison. Fuzzy sets are difficult to compare directly because they are partially ordered rather than the linear or strictly ordered crisp values. Section 6 identifies the most prevalent defuzzification methods.

Check the consistency: Without this step, weights can still be obtained, and thus it is overlooked by some research. However, it is necessary to measure the fuzzy pairwise comparison matrix for the consistency. Suppose that criterion 1 is more important than criterion 2 and much more important than criterion 3. Logically, criterion 2 is more important than criterion 3. If the expert judges criterion 2 less important than criterion 3, then the judgements between criteria 1, 2 and 3 are in conflict. This step takes place after the comparison matrix is established (either the one from an individual expert or the aggregated one from multiple experts). The matrix is considered consistent if the contradictions among the pairwise comparisons are within a predefined threshold, namely consistency ratio. Otherwise, the experts need to recompare the criteria. The discussion is in Section 7.

The calculations of the sub-criteria weights and the alternative priorities follow the same process as described above. The calculated weights of sub-criteria are ‘local weights’, which are transformed to ‘global weights’ by multiplying with the weight of their parent criterion. For ease of explanation, we use ‘weight’ for ‘global weight’. The overall priority of alternative S is the aggregation of its priorities under all the criteria/sub-criteria. w<sub>j</sub> is the weight of criterion/sub-criterion j; $p _ { j } ^ { S i }$ is the priority of S under criterion $\cdot j ;$ n is the number of criteria/sub-criteria.

$$
\text { Priority } _ {S i} = \sum_ {j = 1} ^ {n} w _ {j} \times p _ {j} ^ {S i}\tag{1}
$$

The overall calculation process in Fig. 1 reveals the four important aspects in developing a fuzzy AHP model: (1) representation of judgements for pairwise comparison to establish the matrix, (2) aggregation of fuzzy sets for group decisions and criteria weights, (3) defuzzification of a fuzzy set for further comparison and (4) consistency measurement for limited contradiction, which will be addressed in turn.

## 3. Research methodology

This research was carried out in two stages as shown in Fig. 2. In the first stage, we chose ‘supplier selection’ as the primary investigation topic. Fuzzy AHP is a generic decision-making method, applicable to most problems. Supplier selection is a typical and representative decision-making problem, involving prioritisation, assessment and ranking. It has a mixture of subjective and objective criteria and brings out many situations for which fuzzy AHP is required. As listed in Table A.9, it has been applied in a number of industries. Therefore, supplier selection is a potential target for many of the techniques. It is also a topic where fuzzy AHP has been most commonly used, according to the numbers of the reviewed articles. This corresponds to the survey result of Kubler et al. (2016). We selected 57 articles to analyse the methodological development of fuzzy AHP in terms of the four aspects. Under each aspect, the identified techniques were further categorised according to their properties (cf. fishbone diagram in Fig. 2). Each part of the fishbone diagram is presented in details in the following sections (cf. Figs. 4, 12, 15, 18).

![](images/efb70fb6be100406c18e6e003b3f2c459d946af6132b07d29472354ce4e5c8b4.jpg)  
Fig. 3. Journal distribution.

In the second stage, the study branched out to other domains to cover more techniques under the categorisations defined in the first stage, and included literature on machine selection, location selection, ERP system selection, project selection and technology selection. The topics were selected according to the number of articles using fuzzy AHP in the review paper by Kubler et al. (2016) and complemented by other important topics in industry including evaluation, management and diagnosis. Compared with supplier selection, fewer articles apply fuzzy AHP to rank the alternatives. Almost all the techniques in the selected 52 articles are covered by the review results of the first stage except the defuzzification method proposed by Opricovic and Tzeng (2003), which is problematic as discussed in Section 6.1.3. In addition, Mirhedayatian, Jelodar, Adnani, Akbarnejad, and Saen (2013) propose a different fuzzy programming model to calculate the weights and measure the consistency for selecting the best tunnel ventilation system.

The study targeted journals in four main library databases, i.e. ScienceDirect, Springer, Taylor & Francis and EBSCOhost. Some of the journals cited in this review are Applied Mathematical Modelling, Applied soft computing, Computers & Industrial Engineering, Energy, European Journal of Operational Research, Expert Systems with Applications, International Journal of Production Economics, International Journal of Production Research and Journal of Intelligent & Fuzzy Systems. Articles were searched with keywords ‘FAHP/Fuzzy AHP/Fuzzy Analytic Hierarchy Process’. They were screened according to three criteria:

it was published after 2008;

<sup></sup> fuzzy AHP is used partially (for criteria weights) or completely (for both criteria weights and alternative priorities) in the evaluation process;

it presents clearly how fuzzy AHP is developed or applied.

In total, 109 articles were selected. Fig. 3 shows the distribution of these articles across the journals (the number of the selected articles is presented after the journal name). During the review, the original papers and highly cited papers were also looked back.

Tables A.9 and A.10 in the appendix summarise the literature on supplier selection and the other topics respectively. The column of ‘With methods’ shows the methods fuzzy AHP is combined with, if there are any. The rest of the tables follows the structure of this paper. ‘-’ means ‘not applicable’.

## 4. Representation for pairwise comparison

It is the fundamental step of building a fuzzy AHP model to establish the pairwise comparison matrix with the expert’s judgement. Linguistic terms describe the relative importance of a criterion or an alternative over another (e.g. ‘equally preferred’, ‘fairly strongly preferred’ and ‘absolutely preferred’). In fuzzy AHP, such a term is represented by a fuzzy set which consists of two components, a set of elements x and an associated membership function x (Klir & Yuan, 1995). The membership function assigns to each l<sub>element a value between 0 and 1 as its membership degree to the</sub> set. The mappings between the fuzzy set and the linguistic term must conform to a scale so that the same judgement produces the same measurable value. Such a scale is called fuzzy scale. Fig. 4 outlines the structure of this section. Different types of fuzzy sets are explained by referring to the application context.

## 4.1. Type-1 fuzzy set

The fuzzy set described by a set of elements and crisp values as their membership degrees is called type-1 fuzzy set. A crisp number can be fuzzified. For example, 2 is definitely close to itself, so its membership degree to ‘approximate 2 is 1. If 1.5 is considered neither close nor far to 2, 0.5 can be assigned as its membership degree to ‘approximate 2 . A series of such numbers with their membership degrees compose a fuzzy set ‘approximate 2 , denoted as 2. Let 2 describe ‘moderate importance’ of one criterion over another in AHP. In fuzzy AHP 2 replaces 2. Including a series of numbers addresses the problems that experts in some cases are unable to assign an exact number to the judgement. Their memberships indicate to what extent the experts are sure about the numbers to be used for the judgement. Mathematically, a fuzzy number is a convex normalised fuzzy set of the real line such that its associate membership function is piecewise continuous (Zimmermann, 2001). Because complicated fuzzy numbers may cause important difficulties in data processing such as hard to define arithmetic operations, several simple and representative fuzzy numbers have been proposed (Yeh, 2008, 2017; Ban & Coroianu, 2012;). Triangular fuzzy number (TFN) and trapezoidal fuzzy number (TraFN) are two kinds of such fuzzy numbers that have been well studied.

![](images/031e7ec043514e6b0070987f314e654fbba263339d670adcc2fd55523de8ae66.jpg)  
Fig. 4. Categorisation of the judgement representations.

TFN is the mostly popular means of judgement representation in the reviewed articles (99 out of the 109 articles, i.e. 91%). A TFN $\widetilde { A }$ can be expressed as a triple l; m; h where l and h are the <sup>ð Þ</sup>smallest and the largest values with the smallest membership respectively and m is the value with the largest membership. The membership function of a TFN is defined as follows and illustrated in Fig. 5(a).

$$
\mu (x) = \left\{ \begin{array}{l l} (x - l) / (m - l), & l \leqslant x \leqslant m \\ (h - x) / (h - m), & \mathrm{m} \leqslant x \leqslant h \end{array} \right.\tag{2}
$$

The a-cut set of a fuzzy set ${ \widetilde { A } } ,$ , denoted as $\widetilde { A } _ { \alpha }$ , is a crisp value set <sup>a</sup>containing all the elements with membership degrees greater than or equal to the specified value of a:

$$
\widetilde {A} _ {\alpha} = \{x | \mu (x) \geqslant \alpha \}\tag{3}
$$

The a-cut set of a TFN can be represented as an interval, i.e. $\widetilde { A } _ { \alpha } = [ l + ( m - l ) \alpha , h - ( h - m ) \alpha ]$ shown in Fig. 5 (b). It helps defuz-<sup>a ¼ ½ þ ð</sup>zify a TFN.

TFN is useful when the expert is definitive about a single point representing the total belongingness. For example, if $3 0 ^ { \circ } C$ is considered as a definitely high temperature, slightly below it is hot but not so hot and above it is also hot but too hot, then TFN describes this judgement $( { \mathrm { i . e . } } m = 3 0 ^ { \circ } { \mathsf { C } } )$ . But if the expert is certain within an interval, such as any temperature between 28 and $3 2 ^ { \circ } \mathsf C$ is considered as a definitely high temperature while below 28 $^ \circ \mathsf { C }$ is hot but not so hot and above 32 C is also hot but too hot, then TraFN is needed. It is characterised by a quadruple $( l , m _ { l } , m _ { h } , h )$ as shown in Fig. 6. In the example, $m _ { l } = 2 8 { } ^ { \circ } { \mathrm { C } }$ and $m _ { h } = 3 2 ~ ^ { \circ } C$ . When $m _ { l } = m _ { h } ,$ a TraFN reduces to a TFN. Sometimes, there is a mixed use of TFN and TraFN, for example, Aydin and Kahraman (2010).

## 4.2. Type-2 fuzzy set

The membership space of type-1 fuzzy set is assumed to be the space of real numbers. A natural extension is the definition of type-2 fuzzy set whose membership values are type-1 fuzzy sets rather than real numbers (Zimmermann, 2001). Type-2 fuzzy set captures more imprecision because it expresses the imprecision on both the elements and their memberships. It helps when the expert is not sure about the membership of an element to a set. A type-2 fuzzy set $\widetilde { \widetilde { A } }$ in the universe set X is defined as follows (Mendel & John, 2002):

$$
\widetilde {\widetilde {A}} = \{((x, u), \mu (x, u)) | \forall x \in X, \forall u \in J _ {x} \subseteq [ 0, 1 ], 0 \leqslant \mu (x, u) \leqslant 1 \}\tag{4}
$$

![](images/6e16596aaa3f718fcd7029c9b05b11ef336b2a4f6bfe8a8dda88a2bb605afcc6.jpg)  
Fig. 5. (a) A TFN, A; (b) a-cut of a TFN $\widetilde { A } _ { \alpha }$

![](images/8b03a089b6048a819b9f9be2c8c84e34fa4a91d1e5c867929aea9976f0500da6.jpg)  
Fig. 6. A trapezoidal fuzzy number

where x is the element, u is a primary membership degree of x and $J _ { x }$ is the value set of u under x. $\mu ( x , u )$ is called the secondary memberlð Þ<sub>ship function, which is a type-1 fuzzy set. Fig. 7 depicts</sub> $\mu ( x , u )$ for x and u where $X = ( 1 , 2 , 3 , 4 , 5 )$ and $U = \{ 0 , 0 . 2 , 0 . 4 , 0 . 6 , 0 . 8 \}$ <sup>Þ</sup>. Each of the rods represents $\mu ( x , u )$ at a specific pair $( x , u ) .$ For example, lð Þ<sub>the length of the rod for (2, 0) is 0.5 in Fig. 7, which means</sub> $\mu ( 2$ $0 ) = 0 . \ J _ { 1 } = J _ { 2 } = J _ { 4 } = J _ { 5 } = \{ 0 , \ 0 . 2 , \ 0 . 4 , \ 0 . 6 , \ 0 . 8 \}$ and $J _ { 3 } = \{ 0 . 6 , 0 . 8 \}$ l<sub>. An</sub> example of the secondary membership function at x = 2 is:

$$
\mu (2, u) = \{(2, 0), 0. 5; (2, 0. 2), 0. 3 5; (2, 0. 4), 0. 3 5; (2, 0. 6), 0. 2; (2, 0. 8), 0. 5 \}
$$

The union of the five secondary membership functions at $x = 1$ 2, 3, 4, 5 is $\mu ( x , u )$ of the set.

l<sub>In the above example, the complexity of operations is accept-</sub> able because it is a small discrete set where the elements are finite. For a continuous set, the computation becomes extremely difficult and even its literal description is problematic. Take for example the continuous type-2 fuzzy set defined on [1, 5] in Fig. 8(a). The shadow illustrates the membership function (x,u) which is hardly l<sub>described in formulas. But in the case of all (x,u) = 1, this 3-</sub> l<sub>dimensional set becomes a 2-dimensional set on axes x and u as</sub> shown in Fig. 8(b), the complexity of which reduces greatly. This special type-2 fuzzy set is called interval type-2 fuzzy set. It is the most widely used type-2 fuzzy set because this special kind is relative simple and it is also very difficult to justify the use of any other kind (Mendel & John, 2002).

![](images/2868b774057b4cfb033b28f6d872d8e8e921af730cf358395fc65c515c3ce13d.jpg)  
Fig. 7. Example of a type-2 membership function, adapted from (Mendel & John, 2002)

![](images/6241faa88275a496b9f94793d62cbd42afd82a2ee7088759586bf861b1169efc.jpg)

The interval type-2 fuzzy set can be further distinguished by the shapes of the membership functions, such as triangular and trapezoidal. The adoption of trapezoidal interval type-2 fuzzy set has been found in the reviewed articles of Görener, Ayvaz, Kusakcı, and Altınok (2017) and Celik and Akyuz (2018). As shown in Fig. 9, a trapezoidal interval type-2 fuzzy set can be characterised by the reference points and the heights of its upper and the lower membership functions. The reference points are the elements whose membership degrees can be used to define the shape of membership functions. The trapezoidal ring in Fig. 9 is the analogue of the U shape plane in Fig. 8 (b). A trapezoidal interval type-2 fuzzy set is defined as:

$$
\begin{array}{l} \widetilde {\widetilde {A}} = \left(\widetilde {A} ^ {U}, \widetilde {A} ^ {L}\right) \\ \qquad = \left(\left(a _ {1} ^ {U}, a _ {2} ^ {U}, a _ {3} ^ {U}, a _ {4} ^ {U}; H _ {1} \left(\widetilde {A} ^ {U}\right), H _ {2} \left(\widetilde {A} ^ {U}\right)\right), \left(a _ {1} ^ {L}, a _ {2} ^ {L}, a _ {3} ^ {L}, a _ {4} ^ {L}; H _ {1} \left(\widetilde {A} ^ {L}\right), H _ {2} \left(\widetilde {A} ^ {L}\right)\right)\right) \end{array}
$$

$\widetilde { A } ^ { U }$ and $\widetilde { A } ^ { L }$ are type-1 fuzzy sets; $a _ { 1 } ^ { U } , a _ { 2 } ^ { U } , a _ { 3 } ^ { U } , a _ { 4 } ^ { U } , a _ { 1 } ^ { L } , a _ { 2 } ^ { L } , a _ { 3 } ^ { L }$ and $a _ { 4 } ^ { L }$ are the reference points; $H _ { i } \Big ( \widetilde { \cal A } ^ { U } \Big )$ is the membership degree of element $a _ { i + 1 } ^ { U }$ in the upper trapezoidal membership function $\widetilde { \boldsymbol { A } } ^ { U } ; H _ { i } \left( \widetilde { \boldsymbol { A } } ^ { L } \right)$ is the membership degree of element $a _ { i + } ^ { L }$ in the lower trapezoidal membership function $\widetilde { A } ^ { L } ; 1 \leqslant i \leqslant 2 , H _ { i } \Bigl ( \widetilde { A } ^ { U } \Bigr ) \in [ 0 , 1 ] , H _ { i } \Bigl ( \widetilde { A } ^ { L } \Bigr ) \in [ 0 , 1 ]$

## 4.3. Intuitionistic fuzzy set

The membership degree in a type-1 fuzzy set indicates to what extent an element belongs to the set. There could correspondingly be a value for the extent that the element does not belong to this set. The belongingness and non-belongingness do not necessarily complement each other because of the imprecision of judgement or the possibility of this element belonging to another set. Intuitionistic fuzzy set proposed by Atanassov (1986) is characterised by two such functions expressing the degree of belongingness and the degree of non-belongingness respectively. Intuitionistic fuzzy set deals with the situation that the membership or the nonmembership cannot be determined to the expert’s satisfaction and an indeterministic part remains (De, Biswas, & Roy, 2000; Grzegorzewski & Mrówka, 2005). An intuitionistic fuzzy set A in the universe of discourse X is a set of ordered triples (Atanassov, 2012):

![](images/2d2b5784535bc669f6ce1cec90b397d1a6c6689e4751ba61f114a0b34d6620c8.jpg)  
Fig. 8. Example of continuous type-2 fuzzy set with: (a) x; u –1 and (b) all (x,u) = 1

![](images/22176e4dfd3455f3e2672d24dc02220a69397103625f09e323f0cf41976a197a.jpg)  
Fig. 9. A trapezoidal interval type-2 fuzzy set

$$
A = \{(x, \mu (x), \nu (x)) | x \in X \}\tag{6}
$$

where $\mu ( x )$ and v(x): X ? [0,1] are the membership function and l<sub>non-membership</sub> <sub>function</sub> <sub>respectively;</sub> $0 \leqslant \mu ( x ) + \nu ( x ) \leqslant 1$ . For <sup>lð Þ þ ð Þ</sup>each A, there is another parameter <sub>p</sub>(x), called the degree of nondeterminacy of the membership of x to the set $ A \colon \pi ( x ) = 1 - \mu ( x )$

<sup>l</sup>v(x). In intuitionistic fuzzy AHP, ( (x), v(x), p(x)) is used to  l<sub>describe the preference degree of one criterion/alternative over</sub> another. Büyüközkan and Güleryüz (2016) choose intuitionistic fuzzy sets to express the linguistics terms.

Cuong (2014) introduces the concept of a picture fuzzy set that extends the intuitionistic fuzzy set by adding a degree of neutral belongingness. A picture fuzzy set A in the universe of discourse X is defined as:

$$
A = \{(x, \mu (x), \eta (x), v (x)) | x \in X \}\tag{7}
$$

where (x), x and $\boldsymbol { \upsilon } ( \boldsymbol { x } ) \colon \boldsymbol { X }  [ 0 , 1 ]$ are degree of positive membership, degree of neutral membership and degree of negative membership respectively. They satisfy the condition: $0 \leqslant \mu ( x ) + \eta ( x ) + \nu ( x ) \leqslant 1 . \pi ( x ) = 1 - \mu ( x ) - \eta ( x ) - \nu ( x )$ is the l g p l g<sub>degree of refusal membership. Models based on picture fuzzy sets</sub> can be applied in the situation when experts have opinions involving more answers such as yes, abstain, no and refusal. An example is voting that the voters may be divided into four groups of those who vote for, abstain, vote against and refusal of the voting (invalid voting or not taking the vote) (Cuong, 2014; Son, 2015). However, due to the lack of mathematical discussions with its aggregation and defuzzification, picture fuzzy sets are hardly applied in constructing pairwise comparison decision matrix. For example, Ju, Ju, Gonzalez, Giannakisc, and Wang (2018) apply picture fuzzy sets for site ranking but still use TFNs to construct the comparison matrix in fuzzy AHP.

## 4.4. Fuzzy scales

A fuzzy set describes a particular linguistic term. A fuzzy scale defined by a series of fuzzy sets depicts the levels of linguistic terms, which links the verbal and numerical expressions. (9)- level and 5-level fuzzy scales for relative importance are commonly adopted (34 and 43 out of the 109 articles respectively) as illustrated in Fig. 10(a) and (b). We take TFNs as example to discuss how literature defines these scales because TFNs are largely applied.

The literature uses different linguistic terms when describing the same scale. For example, Ayhan and Kilic (2015) use ‘equally important’, ‘equally to weakly important’, ‘weakly important’, ‘weakly to fairly important’, ‘fairly important’, ‘fairly to strongly important’, ‘strongly important’, ‘strongly to absolutely important’ and ‘absolutely important’ to describe the 9 levels that correspond to TFNs 1, 2, 3, 4, 5, 6, 7, 8 and 9. Pitchipoo, Venkumar, and Rajakarunakaran (2013) map those TFNS with ‘equally preferred’, ‘equally to moderately preferred’, ‘moderately preferred’, ‘moderately to strongly preferred’, ‘strongly preferred’, ‘strongly to very strongly preferred’, ‘very strongly to extremely preferred’ and ‘extremely preferred’.

![](images/f17633151480b09817e57cf4e1283ce792d02cab3a20656165a9891ad198970c.jpg)

![](images/29ec08085d7d99ce73166274280080499b2f2a53726ca43fab2777d78ab9058e.jpg)

![](images/6d32ef65bd54cc4574c80527c4bf5cf268d0bd9bb4748a06ebdc0e2188c2e625.jpg)  
(b)  
Fig. 10. Fuzzy scale of: (a) 9-level and (b) 5-level

Most researchers define the scales in the way as shown in Fig. 10. Slight differences exist in defining TFNs. The TFN 9 could also be interpreted as (7,9,11) (e.g. Viswanadham and Samvedi (2013)), (8, 9, 10) (e.g. Beikkhakhian, Javanmardi, Karbasian, and Khayambashi (2015), (9, 9, 9) (e.g. Kannan, Khodaverdi, Olfat, Jafarian, and Diabat (2013)) and (9,9,10) (e.g. Taylan, Bafail, Abdulaal, and Kabli (2014)). 1 could also be defined as (0,1,1) (e.g. Taylan et al. (2014)). Some researchers take totally different TFNs. For example, Zimmer et al. (2017) use 1, 1:5, 2:5, 3:5 and 4:5 for the 5 levels. Other scales are also applied, including 6- level and 7-level fuzzy scales. The number after ‘TFN’ in the column of ‘Pairwise’ in Tables A.9 and A.10 indicates the scale used by the article.

## 4.5. Short discussion

When type-1 fuzzy set uses one value to deal with the imprecision of an element belonging to a set, type-2 fuzzy set expresses the imprecision of this imprecision (i.e. the imprecision of the membership degree), and intuitionistic fuzzy set complements this imprecision by adding a non-membership. Type-2 fuzzy set and intuitionistic fuzzy set are considered more capable to capture imprecision. However, their arithmetic operations needed in calculations are more complicated due to the introduction of more parameters in their definitions.

There are no specific choice rules as to which type of fuzzy set should be used. A general guidance is suggested as a tree diagram in Fig. 11.

The proper fuzzy set(s) emerge(s) by answering the subsequent questions. The choice should also consider the properties of the fuzzy sets, as concluded in Table 1. The table shows ‘when’ the fuzzy set is applicable, ‘what’ it describes, ‘how’ it is defined and the complexity of its arithmetic operations.

## 5. Aggregation method

The main purpose of aggregation is to produce appropriate results from the pairwise comparison matrix. This involves methods for: (1) synthesising the decisions of multiple experts and (2)

![](images/a6f1f554023d836d303779fb443524bce047372d8c252d87864887a4d1b8d8e4.jpg)  
Fig. 11. Fuzzy set specification chart

Table 1  
Summary of the fuzzy sets applied in fuzzy AHP.

<table><tr><td>Fuzzy set</td><td>When</td><td>What</td><td>How</td><td>Complexity</td></tr><tr><td>TFN</td><td rowspan="2">The opinions involve answers: partly yes and partly no.</td><td rowspan="2">Describe the imprecision of a crisp number with precise membership.</td><td>Define the upper and lower boundaries and the middle point.</td><td>Simple</td></tr><tr><td>TraFN</td><td>Define the upper and lower boundaries and the two middle points.</td><td>Simple</td></tr><tr><td>Trapezoidal interval type-2 fuzzy set</td><td>The opinions involve quite unsure answers.</td><td>Describe the imprecision of a crisp number with imprecision membership.</td><td>Define the upper and lower boundaries and the two middle points of the upper and lower trapezoidal fuzzy numbers respectively.</td><td>Very complicated</td></tr><tr><td>Intuitionistic fuzzy set</td><td>The opinions involve answers: yes, no and not sure.</td><td>Describe the imprecision of a crisp number with precise membership and precise non-membership.</td><td>Define the degrees of belongingness and non-belongingness.</td><td>Complicated</td></tr></table>

deriving the fuzzy weights of criteria and priorities of alternatives. The methods are further categorised according to the types of fuzzy set as discussed in the previous section. Fig. 12 shows the categorisation of the identified methods annotated by their main characteristics. The strength and weakness of each method is discussed at the end of this section.

## 5.1. Aggregation for group decision

One challenge of using subjective values is that the judgements of different experts could vary. Their opinions need to be aggregated to produce a final result. Let $\left( \mathrm { D M } _ { 1 } , \mathrm { D M } _ { 2 } , . . . , \mathrm { D M } _ { \mathrm { q } } \right)$ be the q experts and $( \mathsf { C } _ { 1 } , \mathsf { C } _ { 2 } , . . . , \mathsf { C } _ { \mathrm { n } } )$ be the n performance criteria. This subsection starts with three techniques for type-1 fuzzy set (mainly for TFN) and then discusses the aggregation for type-2 fuzzy set and intuitionistic fuzzy set.

## 5.1.1. Mean method

Mean methods for fuzzy numbers are based on the mean methods for crisp values. They emphasis ‘average’ among all the judgements. Their underlying principle and operations are simple. Geometric mean and arithmetic mean are two popular ones (25 and 16 respectively out of 44 papers that have considered group decision and applied type-1 fuzzy sets).

Let $\widetilde { C } _ { i j } ^ { ( t ) } = \left( l _ { i j } ^ { ( t ) } , m _ { i j } ^ { ( t ) } , h _ { i j } ^ { ( t ) } \right)$ be a TFN representing the relative importance of $\mathsf { C } _ { \mathrm { i } }$ over $\mathsf { C _ { j } }$ judged by $\mathsf { D M } _ { \mathrm { t } } , \widetilde { C } _ { i j } = \left( l _ { i j } , m _ { i j } , h _ { i j } \right)$ be the aggregated relative importance of $\mathsf { C } _ { \mathrm { i } }$ over $\mathsf { C _ { j } }$ and $\widetilde { w } _ { i }$ be the fuzzy weight of $\mathsf { C } _ { \mathrm { i } } .$ Some research applies geometric mean, for example, Yang, Chiu, Tzeng, and Yeh (2008), Chen and Yang (2011), Kannan et al. (2013) and Zimmer et al. (2017).

$$
\begin{array}{l} \widetilde {C} _ {i j} = (l _ {i j}, m _ {i j}, h _ {i j}) = \left(\prod_ {t = 1} ^ {q} \widetilde {C} _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}} = \left(\widetilde {C} _ {i j} ^ {(1)} \otimes \widetilde {C} _ {i j} ^ {(2)} \otimes \dots \otimes \widetilde {C} _ {i j} ^ {(q)}\right) ^ {\frac {1}{q}} \\ = \left(\left(\prod_ {t = 1} ^ {a} l _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}}, \left(\prod_ {t = 1} ^ {q} m _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}}, \left(\prod_ {t = 1} ^ {q} h _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}}\right) \end{array}\tag{8}
$$

An extension to geometric mean is weighted geometric mean that accommodates the weights of experts. Let $( \alpha _ { 1 , } \alpha _ { 2 , } . . . , \alpha _ { q } )$ be a a a<sub>the exponential weighting vector of the q experts. Weighted geo-</sub> metric mean for the collective relative importance of $\mathsf { C } _ { \mathrm { i } }$ over $\mathsf C _ { \mathrm j }$ or weight of $\mathsf { C } _ { \mathrm { i } }$ is as Eq. (9), where $\widetilde { W } _ { i } ^ { ( q ) }$ is the weight of $\mathsf { C } _ { \mathrm { i } }$ judged by $\mathrm { D M } _ { \mathrm { q } } .$

$$
\begin{array}{l} \widetilde {C} _ {i j} = \left(\widetilde {C} _ {i j} ^ {(1)}\right) ^ {\alpha_ {1}} \otimes \left(\widetilde {C} _ {i j} ^ {(2)}\right) ^ {\alpha_ {2}} \otimes \dots \otimes \left(\widetilde {C} _ {i j} ^ {(q)}\right) ^ {\alpha_ {q}} \textbf {o r} \\ \widetilde {W} _ {i} = \left(\widetilde {W} _ {i} ^ {(1)}\right) ^ {\alpha_ {1}} \otimes \left(\widetilde {W} _ {i} ^ {(2)}\right) ^ {\alpha_ {2}} \otimes \dots \otimes \left(\widetilde {W} _ {i} ^ {(q)}\right) ^ {\alpha_ {q}} \end{array}\tag{9}
$$

With Eq. (9), Ertay, Kahveci, and Tabanli (2011) aggregate the pairwise comparison matrices while Kar (2014, 2015) aggregate the weights calculated from the pairwise comparison matrix of each expert.

Similarly, arithmetic mean (Ayhan & Kilic, 2015; Viswanadham & Samvedi, 2013) and its weighted extension (Büyüközkan, 2012) are as Eqs. (10) and (11) respectively. $( \alpha _ { 1 , } \alpha _ { 2 , } . . . , \alpha _ { q } )$ is the normalised weighting vector.

$$
\widetilde {C} _ {i j} = \frac {1}{q} \left(\widetilde {C} _ {i j} ^ {1} \oplus \widetilde {C} _ {i j} ^ {2} \oplus \dots \oplus \widetilde {C} _ {i j} ^ {q}\right) = \frac {1}{q} \sum_ {t = 1} ^ {q} \widetilde {C} _ {i j} ^ {(t)}\tag{10}
$$

$$
\widetilde {C} _ {i j} = \sum_ {t = 1} ^ {q} \alpha_ {t} \widetilde {C} _ {i j} ^ {(t)}\tag{11}
$$

The two mean methods can also be applied to aggregate TraFNs where the operations are on the quadruples instead of the triples. For example, Eq. (8) is changed to the following form for TraFNs.

$$
\begin{array}{l} \widetilde {C} _ {i j} = (l _ {i j}, m _ {1 i j}, m _ {2 i j}, h _ {i j}) = \left(\prod_ {t = 1} ^ {q} \widetilde {C} _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}} \\ = \left(\widetilde {C} _ {i j} ^ {(1)} \otimes \widetilde {C} _ {i j} ^ {(2)} \otimes \dots \otimes \widetilde {C} _ {i j} ^ {(q)}\right) ^ {\frac {1}{q}} = \left(\prod_ {t = 1} ^ {q} \left(l _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}}, \left(\prod_ {t = 1} ^ {q} m _ {1 i j} ^ {(t)}\right) ^ {\frac {1}{q}}, \left(\prod_ {t = 1} ^ {q} m _ {2 i j} ^ {(t)}\right) ^ {\frac {1}{q}}, \left(\prod_ {t = 1} ^ {q} h _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}}\right) \end{array}\tag{12}
$$

![](images/ebc691e7168ff66206cd1596ed2756cafc0a0d8b961e8ffd9f0491ed3950799e.jpg)  
Fig. 12. Categorisation of the aggregation methods

## 5.1.2. Max-min method

Compared to the mean methods using an average solution, max–min methods extend the aggregated value range by including the ‘worst’ and the ‘best’ judgements. Max and min, as two aggregation operators, choose the largest and smallest values respectively. They decide the upper and lower bounds of the aggregated TFN (h and l in Fig. 5). The middle value m is calculated by geometric mean or arithmetic mean (Awasthi et al., 2018; Prakash & Barua, 2016a). The aggregated TFN $\widetilde { C } _ { i j } = \left( l _ { i j } , m _ { i j } , h _ { i j } \right)$ by max–min with geometric mean is:

$$
\begin{array}{l} h _ {i j} = \max _ {t = 1, 2, \ldots , q} \Big (h _ {i j} ^ {(t)} \Big) \\ m _ {i j} = \left(\prod_ {1} ^ {q} m _ {i j} ^ {(t)}\right) ^ {\frac {1}{q}} \\ l _ {i j} = \min _ {t = 1, 2, \ldots , q} \Big (l _ {i j} ^ {(t)} \Big) \end{array}\tag{13}
$$

The aggregated TFN $\widetilde { C } _ { i j } = \left( l _ { i j } , m _ { i j } , h _ { i j } \right)$ by max–min with arithmetic mean is:

$$
\begin{array}{l} h _ {i j} = \max _ {t = 1, 2, \dots , q} \left(h _ {i j} ^ {(t)}\right) \\ m _ {i j} = \frac {1}{q} \sum_ {t = 1} ^ {q} m _ {i j} ^ {(t)} \\ l _ {i j} = \min _ {t = 1, 2, \dots , q} \left(l _ {i j} ^ {(t)}\right) \end{array}\tag{14}
$$

Chen, Wang, Chen, and Lee (2010) combine multiple crisp values of judgements to a TFN as the aggregated relative importance of $\mathsf { C } _ { \mathrm { i } }$ over ${ \mathsf { C } } _ { \mathrm { j } } .$ Let crisp value $e ^ { ( t ) }$ be the judgement of expert DM . The aggregated result $\widetilde { C } _ { i j } = ( l _ { i j } , m _ { i j } , h _ { i j } )$ is computed as:

$$
\begin{array}{l} h _ {i j} = \max _ {t = 1, 2, \dots , q} \left(e ^ {(t)}\right) \\ l _ {i j} = \min _ {t = 1, 2, \dots , q} \left(e ^ {(t)}\right) \\ m _ {i j} = \left(\frac {1}{h _ {i j} \times l _ {i j}} \prod_ {t = 1} ^ {q} e ^ {(t)}\right) ^ {\frac {1}{q - 2}} \end{array}\tag{15}
$$

The article on this method referred to by Chen et al. (2010) (i.e. Kuo, Chi, and Kao (2002)) computes the middle value with geometric mean rather than with Eq. (15).

## 5.1.3. Method based on consensus degree

A method based on consensus degree is proposed by Chen (1998) to handle trapezoidal fuzzy number (TraFN). Its aggregation principle is similar to weighted arithmetic mean. This method introduces a variable of ‘consensus degree coefficient’ for each expert and multiplies it with the individual judgement instead of weight of expert in weighted arithmetic mean. This variable is a compromise between the weight of expert and the difference of its opinion from the opinions of all the others. The process is as follows.

Step 1: Translate the judgement given by expert $\mathrm { D M } _ { \mathrm { t } }$ into a standardised TraFN characterised by a quadruple $\widetilde { C } ^ { ( t ) } = \left( l ^ { ( t ) } , m _ { 1 } ^ { ( t ) } , m _ { 2 } ^ { ( t ) } , h ^ { ( t ) } \right)$ , where $0 \leqslant l ^ { ( t ) } \leqslant m _ { 1 } ^ { ( t ) } \leqslant m _ { 2 } ^ { ( t ) } \leqslant 1$

Step 2: Calculate the degree of agreement $S \left( \widetilde { C } ^ { ( t ) } , \widetilde { C } ^ { ( j ) } \right)$ of the opinions between each pair of experts DM and DM , where $S \bigg ( \widetilde { C } ^ { ( t ) } , \widetilde { C } ^ { ( j ) } \bigg ) \in [ 0 , 1 ] , 1 \leqslant t \leqslant q , \ 1 \leqslant j \leqslant q .$ ; and t–j. The degree is calculated by Eq. (16). The larger value of $S \left( \widetilde { C } ^ { ( t ) } , \widetilde { C } ^ { ( j ) } \right)$ , the greater the similarity between the two standardised TraFNs.

$$
S \left(\widetilde {C} ^ {(t)}, \widetilde {C} ^ {(j)}\right) = 1 - \frac {\left| l ^ {(t)} - l ^ {(j)} \right| + \left| m _ {1} ^ {(t)} - m _ {1} ^ {(j)} \right| + \left| m _ {2} ^ {(t)} - m _ {2} ^ {(j)} \right| + \left| h ^ {(t)} - h ^ {(j)} \right|}{4}\tag{16}
$$

Step 3: Calculate the average degree of agreement A(DM ) of expert $\mathsf { D M } _ { \mathrm { t } } \left( t = 1 , 2 , . . . , \mathsf { n } \right)$ with all the others.

$$
A (D M _ {t}) = \frac {1}{q - 1} \sum_ {j = 1, j \neq t} ^ {q} S \left(\widetilde {C} ^ {(t)}, \widetilde {C} ^ {(j)}\right)\tag{17}
$$

Step 4: Calculate the relative degree of agreement RA(DM ) of expert DM (t = 1, 2, . . ., n).

$$
R A (D M _ {t}) = \frac {A (D M _ {t})}{\sum_ {t = 1} ^ {q} A (D M _ {t})}\tag{18}
$$

Step 5: Calculate the consensus degree coefficient C(DM ) of expert DM<sub>t</sub> (t = 1, 2, . . ., n).

$$
C (D M _ {t}) = \frac {y _ {1}}{y _ {1} + y _ {2}} \times w _ {D M _ {t}} + \frac {y _ {2}}{y _ {1} + y _ {2}} \times R A (D M _ {t})\tag{19}
$$

$w _ { D M t }$ is the weight of expert $\mathsf { D M } _ { \mathrm { f } } ; \boldsymbol { y } _ { 1 }$ and $y _ { 2 }$ are the weight of the importance of experts and the weight of the relative degree of agreement of experts.

Step 6: Aggregate the fuzzy judgements. The result $\widetilde { C } _ { a g g }$ is:

$$
\widetilde {C} _ {\text { agg }} = C (D M _ {1}) \otimes \widetilde {C} ^ {(1)} \oplus C (D M _ {2}) \otimes \widetilde {C} ^ {(2)} \oplus \dots \oplus C (D M _ {q}) \otimes \widetilde {C} ^ {(q)}\tag{20}
$$

Büyüközkan, Karabulut and Arsenyan (2017) employ this method directly to TFNs without adaptation. They calculate the similarity of two TFNs based on Eq. (16) in the following way.

$$
S \left(\widetilde {C} ^ {(t)}, \widetilde {C} ^ {(j)}\right) = 1 - \frac {\left| l ^ {(t)} - l ^ {(j)} \right| + \left| m ^ {(t)} - m ^ {(j)} \right| + \left| h ^ {(t)} - h ^ {(j)} \right|}{4}\tag{21}
$$

For TFNs, Eq. (16) should be revised as Eq. (22) (Chen & Chen, 2001) rather than Eq. (21).

$$
S \left(\widetilde {C} ^ {t}, \widetilde {C} ^ {j}\right) = 1 - \frac {\left| l ^ {(t)} - l ^ {(j)} \right| + \left| m ^ {(t)} - m ^ {(j)} \right| + \left| h ^ {(t)} - h ^ {(j)} \right|}{3}\tag{22}
$$

## 5.1.4. Fuzzy interval geometric mean

Geometric mean is also applied to type-2 fuzzy set but the calculation process is different from type-1 fuzzy set due to the different arithmetic operations defined on these sets. It seems to be the only aggregation operation defined for trapezoidal interval type-2 fuzzy set and does not involve much calculation effort. Görener et al. (2017) use geometric mean to aggregate the multiple interval type-2 fuzzy sets as the multiple judgements. Let $\widetilde { \tilde { C } } ^ { ( t ) } =$ $\begin{array} { r l r } { \left( \widetilde { \boldsymbol { A } } ^ { U ( t ) } , \widetilde { \boldsymbol { A } } ^ { L ( t ) } \right) } & { = } & { \left( \left( a _ { 1 } ^ { U ( t ) } , a _ { 2 } ^ { U ( t ) } , a _ { 3 } ^ { U ( t ) } , a _ { 4 } ^ { U ( t ) } ; H _ { 1 } \left( \widetilde { \boldsymbol { A } } ^ { U ( t ) } \right) , H _ { 2 } \left( \widetilde { \boldsymbol { A } } ^ { U ( t ) } \right) \right) \right. } \end{array}$ $\biggl ( a _ { 1 } ^ { L ( t ) } , \ a _ { 2 } ^ { L ( t ) } , \ a _ { 3 } ^ { L ( t ) } , \ a _ { 4 } ^ { L ( t ) } ; \ H _ { 1 } \biggl ( \widetilde { A } ^ { L ( t ) } \biggr ) , \ H _ { 2 } \biggl ( \widetilde { A } ^ { L ( t ) } \biggr ) \biggr ) \biggr )$ be the judgement of expert DM . The aggregation result $\widetilde { \widetilde { C } } _ { a g g }$ is:

$$
\widetilde {\widetilde {C}} _ {a g g} = \left(\widetilde {\widetilde {C}} ^ {(1)} \otimes \widetilde {\widetilde {C}} ^ {(2)} \otimes \dots \otimes \widetilde {\widetilde {C}} ^ {(q)}\right) ^ {\frac {1}{q}}\tag{23}
$$

where

$$
\begin{array}{l}\widetilde {\widetilde {C}} ^ {(t)} \otimes \widetilde {\widetilde {C}} ^ {(j)} = \left(\left(a _ {1} ^ {U (t)} \times a _ {1} ^ {U (j)}, a _ {2} ^ {U (t)} \times a _ {2} ^ {U (j)}, a _ {3} ^ {U (t)} \times a _ {3} ^ {U (j)}, a _ {4} ^ {U (t)} \times a _ {4} ^ {U (j)}; \right. \right.\\\left. \min \left(H _ {1} \left(\widetilde {A} ^ {U (t)}\right), H _ {1} \left(\widetilde {A} ^ {U (j)}\right)\right), \min \left(H _ {2} \left(\widetilde {A} ^ {U (t)}, H _ {2} \left(\widetilde {A} ^ {U (j)}\right)\right), \right. \right.\\\left. \right.\left(a _ {1} ^ {L (t)} \times a _ {1} ^ {L (j)}, a _ {2} ^ {L (t)} \times a _ {2} ^ {L (j)}, a _ {3} ^ {L (t)} \times a _ {3} ^ {L (j)}, a _ {4} ^ {L (t)} \times a _ {4} ^ {L (j)}; \min \left(H _ {1} \left(\widetilde {A} ^ {L (t)}\right), \right.\right.\\\left. H _ {1} \left(\widetilde {A} ^ {L (j)}\right)\right), \min \left(H _ {2} \left(\widetilde {A} ^ {L (t)}, H _ {2} \left(\widetilde {A} ^ {L (j)}\right)\right)\right)\\\sqrt [ q ]{\widetilde {\widetilde {C}} ^ {(t)}} = \left(\left(\sqrt [ q ]{a _ {1} ^ {U (t)}}, \sqrt [ q ]{a _ {2} ^ {U (t)}}, \sqrt [ q ]{a _ {3} ^ {U (t)}}, \sqrt [ q ]{a _ {4} ^ {U (t)}}; H _ {1} \left(\widetilde {A} ^ {U (t)}\right), H _ {2} \left(\widetilde {A} ^ {U (t)}\right)\right), \right.\\\left. \left(\sqrt [ q ]{a _ {1} ^ {L (t)}}, \sqrt [ q ]{a _ {2} ^ {L (t)}}, \sqrt [ q ]{a _ {3} ^ {L (t)}}, \sqrt [ q ]{a _ {4} ^ {L (t)}}; H _ {1} \left(\widetilde {A} ^ {L (t)}\right), H _ {2} \left(\widetilde {A} ^ {L (t)}\right)\right)\right)\end{array}\tag{24}
$$

<sub>ð</sub><sup>25</sup><sub>Þ</sub>

## 5.1.5. Intuitionistic fuzzy weighted averaging

Intuitionistic fuzzy weighted averaging (IFWA) includes weighted arithmetic and geometric averaging operators (Xu, 2007). If the weights of experts are equal, the two operators reduce to intuitionistic fuzzy arithmetic and geometric averaging operators. Büyüközkan and Güleryüz (2016) and Büyüközkan, Göçer and Karabulut (2019) apply intuitionistic fuzzy weighted arithmetic averaging operator. Let $C ^ { t } = ( \mu ^ { t } , \nu ^ { t } , \pi ^ { t } )$ be the judgement of expert $\mathrm { D M } _ { \mathrm { t } }$ and $\boldsymbol { \nu } = \left( \alpha _ { 1 , } \mathrm { ~ } \alpha _ { 2 , } \mathrm { ~ } . . . . , \mathrm { ~ } \alpha _ { q } \right)$ p<sub>be the weight vector of the</sub> a a<sub>experts. The aggregation result is</sub> $C _ { a g g } ,$ where

$$
\begin{array}{l} C _ {a g g} = \alpha_ {1} C ^ {(1)} \oplus \alpha_ {2} C ^ {(2)} \oplus \dots \oplus \alpha_ {q} C ^ {(q)} \\ = \left(1 - \prod_ {t = 1} ^ {q} (1 - \mu^ {(t)}) ^ {\alpha_ {t}}, \prod (\nu^ {(t)}) ^ {\alpha_ {t}}, \prod_ {t = 1} ^ {q} (1 - \mu^ {(t)}) ^ {\alpha_ {t}} - \prod (\nu^ {(t)}) ^ {\alpha_ {t}}\right) \end{array}\tag{26}
$$

## 5.2. Aggregation for fuzzy weights/priorities

Aggregation of judgements on a single criterion are usually done as a mean or an average value. By contrast, the methods for the weights of criteria are more varied in that they deal with the judgements on different criteria from the fuzzy pairwise comparison matrix. This section starts with four techniques for the matrix of type-1 fuzzy sets. Let $F = \left[ \widetilde { C } _ { i j } \right] _ { n \times n }$ be a fuzzy pairwise comparison matrix and $( \mathsf { C } _ { 1 } , \mathsf { C } _ { 2 } , . . . , \mathsf { C } _ { \mathrm { n } } )$ be the n performance criteria. $\widetilde { C } _ { i j }$ is the relative importance of $\mathsf { C } _ { \mathrm { i } }$ over ${ \mathsf { C } } _ { \mathrm { j } } .$ We describe the methods with notations related to criteria. The calculation of the alternative priorities is the same.

## 5.2.1. Mean method

Geometric mean is a valid means of synthesising different perspectives and also an approximation to eigenvalues of a matrix. It has been widely used to calculate fuzzy weights, e.g. Yang et al. (2008), Sun (2010), Yu, Goh, and Lin (2012), Kar (2014) and Görener et al. (2017). It is immune to the problem of rank reversal and independent on order of operations (Barzilai, 1997). The ‘mean’ value by geometric operation is then normalised to generate the fuzzy weight of a criterion, as shown in Eq. (27).

$$
\begin{array}{l} \widetilde {C} _ {i} = \left(\widetilde {C} _ {i 1} \otimes \widetilde {C} _ {i 2} \otimes \dots \otimes \widetilde {C} _ {i n}\right) ^ {\frac {1}{n}} \\ \widetilde {W} _ {i} = \frac {\widetilde {C} _ {i}}{\sum_ {j = 1} ^ {n} \widetilde {C} _ {j}} \end{array}\tag{27}
$$

Rezaei and Ortt (2013) and Chen et al. (2010) apply arithmetic mean as Eq. (28). It is also utilised in Extent Analysis Method (EAM) to get the fuzzy weights. Some research obtains the weights by applying row sums and then normalising the sums instead of averaging, which is also a simple and convenient methods, for example, Calabrese et al. (2016; 2019).

$$
\begin{array}{l} \widetilde {C} _ {i} = \frac {1}{n} \left(\widetilde {C} _ {i 1} \oplus \widetilde {C} _ {i 2} \oplus \dots \oplus \widetilde {C} _ {i n}\right) \\ \widetilde {W} _ {i} = \frac {\widetilde {C} _ {i}}{\sum_ {j = 1} ^ {n} \widetilde {C} _ {j}} \end{array}\tag{28}
$$

Another method in this group is fuzzy logarithmic least-squares method proposed by van Laarhoven and Pedrycz (1983). It is grouped in mean methods because geometric mean is considered by researchers for example, Büyüközkan (2012), as one optimal solution to this programming problem. However, the weights estimated by logarithmic least-squares might not be valid fuzzy numbers (Csutora & Buckley, 2001). In other words, it can produce fuzzy weight $\widetilde { W } = ( l , m , h )$ with $h < l . ~ c _ { i j }$ is the entry of the pairwise <sup>¼ ð Þ</sup>comparison matrix and w is the weight of criteria i. The method is:

$$
\min _ {w} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\ln c _ {i j} - \left(\ln w _ {i} - \ln w _ {j}\right)\right) ^ {2}\tag{29}
$$

Subject to

$$
\prod_ {i = 1} ^ {n} w _ {i} = 1, w _ {i} > 0, 1 \leqslant i \leqslant n
$$

With regards to the capability of processing size of the matrix, fuzzification level and inconsistency, fuzzy logarithmic leastsquares has the best overall performance, followed by geometric mean and then arithmetic mean (Ahmed & Kilic, 2018).

## 5.2.2. Lambda-max method

The lambda-max method proposed by Csutora and Buckley (2001) transforms the fuzzy comparison matrix into three crisp comparison matrices through the a-cut of a TFN, and then calculates the fuzzy weights. This method directly fuzzifies Saaty’s <sup>k</sup>method (eigenvector method) and reduces the fuzziness in the final fuzzy weights. It can also handle any type-1 fuzzy number used for pairwise comparison. Compared with mean method, it is complicated due to the multiple steps involving calculating eigenvalues, minimising the fuzziness, adjusting the boundaries of the weights. Wang, Cheng, and Huang (2009) apply this method in their fuzzy AHP model. It has the following steps. As introduced in Section 4.1, the a-cut of a TFN $\widetilde { C } _ { i j } = \left( l _ { i j } , m _ { i j } , h _ { i j } \right)$ can be represented as $\widetilde { C } _ { i j x } = \left[ l _ { i j } + \left( m _ { i j } - l _ { i j } \right) \alpha , h _ { i j } - \left( h _ { i j } - m _ { i j } \right) \alpha \right]$

Step 1: Set a = 1. The middle value of each entry of the fuzzy pairwise comparison matrix is $\boldsymbol { F } = \left[ \widetilde { C } _ { i j } \right] _ { n \times n }$ , i.e. $\widetilde { C } _ { i j \alpha = 1 } = m _ { i j } .$ The <sup></sup>corresponding crisp comparison matrix is $F _ { m } = [ m _ { i j } ] _ { \mathrm { n } \times \mathrm { n } } .$ . The middle value of the fuzzy weight of criterion $\mathrm { C } _ { \mathrm { i } } , w _ { i m } ,$ <sup></sup>is calculated by solving Eq. (30). $\lambda _ { \mathrm { { m a x } } }$ is the largest eigenvalue of $F _ { m } .$ $w _ { m }$ is the weight vector, $w _ { m } = ( w _ { 1 m } , w _ { 2 m } , . . . , w _ { n m } ) ^ { \mathrm { T } }$

$$
F _ {m} w _ {m} = \lambda_ {\mathrm{max}} w _ {m}\tag{30}
$$

Step 2: Set ${ \sf { Q } } = \mathbf { 0 } .$ . This calculates the lower and upper bounds of the fuzzy weight of criterion $\mathsf C _ { \mathrm { i } } , \boldsymbol w _ { i l }$ and $w _ { i h } .$ . The two crisp comparison matrices are $\boldsymbol { F } _ { l } = [ l _ { i j } ] _ { \mathrm { n } \times \mathrm { n } }$ and $\begin{array} { r } { F _ { h } = [ h _ { i j } ] _ { \mathrm { n } \times \mathrm { n } } . } \end{array}$ . w and $w _ { h }$ are <sup></sup>the weight vectors generated from $F _ { l }$ and $F _ { u }$ <sup></sup>respectively. The calculation procedure is the same with that of $w _ { m }$ by Eq. (30).

Step 3: Find constants $K _ { l }$ and $K _ { h } .$ They are used to minimise the fuzziness of the weights, which refers to the lengths of the acuts.

$$
\begin{array}{l} K _ {l} = \min \left\{\frac {w _ {i m}}{w _ {i l}} | 1 \leqslant i \leqslant n \right\} \\ K _ {h} = \max \left\{\frac {w _ {i m}}{w _ {i h}} | 1 \leqslant i \leqslant n \right\} \end{array}\tag{31}
$$

Step 4: Use the two constants to adjust the lower and upper bounds of the fuzzy weight of criterion $\mathsf { C } _ { \mathrm { i } }$ obtained in step 2. The adjusted bounds are ${ w _ { i l } } ^ { * }$ and $w _ { i h } ^ { \mathrm { ~ ~ } } { } ^ { * }$

$$
\begin{array}{l} w _ {i l} ^ {*} = K _ {l} w _ {i l} \\ w _ {i h} ^ {*} = K _ {h} w _ {i h} \end{array}\tag{32}
$$

The fuzzy weight of criterion $\mathsf { C } _ { \mathrm { i } }$ is as $\widetilde { W } _ { i } = \left( w _ { i l } ^ { * } , w _ { i m } , w _ { i h } ^ { * } \right)$

## 5.2.3. Eigenvector based on index of optimism

Calculating the eigenvector is the original method to derive weights from the matrix in AHP. This method can be adapted to fuzzy AHP but requires transforming fuzzy values to crisp values. In other words, the fuzzy comparison matrix needs to be transformed to crisp comparison matrix. One common method for this transformation uses a-cut and an index of optimism. Different from Lambda-max method that solely uses a-cut for several crisp matrices, the weights obtained in this manner are crisp values rather than fuzzy numbers. Let $c _ { i j \alpha U }$ and $c _ { i j \alpha L }$ denote the upper and lower bounds of a-cut set $\widetilde { C } _ { i j \alpha }$ , i.e. $\widetilde { C } _ { i j \alpha } = [ { \mathrm { c } } _ { i j \alpha l }$ , c<sub>ij U</sub>]. $\mathbf { C } _ { i j \alpha U }$ indicates an optimistic expert’s point of view towards the priority of criterion $\mathsf { C } _ { \mathrm { i } }$ over ${ \mathsf { C } } _ { \mathrm { j } }$ while ${ \bf C } _ { i j \alpha L }$ is a pessimistic view (Kim & Park, <sup>a</sup>1990). An expert’s attitude may not be purely optimistic or pessimistic, but somewhere in between. Therefore, they are combined with an index of optimism $\mu$ as:

$$
c _ {i j} = \mu c _ {i j \alpha U} + (1 - \mu) c _ {i j \beta L}, \mu \in [ 0, 1 ]\tag{33}
$$

The larger the value of $\dot { \mu }$ is, the higher the degree of optimism is. $c _ { i j }$ l<sub>is also named as degree of satisfaction. The fuzzy comparison</sub> matrix is transformed into a crisp matrix $\boldsymbol { F } = \left[ c _ { i j } \right] _ { \mathrm { n \times n } }$ by Eq. (33). By setting the values of and $\mu$ <sup></sup>(usually set as 0.5 and 0.5), weight a l<sub>calculation turns to finding the eigenvector by</sub> $\mathsf { S a a t y } ^ { \prime } \mathsf { S } \lambda _ { m a x }$ method. <sup>k</sup>The application can be found in Soroor, Tarokh, Khoshalhan, and Sajjadi (2012), Büyüközkan et al. (2017) and Beikkhakhian et al. (2015).

Awasthi et al. (2018) calculate the weights in a similar way that the fuzzy matrix is defuzzified first by Eq. (34) and then the eigenvector is computed. $c _ { i j }$ is the defuzzified value from TFN.

$$
c _ {i j} = \frac {1}{6} \left(l _ {i j} + 4 \times m _ {i j} + h _ {i j}\right)\tag{34}
$$

Pitchipoo et al. (2013) also calculate weights by converting fuzzy numbers into crisp values. They apply centroid method for defuzzification, given in Eq. (35).

$$
\begin{array}{l} \text {Weights (Crisp value)} W _ {i} = \frac {\sum_ {i = 1} ^ {k} D _ {p} ^ {i} \times o ^ {i}}{\sum_ {i = 1} ^ {k} D _ {p} ^ {i}}, \quad \text {where} D _ {p} ^ {i} \\ = \prod_ {i = 1} ^ {n} m _ {l i} \end{array}\tag{35}
$$

![](images/e1c1b8c2478103f100d8646aef7922e567f1127b437ae13e5a796c8ad4047fc4.jpg)  
Fig. 13. Specification chart of aggregation methods for group decisions

k is the number of rules. $O ^ { i }$ is the class generated by rule i (from 0, 1, $\ldots , \operatorname { L - 1 } ) .$ L is the number of classes, n is the number of inputs, and $m _ { l i }$ is the membership grade of feature l in the fuzzy regions that occupy the ith rule. However, it is not clear how the method in

Pitchipoo et al. (2013) actually works without a further explanation on ‘rules’, ‘class’ and ‘inputs’ as well as their mapping with criteria, alternatives and TFNs.

Table 2  
Summary of the aggregation methods for group decisions.

<table><tr><td>Method</td><td>Characteristic</td><td>Complexity</td><td>Extension</td></tr><tr><td>Arithmetic mean</td><td>Emphasis ‘average’. There should be no extreme value due to its sensitivity.</td><td>Very simple, only involving arithmetic addition and division.</td><td>(1) Weighted arithmetic mean by incorporating the weights of experts; (2) intuitionistic fuzzy weighted arithmetic averaging for intuitionistic fuzz sets by adding the weights of experts.</td></tr><tr><td>Geometric mean</td><td>Emphasis ‘average’. It is less affected by extreme value and more suitable to average normalised values. There should be no negative value.</td><td>Very simple, only involving arithmetic multiplication and rooting.</td><td>(1) Weighted geometric mean by incorporating the weights of experts; (2) fuzzy interval geometric mean for interval type-2 fuzzy sets; (3) intuitionistic fuzzy weighted geometric averaging for intuitionistic fuzz sets by adding the weights of experts.</td></tr><tr><td>Max-min method with arithmetic mean</td><td>Include the ‘worst’ and the ‘best’ judgements but introduce more fuzziness due to the enlarged value range. There should be no extreme value.</td><td>Simple, involving arithmetic addition and division, max and min operations.</td><td>-</td></tr><tr><td>Max-min method with geometric mean</td><td>Include the ‘worst’ and the ‘best’ judgements but introduce more fuzziness due to the enlarged value range.</td><td>Simple, involving arithmetic multiplication and rooting, max and min operations.</td><td>Produce a TFN as the aggregated judgement by combining crisp values of the experts’ judgements.</td></tr><tr><td>Method based on Consensus degree</td><td>Consider the distances between the opinions of the experts but assume the weight of the importance of expert and the weight of the relative degree of agreement are known.</td><td>Complicated due to the calculation of degree of agreement.</td><td>-</td></tr></table>

![](images/45e73d41946d4b3f49a53ad41d292b6bde3456dd78efd4c2f6a2c0e6cc20ef7b.jpg)  
Fig. 14. Specification chart of the aggregation methods for weights

Summary of the aggregation methods for weights/priorities.

<table><tr><td>Method</td><td>Principle</td><td>Complexity</td><td>Pros and Cons</td></tr><tr><td>Arithmetic mean</td><td>Row sum divided by n (the number of criteria), which is then normalised.</td><td>Very simple, only involving arithmetic addition and division.</td><td>Perform least in the mean group.</td></tr><tr><td>Geometric mean</td><td>Nth-root of row multiplication, which is then normalised.</td><td>Very simple, only involving arithmetic multiplication and rooting.</td><td>Produce the same weights as Saaty&#x27;s eigenvector method, if the matrix is consistent. Perform better than arithmetic mean.</td></tr><tr><td>Logarithmic least-squares</td><td>A mathematical programming method</td><td>Complicated because it is indeed a programming method but the objective and constraint functions are simple.</td><td>May produce fuzzy weights that are not fuzzy numbers, which could lead to inconsistency. It could generate multiple results as the weight. Perform best in the mean group.</td></tr><tr><td>Lambda-max method</td><td>Transform the fuzzy matrix into multiple crisp matrices by α-cut, and then calculates the fuzzy weights by generating and adjusting the eigenvectors of the crisp matrices.</td><td>A little complicated due to the multiple steps involving calculating eigenvalues, minimising the fuzziness, adjusting the boundaries of the weights.</td><td>Reduce certain fuzziness in the final results; can be applied to all other fuzzy numbers.</td></tr><tr><td>Eigenvector method</td><td>Transform the fuzzy matrix into a crisp matrix and then calculate the crisp weights from the crisp matrix.</td><td>A little complicated, involving defuzzifying the fuzzy matrix and calculating eigenvalue.</td><td>It is worth considering how much this kind of method is about fuzzy AHP since there are no fuzzy weights.</td></tr><tr><td>Fuzzy programming methods</td><td>Iterative algorithms that search every possible value and gradually achieve a solution to a prescribed accuracy.</td><td>Very complicated due to the iterative search and the need of assistant tools to solve the model. The constraint functions are complicated.</td><td>Produce a consistency index while computing the weights.</td></tr></table>

The main principle of the methods based on eigenvector is to transform the fuzzy matrix to a crisp matrix first, so all the defuzzification methods introduced later can be applied here. With the crisp matrix, researchers can also choose geometric mean or arithmetic mean instead of eigenvector to calculate the crisp weights, for example, Balusa and Gorai (2018). However, Csutora and Buckley (2001) argue that this kind of method is not about fuzzy AHP since there are no fuzzy weights.

## 5.2.4. Fuzzy programming method

Fuzzy programming methods are iterative algorithms that search every possible value and gradually achieve a solution to a prescribed accuracy (Luenberger & Ye, 2008). The advantage of programming methods is producing a consistency index while computing the weights. But they require more computational effort than other aggregation methods. Mathematical models have to be established first, and assistant tools like Excel solver are needed to solve the models. Rezaei, Ortt, and Scholten (2013), Rezaei, Fahim, and Tavasszy (2014) use a fuzzy non-linear programming method to derive crisp weights from a fuzzy comparison matrix, which saves the efforts to defuzzify. This method first distinguishes TFNs from their reciprocals and then defines the non-linear model as Eq. (36) where $w _ { i }$ is the weight and is <sup>k</sup>a variable that measures the degree of membership of the fuzzy feasible area (i.e. the height of the intersection region of the fuzzy judgements).

max

s:t:

$$
\begin{array}{l} \left. \begin{array}{l} (m _ {i j} - l _ {i j}) \lambda w _ {j} - w _ {i} + l _ {i j} w _ {j} \leqslant 0, \\ (u _ {i j} - m _ {i j}) \lambda w _ {j} + w _ {i} - u _ {i j} w _ {j} \leqslant 0 \end{array} \right\} \text { for   TFNs } \\ \left. \begin{array}{l} (m _ {j i} - l _ {j i}) \lambda w _ {i} - w _ {j} + l _ {j i} w _ {i} \leqslant 0, \\ (u _ {j i} - m _ {j i}) \lambda w _ {i} + w _ {j} - u _ {j i} w _ {i} \leqslant 0 \end{array} \right\} \text { for   reciprocals } \\ \sum_ {k = 1} ^ {n} w _ {k} = 1, w _ {k} > 0, \\ i = 1,..., n - 1, j = 2,..., n, j > i, k = 1,..., n \end{array}\tag{36}
$$

Solving the problem described in Eq. (36) results in the optimal crisp weight vector $\ b { \mathsf { W } } ^ { * }$ and $\lambda ^ { * } , \lambda ^ { * } > 0$ indicates that all solution <sup>k k</sup>ratios approximately satisfy the fuzzy judgement, i.e. $l _ { i j } { \widetilde \leqslant } \Big ( w _ { i } ^ { \ast } / w _ { j } ^ { \ast } \Big ) { \widetilde \leqslant } u _ { i j } .$ . It means that the pairwise comparisons are approximately consistent. $\lambda ^ { * }$ as a fuzzy consistency index will be <sup>k</sup>discussed in Section 7.2.1. Eq. (36) is an extension to the programming method proposed by Mikhailov and Tsvetinov (2004) in Eq. (62).

Mirhedayatian et al. (2013) develop a programming mode based on Data Envelopment Analysis to calculate the fuzzy weight $\widetilde { W } _ { i } = ( w _ { i l } , w _ { i m } , w _ { i h } )$ as follows:

max t

$$
\begin{array}{l} s. t. w _ {i l}: \sum_ {j = 1} ^ {n} l _ {i j} u _ {j} \geqslant t, \\ w _ {i m}: \sum_ {j = 1} ^ {n} m _ {i j} u _ {j} \geqslant t, \\ w _ {i h}: \sum_ {j = 1} ^ {n} h _ {i j} u _ {j} \geqslant t, \\ \sum_ {j = 1} ^ {n} m _ {i j} u _ {j} \leqslant 1, r = 1,... n, \\ u _ {j} \geqslant \sum_ {j = 1} ^ {n} m _ {i j} u _ {j} / n m _ {i j}, j = 1,..., n \end{array}\tag{37}
$$

## 5.2.5. Fuzzy interval geometric mean and IFWA

Fuzzy interval geometric mean as Eqs. (20) and (21) also calculates the weights from the pairwise comparison matrix of interval type-2 fuzzy sets, for example Celik and Akyuz (2018) and Görener et al. (2017).

Similarly, IFWA operators, introduced in aggregation for group decisions, are also applied to calculate the weights from the matrix of intuitionistic fuzzy sets. The calculation procedure shown in Eq. (22) is used by Büyüközkan et al. (2019).

## 5.3. Short discussion

Various methods are available to aggregate TFNs while few methods exist for interval type-2 and intuitionistic fuzzy sets, which indicates a potential research topic of exploring more applicable aggregation means for the latter two types of fuzzy sets. There are no specific choice rules as to which method should be used for group decisions. Different methods are introduced for different situations. A general guidance is suggested as shown in Fig. 13. The appropriate method(s) emerge(s) by answering the subsequent questions. These methods are also summarised in Table 2 in terms of their characteristics, complexity of the computation and extension (how they can be extended) to help the choice.

It can be seen from Table 2 that the mean methods have wider application because they are easier to implement and produce valid results. The arithmetic mean has been adapted to intuitionistic fuzzy sets and the geometric mean has been adapted to interval type-2 fuzzy sets and intuitionistic fuzzy sets. Arithmetic mean should also be applicable to aggregate interval type-2 fuzzy sets since geometric mean can be expressed as the exponential of the arithmetic mean of logarithms. Max-min method with geometric mean has been used to aggregate crisp values into a TFN while max–min with arithmetic mean should also work. It is worth studying whether and how the mean methods can be extended to other types of fuzzy sets.

The choice as to which method is used for weights/priorities also first depends on the chosen type of fuzzy set. A general guidance is presented in Fig. 14. These methods are summarised in Table 3 in terms of the underlying principle, the complexity of the computation and the pros and cons.

## 6. Defuzzification method

Defuzzification converts the fuzzy results produced by aggregation methods into crisp values. Compared with a fuzzy value, a crisp value is more intuitive and easier for the final comparison because fuzzy sets have partial ordering. As shown in Fig. 15, this section discusses the defuzzification methods for type-1 fuzzy set and then for type-2 and intuitionistic fuzzy sets.

## 6.1. Defuzzification method for type-1 fuzzy set

There are two dominant defuzzification methods applied by researchers, i.e. centroid method and extent analysis method. 33 papers apply the centroid method and 50 paper use the extent analysis method.

## 6.1.1. Centroid method for type-1 fuzzy set

The centroid method, also called as centre of area (COA) or centre of gravity (COG), is the most prevalent defuzzification method (Ross, 2004). The underlying principle is as Eq. (38) where $x ^ { * }$ is the defuzzified value, x indicates the element, and (x) is its associated membership function.

$$
x ^ {*} = \frac {\int \mu (x) x \mathrm{d} x}{\int \mu (x) \mathrm{d} x}\tag{38}
$$

The centroid method can be translated into different forms when defuzzifying a TFN $\widetilde { C } = ( l , m , h )$ . For example, Eq. (39) is <sup>¼ ð Þ</sup>applied by Sun (2010), Yu et al. (2012), Pitchipoo et al. (2013), Rezaei and Ortt (2013), Ayhan and Kilic (2015), Yayla et al. (2015) and Calabrese et al. (2016; 2019).

$$
x ^ {*} = \frac {l + m + h}{3}\tag{39}
$$

Kar (2014, 2015) uses Eq. (40). Awasthi et al. (2018) utilise Eq. (41).

$$
x ^ {*} = \frac {l + 2 m + h}{4}\tag{40}
$$

$$
x ^ {*} = \frac {l + 4 m + h}{6}\tag{41}
$$

Büyüközkan (2012) defuzzify a TFN by taking a-cut set, $\widetilde { C } _ { \alpha } ,$ as shown by Eq. (42).

$$
x ^ {*} = \frac {1}{2} \int_ {0} ^ {1} \left(i n f \widetilde {C} _ {\alpha} + s u p \widetilde {C} _ {\alpha}\right) d \alpha\tag{42}
$$

With the a-cut set $\widetilde { C } _ { \alpha } = [ l + ( m - l ) \alpha , h - ( h - m ) \alpha ] ,$ Eq. (42) can <sup>a ¼</sup>be further transformed as:

$$
\begin{array}{r l} x ^ {*} & = \frac {1}{2} \int_ {0} ^ {1} (l + (m + l) \alpha + h - (h - m) \alpha) \mathrm{d} \alpha = \frac {l + h}{2} + \frac {1}{2} \\ & \times \int_ {0} ^ {1} (2 m - l - h) \alpha d \alpha = \frac {l + 2 m + h}{4} \end{array}\tag{43}
$$

Eq. (43) corresponds to Yager’s approach (Yager, 1981) that analyses the mean of the elements within an interval. It has been proved by Facchinetti, Ricci, and Muzzioli (1998) that this way takes into consideration both the worst and best results arising from a fuzzy number.

## 6.1.2. The extent analysis method

The extent analysis method (EAM), proposed by Chang (1996), aims to calculate the weights and translate TFNs into crisp values in the fuzzy pairwise comparison matrix. Let $F = \left[ \widetilde { C } _ { i j } \right] _ { n \times n }$ be a fuzzy <sup></sup>pairwise comparison matrix. The fuzzy weight of element i is:

![](images/f8dba26a91057a45bc75ca8cd3f5fd4d9aa9955481a007c18e3a1615a529ff22.jpg)  
Fig. 15. Categorisation of the defuzzification method

$$
\widetilde {W} _ {i} = \sum_ {j = 1} ^ {m} \widetilde {C} _ {i j} \otimes \left[ \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \widetilde {C} _ {i j} \right] ^ {- 1}\tag{48}
$$

Eq. (48) is actually the fuzzy arithmetic mean as in Eq. (28). The crisp weight of i is determined as the minimal degree of possibility of its fuzzy weight w being greater than the fuzzy weights of the others. Given two TFNs $\widetilde { A } _ { 1 } = ( l _ { 1 } , m _ { 1 } , h _ { 1 } )$ and $\widetilde { A } _ { 2 } = ( l _ { 2 } , m _ { 2 } , h _ { 2 } )$ as shown in Fig. 16, The degree of possibility of $\widetilde { A } _ { 1 } \geqslant \widetilde { A } _ { 2 }$ is defined as:

$$
V \left(\widetilde {A} _ {2} \geqslant \widetilde {A} _ {1}\right) = h g t \left(\widetilde {A} _ {1} \cap \widetilde {A} _ {2}\right) = \left(l _ {1} - h _ {2}\right) / \left(\left(m _ {2} - h _ {2}\right) - \left(m _ {1} - l _ {1}\right)\right)\tag{49}
$$

The crisp weight of i is then defined by Eq. (50).

w<sub>i</sub>

$$
\begin{array}{r l} & = V \left(\widetilde {A} _ {i} \geqslant \widetilde {A} _ {1}, \widetilde {A} _ {2},..., \widetilde {A} _ {n}\right) \\ & = V \left[ \left(\widetilde {A} _ {i} \geqslant \widetilde {A} _ {1}\right) a n d \left(\widetilde {A} _ {i} \geqslant \widetilde {A} _ {2}\right) a n d \dots a n d \left(\widetilde {A} _ {i} \geqslant \widetilde {A} _ {n}\right) \right] \\ & = \min V \left(\widetilde {A} _ {i} \geqslant \widetilde {A} _ {k}\right), k = 1, 2,.., n, k \neq i \end{array}\tag{50}
$$

EAM is simple to implement but does not produce proper weights. There is a zero assigned when there is no intersection of the two TFNs. Also, the way of calculating is incorrect because it neglects the role of $l _ { 2 }$ and $h _ { 1 }$ in determining the relative importance. This leads to a big inconsistency between the results and the original judgments. Considering EAM is widely applied, we explain how EAM is problematic in details in the short discussion section.

## 6.1.3. Other methods

Opricovic and Tzeng (2003) propose a defuzzification method, namely Converting the Fuzzy data into Crisp Scores (CFCS), which is applied by Sarfaraz, Jenab, and D’Souza (2012) to rank ERP implementation solutions. Let $\boldsymbol { F } = \left[ \widetilde { C } _ { i j } \right] _ { n \times n }$ be a fuzzy pairwise comparison matrix and $( \mathsf { C } _ { 1 } , \mathsf { C } _ { 2 } , . . . , \mathsf { C } _ { \mathrm { n } } )$ <sup></sup>be the n performance criteria. $\widetilde { C } _ { i j } = ( l _ { i j } , m _ { i j } , h _ { i j } ) , j = 1 , 2 , . . . , n$ is the pairwise comparison of $\mathsf { C } _ { \mathrm { i } }$ over ${ \mathsf { C } } _ { \mathrm { j } } .$ The crisp value for each TFN is computed by the following four steps.

Step 1: Normalisation.

$$
h _ {j} ^ {\max} = \max _ {i} h _ {i j}, l _ {j} ^ {\min} = \min _ {i} l _ {i j}, \Delta_ {\min} ^ {\max} = h _ {j} ^ {\max} - l _ {j} ^ {\min}\tag{51}
$$

Normalise the matrix. Let $F = \left[ \widetilde { X } _ { i j } \right] _ { n \times n }$ be the normalised result $; \widetilde { X } _ { i j } = ( x l _ { i j } , x m _ { i j } , x h _ { i j } )$

$$
\begin{array}{l} x l _ {i j} = \left(l _ {i j} - l _ {j} ^ {\min}\right) / \Delta_ {\min} ^ {\max} \\ x m _ {i j} = \left(m _ {i j} - l _ {j} ^ {\min}\right) / \Delta_ {\min} ^ {\max} \\ x h _ {i j} = \left(h _ {i j} - l _ {j} ^ {\min}\right) / \Delta_ {\min} ^ {\max} \end{array}\tag{52}
$$

Step 2: Compute left (ls) and right (hs) normalised values for $\mathbf { i } = 1 , 2 , \ldots \mathbf { n . j } = 1 , 2 , \ldots , \mathbf { n } $

$$
\begin{array}{l} x _ {i j} ^ {l s} = x m _ {i j} / \left(1 + x m _ {i j} - x l _ {i j}\right) \\ x _ {i j} ^ {h s} = x h _ {i j} / \left(1 + x h _ {i j} - x m _ {i j}\right) \end{array}\tag{53}
$$

Step 3: Compute total normalised crisp value.

$$
x _ {i j} ^ {\text { crisp }} = \left[ x _ {i j} ^ {l s} \left(1 - x _ {i j} ^ {l s}\right) + x _ {i j} ^ {h s} x _ {i j} ^ {h s} \right] / \left(1 - x _ {i j} ^ {l s} + x _ {i j} ^ {h s}\right)\tag{54}
$$

Step 4: Compute crisp values. Let $a _ { i j }$ be the crisp value correspondent to $\widetilde { C } _ { i j }$

$$
a _ {i j} = l _ {j} ^ {\mathrm{min}} + x _ {i j} ^ {c r i s p} \Delta_ {\mathrm{min}} ^ {\mathrm{max}}\tag{55}
$$

A major problem of CFCS we have noticed is that it produces varied crisp values for a particular TFN. This is due to the normalisation in step 1. Consider one scenario with 2 criteria and another with 3 criteria. Table 4 shows their comparisons against $\mathsf C _ { 1 }$ . The crisp values for TFN (5, 7, 9) are different in the two scenarios.

Mathematically, defuzzifying a fuzzy set is the process of rounding it off from its location to the nearest vertex, which reduces the set into the most typical or representative value (Ross, 2004). However, CFCS contradicts this principle because the defuzzification result changes as the number of criteria/alternatives changes and also depends on the values of the other TFNs in the comparison matrix. It seems not a suitable defuzzification method.

Mean of limits of a TFN is another method. Alaqeel and Suryanarayanan (2018) apply the geometric mean to the upper and lower limits (i.e. L and h) for a crisp value. This way of defuzzification ignores the middle value of a TFN, which might lead to improper weight.

Index of optimism is also used to defuzzify the fuzzy numbers through their a-cut sets, which has been introduced in Section 5.2.3, for example, Jung (2011), Soroor et al. (2012), Beikkhakhian et al. (2015) and Büyüközkan et al. (2017).

![](images/6d004017236cf21051733a503e4f73d41ead433d9c042e3cf107975c36783d6d.jpg)  
Fig. 16. Fuzzy Triangular Number of $\widetilde { A } _ { 1 }$ and $\widetilde { A } _ { 2 }$

Defuzzification results by CFCS.

<table><tr><td>Criterion</td><td>TFNs</td><td>Normalised fuzzy value</td><td>Crisp value</td></tr><tr><td colspan="4">Scenario 1: 2 criteria</td></tr><tr><td> $C_1$ </td><td>(1, 1, 1)</td><td>(0, 0, 0)</td><td>1</td></tr><tr><td> $C_2$ </td><td>(5, 7, 9)</td><td>(1/2, 3/4, 1)</td><td>6.867</td></tr><tr><td colspan="4">Scenario 2: 3 criteria</td></tr><tr><td> $C_1$ </td><td>(1, 1, 1)</td><td>(0, 0, 0)</td><td>1</td></tr><tr><td> $C_2$ </td><td>(5, 7, 9)</td><td>(4/9, 6/9, 8/9)</td><td>6.916</td></tr><tr><td> $C_3$ </td><td>(6, 8, 10)</td><td>(5/9, 7/9, 1)</td><td>7.86</td></tr></table>

Other applicable defuzzification methods are max membership principle, weighted average and mean of maxima (Ross, 2004) but they are rarely applied in the selection literature.

## 6.2. Centroid method for type-2 fuzzy set

The centroid of an interval type-2 fuzzy set is the union of the centroids of all its embedded type-1 fuzzy sets. Based on this principle, Kahraman, Sari, and Turanog˘lu (2014) propose Eqs. (56) and (57) to defuzzify triangular and trapezoidal interval type-2 fuzzy set.

$$
\begin{array}{l} x _ {T F N} ^ {*} = \frac {\frac {(a _ {3} ^ {U} - a _ {1} ^ {U}) + (a _ {2} ^ {U} - a _ {1} ^ {U})}{3} + a _ {1} ^ {U} + \alpha \left(\frac {(a _ {3} ^ {L} - a _ {1} ^ {L}) + (a _ {2} ^ {L} - a _ {1} ^ {L})}{3} + a _ {1} ^ {L}\right)}{2} \\ x _ {T r a F N} ^ {*} = \frac {\frac {(a _ {4} ^ {U} - a _ {1} ^ {U}) + (H _ {1} (\widetilde {A} ^ {U}) a _ {2} ^ {U} - a _ {1} ^ {U}) + (H _ {2} (\widetilde {A} ^ {U}) a _ {3} ^ {U} - a _ {1} ^ {U})}{4} + a _ {1} ^ {U} + \frac {(a _ {4} ^ {L} - a _ {1} ^ {L}) + (H _ {1} (\widetilde {A} ^ {L}) a _ {2} ^ {L} - a _ {1} ^ {L}) + (H _ {2} (\widetilde {A} ^ {L}) a _ {3} ^ {L} - a _ {1} ^ {L})}{4} + a _ {1} ^ {L}}{2} \end{array} \tag {56}\tag{57}
$$

![](images/81f75c873a7bac2875078278e4bf8bcd2d313d4883ad3ad9662228f352d2de99.jpg)

In Eq. (56), a is the maximum membership degree of the lower membership function; $a _ { 3 } ^ { U }$ and $a _ { 1 } ^ { U }$ are the largest and least possible value of the upper membership function respectively; $a _ { 2 } ^ { \bar { \upsilon } }$ is the most possible (middle) value of the upper membership function; a<sup>L</sup> and a<sup>L</sup> are the largest and least possible value of the lower membership function; a<sup>L</sup> is the middle value of the lower membership function.

In Eq. (57), $H _ { 1 }$ and $H _ { 2 }$ are the two maximum membership degrees; a<sup>U</sup>, a<sup>U</sup> a<sup>U</sup> and a<sup>U</sup> are the largest, the two middle and least possible values of the upper membership function respectively; a<sup>L</sup>, a<sub>3</sub><sup>L</sup> a<sub>2</sub><sup>L</sup> and $a _ { 1 } ^ { L }$ are the largest, the two middle and least possible values of the lower membership function respectively. Celik and Akyuz (2018) and Ayodele, Ogunjuyigbe, Odigiea, and Munda (2018) use this equation in their fuzzy AHP model.

## 6.3. Intuitionistic fuzzy entropy for defuzzification

The defuzzification methods for type-1 and type-2 fuzzy sets transform fuzzy values to representative crisp values. Fuzzy entropy also generates crisp values but measures the fuzziness of the set. Whether it can be considered as a weight is worth considering. Büyüközkan et al. (2019) treats the intuitionistic fuzzy entropy w as the crisp weight value. Let $w _ { i } = \{ \mu _ { i } , \nu _ { i } , \pi _ { i } \}$ be intuitionistic fuzzy weight. Eq. (58) is used to calculate w .

$$
\bar {w} _ {i} = - \frac {1}{n \ln 2} \left[ \mu_ {i} \ln \mu_ {i} + v _ {i} \ln v _ {i} - (1 - \pi_ {i}) \ln (1 - \pi_ {i}) - \pi_ {i} \ln 2 \right]\tag{58}
$$

Büyüközkan et al. (2019) have not provided the reference or proof for this equation. Based on the format of the equation, it might be an extension of Shannon’s function as $\operatorname { E q . }$ (59), which is used to measure the fuzziness of type-1 fuzzy set (Zimmermann, 2001).

![](images/2648ffdc54484be65d3b734afe9ce7a52c4248d7331064324d02bf5c59b2e442.jpg)  
Fig. 17. Two example cases:(a) $m _ { 1 } = m _ { 2 } ; ( { \bf b } )$ m > m but $m _ { 1 } , m _ { 2 } , l _ { 1 }$ , h are very close to each other

Summary of defuzzification methods.

<table><tr><td>Method</td><td>Principle</td><td>Complexity</td><td>Pros and cons</td></tr><tr><td>Centroid method</td><td>Calculate the centre of the area defined by the fuzzy number.</td><td>Very simple (single equation), involving arithmetic addition and division</td><td>Have various forms but Eq. (40) has been well proved. Its application has been extended to type-2 fuzzy set.</td></tr><tr><td>EAM</td><td>Calculate the smallest possibility of one TFN bigger than another as the defuzzified result.</td><td>Simple, involving arithmetic and min operations but having few steps to follow.</td><td>Cannot derive proper crisp weights.</td></tr><tr><td>CFCS</td><td>Calculate the crisp value based on the normalised fuzzy numbers.</td><td>A little complicated, involving arithmetic, min/max, and normalisation operations and having several steps to follow.</td><td>Produce varied crisp values for a particular TFN. It seems not a proper defuzzification method.</td></tr><tr><td>Mean of limits</td><td>Calculate the geometric mean of the upper and lower limits of a TFN.</td><td>Very simple (single equation), involving arithmetic multiplication and rooting.</td><td>Might result in improper results due to ignoring the middle value of a TFN.</td></tr><tr><td>Index of optimism</td><td>Calculate the crisp value based on the α-cut of a TFN and the index of optimism μ.</td><td>Very simple (single equation), involving arithmetic operations.</td><td>The experts need to set values for the two parameters α and μ. But it seems little literature discusses how to set proper values.</td></tr><tr><td>Fuzzy entropy</td><td>Calculate the fuzziness of the fuzzy set.</td><td>Simple (single equation), involving arithmetic and logarithm operations.</td><td>Be used to defuzzify intuitionistic fuzzy set. But fuzzy entropy is used to measure the fuzziness.</td></tr></table>

![](images/41bf1222e4cbdd4407138197268d0f96949bc04c6bf6d620cf146cf115d90e91.jpg)  
Fig. 18. Categorisation of the consistency measurement methods

$$
S (\mu) = - \mu \ln \mu - (1 - \mu) \ln (1 - \mu)\tag{59}
$$

## 6.4. Short discussion

EAM is applied by a large proportion of articles (50 out of the total 109 papers, 46%), which corresponds to the survey results (i.e. 109 out of the 190 papers) by Kubler et al. (2016). However it has been criticised by many researchers for its significant shortcomings in deriving the weights/priorities. Zhu, Jing, and Chang (1999) notice that EAM cannot deal with the comparison if there is no intersection between two fuzzy numbers. This problem is solved by assigning a value of 0 in the case of no intersection and Eq. (49) is extended as:

$$
\begin{array}{l l} V \Big (\widetilde {A} _ {1} \geqslant \widetilde {A} _ {2} \Big) = 1 i f f m _ {1} \geqslant m _ {2} \\ V \Big (\widetilde {A} _ {2} \geqslant \widetilde {A} _ {1} \Big) = \left\{ \begin{array}{l l} (l _ {1} - h _ {2}) / ((m _ {2} - h _ {2}) - (m _ {1} - l _ {1})), & i f l _ {1} \leqslant h _ {2} \\ 0, & o t h e r w i s e. \end{array} \right. \end{array}\tag{60}
$$

Introducing this zero weight leads to some criteria or alternatives being ignored in the analysis and results in a wrong decision (Wang, Luo, & Hua, 2008).

EAM is still inappropriate to attain the relative importance even if every two fuzzy numbers have intersection. Let $\widetilde { A } _ { 1 } = ( l _ { 1 } , m _ { 1 } , h _ { 1 } )$ and $\widetilde { A } _ { 2 } = ( l _ { 2 } , m _ { 2 } , h _ { 2 } )$ be two TFNs. Consider the scenario in Fig. 17 (a) that $m _ { 1 } = m _ { 2 }$ but $l _ { 2 } < l _ { 1 }$ and $h _ { 2 } < h _ { 1 } . \ \widetilde { A } _ { 1 }$ should have a priority above ${ \widetilde { A } } _ { 2 } ,$ but according to Eq. (49), when $m _ { 1 } = m _ { 2 } ,$ $V \Big ( \widetilde { A } _ { 1 } \geqslant \widetilde { A } _ { 2 } \Big ) = V \Big ( \widetilde { A } _ { 2 } \geqslant \widetilde { A } _ { 1 } \Big ) = 1$ that the two TNFs are of the same priority. Consider another case as Fig. 17 (b). $m _ { 2 } = m _ { 1 } + \varepsilon$ where e is a very small positive number close to 0. $h _ { 2 } = m _ { 2 } + \pounds , \ l _ { 1 } = m _ { 1 } - \pounds ,$ $l _ { 2 } = m _ { 2 } + \alpha , h _ { 1 } = m _ { 1 } + \alpha$ , where a is a large positive number. According to Eq. (49), $V \Big ( \widetilde { A } _ { 2 } \geqslant \widetilde { A } _ { 1 } \Big ) = 1 > V \Big ( \widetilde { A } _ { 1 } \geqslant \widetilde { A } _ { 2 } \Big )$ which indicates $\widetilde { A } _ { 2 }$ has a higher priority. However, it is apparent that $\widetilde { A } _ { 1 }$ should be preferred over $\widetilde { A } _ { 2 }$ . The ordinate of the highest intersection in EAM cannot represent the degree of possibility of $\widetilde { A } _ { 2 } \geqslant \widetilde { A } _ { 1 }$ or their relative weights, because it only depends on the two lines defined by $m _ { 2 } ,$ h and $l _ { 1 } , m _ { 1 }$ respectively. Values $l _ { 2 }$ and $h _ { 1 }$ should also play a role to determine the relative importance and neglecting them leads to improper weights. EAM has the advantage of ease of use and simple logic, which might be the reason why it is still widely applied.

It seems that centroid method is the most suitable choice for type-1 and type-2 fuzzy sets as concluded in Table 5.

## 7. Consistency measurement

Consistency measurement ensures that there are limited contradictions among the pairwise comparisons in the matrix. It is a necessary step because a big inconsistency may indicate a lack of understanding of the problem. There are two ways of measuring the consistency of the fuzzy pairwise comparison matrix. ‘Crisp consistency’ is computed by translating the fuzzy matrix to a representative crisp one. ‘Fuzzy consistency’ calculates a consistency index directly from a fuzzy matrix. Fig. 18 outlines the methods.

## 7.1. Crisp consistency

The principle of crisp consistency is to defuzzify the fuzzy matrix first and then use Saaty’s consistency ratio (CR) (see Jung (2011), Kilincci and Onal (2011), Büyüközkan (2012), Pitchipoo et al. (2013), Calabrese et al. (2016; 2019), Büyüközkan et al. (2017) and Ayodele et al. (2018)). The implementation would be different in defuzzification as there are various defuzzification methods as introduced in Section 6. The defuzzified matrix with a CR less than 0.1 is considered as adequately consistent.

$$
\begin{array}{l} C R = C I / R I \\ C I = (\lambda_ {\max} - n) / (n - 1) \end{array}\tag{61}
$$

CI is consistency index; $\lambda _ { m a x }$ is the max eigenvalue of the com-<sup>k</sup>parison matrix; RI is the random index. The value of RI depends on the size of the matrix that can be looked up in Saaty (2008).

Büyüközkan et al. (2019) check the intuitionistic fuzzy matrix by Saaty’s method, but calculate the consistency ratio in the following way:

$$
C R = \left(R I - \frac {\sum \pi_ {i j}}{n}\right) / (n - 1)\tag{62}
$$

where n is the number of the elements and $\pi _ { i j }$ is the degree of nonp<sub>determinacy of the membership. The value of RI is taken from</sub> Saaty’s method. CR is considered acceptable if less than or equal to 0.1. However, they did not explain why the ratio from Eq. (62) works to measure the consistency. It seems that mathematical proof is needed.

## 7.2. Fuzzy consistency

This way of measuring consistency usually requires establishing and solving fuzzy programming models. The consistency index is derived along with the weights of criteria from the models. This section first introduces various programming models starting from the explanation of their origin and then presents a different fuzzy consistency method.

## 7.2.1. Fuzzy programming method

According to Buckley (1985), the fuzzy comparison matrix $F = \left[ \widetilde { A } _ { i j } \right] _ { n \times n }$ is consistent if and only if:

$$
\widetilde {A} _ {i k} \otimes \widetilde {A} _ {k j} \approx \widetilde {A} _ {i j}\tag{63}
$$

The approximate equal $\because$ between two fuzzy numbers $\widetilde { A } _ { 1 }$ and $\widetilde { A } _ { 2 }$ whose membership functions are $\mu _ { A 1 } ( x )$ and $\mu _ { A 2 } ( x )$ is defined as:

$$
\min \left(\nu \left(\widetilde {A} _ {1} \geqslant \widetilde {A} _ {2}\right), \nu \left(\widetilde {A} _ {2} \geqslant \widetilde {A} _ {1}\right)\right) \geqslant \theta\tag{64}
$$

where $\nu \Big ( \widetilde { A } _ { 1 } \geqslant \widetilde { A } _ { 2 } \Big ) = \underset { x \geqslant y } { \operatorname* { s u p } } \big ( \operatorname* { m i n } \big ( \mu _ { A 1 } ( x ) , \mu _ { A 2 } ( y ) \big ) \big )$ and is a fixed positive fraction less than or equal to 1. Literally speaking, $\widetilde { A } _ { 1 }$ and $\widetilde { A } _ { 2 }$ are approximately equal if $\widetilde { A } _ { 1 }$ is not greater than $\widetilde { A } _ { 2 }$ and $\widetilde { A } _ { 2 }$ is not greater than $\widetilde { A } _ { 1 }$

Based on Eq. (63), Arbel (1989) further proves that a fuzzy comparison matrix can be considered as consistent when the ratio of the weight w<sub>i</sub> of criterion $\mathsf { C } _ { \mathrm { i } }$ to the weight w<sub>j</sub> of criterion ${ \mathsf { C } } _ { \mathrm { j } }$ is within the upper and lower bounds of the corresponding TFN $\widetilde { A } _ { i j } = ( l _ { i j } , m _ { i j } , h _ { i j } ) , \mathrm { i . } \epsilon$ .

$$
l _ {i j} \leqslant \left(w _ {i} / w _ {j}\right) \leqslant h _ {i j}\tag{65}
$$

This equation is the base of the following non-linear programming model (Mikhailov & Tsvetinov, 2004). The outcomes of fuzzy programming method provide the optimal crisp weight vector and a consistency index .

$$
\begin{array}{l} \max \lambda \\ s. t. \\ (m _ {i j} - l _ {i j}) \lambda w _ {j} - w _ {i} + l _ {i j} w _ {j} \leqslant 0 \\ (h _ {i j} - m _ {i j}) \lambda w _ {j} + w _ {i} - h _ {i j} w _ {j} \leqslant 0 \\ \sum_ {k = 1} ^ {n} w _ {k} = 1, w _ {k} > 0, \\ i = 1,..., n - 1, j = 2,... n, j > i, k = 1,..., n \end{array}\tag{66}
$$

That the optimal value $\lambda ^ { * } > 0$ means that all solution ratios completely satisfy the fuzzy judgements. A negative value indicates that the judgements are inconsistent.

As discussed by Mikhailov (2004), in inconsistent cases, there does not exist a weight vector that satisfies all inequalities in Eq. (65) simultaneously. But it is reasonable to try to find a vector satisfying all inequalities as well as possible, which introduces ‘approximately less than or equal to’, i.e. $\cdot \tilde { \leqslant } ^ { \prime }$ ’, to Eq. (65).

$$
l _ {i j} \widetilde {\leqslant} (w _ {i} / w _ {j}) \widetilde {\leqslant} h _ {i j}\tag{67}
$$

The following non-linear programming model is then proposed, which adds a tolerance parameter $p _ { i j } .$ This parameter extends the feasible region by extending the lower and upper bounds.

max

$$
\begin{array}{l} s. t. \\ p _ {i j} \lambda w _ {j} + (l _ {i j} - p _ {i j}) w _ {j} - w _ {i} \leqslant 0 \\ p _ {i j} \lambda w _ {j} - (h _ {i j} + p _ {i j}) w _ {j} + w _ {i} \leqslant 0 \\ \sum_ {k = 1} ^ {n} w _ {k} = 1, w _ {k} > 0, \\ i = 1,..., n - 1, j = 2,... n, j > i, k = 1,..., n \end{array}\tag{68}
$$

That the optimal value $\lambda ^ { * } \geq 1$ indicates consistent fuzzy judge-<sup>k </sup>ments. For a weak consistency but the solution ratio is within the extended bounds, $\lambda ^ { * }$ is a value between 1 and 0, depending on the <sup>k</sup>degree of inconsistency and the values of the tolerance parameters. Chen and Yang (2011) use Mikhailov (2004)’s method to examine the consistency. In the first example of Chen and Yang’s paper (i.e. Example 1), a consistency index value 0.7602 is obtained so they consider the comparison matrix consistent. But according to Mikhailov (2004), a value within [0, 1] should be weakly inconsistent.

## 7.2.2. Geometric consistency index

Kar (2014, 2015) apply Geometric consistency index (GCI) to the fuzzy matrix $F = \left[ \widetilde { A } _ { i j } \right] _ { n \times n }$ as Eq. (69):

$$
G C I (F) = \frac {2}{(n - 1) (n - 2)} \sum_ {j > i} ^ {n} \left(\log \left| \widetilde {A} _ {i j} \right| - \left(\log | \widetilde {w} _ {i} | - \log | \widetilde {w} _ {j} |\right) ^ {2}\right)\tag{69}
$$

If $G C I ( F ) \leqslant { \bar { G } } C I$ , the matrix is consistent. $\bar { G C I }$ are fixed values that GCI<sup></sup> = 0.31 for n = 3, GCI<sup></sup> = 0.35 for n = 4 and GCI<sup></sup> = 0.37 for n > 4.

This consistency measure is proposed by Crawford and Williams (1985) for crisp matrix. The thresholds of CGI are determined by Aguarón and Moreno-Jiménez (2003) who provide an interpretation of GCI analogous to the consistency index in AHP proposed by Saaty. It checks the consistency only after the weights of alternatives are obtained. Considering that row geometric mean instead of right eigenvector is used for the prioritisation, the computation efforts do not increase compared with Saaty’s method. The problem when applying this measure to the fuzzy matrix is how to calculate the logarithm of a fuzzy number. Kar (2014, 2015) do not explain this and it seems that crisp values are used though the equation presents fuzzy numbers. There is also a mistake in their used equation (i.e. Eq. (69)) that the square should be placed in the outer bracket as shown in Eq. (70).

$$
G C I (F) = \frac {2}{(n - 1) (n - 2)} \sum_ {j > i} ^ {n} \left(\log \left| \widetilde {A} _ {i j} \right| - \left(\log | \widetilde {w} _ {i} | - \log | \widetilde {w} _ {j} |\right)\right) ^ {2}\tag{70}
$$

## 7.3. Short discussion

Crisp consistency based on Saaty’s method is mostly used and suitable for all types of fuzzy sets. Mahmoudzadeh and Bafandeh (2013) explain why a crisp consistency can represent the consistency of the fuzzy matrix. In the case of calculating a fuzzy inconsistency ratio, they have proved that if the comparison matrix obtained from an $\mathsf { q } = 1$ cut set of $\widetilde { A }$ is consistent, then the original fuzzy comparison matrix is consistent. For a TFN $\widetilde { A } = ( l , m , n )$ , its = 1 cut set reduces to a crisp number, i.e. $A _ { \alpha } = m$ . The consistency check of the fuzzy matrix $F = \left[ \widetilde { A } _ { i j } \right] _ { n \times n }$ becomes the check of the crisp matrix $F _ { \alpha = 1 } = [ m _ { i j } ] _ { n \times n } .$ <sup></sup>Saaty’s consistency ratio then can be used.

Table 6 summarises the methods to measure the consistency in terms of the underlying principle, the complexity of the computation and the pros and cons.

## 8. Conclusion and future research

How the expert’s judgements are represented by fuzzy sets is fundamental to the development of fuzzy AHP. The choice of the fuzzy sets determines the overall calculation complexity of the model. Among the three types of fuzzy sets, type-1 fuzzy set requires the least effort, followed by intuitionistic fuzzy set and interval type-2 fuzzy set. This is because the operations on fuzzy sets are defined via the elements and their memberships, as compared in Table 7.

Aggregation is the key operation to produce the weights/priorities. Different techniques may produce different results and have distinct performance. According to the experimental analysis of Ahmed and Kilic (2018), the logarithmic least-squares method outperforms the fuzzy geometric mean and the fuzzy geometric mean outperforms the fuzzy arithmetic mean. To the best of our knowledge, no comparison has been done between these mean methods and other methods such as lambda-max, which could be a future research topic.

Defuzzification assists the comparison of the results because crisp values are more intuitive than fuzzy values. It also simplifies the calculation if the matrix is defuzzified before computing the weights, which translates a fuzzy matrix into a crisp matrix. The consistency check ensures that the results are produced based on effective judgments since inconsistency may indicate a lack of understanding of the problem.

As indicated in Fig. 1, there is no fixed execution sequence of synthesising multiple judgments, checking consistency, calculating weights/priorities and defuzzifying the fuzzy values. However, the sequence along with the chosen techniques influences the effect of the fuzzy AHP model.

## 8.1. Suggestion on the choice of sequence and technique

This review concludes the techniques used to develop a fuzzy AHP model in the literature. Except the problematic ones (i.e. EAM and $C { \mathrm { F C S } } ) ,$ it is hard to identify which one is the best because each has its advantages and varies in their underlying principles as discussed in the previous sections. Experts could determine according to their practical context. As discussed in Section 4.5, if they are relatively confident in their judgement, then type-1 fuzzy set can be chosen. If preferring a simple but practical tool, they can use geometric mean for aggregation, centroid method for defuzzification and Saaty’s method for consistency measurement. If the experts have good mathematical background and look for more optimal solutions, fuzzy programming method is a nice option. But the following should be avoided when building the fuzzy AHP model.

8.1.1. Using fuzzy arithmetic mean for aggregation and centroid method for defuzzifying when symmetrical TFNs are used for judgement representation.

For a symmetrical TFN ${ \widetilde { C } } _ { i } = ( l _ { i } , m _ { i } , h _ { i } ) ,$ there is $m _ { i } - l _ { i } = h _ { i } - m _ { i } = \Delta _ { i }$ <sup>¼ ð Þ</sup>. Symmetrical TFNs are commonly used to <sup> ¼  ¼</sup>define the fuzzy scales as seen in Section 4.4. Applying fuzzy arithmetic mean as Eq. (10) to such TFNs for aggregation also produces a symmetrical TFN C:

$$
\widetilde {C} = (l, m, h) = \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \left(m _ {i} - \Delta_ {i}\right), \frac {1}{n} \sum_ {i = 1} ^ {n} m _ {i}, \frac {1}{n} \sum_ {i = 1} ^ {n} \left(m _ {i} + \Delta_ {1}\right)\right)
$$

where $\begin{array} { r } { m - l = h - m = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Delta _ { i } , } \end{array}$ n is the number of the TFNs.

Defuzzifying a symmetrical TFN $\widetilde { C } = ( l , m , h )$ by the centroid <sup>¼ ð Þ</sup>method as Eqs. (39), (40) or (41), a crisp value equal to m is obtained.

In this case, if the model is built in the sequence where the TFNs of the pairwise judgements is defuzzified before calculating the weights, the problem of solving a fuzzy AHP model $\widetilde { \boldsymbol { F } } = \left[ \widetilde { C } _ { i j } \right] _ { n \times n } = \left[ \left( l _ { i j } , m _ { i j } , h _ { i j } \right) \right] _ { n \times n }$ reduces to solving an AHP model $F = [ m _ { i j } ] _ { n \times n } .$ The use of a fuzzy scale does not make any sense <sup></sup>because it is equal to the use of crisp scale with the same level.

If the sequence of steps is used where the weights are calculated and then defuzzified, the method will produce the same unnormalised weight vector W with AHP model that calculates the weights by arithmetic mean.

$$
W = \left\{\sum_ {j = 1} ^ {n} m _ {1 j}, \sum_ {j = 1} ^ {n} m _ {2 j}, \dots \sum_ {j = 1} ^ {n} m _ {n j} \right\}
$$

## 8.1.2. Checking the consistency after multiple judgements synthesis.

The inconsistent judgement from an individual expert might be overlooked if checking the consistency after synthesising the multiple judgements. Consider the following two fuzzy comparison matrices $\widetilde { \boldsymbol { F } } _ { 1 }$ and $\widetilde { F } _ { 2 }$ from two experts and their synthesised matrix ${ \widetilde { \cal F } } _ { a g g } .$

$$
\widetilde {F} _ {1} = \left( \begin{array}{c c c} (1, 1, 1) & (2, 3, 4) & (4, 5, 6) \\ (\frac {1}{4}, \frac {1}{3}, \frac {1}{2}) & (1, 1, 1) & (1, 2, 3) \\ (\frac {1}{6}, \frac {1}{5}, \frac {1}{4}) & (\frac {1}{3}, \frac {1}{2}, 1) & (1, 1, 1) \end{array} \right) \widetilde {F} _ {2} = \left( \begin{array}{c c c} (1, 1, 1) & (7, 8, 9) & (1, 2, 3) \\ (\frac {1}{9}, \frac {1}{8}, \frac {1}{7}) & (1, 1, 1) & (1, 1, 1) \\ (\frac {1}{3}, \frac {1}{2}, 1) & (1, 1, 1) & (1, 1, 1) \end{array} \right)
$$

$$
\widetilde {F} _ {a g g} = \left( \begin{array}{c c c} (1, 1, 1) & (3. 7 4, 4. 9 0, 6) & (2, 3. 1 6, 4. 2 4) \\ (0. 1 7, 0. 2 0, 0. 2 7) & (1, 1, 1) & (1, 1. 4 1, 1. 7 3) \\ (0. 2 4, 0. 3 2, 0. 5) & (0. 5 8, 0. 7 1, 1) & (1, 1, 1) \end{array} \right)
$$

After defuzzifying the matrices by the centroid method (Eq. (39)), the consistency is checked using Saaty’s method. The consistency ratios of the three matrices are 0.0036, 0.209 and 0.066 respectively. If the consistency is measured after synthesis, the judgements are considered consistent $( C R _ { _ { F a g g } } { = } 0 . 0 6 6 < 0 . 1 )$ and the weights are calculated based on actually inconsistent judgement from expert $2 \ ( C R _ { _ { F 2 } } = 0 . 2 0 9 > 0 . 1 )$ . The almost perfect consistency from expert $1 \quad ( C R _ { _ { F 1 } } { = } 0 . 0 0 3 6 )$ compensates the big <sup>e</sup>inconsistency from expert 2 via aggregation.

## 8.2. Future work

This section presents some open questions that arise from the review and the discussion of the techniques. We hope these questions could inspire researchers for future work.

## 8.2.1. Open questions on fuzzy scale

There are 5, 6, 7 and 9-level scales that have been applied to describe the relative importance between every two criteria/alternatives. There seems no explanation on the choice of the scale in the research that have applied the fuzzy scale.

Operation comparisons between fuzzy sets.

<table><tr><td>Fuzzy set</td><td>Operation on</td><td>Membership value</td></tr><tr><td>Type-1 fuzzy set</td><td>Element, membership</td><td>Crisp values</td></tr><tr><td>Intuitionistic fuzzy set</td><td>Element, membership, non-membership</td><td>Crisp values</td></tr><tr><td>Type-2 fuzzy set</td><td>Element, membership</td><td>Type-1 fuzzy sets</td></tr></table>

Summary of the methods for consistency measurement

<table><tr><td>Method</td><td>Principle</td><td>Complexity</td><td>Pros and cons</td></tr><tr><td>Saaty&#x27;s method</td><td>Check the consistency of the defuzzified fuzzy matrix by Saaty&#x27;s consistency ratio.</td><td>Simple (simple equations),involving arithmetic operationsand calculation of max eigenvalue of the matrix.</td><td>The choice of defuzzification methods may influence the results since different defuzzification methods could produce different crisp matrices. It is extended to type-2 and intuitionistic fuzzy sets.</td></tr><tr><td>Fuzzy programming method</td><td>Establish the objective and constraint functions based on that the weight ratio of a criterion to another is bounded by the lower and upper limits of the TFN representing their pairwise comparison.</td><td>Very complicated due to the iterative search and the need of assistant tools to solve the model.</td><td>It generates the consistency ratio while producing the weights.</td></tr><tr><td>Geometric consistency index</td><td>Calculate the consistency ratio based on the distance between pairwise comparison and the weight ratio which are taken the logarithm first.</td><td>Simple (simple equations),involving arithmetic and logarithm operations.</td><td>It is hard to apply the equation to fuzzy set because little research has been done for logarithm calculation on fuzzy sets. It checks the consistency after the weights are obtained.</td></tr></table>

Table 8 Summary of the techniques.

<table><tr><td colspan="2"></td><td>Simple</td><td>Complicated</td><td>Very complicated</td></tr><tr><td rowspan="16" colspan="2">Representation for pairwise comparison Aggregation for group decision weights/priorities Defuzzification Consistency</td><td rowspan="16">TFN, TraFN Arithmetic mean, Geometric mean, Max-min method with arithmetic mean, Max-min method with geometric mean Arithmetic mean, Geometric mean, Centroid method, EAM, Mean of limits, Index of optimism, Fuzzy entropy Saaty&#x27;s method, Geometric consistency index</td><td rowspan="16">Intuitionistic fuzzy set Method based on Consensus degree Logarithmic least-squares, Lambda-max method, Eigenvector method CFCS</td><td rowspan="16">Trapezoidal interval type-2 fuzzy set Fuzzy programming method</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

Saaty (2008) discusses that psychologically people are able to distinguish between high, medium and low at one level and for each in a second level below to also distinguish between high, medium and low. This produces nine different categories, where the smallest is (low, low) and the highest is (high, high). This is the principle that AHP has a 9-level scale for the top of pairwise comparisons as compared with the lowest value on the scale. A scale provides a reference for comparison. It is reasonable that other scales exist as long as they cover the spectrum of possibilities and discriminate the alternatives in their application context. Small changes in judgement lead to small changes in the derived weights/priorities (Wilkinson, 1965). When two or more scales are applicable to one problem, for example, supplier selection where the four types of fuzzy scales can be used. Several questions arise:

Q1: Do different scales have different impacts on the final result in terms of accuracy and reliability?

To define a particular expression in the scale, various types of fuzzy sets are used such as type-1 and type-2 fuzzy sets. If using the same type, the choices of the fuzzy numbers by the researchers can also be different. For example, Zimmer et al. (2017) specify ‘moderately important’ with 1:5 while most research adopts 2 in the 5 level scale. The same fuzzy number may also be defined differently. As discussed in Section 4.4, 9 is interpreted as (9, 9, 9) or (8, 9, 10). This leads to the concern:

Q2: What are the impacts on the results if using different fuzzy sets regarding the types, the chosen fuzzy numbers and the definitions on the same scale?

## 8.2.2. Open questions on aggregation

Some aggregation methods accommodate the weights of the experts, which are assumed as known. Experts may have different capabilities since they come from different functional departments, such as purchasing, financing, engineering and quality assurance. People from purchasing have better knowledge to compare the cost related criteria while those from quality assurance are more reliable to analyse the quality related criteria. It is hard to judge which expert overall is more important than another. Two questions arise.

Q3: When experts judge the relative importance between criteria, who judges their importance?

Q4: When people have distinctive expertise, how is their importance judged?

One possible solution is that the experts evaluate the criteria within their capabilities, and those of the same capability are weighted by their experience such as the working years, reputation and position in the department. This brings a new research topic in decision-making.

## 8.2.3. Open questions on consistency

When research focuses on the consistency measurement problem, it seems little attention has been paid to dealing with inconsistency. If the matrix is consistent, then the process continues. Otherwise, the experts need re-compare the criteria/alternatives until the consistency ratio is within the acceptable range. This is the usual solution to adjust the matrix. However, this is still insuf ficient because it is not clear that:

Q5: Which part of matrix needs adjustment?

Q6: How can the inconsistent part be adjusted to meet the condition?

To re-compare the whole matrix consumes effort, especially when the number of criteria/alternatives is large. In addition, recomparison cannot guarantee the consistency of the judgements if the experts have no idea about the adjustment. The answers to the above two questions might help make decision making more efficient.

## 8.3. Concluding remarks

Fuzzy set theory has been proposed as a valid means of dealing with imprecision and vagueness. However, as discussed in Kubler et al. (2016), the extent of benefits brought by introducing this fuzzy paradigm to AHP is not clear, especially given that Saaty (2006) argued that the pairwise judgements are fuzzy enough. Using fuzzy numbers is not only for fuzziness (certain inconsistency among the judgements) but also for ‘uncertainty’ or ‘hesitation’ of the experts towards their judgements. Different types of fuzzy numbers provide choices to express ‘not sure’ to different extents. Although the extent to which fuzzy AHP solves the problem of uncertainty is disputed, it is a simple and useful decisionmaking method that has been widely applied. It retains the advantages of AHP, i.e. structuring the problems, calculating both weights and priorities and well-proved mathematical properties. This paper provided guidance on how to choose appropriate techniques for building fuzzy AHP models in term of representation, aggregation, defuzzification and consistency. In offering the guidance, this research traced the origin of the methods and matched the context to the techniques. The methods are also analysed regarding their characteristics, complexity and extension.

TFN stands out from other types of fuzzy set, because of its simplicity in representing the judgements. It seems able to deal with uncertainty in most cases (applied by 91% of reviewed articles in various fields), but is limited because the degree of membership is expressed as real numbers. In the cases where the decision makers find it difficult to determine the memberships, trapezoidal interval type-2 or intuitionistic fuzzy sets can help. Mean methods are mostly used in aggregating group decisions and deriving weights, for the three reviewed types of fuzzy sets. In particular geometric mean has proved a valid approach of approximating the eigenvalues of a matrix. The fuzzy programming methods are also efficient ways of computing the weights because they also generate a consistency index. But they require more computational effort. Centroid methods are valid means of defuzzifying fuzzy sets, which come in several forms. The one of Eq. (40) is a nice choice, because it considers both the worst and best results arising from a fuzzy number. This equation can also be inferred from Yager’s approach and has been proved by Facchinetti et al. (1998). It is worth mentioning that the EAM is problematic as shown in the discussion but still widely applied because of its ease of use in obtaining the weights and crisp values. This indicates that ‘a simple but practical’ method is what the decision makers need.

![](images/7a748799485ab763c36fe068ef4e781571ce245a7023778703bc13edcb53802b.jpg)  
Fig. 19. Paths of building fuzzy AHP models

Therefore, the reviewed techniques are summarised according to their complexity as listed in Table 8. More properties can be found in Tables 2 and 3 and Tables 5 and 6. It is also noticed that more than half of articles (61 out of 109 articles) do not check the consistency of the pairwise comparison matrix. Consistency measurement is necessary to reduce the contradictions among different decision makers.

Fig. 19 presents the paths with simple and commonly used techniques in the four important aspects of a fuzzy AHP model, starting with the types of fuzzy sets. Figs. 11, 13 and 14 explains which fuzzy set and aggregation methods should be chosen. The appropriate techniques(s) emerge(s) by answering the subsequent questions.

This research has adopted a two-stage approach to examine the fuzzy AHP models used in different decision-making topics in industry. Although many techniques have been reviewed, there may still be ones that have been overlooked. The guidance of this paper could help to categorise and analyse the techniques by reflecting what they describe, when they are applicable, how they are defined and the complexity of the computation.

## Funding

This research was supported by the Natural Science Foundation of Jilin Province of China (Grant No. 20180101035JC) and the Education Department of Jilin Province of China (Grant No. JJKH20200796KJ).

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper

## Appendix

It is noted that the number after the types of fuzzy sets in the column ‘Pairwise’ indicates the levels of the fuzzy scales. For example, ‘TFN 9 means this paper takes a 9-level scale based on TFNs.

Table A.9  
Supplier selection articles with the techniques in their fuzzy AHP models

<table><tr><td rowspan="2"></td><td rowspan="2">Authors</td><td rowspan="2">Industry</td><td rowspan="2">With method(s)</td><td colspan="2">Representation</td><td colspan="2">Aggregation</td><td rowspan="2">Defuzzification</td><td rowspan="2">Consistency</td></tr><tr><td>Pairwise</td><td>Performance</td><td>Weight/Priority</td><td>Multi-experts</td></tr><tr><td>1</td><td>Chan, Kumar, Tiwari, Lau, and Choy (2008)</td><td>Manufacturing</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>2</td><td>Büyüközkan, Feyziog Tu and Nebol (2008)</td><td>e-logistics</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>3</td><td>Yang et al. (2008)</td><td>-</td><td>Non-additive fuzzy measure</td><td>TFN 9</td><td>TFN</td><td>Geometric mean</td><td>Geometric mean</td><td>COA</td><td>-</td></tr><tr><td>4</td><td>Celik, Deha Er and Ozok (2009)</td><td>Maritime</td><td>-</td><td>TFN 5</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>5</td><td>Lee (2009)</td><td>Manufacturing</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>6</td><td>Wang et al. (2009)</td><td>-</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>Lambda-max</td><td>Geometric mean</td><td>-</td><td>Saaty</td></tr><tr><td>7</td><td>Aydin and Kahraman (2010)</td><td>Manufacturing</td><td>-</td><td>TraFN</td><td>-</td><td>Arithmetic mean (defuzzify first)</td><td>Weighted arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>8</td><td>Chen et al. (2010)</td><td>Manufacturing</td><td>-</td><td>TFN 7</td><td>-</td><td>Arithmetic mean</td><td>Max-min for TFN construction &amp; Arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>9</td><td>Chen and Hung (2010)</td><td>Pharmaceutical</td><td>TOPSIS</td><td>TFN 6</td><td>TFN</td><td>Geometric mean</td><td>Arithmetic (alternative)&amp; Geometric mean (criteria)</td><td>-</td><td>Saaty</td></tr><tr><td>10</td><td>Kuo, Lee, and Hu (2010)</td><td>Manufacturing</td><td>DEA</td><td>TFN 5</td><td></td><td>Lambda-max</td><td>Average but not specified</td><td>-</td><td>Saaty</td></tr><tr><td>11</td><td>Şen, Şen, and Başligil (2010)</td><td>Electronic</td><td>Max-min</td><td>TFN 9</td><td>Crisp (criteria weights)</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>12</td><td>Sun (2010)</td><td>-</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td><td>Geometric mean</td><td>-</td><td>COA (but fuzzy values are used)</td><td>-</td></tr><tr><td>13</td><td>Chen and Yang (2011)</td><td>-</td><td>TOPSIS</td><td>TFN 6</td><td>TFN</td><td>Modified EAM</td><td>Geometric mean</td><td>EAM</td><td>FP</td></tr><tr><td>14</td><td>Chiouy, Chou, and Yeh (2011)</td><td>Electronic</td><td>-</td><td>TFN 9</td><td>-</td><td>Lambda-max</td><td>Geometric mean</td><td>-(not specified)</td><td>Saaty</td></tr><tr><td>15</td><td>Ertay et al. (2011)</td><td>Pharmaceutical</td><td>ELECTRE III</td><td>TFN 9</td><td>Crisp</td><td>EAM</td><td>Weighted Geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>16</td><td>Jung (2011)</td><td>Manufacturing</td><td>GP for allocation</td><td>TFN 5</td><td>-</td><td>Geometric mean</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>17</td><td>Kilinci and Onal (2011)</td><td>Manufacturing</td><td>-</td><td>TFN 5</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>Saaty</td></tr><tr><td>18</td><td>Zeydan, Çolpan, and Çobanoğlu (2011)</td><td>Automobile</td><td>TOPSIS</td><td>TFN 9</td><td>TFN 7</td><td>EAM</td><td>Arithmetic mean (for performance, no for criteria)</td><td>-</td><td>Y no method</td></tr><tr><td>19</td><td>Yücenur, Vayvay, and Demirel (2011)</td><td>Logistics</td><td>-</td><td>TFN -(not mention)</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>20</td><td>Büyüközkan (2012)</td><td>Automotive</td><td>TOPSIS</td><td>TFN 11</td><td>TFN</td><td>Geometric mean</td><td>Weighted arithmetic mean</td><td>COA</td><td>Saaty</td></tr><tr><td>21</td><td>Kubat and Yuce (2012)</td><td>-</td><td>GA</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>22</td><td>Shaw, Shankar, Yadav, and Thakur (2012)</td><td>Manufacturing</td><td>LP for allocation</td><td>TFN 9</td><td></td><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>23</td><td>Soroor et al. (2012)</td><td>-</td><td>-</td><td>TFN 9</td><td>-</td><td>Eigenvector based on index of optimism</td><td></td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>24</td><td>Yu et al. (2012)</td><td>Manufacturing</td><td>MP</td><td>TFN -</td><td>-</td><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>25</td><td>Zouggari and Benyoucef (2012)</td><td>-</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>Max-min</td><td>EAM</td><td>Saaty</td></tr><tr><td>26</td><td>Alinezad et al. (2013)</td><td>Pharmaceutical agricultural machinery</td><td>-</td><td>TFN 4</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>27</td><td>Ghorbani, Mohammad Arabzad, and Shahin (2013)</td><td></td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>28</td><td>Kannan et al. (2013)</td><td>Automobile</td><td>TOPSIS MP for allocation</td><td>TFN 9</td><td>TFN 9</td><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>Saaty</td></tr></table>

Table A.9 (continued)

<table><tr><td rowspan="2"></td><td rowspan="2">Authors</td><td rowspan="2">Industry</td><td rowspan="2">With method(s)</td><td colspan="2">Representation</td></tr><tr><td>Pairwise</td><td>Performance</td></tr><tr><td>29</td><td>Pitchipoo et al. (2013)</td><td>electroplating</td><td>GRA</td><td>TFN 9</td><td>-</td></tr><tr><td>30</td><td>Rezaei and Ort (2013)</td><td>food</td><td>-</td><td>TFN 7</td><td>TFN 7</td></tr><tr><td>31</td><td>Roshandel, Miri-Nargesi, and Hatami-Shirkouhi (2013)</td><td>material</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td></tr><tr><td>32</td><td>Viswanadham and Samvedi (2013)</td><td>-</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td></tr><tr><td>33</td><td>Hashemian et al. (2014)</td><td>Diary</td><td>PROMETHEE</td><td>TFN 5</td><td>TFN</td></tr><tr><td>34</td><td>Kar (2014)</td><td>Manufacturing</td><td>MP</td><td>TFN 5</td><td>-</td></tr><tr><td>35</td><td>Rezaei et al. (2014)</td><td>Airline retail</td><td>-</td><td>TFN 9</td><td>-</td></tr><tr><td>36</td><td>Shad, Roghanian and Mojibian (2014)</td><td></td><td>LP</td><td>TFN 5</td><td>TFN</td></tr><tr><td>37</td><td>Ayhan and Kilic (2015)</td><td>Manuf</td><td>MILP for allocation</td><td>TFN 9</td><td>Crisp values</td></tr><tr><td>38</td><td>Beikkhakhian et al. (2015)</td><td>-</td><td>TOPSIS</td><td>TFN 9</td><td>TFN 5</td></tr><tr><td>39</td><td>Kar (2015)</td><td>Manufacturing</td><td>NN for classification</td><td>TFN 5</td><td>crisp</td></tr><tr><td>40</td><td>Sultana, Ahmed, and Azeem (2015)</td><td>Manufacturing</td><td>Delphi, TOPSIS</td><td>TFN 5</td><td>TFN</td></tr><tr><td>41</td><td>Uygun, Kaçamak and Kahraman (2015)</td><td>Communication</td><td>ANP, DEMATEL</td><td>TFN 5</td><td>TFN</td></tr><tr><td>42</td><td>Yayla et al. (2015)</td><td>Logistics</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td></tr><tr><td>43</td><td>Büyüközkan and Güleryüz (2016)</td><td>Automotive</td><td>TOPSIS</td><td>Intuitionistic fuzzy sets</td><td>Intuitionistic fuzzy sets</td></tr><tr><td>44</td><td>Prakash and Barua (2016b)</td><td>Electronic</td><td>VIKOR</td><td>TFN 7</td><td>crisp</td></tr><tr><td>45</td><td>Prakash and Barua (2016a)</td><td>Logistics</td><td>TOPSIS</td><td>TFN 7</td><td>TFN</td></tr><tr><td>46</td><td>Prasannavenkatesan and Goh (2016)</td><td>-</td><td>PROMETHEE</td><td>TFN 5</td><td>TFN</td></tr><tr><td>47</td><td>Shakourloo et al. (2016)</td><td>Manufacturing</td><td>LP for allocation</td><td>TFN 6</td><td>-</td></tr><tr><td>48</td><td>Wang Chen, Chou, Luu and Yu (2016)</td><td>Manufacturing</td><td>TOPSIS</td><td>TFN 6</td><td>TFN</td></tr><tr><td>49</td><td>Büyüközkan et al. (2017)</td><td>RFID service provider</td><td>Fuzzy AD (Axiomatic design)</td><td>TFN 11</td><td>TFN</td></tr><tr><td>50</td><td>Kumar et al. (2017)</td><td>Automobile</td><td>LP</td><td>TFN 9</td><td>TFN</td></tr><tr><td>51</td><td>Görener et al. (2017)</td><td>Airline</td><td>TOPSIS</td><td>Interval type 2 fuzzy set</td><td>Interval type 2 fuzzy set</td></tr><tr><td>52</td><td>Zimmer et al. (2017)</td><td>Automobile</td><td>IO</td><td>TFN 5</td><td>Crisip</td></tr><tr><td>53</td><td>Awasthi et al. (2018)</td><td>electronic</td><td>VIKOR</td><td>TFN 5</td><td>TFN</td></tr><tr><td>54</td><td>Celik and Akyuz (2018)</td><td>Maritime trans</td><td>TOPSIS</td><td>Interval type-2 fuzzy sets</td><td>Interval type-2 fuzzy sets</td></tr><tr><td>55</td><td>Khorasani (2018)</td><td>Service</td><td>Copras</td><td>TFN 9</td><td>TFN</td></tr><tr><td>56</td><td>Liu et al. (2019)</td><td>Agriculture</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td></tr><tr><td>57</td><td>Büyüközkan et al. (2019)</td><td>Chemistry</td><td>VIKOR</td><td>Intuitionistic fuzzy sets</td><td>Intuitionistic fuzzy sets</td></tr></table>

<table><tr><td colspan="2">Aggregation</td><td>Defuzzification</td><td>Consistency</td></tr><tr><td>Weight/Priority</td><td>Multi-experts</td><td></td><td></td></tr><tr><td>Crisp weights by defuzzifying first</td><td>-</td><td>COA</td><td>Saaty</td></tr><tr><td>Arithmetic mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>Arithmetic mean</td><td>Arithmetic mean</td><td>-</td><td>-</td></tr><tr><td>EAM</td><td>Arithmetic mean (in performance)</td><td>EAM</td><td>-</td></tr><tr><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>Geometric mean</td><td>Weighted geometric mean</td><td>COA</td><td>GCI</td></tr><tr><td>FP (non-linear)</td><td>-</td><td>FP</td><td>FP</td></tr><tr><td>Geometric mean</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Geometric mean</td><td>Arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>Eigenvector based on index of optimism</td><td>Geometric mean</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>Geometric mean</td><td>Weighted geometric mean</td><td>COA</td><td>GCI</td></tr><tr><td>EAM</td><td>Geometric mean</td><td>COA</td><td>Saaty</td></tr><tr><td>EAM</td><td>Arithmetic mean</td><td>EAM</td><td>-</td></tr><tr><td>Geometric mean</td><td>-</td><td>COA for BNP</td><td>-</td></tr><tr><td>Weight of a criterion from an individual DM is supposed as being given</td><td>IFWA</td><td>-</td><td>Saaty,</td></tr><tr><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>EAM</td><td>Max-min</td><td>EAM</td><td>-</td></tr><tr><td>EAM</td><td>-</td><td>EAM</td><td>Saaty</td></tr><tr><td>Updated EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>EAM</td><td>Arithmetic mean</td><td>EAM</td><td>-</td></tr><tr><td>Eigenvector based on index of optimism</td><td>Aggregation based on consensus degree</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>Geometric mean</td><td>Geometric mean</td><td>-Fuzzy weights are used</td><td>Saaty</td></tr><tr><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>Saaty</td></tr><tr><td>Eigenvector by defuzzifying first</td><td>Max-min with arithmetic mean</td><td>COA</td><td>Saaty</td></tr><tr><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>Geometric mean</td><td>Geometric mean</td><td>-</td><td>-</td></tr><tr><td>Geometric mean</td><td>Geometric mean</td><td>COA</td><td>Saaty</td></tr><tr><td>IFWA</td><td>IFWA</td><td>Fuzzy entropy</td><td>Saaty</td></tr></table>

Table A.10  
Other selection articles with the techniques in their fuzzy AHP models.

<table><tr><td rowspan="2"></td><td rowspan="2">Authors</td><td rowspan="2">With method(s)</td><td colspan="2">Representation</td><td colspan="2">Aggregation</td><td rowspan="2">Defuzzification</td><td rowspan="2">Consistency</td></tr><tr><td>Pairwise</td><td>Performance</td><td>Weights/ Priorities</td><td>Multi-experts</td></tr><tr><td colspan="9">Machine/tool selection</td></tr><tr><td>1</td><td>Taha and Rostam (2011)</td><td>ANN</td><td>TFN 9</td><td>-</td><td>Eigenvector</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>2</td><td>Yazdani-Chamzini and Yakhchali (2012)</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td><td>EAM</td><td>Arithmetic mean</td><td>EAM</td><td>-</td></tr><tr><td>3</td><td>Ic, Yurdakul, and Dengiz (2013)</td><td>-</td><td>TraFN</td><td>-</td><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>4</td><td>Nguyen et al. (2015)</td><td>COPRAS</td><td>TFN 7</td><td>TFN</td><td>Arithmetic mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>5</td><td>Parameshwaran et al. (2015)</td><td>Delphi and TOPSIS/VIKOR</td><td>TFN 9</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td colspan="9">Location/site selection</td></tr><tr><td>6</td><td>Vahidnia, Alesheikh, and Alimohammadi (2009)</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM/COA/index of optimism</td><td>Saaty</td></tr><tr><td>7</td><td>Choudhary and Shankar (2012)</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>8</td><td>Mosadeghi, Warnken, Tomlinson, and Mirfenderesk (2015)</td><td>-</td><td>TFN scale is not specified</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>9</td><td>Samanlioglu and Ayag (2017)</td><td>PROMETHEE</td><td>TFN 5</td><td>TFN</td><td>Eigenvector</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>10</td><td>Ayodele et al. (2018)</td><td>-</td><td>Interval type 2 fuzzy set</td><td>-</td><td>Geometric mean</td><td>Geometric mean</td><td>COA</td><td>Saaty</td></tr><tr><td>11</td><td>Erbas et al. (2018)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>Geometric mean</td><td>-</td><td>COA</td><td>Saaty</td></tr><tr><td>12</td><td>Ju et al. (2018)</td><td>Grey relational projection</td><td>TFN 6</td><td>Picture fuzzy set</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>13</td><td>Singh et al. (2018)</td><td>-</td><td>TFN 6</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td colspan="9">ERP selection</td></tr><tr><td>14</td><td>Cebeci (2009)</td><td>-</td><td>TFN 5</td><td>-</td><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>15</td><td>Kahraman, Beskese, and Kaya (2010)</td><td>-</td><td>TraFN (fuzzify the judgements first)</td><td>-</td><td>Crisp weights but defuzzify first</td><td>Weighted arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>16</td><td>Onut and Efendigil (2010)</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>17</td><td>Sarfaraz et al. (2012)</td><td>-</td><td>TFN 9</td><td>-</td><td>Crisp weights but defuzzify first</td><td>Geometric mean but defuzzify the decision matrix first</td><td>CFCS</td><td>Saaty</td></tr><tr><td>18</td><td>Kilic,Selimzaim and Delen (2014)</td><td>TOPSIS</td><td>TFN 9</td><td>Crisp value</td><td>Geometric mean</td><td>Arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>19</td><td>Ahmadi, Yeh, Papageorgiou, and Martin. (2015)</td><td>Fuzzy cognitive maps</td><td>TFN 6</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>20</td><td>Efe (2016)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM/COA</td><td>Saaty</td></tr><tr><td colspan="9">Project selection</td></tr><tr><td>21</td><td>Taylan et al. (2014)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>-Mentioned averaging but not specified</td><td>EAM</td><td>-</td></tr><tr><td>22</td><td>Baysal, Kaya, Sarucan, Kahraman, and Engina (2015)</td><td>TOPSIS</td><td>TFN 5</td><td></td><td>Arithmetic mean</td><td>-</td><td>Index of optimism</td><td>-</td></tr><tr><td colspan="9">Technology selection</td></tr><tr><td>23</td><td>Ayag (2010)</td><td>-</td><td>TFN 5</td><td>-</td><td>Eigenvector</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>24</td><td>García-Cascales (2012)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>Arithmetic mean</td><td>-</td><td>-</td><td>-</td></tr><tr><td>25</td><td>Mirhedayatian et al. (2013)</td><td>DEA</td><td>TFN 5</td><td>-</td><td>FP (based on DEA)</td><td>-</td><td>-</td><td>FP</td></tr><tr><td>26</td><td>Avikal, Mishra, and Jain (2014)</td><td>PROMETHEE</td><td>TFN 5</td><td>crisp</td><td>Eigenvector</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>27</td><td>Demirtas, Özgürler, Özgürler, Güneri (2014)</td><td></td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>28</td><td>Tan, Aviso, Huelgas, and Promentilla (2014)</td><td>-</td><td>TFN 5</td><td>-</td><td>FP</td><td>-</td><td>FP</td><td>FP</td></tr><tr><td>29</td><td>Vinodh, Prasanna, and Prakash (2014)</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td>30</td><td>Wang and Wang (2014)</td><td>Kano</td><td>TFN 5</td><td>-</td><td>Eigenvector</td><td>Max-min</td><td>COA</td><td>Saaty</td></tr><tr><td>31</td><td>Budak and Ustundag (2015)</td><td>-</td><td>TFN 5</td><td>-</td><td>Geometric mean</td><td>Arithmetic mean</td><td>COA</td><td>-</td></tr><tr><td>32</td><td>Mahjouri et al. (2017)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>Geometric mean</td><td>Arithmetic mean</td><td>-</td><td>-</td></tr><tr><td>33</td><td>Naderzadeh et al. (2017)</td><td>-</td><td>TFN 5</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>34</td><td>Alaqeel and Suryanarayanan (2018)</td><td>-</td><td>TFN 9</td><td>-</td><td>Eigenvector</td><td>-</td><td>Geometric mean</td><td>Saaty</td></tr><tr><td>35</td><td>Balusa and Gorai (2018)</td><td>-</td><td>TFN 9</td><td>-</td><td>Geometric mean</td><td>-</td><td>Index of optimism</td><td>Saaty</td></tr><tr><td>36</td><td>Canan, Ahmet, and Tekin (2018)</td><td>-</td><td>TraFN</td><td>-</td><td>Geometric mean</td><td>Geometric mean</td><td>COA</td><td>Saaty</td></tr><tr><td>37</td><td>Goyal, Kaushal, and Sangaiah (2018)</td><td>-</td><td>TFN self-defined scale</td><td>-</td><td>FP/EAM</td><td>-</td><td>FP/EAM</td><td>FP</td></tr><tr><td>38</td><td>Wang et al. (2019)</td><td>VIKOR</td><td>TFN (not specified)</td><td>-</td><td>EAM</td><td>Mentioned but not specified</td><td>EAM</td><td>-</td></tr><tr><td>39</td><td>Bostancioglu (2020)</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td colspan="9">Evaluation of engineering sector, teaching performance and health service</td></tr><tr><td>40</td><td>Akkaya et al. (2015)</td><td>MOORA</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>41</td><td>Chen et al. (2015)</td><td>-</td><td>TFN 6</td><td>-</td><td>EAM</td><td>Max-min</td><td>EAM</td><td>Saaty</td></tr><tr><td>42</td><td>Singh and Prasher (2017)</td><td>-</td><td>TFN 5</td><td>-</td><td>Geometric mean</td><td>-</td><td>COA</td><td>-</td></tr><tr><td colspan="9">Management of risk, sustainability, resource and process</td></tr><tr><td>43</td><td>Mangla et al. (2015)</td><td>-</td><td>TFN 9</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>44</td><td>Calabrese et al. (2016)</td><td>-</td><td>TFN 5</td><td>-</td><td>Row sum (similar to arithmetic mean)</td><td>-</td><td>COA</td><td>Saaty</td></tr><tr><td>45</td><td>Calabrese et al. (2019)</td><td>-</td><td>TFN 5</td><td>-</td><td>Row sum (similar to arithmetic mean)</td><td>-</td><td>COA</td><td>Saaty</td></tr><tr><td>46</td><td>Zyoud, Kaufmann, Shaheen, Samhan, and Fuchs-Hanusch (2016)</td><td>TOPSIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>Max-min Arithmetic and geometric mean</td><td>EAM</td><td>-</td></tr><tr><td>47</td><td>Sirisawat and Kiatcharoenpol (2018)</td><td>TOPSIS</td><td>TFN 9</td><td>TFN</td><td>EAM</td><td></td><td>EAM</td><td>-</td></tr><tr><td>48</td><td>Celik and Akyuz (2018)</td><td>TOPSIS</td><td>Interval type 2 fuzzy set</td><td>-</td><td>Geometric mean</td><td>-</td><td>COA</td><td>Saaty</td></tr><tr><td>49</td><td>Khan, Shameem, Kumar, Hussain, and Yan (2019)</td><td>-</td><td>TFN 6</td><td>-</td><td>EAM</td><td>-</td><td>EAM</td><td>Saaty</td></tr><tr><td>50</td><td>Singh and Sarkar (2019)</td><td>TOPSIS</td><td>TFN self-defined scale</td><td>TFN</td><td>EAM</td><td>-</td><td>EAM</td><td>-</td></tr><tr><td>51</td><td>Tavana, Shaabani, Mansouri Mohammadabadi, and Varzgani (2020)</td><td>MOORA</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>Saaty</td></tr><tr><td colspan="9">Diagnosis of diseases</td></tr><tr><td>52</td><td>Nazari, Fallah, Kazemipoor, and Salehipour (2018)</td><td>FIS</td><td>TFN 5</td><td>TFN</td><td>EAM</td><td>Geometric mean</td><td>EAM</td><td>-</td></tr></table>

## References

Aguarón, J., & Moreno-Jiménez, J. M. (2003). The geometric consistency index: Approximated thresholds. European Journal of Operational Research, 147, 137-145

Ahmadi, S., Yeh, C.-H., Papageorgiou, E. I., & Martin, A. R. (2015). An FCM–FAHP approach for managing readiness-relevant activities for ERP implementation. Computers & Industrial Engineering, 88, 501–517.

Ahmed, F., & Kilic, K. (2018). Fuzzy Analytic Hierarchy Process: A performance analysis of various algorithms. Fuzzy Sets and Systems (In press).

Akkaya, G., Turanog˘lu, B., & Öztas, S. (2015). An integrated fuzzy AHP and fuzzy MOORA approach to the problem of industrial engineering sector choosing. Expert Systems with Applications, 42, 9565–9573.

Alaqeel, T. A., & Suryanarayanan, S. (2018). A fuzzy Analytic Hierarchy Process algorithm to prioritize Smart Grid technologies for the Saudi electricity infrastructure, Sustainable Energy, Grids and Networks. 13 122–133.

Alinezad, A., Seif, A., & Esfandiari, N. (2013). Supplier evaluation and selection with QFD and FAHP in a pharmaceutical company. The International Journal of Advanced Manufacturing Technology, 68, 355–364.

Arbel, A. (1989). Approximate articulation of preference and priority derivation. European Journal of Operational Research, 43, 317–326.

Atanassov, K. T. (1986). Intuitionistic fuzzy sets. Fuzzy Sets and Systems, 20, 87–96.

Atanassov, K. T. (2012). On intuitionistic fuzzy sets theory. Berlin: Germany, Springer-Verlag.

Avikal, S., Mishra, P. K., & Jain, R. (2014). A Fuzzy AHP and PROMETHEE methodbased heuristic for disassembly line balancing problems. International Journal of Production Research. 52.1306-1317

Awasthi, A., Govindan, K., & Gold, S. (2018). Multi-tier sustainable global supplier selection using a fuzzy AHP-VIKOR based approach. International Journal of Production Economics, 195, 106–117.

Ayag, Z. (2010). A combined fuzzy AHP-simulation approach to CAD software selection. International Journal of General Systems. 39 731-756

Aydin, S., & Kahraman, C. (2010). Multiattribute supplier selection using fuzzy Analytic Hierarchy Process. International Journal of Computational Intelligence Systems, 3, 553–565.

Ayhan, M. B., & Kilic, H. S. (2015). A two stage approach for supplier selection problem in multi-item/multi-supplier environment with quantity discounts. Computers & Industrial Engineering, 85 1–12

Ayodele, T. R., Ogunjuyigbe, A. S. O., Odigiea, O., & Munda, J. L. (2018). A multicriteria GIS based model for wind farm site selection using interval type-2 fuzzy analytic hierarchy process: The case study of Nigeria. Applied Energy, 228, 1853-1869

Büyüközkan, G., & Güleryüz, S. (2016). A new integrated intuitionistic fuzzy group decision making approach for product development partner selection. Computers & Industrial Engineering, 102, 383–395.

Büyüközkan, G. (2012). An integrated fuzzy multi-criteria group decision-making approach for green supplier evaluation. International Journal of Production Research 50.2892-2909

Büyüközkan, G., Feyziog˘lu, O., & Nebol, E. (2008). Selection of the strategic alliance partner in logistics value chain. International Journal of Production Economics 113, 148–158.

Büyüközkan, G., Karabulut, Y., & Arsenyan, J. (2017). RFID service provider selection: An integrated fuzzy MCDM approach. Measurement, 112, 88–98.

Büyüközkan, G., Göçer, F., & Karabulut, Y. (2019). A new group decision making approach with IF AHP and IF VIKOR for selecting hazardous waste carriers. Measurement, 134

Balusa, B. C., & Gorai, A. K. (2018). Sensitivity analysis of fuzzy-analytic hierarchical process (FAHP) decision-making model in selection of underground metal mining method. Journal of Sustainable Mining (in press).

Ban, A. I., & Coroianu, L. (2012). Nearest interval, triangular and trapezoidal approximation of a fuzzy number preserving ambiguity. International Journal of Approximate Reasoning, 53, 805–836.

Barzilai, J. (1997). Deriving weights from pairwise comparison matrices. Journal of the Operational Research Society, 48, 1226–1232.

Baysal, M. E., Kaya, <sup>\_</sup>I., Sarucan, A., Kahraman, C., & Engina, O. (2015). A two phased fuzzy methodology for selection among municipal projects. Technological and Economic Development of Economy, 21, 405–422.

Beikkhakhian, Y., Javanmardi, M., Karbasian, M., & Khayambashi, B. (2015). The application of ISM model in evaluating agile suppliers selection criteria and ranking suppliers using fuzzy TOPSIS-AHP methods. Expert Systems with Applications, 42, 6224–6236.

Bostancioglu, E. (2020). Double skin façade assessment by fuzzy AHP and comparison with AHP. Architectural Engineering and Design Management, 1–21.

Buckley, J. J. (1985). Fuzzy hierarchical analysis. Fuzzy sets and systems, 17, 233–247.

Budak, A., & Ustundag, A. (2015). Fuzzy decision making model for selection of real time location systems. Applied Soft Computing, 36, 177–184.

Calabrese, A., Costa, R., Levialdi, N., & Menichini, T. (2016). A fuzzy analytic hierarchy process method to support materiality assessment in sustainability reporting. Journal of Cleaner Production, 121, 248–264.

Calabrese, A., Costa, R., Levialdi, N., & Menichini, T. (2019). Integrating sustainability into strategic decision-making: A fuzzy AHP method for the selection of relevant sustainability issues. Technological Forecasting and Social Change, 139, 155–168.

Calabrese, A., Costa, R., & Menichini, T. (2013). Using Fuzzy AHP to manage Intellectual Capital assets: An application to the ICT service industry. Expert Systems with Applications, 40, 3747–3755.

Canan, A., Ahmet, B., & Tekin, T. G. (2018). Sustainability analysis of different hydrogen production options using hesitant fuzzy AHP. International Journal of Hydrogen Energy, 43, 18059–18076.

Cebeci, U. (2009). Fuzzy AHP-based decision support system for selecting ERP systems in textile industry by using balanced scorecard. Expert Systems with Applications, 36, 8900–8909.

Celik, E., & Akyuz, E. (2018). An interval type-2 fuzzy AHP and TOPSIS methods for decision-making problems in maritime transportation engineering: The case of ship loader. Ocean Engineering, 155, 371–381.

Celik, M., Deha Er, I., & Ozok, A. F. (2009). Application of fuzzy extended AHP methodology on shipping registry selection: The case of Turkish maritime industry. Expert Systems with Applications, 36, 190–198.

Yücenur, G. N., Vayvay, Ö., & Demirel, N. Ç. (2011). Supplier selection problem in global supply chains by AHP and ANP approaches under fuzzy environment. The International Journal of Advanced Manufacturing Technology, 56, 823–833.

Chai, J., Liu, J. N. K., & Ngai, E. W. T. (2013). Application of decision-making techniques in supplier selection: A systematic review of literature. Expert Systems with Applications. 40. 3872–3885.

Chan, F. T. S., & Kumar, N. (2007). Global supplier development considering risk factors using fuzzy extended AHP-based approach. Omega, 35, 417–431.

Chan, F. T. S., Kumar, N., Tiwari, M. K., Lau, H. C. W., & Choy, K. L. (2008). Global supplier selection: A fuzzy-AHP approach. International Journal of Production Research, 46, 3825–3857.

Chang, D.-Y. (1996). Applications of the extent analysis method on fuzzy AHP. European journal of operational research, 95, 649–655.

Chen, S. J. & Chen, S. M. (2001). A new method to measure the similarity between fuzzy numbers.

Chen, J.-F., Hsieh, H.-N., & Do, Q. H. (2015). Evaluating teaching performance based on fuzzy AHP and comprehensive evaluation approach. Applied Soft Computing, 28, 100–108.

Chen, L.-H., & Hung, C.-C. (2010). An integrated fuzzy approach for the selection of outsourcing manufacturing partners in pharmaceutical R&D. International Journal of Production Research, 48, 7483–7506.

Chen, S. H., Wang, P. W., Chen, C. M., & Lee, H. T. (2010). An analytic hierarchy process approach with linguistic variables for selection of an R&D strategic alliance partner. Computers & Industrial Engineering, 58, 278–287.

Chen, Z., & Yang, W. (2011). An MAGDM based on constrained FAHP and FTOPSIS and its application to supplier selection. Mathematical and Computer Modelling, 54.2802-2815

Chen, S.-M. (1998). Aggregating fuzzy opinions in the group decision-making environment, Journal of Cybernetics. 29 363–376.

Wang Chen, H. M., Chou, S.-Y., Luu, Q. D., & Yu, T. H.-K. (2016). A fuzzy MCDM approach for green supplier selection from the economic and environmental aspects. Mathematical Problems in Engineering, 2016 1–10

Chiouy, C.-Y., Chou, S.-H., & Yeh, C.-Y. (2011). Using fuzzy AHP in selecting and prioritizing sustainable supplier on CSR for Taiwan s electronics industry. Journal of Information and Optimization Sciences, 32, 1135–1153.

Choudhary, D., & Shankar, R. (2012). An STEEP-fuzzy AHP-TOPSIS framework for evaluation and selection of thermal power plant location. Energy, 42, 510–521.

Crawford, G., & Williams, C. (1985). A note on the analysis of subjective judgment matrices ☆. Journal of Mathematical Psychology. 29. 387–405.

Csutora, R., & Buckley, J. J. (2001). Fuzzy hierarchical analysis: The Lambda-Max method. Fuzzy Sets & Systems, 120, 181–195.

Cuong, B. C. (2014). Picture fuzzy sets. Journal of Computer Science and Cybernetics, 30, 409–420.

De, S. K., Biswas, R., & Roy, A. R. (2000). Some operations on intuitionistic fuzzy sets. Fuzzy Sets and Systems, 114, 477–484.

Demirtas, N., Özgürler, S., Özgürler, M., & Güneri, A. F. (2014). Selecting e-Purse smart card technology via Fuzzy AHP and ANP. Journal of Applied Mathematics..

Efe, B. (2016). An integrated fuzzy multi criteria group decision making approach for ERP system selection. Applied Soft Computing, 38, 106–117.

Emrouznejad, A., & Marra, M. (2017). The state of the art development of AHP (1979–2017): A literature review with a social network analysis. International Journal of Production Research, 55, 6653–6675.

Erbas, M., Kabak, M., Ozceylan, E., & Çetinkaya, C. (2018). Optimal siting of electric vehicle charging stations: A GIS-based fuzzy Multi-Criteria Decision Analysis. Energy, 163, 1017–1031.

Ertay, T., Kahveci, A., & Tabanli, R. M. (2011). An integrated multi-criteria group decision-making approach to efficient supplier selection and clustering using fuzzy preference relations. International Journal of Computer Integrated Manufacturing, 24, 1152–1167.

Facchinetti, G., Ricci, R. G., & Muzzioli, S. (1998). Note on ranking fuzzy triangular numbers. International Journal of Intelligent Systems, 13, 613–622.

García-Cascales, M. S. (2012). Evaluation of photovoltaic cells in a multi-criteria decision making process. Annals of Operations Research, 199, 373–391.

Ghorbani, M., Mohammad Arabzad, S., & Shahin, A. (2013). A novel approach for supplier selection based on the Kano model and fuzzy MCDM. International Journal of Production Research, 51, 5469–5484.

Goyal, R. K., Kaushal, S., & Sangaiah, A. K. (2018). The utility based non-linear fuzzy AHP optimization model for network selection in heterogeneous wireless networks. Applied Soft Computing, 67, 800–811.

Grzegorzewski, P., & Mrówka, E. (2005). Some notes on (Atanassov’s) intuitionistic fuzzy sets. Fuzzy Sets and Systems, 156, 492–495.

Hashemian, S. M., Behzadian, M., Samizadeh, R., & Ignatius, J. (2014). A fuzzy hybrid group decision support system approach for the supplier evaluation process. The International Journal of Advanced Manufacturing Technology, 73, 1105–1117.

Ic, Y. T., Yurdakul, M., & Dengiz, B. (2013). Development of a decision support system for robot selection. Robotics and Computer-Integrated Manufacturing, 29, 142–157.

Ju, Y., Ju, D., Gonzalez, E. D. R. S., Giannakisc, M., & Wang, A. (2018). Study of site selection of electric vehicle charging station based on extended GRP method under picture fuzzy environment. Computers & Industrial Engineering (in press).

Jung, H. (2011). A fuzzy AHP–GP approach for integrated production-planning considering manufacturing partners. Expert Systems with Applications, 38, 5833–5840.

Kahraman, C., Beskese, A., & Kaya, I. (2010). Selection among ERP outsourcing alternatives using a fuzzy multi-criteria decision making methodology. International Journal of Production Research, 48, 547–566.

Kahraman, C., Sari, <sup>\_</sup>I. U., & Turanog˘lu, E. (2014). Fuzzy analytic hierarchy process with type-2 fuzzy sets. Knowledge-Based Systems, 59, 48–57.

Kannan, D., Khodaverdi, R., Olfat, L., Jafarian, A., & Diabat, A. (2013). Integrated fuzzy multi criteria decision making method and multi-objective programming approach for supplier selection and order allocation in a green supply chain. Journal of Cleaner Production, 47, 355–367.

Kar, A. K. (2014). Revisiting the supplier selection problem: An integrated approach for group decision support. Expert Systems with Applications, 41, 2762–2771.

Kar, A. K. (2015). A hybrid group decision support system for supplier selection using analytic hierarchy process, fuzzy set theory and neural network. Journal of Computational Science, 6, 23–33.

Karsak, E. E., & Dursun, M. (2016). Taxonomy and review of non-deterministic analytical methods for supplier selection. International Journal of Computer Integrated Manufacturing, 29, 263–286.

Khan, A. A., Shameem, M., Kumar, R. R., Hussain, S., & Yan, X. (2019). Fuzzy AHP based prioritization and taxonomy of software process improvement success factors in global software development. Applied Soft Computing, 83 105648.

Khorasani, S. T. (2018). Green supplier evaluation by using the integrated Fuzzy AHP model and Fuzzy Copras. Process Integration and Optimization for Sustainability. 2. 17–25.

Kilic, H. S., Selimzaim & Delen, D. (2014). Development of a hybrid methodology for ERP system selection: The case of Turkish airlines. Decision Support Systems, 66, 82–92.

Kilincci, O., & Onal, S. A. (2011). Fuzzy AHP approach for supplier selection in a washing machine company. Expert Systems with Applications, 38, 9656–9664.

Kim, K., & Park, K. S. (1990). Ranking fuzzy numbers with index of optimism. Fuzzy Sets & Systems. 35 143-150

Klir, G., & Yuan, B. (1995). Fuzzy sets and fuzzy logic. New Jersey: Prentice Hall.

Kubat, C., & Yuce, B. (2012). A hybrid intelligent approach for supply chain management system. Journal of Intelligent Manufacturing. 23 1237-1244.

Kubler S. Robert L Derigent W. Voisin A. & le Traon Y. (2016). A state-of the-art survey & testbed of fuzzy AHP (FAHP) applications. Expert Systems with Applications. 65. 398–422.

Kumar. D.. Rahman. Z.. & Chan. F. T. S. (2017). A fuzzy AHP and fuzzy multi obiective linear programming model for order allocation in a sustainable supply chain A case study. International Journal of Computer Integrated Manufacturing, 30, 535–551.

Kuo, R. J., Chi, S. C., & Kao, S. S. (2002). A decision support system for selecting convenience store location through integration of fuzzy AHP and artificial neural network. Computers in Industry, 47, 199–214.

Kuo, R. J., Lee, L. Y., & Hu, T.-L. (2010). Developing a supplier selection system through integrating fuzzy AHP and fuzzy DEA a case study on an auto lighting system company in Taiwan. Production Planning and Control, 21, 468–484.

Lee, J., Cho, H., & Kim, Y. S. (2015). Assessing business impacts of agility criterion and order allocation strategy in multi-criteria supplier selection. Expert Systems with Applications, 42, 1136–1148.

Lee, A. H. I. (2009). A fuzzy supplier selection model with the consideration of benefits, opportunities, costs and risks. Expert Systems with Applications, 36, 2879–2893.

Liu, Y., Eckert, C., Bris, G. Y.-L., & Petit, Galle (2019). A fuzzy decision tool to evaluate the sustainable performance of suppliers in an agrifood value chain. Computers & Industrial Engineering, 127, 196–212.

Luenberger, D. G., & Ye, Y. (2008). Linear and nonlinear programming. Springer Science & Business Media.

Mahjouri, M., Ishak, M. B., Torabian, A., Manaf, L. A., Halimoon, N., & Ghoddusi, J. (2017). Optimal selection of Iron and Steel wastewater treatment technology using integrated multi-criteria decision-making techniques and fuzzy logic. Process Safety and Environmental Protection, 107, 54–68.

Mahmoudzadeh, M., & Bafandeh, A. R. (2013). A new method for consistency test in fuzzy AHP. Journal of Intelligent & Fuzzy Systems, 25, 457–461.

Mangla, S. K., Kumar, P., & Barua, M. K. (2015). Risk analysis in green supply chain using fuzzy AHP approach: A case study. Resources, Conservation and Recycling, 104, 375–390.

Mardani, A., Jusoh, A., & Zavadskas, E. K. (2015). Fuzzy multiple criteria decisionmaking techniques and applications – Two decades review from 1994 to 2014. Expert Systems with Applications, 42, 4126–4148.

Mendel, J. M., & John, R. I. B. (2002). Type-2 fuzzy sets made simple. IEEE Transactions on Fuzzy Systems, 20, 117–127.

Mikhailov, L., & Tsvetinov, P. (2004). Evaluation of services using a fuzzy analytic hierarchy process. Applied Soft Computing Journal, 5, 23–33.

Mikhailov, L. (2004). A fuzzy approach to deriving priorities from interval pairwise comparison judgements. European Journal of Operational Research, 159, 687–704.

Mirhedayatian, M., Jelodar, M., Adnani, S., Akbarnejad, M., & Saen, R. (2013). A new approach for prioritization in fuzzy ahp with an application for selecting the best tunnel ventilation system. International Journal of Advanced Manufacturing Technology, 68, 2589–2599.

Mosadeghi R. Warnken L Tomlinson R. & Mirfenderesk H. (2015) Comparison of Fuzzy-AHP and AHP in a spatial multi-criteria decision making model for urban land-use planning. Computers, Environment and Urban Systems, 49, 54–65.

Naderzadeh, M., Arabalibeik, H., Monazzam, M. R., & Ghasemi, I. (2017). Comparative analysis of ahp-topsis and fuzzy ahp models in selecting appropriate nanocomposites for environmental noise barrier applications. Fluctuation and Noise Letters, 16.

Nazari, S., Fallah, M., Kazemipoor, H., & Salehipour, A. (2018). A fuzzy inferencefuzzy analytic hierarchy process-based clinical decision support system for diagnosis of heart diseases. Expert Systems with Applications, 95, 261–271.

Nguyen, H. T., Md Dawal, S. Z., Nukman, Y., Aoyama, H., & Case, K. (2015). An integrated approach of fuzzy linguistic preference based AHP and Fuzzy COPRAS for machine tool evaluation. PLoS ONE, 10 e0133599.

Onut, S., & Efendigil, T. (2010). A theorical model design for ERP software selection process under the constraints of cost and quality: A fuzzy approach. Journal of Intelligent & Fuzzy Systems, 21, 365–378.

Opricovic, S., & Tzeng, G.-H. (2003). Defuzzification within a multicriteria decision model. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 11, 635–652.

Parameshwaran, R., Kumar, S. P., & Saravanakumar, K. (2015). An integrated fuzzy MCDM based approach for robot selection considering objective and subjective criteria. Applied Soft Computing, 26, 31–41.

Pitchipoo, P., Venkumar, P., & Rajakarunakaran, S. (2013). Fuzzy hybrid decision model for supplier evaluation and selection. International Journal of Production Research, 51, 3903–3919.

Prakash, C., & Barua, M. K. (2016a). An analysis of integrated robust hybrid model for third-party reverse logistics partner selection under fuzzy environment. Resources, Conservation and Recycling, 108, 63–81.

Prakash C. & Barua M. K. (2016b). A combined MCDM approach for evaluation and selection of third-party reverse logistics partner for Indian electronics industry. Sustainable Production and Consumption, 7, 66–78.

Prasannavenkatesan, S., & Goh, M. (2016). Multi-objective supplier selection and order allocation under disruption risk. Transportation Research Part E: Logistics and Transportation Review, 95, 124–142.

Görener, A., Ayvaz, B., Kusakcı, A. O., & Altınok, E. (2017). A hybrid type-2 fuzzy based supplier performance evaluation methodology: The Turkish Airlines technic case. Applied Soft Computing, 56, 436–445.

Rezaei, J., Fahim, P. B. M., & Tavasszy, L. (2014). Supplier selection in the airline retail industry using a funnel methodology: Conjunctive screening method and fuzzy AHP. Expert Systems with Applications, 41. 8165–8179

Rezaei, J., & Ortt, R. (2013). Multi-criteria supplier segmentation using a fuzzy preference relations based AHP. European Journal of Operational Research, 225, 75–84.

Rezaei, J., Ortt, R., & Scholten, V. (2013). An improved fuzzy preference programming to evaluate entrepreneurship orientation. Applied Soft Computing Journal, 13, 2749–2758.

Roshandel, J., Miri-Nargesi, S. S., & Hatami-Shirkouhi, L. (2013). Evaluating and selecting the supplier in detergent production industry using hierarchical fuzzy TOPSIS. Applied Mathematical Modelling, 37, 10170–10181.

Ross, T. J. (2004). Fuzzy logic with engineering applications. John Wiley & Sons Ltd..

Saaty, T. L. (1980). The analytic hierarchy process: Planning, priority setting, resources allocation. New York: McGraw.

Saaty, T. L. (1990). How to make a decision: The analytic hierarchy process. European journal of operational research, 48, 9–26.

Saaty, T. L. (2006). There is no mathematical validity for using fuzzy number crunching in the analytic hierarchy process. Journal of Systems Science and Systems Engineering, 15, 457–464.

Saaty, T. L. (2008). Relative measurement and its generalization in decision making why pairwise comparisons are central in mathematics for the measurement of intangible factors the analytic hierarchy/network process. RACSAM-Revista de la

Real Academia de Ciencias Exactas Fisicas y Naturales. Serie A. Matematicas, 102, 251-318.

Samanlioglu, F., & Ayag, Z. (2017). A fuzzy AHP-PROMETHEE II approach for evaluation of solar power plant location alternatives in Turkey. Journal of Intelligent & Fuzzy Systems, 33, 859–871.

Sarfaraz, A., Jenab, K., & D’Souza, A. C. (2012). Evaluating ERP implementation choices on the basis of customisation using fuzzy AHP. International Journal of Production Research, 50, 7057–7067

Sen, C. G., Sen, S., & Baslıgil, H. (2010). Pre-selection of suppliers through an integrated fuzzy analytic hierarchy process and max-min methodology. International Journal of Production Research, 48, 1603–1625.

Shad, Z., Roghanian, E., & Mojibian, F. (2014). Integration of QFD, AHP, and LPP methods in supplier development problems under uncertainty. Journal of Industrial Engineering International, 10.

Shakourloo, A., Kazemi, A., & Javad, M. O. M. (2016). A new model for more effective supplier selection and remanufacturing process in a closed-loop supply chain. Applied Mathematical Modelling, 40, 9914–9931.

Shaw, K., Shankar, R., Yadav, S. S., & Thakur, L. S. (2012). Supplier selection using fuzzy AHP and fuzzy multi-objective linear programming for developing low carbon supply chain. Expert Systems with Applications, 39, 8182–8192.

Singh, R. K., Chaudhary, N., & Saxena, Nikhil (2018). Selection of warehouse location for a global supply chain: A case study. IIMB Management Review..

Singh, A., & Prasher, A. (2017). Measuring healthcare service quality from patients’ perspective: Using Fuzzy AHP application. Total Quality Management & Business Excellence 30.284-300

Singh, P. K., & Sarkar, P. (2019). A framework based on fuzzy AHP-TOPSIS for prioritizing solutions to overcome the barriers in the implementation of ecodesign practices in SMEs. International Journal of Sustainable Development & World Ecology, 26, 506–521.

Sirisawat, P., & Kiatcharoenpol, T. (2018). Fuzzy AHP-TOPSIS approaches to prioritizing solutions for reverse logistics barriers. Computers & Industrial Engineering, 117, 303–318.

Son, L. H. (2015). DPFCM: A novel distributed picture fuzzy clustering method on picture fuzzy sets. Expert Systems with Applications, 42, 51–66.

Soroor, J., Tarokh, M. J., Khoshalhan, F., & Sajjadi, S. (2012). Intelligent evaluation of supplier bids using a hybrid technique in distributed supply chains. Journal of Manufacturing Systems, 31, 240–252.

Subramanian, N., & Ramanathan, R. (2012). A review of applications of Analytic Hierarchy Process in operations management. International Journal of Production Economics, 138, 215–241.

Sultana, I., Ahmed, I., & Azeem, A. (2015). An integrated approach for multiple criteria supplier selection combining Fuzzy Delphi, Fuzzy AHP & Fuzzy TOPSIS. Journal of Intelligent & Fuzzy Systems, 29, 1273–1287.

Sun, C.-C. (2010). A performance evaluation model by integrating fuzzy AHP and fuzzy TOPSIS methods. Expert Systems with Applications, 37, 7745–7754

Taha, Z., & Rostam, S. (2011). A fuzzy AHP–ANN-based decision support system for machine tool selection in a flexible manufacturing cell. The International Journa of Advanced Manufacturing Technology, 57, 719–733.

Tan, R. R., Aviso, K. B., Huelgas, A. P., & Promentilla, M. A. B. (2014). Fuzzy AHP approach to selection problems in process engineering involving quantitative and qualitative aspects. Process Safety and Environmental Protection, 92, 467–475.

Tavana, M., Shaabani, A., Mansouri Mohammadabadi, S., & Varzgani, N. (2020). An integrated fuzzy AHP-fuzzy MULTIMOORA model for supply chain risk-benefit assessment and supplier selection. International Journal of Systems Science: Operations & Logistics, 1–24.

Taylan, O., Bafail, A. O., Abdulaal, R. M. S., & Kabli, M. R. (2014). Construction projects selection and risk assessment by fuzzy AHP and fuzzy TOPSIS methodologies. Applied Soft Computing, 17, 105–116.

Uygun, Ö., Kaçamak, H., & Kahraman, Ü. A. (2015). An integrated DEMATEL and Fuzzy ANP techniques for evaluation and selection of outsourcing provider for a telecommunication company. Computers & Industrial Engineering, 86, 137–146.

Vahidnia, M. H., Alesheikh, A. A., & Alimohammadi, A. (2009). Hospital site selection using fuzzy AHP and its derivatives. Journal of Environment Management, 90, 3048-3056.

van Laarhoven, P. J. M., & Pedrycz, W. (1983). A fuzzy extension of Saaty’s priority theory. Fuzzy Sets & Systems. 11. 199–227.

Vinodh, S., Prasanna, M., & Prakash, N. H. (2014). Integrated Fuzzy AHP-TOPSIS for selecting the best plastic recycling method: A case study. Applied Mathematical Modelling, 38, 4662–4672.

Viswanadham, N., & Samvedi, A. (2013). Supplier selection based on supply chain ecosystem, performance and risk criteria. International Journal of Production Research, 51, 6484–6498.

Wang, J.-W., Cheng, C.-H., & Huang, K.-C. (2009). Fuzzy hierarchical TOPSIS for supplier selection. Applied Soft Computing, 9, 377–386.

Wang. Y.-M., Luo. Y., & Hua, Z. (2008), On the extent analysis method for fuzzy AHP and its applications. European Journal of Operational Research, 186, 735–747.

Wang, B., Song, J., Ren, J., Li, K., Duan, H., & Wang, X. E. (2019). Selecting sustainable energy conversion technologies for agricultural residues: A fuzzy AHP-VIKOR based prioritization from life cycle perspective. Resources, Conservation and Recycling, 142, 78–87.

Wang, C.-H., & Wang, J. (2014). Combining fuzzy AHP and fuzzy Kano to optimize product varieties for smart cameras: A zero-one integer programming perspective. Applied Soft Computing, 22, 410–416.

Wilkinson, J. H. (1965). The algebraic eigenvalue problem. Oxford: Clarendon Press.

Xu, Z., & Liao, H. (2014). Intuitionistic Fuzzy analytic hierarchy process. IEEE Transactions on Fuzzy Systems, 22, 749–761.

Xu, Z. (2007). Intuitionistic preference relations and their application in group decision making q. Information Sciences An International Journal, 177, 2363–2379.

Yager, R. R. (1981). A procedure for ordering fuzzy subsets of the unit interval. Information Sciences, 24, 143–161.

Yang, J. L., Chiu, H. N., Tzeng, G.-H., & Yeh, R. H. (2008). Vendor selection by integrated fuzzy MCDM techniques with independent and interdependent relationships. Information Sciences, 178, 4166–4183.

Yayla, A. Y., Oztekin, A., Gumus, A. T., & Gunasekaran, A. (2015). A hybrid data analytic methodology for 3PL transportation provider evaluation using fuzzy multi-criteria decision making. International Journal of Production Research, 53, 6097–6113.

Yazdani-Chamzini, A., & Yakhchali, S. H. (2012). Tunnel Boring Machine (TBM) selection using fuzzy multicriteria decision making methods. Tunnelling and Underground Space Technology, 30, 194–204.

Yeh, C.-T. (2008). On improving trapezoidal and triangular approximations of fuzzy numbers. International Journal of Approximate Reasoning, 48, 297–313.

Yeh, C.-T. (2017). Existence of interval, triangular, and trapezoidal approximations of fuzzy numbers under a general condition. Fuzzy Sets and Systems, 310, 1–13.

Yu, M.-C., Goh, M., & Lin, H.-C. (2012). Fuzzy multi-objective vendor selection under lean procurement. European Journal of Operational Research, 219, 305–311.

Zadeh, L. A. (1965). Fuzzy sets. Information and Control, 8, 338–353.

Zeydan, M., Çolpan, C., & Çobanog˘lu, C. (2011). A combined methodology for supplier selection and performance evaluation. Expert Systems with Applications, 38.2741-2751.

Zhu, K.-J., Jing, Y., & Chang, D.-Y. (1999). A discussion on extent analysis method and applications of fuzzy AHP. European journal of operational research, 116, 450–456.

Zimmer, K., Fröhling, M., & Schultmann, F. (2016). Sustainable supplier management – A review of models supporting sustainable supplier selection, monitoring and development. International Journal of Production Research, 54, 1412–1442.

Zimmer, K., Fröhling, M., Breun, P., & Schultmann, F. (2017). Assessing social risks of global supply chains: A quantitative analytical approach and its application to supplier selection in the German automotive industry. Journal of Cleaner Production, 149, 96–109.

Zimmermann, H.-J. (2001). Fuzzy set theory and its applications. Kluwer Academic.

Zouggari, A., & Benyoucef, L. (2012). Simulation based fuzzy TOPSIS approach for group multi-criteria supplier selection problem. Engineering Applications of Artificial Intelligence, 25, 507–519.

Zyoud, S. H., Kaufmann, L. G., Shaheen, H., Samhan, S., & Fuchs-Hanusch, D. (2016). A framework for water loss management in developing countries under fuzzy environment: Integration of Fuzzy AHP with Fuzzy TOPSIS. Expert Systems with Applications, 61, 86–105.

## Glossary

AHP: Analytic Hierarchy Process

ANP: Analytic Network Process

CFCS: Converting the Fuzzy data into Crisp Scores

COA: Centre of Area

COG: Centre of Gravity

CI: Consistency Index

CR: Consistency Ratio

DEA: Data Envelopment Analysis

EAM: Extent Analysis Method

ELECTRE: ELimination Et Choix Traduisant la REalité

FAHP: Fuzzy Analytic Hierarchy Process

FP: Fuzzy Programming

GA: Genetic Algorithm

GCI: Geometric Consistency Index

GP: Goal programming

IFWA: Intuitionistic Fuzzy Weighted Averaging

LP: Linear programming

MCDM: Multi-Criteria Decision-Making

MOORA: Multi-Objective Optimisation by Ratio Analysis

MP: Mathematical Programming

PROMETHEE: Preference Ranking Organization METHod for Enrichment of Evaluations

RI: Radom Index

TFN: Triangular Fuzzy Number

TraFN: Trapezoidal Fuzzy Number

TOPSIS: Technique for Order of Preference by Similarity to Ideal Solution