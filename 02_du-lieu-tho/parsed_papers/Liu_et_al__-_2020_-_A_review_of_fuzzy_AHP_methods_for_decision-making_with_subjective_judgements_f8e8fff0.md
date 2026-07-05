<!-- image -->

## Review

## A review of fuzzy AHP methods for decision-making with subjective judgements

Yan Liu a, ⇑ , Claudia M. Eckert b , Christopher Earl b

a School of Computer Science and Technology, Changchun University of Science and Technology, Changchun 130022, Jilin, China b School of Engineering and Innovation, The Open University, Walton Hall, Milton Keynes MK7 6AA, UK

## a r t i c l e i n f o

Article history: Received 26 January 2020 Revised 5 June 2020 Accepted 9 July 2020 Available online 19 July 2020

## Keywords:

Fuzzy Analytic Hierarchy Process

Fuzzy set Multi-criteria decision-making Subjective judgement Selection problem

## 1. Introduction

In many professional situations, experts are confronted with a given set of alternatives that they need to choose from, for example when selecting a supplier or a technology. This type of decisionmaking problem is intuitive when considering a single criterion, since experts can choose the alternative of the highest preference. It becomes complicated when there are multiple criteria. These criteria are often not of equal importance and the alternatives have very varied performance. Formal methods are needed to ensure a structured means of making decisions. Many methods are available such as Analytic Hierarchy Process (AHP), Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) and Data Envelopment Analysis (DEA) (see Chai, Liu, and Ngai (2013), Karsak and Dursun (2016) and Zimmer, Fröhling, and Schultmann (2016) for

⇑ Corresponding author at: Office 412, Building of Shixun, Changchun University of Science and Technology, No. 7186 Weixing Road, Changchun, Jilin Province 130022, China.

E-mail addresses: yanl@cust.edu.cn (Y. Liu), claudia.eckert@open.ac.uk (C.M. Eckert), c.f.earl@open.ac.uk (C. Earl).

## a b s t r a c t

Analytic Hierarchy Process (AHP) is a broadly applied multi-criteria decision-making method to determine the weights of criteria and priorities of alternatives in a structured manner based on pairwise comparison. As subjective judgments during comparison might be imprecise, fuzzy sets have been combined with AHP. This is referred to as fuzzy AHP or FAHP. An increasing amount of papers are published which describe different ways to derive the weights/priorities from a fuzzy comparison matrix, but seldomly set out the relative benefits of each approach so that the choice of the approach seems arbitrary. A review of various fuzzy AHP techniques is required to guide both academic and industrial experts to choose suitable techniques for a specific practical context. This paper reviews the literature published since 2008 where fuzzy AHP is applied to decision-making problems in industry, particularly the various selection problems. The techniques are categorised by the four aspects of developing a fuzzy AHP model: (i) representation of the relative importance for pairwise comparison, (ii) aggregation of fuzzy sets for group decisions and weights/priorities, (iii) defuzzification of a fuzzy set to a crisp value for final comparison, and (iv) consistency measurement of the judgements. These techniques are discussed in terms of their underlying principles, origins, strengths and weakness. Summary tables and specification charts are provided to guide the selection of suitable techniques. Tips for building a fuzzy AHP model are also included and six open questions are posed for future work.

Ó 2020 Elsevier Ltd. All rights reserved.

an overview of available decision-making methods). Among them, AHP proposed by Saaty (1980) has been applied extensively to evaluate complex multi-criteria alternatives in a number of fields (Emrouznejad &amp; Marra, 2017; Subramanian &amp; Ramanathan, 2012). It outperforms by ease of use, structuring problems systematically and calculating both criteria weights and alternative priorities. As a popular methodology for handling imprecision, fuzzy sets proposed by Zadeh (1965) are combined with AHP, namely fuzzy AHP or FAHP. This integrated method maintains the advantage of AHP and has been widely applied (Mardani, Jusoh, &amp; Zavadskas, 2015). The procedure of building a fuzzy AHP model follows establishing the comparison matrix, aggregating multiple judgements, measuring the consistency and defuzzifying the fuzzy weights. Various techniques exist for each aspect. However, Little research has examined fuzzy AHP in terms of these aspects and set out the relative benefits of the techniques. This paper reviews the techniques regarding these four aspects, aiming to guide both academics and industrial experts to choose suitable techniques according to their practical context.

AHP structures a problem in a hierarchical way, descending from a goal to criteria, sub-criteria and alternatives in successive

Contents lists available at ScienceDirect

## Expert Systems with Applications

j o u r n a l homepage: www.elsevier.com/locate/eswa levels (Saaty, 1990). The hierarchy provides the experts with an overall view of the complex relationships inherent in the context; and helps them to assess whether the elements of the same level are comparable. Elements are then pairwise compared according to 9 level-scales to derive their weights. However, pairwise comparison, the essence of AHP, introduces imprecision because it requires the judgements of experts. In practical cases, experts might not be able to assign exact numerical values to their preferences due to limited information or capability (Chan &amp; Kumar, 2007; Xu &amp; Liao, 2014).

<!-- image -->

<!-- image -->

To handle the imprecision in AHP, exact numbers are replaced with fuzzy numbers representing the linguistic expressions in fuzzy AHP. This tolerates the vague judgements by assigning membership degrees to exact numbers to describe to what extent these numbers belong to an expression. However, introducing fuzzy sets to AHP makes the calculation process less straightforward because different fuzzy sets exist and the associated operations are complex. The techniques for AHP such as eigenvector method and geometric mean cannot directly be used to derive the weights/ priorities from a fuzzy comparison matrix. Many techniques for building a fuzzy AHP model have been proposed. They vary in terms of essential features, strengths and weakness. To the best of our knowledge, limited research has reviewed fuzzy AHP except Kubler, Robert, Derigent, Voisin, and le Traon (2016) who discuss the application areas.

The earliest reference that we have found dates from 1983 (van Laarhoven &amp; Pedrycz, 1983). Now, fuzzy AHP has become a popular fuzzy multi-criteria decision-making (MCDM) method (Kubler et al., 2016). It is applied in various industries, for example airline retail (Rezaei, Fahim, &amp; Tavasszy, 2014), agriculture (Hashemian, Behzadian, Samizadeh, &amp; Ignatius, 2014; Liu, Eckert, Bris, &amp; Petit, 2019), automobile (Büyüközkan &amp; Güleryüz, 2016; Zimmer, Fröhling, Breun &amp; Schultmann, 2017), logistics (Yayla, Oztekin, Gumus, &amp; Gunasekaran, 2015), manufacturing (Kar, 2014; Ayhan &amp; Kilic, 2015), maritime (Celik &amp; Akyuz, 2018), pharmacy (Alinezad, Seif, &amp; Esfandiari, 2013) and service (Khorasani, 2018), and to solve various problems, for example location selection (Erbas, Kabak, Ozceylan, &amp; Çetinkaya, 2018; Singh, Chaudhary, &amp; Saxena, 2018), machine selection (Nguyen, Md Dawal, Nukman, Aoyama, &amp; Case, 2015; Parameshwaran, Kumar, &amp; Saravanakumar, 2015), supplier selection (Akkaya, Turanog ˘lu, &amp; Öztas ß , 2015; Awasthi, Govindan, &amp; Gold, 2018; Kumar, Rahman, &amp; Chan, 2017; Shakourloo, Kazemi, &amp; Javad, 2016), technique selection (Balusa &amp; Gorai, 2018; Budak &amp; Ustundag, 2015; Naderzadeh, Arabalibeik, Monazzam, &amp; Ghasemi, 2017), sustainability management (Calabrese, Costa, Levialdi &amp; Menichin, 2019, 2016), business impacts assessment (Lee, Cho, &amp; Kim, 2015), risk analysis (Mangla, Kumar, &amp; Barua, 2015), intellectual capital assets management (Calabrese, Costa, &amp; Menichini, 2013) and teaching performance evaluation (Chen, Hsieh, &amp; Do, 2015). These decision problems all deal with the assessment and prioritisation of the alternatives which could be physical entities (e.g. machines, suppliers and locations) or abstract items (e.g. business impact indicators and risk factors). The results are used for selection if a preferred solution is required. The fuzzy AHP models built for the assessment problem in one field are applicable to other fields. This review paper is based on a systematic search of literature published since 2008 where fuzzy AHP is applied to the decision-making problems in industry. Our research originates from supplier selection and then branches out to other topics such as machine selection, location selection, ERP system selection, project selection and technology selection.

Fig. 1. The calculation process of fuzzy AHP using triangular fuzzy numbers.

<!-- image -->

The rest of paper is organised as follows. Section 2 explains the principle of fuzzy AHP method. Section 3 shows the research methodology of this study. There are four important aspects to develop a fuzzy AHP model, which are explained in Sections 4-7.

-  Section 4 explains how different fuzzy numbers, as a special type of fuzzy set, can be defined for judgement representations when establishing the comparison matrix.
-  Section 5 discusses how these fuzzy numbers are aggregated for group decisions and for deriving the weights.
-  Section 6 identifies the defuzzification method to obtain a crisp value from a fuzzy value for intuitive comparison.
-  Section 7 examines the consistency measurement which is an important way to ensure valid pairwise judgements.

To help readers extract quick information, the reviewed techniques are summarised in graphical and tabular forms. Discussions and insights are provided at the end of each section for choosing appropriate techniques. We also point out mistakes in few papers and indicate possible corrections, along with the review. Section 8 concludes this study with open questions for future research and a general guidance for building a fuzzy AHP model.

## 2. Principle of fuzzy AHP

The development of a fuzzy AHP model overall follows the process to develop an AHP model as illustrated in Fig. 1. The white and the light grey boxes show the common steps between AHP and fuzzy AHP but different techniques are applied in the steps of light grey boxes. The dark grey box is the step in fuzzy AHP but not in AHP. We illustrate the process with supplier selection using a special type of fuzzy set, triangular fuzzy number.

Structure the problem : The problem is decomposed in a hierarchy, which includes goal ('select best suppliers' in Fig. 1), criteria/ sub-criteria (Criterion 1 to Criterion 3) and alternatives (Supplier 1 to Supplier 3).

Establish the fuzzy pairwise comparison matrix : Let F ¼ e cij - n -n be the matrix for n criteria against the goal. e cij is a fuzzy set representing the relative importance of criterion i over j . Its reciprocal, 1 = e cij , is equal to the relative importance of criterion j over i , e cji . For example, the triangular fuzzy number (2,3,4) in the judgement table of expert 1 is the relative importance of criterion 1 over criterion 2 and thus (1/4,1/3,1/2) is that of criterion 2 over criterion 1. Replacing crisp values with fuzzy sets is the fundamental difference between fuzzy AHP and AHP. It results in that the techniques to derive weights/priorities in AHP cannot directly be used. Several fuzzy sets are applicable to establish the comparison matrix as explained in Section 4.

Fig. 2. Research framework.

<!-- image -->

Synthesise the judgements : if there are multiple experts, their opinions will be aggregated. As illustrated in Fig. 1, it takes place either before or after calculating the fuzzy weights, i.e. synthesising the pairwise comparisons (as labelled by ① in Fig. 1) or the fuzzy weights (as labelled by ② ). In the example, the relative importance of criterion 1 over criterion 2 from the two experts are different, i.e. (2, 3, 4) and (1, 2, 3). They are aggregated first. The techniques are examined in Section 5.

Calculate the fuzzy weights of the criteria : This step aggregates multiple fuzzy sets in the matrix into a single fuzzy set. Some aggregation methods in the previous step are applicable. Specialised methods are presented in Section 5.

Defuzzify the fuzzy weights : This is an extra step compared with AHP which maps a fuzzy set (i.e. fuzzy weight) to a crisp value (i.e. crisp weight) for further comparison. Fuzzy sets are difficult to compare directly because they are partially ordered rather than the linear or strictly ordered crisp values. Section 6 identifies the most prevalent defuzzification methods.

Check the consistency : Without this step, weights can still be obtained, and thus it is overlooked by some research. However, it is necessary to measure the fuzzy pairwise comparison matrix for the consistency. Suppose that criterion 1 is more important than criterion 2 and much more important than criterion 3. Logically, criterion 2 is more important than criterion 3. If the expert judges criterion 2 less important than criterion 3, then the judgements between criteria 1, 2 and 3 are in conflict. This step takes place after the comparison matrix is established (either the one from an individual expert or the aggregated one from multiple experts). The matrix is considered consistent if the contradictions among the pairwise comparisons are within a predefined threshold, namely consistency ratio. Otherwise, the experts need to recompare the criteria. The discussion is in Section 7.

The calculations of the sub-criteria weights and the alternative priorities follow the same process as described above. The calculated weights of sub-criteria are 'local weights', which are trans- formed to 'global weights' by multiplying with the weight of their parent criterion. For ease of explanation, we use 'weight' for 'global weight'. The overall priority of alternative Si is the aggregation of its priorities under all the criteria/sub-criteria. wj is the weight of criterion/sub-criterion j ; pj Si is the priority of Si under criterion j ; n is the number of criteria/sub-criteria.

<!-- formula-not-decoded -->

The overall calculation process in Fig. 1 reveals the four important aspects in developing a fuzzy AHP model: (1) representation of judgements for pairwise comparison to establish the matrix, (2) aggregation of fuzzy sets for group decisions and criteria weights, (3) defuzzification of a fuzzy set for further comparison and (4) consistency measurement for limited contradiction, which will be addressed in turn.

## 3. Research methodology

This research was carried out in two stages as shown in Fig. 2. In the first stage, we chose 'supplier selection' as the primary investigation topic. Fuzzy AHP is a generic decision-making method, applicable to most problems. Supplier selection is a typical and representative decision-making problem, involving prioritisation, assessment and ranking. It has a mixture of subjective and objective criteria and brings out many situations for which fuzzy AHP is required. As listed in Table A.9, it has been applied in a number of industries. Therefore, supplier selection is a potential target for many of the techniques. It is also a topic where fuzzy AHP has been most commonly used, according to the numbers of the reviewed articles. This corresponds to the survey result of Kubler et al. (2016). We selected 57 articles to analyse the methodological development of fuzzy AHP in terms of the four aspects. Under each aspect, the identified techniques were further categorised according to their properties (cf. fishbone diagram in Fig. 2). Each part of the fishbone diagram is presented in details in the following sections (cf. Figs. 4, 12, 15, 18).

Fig. 3. Journal distribution.

<!-- image -->

In the second stage, the study branched out to other domains to cover more techniques under the categorisations defined in the first stage, and included literature on machine selection, location selection, ERP system selection, project selection and technology selection. The topics were selected according to the number of articles using fuzzy AHP in the review paper by Kubler et al. (2016) and complemented by other important topics in industry including evaluation, management and diagnosis. Compared with supplier selection, fewer articles apply fuzzy AHP to rank the alternatives. Almost all the techniques in the selected 52 articles are covered by the review results of the first stage except the defuzzification method proposed by Opricovic and Tzeng (2003), which is problematic as discussed in Section 6.1.3. In addition, Mirhedayatian, Jelodar, Adnani, Akbarnejad, and Saen (2013) propose a different fuzzy programming model to calculate the weights and measure the consistency for selecting the best tunnel ventilation system.

The study targeted journals in four main library databases, i.e. ScienceDirect, Springer, Taylor &amp; Francis and EBSCOhost. Some of the journals cited in this review are Applied Mathematical Modelling, Applied soft computing, Computers &amp; Industrial Engineering, Energy, European Journal of Operational Research, Expert Systems with Applications, International Journal of Production Economics, International Journal of Production Research and Journal of Intelligent &amp; Fuzzy Systems. Articles were searched with keywords 'FAHP/Fuzzy AHP/Fuzzy Analytic Hierarchy Process'. They were screened according to three criteria:

-  it was published after 2008;
-  fuzzy AHP is used partially (for criteria weights) or completely (for both criteria weights and alternative priorities) in the evaluation process;
-  it presents clearly how fuzzy AHP is developed or applied.

In total, 109 articles were selected. Fig. 3 shows the distribution of these articles across the journals (the number of the selected articles is presented after the journal name). During the review, the original papers and highly cited papers were also looked back. Tables A.9 and A.10 in the appendix summarise the literature on supplier selection and the other topics respectively. The column of

'With methods' shows the methods fuzzy AHP is combined with, if there are any. The rest of the tables follows the structure of this paper. '-' means 'not applicable'.

## 4. Representation for pairwise comparison

It is the fundamental step of building a fuzzy AHP model to establish the pairwise comparison matrix with the expert's judgement. Linguistic terms describe the relative importance of a criterion or an alternative over another (e.g. 'equally preferred', 'fairly strongly preferred' and 'absolutely preferred'). In fuzzy AHP, such a term is represented by a fuzzy set which consists of two components, a set of elements x and an associated membership function l x ð Þ (Klir &amp; Yuan, 1995). The membership function assigns to each element a value between 0 and 1 as its membership degree to the set. The mappings between the fuzzy set and the linguistic term must conform to a scale so that the same judgement produces the same measurable value. Such a scale is called fuzzy scale. Fig. 4 outlines the structure of this section. Different types of fuzzy sets are explained by referring to the application context.

## 4.1. Type-1 fuzzy set

The fuzzy set described by a set of elements and crisp values as their membership degrees is called type-1 fuzzy set. A crisp number can be fuzzified. For example, 2 is definitely close to itself, so its membership degree to 'approximate 2 0 is 1. If 1.5 is considered neither close nor far to 2, 0.5 can be assigned as its membership degree to 'approximate 2 0 . A series of such numbers with their membership degrees compose a fuzzy set 'approximate 2 0 , denoted as e 2. Let 2 describe 'moderate importance' of one criterion over another in AHP. In fuzzy AHP e 2 replaces 2. Including a series of numbers addresses the problems that experts in some cases are unable to assign an exact number to the judgement. Their memberships indicate to what extent the experts are sure about the numbers to be used for the judgement. Mathematically, a fuzzy number is a convex normalised fuzzy set of the real line such that its associate membership function is piecewise continuous (Zimmermann, 2001). Because complicated fuzzy numbers may cause important difficulties in data processing such as hard to define arithmetic operations, several simple and representative fuzzy numbers have been proposed (Yeh, 2008, 2017; Ban &amp; Coroianu, 2012;). Triangular fuzzy number (TFN) and trapezoidal fuzzy number (TraFN) are two kinds of such fuzzy numbers that have been well studied.

Fig. 4. Categorisation of the judgement representations.

<!-- image -->

TFN is the mostly popular means of judgement representation in the reviewed articles (99 out of the 109 articles, i.e. 91%). A TFN e A can be expressed as a triple l ; m ; h ð Þ where l and h are the smallest and the largest values with the smallest membership respectively and m is the value with the largest membership. The membership function of a TFN is defined as follows and illustrated in Fig. 5(a).

<!-- formula-not-decoded -->

The a -cut set of a fuzzy set e A , denoted as e A a , is a crisp value set containing all the elements with membership degrees greater than or equal to the specified value of a :

<!-- formula-not-decoded -->

The a -cut set of a TFN can be represented as an interval, i.e. e A a ¼ l þ m   l ð Þ a ; h   h   m ð Þ a ½  shown in Fig. 5 (b). It helps defuzzify a TFN.

TFN is useful when the expert is definitive about a single point representing the total belongingness. For example, if 30 ° C is considered as a definitely high temperature, slightly below it is hot but not so hot and above it is also hot but too hot, then TFN describes this judgement (i.e. m = 30 ° C). But if the expert is certain within an interval, such as any temperature between 28 and 32 ° C is considered as a definitely high temperature while below 28 ° C is hot but not so hot and above 32 ° C is also hot but too hot, then TraFN is needed. It is characterised by a quadruple ( l , ml , mh , h ) as shown in Fig. 6. In the example, ml = 28 ° C and mh = 32 ° C. When ml = mh , a TraFN reduces to a TFN. Sometimes, there is a mixed use of TFN and TraFN, for example, Aydin and Kahraman (2010).

## 4.2. Type-2 fuzzy set

The membership space of type-1 fuzzy set is assumed to be the space of real numbers. A natural extension is the definition of type2 fuzzy set whose membership values are type-1 fuzzy sets rather than real numbers (Zimmermann, 2001). Type-2 fuzzy set captures more imprecision because it expresses the imprecision on both the elements and their memberships. It helps when the expert is not sure about the membership of an element to a set. A type-2 fuzzy set e e A in the universe set X is defined as follows (Mendel &amp; John, 2002):

<!-- formula-not-decoded -->

<!-- image -->

where x is the element, u is a primary membership degree of x and J x is the value set of u under x . l x ; u ð Þ is called the secondary membership function, which is a type-1 fuzzy set. Fig. 7 depicts l x ; u ð Þ for x and u where X = (1, 2, 3, 4, 5) and U = {0, 0.2, 0.4, 0.6, 0.8}. Each of the rods represents l x ; u ð Þ at a specific pair ( x , u ). For example, the length of the rod for (2, 0) is 0.5 in Fig. 7, which means l (2, 0) = 0. J1 = J2 = J4 = J5 = {0, 0.2, 0.4, 0.6, 0.8} and J3 = {0.6, 0.8}. An example of the secondary membership function at x = 2 is:

<!-- formula-not-decoded -->

The union of the five secondary membership functions at x = 1, 2, 3, 4, 5 is l x ; u ð Þ of the set.

In the above example, the complexity of operations is acceptable because it is a small discrete set where the elements are finite. For a continuous set, the computation becomes extremely difficult and even its literal description is problematic. Take for example the continuous type-2 fuzzy set defined on [1, 5] in Fig. 8(a). The shadow illustrates the membership function l ( x,u ) which is hardly described in formulas. But in the case of all l ( x,u ) = 1, this 3dimensional set becomes a 2-dimensional set on axes x and u as shown in Fig. 8(b), the complexity of which reduces greatly. This special type-2 fuzzy set is called interval type-2 fuzzy set. It is the most widely used type-2 fuzzy set because this special kind is relative simple and it is also very difficult to justify the use of any other kind (Mendel &amp; John, 2002).

Fig. 7. Example of a type-2 membership function, adapted from (Mendel &amp; John, 2002)

<!-- image -->

Fig. 5. (a) A TFN, e A ; (b) a -cut of a TFN, e A a

<!-- image -->

The interval type-2 fuzzy set can be further distinguished by the shapes of the membership functions, such as triangular and trapezoidal. The adoption of trapezoidal interval type-2 fuzzy set has been found in the reviewed articles of Görener, Ayvaz, Kus ß akcı, and Altınok (2017) and Celik and Akyuz (2018). As shown in Fig. 9, a trapezoidal interval type-2 fuzzy set can be characterised by the reference points and the heights of its upper and the lower membership functions. The reference points are the elements whose membership degrees can be used to define the shape of membership functions. The trapezoidal ring in Fig. 9 is the analogue of the U shape plane in Fig. 8 (b). A trapezoidal interval type-2 fuzzy set is defined as:

<!-- formula-not-decoded -->

e A U and e A L are type-1 fuzzy sets; a1 U , a2 U , a3 U , a4 U , a1 L , a2 L , a3 L and a4 L are the reference points; Hi e A U   is the membership degree of element a U i þ 1 in the upper trapezoidal membership function e A U ; Hi e A L   is the membership degree of element a L i þ 1 in the lower trapezoidal membership function e A L ; 1 6 i 6 2, Hi e A U   2 0 ; 1 ½  , Hi e A L   2 0 ; 1 ½  .

## 4.3. Intuitionistic fuzzy set

The membership degree in a type-1 fuzzy set indicates to what extent an element belongs to the set. There could correspondingly be a value for the extent that the element does not belong to this set. The belongingness and non-belongingness do not necessarily complement each other because of the imprecision of judgement or the possibility of this element belonging to another set. Intuitionistic fuzzy set proposed by Atanassov (1986) is characterised by two such functions expressing the degree of belongingness and the degree of non-belongingness respectively. Intuitionistic fuzzy set deals with the situation that the membership or the nonmembership cannot be determined to the expert's satisfaction and an indeterministic part remains (De, Biswas, &amp; Roy, 2000; Grzegorzewski &amp; Mrówka, 2005). An intuitionistic fuzzy set A in the universe of discourse X is a set of ordered triples (Atanassov, 2012):

Fig. 8. Example of continuous type-2 fuzzy set with: (a) l x ; u ð Þ -1 and (b) all l ( x,u ) = 1

<!-- image -->

Fig. 9. A trapezoidal interval type-2 fuzzy set

<!-- image -->

<!-- formula-not-decoded -->

where l ( x ) and v ( x ): X ? [0,1] are the membership function and non-membership function respectively; 0 6 l x ð Þ þ v x ð Þ 6 1. For each A , there is another parameter p ( x ), called the degree of nondeterminacy of the membership of x to the set A ; p ( x ) = 1   l ( x )   v ( x ). In intuitionistic fuzzy AHP, ( l ( x ), v ( x ), p ( x )) is used to describe the preference degree of one criterion/alternative over another. Büyüközkan and Güleryüz (2016) choose intuitionistic fuzzy sets to express the linguistics terms.

Cuong (2014) introduces the concept of a picture fuzzy set that extends the intuitionistic fuzzy set by adding a degree of neutral belongingness. A picture fuzzy set A in the universe of discourse X is defined as:

<!-- formula-not-decoded -->

where l ( x ), g x ð Þ and v ( x ): X ? [0,1] are degree of positive membership, degree of neutral membership and degree of negative membership respectively. They satisfy the condition: 0 6 l x ð Þ þ g x ð Þ þ v x ð Þ 6 1 : p x ð Þ ¼ 1   l x ð Þ   g x ð Þ   v x ð Þ is the degree of refusal membership. Models based on picture fuzzy sets can be applied in the situation when experts have opinions involving more answers such as yes, abstain, no and refusal. An example is voting that the voters may be divided into four groups of those who vote for, abstain, vote against and refusal of the voting (invalid voting or not taking the vote) (Cuong, 2014; Son, 2015). However, due to the lack of mathematical discussions with its aggregation and defuzzification, picture fuzzy sets are hardly applied in constructing pairwise comparison decision matrix. For example, Ju, Ju, Gonzalez, Giannakisc, and Wang (2018) apply picture fuzzy sets for site ranking but still use TFNs to construct the comparison matrix in fuzzy AHP.

## 4.4. Fuzzy scales

A fuzzy set describes a particular linguistic term. A fuzzy scale defined by a series of fuzzy sets depicts the levels of linguistic terms, which links the verbal and numerical expressions. (9)level and 5-level fuzzy scales for relative importance are commonly adopted (34 and 43 out of the 109 articles respectively) as illustrated in Fig. 10(a) and (b). We take TFNs as example to discuss how literature defines these scales because TFNs are largely applied.

The literature uses different linguistic terms when describing the same scale. For example, Ayhan and Kilic (2015) use 'equally important', 'equally to weakly important', 'weakly important', 'weakly to fairly important', 'fairly important', 'fairly to strongly important', 'strongly important', 'strongly to absolutely important' and 'absolutely important' to describe the 9 levels that correspond to TFNs e 1, e 2, e 3, e 4, e 5, e 6, e 7, e 8 and e 9. Pitchipoo, Venkumar, and Rajakarunakaran (2013) map those TFNS with 'equally preferred', 'equally to moderately preferred', 'moderately preferred', 'moderately to strongly preferred', 'strongly preferred', 'strongly to very strongly preferred', 'very strongly to extremely preferred' and 'extremely preferred'.

<!-- image -->

Equal

importance importance

importance

1

Moderate

2

Extremely strong

Very strong

importance

importance

4

5

1

0

importance importance

Moderate

importance

1

3

(b)

Fig. 10. Fuzzy scale of: (a) 9-level and (b) 5-level

Extremely strong

Very strong

importance

importance

7

9

Strong

3

Equal Strong

5

1

0

Most researchers define the scales in the way as shown in Fig. 10. Slight differences exist in defining TFNs. The TFN e 9 could also be interpreted as (7,9,11) (e.g. Viswanadham and Samvedi (2013)), (8, 9, 10) (e.g. Beikkhakhian, Javanmardi, Karbasian, and Khayambashi (2015), (9, 9, 9) (e.g. Kannan, Khodaverdi, Olfat, Jafarian, and Diabat (2013)) and (9,9,10) (e.g. Taylan, Bafail, Abdulaal, and Kabli (2014)). e 1 could also be defined as (0,1,1) (e.g. Taylan et al. (2014)). Some researchers take totally different TFNs. For example, Zimmer et al. (2017) use e 1, g 1 : 5, g 2 : 5, g 3 : 5 and g 4 : 5 for the 5 levels. Other scales are also applied, including 6level and 7-level fuzzy scales. The number after 'TFN' in the column of 'Pairwise' in Tables A.9 and A.10 indicates the scale used by the article.

## 4.5. Short discussion

When type-1 fuzzy set uses one value to deal with the imprecision of an element belonging to a set, type-2 fuzzy set expresses the imprecision of this imprecision (i.e. the imprecision of the membership degree), and intuitionistic fuzzy set complements this imprecision by adding a non-membership. Type-2 fuzzy set and intuitionistic fuzzy set are considered more capable to capture imprecision. However, their arithmetic operations needed in calculations are more complicated due to the introduction of more parameters in their definitions.

There are no specific choice rules as to which type of fuzzy set should be used. A general guidance is suggested as a tree diagram in Fig. 11.

The proper fuzzy set(s) emerge(s) by answering the subsequent questions. The choice should also consider the properties of the fuzzy sets, as concluded in Table 1. The table shows 'when' the fuzzy set is applicable, 'what' it describes, 'how' it is defined and the complexity of its arithmetic operations.

## 5. Aggregation method

The main purpose of aggregation is to produce appropriate results from the pairwise comparison matrix. This involves methods for: (1) synthesising the decisions of multiple experts and (2)

Fig. 11. Fuzzy set specification chart

<!-- image -->

Table 1 Summary of the fuzzy sets applied in fuzzy AHP.

| Fuzzy set                             | When                                                | What                                                                                            | How                                                                                                                            | Complexity       |
|---------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------|
| TFN                                   | The opinions involve answers: partly yes and        | Describe the imprecision of a crisp number with precise membership.                             | Define the upper and lower boundaries and the middle point.                                                                    | Simple           |
| TraFN                                 | partly no.                                          |                                                                                                 | Define the upper and lower boundaries and the two middle points.                                                               | Simple           |
| Trapezoidal interval type-2 fuzzy set | The opinions involve quite unsure answers.          | Describe the imprecision of a crisp number with imprecision membership.                         | Define the upper and lower boundaries and the two middle points of the upper and lower trapezoidal fuzzy numbers respectively. | Very complicated |
| Intuitionistic fuzzy set              | The opinions involve answers: yes, no and not sure. | Describe the imprecision of a crisp number with precise membership and precise non- membership. | Define the degrees of belongingness and non- belongingness.                                                                    | Complicated      |

deriving the fuzzy weights of criteria and priorities of alternatives. The methods are further categorised according to the types of fuzzy set as discussed in the previous section. Fig. 12 shows the categorisation of the identified methods annotated by their main characteristics. The strength and weakness of each method is discussed at the end of this section.

## 5.1. Aggregation for group decision

One challenge of using subjective values is that the judgements of different experts could vary. Their opinions need to be aggregated to produce a final result. Let (DM1, DM2, . . . , DMq) be the q experts and (C1, C2, . . . , Cn) be the n performance criteria. This subsection starts with three techniques for type-1 fuzzy set (mainly for TFN) and then discusses the aggregation for type-2 fuzzy set and intuitionistic fuzzy set.

## 5.1.1. Mean method

Mean methods for fuzzy numbers are based on the mean methods for crisp values. They emphasis 'average' among all the judgements. Their underlying principle and operations are simple. Geometric mean and arithmetic mean are two popular ones (25 and 16 respectively out of 44 papers that have considered group decision and applied type-1 fuzzy sets).

<!-- formula-not-decoded -->

importance of Ci over Cj judged by DMt, e Cij ¼ l ij ; mij ; hij    be the aggregated relative importance of Ci over Cj and e wi be the fuzzy weight of Ci. Some research applies geometric mean, for example, Yang, Chiu, Tzeng, and Yeh (2008), Chen and Yang (2011), Kannan et al. (2013) and Zimmer et al. (2017).

<!-- formula-not-decoded -->

An extension to geometric mean is weighted geometric mean that accommodates the weights of experts. Let ( a 1 , a 2 , . . . , a q ) be the exponential weighting vector of the q experts. Weighted geometric mean for the collective relative importance of Ci over Cj or weight of Ci is as Eq. (9), where f W q ð Þ i is the weight of Ci judged by DMq.

<!-- formula-not-decoded -->

With Eq. (9), Ertay, Kahveci, and Tabanli (2011) aggregate the pairwise comparison matrices while Kar (2014, 2015) aggregate the weights calculated from the pairwise comparison matrix of each expert.

Similarly, arithmetic mean (Ayhan &amp; Kilic, 2015; Viswanadham &amp; Samvedi, 2013) and its weighted extension (Büyüközkan, 2012) are as Eqs. (10) and (11) respectively. ( a 1 , a 2 , . . . , a q ) is the normalised weighting vector.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The two mean methods can also be applied to aggregate TraFNs where the operations are on the quadruples instead of the triples. For example, Eq. (8) is changed to the following form for TraFNs.

<!-- formula-not-decoded -->

Fig. 12. Categorisation of the aggregation methods

<!-- image -->

## 5.1.2. Max-min method

Compared to the mean methods using an average solution, max-min methods extend the aggregated value range by including the 'worst' and the 'best' judgements. Max and min, as two aggregation operators, choose the largest and smallest values respectively. They decide the upper and lower bounds of the aggregated TFN ( h and l in Fig. 5). The middle value m is calculated by geometric mean or arithmetic mean (Awasthi et al., 2018; Prakash &amp; Barua, 2016a). The aggregated TFN e Cij ¼ l ij ; mij ; hij    by max-min with geometric mean is:

<!-- formula-not-decoded -->

The aggregated TFN e Cij ¼ l ij ; mij ; hij    by max-min with arithmetic mean is:





<!-- formula-not-decoded -->

Chen, Wang, Chen, and Lee (2010) combine multiple crisp values of judgements to a TFN as the aggregated relative importance of Ci over Cj. Let crisp value e (t) be the judgement of expert DMt. The aggregated result e Cij ¼ l ij ; mij ; hij    is computed as:

 

<!-- formula-not-decoded -->



The article on this method referred to by Chen et al. (2010) (i.e. Kuo, Chi, and Kao (2002)) computes the middle value with geometric mean rather than with Eq. (15).

## 5.1.3. Method based on consensus degree

A method based on consensus degree is proposed by Chen (1998) to handle trapezoidal fuzzy number (TraFN). Its aggregation principle is similar to weighted arithmetic mean. This method introduces a variable of 'consensus degree coefficient' for each expert and multiplies it with the individual judgement instead of weight of expert in weighted arithmetic mean. This variable is a compromise between the weight of expert and the difference of its opinion from the opinions of all the others. The process is as follows.

Step 1: Translate the judgement given by expert DMt into a standardised TraFN characterised by a quadruple e C t ð Þ ¼ l t ð Þ ; m t ð Þ 1 ; m t ð Þ 2 ; h t ð Þ   , where 0 6 l t ð Þ 6 m t ð Þ 1 6 m t ð Þ 2 6 1. Step 2: Calculate the degree of agreement S e C t ð Þ ; e C j ð Þ   of the opinions between each pair of experts DMt and DMj, where S e C t ð Þ ; e C j ð Þ   2 0 ; 1 ½  , 1 6 t 6 q ; 1 6 j 6 q ; and t -j . The degree is calculated by Eq. (16). The larger value of S e C t ð Þ ; e C j ð Þ   , the greater the similarity between the two standardised TraFNs.

<!-- formula-not-decoded -->

Step 3: Calculate the average degree of agreement A ( DMt ) of expert DMt ( t = 1, 2, . . . , n) with all the others.

<!-- formula-not-decoded -->

Step 4: Calculate the relative degree of agreement RA ( DMt ) of expert DMt ( t = 1, 2, . . . , n).

<!-- formula-not-decoded -->

Step 5: Calculate the consensus degree coefficient C ( DMt ) of expert DMt ( t = 1, 2, . . . , n).

<!-- formula-not-decoded -->

wDMt is the weight of expert DMt; y1 and y2 are the weight of the importance of experts and the weight of the relative degree of agreement of experts.

Step 6: Aggregate the fuzzy judgements. The result e Cagg is:

<!-- formula-not-decoded -->

Büyüközkan, Karabulut and Arsenyan (2017) employ this method directly to TFNs without adaptation. They calculate the similarity of two TFNs based on Eq. (16) in the following way.

<!-- formula-not-decoded -->

For TFNs, Eq. (16) should be revised as Eq. (22) (Chen &amp; Chen, 2001) rather than Eq. (21).

<!-- formula-not-decoded -->

## 5.1.4. Fuzzy interval geometric mean

Geometric mean is also applied to type-2 fuzzy set but the calculation process is different from type-1 fuzzy set due to the different arithmetic operations defined on these sets. It seems to be the only aggregation operation defined for trapezoidal interval type-2 fuzzy set and does not involve much calculation effort. Görener et al. (2017) use geometric mean to aggregate the multiple interval

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.1.5. Intuitionistic fuzzy weighted averaging

Intuitionistic fuzzy weighted averaging (IFWA) includes weighted arithmetic and geometric averaging operators (Xu, 2007). If the weights of experts are equal, the two operators reduce to intuitionistic fuzzy arithmetic and geometric averaging operators. Büyüközkan and Güleryüz (2016) and Büyüközkan, Göçer and Karabulut (2019) apply intuitionistic fuzzy weighted arithmetic averaging operator. Let C t = ( l t , v t , p t ) be the judgement of expert DMt and v = ( a 1 , a 2 , . . . , a q ) be the weight vector of the experts. The aggregation result is Cagg , where

<!-- formula-not-decoded -->

## 5.2. Aggregation for fuzzy weights/priorities

Aggregation of judgements on a single criterion are usually done as a mean or an average value. By contrast, the methods for the weights of criteria are more varied in that they deal with the judgements on different criteria from the fuzzy pairwise comparison matrix. This section starts with four techniques for the matrix of type-1 fuzzy sets. Let F ¼ e Cij h i n -n be a fuzzy pairwise comparison matrix and (C1, C2, . . . , Cn) be the n performance criteria. e Cij is the relative importance of Ci over Cj. We describe the methods with notations related to criteria. The calculation of the alternative priorities is the same.

## 5.2.1. Mean method

Geometric mean is a valid means of synthesising different perspectives and also an approximation to eigenvalues of a matrix. It has been widely used to calculate fuzzy weights, e.g. Yang et al. (2008), Sun (2010), Yu, Goh, and Lin (2012), Kar (2014) and Görener et al. (2017). It is immune to the problem of rank reversal and independent on order of operations (Barzilai, 1997). The 'mean' value by geometric operation is then normalised to generate the fuzzy weight of a criterion, as shown in Eq. (27).

<!-- formula-not-decoded -->

Rezaei and Ortt (2013) and Chen et al. (2010) apply arithmetic mean as Eq. (28). It is also utilised in Extent Analysis Method (EAM) to get the fuzzy weights. Some research obtains the weights by applying row sums and then normalising the sums instead of averaging, which is also a simple and convenient methods, for example, Calabrese et al. (2016; 2019).





<!-- formula-not-decoded -->

Another method in this group is fuzzy logarithmic least-squares method proposed by van Laarhoven and Pedrycz (1983). It is grouped in mean methods because geometric mean is considered by researchers for example, Büyüközkan (2012), as one optimal solution to this programming problem. However, the weights estimated by logarithmic least-squares might not be valid fuzzy numbers (Csutora &amp; Buckley, 2001). In other words, it can produce fuzzy weight f W ¼ l ; m ; h ð Þ with h &lt; l . cij is the entry of the pairwise comparison matrix and wi is the weight of criteria i . The method is:

<!-- formula-not-decoded -->

Subject to

<!-- formula-not-decoded -->

With regards to the capability of processing size of the matrix, fuzzification level and inconsistency, fuzzy logarithmic leastsquares has the best overall performance, followed by geometric mean and then arithmetic mean (Ahmed &amp; Kilic, 2018).

## 5.2.2. Lambda-max method

The lambda-max method proposed by Csutora and Buckley (2001) transforms the fuzzy comparison matrix into three crisp comparison matrices through the a -cut of a TFN, and then calculates the fuzzy weights. This method directly fuzzifies Saaty's k max method (eigenvector method) and reduces the fuzziness in the final fuzzy weights. It can also handle any type-1 fuzzy number used for pairwise comparison. Compared with mean method, it is complicated due to the multiple steps involving calculating eigenvalues, minimising the fuzziness, adjusting the boundaries of the weights. Wang, Cheng, and Huang (2009) apply this method in their fuzzy AHP model. It has the following steps. As introduced in Section 4.1, the a -cut of a TFN e Cij ¼ l ij ; mij ; hij    can be represented as e Cij a ¼ l ij þ mij   l ij    a ; hij   hij   mij    a - .

Step 1: Set a = 1. The middle value of each entry of the fuzzy pairwise comparison matrix is F ¼ e Cij h i n -n , i.e. e Cij a ¼ 1 = mij . The corresponding crisp comparison matrix is Fm = [ mij ]n -n. The middle value of the fuzzy weight of criterion Ci, wim , is calculated by solving Eq. (30). k max is the largest eigenvalue of Fm . wm is the weight vector, wm = ( w1m , w2m , . . . , wnm ) T .

<!-- formula-not-decoded -->

Step 2: Set a = 0. This calculates the lower and upper bounds of the fuzzy weight of criterion Ci, wil and wih . The two crisp comparison matrices are Fl = [ l ij ]n -n and Fh = [ hij ]n -n. wl and wh are the weight vectors generated from Fl and Fu respectively. The calculation procedure is the same with that of wm by Eq. (30).

Step 3: Find constants Kl and Kh . They are used to minimise the fuzziness of the weights, which refers to the lengths of the a -cuts.

n

o

<!-- formula-not-decoded -->

Step 4: Use the two constants to adjust the lower and upper bounds of the fuzzy weight of criterion Ci obtained in step 2. The adjusted bounds are wil* and wih* .

<!-- formula-not-decoded -->

The fuzzy weight of criterion Ci is as f Wi ¼ w  il ; wim ; w  ih    .

## 5.2.3. Eigenvector based on index of optimism

Calculating the eigenvector is the original method to derive weights from the matrix in AHP. This method can be adapted to fuzzy AHP but requires transforming fuzzy values to crisp values. In other words, the fuzzy comparison matrix needs to be transformed to crisp comparison matrix. One common method for this transformation uses a -cut and an index of optimism. Different from Lambda-max method that solely uses a -cut for several crisp matrices, the weights obtained in this manner are crisp values rather than fuzzy numbers. Let cij a U and cij a L denote the upper and lower bounds of a -cut set e Cij a , i.e. e Cij a = [c ij a L , cij a U ]. c ij a U indi- cates an optimistic expert's point of view towards the priority of criterion Ci over Cj while c ij a L is a pessimistic view (Kim &amp; Park, 1990). An expert's attitude may not be purely optimistic or pessimistic, but somewhere in between. Therefore, they are combined with an index of optimism l as:

<!-- formula-not-decoded -->

The larger the value of l is, the higher the degree of optimism is. cij is also named as degree of satisfaction. The fuzzy comparison matrix is transformed into a crisp matrix F = [ cij ]n -n by Eq. (33). By setting the values of a and l (usually set as 0.5 and 0.5), weight calculation turns to finding the eigenvector by Saaty's k max method. The application can be found in Soroor, Tarokh, Khoshalhan, and Sajjadi (2012), Büyüközkan et al. (2017) and Beikkhakhian et al. (2015).

Awasthi et al. (2018) calculate the weights in a similar way that the fuzzy matrix is defuzzified first by Eq. (34) and then the eigenvector is computed. cij is the defuzzified value from TFN.

<!-- formula-not-decoded -->

Pitchipoo et al. (2013) also calculate weights by converting fuzzy numbers into crisp values. They apply centroid method for defuzzification, given in Eq. (35).

<!-- formula-not-decoded -->

Fig. 13. Specification chart of aggregation methods for group decisions

<!-- image -->

k is the number of rules. O i is the class generated by rule i (from 0, 1, . . . , L   1). L is the number of classes, n is the number of inputs, and mli is the membership grade of feature l in the fuzzy regions that occupy the i th rule. However, it is not clear how the method in Pitchipoo et al. (2013) actually works without a further explanation on 'rules', 'class' and 'inputs' as well as their mapping with criteria, alternatives and TFNs.

Table 2 Summary of the aggregation methods for group decisions.

| Method                              | Characteristic                                                                                                                                                             | Complexity                                                                       | Extension                                                                                                                                                                                                                                                   |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arithmetic mean                     | Emphasis 'average'. There should be no extreme value due to its sensitivity.                                                                                               | Very simple, only involving arithmetic addition and division.                    | (1) Weighted arithmetic mean by incorporating the weights of experts; (2) intuitionistic fuzzy weighted arithmetic averaging for intuitionistic fuzz sets by adding the weights of experts.                                                                 |
| Geometric mean                      | Emphasis 'average'. It is less affected by extreme value and more suitable to average normalised values. There should be no negative value.                                | Very simple, only involving arithmetic multiplication and rooting.               | (1) Weighted geometric mean by incorporating the weights of experts; (2) fuzzy interval geometric mean for interval type-2 fuzzy sets; (3) intuitionistic fuzzy weighted geometric averaging for intuitionistic fuzz sets by adding the weights of experts. |
| Max-min method with arithmetic mean | Include the 'worst' and the 'best' judgements but introduce more fuzziness due to the enlarged value range. There should be no extreme value.                              | Simple, involving arithmetic addition and division, max and min operations.      | -                                                                                                                                                                                                                                                           |
| Max-min method with geometric mean  | Include the 'worst' and the 'best' judgements but introduce more fuzziness due to the enlarged value range.                                                                | Simple, involving arithmetic multiplication and rooting, max and min operations. | Produce a TFN as the aggregated judgement by combining crisp values of the experts' judgements.                                                                                                                                                             |
| Method based on Consensus degree    | Consider the distances between the opinions of the experts but assume the weight of the importance of expert and the weight of the relative degree of agreement are known. | Complicated due to the calculation of degree of agreement.                       | -                                                                                                                                                                                                                                                           |

Fig. 14. Specification chart of the aggregation methods for weights

<!-- image -->

Table 3 Summary of the aggregation methods for weights/priorities.

| Method                     | Principle                                                                                                                                                                    | Complexity                                                                                                                                           | Pros and Cons                                                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arithmetic mean            | Row sum divided by n (the number of criteria), which is then normalised.                                                                                                     | Very simple, only involving arithmetic addition and division.                                                                                        | Perform least in the mean group.                                                                                                                                           |
| Geometric mean             | N th-root of row multiplication, which is then normalised.                                                                                                                   | Very simple, only involving arithmetic multiplication and rooting.                                                                                   | Produce the same weights as Saaty's eigenvector method, if the matrix is consistent. Perform better than arithmetic mean.                                                  |
| Logarithmic least- squares | A mathematical programming method                                                                                                                                            | Complicated because it is indeed a programming method but the objective and constraint functions are simple.                                         | May produce fuzzy weights that are not fuzzy numbers, which could lead to inconsistency. It could generate multiple results as the weight. Perform best in the mean group. |
| Lambda-max method          | Transform the fuzzy matrix into multiple crisp matrices by a -cut, and then calculates the fuzzy weights by generating and adjusting the eigenvectors of the crisp matrices. | A little complicated due to the multiple steps involving calculating eigenvalues, minimising the fuzziness, adjusting the boundaries of the weights. | Reduce certain fuzziness in the final results; can be applied to all other fuzzy numbers.                                                                                  |
| Eigenvector method         | Transform the fuzzy matrix into a crisp matrix and then calculate the crisp weights from the crisp matrix.                                                                   | A little complicated, involving defuzzifying the fuzzy matrix and calculating eigenvalue.                                                            | It is worth considering how much this kind of method is about fuzzy AHP since there are no fuzzy weights.                                                                  |
| Fuzzy programming methods  | Iterative algorithms that search every possible value and gradually achieve a solution to a prescribed accuracy.                                                             | Very complicated due to the iterative search and the need of assistant tools to solve the model. The constraint functions are complicated.           | Produce a consistency index while computing the weights.                                                                                                                   |

The main principle of the methods based on eigenvector is to transform the fuzzy matrix to a crisp matrix first, so all the defuzzification methods introduced later can be applied here. With the crisp matrix, researchers can also choose geometric mean or arithmetic mean instead of eigenvector to calculate the crisp weights, for example, Balusa and Gorai (2018). However, Csutora and Buckley (2001) argue that this kind of method is not about fuzzy AHP since there are no fuzzy weights.

## 5.2.4. Fuzzy programming method

Fuzzy programming methods are iterative algorithms that search every possible value and gradually achieve a solution to a prescribed accuracy (Luenberger &amp; Ye, 2008). The advantage of programming methods is producing a consistency index while computing the weights. But they require more computational effort than other aggregation methods. Mathematical models have to be established first, and assistant tools like Excel solver are needed to solve the models. Rezaei, Ortt, and Scholten (2013), Rezaei, Fahim, and Tavasszy (2014) use a fuzzy non-linear programming method to derive crisp weights from a fuzzy comparison matrix, which saves the efforts to defuzzify. This method first distinguishes TFNs from their reciprocals and then defines the non-linear model as Eq. (36) where wi is the weight and k is a variable that measures the degree of membership of the fuzzy feasible area (i.e. the height of the intersection region of the fuzzy judgements).

<!-- formula-not-decoded -->

Solving the problem described in Eq. (36) results in the optimal crisp weight vector W* and k *. k * &gt; 0 indicates that all solution ratios approximately satisfy the fuzzy judgement, i.e. l ij e 6 w  i = w  j   e 6 uij . It means that the pairwise comparisons are approximately consistent. k * as a fuzzy consistency index will be discussed in Section 7.2.1. Eq. (36) is an extension to the programming method proposed by Mikhailov and Tsvetinov (2004) in Eq. (62).

Mirhedayatian et al. (2013) develop a programming model based on Data Envelopment Analysis to calculate the fuzzy weight f Wi ¼ wil ; wim ; wih ð Þ as follows:

<!-- formula-not-decoded -->

## 5.2.5. Fuzzy interval geometric mean and IFWA

Fuzzy interval geometric mean as Eqs. (20) and (21) also calculates the weights from the pairwise comparison matrix of interval type-2 fuzzy sets, for example Celik and Akyuz (2018) and Görener et al. (2017).

Similarly, IFWA operators, introduced in aggregation for group decisions, are also applied to calculate the weights from the matrix of intuitionistic fuzzy sets. The calculation procedure shown in Eq. (22) is used by Büyüközkan et al. (2019).

## 5.3. Short discussion

Various methods are available to aggregate TFNs while few methods exist for interval type-2 and intuitionistic fuzzy sets, which indicates a potential research topic of exploring more applicable aggregation means for the latter two types of fuzzy sets. There are no specific choice rules as to which method should be used for group decisions. Different methods are introduced for different situations. A general guidance is suggested as shown in Fig. 13. The appropriate method(s) emerge(s) by answering the subsequent questions. These methods are also summarised in Table 2 in terms of their characteristics, complexity of the computation and extension (how they can be extended) to help the choice.

It can be seen from Table 2 that the mean methods have wider application because they are easier to implement and produce valid results. The arithmetic mean has been adapted to intuitionistic fuzzy sets and the geometric mean has been adapted to interval type-2 fuzzy sets and intuitionistic fuzzy sets. Arithmetic mean should also be applicable to aggregate interval type-2 fuzzy sets since geometric mean can be expressed as the exponential of the arithmetic mean of logarithms. Max-min method with geometric mean has been used to aggregate crisp values into a TFN while max-min with arithmetic mean should also work. It is worth studying whether and how the mean methods can be extended to other types of fuzzy sets.

The choice as to which method is used for weights/priorities also first depends on the chosen type of fuzzy set. A general guidance is presented in Fig. 14. These methods are summarised in Table 3 in terms of the underlying principle, the complexity of the computation and the pros and cons.

## 6. Defuzzification method

Defuzzification converts the fuzzy results produced by aggregation methods into crisp values. Compared with a fuzzy value, a crisp value is more intuitive and easier for the final comparison because fuzzy sets have partial ordering. As shown in Fig. 15, this section discusses the defuzzification methods for type-1 fuzzy set and then for type-2 and intuitionistic fuzzy sets.

## 6.1. Defuzzification method for type-1 fuzzy set

There are two dominant defuzzification methods applied by researchers, i.e. centroid method and extent analysis method. 33 papers apply the centroid method and 50 paper use the extent analysis method.

## 6.1.1. Centroid method for type-1 fuzzy set

The centroid method, also called as centre of area (COA) or centre of gravity (COG), is the most prevalent defuzzification method (Ross, 2004). The underlying principle is as Eq. (38) where x* is the defuzzified value, x indicates the element, and l ( x ) is its associated membership function.

R

<!-- formula-not-decoded -->

Fig. 15. Categorisation of the defuzzification methods

<!-- image -->

The centroid method can be translated into different forms when defuzzifying a TFN e C ¼ l ; m ; h ð Þ . For example, Eq. (39) is applied by Sun (2010), Yu et al. (2012), Pitchipoo et al. (2013), Rezaei and Ortt (2013), Ayhan and Kilic (2015), Yayla et al. (2015) and Calabrese et al. (2016; 2019).

<!-- formula-not-decoded -->

Kar (2014, 2015) uses Eq. (40). Awasthi et al. (2018) utilise Eq. (41).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Büyüközkan (2012) defuzzify a TFN by taking a -cut set, e C a , as shown by Eq. (42).

<!-- formula-not-decoded -->

With the a -cut set e C a ¼ l þ m   l ð Þ a ; h   h   m ð Þ a ½  , Eq. (42) can be further transformed as:

<!-- formula-not-decoded -->

Eq. (43) corresponds to Yager's approach (Yager, 1981) that analyses the mean of the elements within an interval. It has been proved by Facchinetti, Ricci, and Muzzioli (1998) that this way takes into consideration both the worst and best results arising from a fuzzy number.

## 6.1.2. The extent analysis method

The extent analysis method (EAM), proposed by Chang (1996), aims to calculate the weights and translate TFNs into crisp values in the fuzzy pairwise comparison matrix. Let F ¼ e Cij h i n -n be a fuzzy pairwise comparison matrix. The fuzzy weight of element i is:

<!-- formula-not-decoded -->

Eq. (48) is actually the fuzzy arithmetic mean as in Eq. (28). The crisp weight of i is determined as the minimal degree of possibility of its fuzzy weight e wi being greater than the fuzzy weights of the others. Given two TFNs e A 1 ¼ l 1 ; m 1 ; h 1 ð Þ and e A 2 ¼ l 2 ; m 2 ; h 2 ð Þ as shown in Fig. 16, The degree of possibility of e A 1 P e A 2 is defined as:





<!-- formula-not-decoded -->

The crisp weight of i is then defined by Eq. (50).





<!-- formula-not-decoded -->

EAM is simple to implement but does not produce proper weights. There is a zero assigned when there is no intersection of the two TFNs. Also, the way of calculating is incorrect because it neglects the role of l 2 and h1 in determining the relative importance. This leads to a big inconsistency between the results and the original judgments. Considering EAM is widely applied, we explain how EAM is problematic in details in the short discussion section.

## 6.1.3. Other methods

Opricovic and Tzeng (2003) propose a defuzzification method, namely Converting the Fuzzy data into Crisp Scores (CFCS), which is applied by Sarfaraz, Jenab, and D'Souza (2012) to rank ERP implementation solutions. Let F ¼ e Cij h i n -n be a fuzzy pairwise comparison matrix and (C1, C2, . . . , Cn) be the n performance criteria. e Cij ¼ l ij ; mij ; hij    ; j ¼ 1 ; 2 ; :::; n is the pairwise comparison of Ci over Cj. The crisp value for each TFN is computed by the following four steps.

Step 1: Normalisation.

<!-- formula-not-decoded -->

h

i

Normalise the matrix. Let F ¼ e Xij n -n be the normalised result; e Xij ¼ xl ij ; xmij ; xhij    .





<!-- formula-not-decoded -->

Step 2: Compute left ( ls ) and right ( hs ) normalised values for i = 1, 2, . . . n. j = 1, 2, . . . , n.

 

<!-- formula-not-decoded -->



Step 3: Compute total normalised crisp value.

<!-- formula-not-decoded -->

Step 4: Compute crisp values. Let aij be the crisp value correspondent to e Cij .

<!-- formula-not-decoded -->

A major problem of CFCS we have noticed is that it produces varied crisp values for a particular TFN. This is due to the normalisation in step 1. Consider one scenario with 2 criteria and another with 3 criteria. Table 4 shows their comparisons against C1. The crisp values for TFN (5, 7, 9) are different in the two scenarios.

Mathematically, defuzzifying a fuzzy set is the process of rounding it off from its location to the nearest vertex, which reduces the set into the most typical or representative value (Ross, 2004). However, CFCS contradicts this principle because the defuzzification result changes as the number of criteria/alternatives changes and also depends on the values of the other TFNs in the comparison matrix. It seems not a suitable defuzzification method.

Mean of limits of a TFN is another method. Alaqeel and Suryanarayanan (2018) apply the geometric mean to the upper and lower limits (i.e. L and h ) for a crisp value. This way of defuzzification ignores the middle value of a TFN, which might lead to improper weight.

Index of optimism is also used to defuzzify the fuzzy numbers through their a -cut sets, which has been introduced in Section 5.2.3, for example, Jung (2011), Soroor et al. (2012), Beikkhakhian et al. (2015) and Büyüközkan et al. (2017).

Fig. 16. Fuzzy Triangular Number of e A 1 and e A 2

<!-- image -->

Table 4 Defuzzification results by CFCS.

| Criterion              | TFNs                   | Normalised fuzzy value   |   Crisp value |
|------------------------|------------------------|--------------------------|---------------|
| Scenario 1: 2 criteria | Scenario 1: 2 criteria |                          |               |
| C 1                    | (1, 1, 1)              | (0, 0, 0)                |             1 |
| C 2                    | (5, 7, 9)              | (1/2, 3/4, 1)            |         6.867 |
| Scenario 2: 3 criteria | Scenario 2: 3 criteria |                          |               |
| C 1                    | (1, 1, 1)              | (0, 0, 0)                |             1 |
| C 2                    | (5, 7, 9)              | (4/9, 6/9, 8/9)          |         6.916 |
| C 3                    | (6, 8, 10)             | (5/9, 7/9, 1)            |          7.86 |

Other applicable defuzzification methods are max membership principle, weighted average and mean of maxima (Ross, 2004) but they are rarely applied in the selection literature.

## 6.2. Centroid method for type-2 fuzzy set

The centroid of an interval type-2 fuzzy set is the union of the centroids of all its embedded type-1 fuzzy sets. Based on this principle, Kahraman, Sari, and Turanog ˘lu (2014) propose Eqs. (56) and (57) to defuzzify triangular and trapezoidal interval type-2 fuzzy set.





<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

In Eq. (56), a is the maximum membership degree of the lower membership function; a3 U and a1 U are the largest and least possible value of the upper membership function respectively; a2 U is the most possible (middle) value of the upper membership function; a3 L and a1 L are the largest and least possible value of the lower membership function; a2 L is the middle value of the lower membership function.

In Eq. (57), H1 and H2 are the two maximum membership degrees; a4 U , a3 U a2 U and a1 U are the largest, the two middle and least possible values of the upper membership function respectively; a4 L , a3 L a2 L and a1 L are the largest, the two middle and least possible values of the lower membership function respectively. Celik and Akyuz (2018) and Ayodele, Ogunjuyigbe, Odigiea, and Munda (2018) use this equation in their fuzzy AHP model.

## 6.3. Intuitionistic fuzzy entropy for defuzzification

The defuzzification methods for type-1 and type-2 fuzzy sets transform fuzzy values to representative crisp values. Fuzzy entropy also generates crisp values but measures the fuzziness of the set. Whether it can be considered as a weight is worth considering. Büyüközkan et al. (2019) treats the intuitionistic fuzzy entropy w   i as the crisp weight value. Let wi ¼ l i ; v i ; p i  be intuitionistic fuzzy weight. Eq. (58) is used to calculate w   i .

<!-- formula-not-decoded -->

Büyüközkan et al. (2019) have not provided the reference or proof for this equation. Based on the format of the equation, it might be an extension of Shannon's function as Eq. (59), which is used to measure the fuzziness of type-1 fuzzy set (Zimmermann, 2001).

Fig. 17. Two example cases:(a) m1 = m2 ; (b) m2 &gt; m1 but m1 , m2 , l 1 , h2 are very close to each other

<!-- image -->

Table 5 Summary of defuzzification methods.

| Method            | Principle                                                                                    | Complexity                                                                                                            | Pros and cons                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Centroid method   | Calculate the centre of the area defined by the fuzzy number.                                | Very simple (single equation), involving arithmetic addition and division                                             | Have various forms but Eq. (40) has been well proved. Its application has been extended to type-2 fuzzy set.                       |
| EAM               | Calculate the smallest possibility of one TFN bigger than another as the defuzzified result. | Simple, involving arithmetic and min operations but having few steps to follow.                                       | Cannot derive proper crisp weights.                                                                                                |
| CFCS              | Calculate the crisp value based on the normalised fuzzy numbers.                             | A little complicated, involving arithmetic, min/max, and normalisation operations and having several steps to follow. | Produce varied crisp values for a particular TFN. It seems not a proper defuzzification method.                                    |
| Mean of limits    | Calculate the geometric mean of the upper and lower limits of a TFN.                         | Very simple (single equation), involving arithmetic multiplication and rooting.                                       | Might result in improper results due to ignoring the middle value of a TFN.                                                        |
| Index of optimism | Calculate the crisp value based on the a -cut of a TFN and the index of optimism l .         | Very simple (single equation), involving arithmetic operations.                                                       | The experts need to set values for the two parameters a and l . But it seems little literature discusses how to set proper values. |
| Fuzzy entropy     | Calculate the fuzziness of the fuzzy set.                                                    | Simple (single equation), involving arithmetic and logarithm operations.                                              | Be used to defuzzify intuitionistic fuzzy set. But fuzzy entropy is used to measure the fuzziness.                                 |

Fig. 18. Categorisation of the consistency measurement methods

<!-- image -->

<!-- formula-not-decoded -->

## 6.4. Short discussion

EAM is applied by a large proportion of articles (50 out of the total 109 papers, 46%), which corresponds to the survey results (i.e. 109 out of the 190 papers) by Kubler et al. (2016). However it has been criticised by many researchers for its significant shortcomings in deriving the weights/priorities. Zhu, Jing, and Chang (1999) notice that EAM cannot deal with the comparison if there is no intersection between two fuzzy numbers. This problem is solved by assigning a value of 0 in the case of no intersection and Eq. (49) is extended as:





<!-- formula-not-decoded -->

Introducing this zero weight leads to some criteria or alternatives being ignored in the analysis and results in a wrong decision (Wang, Luo, &amp; Hua, 2008).

EAM is still inappropriate to attain the relative importance even if every two fuzzy numbers have intersection. Let e A 1 ¼ l 1 ; m 1 ; h 1 ð Þ and e A 2 ¼ l 2 ; m 2 ; h 2 ð Þ be two TFNs. Consider the scenario in Fig. 17 (a) that m1 = m2 but l 2 &lt; l 1 and h2 &lt; h1 . e A 1 should have a priority above e A 2 , but according to Eq. (49), when m1 = m2 , V e A 1 P e A 2   ¼ V e A 2 P e A 1   ¼ 1 that the two TNFs are of the same priority. Consider another case as Fig. 17 (b). m2 = m1 + e where e is a very small positive number close to 0. h2 = m2 + e , l 1 = m1 -e , l2 = m2 + a , h1 = m1 + a , where a is a large positive number. According to Eq. (49), V e A 2 P e A 1   ¼ 1 &gt; V e A 1 P e A 2   which indicates e A 2

has a higher priority. However, it is apparent that e A 1 should be preferred over e A 2. The ordinate of the highest intersection in EAM cannot represent the degree of possibility of e A 2 P e A 1 or their relative weights, because it only depends on the two lines defined by m2 , h2 and l 1 , m1 respectively. Values l 2 and h1 should also play a role to determine the relative importance and neglecting them leads to improper weights. EAM has the advantage of ease of use and simple logic, which might be the reason why it is still widely applied.

It seems that centroid method is the most suitable choice for type-1 and type-2 fuzzy sets as concluded in Table 5.

## 7. Consistency measurement

Consistency measurement ensures that there are limited contradictions among the pairwise comparisons in the matrix. It is a necessary step because a big inconsistency may indicate a lack of understanding of the problem. There are two ways of measuring the consistency of the fuzzy pairwise comparison matrix. 'Crisp consistency' is computed by translating the fuzzy matrix to a representative crisp one. 'Fuzzy consistency' calculates a consistency index directly from a fuzzy matrix. Fig. 18 outlines the methods.

## 7.1. Crisp consistency

The principle of crisp consistency is to defuzzify the fuzzy matrix first and then use Saaty's consistency ratio (CR) (see Jung (2011), Kilincci and Onal (2011), Büyüközkan (2012), Pitchipoo et al. (2013), Calabrese et al. (2016; 2019), Büyüközkan et al. (2017) and Ayodele et al. (2018)). The implementation would be different in defuzzification as there are various defuzzification methods as introduced in Section 6. The defuzzified matrix with a CR less than 0.1 is considered as adequately consistent.

<!-- formula-not-decoded -->

CI is consistency index; k max is the max eigenvalue of the comparison matrix; RI is the random index. The value of RI depends on the size of the matrix that can be looked up in Saaty (2008).

Büyüközkan et al. (2019) check the intuitionistic fuzzy matrix by Saaty's method, but calculate the consistency ratio in the following way:

<!-- formula-not-decoded -->

where n is the number of the elements and p ij is the degree of nondeterminacy of the membership. The value of RI is taken from Saaty's method. CR is considered acceptable if less than or equal to 0.1. However, they did not explain why the ratio from Eq. (62) works to measure the consistency. It seems that mathematical proof is needed.

## 7.2. Fuzzy consistency

This way of measuring consistency usually requires establishing and solving fuzzy programming models. The consistency index is derived along with the weights of criteria from the models. This section first introduces various programming models starting from the explanation of their origin and then presents a different fuzzy consistency method.

## 7.2.1. Fuzzy programming method

According to Buckley (1985), the fuzzy comparison matrix F ¼ e Aij h i n n is consistent if and only if:

-

<!-- formula-not-decoded -->

The approximate equal '  ' between two fuzzy numbers e A 1 and e A 2 whose membership functions are m A1 ( x ) and m A2 ( x ) is defined as:

<!-- formula-not-decoded -->



<!-- formula-not-decoded -->



itive fraction less than or equal to 1. Literally speaking, e A 1 and e A 2 are approximately equal if e A 1 is not greater than e A 2 and e A 2 is not greater than e A 1 .

Based on Eq. (63), Arbel (1989) further proves that a fuzzy comparison matrix can be considered as consistent when the ratio of the weight wi of criterion Ci to the weight wj of criterion Cj is within the upper and lower bounds of the corresponding TFN e Aij ¼ l ij ; mij ; hij    , i.e.

 

<!-- formula-not-decoded -->



This equation is the base of the following non-linear programming model (Mikhailov &amp; Tsvetinov, 2004). The outcomes of fuzzy programming method provide the optimal crisp weight vector and a consistency index k .

<!-- formula-not-decoded -->

That the optimal value k * &gt; 0 means that all solution ratios completely satisfy the fuzzy judgements. A negative value indicates that the judgements are inconsistent.

As discussed by Mikhailov (2004), in inconsistent cases, there does not exist a weight vector that satisfies all inequalities in Eq. (65) simultaneously. But it is reasonable to try to find a vector satisfying all inequalities as well as possible, which introduces 'approximately less than or equal to', i.e. ' e 6 ', to Eq. (65).

<!-- formula-not-decoded -->

The following non-linear programming model is then proposed, which adds a tolerance parameter pij . This parameter extends the feasible region by extending the lower and upper bounds.

max k

s : t :

<!-- formula-not-decoded -->

That the optimal value k *  1 indicates consistent fuzzy judgements. For a weak consistency but the solution ratio is within the extended bounds, k * is a value between 1 and 0, depending on the degree of inconsistency and the values of the tolerance parameters. Chen and Yang (2011) use Mikhailov (2004)'s method to examine the consistency. In the first example of Chen and Yang's paper (i.e. Example 1), a consistency index value 0.7602 is obtained so they consider the comparison matrix consistent. But according to Mikhailov (2004), a value within [0, 1] should be weakly inconsistent.

## 7.2.2. Geometric consistency index

Kar (2014, 2015) apply Geometric consistency index (GCI) to the fuzzy matrix F ¼ e Aij h i n -n as Eq. (69):

<!-- formula-not-decoded -->

If GCI F ð Þ 6 GCI   , the matrix is consistent. GCI   are fixed values that GCI   = 0.31 for n = 3, GCI   = 0.35 for n = 4 and GCI   = 0.37 for n &gt; 4.

This consistency measure is proposed by Crawford and Williams (1985) for crisp matrix. The thresholds of CGI are determined by Aguarón and Moreno-Jiménez (2003) who provide an interpretation of GCI analogous to the consistency index in AHP proposed by Saaty. It checks the consistency only after the weights of alternatives are obtained. Considering that row geometric mean instead of right eigenvector is used for the prioritisation, the computation efforts do not increase compared with Saaty's method. The problem when applying this measure to the fuzzy matrix is how to calculate the logarithm of a fuzzy number. Kar (2014, 2015) do not explain this and it seems that crisp values are used though the equation presents fuzzy numbers. There is also a mistake in their used equation (i.e. Eq. (69)) that the square should be placed in the outer bracket as shown in Eq. (70).

<!-- formula-not-decoded -->

## 7.3. Short discussion

Crisp consistency based on Saaty's method is mostly used and suitable for all types of fuzzy sets. Mahmoudzadeh and Bafandeh (2013) explain why a crisp consistency can represent the consistency of the fuzzy matrix. In the case of calculating a fuzzy inconsistency ratio, they have proved that if the comparison matrix obtained from an a = 1 cut set of e A is consistent, then the original fuzzy comparison matrix is consistent. For a TFN e A = ( l , m , n ), its a = 1 cut set reduces to a crisp number, i.e. A a = m . The consistency check of the fuzzy matrix F ¼ e Aij h i n -n becomes the check of the crisp matrix F a =1 = [ mij ] n -n . Saaty's consistency ratio then can be used.

Table 6 summarises the methods to measure the consistency in terms of the underlying principle, the complexity of the computation and the pros and cons.

## 8. Conclusion and future research

How the expert's judgements are represented by fuzzy sets is fundamental to the development of fuzzy AHP. The choice of the fuzzy sets determines the overall calculation complexity of the model. Among the three types of fuzzy sets, type-1 fuzzy set requires the least effort, followed by intuitionistic fuzzy set and interval type-2 fuzzy set. This is because the operations on fuzzy sets are defined via the elements and their memberships, as compared in Table 7.

Aggregation is the key operation to produce the weights/priorities. Different techniques may produce different results and have distinct performance. According to the experimental analysis of Ahmed and Kilic (2018), the logarithmic least-squares method outperforms the fuzzy geometric mean and the fuzzy geometric mean outperforms the fuzzy arithmetic mean. To the best of our knowledge, no comparison has been done between these mean methods and other methods such as lambda-max, which could be a future research topic.

Defuzzification assists the comparison of the results because crisp values are more intuitive than fuzzy values. It also simplifies the calculation if the matrix is defuzzified before computing the weights, which translates a fuzzy matrix into a crisp matrix. The consistency check ensures that the results are produced based on effective judgments since inconsistency may indicate a lack of understanding of the problem.

As indicated in Fig. 1, there is no fixed execution sequence of synthesising multiple judgments, checking consistency, calculating weights/priorities and defuzzifying the fuzzy values. However, the sequence along with the chosen techniques influences the effect of the fuzzy AHP model.

## 8.1. Suggestion on the choice of sequence and technique

This review concludes the techniques used to develop a fuzzy AHP model in the literature. Except the problematic ones (i.e. EAM and CFCS), it is hard to identify which one is the best because each has its advantages and varies in their underlying principles as discussed in the previous sections. Experts could determine according to their practical context. As discussed in Section 4.5, if they are relatively confident in their judgement, then type-1 fuzzy set can be chosen. If preferring a simple but practical tool, they can use geometric mean for aggregation, centroid method for defuzzification and Saaty's method for consistency measurement. If the experts have good mathematical background and look for more optimal solutions, fuzzy programming method is a nice option. But the following should be avoided when building the fuzzy AHP model.

## 8.1.1. Using fuzzy arithmetic mean for aggregation and centroid method for defuzzifying when symmetrical TFNs are used for judgement representation.

For a symmetrical TFN e Ci ¼ l i ; mi ; hi ð Þ , there is mi   l i ¼ hi   mi ¼ D i . Symmetrical TFNs are commonly used to define the fuzzy scales as seen in Section 4.4. Applying fuzzy arithmetic mean as Eq. (10) to such TFNs for aggregation also produces a symmetrical TFN e C :

!

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Defuzzifying a symmetrical TFN e C ¼ l ; m ; h ð Þ by the centroid method as Eqs. (39), (40) or (41), a crisp value equal to m is obtained.

In this case, if the model is built in the sequence where the TFNs of the pairwise judgements is defuzzified before calculating the weights, the problem of solving a fuzzy AHP model e F ¼ e Cij h i n -n ¼ l ij ; mij ; hij    - n -n reduces to solving an AHP model F ¼ mij - n -n . The use of a fuzzy scale does not make any sense because it is equal to the use of crisp scale with the same level.

If the sequence of steps is used where the weights are calculated and then defuzzified, the method will produce the same unnormalised weight vector W with AHP model that calculates the weights by arithmetic mean.

Table 6 Summary of the methods for consistency measurement.

| Method                      | Principle                                                                                                                                                                                             | Complexity                                                                                                  | Pros and cons                                                                                                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Saaty's method              | Check the consistency of the defuzzified fuzzy matrix by Saaty's consistency ratio.                                                                                                                   | Simple (simple equations), involving arithmetic operations and calculation of max eigenvalue of the matrix. | The choice of defuzzification methods may influence the results since different defuzzification methods could produce different crisp matrices. It is extended to type-2 and intuitionistic fuzzy sets. |
| Fuzzy programming method    | Establish the objective and constraint functions based on that the weight ratio of a criterion to another is bounded by the lower and upper limits of the TFN representing their pairwise comparison. | Very complicated due to the iterative search and the need of assistant tools to solve the model.            | It generates the consistency ratio while producing the weights.                                                                                                                                         |
| Geometric consistency index | Calculate the consistency ratio based on the distance between pairwise comparison and the weight ratio which are taken the logarithm first.                                                           | Simple (simple equations), involving arithmetic and logarithm operations.                                   | It is hard to apply the equation to fuzzy set because little research has been done for logarithm calculation on fuzzy sets. It checks the consistency after the weights are obtained.                  |

<!-- formula-not-decoded -->

)

## 8.1.2. Checking the consistency after multiple judgements synthesis.

The inconsistent judgement from an individual expert might be overlooked if checking the consistency after synthesising the multiple judgements. Consider the following two fuzzy comparison matrices e F 1 and e F 2 from two experts and their synthesised matrix e Fagg .

<!-- formula-not-decoded -->

After defuzzifying the matrices by the centroid method (Eq. (39)), the consistency is checked using Saaty's method. The consistency ratios of the three matrices are 0.0036, 0.209 and 0.066 respectively. If the consistency is measured after synthesis, the judgements are considered consistent ( CR e Fagg =0.066 &lt; 0.1) and the weights are calculated based on actually inconsistent judgement from expert 2 ( CR e F 2 =0.209 &gt; 0.1). The almost perfect consistency from expert 1 ( CR e F 1 =0.0036) compensates the big inconsistency from expert 2 via aggregation.

## 8.2. Future work

This section presents some open questions that arise from the review and the discussion of the techniques. We hope these questions could inspire researchers for future work.

## 8.2.1. Open questions on fuzzy scale

There are 5, 6, 7 and 9-level scales that have been applied to describe the relative importance between every two criteria/alter- natives. There seems no explanation on the choice of the scale in the research that have applied the fuzzy scale.

Table 7 Operation comparisons between fuzzy sets.

| Fuzzy set                | Operation on                         | Membership value   |
|--------------------------|--------------------------------------|--------------------|
| Type-1 fuzzy set         | Element, membership                  | Crisp values       |
| Intuitionistic fuzzy set | Element, membership, non- membership | Crisp values       |
| Type-2 fuzzy set         | Element, membership                  | Type-1 fuzzy sets  |

Table 8 Summary of the techniques.

|                                                                                          | Simple                                                                                                                                               | Complicated                                                                                             | Very complicated                                               |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Representation for pairwise comparison Aggregation for group decision weights/priorities | TFN, TraFN Arithmetic mean, Geometric mean, Max-min method with arithmetic mean, Max-min method with geometric mean Arithmetic mean, Geometric mean, | Intuitionistic fuzzy set Method based on Consensus degree Logarithmic least-squares, Lambda-max method, | Trapezoidal interval type-2 fuzzy set Fuzzy programming method |
| Defuzzification                                                                          | Centroid method, EAM, Mean of limits, Index of optimism, Fuzzy entropy                                                                               | Eigenvector method CFCS                                                                                 |                                                                |
| Consistency                                                                              | Saaty's method, Geometric consistency index                                                                                                          |                                                                                                         | Fuzzy programming method                                       |

Saaty (2008) discusses that psychologically people are able to distinguish between high, medium and low at one level and for each in a second level below to also distinguish between high, medium and low. This produces nine different categories, where the smallest is (low, low) and the highest is (high, high). This is the principle that AHP has a 9-level scale for the top of pairwise comparisons as compared with the lowest value on the scale. A scale provides a reference for comparison. It is reasonable that other scales exist as long as they cover the spectrum of possibilities and discriminate the alternatives in their application context. Small changes in judgement lead to small changes in the derived weights/priorities (Wilkinson, 1965). When two or more scales are applicable to one problem, for example, supplier selection where the four types of fuzzy scales can be used. Several questions arise:

Q1: Do different scales have different impacts on the final result in terms of accuracy and reliability?

To define a particular expression in the scale, various types of fuzzy sets are used such as type-1 and type-2 fuzzy sets. If using the same type, the choices of the fuzzy numbers by the researchers can also be different. For example, Zimmer et al. (2017) specify 'moderately important' with g 1 : 5 while most research adopts e 2 in the 5 level scale. The same fuzzy number may also be defined differently. As discussed in Section 4.4, e 9 is interpreted as (9, 9, 9) or (8, 9, 10). This leads to the concern:

Q2: What are the impacts on the results if using different fuzzy sets regarding the types, the chosen fuzzy numbers and the definitions on the same scale?

## 8.2.2. Open questions on aggregation

Some aggregation methods accommodate the weights of the experts, which are assumed as known. Experts may have different capabilities since they come from different functional departments, such as purchasing, financing, engineering and quality assurance. People from purchasing have better knowledge to compare the cost related criteria while those from quality assurance are more reliable to analyse the quality related criteria. It is hard to judge which expert overall is more important than another. Two questions arise.

Q3: When experts judge the relative importance between criteria, who judges their importance?

- Q4: When people have distinctive expertise, how is their importance judged?

One possible solution is that the experts evaluate the criteria within their capabilities, and those of the same capability are weighted by their experience such as the working years, reputation and position in the department. This brings a new research topic in decision-making.

## 8.2.3. Open questions on consistency

When research focuses on the consistency measurement problem, it seems little attention has been paid to dealing with inconsistency. If the matrix is consistent, then the process continues. Otherwise, the experts need re-compare the criteria/alternatives until the consistency ratio is within the acceptable range. This is the usual solution to adjust the matrix. However, this is still insufficient because it is not clear that:

Q5: Which part of matrix needs adjustment?

Q6: How can the inconsistent part be adjusted to meet the condition?

To re-compare the whole matrix consumes effort, especially when the number of criteria/alternatives is large. In addition, recomparison cannot guarantee the consistency of the judgements if the experts have no idea about the adjustment. The answers to the above two questions might help make decision making more efficient.

## 8.3. Concluding remarks

Fuzzy set theory has been proposed as a valid means of dealing with imprecision and vagueness. However, as discussed in Kubler et al. (2016), the extent of benefits brought by introducing this fuzzy paradigm to AHP is not clear, especially given that Saaty (2006) argued that the pairwise judgements are fuzzy enough. Using fuzzy numbers is not only for fuzziness (certain inconsistency among the judgements) but also for 'uncertainty' or 'hesitation' of the experts towards their judgements. Different types of fuzzy numbers provide choices to express 'not sure' to different extents. Although the extent to which fuzzy AHP solves the problem of uncertainty is disputed, it is a simple and useful decisionmaking method that has been widely applied. It retains the advantages of AHP, i.e. structuring the problems, calculating both weights and priorities and well-proved mathematical properties. This paper provided guidance on how to choose appropriate techniques for building fuzzy AHP models in term of representation, aggregation, defuzzification and consistency. In offering the guidance, this research traced the origin of the methods and matched the context to the techniques. The methods are also analysed regarding their characteristics, complexity and extension.

TFN stands out from other types of fuzzy set, because of its simplicity in representing the judgements. It seems able to deal with uncertainty in most cases (applied by 91% of reviewed articles in various fields), but is limited because the degree of membership is expressed as real numbers. In the cases where the decision makers find it difficult to determine the memberships, trapezoidal interval type-2 or intuitionistic fuzzy sets can help. Mean methods are mostly used in aggregating group decisions and deriving weights, for the three reviewed types of fuzzy sets. In particular geometric mean has proved a valid approach of approximating the eigenvalues of a matrix. The fuzzy programming methods are also efficient ways of computing the weights because they also generate a consistency index. But they require more computational effort. Centroid methods are valid means of defuzzifying fuzzy sets, which come in several forms. The one of Eq. (40) is a nice choice, because it considers both the worst and best results arising from a fuzzy number. This equation can also be inferred from Yager's approach and has been proved by Facchinetti et al. (1998). It is worth mentioning that the EAM is problematic as shown in the discussion but still widely applied because of its ease of use in obtaining the weights and crisp values. This indicates that 'a simple but practical' method is what the decision makers need.

Fig. 19. Paths of building fuzzy AHP models

<!-- image -->

Therefore, the reviewed techniques are summarised according to their complexity as listed in Table 8. More properties can be found in Tables 2 and 3 and Tables 5 and 6. It is also noticed that more than half of articles (61 out of 109 articles) do not check the consistency of the pairwise comparison matrix. Consistency measurement is necessary to reduce the contradictions among different decision makers.

Fig. 19 presents the paths with simple and commonly used techniques in the four important aspects of a fuzzy AHP model, starting with the types of fuzzy sets. Figs. 11, 13 and 14 explains which fuzzy set and aggregation methods should be chosen. The appropriate techniques(s) emerge(s) by answering the subsequent questions.

This research has adopted a two-stage approach to examine the fuzzy AHP models used in different decision-making topics in industry. Although many techniques have been reviewed, there may still be ones that have been overlooked. The guidance of this paper could help to categorise and analyse the techniques by reflecting what they describe, when they are applicable, how they are defined and the complexity of the computation.

## Funding

This research was supported by the Natural Science Foundation of Jilin Province of China (Grant No. 20180101035JC) and the Education Department of Jilin Province of China (Grant No. JJKH20200796KJ).

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper

## Appendix

It is noted that the number after the types of fuzzy sets in the column 'Pairwise' indicates the levels of the fuzzy scales. For example, 'TFN 9 0 means this paper takes a 9-level scale based on TFNs.

Table A.9 Supplier selection articles with the techniques in their fuzzy AHP models.

|       | Authors                                        | Industry               | With                        | Representation     | Representation           | Aggregation                            |                                                    | Defuzzification           | Consistency   |
|-------|------------------------------------------------|------------------------|-----------------------------|--------------------|--------------------------|----------------------------------------|----------------------------------------------------|---------------------------|---------------|
|       |                                                |                        | method(s)                   | Pairwise           | Performance              | Weight/Priority                        | Multi-experts                                      |                           |               |
| 1     | Chan, Kumar, Tiwari, Lau, and Choy (2008)      | Manufacturing          | -                           | TFN 9              | -                        | EAM                                    | -                                                  | EAM                       | -             |
| 2     | Büyüközkan, Feyziog ˘ lu and Nebol (2008)      | e-logistics            | TOPSIS                      | TFN 5              | TFN                      | EAM                                    | -                                                  | EAM                       | -             |
| 3     | Yang et al. (2008)                             | -                      | Non- additive fuzzy measure | TFN 9              | TFN                      | Geometric mean                         | Geometric mean                                     | COA                       | -             |
| 4     | Celik, Deha Er and Ozok (2009)                 | Maritime               | -                           | TFN 5              | -                        | EAM                                    | -                                                  | EAM                       | -             |
| 5     | Lee (2009)                                     | Manufacturing          | -                           | TFN 9              | -                        | EAM                                    | Geometric                                          | EAM                       | -             |
| 6     | Wang et al. (2009)                             | -                      | TOPSIS                      | TFN 5              | TFN                      | Lambda-max                             | mean Geometric mean                                | -                         | Saaty         |
| 7     | Aydin and Kahraman (2010)                      | Manufacturing          | -                           | TraFN              | -                        | Arithmetic mean (defuzzify first)      | Weighted arithmetic                                | COA                       | -             |
| 8     | Chen et al. (2010)                             | Manufacturing          | -                           | TFN 7              | -                        | Arithmetic mean                        | mean Max-min for TFN construction & Arithmetic     | COA                       | -             |
| 9     | Chen and Hung (2010)                           | Pharmaceutical         | TOPSIS                      | TFN 6              | TFN                      | Geometric mean                         | mean Arithmetic (alternative)& Geometric           | -                         | Saaty         |
| 10    | Kuo, Lee, and Hu (2010)                        | Manufacturing          | DEA                         | TFN 5              |                          | Lambda-max                             | mean (criteria) Average but not specified          | -                         | Saaty         |
| 11    | S ß en, S ß en, and Bas ß ligil (2010)         | Electronic             | Max-min                     | TFN 9              | Crisp (criteria weights) | EAM                                    | -                                                  | EAM                       | -             |
| 12    | Sun (2010)                                     | -                      | TOPSIS                      | TFN 9              | TFN                      | Geometric mean                         | -                                                  | COA (but fuzzy values are | -             |
| 13    | Chen and Yang (2011)                           | -                      | TOPSIS                      | TFN 6              | TFN                      | Modified EAM                           | Geometric mean                                     | used) EAM                 | FP            |
| 14    | Chiouy, Chou, and                              | Electronic             | -                           | TFN 9              | -                        | Lambda-max                             | Geometric                                          | -(not                     | Saaty         |
| 15    | Yeh (2011) Ertay et al. (2011)                 | Pharmaceutical         | ELECTRE III                 | TFN 9              | Crisp                    | EAM                                    | mean Weighted Geometric                            | specified) EAM            | -             |
| 16    | Jung (2011)                                    | Manufacturing          | GP for allocation           | TFN 5              | -                        | Geometric mean                         | mean -                                             | Index of                  | Saaty         |
| 17    | Kilincci and Onal (2011)                       | Manufacturing          | -                           | TFN 5              | -                        | EAM                                    | -                                                  | optimism EAM              | Saaty         |
| 18    | Zeydan, Çolpan, and Çobanog ˘lu (2011)         | Automobile             | TOPSIS                      | TFN 9              | TFN 7                    | EAM                                    | Arithmetic mean (for performance, no for criteria) | -                         | Y no method   |
| 19    | Yücenur, Vayvay,                               | Logistics              | -                           | TFN -(not mention) | -                        | EAM                                    | -                                                  | EAM                       | -             |
| 20    | and Demirel (2011) Büyüközkan (2012)           | Automotive             | TOPSIS                      | TFN 11             | TFN                      | Geometric mean                         | Weighted arithmetic                                | COA                       | Saaty         |
| 21    | Kubat and Yuce                                 | -                      | GA                          | TFN 9              | -                        | EAM                                    | mean -                                             | EAM                       | -             |
| 22    | (2012) Shaw, Shankar, Yadav, and Thakur (2012) | Manufacturing          | LP for allocation           | TFN 9              |                          | EAM                                    | Geometric mean                                     | EAM                       | -             |
| 23    | Soroor et al. (2012)                           | -                      | -                           | TFN 9              | -                        | Eigenvector based on index of optimism |                                                    | Index of optimism         | Saaty         |
| 24 25 | Yu et al. (2012) Zouggari and                  | Manufacturing -        | MP TOPSIS                   | TFN - TFN 5        | - TFN                    | Geometric mean EAM                     | - Max-min                                          | COA EAM                   | - Saaty       |
|       | Benyoucef (2012) Alinezad et al. (2013)        | Pharmaceutical         | -                           | TFN 4              | -                        | EAM                                    | -                                                  | EAM                       | -             |
| 26 27 | Ghorbani, Mohammad Arabzad, and Shahin (2013)  | agricultural machinery | TOPSIS                      | TFN 5              | TFN                      | EAM                                    | -                                                  | EAM                       | -             |
| 28    | Kannan et al. (2013)                           | Automobile             | TOPSIS MP for               | TFN 9              | TFN 9                    | EAM                                    | Geometric mean                                     | EAM                       | Saaty         |

allocation optimism

Table A.9 ( continued )

|       | Authors                                                       | Industry              | With                          | Representation                  | Representation                | Aggregation                                                                     | Aggregation                    | Defuzzification         | Consistency   |
|-------|---------------------------------------------------------------|-----------------------|-------------------------------|---------------------------------|-------------------------------|---------------------------------------------------------------------------------|--------------------------------|-------------------------|---------------|
|       |                                                               |                       | method(s)                     | Pairwise                        | Performance                   | Weight/Priority                                                                 | Multi-experts                  |                         |               |
| 29    | Pitchipoo et al.                                              | electroplating        | GRA                           | TFN 9                           | -                             | Crisp weights by                                                                | -                              | COA                     | Saaty         |
| 30    | (2013) Rezaei and Ort                                         | food                  | -                             | TFN 7                           | TFN 7                         | defuzzifying first Arithmetic mean                                              | -                              | COA                     | -             |
| 31    | (2013) Roshandel, Miri- Nargesi, and Hatami- Shirkouhi (2013) | material              | TOPSIS                        | TFN 5                           | TFN                           | Arithmetic mean                                                                 | Arithmetic mean                | -                       | -             |
| 32    | Viswanadham and Samvedi (2013)                                | -                     | TOPSIS                        | TFN 5                           | TFN                           | EAM                                                                             | Arithmetic mean (in            | EAM                     | -             |
| 33    | Hashemian et al. (2014)                                       | Diary                 | PROMETHEE                     | TFN 5                           | TFN                           | EAM                                                                             | performance) Geometric         | EAM                     | -             |
| 34    | Kar (2014)                                                    | Manufacturing         | MP                            | TFN 5                           | -                             | Geometric mean                                                                  | mean Weighted geometric mean   | COA                     | GCI           |
| 35    | Rezaei et al. (2014)                                          | Airline retail        | -                             | TFN 9                           | -                             | FP (non-linear)                                                                 | -                              | FP                      | FP            |
| 36    | Shad, Roghanian and Mojibian (2014)                           |                       | LP                            | TFN 5                           | TFN                           | Geometric mean                                                                  | -                              | -                       | -             |
| 37    | Ayhan and Kilic                                               | Manuf                 | MILP for                      | TFN 9                           | Crisp values                  | Geometric mean                                                                  | Arithmeticmean                 | COA                     | -             |
| 38    | (2015) Beikkhakhian et al. (2015)                             | -                     | allocation TOPSIS             | TFN 9                           | TFN 5                         | Eigenvector based on index of                                                   | Geometric mean                 | Index of optimism       | Saaty         |
| 39    | Kar (2015)                                                    | Manufacturing         | NN for                        | TFN 5                           | crisp                         | optimism Geometric mean                                                         | Weighted                       | COA                     | GCI           |
| 40    | Sultana, Ahmed, and Azeem (2015)                              | Manufacturing         | classification Delphi, TOPSIS | TFN 5                           | TFN                           | EAM                                                                             | geometric mean Geometric mean  | COA                     | Saaty         |
| 41    | Uygun, Kaçamak and Kahraman (2015)                            | Communication         | ANP, DEMATEL                  | TFN 5                           | TFN                           | EAM                                                                             | Arithmetic mean                | EAM                     | -             |
| 42 43 | Yayla et al. (2015) Büyüközkan and Güleryüz (2016)            | Logistics Automotive  | TOPSIS TOPSIS                 | TFN 5 Intuitionistic fuzzy sets | TFN Intuitionistic fuzzy sets | Geometric mean Weight of a criterion from an individual DM is supposed as being | - IFWA                         | COA for BNP -           | - Saaty,      |
| 44    | Prakash and Barua                                             | Electronic            | VIKOR                         | TFN 7                           | crisp                         | EAM                                                                             | -                              | EAM                     | -             |
| 45    | (2016b) Prakash and Barua (2016a)                             | Logistics             | TOPSIS                        | TFN 7                           | TFN                           | EAM                                                                             | Max-min                        | EAM                     | -             |
| 46    | Prasannavenkatesan and Goh (2016)                             | -                     | PROMETHEE                     | TFN 5                           | TFN                           | EAM                                                                             | -                              | EAM                     | Saaty         |
| 47    | Shakourloo et al. (2016)                                      | Manufacturing         | LP for allocation             | TFN 6                           | -                             | Updated EAM                                                                     | -                              | EAM                     | -             |
| 48    | Wang Chen, Chou, Luu and Yu (2016)                            | Manufacturing         | TOPSIS                        | TFN 6                           | TFN                           | EAM                                                                             | Arithmetic mean                | EAM                     | -             |
| 49    | Büyüközkan et al. (2017)                                      | RFID service provider | Fuzzy AD (Axiomatic design)   | TFN 11                          | TFN                           | Eigenvector based on index of optimism                                          | Aggregation based on consensus | Index of optimism       | Saaty         |
| 50    | Kumar et al. (2017)                                           | Automobile            | LP                            | TFN 9                           | TFN                           | EAM                                                                             | degree Geometric               | EAM                     | -             |
| 51    | Görener et al. (2017)                                         | Airline               | TOPSIS                        | Interval type set               | Interval type 2 fuzzy set     | Geometric mean                                                                  | mean Geometric mean            | -Fuzzy weights are used | Saaty         |
| 52    | Zimmer et al. (2017)                                          | Automobile            | IO                            | 2 fuzzy TFN 5                   | Crsip                         | EAM                                                                             | Geometric mean                 | EAM                     | Saaty         |
| 53    | Awasthi et al. (2018)                                         | electronic            | VIKOR                         | TFN 5                           | TFN                           | Eigenvector by defuzzifying first                                               | Max-min with arithmetic        | COA                     | Saaty         |
| 54    | Celik and Akyuz (2018)                                        | Maritime trans        | TOPSIS                        | Interval type-                  | Interval type- 2 fuzzy sets   | Geometric mean                                                                  | mean -                         | COA                     | -             |
| 55    | Khorasani (2018)                                              | Service               | Copras                        | 2 fuzzy sets TFN 9              | TFN                           | Geometric mean                                                                  | Geometric mean                 | -                       | -             |
| 56    | Liu et al. (2019)                                             | Agriculture           | TOPSIS                        | TFN 9                           | TFN                           | Geometric mean                                                                  | Geometric                      | COA                     | Saaty         |
| 57    | Büyüközkan et al. (2019)                                      | Chemistry             | VIKOR                         | Intuitionistic fuzzy sets       | Intuitionistic fuzzy sets     | IFWA                                                                            | mean IFWA                      | Fuzzy entropy           | Saaty         |

Table A.10 Other selection articles with the techniques in their fuzzy AHP models.

|                        | Authors                                                              | With method(s)                    | Representation                      | Representation         | Aggregation                                      | Aggregation                               | Defuzzification            | Consistency            |
|------------------------|----------------------------------------------------------------------|-----------------------------------|-------------------------------------|------------------------|--------------------------------------------------|-------------------------------------------|----------------------------|------------------------|
|                        |                                                                      |                                   | Pairwise                            | Performance            | Weights/ Priorities                              | Multi-experts                             |                            |                        |
| Machine/tool selection | Machine/tool selection                                               | Machine/tool selection            | Machine/tool selection              | Machine/tool selection | Machine/tool selection                           | Machine/tool selection                    | Machine/tool selection     | Machine/tool selection |
| 1                      | Taha and Rostam (2011)                                               | ANN                               | TFN 9                               | -                      | Eigenvector                                      | -                                         | Index of optimism          | Saaty                  |
| 2                      | Yazdani-Chamzini and Yakhchali (2012)                                | TOPSIS                            | TFN 9                               | TFN                    | EAM                                              | Arithmetic mean                           | EAM                        | -                      |
| 3                      | Ic, Yurdakul, and Dengiz (2013)                                      | -                                 | TraFN                               | -                      | Geometric mean                                   | -                                         | COA                        | -                      |
| 4                      | Nguyen et al. (2015)                                                 | COPRAS                            | TFN 7                               | TFN                    | Arithmetic mean                                  | -                                         | COA                        | -                      |
| 5                      | Parameshwaran et al. (2015)                                          | Delphi and TOPSIS/ VIKOR          | TFN 9                               | TFN                    | EAM                                              | -                                         | EAM                        | -                      |
| 6                      | Location/site selection Vahidnia, Alesheikh, and Alimohammadi (2009) | -                                 | TFN 9                               | -                      | EAM                                              | -                                         | EAM/COA/ index of optimism | Saaty                  |
| 7                      | Choudhary and Shankar                                                | TOPSIS                            | TFN 9                               | TFN                    | EAM                                              | -                                         | EAM                        | -                      |
| 8                      | (2012) Mosadeghi, Warnken, Tomlinson, and Mirfenderesk (2015)        | -                                 | TFN scale is not specified          | -                      | EAM                                              | -                                         | EAM                        | -                      |
| 9                      | Samanlioglu and Ayag (2017)                                          | PROMETHEE                         | TFN 5                               | TFN                    | Eigenvector                                      | -                                         | Index of                   | Saaty                  |
| 10                     | Ayodele et al. (2018)                                                | -                                 | Interval type 2                     | -                      | Geometric mean                                   | Geometric mean                            | optimism COA               | Saaty                  |
| 11 12                  | Erbas et al. (2018) Ju et al. (2018)                                 | TOPSIS Grey relational projection | fuzzy set TFN 5 TFN 6               | TFN Picture fuzzy set  | Geometric mean EAM                               | - -                                       | COA EAM                    | Saaty -                |
| 13                     | Singh et al. (2018)                                                  | -                                 | TFN 6                               | -                      | EAM                                              | -                                         | EAM                        | -                      |
| ERP selection          | ERP selection                                                        | ERP selection                     | ERP selection                       | ERP selection          | ERP selection                                    | ERP selection                             | ERP selection              | ERP selection          |
| 14 15 (2010)           | Cebeci (2009) Kahraman, Beskese, and Kaya                            | - -                               | TFN 5 TraFN (fuzzify the judgements | - -                    | Geometric mean Crisp weights but defuzzify first | - Weighted arithmetic mean                | COA COA                    | - -                    |
| 16                     | Onut and Efendigil (2010) Sarfaraz et al. (2012)                     | -                                 | first) TFN 9 TFN 9                  | -                      | EAM Crisp weights                                | -                                         | EAM                        | -                      |
| 17                     |                                                                      | -                                 |                                     | -                      | but defuzzify first                              | Geometric mean but defuzzify the decision | CFCS                       | Saaty                  |
| 18                     | Kilic,Selimzaim and Delen (2014)                                     | TOPSIS                            | TFN 9                               | Crisp value            | Geometric mean                                   | matrix first Arithmetic mean              | COA                        | -                      |
| 19                     | Ahmadi, Yeh, Papageorgiou, and Martin. (2015)                        | Fuzzy cognitive maps              | TFN 6                               | -                      | EAM                                              | -                                         | EAM                        | -                      |
| 20                     | Efe (2016)                                                           | TOPSIS                            | TFN 5                               | TFN                    | EAM                                              | -                                         | EAM/COA                    | Saaty                  |
| Project selection      | Project selection                                                    | Project selection                 | Project selection                   | Project selection      | Project selection                                | Project selection                         | Project selection          | Project selection      |
| 21                     | Taylan et al. (2014)                                                 | TOPSIS                            | TFN 5                               | TFN                    | EAM                                              | -Mentioned averaging but not specified    | EAM                        | -                      |
| 22                     | Baysal, Kaya, Sarucan, Kahraman, and Engina (2015)                   | TOPSIS                            | TFN 5                               |                        | Arithmetic mean                                  | -                                         | Index of optimism          | -                      |
| Technology selection   | Technology selection                                                 | Technology selection              | Technology selection                | Technology selection   | Technology selection                             | Technology selection                      | Technology selection       | Technology selection   |
| 23                     | Ayag (2010)                                                          | -                                 | TFN 5                               | -                      | Eigenvector                                      | -                                         | Index of optimism          | Saaty                  |
| 24                     | García-Cascales (2012)                                               | TOPSIS                            | TFN 5                               | TFN                    | Arithmetic mean                                  | -                                         | -                          | -                      |
| 25                     | Mirhedayatian et al. (2013)                                          | DEA                               | TFN 5                               | -                      | FP (based on DEA)                                | -                                         | -                          | FP                     |
| 26                     | Avikal, Mishra, and Jain                                             | PROMETHEE                         | TFN 5                               | crisp                  | Eigenvector                                      | -                                         | Index of                   | Saaty                  |
| 27                     | (2014) Demirtas ß , Özgürler, Özgürler, Güneri (2014)                |                                   | TFN 9                               | -                      | EAM                                              | -                                         | optimism EAM               | -                      |
| 28                     | Tan, Aviso, Huelgas, and                                             | -                                 | TFN 5                               | -                      | FP                                               | -                                         | FP                         | FP                     |
| 29                     | Promentilla (2014) Vinodh, Prasanna, and                             | TOPSIS                            | TFN 9                               | TFN                    | Geometric mean                                   | -                                         | COA                        | -                      |
| 30                     | Prakash (2014) Wang and Wang (2014)                                  | Kano                              | TFN 5                               | -                      | Eigenvector                                      | Max-min                                   | COA                        | Saaty                  |
| 31                     | Budak and Ustundag (2015)                                            | -                                 | TFN 5                               | -                      | Geometric mean                                   | Arithmetic mean                           | COA                        | -                      |
| 32                     | Mahjouri et al. (2017) Naderzadeh et al. (2017)                      | TOPSIS -                          | TFN 5 TFN 5                         | TFN -                  | Geometric mean EAM                               | Arithmetic mean -                         | -                          | - -                    |
| 33 34                  | Alaqeel and Suryanarayanan (2018)                                    | -                                 | TFN 9                               | -                      | Eigenvector                                      | -                                         | EAM Geometric mean         | Saaty                  |
| 35                     | Balusa and Gorai (2018)                                              | -                                 | TFN 9                               | -                      | Geometric mean                                   | -                                         | Index of                   | Saaty                  |

Table A.10 ( continued )

|                                                                           | Authors                                                                   | With method(s)                                                            | Representation                                                            | Representation                                                            | Aggregation                                                               | Aggregation                                                               | Defuzzification                                                           | Consistency                                                               |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
|                                                                           |                                                                           |                                                                           | Pairwise                                                                  | Performance                                                               | Weights/ Priorities                                                       | Multi-experts                                                             |                                                                           |                                                                           |
| 36                                                                        | Canan, Ahmet, and Tekin (2018)                                            | -                                                                         | TraFN                                                                     | -                                                                         | Geometric mean                                                            | Geometric mean                                                            | COA                                                                       | Saaty                                                                     |
| 37                                                                        | Goyal, Kaushal, and Sangaiah (2018)                                       | -                                                                         | TFN self- defined scale                                                   | -                                                                         | FP/EAM                                                                    | -                                                                         | FP/EAM                                                                    | FP                                                                        |
| 38                                                                        | Wang et al. (2019)                                                        | VIKOR                                                                     | TFN (not specified)                                                       | -                                                                         | EAM                                                                       | Mentioned but not specified                                               | EAM                                                                       | -                                                                         |
| 39                                                                        | Bostancioglu (2020)                                                       | -                                                                         | TFN 9                                                                     | -                                                                         | EAM                                                                       | -                                                                         | EAM                                                                       | -                                                                         |
| Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service | Evaluation of engineering sector, teaching performance and health service |
| 40                                                                        | Akkaya et al. (2015)                                                      | MOORA                                                                     | TFN 5                                                                     | TFN                                                                       | EAM                                                                       | -                                                                         | EAM                                                                       | -                                                                         |
| 41                                                                        | Chen et al. (2015)                                                        | -                                                                         | TFN 6                                                                     | -                                                                         | EAM                                                                       | Max-min                                                                   | EAM                                                                       | Saaty                                                                     |
| 42                                                                        | Singh and Prasher (2017)                                                  | -                                                                         | TFN 5                                                                     | -                                                                         | Geometric mean                                                            | -                                                                         | COA                                                                       | -                                                                         |
| Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  | Management of risk, sustainability, resource and process                  |
| 43                                                                        | Mangla et al. (2015)                                                      | -                                                                         | TFN 9                                                                     | -                                                                         | EAM                                                                       | -                                                                         | EAM                                                                       | -                                                                         |
| 44                                                                        | Calabrese et al. (2016)                                                   | -                                                                         | TFN 5                                                                     | -                                                                         | Row sum (similar to arithmetic mean)                                      | -                                                                         | COA                                                                       | Saaty                                                                     |
| 45                                                                        | Calabrese et al. (2019)                                                   | -                                                                         | TFN 5                                                                     | -                                                                         | Row sum (similar to arithmetic mean)                                      | -                                                                         | COA                                                                       | Saaty                                                                     |
| 46                                                                        | Zyoud, Kaufmann, Shaheen, Samhan, and Fuchs-Hanusch (2016)                | TOPSIS                                                                    | TFN 5                                                                     | TFN                                                                       | EAM                                                                       | Max-min Arithmetic and geometric mean                                     | EAM                                                                       | -                                                                         |
| 47                                                                        | Sirisawat and Kiatcharoenpol (2018)                                       | TOPSIS                                                                    | TFN 9                                                                     | TFN                                                                       | EAM                                                                       |                                                                           | EAM                                                                       | -                                                                         |
| 48                                                                        | Celik and Akyuz (2018)                                                    | TOPSIS                                                                    | Interval type 2 fuzzy set                                                 | -                                                                         | Geometric mean                                                            | -                                                                         | COA                                                                       | Saaty                                                                     |
| 49                                                                        | Khan, Shameem, Kumar, Hussain, and Yan (2019)                             | -                                                                         | TFN 6                                                                     | -                                                                         | EAM                                                                       | -                                                                         | EAM                                                                       | Saaty                                                                     |
| 50                                                                        | Singh and Sarkar (2019)                                                   | TOPSIS                                                                    | TFN self- defined scale                                                   | TFN                                                                       | EAM                                                                       | -                                                                         | EAM                                                                       | -                                                                         |
| 51                                                                        | Tavana, Shaabani, Mansouri Mohammadabadi, and Varzgani (2020)             | MOORA                                                                     | TFN 5                                                                     | TFN                                                                       | EAM                                                                       | Geometric mean                                                            | EAM                                                                       | Saaty                                                                     |
| Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     | Diagnosis of diseases                                                     |
| 52                                                                        | Nazari, Fallah, Kazemipoor, and Salehipour (2018)                         | FIS                                                                       | TFN 5                                                                     | TFN                                                                       | EAM                                                                       | Geometric mean                                                            | EAM                                                                       | -                                                                         |

## References

- [Aguarón, J., &amp; Moreno-Jiménez, J. M. (2003). The geometric consistency index: Approximated thresholds. European Journal of Operational Research, 147 , 137-145.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0005)
- [Ahmadi, S., Yeh, C.-H., Papageorgiou, E. I., &amp; Martin, A. R. (2015). An FCM-FAHP approach for managing readiness-relevant activities for ERP implementation. Computers &amp; Industrial Engineering, 88 , 501-517.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0010)
- [Ahmed, F., &amp; Kilic, K. (2018). Fuzzy Analytic Hierarchy Process: A performance analysis of various algorithms. Fuzzy Sets and Systems (In press).](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0015)
- [Akkaya, G., Turanog ˘lu, B., &amp; Öztas ß , S. (2015). An integrated fuzzy AHP and fuzzy MOORA approach to the problem of industrial engineering sector choosing. Expert Systems with Applications, 42 , 9565-9573.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0020)
- [Alaqeel, T. A., &amp; Suryanarayanan, S. (2018). A fuzzy Analytic Hierarchy Process algorithm to prioritize Smart Grid technologies for the Saudi electricity infrastructure. Sustainable Energy, Grids and Networks, 13 , 122-133.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0025)
- [Alinezad, A., Seif, A., &amp; Esfandiari, N. (2013). Supplier evaluation and selection with QFD and FAHP in a pharmaceutical company. The International Journal of Advanced Manufacturing Technology, 68 , 355-364.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0030)
- [Arbel, A. (1989). Approximate articulation of preference and priority derivation. European Journal of Operational Research, 43 , 317-326.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0035)
- Atanassov, K. T. (1986). Intuitionistic fuzzy sets. Fuzzy Sets and Systems, 20 , 87-96. Atanassov, K. T. (2012). On intuitionistic fuzzy sets theory . Berlin: Germany, SpringerVerlag.
- [Avikal, S., Mishra, P. K., &amp; Jain, R. (2014). A Fuzzy AHP and PROMETHEE methodbased heuristic for disassembly line balancing problems. International Journal of Production Research, 52 , 1306-1317.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0050)

[Awasthi, A., Govindan, K., &amp; Gold, S. (2018). Multi-tier sustainable global supplier selection using a fuzzy AHP-VIKOR based approach. International Journal of Production Economics, 195 , 106-117.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0055)

- [Ayag, Z. (2010). A combined fuzzy AHP-simulation approach to CAD software selection. International Journal of General Systems, 39 , 731-756.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0060)

[Aydin, S., &amp; Kahraman, C. (2010). Multiattribute supplier selection using fuzzy Analytic Hierarchy Process. International Journal of Computational Intelligence Systems, 3 , 553-565.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0065)

- [Ayhan, M. B., &amp; Kilic, H. S. (2015). A two stage approach for supplier selection problem in multi-item/multi-supplier environment with quantity discounts. Computers &amp; Industrial Engineering, 85 , 1-12.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0070)

[Ayodele, T. R., Ogunjuyigbe, A. S. O., Odigiea, O., &amp; Munda, J. L. (2018). A multicriteria GIS based model for wind farm site selection using interval type-2 fuzzy analytic hierarchy process: The case study of Nigeria. Applied Energy, 228 , 1853-1869.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0075)

[Büyüközkan, G., &amp; Güleryüz, S. (2016). A new integrated intuitionistic fuzzy group decision making approach for product development partner selection. Computers &amp; Industrial Engineering, 102 , 383-395.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0080)

[Büyüközkan, G. (2012). An integrated fuzzy multi-criteria group decision-making approach for green supplier evaluation. International Journal of Production Research, 50 , 2892-2909.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0085)

[Büyüközkan, G., Feyziog ˘lu, O., &amp; Nebol, E. (2008). Selection of the strategic alliance partner in logistics value chain. International Journal of Production Economics, 113 , 148-158.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0090)

- [Büyüközkan, G., Karabulut, Y., &amp; Arsenyan, J. (2017). RFID service provider selection: An integrated fuzzy MCDM approach. Measurement, 112 , 88-98.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0095)
- [Büyüközkan, G., Göçer, F., &amp; Karabulut, Y. (2019). A new group decision making approach with IF AHP and IF VIKOR for selecting hazardous waste carriers. Measurement, 134 .](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0100)

[Balusa, B. C., &amp; Gorai, A. K. (2018). Sensitivity analysis of fuzzy-analytic hierarchical process (FAHP) decision-making model in selection of underground metal mining method. Journal of Sustainable Mining (in press).](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0105)

[Ban, A. I., &amp; Coroianu, L. (2012). Nearest interval, triangular and trapezoidal approximation of a fuzzy number preserving ambiguity. International Journal of Approximate Reasoning, 53 , 805-836.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0110)

- [Barzilai, J. (1997). Deriving weights from pairwise comparison matrices. Journal of the Operational Research Society, 48 , 1226-1232.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0115)

- [Baysal, M. E., Kaya, \_ I., Sarucan, A., Kahraman, C., &amp; Engina, O. (2015). A two phased fuzzy methodology for selection among municipal projects. Technological and Economic Development of Economy, 21 , 405-422.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0120)

[Beikkhakhian, Y., Javanmardi, M., Karbasian, M., &amp; Khayambashi, B. (2015). The application of ISM model in evaluating agile suppliers selection criteria and ranking suppliers using fuzzy TOPSIS-AHP methods. Expert Systems with Applications, 42 , 6224-6236.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0125)

- [Bostancioglu, E. (2020). Double skin façade assessment by fuzzy AHP and comparison with AHP. Architectural Engineering and Design Management , 1-21.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0130)

Buckley, J. J. (1985). Fuzzy hierarchical analysis. Fuzzy sets and systems, 17 , 233-247. Budak, A., &amp; Ustundag, A. (2015). Fuzzy decision making model for selection of real time location systems. Applied Soft Computing, 36 , 177-184.

[Calabrese, A., Costa, R., Levialdi, N., &amp; Menichini, T. (2016). A fuzzy analytic hierarchy process method to support materiality assessment in sustainability reporting. Journal of Cleaner Production, 121 , 248-264.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0145)

[Calabrese, A., Costa, R., Levialdi, N., &amp; Menichini, T. (2019). Integrating sustainability into strategic decision-making: A fuzzy AHP method for the selection of relevant sustainability issues. Technological Forecasting and Social Change, 139 , 155-168.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0150)

- [Calabrese, A., Costa, R., &amp; Menichini, T. (2013). Using Fuzzy AHP to manage Intellectual Capital assets: An application to the ICT service industry. Expert Systems with Applications, 40 , 3747-3755.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0155)

[Canan, A., Ahmet, B., &amp; Tekin, T. G. (2018). Sustainability analysis of different hydrogen production options using hesitant fuzzy AHP. International Journal of Hydrogen Energy, 43 , 18059-18076.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0160)

- [Cebeci, U. (2009). Fuzzy AHP-based decision support system for selecting ERP systems in textile industry by using balanced scorecard. Expert Systems with Applications, 36 , 8900-8909.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0165)

[Celik, E., &amp; Akyuz, E. (2018). An interval type-2 fuzzy AHP and TOPSIS methods for decision-making problems in maritime transportation engineering: The case of ship loader. Ocean Engineering, 155 , 371-381.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0170)

- [Celik, M., Deha Er, I., &amp; Ozok, A. F. (2009). Application of fuzzy extended AHP methodology on shipping registry selection: The case of Turkish maritime industry. Expert Systems with Applications, 36 , 190-198.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0175)
- [Yücenur, G. N., Vayvay, Ö., &amp; Demirel, N. Ç. (2011). Supplier selection problem in global supply chains by AHP and ANP approaches under fuzzy environment. The International Journal of Advanced Manufacturing Technology, 56 , 823-833.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0180)

[Chai, J., Liu, J. N. K., &amp; Ngai, E. W. T. (2013). Application of decision-making techniques in supplier selection: A systematic review of literature. Expert Systems with Applications, 40 , 3872-3885.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0185)

[Chan, F. T. S., &amp; Kumar, N. (2007). Global supplier development considering risk factors using fuzzy extended AHP-based approach. Omega, 35 , 417-431.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0190)

- [Chan, F. T. S., Kumar, N., Tiwari, M. K., Lau, H. C. W., &amp; Choy, K. L. (2008). Global supplier selection: A fuzzy-AHP approach. International Journal of Production Research, 46 , 3825-3857.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0195)
- [Chang, D.-Y. (1996). Applications of the extent analysis method on fuzzy AHP. European journal of operational research, 95 , 649-655.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0200)
- Chen, S. J. &amp; Chen, S. M. (2001). A new method to measure the similarity between fuzzy numbers.
- [Chen, J.-F., Hsieh, H.-N., &amp; Do, Q. H. (2015). Evaluating teaching performance based on fuzzy AHP and comprehensive evaluation approach. Applied Soft Computing, 28 , 100-108.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0210)
- [Chen, L.-H., &amp; Hung, C.-C. (2010). An integrated fuzzy approach for the selection of outsourcing manufacturing partners in pharmaceutical R&amp;D. International Journal of Production Research, 48 , 7483-7506.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0215)

[Chen, S. H., Wang, P. W., Chen, C. M., &amp; Lee, H. T. (2010). An analytic hierarchy process approach with linguistic variables for selection of an R&amp;D strategic alliance partner. Computers &amp; Industrial Engineering, 58 , 278-287.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0220)

- [Chen, Z., &amp; Yang, W. (2011). An MAGDM based on constrained FAHP and FTOPSIS and its application to supplier selection. Mathematical and Computer Modelling, 54 , 2802-2815.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0225)
- [Chen, S.-M. (1998). Aggregating fuzzy opinions in the group decision-making environment. Journal of Cybernetics, 29 , 363-376.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0230)
- [Wang Chen, H. M., Chou, S.-Y., Luu, Q. D., &amp; Yu, T. H.-K. (2016). A fuzzy MCDM approach for green supplier selection from the economic and environmental aspects. Mathematical Problems in Engineering, 2016 , 1-10.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0235)

[Chiouy, C.-Y., Chou, S.-H., &amp; Yeh, C.-Y. (2011). Using fuzzy AHP in selecting and prioritizing sustainable supplier on CSR for Taiwan s electronics industry. Journal of Information and Optimization Sciences, 32 , 1135-1153.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0240)

[Choudhary, D., &amp; Shankar, R. (2012). An STEEP-fuzzy AHP-TOPSIS framework for](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0245)

[evaluation and selection of thermal power plant location.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0245)

[Energy, 42](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0245)

[, 510-521.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0245)

- [Crawford, G., &amp; Williams, C. (1985). A note on the analysis of subjective judgment matrices q . Journal of Mathematical Psychology, 29 , 387-405.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0250)
- [Csutora, R., &amp; Buckley, J. J. (2001). Fuzzy hierarchical analysis: The Lambda-Max method. Fuzzy Sets &amp; Systems, 120 , 181-195.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0255)
- [Cuong, B. C. (2014). Picture fuzzy sets. Journal of Computer Science and Cybernetics, 30 , 409-420.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0260)
- [De, S. K., Biswas, R., &amp; Roy, A. R. (2000). Some operations on intuitionistic fuzzy sets. Fuzzy Sets and Systems, 114 , 477-484.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0265)

[Demirtas](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0270)

ß

[, N., Özgürler, S](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0270)

ß

[., Özgürler, M., &amp; Güneri, A. F. (2014). Selecting e-Purse](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0270)

[smart card technology via Fuzzy AHP and ANP.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0270)

[Journal of Applied Mathematics.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0270)

.

- [Efe, B. (2016). An integrated fuzzy multi criteria group decision making approach for ERP system selection. Applied Soft Computing, 38 , 106-117.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0275)
- [Emrouznejad, A., &amp; Marra, M. (2017). The state of the art development of AHP (1979-2017): A literature review with a social network analysis. International Journal of Production Research, 55 , 6653-6675.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0280)
- [Erbas, M., Kabak, M., Ozceylan, E., &amp; Çetinkaya, C. (2018). Optimal siting of electric vehicle charging stations: A GIS-based fuzzy Multi-Criteria Decision Analysis. Energy, 163 , 1017-1031.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0285)

[Ertay, T., Kahveci, A., &amp; Tabanli, R. M. (2011). An integrated multi-criteria group decision-making approach to efficient supplier selection and clustering using fuzzy preference relations. International Journal of Computer Integrated Manufacturing, 24 , 1152-1167.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0290)

[Facchinetti, G., Ricci, R. G., &amp; Muzzioli, S. (1998). Note on ranking fuzzy triangular numbers. International Journal of Intelligent Systems, 13 , 613-622.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0295)

[García-Cascales, M. S. (2012). Evaluation of photovoltaic cells in a multi-criteria decision making process. Annals of Operations Research, 199 , 373-391.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0300)

[Ghorbani, M., Mohammad Arabzad, S., &amp; Shahin, A. (2013). A novel approach for supplier selection based on the Kano model and fuzzy MCDM. International Journal of Production Research, 51 , 5469-5484.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0305)

[Goyal, R. K., Kaushal, S., &amp; Sangaiah, A. K. (2018). The utility based non-linear fuzzy AHP optimization model for network selection in heterogeneous wireless networks. Applied Soft Computing, 67 , 800-811.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0310)

[Grzegorzewski, P., &amp; Mrówka, E. (2005). Some notes on (Atanassov's) intuitionistic fuzzy sets. Fuzzy Sets and Systems, 156 , 492-495.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0315)

[Hashemian, S. M., Behzadian, M., Samizadeh, R., &amp; Ignatius, J. (2014). A fuzzy hybrid group decision support system approach for the supplier evaluation process. The International Journal of Advanced Manufacturing Technology, 73 , 1105-1117.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0320)

[Ic, Y. T., Yurdakul, M., &amp; Dengiz, B. (2013). Development of a decision support system for robot selection. Robotics and Computer-Integrated Manufacturing, 29 , 142-157.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0325)

[Ju, Y., Ju, D., Gonzalez, E. D. R. S., Giannakisc, M., &amp; Wang, A. (2018). Study of site selection of electric vehicle charging station based on extended GRP method under picture fuzzy environment. Computers &amp; Industrial Engineering (in press).](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0330)

- [Jung, H. (2011). A fuzzy AHP-GP approach for integrated production-planning considering manufacturing partners. Expert Systems with Applications, 38 , 5833-5840.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0335)

[Kahraman, C., Beskese, A., &amp; Kaya, I. (2010). Selection among ERP outsourcing alternatives using a fuzzy multi-criteria decision making methodology. International Journal of Production Research, 48 , 547-566.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0340)

[Kahraman, C., Sari, \_ I. U., &amp; Turanog ˘lu, E. (2014). Fuzzy analytic hierarchy process with type-2 fuzzy sets. Knowledge-Based Systems, 59 , 48-57.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0345)

[Kannan, D., Khodaverdi, R., Olfat, L., Jafarian, A., &amp; Diabat, A. (2013). Integrated fuzzy multi criteria decision making method and multi-objective programming approach for supplier selection and order allocation in a green supply chain. Journal of Cleaner Production, 47 , 355-367.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0350)

[Kar, A. K. (2014). Revisiting the supplier selection problem: An integrated approach for group decision support. Expert Systems with Applications, 41 , 2762-2771.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0355)

- [Kar, A. K. (2015). A hybrid group decision support system for supplier selection using analytic hierarchy process, fuzzy set theory and neural network. Journal of Computational Science, 6 , 23-33.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0360)

[Karsak, E. E., &amp; Dursun, M. (2016). Taxonomy and review of non-deterministic analytical methods for supplier selection. International Journal of Computer Integrated Manufacturing, 29 , 263-286.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0365)

[Khan, A. A., Shameem, M., Kumar, R. R., Hussain, S., &amp; Yan, X. (2019). Fuzzy AHP based prioritization and taxonomy of software process improvement success factors in global software development. Applied Soft Computing, 83 105648.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0370)

- [Khorasani, S. T. (2018). Green supplier evaluation by using the integrated Fuzzy AHP model and Fuzzy Copras. Process Integration and Optimization for Sustainability, 2 , 17-25.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0375)

[Kilic, H. S., Selimzaim &amp; Delen, D. (2014). Development of a hybrid methodology for ERP system selection: The case of Turkish airlines. Decision Support Systems, 66 , 82-92.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0380)

[Kilincci, O., &amp; Onal, S. A. (2011). Fuzzy AHP approach for supplier selection in a washing machine company. Expert Systems with Applications, 38 , 9656-9664.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0385)

- [Kim, K., &amp; Park, K. S. (1990). Ranking fuzzy numbers with index of optimism. Fuzzy Sets &amp; Systems, 35 , 143-150.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0390)

[Klir, G., &amp; Yuan, B. (1995). Fuzzy sets and fuzzy logic . New Jersey: Prentice Hall.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0395)

- [Kubat, C., &amp; Yuce, B. (2012). A hybrid intelligent approach for supply chain management system. Journal of Intelligent Manufacturing, 23 , 1237-1244.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0400)

[Kubler, S., Robert, J., Derigent, W., Voisin, A., &amp; le Traon, Y. (2016). A state-of the-art survey &amp; testbed of fuzzy AHP (FAHP) applications. Expert Systems with Applications, 65 , 398-422.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0405)

- [Kumar, D., Rahman, Z., &amp; Chan, F. T. S. (2017). A fuzzy AHP and fuzzy multi objective linear programming model for order allocation in a sustainable supply chain A case study. International Journal of Computer Integrated Manufacturing, 30 , 535-551.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0410)
- [Kuo, R. J., Chi, S. C., &amp; Kao, S. S. (2002). A decision support system for selecting convenience store location through integration of fuzzy AHP and artificial neural network. Computers in Industry, 47 , 199-214.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0415)

[Kuo, R. J., Lee, L. Y., &amp; Hu, T.-L. (2010). Developing a supplier selection system through integrating fuzzy AHP and fuzzy DEA a case study on an auto lighting system company in Taiwan. Production Planning and Control, 21 , 468-484.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0420)

- [Lee, J., Cho, H., &amp; Kim, Y. S. (2015). Assessing business impacts of agility criterion and order allocation strategy in multi-criteria supplier selection. Expert Systems with Applications, 42 , 1136-1148.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0425)

[Lee, A. H. I. (2009). A fuzzy supplier selection model with the consideration of benefits, opportunities, costs and risks. Expert Systems with Applications, 36 , 2879-2893.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0430)

[Liu, Y., Eckert, C., Bris, G. Y.-L., &amp; Petit, Galle (2019). A fuzzy decision tool to evaluate the sustainable performance of suppliers in an agrifood value chain. Computers &amp; Industrial Engineering, 127 , 196-212.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0435)

[Luenberger, D. G., &amp; Ye, Y. (2008). Linear and nonlinear programming . Springer Science &amp; Business Media.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0440)

[Mahjouri, M., Ishak, M. B., Torabian, A., Manaf, L. A., Halimoon, N., &amp; Ghoddusi, J. (2017). Optimal selection of Iron and Steel wastewater treatment technology using integrated multi-criteria decision-making techniques and fuzzy logic. Process Safety and Environmental Protection, 107 , 54-68.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0445)

[Mahmoudzadeh, M., &amp; Bafandeh, A. R. (2013). A new method for consistency test in fuzzy AHP. Journal of Intelligent &amp; Fuzzy Systems, 25 , 457-461.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0450)

[Mangla, S. K., Kumar, P., &amp; Barua, M. K. (2015). Risk analysis in green supply chain using fuzzy AHP approach: A case study. Resources, Conservation and Recycling, 104 , 375-390.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0455)

[Mardani, A., Jusoh, A., &amp; Zavadskas, E. K. (2015). Fuzzy multiple criteria decisionmaking techniques and applications - Two decades review from 1994 to 2014. Expert Systems with Applications, 42 , 4126-4148.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0460)

[Mendel, J. M., &amp; John, R. I. B. (2002). Type-2 fuzzy sets made simple. IEEE Transactions on Fuzzy Systems, 20 , 117-127.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0465)

[Mikhailov, L., &amp; Tsvetinov, P. (2004). Evaluation of services using a fuzzy analytic hierarchy process. Applied Soft Computing Journal, 5 , 23-33.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0470)

[Mikhailov, L. (2004). A fuzzy approach to deriving priorities from interval pairwise comparison judgements. European Journal of Operational Research, 159 , 687-704.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0475)

[Mirhedayatian, M., Jelodar, M., Adnani, S., Akbarnejad, M., &amp; Saen, R. (2013). A new approach for prioritization in fuzzy ahp with an application for selecting the best tunnel ventilation system. International Journal of Advanced Manufacturing Technology, 68 , 2589-2599.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0480)

[Mosadeghi, R., Warnken, J., Tomlinson, R., &amp; Mirfenderesk, H. (2015). Comparison of Fuzzy-AHP and AHP in a spatial multi-criteria decision making model for urban land-use planning. Computers, Environment and Urban Systems, 49 , 54-65.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0485)

[Naderzadeh, M., Arabalibeik, H., Monazzam, M. R., &amp; Ghasemi, I. (2017). Comparative analysis of ahp-topsis and fuzzy ahp models in selecting appropriate nanocomposites for environmental noise barrier applications. Fluctuation and Noise Letters , 16.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0490)

[Nazari, S., Fallah, M., Kazemipoor, H., &amp; Salehipour, A. (2018). A fuzzy inferencefuzzy analytic hierarchy process-based clinical decision support system for diagnosis of heart diseases. Expert Systems with Applications, 95 , 261-271.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0495)

[Nguyen, H. T., Md Dawal, S. Z., Nukman, Y., Aoyama, H., &amp; Case, K. (2015). An integrated approach of fuzzy linguistic preference based AHP and Fuzzy COPRAS for machine tool evaluation. PLoS ONE, 10 e0133599.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0500)

[Onut, S., &amp; Efendigil, T. (2010). A theorical model design for ERP software selection process under the constraints of cost and quality: A fuzzy approach. Journal of Intelligent &amp; Fuzzy Systems, 21 , 365-378.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0505)

[Opricovic, S., &amp; Tzeng, G.-H. (2003). Defuzzification within a multicriteria decision model. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 11 , 635-652.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0510)

[Parameshwaran, R., Kumar, S. P., &amp; Saravanakumar, K. (2015). An integrated fuzzy MCDM based approach for robot selection considering objective and subjective criteria. Applied Soft Computing, 26 , 31-41.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0515)

[Pitchipoo, P., Venkumar, P., &amp; Rajakarunakaran, S. (2013). Fuzzy hybrid decision model for supplier evaluation and selection. International Journal of Production Research, 51 , 3903-3919.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0520)

[Prakash, C., &amp; Barua, M. K. (2016a). An analysis of integrated robust hybrid model for third-party reverse logistics partner selection under fuzzy environment. Resources, Conservation and Recycling, 108 , 63-81.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0525)

[Prakash, C., &amp; Barua, M. K. (2016b). A combined MCDM approach for evaluation and selection of third-party reverse logistics partner for Indian electronics industry. Sustainable Production and Consumption, 7 , 66-78.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0530)

[Prasannavenkatesan, S., &amp; Goh, M. (2016). Multi-objective supplier selection and order allocation under disruption risk. Transportation Research Part E: Logistics and Transportation Review, 95 , 124-142.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0535)

[Görener, A., Ayvaz, B., Kus ß akcı, A. O., &amp; Altınok, E. (2017). A hybrid type-2 fuzzy based supplier performance evaluation methodology: The Turkish Airlines technic case. Applied Soft Computing, 56 , 436-445.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0540)

[Rezaei, J., Fahim, P. B. M., &amp; Tavasszy, L. (2014). Supplier selection in the airline retail industry using a funnel methodology: Conjunctive screening method and fuzzy AHP. Expert Systems with Applications, 41 , 8165-8179.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0545)

[Rezaei, J., &amp; Ortt, R. (2013). Multi-criteria supplier segmentation using a fuzzy preference relations based AHP. European Journal of Operational Research, 225 , 75-84.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0550)

[Rezaei, J., Ortt, R., &amp; Scholten, V. (2013). An improved fuzzy preference programming to evaluate entrepreneurship orientation. Applied Soft Computing Journal, 13 , 2749-2758.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0555)

[Roshandel, J., Miri-Nargesi, S. S., &amp; Hatami-Shirkouhi, L. (2013). Evaluating and selecting the supplier in detergent production industry using hierarchical fuzzy TOPSIS. Applied Mathematical Modelling, 37 , 10170-10181.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0560)

[Ross, T. J. (2004). Fuzzy logic with engineering applications . John Wiley &amp; Sons Ltd..](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0565)

[Saaty, T. L. (1980). The analytic hierarchy process: Planning, priority setting, resources allocation . New York: McGraw.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0570)

[Saaty, T. L. (1990). How to make a decision: The analytic hierarchy process. European journal of operational research, 48 , 9-26.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0575)

[Saaty, T. L. (2006). There is no mathematical validity for using fuzzy number crunching in the analytic hierarchy process. Journal of Systems Science and Systems Engineering, 15 , 457-464.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0580)

Saaty, T. L. (2008). Relative measurement and its generalization in decision making why pairwise comparisons are central in mathematics for the measurement of intangible factors the analytic hierarchy/network process. RACSAM-Revista de la Real Academia de Ciencias Exactas Fisicas y Naturales. Serie A. Matematicas, 102 , 251-318.

[Samanlioglu, F., &amp; Ayag, Z. (2017). A fuzzy AHP-PROMETHEE II approach for evaluation of solar power plant location alternatives in Turkey. Journal of Intelligent &amp; Fuzzy Systems, 33 , 859-871.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0590)

[Sarfaraz, A., Jenab, K., &amp; D'Souza, A. C. (2012). Evaluating ERP implementation choices on the basis of customisation using fuzzy AHP. International Journal of Production Research, 50 , 7057-7067.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0595)

[S ß en, C. G., S ß en, S., &amp; Bas ß lıgil, H. (2010). Pre-selection of suppliers through an integrated fuzzy analytic hierarchy process and max-min methodology. International Journal of Production Research, 48 , 1603-1625.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0600)

[Shad, Z., Roghanian, E., &amp; Mojibian, F. (2014). Integration of QFD, AHP, and LPP methods in supplier development problems under uncertainty. Journal of Industrial Engineering International, 10 .](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0605)

[Shakourloo, A., Kazemi, A., &amp; Javad, M. O. M. (2016). A new model for more effective supplier selection and remanufacturing process in a closed-loop supply chain. Applied Mathematical Modelling, 40 , 9914-9931.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0610)

[Shaw, K., Shankar, R., Yadav, S. S., &amp; Thakur, L. S. (2012). Supplier selection using fuzzy AHP and fuzzy multi-objective linear programming for developing low carbon supply chain. Expert Systems with Applications, 39 , 8182-8192.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0615)

[Singh, R. K., Chaudhary, N., &amp; Saxena, Nikhil (2018). Selection of warehouse location for a global supply chain: A case study. IIMB Management Review. .](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0620)

[Singh, A., &amp; Prasher, A. (2017). Measuring healthcare service quality from patients' perspective: Using Fuzzy AHP application. Total Quality Management &amp; Business Excellence, 30 , 284-300.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0625)

[Singh, P. K., &amp; Sarkar, P. (2019). A framework based on fuzzy AHP-TOPSIS for prioritizing solutions to overcome the barriers in the implementation of ecodesign practices in SMEs. International Journal of Sustainable Development &amp; World Ecology, 26 , 506-521.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0630)

[Sirisawat, P., &amp; Kiatcharoenpol, T. (2018). Fuzzy AHP-TOPSIS approaches to prioritizing solutions for reverse logistics barriers. Computers &amp; Industrial Engineering, 117 , 303-318.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0635)

[Son, L. H. (2015). DPFCM: A novel distributed picture fuzzy clustering method on picture fuzzy sets. Expert Systems with Applications, 42 , 51-66.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0640)

[Soroor, J., Tarokh, M. J., Khoshalhan, F., &amp; Sajjadi, S. (2012). Intelligent evaluation of supplier bids using a hybrid technique in distributed supply chains. Journal of Manufacturing Systems, 31 , 240-252.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0645)

[Subramanian, N., &amp; Ramanathan, R. (2012). A review of applications of Analytic Hierarchy Process in operations management. International Journal of Production Economics, 138 , 215-241.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0650)

[Sultana, I., Ahmed, I., &amp; Azeem, A. (2015). An integrated approach for multiple criteria supplier selection combining Fuzzy Delphi, Fuzzy AHP &amp; Fuzzy TOPSIS. Journal of Intelligent &amp; Fuzzy Systems, 29 , 1273-1287.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0655)

[Sun, C.-C. (2010). A performance evaluation model by integrating fuzzy AHP and fuzzy TOPSIS methods. Expert Systems with Applications, 37 , 7745-7754.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0660)

[Taha, Z., &amp; Rostam, S. (2011). A fuzzy AHP-ANN-based decision support system for machine tool selection in a flexible manufacturing cell. The International Journal of Advanced Manufacturing Technology, 57 , 719-733.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0665)

[Tan, R. R., Aviso, K. B., Huelgas, A. P., &amp; Promentilla, M. A. B. (2014). Fuzzy AHP approach to selection problems in process engineering involving quantitative and qualitative aspects. Process Safety and Environmental Protection, 92 , 467-475.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0670)

[Tavana, M., Shaabani, A., Mansouri Mohammadabadi, S., &amp; Varzgani, N. (2020). An integrated fuzzy AHP-fuzzy MULTIMOORA model for supply chain risk-benefit assessment and supplier selection. International Journal of Systems Science: Operations &amp; Logistics , 1-24.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0675)

[Taylan, O., Bafail, A. O., Abdulaal, R. M. S., &amp; Kabli, M. R. (2014). Construction projects selection and risk assessment by fuzzy AHP and fuzzy TOPSIS methodologies. Applied Soft Computing, 17 , 105-116.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0680)

[Uygun, Ö., Kaçamak, H., &amp; Kahraman, Ü. A. (2015). An integrated DEMATEL and Fuzzy ANP techniques for evaluation and selection of outsourcing provider for a telecommunication company. Computers &amp; Industrial Engineering, 86 , 137-146.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0685)

[Vahidnia, M. H., Alesheikh, A. A., &amp; Alimohammadi, A. (2009). Hospital site selection using fuzzy AHP and its derivatives. Journal of Environment Management, 90 , 3048-3056.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0690)

[van Laarhoven, P. J. M., &amp; Pedrycz, W. (1983). A fuzzy extension of Saaty's priority theory. Fuzzy Sets &amp; Systems, 11 , 199-227.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0695)

[Vinodh, S., Prasanna, M., &amp; Prakash, N. H. (2014). Integrated Fuzzy AHP-TOPSIS for selecting the best plastic recycling method: A case study. Applied Mathematical Modelling, 38 , 4662-4672.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0700)

[Viswanadham, N., &amp; Samvedi, A. (2013). Supplier selection based on supply chain ecosystem, performance and risk criteria. International Journal of Production Research, 51 , 6484-6498.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0705)

[Wang, J.-W., Cheng, C.-H., &amp; Huang, K.-C. (2009). Fuzzy hierarchical TOPSIS for supplier selection. Applied Soft Computing, 9 , 377-386.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0710)

[Wang, Y.-M., Luo, Y., &amp; Hua, Z. (2008). On the extent analysis method for fuzzy AHP and its applications. European Journal of Operational Research, 186 , 735-747.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0715)

[Wang, B., Song, J., Ren, J., Li, K., Duan, H., &amp; Wang, X. E. (2019). Selecting sustainable energy conversion technologies for agricultural residues: A fuzzy AHP-VIKOR based prioritization from life cycle perspective. Resources, Conservation and Recycling, 142 , 78-87.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0720)

[Wang, C.-H., &amp; Wang, J. (2014). Combining fuzzy AHP and fuzzy Kano to optimize product varieties for smart cameras: A zero-one integer programming perspective. Applied Soft Computing, 22 , 410-416.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0725)

[Wilkinson, J. H. (1965). The algebraic eigenvalue problem . Oxford: Clarendon Press.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0730)

- [Xu, Z., &amp; Liao, H. (2014). Intuitionistic Fuzzy analytic hierarchy process. IEEE Transactions on Fuzzy Systems, 22 , 749-761.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0735)
- [Xu, Z. (2007). Intuitionistic preference relations and their application in group decision making q . Information Sciences An International Journal, 177 , 2363-2379.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0740)
- [Yager, R. R. (1981). A procedure for ordering fuzzy subsets of the unit interval. Information Sciences, 24 , 143-161.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0745)
- [Yang, J. L., Chiu, H. N., Tzeng, G.-H., &amp; Yeh, R. H. (2008). Vendor selection by integrated fuzzy MCDM techniques with independent and interdependent relationships. Information Sciences, 178 , 4166-4183.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0750)

[Yayla, A. Y., Oztekin, A., Gumus, A. T., &amp; Gunasekaran, A. (2015). A hybrid data analytic methodology for 3PL transportation provider evaluation using fuzzy multi-criteria decision making. International Journal of Production Research, 53 , 6097-6113.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0755)

- [Yazdani-Chamzini, A., &amp; Yakhchali, S. H. (2012). Tunnel Boring Machine (TBM) selection using fuzzy multicriteria decision making methods. Tunnelling and Underground Space Technology, 30 , 194-204.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0760)
- [Yeh, C.-T. (2008). On improving trapezoidal and triangular approximations of fuzzy numbers. International Journal of Approximate Reasoning, 48 , 297-313.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0765)
- [Yeh, C.-T. (2017). Existence of interval, triangular, and trapezoidal approximations of fuzzy numbers under a general condition. Fuzzy Sets and Systems, 310 , 1-13.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0770)
- [Yu, M.-C., Goh, M., &amp; Lin, H.-C. (2012). Fuzzy multi-objective vendor selection under lean procurement. European Journal of Operational Research, 219 , 305-311.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0775)
- [Zadeh, L. A. (1965). Fuzzy sets. Information and Control, 8 , 338-353.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0780)
- [Zeydan, M., Çolpan, C., &amp; Çobanog ˘lu, C. (2011). A combined methodology for supplier selection and performance evaluation. Expert Systems with Applications, 38 , 2741-2751.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0785)
- [Zhu, K.-J., Jing, Y., &amp; Chang, D.-Y. (1999). A discussion on extent analysis method and applications of fuzzy AHP. European journal of operational research, 116 , 450-456.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0790)
- [Zimmer, K., Fröhling, M., &amp; Schultmann, F. (2016). Sustainable supplier management - A review of models supporting sustainable supplier selection, monitoring and development. International Journal of Production Research, 54 , 1412-1442.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0795)
- [Zimmer, K., Fröhling, M., Breun, P., &amp; Schultmann, F. (2017). Assessing social risks of global supply chains: A quantitative analytical approach and its application to supplier selection in the German automotive industry. Journal of Cleaner Production, 149 , 96-109.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0800)

[Zimmermann, H.-J. (2001). Fuzzy set theory and its applications . Kluwer Academic.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0805)

- [Zouggari, A., &amp; Benyoucef, L. (2012). Simulation based fuzzy TOPSIS approach for group multi-criteria supplier selection problem. Engineering Applications of Artificial Intelligence, 25 , 507-519.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0810)

[Zyoud, S. H., Kaufmann, L. G., Shaheen, H., Samhan, S., &amp; Fuchs-Hanusch, D. (2016). A framework for water loss management in developing countries under fuzzy environment: Integration of Fuzzy AHP with Fuzzy TOPSIS. Expert Systems with Applications, 61 , 86-105.](http://refhub.elsevier.com/S0957-4174(20)30562-5/h0815)

## Glossary

- AHP: Analytic Hierarchy Process

ANP: Analytic Network Process

- CFCS: Converting the Fuzzy data into Crisp Scores

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

TFN:

Triangular Fuzzy Number

TraFN:

Trapezoidal Fuzzy Number

TOPSIS: Technique for Order of Preference by Similarity to Ideal Solution