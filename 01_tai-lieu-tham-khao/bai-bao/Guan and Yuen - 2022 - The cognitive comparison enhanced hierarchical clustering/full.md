![](images/050d71e8a5cd2b879442073d0d76711b5cf8110e3ed673e812f666787a795868.jpg)

# The cognitive comparison enhanced hierarchical clustering

Chun Guan<sup>1</sup> • Kevin Kam Fung Yuen<sup>2,3</sup>

Received: 15 June 2021 / Accepted: 2 September 2021 / Published online: 28 October 2021 - The Author(s) 2021

## Abstract

The growth of online shopping is rapidly changing the buying behaviour of consumers. Today, there are challenges facing buyers in the selection of a preferred item from the numerous choices available in the market. To improve the consumer online shopping experience, recommender systems have been developed to reduce the information overload. In this paper, a cognitive comparison-enhanced hierarchical clustering (CCEHC) system is proposed to provide personalised product recommendations based on user preferences. A novel rating method, cognitive comparison rating (CCR), is applied to weigh the product attributes and measure the categorical scales of attributes according to expert knowledge and user preferences. Hierarchical clustering is used to cluster the products into different preference categories. The CCEHC model can be used to rank and cluster product data with the input of user preferences and produce reliable customised recom mendations for the users. To demonstrate the advantages of the proposed model, the CCR method is compared with the rating approach of the analytic hierarchy process. Two recommendation cases are demonstrated in this paper with two datasets, one collected by this research for laptop recommendation and the other an open dataset for workstation recommendation. The simulation results demonstrate that the proposed system is feasible for providing personalised recommendations. The significance of this research is the provision of a recommendation solution that does not depend on historical purchase records; rather, one wherein the users’ rating preferences and expert knowledge, both of which are measured by CCR, is considered. The proposed CCEHC model could be further applied to other types of similar recommendation cases such as music, books, and movies.

Keywords Decision making - Expert system - Pairwise comparisons - Recommender system - Clustering

## 1 Introduction

Online shopping has already influenced the purchasing behaviour of consumers. Today, buyers face an overload of information to select the most preferred goods. Recom mender systems (RSs) are developed to recommend appropriate products to consumers on the basis of their historical records. An effective RS service can boost sales by building and increasing customer loyalty (Aggarwal 2016). Reviews of RS technologies can be found in (Aggarwal 2016; Haruna, et al. 2017; Adomavicius and Kwon 2015; Kunaver and Pozˇrl 2017; Kotkov et al. 2016; Zhang et al. 2017; Ma et al. 2018). RSs are typically categorised into three types: collaborative filtering, content-based, and hybrid (Aggarwal 2016). Since these types are based on user profiles including their historical ratings and purchase records (Lika et al. 2014), the RSs have insufficient information to learn the interests of new users. Lacking information for newly joined users is known as the coldstart problem, which is a critical challenge of RS (Kunaver and Pozˇrl 2017; Lika et al. 2014; Volkovs et al. 2017; Viktoratos et al. 2018). A discussion and review of the cold-start problem can be found in Lika et al., (2014).

Cold start problems have significant influence on highend consumer electronics such as smartphones, laptops, game consoles, and audio–video equipment. Since their electronic components and technologies are frequently updated, recommendations based on historical purchasing records could possibly not be applicable to new products. The motivation of this research is to propose an expert system for product recommendations that is based on the current individual users’ preferences and expert knowledge elicited from cognitive comparison rating (CCR) method. The proposed model does not have such a cold-start problem, as historical information is not used for the recommendations.

The evaluation of expert judgments and user preferences for products is complicated as numerous products such as the aforementioned high-end consumer electronics consist of different attributes. Multi-criteria decision making (MCDM) methods, which can measure both user preferences and expert judgments for multiple product attributes, have been used in RSs (van Capelleveen et al. 2019; Song 2018; Zhang et al. 2018). The analytic hierarchy process (AHP), a classical MCDM, has been adopted to evaluate user preferences for different product attributes (Hinduja and Pandey 2018; Karthikeyan et al. 2017; Pamucˇar et al. 2018; Wang and Tseng 2013). CCR, an improved alternative to AHP, is introduced in this study for evaluating expert judgments and user preferences. As an approach to rectify the mathematical representation problem of the perception of the paired differences in AHP, CCR is an ideal method for weighing product attributes and defining numerical values of nominal scales based on user preferences (Yuen 2009, 2012, 2014a; b).

To provide product recommendation services, the hierarchical clustering (HC) method is used to group the products based on the evaluation results of CCR. Different clustering analysis methods have been applied to identify groups of products that have similar attributes with respect to consumer preferences (Nilashi 2017; Fre´mal and Lecron 2017; Katarya and Verma 2017; Selvi and Sivasankar 2019). HC (Murtagh 1983; Ward Jr 1963; Han et al. 2011) is a popular clustering method; for example, HC has been adopted in other RSs (Selvi and Sivasankar 2019; Gupta and Patil 2015; Zheng et al. 2013; de Aguiar Neto et al. 2020). A hierarchical decomposition of a dataset can be built by HC in the form of a tree graph (called a dendrogram). The major advantage of HC is that the dendrogram can be easily interpreted since the distances between the objects are directly presented. HC has limitations when applied to product-recommendation cases. Firstly, the attributes of products are equally considered; however, different consumers can have different preferences for each attribute. Secondly, the product attributes of nominal scales cannot be directly used in clustering processes. To address these limitations, CCR is used to weigh product attributes and define numerical values of nominal scales with respect to user preferences. A novel system, cognitive comparisonenhanced hierarchical clustering (CCEHC), is proposed to provide product recommendations with respect to the current individual user’s rating preferences. The new method provides a solution to the cold start problem in RSs by using the expert knowledge elicited from CCR instead of the users’ historical data. In addition, non-specialized consumers can express their references to interact with the system.

This paper offers a significant extension of the previous initial work (Guan and Yuen 2015; Guan 2018), especially for the sections of methods, experiments, comparisons, and discussions. The remainder of this paper is organised as follows. Section 2 proposes the novel CCEHC system. Section 3 demonstrates the validity and feasibility of the proposed method using a laptop recommendation case, for which the dataset was collected in this study. Section 4 discusses the advantages and limitations of the proposed approach. Section 5 presents the application of CCEHC for workstation recommendations using an open dataset. Finally, Sect. 6 concludes the study.

## 2 Cognitive comparison enhanced hierarchical clustering

The procedures of the CCEHC model are presented in Fig. 1. In Steps 1 and 2, the attributes of the products are structured as an attribute tree. According to the attribute tree, a raw data table is collected from different sources. In

![](images/f07b750bf7052a1687255015e0315519f4bb9267381ecf9cbb318efb5f19a561.jpg)  
Fig. 1 CCEHC procedures

Step 3, CCR is applied to measure the nominal attribute values and attribute weights with user preferences. The resulting table is normalised in Step 4. In Step 5, the values of the products are produced by aggregating the normalised table and attribute weights. In Step 6, a personalised top N recommendation is produced by ranking the product values. In the final step, the products are clustered by HC, and similar products can be recommended to the different users.

## 2.1 Specifying attributes

Detailed product information can be obtained from different sources including manufacturer websites, product engineers, and retailers. A product is represented as a group of attributes, $\{ \delta _ { i } \} = ( \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { i } , \dots , \delta _ { n } )$ , where $\delta _ { i }$ is the ith attribute of the product. Attributes can have sub-attributes. For example, an attribute $\delta _ { i }$ is represented by $n _ { i }$ sub-attributes, $\left\{ \delta _ { i , j } \right\} = \left( \delta _ { i , 1 } , \delta _ { i , 2 } , . . . , \delta _ { i , j } , . . . , \delta _ { i , n _ { i } } \right)$ ; where $\delta _ { i , j }$ is represented by the jth sub-attribute of $\delta _ { i } ;$ the attribute $\delta _ { i , j }$ is represented by $n _ { i , j }$ sub-attributes, $\left\{ \delta _ { i , j , k } \right\} = \left( \delta _ { i , j , 1 } \right.$ $\delta _ { i , j , 2 } , . . . , \delta _ { i , j , k } , . . . , \delta _ { i , j , n _ { i , j } } )$ , where $\delta _ { i , j , k }$ is the kth sub-attribute of $\delta _ { i , j }$ . The attributes of the different levels are structured as an attributes tree. A sample of the laptop attribute tree is presented in Fig. 2 in Sect. 3.

## 2.2 Preprocessing data

The leaf attributes, denoted as L, are attributes without subattributes. The measurable values of leaf attributes are collected from different sources, as mentioned in Sect. 2.1. Product dataset D consisting of m products and l leaf attributes is denoted as $D = \bigl \{ d _ { \alpha \beta } \mathopen { } \mathclose \bgroup | \forall \alpha \in ( 1 , . . . , m ) , \forall \beta \in$ $( 1 , . . . . , l ) , \}$ . An example of a laptop data matrix is presented in Sect. 3.2. D cannot be directly clustered since it could contain nominal scales that do not have a natural ordering. In the proposed CCEHC system, the nominal scales are substituted by the numerical values measured using the CCR approach presented in the next step.

## 2.3 Evaluating user preferences by CCR

The user preferences for different attributes and nominal scales are measured using the CCR method. A sample of the CCR interface is displayed in Fig. 3.

Table 1 is a typical measurement scale schema $\left( \aleph , { \overline { { X } } } \right)$ applied to CCR (Yuen 2009, 2014a). The space of the linguistic labels @ of the paired interval scales is {Equally, Slightly, …, Outstandingly, Absolutely}. The numerical representation of the paired interval scales X is as follows: X ¼ x<sub>q</sub> ¼ <sup>qj</sup> j8q 2 f g s; . . .; 1; 0; 1; . . .; s ; j [ 0<sup>n</sup> <sup>o</sup>: s

ð1Þ

The subjective perception of the difference between pairs is represented as the normal utility, j. By default, j. is set to max X . Denoting the number of linguistic labels as s, the number of scales is 2s þ 1.

To measure the user preferences in paired interval scales, a pairwise opposite matrix (POM) is defined as follows.

Fig. 2 Attributes tree for laptops with weights for User A  
![](images/d90befc7152c6871427cf24bb9bf06b936b52e135a26728348444b88c7f2740b.jpg)

Fig. 3 Cognitive comparison Interface for evaluating laptop attributes  
Regarding the attributes of Laptop : Processor (δ1), OS (δ2), Storage $( \delta _ { 3 } ) ,$ Brand $( \delta _ { 4 } ) ,$ ,Display $( \delta _ { 5 } ) _ { : }$ ,Prices $( \delta _ { 6 } ) _ { : }$ ,Portable $( \delta _ { 7 } ) _ { \cdots }$ Compare the relative preference for each pair, and circle the mark accordingly.

<table><tr><td></td><td colspan="4">Absolutely</td><td colspan="4">Highly</td><td colspan="4">Equally</td><td colspan="4">Highly</td><td colspan="2">Absolutely</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>OS</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Storage</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Brand</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Display</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Prices</td></tr><tr><td>Processor</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr><tr><td>OS</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Storage</td></tr><tr><td>OS</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Brand</td></tr><tr><td>OS</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Display</td></tr><tr><td>OS</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Prices</td></tr><tr><td>OS</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr><tr><td>Storage</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Brand</td></tr><tr><td>Storage</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Display</td></tr><tr><td>Storage</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Prices</td></tr><tr><td>Storage</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr><tr><td>Brand</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Display</td></tr><tr><td>Brand</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Prices</td></tr><tr><td>Brand</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr><tr><td>Display</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Prices</td></tr><tr><td>Display</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr><tr><td>Prices</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Portable</td></tr></table>

Table 1 Measurement scale schema for CCR

<table><tr><td>Label (N)</td><td></td><td>Paired Interval Scale ( $\overline{X}$ )</td></tr><tr><td colspan="3">Equally</td></tr><tr><td>Slightly</td><td>1</td><td> $\kappa/8$ </td></tr><tr><td>Moderately</td><td>2</td><td> $2\kappa/8$ </td></tr><tr><td>Fairly</td><td>3</td><td> $3\kappa/8$ </td></tr><tr><td>Highly</td><td>4</td><td> $4\kappa/8$ </td></tr><tr><td>Strongly</td><td>5</td><td> $5\kappa/8$ </td></tr><tr><td>Significantly</td><td>6</td><td> $6\kappa/8$ </td></tr><tr><td>Outstandingly</td><td>7</td><td> $7\kappa/8$ </td></tr><tr><td>Absolutely</td><td>8</td><td> $\kappa$ </td></tr></table>

$$
\begin{array}{l} B = \left[ b _ {i j} \right] = \left[ \begin{array}{c c c c} 0 & v _ {1} - v _ {2} & \dots & v _ {1} - v _ {n} \\ v _ {2} - v _ {1} & 0 & \dots & v _ {2} - v _ {n} \\ \vdots & \vdots & \ddots & \vdots \\ v _ {n} - v _ {1} & v _ {n} - v _ {2} & \dots & 0 \end{array} \right] \\ \cong \left[ \begin{array}{c c c c} 0 & b _ {1 2} & \dots & b _ {1 n} \\ b _ {2 1} & 0 & \dots & b _ {2 n} \\ \vdots & \vdots & \ddots & \vdots \\ b _ {n 1} & b _ {n 2} & \dots & 0 \end{array} \right] = \left[ b _ {i j} \right] = B, \end{array}\tag{2}
$$

where B denotes a POM. v<sub>i</sub> denotes the priority value, and $b _ { i j } { \cong } \left[ \nu _ { i } - \nu _ { j } \right]$ denotes the approximate comparison value between objects i and j. The values of $b _ { i j }$ are obtained from a questionnaire. For example, $b _ { 1 3 } = 3$ means that the customer considers the first object to be fairly more important than the third.

To verify the validity of the POM, an Accordance Index (AI) is defined in Eq. (3). AI = 0 indicates that B is absolutely accordant. If $0 < \mathrm { A I } \le 0 . 1$ , then B is recommended. If $\mathrm { A I } > 0 . 1$ , B is unacceptable, the survey should be rechecked.

$$
\mathrm{AI} = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \sqrt {\frac {1}{n} \sum_ {p = 1} ^ {n} \left(\frac {b _ {i p} + b _ {p j} - b _ {i j}}{\kappa}\right) ^ {2}}.\tag{3}
$$

The priority values of objects are computed using the row average plus normal utility (RAU) as follows:

$$
\operatorname{RAU} (B, \kappa) = \left\{v _ {i}: v _ {i} = \frac {1}{n} \sum_ {j = 1} ^ {n} b _ {i j} + \kappa , \forall i \in \{1, \dots , n \} \right\}.\tag{4}
$$

The RAU values are subsequently normalised as a vector W as follows:

$$
\begin{array}{l} W = \left\{w _ {i}: w _ {i} = \frac {v _ {i}}{n \kappa}, \forall i \in \{1, \dots , n \} \right\}, \text {where} \sum_ {i \in \{1, \dots , n \}} v _ {i} \\ = n \kappa . \end{array} \qquad \rho^ {(\alpha)} = \sum_ {i = 1} ^ {n} r _ {i} \cdot \delta_ {i} ^ {(\alpha)}, \forall \alpha \in (1, \dots , m).\tag{10}
$$

ð5Þ

The vector W can represent a variety of items such as the priorities of options, item utilities, weights of features, and preferences for nominal values. In CCEHC, the weights of the product attributes and nominal scales in raw dataset D are substituted with their normalised RAU values.

## 2.4 Normalising dataset

Two equations are introduced to normalise the raw dataset D. If a higher value indicates a higher preference for a leaf attribute, the dividing maximal function $\Delta _ { \mathrm { m a x } }$ defined in Eq. (6) is used to rescale the column of raw attribute values, i.e., ${ D } _ { \beta } ^ { T } = \left\{ d _ { 1 , \beta } , . . . , d _ { \alpha , \beta } , . . . , d _ { m , \beta } \right\}$ . If a lower value reveals a higher preference, the minimal dividing function $\Delta _ { \mathrm { m i n } }$ defined in Eq. (7) is applied. The normalised data matrix is denoted as

$$
D ^ {\prime} = \left\{x _ {\alpha \beta} | \forall \alpha \in (1, \dots , m), \forall \beta \in (1, \dots , l), \right\}.
$$

$$
x _ {\alpha \beta} = \Delta_ {\max} (d _ {\alpha \beta}) = \frac {d _ {\alpha \beta}}{\max (D _ {\beta} ^ {T})}, \forall \alpha \in (1, \dots , m), \forall \beta\tag{6}
$$

$$
\begin{array}{l} x _ {\alpha \beta} = \Delta_ {\min} \big (d _ {\alpha \beta} \big) = \frac {\min \Big (D _ {\beta} ^ {T} \Big)}{d _ {\alpha \beta}}, \forall \alpha \in (1, \ldots , m), \forall \beta \\ \quad \in (1, \ldots , l). \end{array}\tag{7}
$$

## 2.5 Fusing data

The product values $\left\{ \rho ^ { ( a ) } | \forall \alpha \in ( 1 , . . . , m ) \right\}$ are the weighted summation of the product attribute values, where a is the index of the product. Attribute values are the weighted summation of their sub-attributes. The detailed calculations of product/attribute are presented in Eqs. (8)–(10), where $r _ { i } , \ r _ { i , j } ,$ and $r _ { i , j , k }$ are the weights of $\delta _ { i } , \delta _ { i , j } ,$ and $\delta _ { i , j , k } .$ respectively. The leaf attribute values are obtained from the normalised data matrix $D ^ { \prime }$

$$
\begin{array}{l} \delta_ {i, j} ^ {(\alpha)} = \sum_ {k = 1} ^ {n _ {i, j}} r _ {i, j, k} \cdot \delta_ {i, j, k} ^ {(\alpha)}, \forall i \in (1, \ldots , n), \forall j \in (1, \ldots , n _ {i}), \forall \alpha \\ \quad \in (1, \ldots , m), \end{array}\tag{8}
$$

$$
\delta_ {i} ^ {(\alpha)} = \sum_ {j = 1} ^ {n _ {i}} r _ {i, j} \cdot \delta_ {i, j} ^ {(\alpha)}, \forall j \in (1, \dots , n _ {i}), \forall \alpha \in (1, \dots , m),\tag{9}
$$

## 2.6 Generating top-N list

According to the product values, a personalised top-N list consisting of the N highest value products in descending order is provided to the user; the calculation details are described in Algorithm 1. For different users, the top-N lists are different since the product values are calculated with respect to personal preferences.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Top-N list
Input: $\{\rho^{(\alpha)}\}$ , N
For i=1 to N,
    $M = Max(\{\rho^{(\alpha)}\})$ 
TopN[i]=M
$\{\rho^{(\alpha)}\} = M/\{\rho^{(\alpha)}\}$ , where / is a complement operator.
Output: TopN
</div>

## 2.7 Clustering products

HC is used to group products according to their product values. The aim of HC is to iteratively combine the two nearest clusters into a larger cluster until all the objects are in one cluster or a preset termination condition is reached (Han et al. 2011). Murtagh (1983) briefly described the steps of hierarchical clustering methods. The steps of HC applied to the CCEHC are described below.

Step 1: One product is an atomic cluster, $C _ { \sigma } = \{ \rho ^ { ( a ) } \}$ The distances between each pair of clusters are computed in the following form:

$$
d _ {\alpha , a ^ {\prime}} = \left| \rho^ {(a)} - \rho^ {(a ^ {\prime})} \right|, \forall a, \forall a ^ {\prime} \in (1, \dots , m),\tag{11}
$$

where $d _ { \alpha , a ^ { \prime } }$ is the dissimilarity of product values for any two different products $\rho ^ { ( a ) }$ and $\rho ^ { ( a ^ { \prime } ) }$

Step 2: The two closest clusters, $C _ { s }$ and $C _ { t } ,$ , where $( s , t ) =$ argmin( $\{ d _ { \alpha , a ^ { \prime } } \} )$ , are combined into a larger cluster, i.e., $C _ { s } = C _ { s } \cup C _ { t }$ , which means $C _ { s }$ is updated by merging $C _ { t }$ and $C _ { s }$ . The distances between the updated cluster $C _ { s }$ and other clusters $C _ { \neg s }$ are computed as the average distance (Han et al. 2011) in the following form:

$$
d_{\text{avg}}(C_{s},C_{\neg s}) = \frac{1}{\eta_{s}\eta_{\neg s}}\sum_{\substack{\rho^{(a)}\in C_{s},\rho^{\left(a^{\prime}\right)}\in C_{\neg s}}}d_{\rho^{(a)},\rho^{\left(a^{\prime}\right)}},\tag{12}
$$

where $\eta _ { s }$ is the number of objects in cluster $C _ { s } .$ $d _ { \mathrm { a v g } } ( C _ { s } , C _ { \neg s } )$ updates the distances between clusters $C _ { s }$ and $C _ { \neg s } . \ d _ { \rho ^ { ( a ) } , \rho ^ { ( a ^ { \prime } ) } }$ is the distance between products $\rho ^ { ( a ) }$ and $\rho ^ { ( a ^ { \prime } ) }$ , where $\rho ^ { ( a ) } \in C _ { s }$ and $\rho ^ { ( a ^ { \prime } ) } \in C _ { \neg s } .$ . Step 2 is repeated until all products are in one cluster.

Step 3: A dendrogram indicating the arrangement of the merged clusters is produced. Two examples of dendrograms for similar laptop clusters are displayed in Fig. 4. The products are grouped into different clusters by cutting the branches at an appropriate height, which represents the distance between the clusters. Clustering results can be used for similar product recommendations. When a user searches for product $\rho ^ { ( a ) }$ such that $\rho ^ { ( a ) } \in C _ { \sigma }$ , the other products in Cluster $C _ { \sigma } ,$ , i.e., R, are recommended to the user. R is defined as follows:

$$
R = C _ {\sigma} / \left\{\rho^ {(a)} \right\},\tag{13}
$$

where / is a complement operator.

## 3 Application of laptop recommendation

Laptops can be represented by a set of attributes. Consumers search for a set of preferred product attributes when searching for a laptop. To demonstrate the applicability and validity of the proposed CCEHC system, a laptop recommendation case for a consumer (denoted as User A) is illustrated. For the cases in Sects. 3–5, a dataset of 27 laptop configurations was manually collected from the websites of online retail shops and manufacturers in 2015.

## 3.1 Specifying attributes

A large number of laptop configurations can be found on websites for selling, introducing, and comparing electronic products. The majority of consumers are likely unfamiliar with specific technical properties such as the wireless type and video output details. Certain laptop components could be unimportant to other consumers such as USB ports,

![](images/d680b71f3dc28bce48936fde39edc3b0a45da4dcc50a0a34f5e1f149b91f88f6.jpg)  
Fig. 4 Dendrogram for clusters of similar laptops produced for User A (left) and User B (right)

DVD/CD burners, and speakers. These attributes are not considered in this recommendation case. The selected attributes for choosing an ideal laptop are structured as a 3-level attribute tree, as indicated in Fig. 2.

The attributes in the first level of the tree are CPU $( \delta _ { 1 } ) _ { \cdot }$ Operating System $( \delta _ { 2 } )$ , Storage $( \delta _ { 3 } )$ , Brand $( \delta _ { 4 } )$ , Display $( \delta _ { 5 } )$ , Portable $( \delta _ { 6 } )$ , and Price $( \delta _ { 7 } )$ . Five of these have subattributes. For example, Storage includes the Hard Drive and Random-Access Memory (RAM). The sub-attributes of the first-level attributes are structured in the second level, including {RAM $( \delta _ { 3 , 1 } )$ , Hard Drive $( \delta _ { 3 , 2 } ) \}$ , {USA $( \delta _ { 4 , 1 } )$ , Asia $( \delta _ { 4 , 2 } ) \}$ , {Screen $( \delta _ { 5 , 1 } )$ , Graphics Card $( \delta _ { 5 , 2 } ) \}$ {Weight $( \delta _ { 7 , 1 } )$ , Battery $( \delta _ { 7 , 2 } ) \}$ . The sub-attributes of the second-level attributes are in the third level of the tree, which are {SSD $( \delta _ { 3 , 2 , 1 } )$ , Size $( \delta _ { 3 , 2 , 2 } ) \}$ , {Size $( \delta _ { 5 , 1 , 1 } )$ , Resolution $( \delta _ { 5 , 1 , 2 } ) \}$

## 3.2 Preprocessing data

From the attributes tree presented in Fig. 2, a laptop has 13 leaf attributes. A raw data matrix D of is obtained from the laptop configurations as indicated in Table 15 of the Appendix. The quantification approaches used to preprocess leaf attributes are summarised in Table 2. For example, the attribute values of the CPU and Graphics Card are quantified by their performance scores (3DMARK 2015). The SSD attribute has three nominal labels: SSD, which indicates that the laptop has an SSD, No SSD indicating that the laptop has no SSD and Hybrid indicating that the laptop has SSD and another type of hard disk. The three labels are respectively replaced by ‘‘2’’, ‘‘0’’, and $^ { 6 6 } 1 ^ { , 5 }$ . The screen resolution attribute is represented by the production of the width and height pixels of the screen. The nominal scales of the attributes OS and Brand are measured by CCR in Sect. 3.3.

![](images/02c91d2aa29122869b78fe12c76c462d4609d71bbc6733ca9c5c28c055e9bc63.jpg)

Table 2 Schema of laptop leaf attributes

<table><tr><td></td><td>Leaf attribute name</td><td>Measurement scale</td><td>Quantification approach</td><td>Normalization function</td></tr><tr><td> $L_1$ </td><td>CPU  $\delta_1$ </td><td>Nominal: CPU model</td><td>3DMark06 Score</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_2$ </td><td>OS  $\delta_2$ </td><td>Nominal: Linux OS X Windows 7 Windows 8</td><td>CCR</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_3$ </td><td>RAM  $\delta_{3,1}$ </td><td>GB</td><td>GB</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_4$ </td><td>SSD  $\delta_{3,2,1}$ </td><td>Nominal: SSD Hybrid No SSD</td><td>SSD: 2 Hybrid:1 No SSD: 0</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_5$ </td><td>Hard Drive Size  $\delta_{3,2,2}$ </td><td>GB</td><td>GB</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_6$ </td><td>Brand (USA) $\delta_{4,1}$ </td><td>Nominal: Alienware Apple Dell Microsoft</td><td>CCR</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_7$ </td><td>Brand (Asia) $\delta_{4,2}$ </td><td>Nominal: Acer ASUS HP Lenovo Samsung</td><td>CCR</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_8$ </td><td>Screen Size  $\delta_{5,1,1}$ </td><td>Inch</td><td>Inch</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_9$ </td><td>Screen Resolution  $\delta_{5,1,2}$ </td><td>DPI</td><td>Width pixel × height pixel</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_{10}$ </td><td>Graphics Card  $\delta_{5,2}$ </td><td>Nominal: Graphics Card model</td><td>3DMark06 Scores</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_{11}$ </td><td>Weight  $\delta_{6,1}$ </td><td>Kg</td><td>Kg</td><td> $\Delta_{\text{min}}$ </td></tr><tr><td> $L_{12}$ </td><td>Battery  $\delta_{6,2}$ </td><td>Hour</td><td>Hour</td><td> $\Delta_{\text{max}}$ </td></tr><tr><td> $L_{13}$ </td><td>Price  $\delta_7$ </td><td>RMB</td><td>Thousand RMB</td><td> $\Delta_{\text{min}}$ </td></tr></table>

## 3.3 Evaluating user preferences by CCR

The preferences of user were gathered from a CCR questionnaire. An example of a questionnaire using CCR is presented in Fig. 3. The measurement scale schema defined in Table 1 is used in this case, and j is set to $\mathbf { \delta } ^ { 6 6 } 8 ^ { 9 }$ ’. The POM for User A presented in Table 3 is obtained from the questionnaire results in Fig. 3 based on Eq. (2). The AI for the POM computed by Eq. (3) is less than 0.1, which

Table 3 Comparison matrices for 1st level laptop attributes (User A)

means that the POM is acceptable. Table 3 lists the weights of the 1st level laptop attributes computed by Eqs. (4) and (5) within the detailed calculations steps. The POMs, AIs, and weights of the remaining sub-attributes are provided in Table 4. All the attribute weights for User A are given, including the attribute tree, in Fig. 2. The nominal attribute labels for User A of Operating System $( L _ { 2 } )$ , Asia Brand $\left( L _ { 6 } \right)$ and USA Brand $( L _ { 7 } )$ are also measured by CCR. The POMs and prioritisation results (called as preference

<table><tr><td> $B_0$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td><td> $\sum_{j=1}^{7} b_{ij}$ </td><td> $\frac{1}{7}\sum_{j=1}^{7} b_{ij}$ </td><td> $v_i = \frac{1}{7}\sum_{j=1}^{7} b_{ij} + 8$ </td><td> $r_i = w_i = \frac{v_i}{7\times 8}$ </td></tr><tr><td> $\delta_1$ </td><td>0</td><td>1</td><td>-1</td><td>7</td><td>-1</td><td>1</td><td>3</td><td>10</td><td>1.429</td><td>9.429</td><td>0.168</td></tr><tr><td> $\delta_2$ </td><td>-1</td><td>0</td><td>-3</td><td>5</td><td>-2</td><td>0</td><td>2</td><td>1</td><td>0.143</td><td>8.143</td><td>0.145</td></tr><tr><td> $\delta_3$ </td><td>1</td><td>3</td><td>0</td><td>7</td><td>0</td><td>3</td><td>5</td><td>19</td><td>2.714</td><td>10.714</td><td>0.191</td></tr><tr><td> $\delta_4$ </td><td>-7</td><td>-5</td><td>-7</td><td>0</td><td>-7</td><td>-5</td><td>-3</td><td>-34</td><td>-4.857</td><td>3.143</td><td>0.056</td></tr><tr><td> $\delta_5$ </td><td>1</td><td>2</td><td>0</td><td>7</td><td>0</td><td>2</td><td>4</td><td>16</td><td>2.286</td><td>10.286</td><td>0.184</td></tr><tr><td> $\delta_6$ </td><td>-1</td><td>0</td><td>-3</td><td>5</td><td>-2</td><td>0</td><td>2</td><td>1</td><td>0.143</td><td>8.143</td><td>0.145</td></tr><tr><td> $\delta_7$ </td><td>-3</td><td>-2</td><td>-5</td><td>3</td><td>-4</td><td>-2</td><td>0</td><td>-13</td><td>-1.857</td><td>6.143</td><td>0.110</td></tr><tr><td colspan="12">AI = 0.051</td></tr></table>

Table 4 Comparison matrices for 2nd and 3rd levels laptop attributes (User A)

ð14Þ

ð15Þ

For each laptop, the $2 ^ { \mathrm { n d } }$ level attribute values are calculated using Eq. (8), the weights in Tables 3 and 4, and the normalised data matrix $D ^ { \prime }$ in Table 16 in the Appendix. An example of the calculation process for ${ \delta _ { 3 , 2 } } ^ { ( 1 ) }$ is presented below.

$$
x _ {1, 1} = \Delta_ {\max} (d _ {1, 1}) = \frac {d _ {1 , 1}}{\max (D _ {1} ^ {T})} = \frac {3 3 6 7}{7 0 6 0} = 0. 4 4 7,
$$

The suitable normalisation equations for the leaf attributes are listed in Table 2. For example, a CPU $\left( L _ { 1 } \right)$ with a higher performance score is attractive. $\Delta _ { \mathrm { m a x } }$ defined in Eq. (6) is therefore applied to normalise the CPU attribute values. Typically, consumers prefer a lower product price; therefore, $\Delta _ { \mathrm { m i n } }$ defined in Eq. (7) is used to normalise Price $( L _ { 1 3 } )$ . The normalised data matrix D<sup>0</sup> is provided in Table 16 in the Appendix. Two samples of the normalisation process for the attribute values of CPU and Price for laptop ID1 are given below.

$$
x _ {1, 1 3} = \Delta_ {\min} \left(d _ {1, 1 3}\right) = \frac {\min \left(D _ {1 3} ^ {T}\right)}{d _ {1 , 1 3}} = \frac {2}{7} = 0. 2 8 5.
$$

## 3.5 Fusing data

## 3.4 Normalising dataset

$$
\begin{array}{l} \delta_ {3, 2} ^ {(1)} = \sum_ {k = 1} ^ {2} r _ {3, 2, k} \bullet \delta_ {3, 2, k} ^ {(1)} = \left(r _ {3, 2, 1} \bullet \delta_ {3, 2, 1} ^ {(1)}\right) + \left(r _ {3, 2, 2} \bullet \delta_ {3, 2, 2} ^ {(1)}\right) \\ = (0. 3 1 3 \bullet x _ {1, 4}) + (0. 6 8 7 \bullet x _ {1, 5}) \\ = (0. 3 1 3 \bullet 1. 0 0 0) + (0. 6 8 7 \bullet 0. 1 6 9) = 0. 4 2 9. \end{array}
$$

values) are displayed in Table 5. The nominal attribute values in raw dataset D can be substituted with their preference values.

ð16Þ

<table><tr><td> $B_3$ </td><td> $\delta_{3,1}$ </td><td> $\delta_{3,2}$ </td><td> $r_{3,i}$ </td><td> $B_{3,2}$ </td><td> $\delta_{3,2,1}$ </td><td> $\delta_{3,2,2}$ </td><td> $r_{3,2,i}$ </td><td> $B_4$ </td><td> $\delta_{4,1}$ </td><td> $\delta_{4,2}$ </td><td> $r_{4,i}$ </td></tr><tr><td> $\delta_{3,1}$ </td><td>0</td><td>0</td><td>0.5</td><td> $\delta_{3,2,1}$ </td><td>0</td><td>-6</td><td>0.313</td><td> $\delta_{4,1}$ </td><td>0</td><td>-2</td><td>0.437</td></tr><tr><td> $\delta_{3,2}$ </td><td>0</td><td>0</td><td>0.5</td><td> $\delta_{3,2,2}$ </td><td>6</td><td>0</td><td>0.687</td><td> $\delta_{4,2}$ </td><td>2</td><td>0</td><td>0.563</td></tr><tr><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td></tr><tr><td> $B_5$ </td><td> $\delta_{5,1}$ </td><td> $\delta_{5,2}$ </td><td> $r_{5,i}$ </td><td> $B_{5,1}$ </td><td> $\delta_{5,1,1}$ </td><td> $\delta_{5,1,2}$ </td><td> $r_{5,1,i}$ </td><td> $B_6$ </td><td> $\delta_{6,1}$ </td><td> $\delta_{6,2}$ </td><td> $r_{6,i}$ </td></tr><tr><td> $\delta_{5,1}$ </td><td>0</td><td>-4</td><td>0.375</td><td> $\delta_{5,1,1}$ </td><td>0</td><td>-2</td><td>0.437</td><td> $\delta_{6,1}$ </td><td>0</td><td>0</td><td>0.5</td></tr><tr><td> $\delta_{5,2}$ </td><td>4</td><td>0</td><td>0.625</td><td> $\delta_{5,1,2}$ </td><td>2</td><td>0</td><td>0.563</td><td> $\delta_{6,2}$ </td><td>0</td><td>0</td><td>0.5</td></tr><tr><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td></tr></table>

The value of attribute ${ \delta _ { 5 , 2 } } ^ { ( 1 ) }$ is computed as 0.556. The 1st level attribute values are computed using Eq. (9). The calculation process for ${ \delta _ { 3 } } ^ { ( 1 ) }$ is given in Eq. (17) as an example.

$$
\begin{array}{l} \delta_ {3} ^ {(1)} = \sum_ {j = 1} ^ {2} r _ {3, j} \bullet \delta_ {3, j} ^ {(1)} = \left(r _ {3, 1} \bullet \delta_ {3, 1} ^ {(1)}\right) + \left(r _ {3, 2} \bullet \delta_ {3, 2} ^ {(1)}\right) \\ \qquad = \left(r _ {3, 1} \bullet x _ {1, 5}\right) + \left(r _ {3, 2} \bullet \delta_ {3, 2} ^ {(1)}\right) \\ \qquad = (0. 5 0 0 \bullet 0. 2 5 0) + (0. 5 0 0 \bullet 0. 4 2 9) = 0. 3 4 0. \end{array}\tag{17}
$$

The values of attributes $\delta _ { 4 } ^ { ( 1 ) } , \delta _ { 5 } ^ { ( 1 ) }$ and $\delta _ { 6 } ^ { ( 1 ) }$ are 0.563, 0.327 and 0.550, respectively. The laptop product values are computed using Eq. (10). For example, the product value of the first laptop is 0.448; the detailed steps are presented in Eq. (18). All 27 laptop product values for User A are listed in Table 6.

$$
\begin{array}{l} \rho^ {(1)} = \sum_ {j = 1} ^ {7} r _ {i} \bullet \delta_ {i} ^ {(1)} \\ \qquad = \left(r _ {1} \bullet \delta_ {1} ^ {(1)}\right) + \left(r _ {2} \bullet \delta_ {2} ^ {(1)}\right) + \left(r _ {3} \bullet \delta_ {3} ^ {(1)}\right) \\ \qquad + \left(r _ {4} \bullet \delta_ {4} ^ {(1)}\right) + \left(r _ {5} \bullet \delta_ {5} ^ {(1)}\right) + \left(r _ {6} \bullet \delta_ {6} ^ {(1)}\right) \\ \qquad + \left(r _ {7} \bullet \delta_ {7} ^ {(1)}\right) \\ \qquad = \left(r _ {1} \bullet x _ {1, 1}\right) + \left(r _ {2} \bullet x _ {1, 2}\right) + \left(r _ {3} \bullet \delta_ {3} ^ {(1)}\right) + \left(r _ {4} \bullet \delta_ {4} ^ {(1)}\right) \\ \qquad + \left(r _ {5} \bullet \delta_ {5} ^ {(1)}\right) + \left(r _ {6} \bullet \delta_ {6} ^ {(1)}\right) + \left(r _ {2} \bullet x _ {1, 1 3}\right) \\ \qquad = 0. 4 4 8. \end{array}\tag{18}
$$

## 3.6 Generating top-N list

The top-N list for laptops is produced using Algorithm 1. According to User A’s preferences for laptop attributes, a top-10 list of laptops is provided in Table 7. The information and correspondingly web links of the laptops in the top-10 list can be recommended to User A in descending order after the user has completed the CCR survey.

Table 5 Comparison matrices for nominal attribute of L , L and L (User A)

<table><tr><td> $B_2$ </td><td>Linux</td><td>OS X</td><td>Windows 7</td><td>Windows 8</td><td></td><td>Preference value</td></tr><tr><td>Linux</td><td>0</td><td>-2</td><td>-3</td><td>0</td><td></td><td>0.211</td></tr><tr><td>OS X</td><td>2</td><td>0</td><td>-1</td><td>2</td><td></td><td>0.273</td></tr><tr><td>Windows 7</td><td>3</td><td>1</td><td>0</td><td>3</td><td></td><td>0.305</td></tr><tr><td>Windows 8</td><td>0</td><td>-2</td><td>-3</td><td>0</td><td></td><td>0.211</td></tr><tr><td>AI = 0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $B_6$ </td><td>Alienware</td><td>Apple</td><td>Dell</td><td>Microsoft</td><td>HP</td><td>Preference value</td></tr><tr><td>Alienware</td><td>0</td><td>1</td><td>3</td><td>4</td><td>4</td><td>0.260</td></tr><tr><td>Apple</td><td>-1</td><td>0</td><td>2</td><td>3</td><td>3</td><td>0.235</td></tr><tr><td>Dell</td><td>-3</td><td>-2</td><td>0</td><td>1</td><td>2</td><td>0.190</td></tr><tr><td>Microsoft</td><td>-4</td><td>-3</td><td>-1</td><td>0</td><td>0</td><td>0.160</td></tr><tr><td>HP</td><td>-4</td><td>-3</td><td>-2</td><td>0</td><td>0</td><td>0.155</td></tr><tr><td>AI = 0.043</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $B_7$ </td><td>Acer</td><td>ASUS</td><td>Lenovo</td><td>Samsung</td><td></td><td>Preference value</td></tr><tr><td>Acer</td><td>0</td><td>-1</td><td>-3</td><td>2</td><td></td><td>0.234</td></tr><tr><td>ASUS</td><td>1</td><td>0</td><td>-2</td><td>3</td><td></td><td>0.266</td></tr><tr><td>Lenovo</td><td>3</td><td>2</td><td>0</td><td>4</td><td></td><td>0.320</td></tr><tr><td>Samsung</td><td>-2</td><td>-3</td><td>-4</td><td>0</td><td></td><td>0.180</td></tr><tr><td>AI = 0.042</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 3.7 Clustering products

The details of the HC method are described in Sect. 2.7. The HC method is used to cluster the similar laptop products into different groups by measuring the dissimilarities between the product values calculated using Eq. (11). After merging the two closest clusters, the dissimilarities are updated using Eq. (12). The dendrogram produced by HC for User A is displayed in Fig. 4a. By cutting the dendrogram at height of 0.05, six clusters are generated: {4, 18, 19}, {14, 13, 16, 20, 1, 5, 22, 3, 24, 6, 26}, {25, 27, 8, 11}, {7, 9, 10, 12, 21, 23}, {15} and {2, 17}. The clustering results are used for product recommendations. For example, if User A browses the webpage of Laptop 4, Laptops 18 and 19, which are in the same cluster of Laptop 4, are recommended to the user. Similarly, if User A browses Laptop 2, Laptop 17 is recommended.

## 4 Discussions

Comparisons and discussions are presented in this section to demonstrate the advantages of the proposed RS. To demonstrate the advantage of providing personalization recommendations, the recommendations for User B are presented in Sect. 4.1. To demonstrate the differences between CCR and AHP, the results produced by AHP enhanced method are presented in Sect. 4.2. The limitations of the proposed method are discussed in Sect. 4.3.

## 4.1 Personalization

User B completes the questionnaire. The rating scores are presented in Tables 8, 9, 10; the rating scores of User A are given in Tables 3, 4, 5. The product values for Users A and B are listed in Table 6. The system produces personalised top-10 laptop lists and laptop clusters with respect to the two users’ preferences. Table 7 presents the top-10 laptops recommended for User A; Table 11 lists the top-10 laptops recommended for User B. The two dendrograms in Fig. 4 indicate the laptops clustering results for User A and B.

Comparing the preferences indicated in Tables 3 and 8, both users require a laptop with a high-speed CPU, large storage, and acceptable graphics. Three differences between the preferences of the two users can be summarised by comparing Tables 3, 4, 5 with Tables 8, 9, 10. Firstly, User A is not very price sensitive, whereas for User B, the price is considerably more important. Secondly, User A requires a portable laptop that is light and has a long battery life; User B hardly considers portability. Thirdly, User A has no strong preference for the brand, whereas User B strongly prefers laptops produced by US companies, especially Apple and Alienware.

From the laptop configurations presented in Table 15 and the two top-10 lists generated for Users A and B, respectively, in Tables 7 and 11, it can be concluded that the laptops in the two top-10 lists meet the common requirements (high speed CPU, large storage and acceptable graphics) of the two users. There are three issues for the two users’ preferences leading to the top-10 lists results. Firstly, the best laptop for Users A and B is the same: Laptop 27. This laptop has almost all the best configurations, yet is the most expensive. The product value of Laptop 27 for User B is less than for User A. The main reason is that User B is more price sensitive. Secondly, two portable laptops, Laptops 21 and 23, are recommended to User A, even though the other configurations of the two laptops are not attractive. The main reason is that User A prefers portable laptops. Thirdly, as User B is faithful to the brands Apple and Alienware, all the laptops of the two brands are recommended to User B in the top-10 list. The laptop recommendations provided for the two users match their requirements, and it can be concluded that the proposed CCEHC method can provide personalized recommendations with respect to user preferences.

Table 6 Laptop product values for 2 users

<table><tr><td>ID (α)</td><td>Product value ( $\rho^{(\alpha)}$ ) for User A</td><td>Product value ( $\rho^{(\alpha)}$ ) for User B</td></tr><tr><td>1</td><td>0.448</td><td>0.392</td></tr><tr><td>2</td><td>0.553</td><td>0.479</td></tr><tr><td>3</td><td>0.465</td><td>0.347</td></tr><tr><td>4</td><td>0.403</td><td>0.398</td></tr><tr><td>5</td><td>0.447</td><td>0.443</td></tr><tr><td>6</td><td>0.459</td><td>0.431</td></tr><tr><td>7</td><td>0.507</td><td>0.503</td></tr><tr><td>8</td><td>0.660</td><td>0.661</td></tr><tr><td>9</td><td>0.478</td><td>0.507</td></tr><tr><td>10</td><td>0.476</td><td>0.437</td></tr><tr><td>11</td><td>0.662</td><td>0.609</td></tr><tr><td>12</td><td>0.475</td><td>0.423</td></tr><tr><td>13</td><td>0.427</td><td>0.382</td></tr><tr><td>14</td><td>0.419</td><td>0.374</td></tr><tr><td>15</td><td>0.603</td><td>0.548</td></tr><tr><td>16</td><td>0.431</td><td>0.408</td></tr><tr><td>17</td><td>0.535</td><td>0.377</td></tr><tr><td>18</td><td>0.380</td><td>0.386</td></tr><tr><td>19</td><td>0.378</td><td>0.356</td></tr><tr><td>20</td><td>0.431</td><td>0.361</td></tr><tr><td>21</td><td>0.488</td><td>0.414</td></tr><tr><td>22</td><td>0.445</td><td>0.400</td></tr><tr><td>23</td><td>0.493</td><td>0.409</td></tr><tr><td>24</td><td>0.457</td><td>0.414</td></tr><tr><td>25</td><td>0.643</td><td>0.658</td></tr><tr><td>26</td><td>0.462</td><td>0.512</td></tr><tr><td>27</td><td>0.676</td><td>0.680</td></tr></table>

Table 7 The top-10 laptops for User A

<table><tr><td>Rank</td><td>ID (α)</td><td>Product value ( $\rho^{(\alpha)}$ )</td></tr><tr><td>1</td><td>27</td><td>0.676</td></tr><tr><td>2</td><td>11</td><td>0.662</td></tr><tr><td>3</td><td>8</td><td>0.660</td></tr><tr><td>4</td><td>25</td><td>0.643</td></tr><tr><td>5</td><td>15</td><td>0.603</td></tr><tr><td>6</td><td>2</td><td>0.553</td></tr><tr><td>7</td><td>17</td><td>0.535</td></tr><tr><td>8</td><td>7</td><td>0.507</td></tr><tr><td>9</td><td>23</td><td>0.493</td></tr><tr><td>10</td><td>21</td><td>0.488</td></tr></table>

## 4.2 Comparisons between CCR and AHP

CCR is based on the cognitive network process (CNP) (Yuen 2009, 2014a). The CNP is proposed as an ideal alternative to AHP to solve the rating scale problem in AHP. The numerical definition of the $\mathbf { A H P } ^ { * } s$ s paired ratio scale inappropriately represents the human intuitive judgment of paired difference; CNP uses a paired interval scale instead of a paired ratio scale. Detailed comparisons between CNP and AHP can be found in Yuen (2009, 2014a).

This study uses the original version of AHP proposed in Saaty (1980) for comparisons. To produce the AHP results, the CCP rating scales are transformed to AHP scales. The method employed is called AHP Enhanced Hierarchical Clustering (AHPEHC). The transformation method of the rating scale between AHP and CCR is given in Yuen

Table 8 Comparison matrices for 1st level laptop attributes (User B)

<table><tr><td> $B_0$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td><td> $r_i$ </td></tr><tr><td> $\delta_1$ </td><td>0</td><td>4</td><td>2</td><td>0</td><td>2</td><td>8</td><td>0</td><td>0.184</td></tr><tr><td> $\delta_2$ </td><td>-4</td><td>0</td><td>-2</td><td>-3</td><td>-2</td><td>4</td><td>-4</td><td>0.115</td></tr><tr><td> $\delta_3$ </td><td>-2</td><td>2</td><td>0</td><td>-2</td><td>0</td><td>6</td><td>-2</td><td>0.148</td></tr><tr><td> $\delta_4$ </td><td>0</td><td>3</td><td>2</td><td>0</td><td>2</td><td>8</td><td>0</td><td>0.181</td></tr><tr><td> $\delta_5$ </td><td>-2</td><td>2</td><td>0</td><td>-2</td><td>0</td><td>6</td><td>-2</td><td>0.148</td></tr><tr><td> $\delta_6$ </td><td>-8</td><td>-4</td><td>-6</td><td>-8</td><td>-6</td><td>0</td><td>-8</td><td>0.041</td></tr><tr><td> $\delta_7$ </td><td>0</td><td>4</td><td>2</td><td>0</td><td>2</td><td>8</td><td>0</td><td>0.184</td></tr><tr><td colspan="9">AI = 0.024 &lt; 0.1</td></tr></table>

Table 9 Comparison matrices for 2nd and 3rd levels laptop attributes (User B)

(2009, 2014a). Table 12 presents the transformed rating matrix and weights of the ratings listed in Table 3. The product values and clustering results of the laptops computed using AHP are shown in Table 13 and Fig. 5, respectively.

The 27 laptop product values are displayed in Fig. 6. A significant difference between the values computed by CCR and AHP is that the product values computed by CCR are considerably closer than those computed by AHP. The results of CCR reflect that the recommendations for the products are difficult to make, whereas AHP results reflect that the problem is trivial. The reason for this difference is that the paired ratio scales applied in AHP typically exaggerate the human perception of the paired difference in ratio. It can be concluded that CCR outperforms AHP in reflecting the preferences of both expert and users.

Table 10 Comparison matrices for nominal attribute of $L _ { 2 } ,$ L and $L _ { 7 }$ (User B)

<table><tr><td> $B_3$ </td><td> $\delta_{3,1}$ </td><td> $\delta_{3,2}$ </td><td> $r_{3,i}$ </td><td> $B_{3,2}$ </td><td> $\delta_{3,2,1}$ </td><td> $\delta_{3,2,2}$ </td><td> $r_{3,2,i}$ </td><td> $B_4$ </td><td> $\delta_{4,1}$ </td><td> $\delta_{4,2}$ </td><td> $r_{4,i}$ </td></tr><tr><td> $\delta_{3,1}$ </td><td>0</td><td>2</td><td>0.5625</td><td> $\delta_{3,2,1}$ </td><td>0</td><td>8</td><td>0.75</td><td> $\delta_{4,1}$ </td><td>0</td><td>6</td><td>0.6875</td></tr><tr><td> $\delta_{3,2}$ </td><td>-2</td><td>0</td><td>0.4375</td><td> $\delta_{3,2,2}$ </td><td>-8</td><td>0</td><td>0.25</td><td> $\delta_{4,2}$ </td><td>-6</td><td>0</td><td>0.3125</td></tr><tr><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td></tr><tr><td> $B_5$ </td><td> $\delta_{5,1}$ </td><td> $\delta_{5,2}$ </td><td> $r_{5,i}$ </td><td> $B_{5,1}$ </td><td> $\delta_{5,1,1}$ </td><td> $\delta_{5,1,2}$ </td><td> $r_{5,1,i}$ </td><td> $B_6$ </td><td> $\delta_{6,1}$ </td><td> $\delta_{6,2}$ </td><td> $r_{6,i}$ </td></tr><tr><td> $\delta_{5,1}$ </td><td>0</td><td>-8</td><td>0.25</td><td> $\delta_{5,1,1}$ </td><td>0</td><td>-4</td><td>0.375</td><td> $\delta_{6,1}$ </td><td>0</td><td>-2</td><td>0.4375</td></tr><tr><td> $\delta_{5,2}$ </td><td>8</td><td>0</td><td>0.75</td><td> $\delta_{5,1,2}$ </td><td>4</td><td>0</td><td>0.625</td><td> $\delta_{6,2}$ </td><td>2</td><td>0</td><td>0.5625</td></tr><tr><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td><td colspan="4">AI = 0</td></tr></table>

<table><tr><td> $B_2$ </td><td>Linux</td><td>OS X</td><td>Windows 7</td><td>Windows 8</td><td></td><td>Preference value</td></tr><tr><td>Linux</td><td>0</td><td>-8</td><td>-1</td><td>-5</td><td></td><td>0.141</td></tr><tr><td>OS X</td><td>8</td><td>0</td><td>7</td><td>3</td><td></td><td>0.391</td></tr><tr><td>Windows 7</td><td>1</td><td>-7</td><td>0</td><td>-4</td><td></td><td>0.172</td></tr><tr><td>Windows 8</td><td>5</td><td>-3</td><td>4</td><td>0</td><td></td><td>0.297</td></tr><tr><td colspan="7">AI = 0</td></tr><tr><td> $B_6$ </td><td>Alienware</td><td>Apple</td><td>Dell</td><td>Microsoft</td><td>HP</td><td>Preference value</td></tr><tr><td>Alienware</td><td>0</td><td>0</td><td>4</td><td>8</td><td>6</td><td>0.290</td></tr><tr><td>Apple</td><td>0</td><td>0</td><td>4</td><td>7</td><td>6</td><td>0.285</td></tr><tr><td>Dell</td><td>-4</td><td>-4</td><td>0</td><td>4</td><td>3</td><td>0.195</td></tr><tr><td>Microsoft</td><td>-8</td><td>-7</td><td>-4</td><td>0</td><td>-2</td><td>0.095</td></tr><tr><td>HP</td><td>-6</td><td>-6</td><td>-3</td><td>2</td><td>0</td><td>0.135</td></tr><tr><td colspan="7">AI = 0.059</td></tr><tr><td> $B_7$ </td><td>Acer</td><td>ASUS</td><td>Lenovo</td><td>Samsung</td><td></td><td>Preference value</td></tr><tr><td>Acer</td><td>0</td><td>-6</td><td>-1</td><td>0</td><td></td><td>0.195</td></tr><tr><td>ASUS</td><td>6</td><td>0</td><td>5</td><td>6</td><td></td><td>0.383</td></tr><tr><td>Lenovo</td><td>1</td><td>-5</td><td>0</td><td>1</td><td></td><td>0.227</td></tr><tr><td>Samsung</td><td>0</td><td>-6</td><td>-1</td><td>0</td><td></td><td>0.195</td></tr><tr><td colspan="7">AI = 0</td></tr></table>

## 4.3 Limitations

Regarding the limitations, as the proposed approach is typically designed for recommendations of the latest launch products, the datasets consider the latest products (assuming that a consumer is not likely to buy an obsolete product). As the obsolete products are not considered, the data set should not be excessively large. The proposed method is not designed for processing large-scale data; the processing capability for large datasets is limited; however, this is not typically a problem as it is rare that there are a large number of new products. The scope of the proposed RS is not to address the problems solved by content based and collaborative filtering RSs; in turn, the content-based and collaborative filtering RSs are not designed to address the research problem solved by the proposed approach. The clustering validity of the proposed method is not discussed as no ground truth class labels can be used to verify the results. Internal clustering criteria, such as Davies and Bouldin (1979) and Silhoette (Rousseeuw 1987) are normally used as references, although these do not necessarily reflect real validity.

Table 11 The top-10 laptops for User B

<table><tr><td>Rank</td><td>ID (α)</td><td>Product Value (ρ(α))</td></tr><tr><td>1</td><td>27</td><td>0.680</td></tr><tr><td>2</td><td>8</td><td>0.661</td></tr><tr><td>3</td><td>25</td><td>0.658</td></tr><tr><td>4</td><td>11</td><td>0.609</td></tr><tr><td>5</td><td>15</td><td>0.548</td></tr><tr><td>6</td><td>26</td><td>0.512</td></tr><tr><td>7</td><td>9</td><td>0.507</td></tr><tr><td>8</td><td>7</td><td>0.503</td></tr><tr><td>9</td><td>2</td><td>0.479</td></tr><tr><td>10</td><td>5</td><td>0.443</td></tr></table>

Table 12 AHP comparison matrices for 1st level laptop attributes (User A)

<table><tr><td> $B_0$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td><td>weight</td></tr><tr><td> $\delta_1$ </td><td>1</td><td>2</td><td>1/2</td><td>8</td><td>1/2</td><td>2</td><td>4</td><td>0.168</td></tr><tr><td> $\delta_2$ </td><td>1/2</td><td>1</td><td>1/4</td><td>6</td><td>1/3</td><td>1</td><td>3</td><td>0.100</td></tr><tr><td> $\delta_3$ </td><td>2</td><td>4</td><td>1</td><td>8</td><td>1</td><td>4</td><td>6</td><td>0.298</td></tr><tr><td> $\delta_4$ </td><td>1/8</td><td>1/6</td><td>1/8</td><td>1</td><td>1/8</td><td>1/6</td><td>1/4</td><td>0.022</td></tr><tr><td> $\delta_5$ </td><td>2</td><td>3</td><td>1</td><td>8</td><td>1</td><td>3</td><td>5</td><td>0.264</td></tr><tr><td> $\delta_6$ </td><td>1/2</td><td>1</td><td>1/4</td><td>6</td><td>1/3</td><td>1</td><td>3</td><td>0.100</td></tr><tr><td> $\delta_7$ </td><td>1/4</td><td>1/3</td><td>1/6</td><td>4</td><td>1/5</td><td>1/3</td><td>1</td><td>0.048</td></tr></table>

## 5 Workstation recommendation with open dataset

The proposed CCEHC method can be applied to different kinds of RSs. A workstation RS is developed to demonstrate the usability of the CCEHC. As a special type of laptop, workstation is designed for technical, scientific, and other professional purposes. In general, the workstations are more expensive than the laptops. Thus, users typically spend more time selecting a suitable workstation. The RS built by CCEHC with expert opinions and user preferences could be helpful for workstation recommendation.

Table 13 Laptop product values by AHP (User A)

<table><tr><td>ID (α)</td><td>Product Value (ρ(α))</td></tr><tr><td>1</td><td>0.328</td></tr><tr><td>2</td><td>0.511</td></tr><tr><td>3</td><td>0.373</td></tr><tr><td>4</td><td>0.268</td></tr><tr><td>5</td><td>0.378</td></tr><tr><td>6</td><td>0.391</td></tr><tr><td>7</td><td>0.379</td></tr><tr><td>8</td><td>0.597</td></tr><tr><td>9</td><td>0.340</td></tr><tr><td>10</td><td>0.412</td></tr><tr><td>11</td><td>0.734</td></tr><tr><td>12</td><td>0.336</td></tr><tr><td>13</td><td>0.342</td></tr><tr><td>14</td><td>0.265</td></tr><tr><td>15</td><td>0.605</td></tr><tr><td>16</td><td>0.376</td></tr><tr><td>17</td><td>0.517</td></tr><tr><td>18</td><td>0.240</td></tr><tr><td>19</td><td>0.226</td></tr><tr><td>20</td><td>0.282</td></tr><tr><td>21</td><td>0.366</td></tr><tr><td>22</td><td>0.280</td></tr><tr><td>23</td><td>0.384</td></tr><tr><td>24</td><td>0.296</td></tr><tr><td>25</td><td>0.682</td></tr><tr><td>26</td><td>0.398</td></tr><tr><td>27</td><td>0.758</td></tr></table>

An open dataset for the characteristics and prices of laptop models (Kaggle 2018) is used for the workstation RS. The dataset contains 29 items related to workstation. The characteristics and prices of workstations obtained from the original datasets can be summarised as 13 attributes organised as a two-level attributes tree, as displayed in Fig. 7. The POMs are presented in Table 17 in the Appendix. The weights of the seven attributes $( B _ { 0 } )$ in the first level and three second-level attributes, Screen $( B _ { 2 } ) .$ Processor $( B _ { 3 } )$ , and Memory $( B _ { 4 } )$ , are evaluated by CCR. In addition, the attributes, Company $( L _ { 1 } )$ , Screen Type $( L _ { 3 } ) .$ Hard Disk Type $\left( L _ { 8 } \right)$ and OS $\left( L _ { 1 0 } \right)$ , are nominal and evaluated by CCR.

To demonstrate the usability of the workstation RS, two users, User C and D, use the CCEHC system to determine what workstation would fit their purpose. The comparison matrices of User C and D are presented in Table 17 in the Appendix. The weights of the users are indicated in the attribute trees presented in Fig. 7. To compare the results of CCR and AHP, both CCEHC and AHPEHC are used to build the workstation RSs. The recommendations produced by CCEHC and AHPEHC RSs for both users are displayed as dendrograms with clusters in Fig. 8 and the top-10 lists presented in Table 14.

![](images/72f57f3621d1bef2cf56ff5e7247ee3d81a3fa93ca70c69ea8ef7b88b8d8ef65.jpg)  
Fig. 5 Dendrogram for clusters of similar laptops produced by AHPEHC

By reading the preferences of the two users in Table 17 and Fig. 7, it can be determined that the preferences of Users C and D are not significantly different. For example, the two users both feel the memory and OS are important, and the price and weight are less important. Their preferences for Memory in the second-level attributes are also similar. The larger RAM and better type of hard disk (such as solid-state disk) are more important; however, a large hard disk capacity is less essential. The preferences of the company and processor are different. User C has certain preferences for the company of workstation, and feels the CPU and GPU are equally important; User D is not overly concerned with the company and feels the CPU is more important than GPU. By comparing the four top-10 lists produced by the two RSs for the two users, it can be observed that the RS applying CCEHC produces similar recommenders for the two users, whereas the RS applying AHPEHC method does otherwise. The recommendations produced by the two RSs are different for each user.

For the two users with similar preferences for the workstation, the RS applying CCEHC provides similar recommendations, whereas the RS applying AHPEHC provides considerably different results. The results demonstrate that the CCEHC can better reflect the user preferences than AHPEHC. The reason for the different results of CCR and AHP is the different mathematical representation of human opinions. As mentioned in Sect. 4.2, the paired ratio scales applied in AHP typically exaggerate the human perception of the paired difference in times; hence, the marginal difference in user preferences can lead to considerably different results. The application of workstation RS demonstrates that the CCEHC method can produce reasonable personalized recommendations to users.

Fig. 6 Comparsion between product values computed by CCR and AHP  
![](images/d801fdca2243127944127fd97d3d4b44cbd5d20bd5a45b97428835953ad809c8.jpg)

![](images/22fc342809a46c79878ccc1623411af066b381abd794e1d776c46a2f03885ae5.jpg)  
Fig. 7 Workstation attribute trees with the weights for User C (left) and User D (right)

![](images/17a5e194bb50a433d97088ccf0d42099424eb409c5fdae81ca8511945971d236.jpg)  
(a)

![](images/bb7942ea6c12c59453907e81ff3f65dd0b89d17c62b2bf7c6379e6af27c46074.jpg)  
(b)

![](images/e183e7de8699a40d2277f9b33a4f4c644e01e3cbe246d525d5532b2df878e25c.jpg)  
(c)

![](images/be9fa928a23bcd759231c26a764535551f52b652339ae5fa2203cc446663eec5.jpg)  
(d)  
Fig. 8 Dendrogram for workstations for a User C applying CCEHC, b User C applying AHPEHC, c User D applying CCEHC, d User D applying AHPEHC

Table 14 The top-10 workstations for each user using CCEHC and AHPEHC

<table><tr><td rowspan="3">Rank</td><td colspan="4">User C</td><td colspan="4">User D</td></tr><tr><td colspan="2">CCEHC</td><td colspan="2">AHPEHC</td><td colspan="2">CCEHC</td><td colspan="2">AHPEHC</td></tr><tr><td>ID (α)</td><td>PV ( $\rho^{(\alpha)}$ )</td><td>ID (α)</td><td>PV ( $\rho^{(\alpha)}$ )</td><td>ID (α)</td><td>PV ( $\rho^{(\alpha)}$ )</td><td>ID (α)</td><td>PV ( $\rho^{(\alpha)}$ )</td></tr><tr><td>1</td><td>1</td><td>0.860</td><td>6</td><td>0.896</td><td>1</td><td>0.852</td><td>10</td><td>0.874</td></tr><tr><td>2</td><td>6</td><td>0.850</td><td>13</td><td>0.895</td><td>6</td><td>0.837</td><td>2</td><td>0.874</td></tr><tr><td>3</td><td>13</td><td>0.829</td><td>10</td><td>0.892</td><td>10</td><td>0.818</td><td>6</td><td>0.873</td></tr><tr><td>4</td><td>10</td><td>0.829</td><td>12</td><td>0.871</td><td>13</td><td>0.812</td><td>1</td><td>0.872</td></tr><tr><td>5</td><td>9</td><td>0.819</td><td>5</td><td>0.863</td><td>9</td><td>0.810</td><td>13</td><td>0.870</td></tr><tr><td>6</td><td>12</td><td>0.815</td><td>15</td><td>0.862</td><td>15</td><td>0.805</td><td>15</td><td>0.862</td></tr><tr><td>7</td><td>15</td><td>0.813</td><td>2</td><td>0.854</td><td>12</td><td>0.795</td><td>12</td><td>0.856</td></tr><tr><td>8</td><td>23</td><td>0.810</td><td>1</td><td>0.850</td><td>5</td><td>0.794</td><td>5</td><td>0.854</td></tr><tr><td>9</td><td>5</td><td>0.807</td><td>19</td><td>0.815</td><td>19</td><td>0.786</td><td>7</td><td>0.854</td></tr><tr><td>10</td><td>19</td><td>0.797</td><td>8</td><td>0.804</td><td>7</td><td>0.784</td><td>18</td><td>0.826</td></tr></table>

## 6 Conclusions

RSs are helpful for consumers making choices among different products. To address the limitations of current AHC methods applied to RSs, this paper proposes a CCEHC approach for providing personalised product recommendations. CCEHC consists of two major parts: CCR and hierarchical clustering. CCR is used for user preferences elicitation. The user preferences elicited by CCR can be used to weigh the multi-level product attributes and quantify the nominal attribute values. The product values can be calculated by considering the attribute weights and normalised numerical attribute values. Hierarchical clustering is used to group similar products according to their product values. Recommendations can be produced according to the product values and clustering results. The applications of a laptop RS, where the dataset is collected by this research, and a workstation RS with an open dataset are demonstrated to confirm the validity and applicability of the proposed method. In RS applications, CCEHC can provide a top-10 list of products and similar products recommendations to customers based on their preferences provided.

The CCEHC method can be considered as an expert system that serves the recommendation function. As CCR can be used for expert judgments and user preferences, product data with human input can be processed by the clustering method and recommendations can be generated. The experimental results demonstrated that the proposed CCEHC method can provide personalised recommendations based on different user preferences. CCR outperformed AHP in reflecting the preferences of both expert(s) and users.

There are several possible paths for future work based on this research. Firstly, other clustering methods can be considered. Secondly, the interfaces for user input and recommendation output could be further improved for a better user experience. Thirdly, the approach to addressing missing values, such as user input data and the product data, could be further investigated. Fourthly, regarding the size of the data, the proposed method could be further improved to process large scale of data. Finally, to extend the application areas, the proposed CCEHC method could be further applied to numerous other product recommendation applications such as movie, music, book, cars, and smartphones.

## Appendix

See Tables 15, 16 and 17.

Table 15 Raw matrix D of 27 laptops

<table><tr><td>ID</td><td>Laptop model</td><td> $L_1$ </td><td> $L_2$ </td><td> $L_3$ </td><td> $L_4$ </td><td> $L_5$ </td><td> $L_6$ </td><td> $L_7$ </td><td> $L_8$ </td><td> $L_9$ </td><td> $L_{10}$ </td><td> $L_{11}$ </td><td> $L_{12}$ </td><td> $L_{13}$ </td></tr><tr><td>1</td><td>Lenovo Yoga3 14-IFI</td><td>3367</td><td>Win8</td><td>4</td><td>1</td><td>256</td><td>0</td><td>Lenovo</td><td>14</td><td>2,073,600</td><td>2385</td><td>1.6</td><td>6</td><td>7</td></tr><tr><td>2</td><td>Lenovo Y430p AT-ISE</td><td>6830</td><td>Win8</td><td>8</td><td>0</td><td>1000</td><td>0</td><td>Lenovo</td><td>14</td><td>1,049,088</td><td>4385</td><td>2.5</td><td>5</td><td>6</td></tr><tr><td>3</td><td>Lenovo ThinkPad E540 20C60019CD</td><td>3882</td><td>Linux</td><td>4</td><td>0</td><td>1000</td><td>0</td><td>Lenovo</td><td>15.6</td><td>1,049,088</td><td>1848</td><td>2.44</td><td>6</td><td>4</td></tr><tr><td>4</td><td>Dell XPS 11 (XPS11D-1508T)</td><td>2039</td><td>Win8</td><td>4</td><td>1</td><td>256</td><td>Dell</td><td>0</td><td>11.6</td><td>3,686,400</td><td>638</td><td>1.13</td><td>6</td><td>8</td></tr><tr><td>5</td><td>Dell Inspiron 15 (INS15UD-1748S)</td><td>3807</td><td>Win8</td><td>8</td><td>0</td><td>1000</td><td>Dell</td><td>0</td><td>15.6</td><td>1,049,088</td><td>1705</td><td>2.3</td><td>4</td><td>5</td></tr><tr><td>6</td><td>Dell Inspiron 15 7000 (Ins15BD-1748)</td><td>3807</td><td>Win8</td><td>8</td><td>0</td><td>1000</td><td>Dell</td><td>0</td><td>15.6</td><td>1,049,088</td><td>1857</td><td>2.11</td><td>7</td><td>7</td></tr><tr><td>7</td><td>MacBook 256 GB</td><td>2589</td><td>OS</td><td>8</td><td>1</td><td>256</td><td>Apple</td><td>0</td><td>12</td><td>3,317,760</td><td>658</td><td>0.92</td><td>9</td><td>9</td></tr><tr><td>8</td><td>MacBook Pro 15&#x27;</td><td>6990</td><td>OS</td><td>16</td><td>1</td><td>512</td><td>Apple</td><td>0</td><td>15.4</td><td>5,184,000</td><td>2543</td><td>2.02</td><td>9</td><td>17</td></tr><tr><td>9</td><td>MacBook Air (MJVE2CH/A)</td><td>3393</td><td>OS</td><td>4</td><td>1</td><td>128</td><td>Apple</td><td>0</td><td>13.3</td><td>1,296,000</td><td>1333</td><td>1.35</td><td>9</td><td>7</td></tr><tr><td>10</td><td>ASUS A550JK4200</td><td>4361</td><td>Win8</td><td>4</td><td>0</td><td>1000</td><td>0</td><td>ASUS</td><td>15.6</td><td>2,073,600</td><td>4385</td><td>2.35</td><td>4</td><td>5</td></tr><tr><td>11</td><td>ASUS GFX71JY4710</td><td>6980</td><td>Win8</td><td>16</td><td>0.5</td><td>1256</td><td>0</td><td>ASUS</td><td>17.3</td><td>2,073,600</td><td>12,632</td><td>4.8</td><td>3</td><td>19</td></tr><tr><td>12</td><td>ASUS U305FA5Y71 (8 GB/256 GB)</td><td>2503</td><td>Win8</td><td>8</td><td>4</td><td>256</td><td>0</td><td>ASUS</td><td>13.3</td><td>2,073,600</td><td>658</td><td>1.2</td><td>10</td><td>6</td></tr><tr><td>13</td><td>Acer VN7-591G-56BD</td><td>3367</td><td>Win8</td><td>4</td><td>0</td><td>500</td><td>0</td><td>Acer</td><td>15.6</td><td>2,073,600</td><td>4385</td><td>2.4</td><td>4</td><td>5</td></tr><tr><td>14</td><td>Acer E1-470G-33212G50Dnkk</td><td>2229</td><td>Linux</td><td>2</td><td>0</td><td>500</td><td>0</td><td>Acer</td><td>14</td><td>1,049,088</td><td>1213</td><td>2.1</td><td>4</td><td>2</td></tr><tr><td>15</td><td>Acer VN7-791G-78KL</td><td>7060</td><td>Win8</td><td>8</td><td>0.5</td><td>1064</td><td>0</td><td>Acer</td><td>17.3</td><td>2,073,600</td><td>9840</td><td>3</td><td>3</td><td>8</td></tr><tr><td>16</td><td>HP Envy 15-k222tx</td><td>3367</td><td>Win8</td><td>4</td><td>0</td><td>1000</td><td>HP</td><td>0</td><td>15.6</td><td>1,049,088</td><td>4385</td><td>2.34</td><td>4</td><td>5</td></tr><tr><td>17</td><td>HP ProBook 440 G2 (J7W06PA)</td><td>3420</td><td>Win7</td><td>8</td><td>0</td><td>1500</td><td>HP</td><td>0</td><td>14</td><td>1,440,000</td><td>1784</td><td>1.83</td><td>9</td><td>6</td></tr><tr><td>18</td><td>HP Pavilion 11-h112tu × 2 (G0A07PA)</td><td>2071</td><td>Win8</td><td>4</td><td>1</td><td>128</td><td>HP</td><td>0</td><td>11.6</td><td>1,049,088</td><td>638</td><td>1.49</td><td>6</td><td>5</td></tr><tr><td>19</td><td>Samsung 910S3G-K04</td><td>1375</td><td>Win8</td><td>4</td><td>1</td><td>128</td><td>0</td><td>Samsung</td><td>13.3</td><td>1,049,088</td><td>638</td><td>1.44</td><td>5</td><td>4</td></tr><tr><td>20</td><td>Samsung 930X2K-K01</td><td>2492</td><td>Win8</td><td>4</td><td>1</td><td>128</td><td>0</td><td>Samsung</td><td>12.2</td><td>4,096,000</td><td>658</td><td>0.95</td><td>7</td><td>8</td></tr><tr><td>21</td><td>Samsung 900X3K-K01</td><td>3807</td><td>Win8</td><td>8</td><td>1</td><td>256</td><td>0</td><td>Samsung</td><td>13.3</td><td>5,760,000</td><td>968</td><td>1.07</td><td>6</td><td>10</td></tr><tr><td>22</td><td>Surface Pro 3(i3/64 GB)</td><td>1675</td><td>Win8</td><td>4</td><td>1</td><td>64</td><td>Microsoft</td><td>0</td><td>12</td><td>3,110,400</td><td>638</td><td>0.8</td><td>9</td><td>4</td></tr><tr><td>23</td><td>Surface Pro 3 (i7/512 GB/Profession)</td><td>3249</td><td>Win8</td><td>8</td><td>1</td><td>512</td><td>Microsoft</td><td>0</td><td>12</td><td>3,110,400</td><td>1033</td><td>0.8</td><td>9</td><td>12</td></tr><tr><td>24</td><td>Surface 3 (4 GB/128 GB)</td><td>2320</td><td>Win8</td><td>4</td><td>1</td><td>128</td><td>Microsoft</td><td>0</td><td>10.8</td><td>2,457,600</td><td>638</td><td>0.887</td><td>10</td><td>4</td></tr><tr><td>25</td><td>Alienware 15 (ALW15ED-1718)</td><td>6980</td><td>Win8</td><td>16</td><td>0.5</td><td>1128</td><td>Alienware</td><td>0</td><td>15.6</td><td>2,073,600</td><td>9809</td><td>3.207</td><td>4</td><td>15</td></tr><tr><td>26</td><td>Alienware 13 (ALW13ED-2708)</td><td>3807</td><td>Win8</td><td>8</td><td>1</td><td>384</td><td>Alienware</td><td>0</td><td>13.3</td><td>2,073,600</td><td>5249</td><td>2.058</td><td>3</td><td>13</td></tr><tr><td>27</td><td>Alienware 17 (ALW17ED-2728)</td><td>7060</td><td>Win8</td><td>16</td><td>0.5</td><td>1512</td><td>Alienware</td><td>0</td><td>17.3</td><td>2,073,600</td><td>12,632</td><td>3.78</td><td>3</td><td>21</td></tr></table>

Table 16 Comparison matrices of User C and User D (for attribute weights and nominal attribute values)

<table><tr><td colspan="12">User C</td><td colspan="11">User D</td><td></td><td></td></tr><tr><td> $B_0$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td><td> $B_2$ </td><td> $\delta_{2,1}$ </td><td> $\delta_{2,2}$ </td><td> $\delta_{2,3}$ </td><td> $B_0$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td><td> $B_2$ </td><td> $\delta_{2,1}$ </td><td> $\delta_{2,2}$ </td><td> $\delta_{2,3}$ </td><td></td></tr><tr><td> $\delta_1$ </td><td>0</td><td>3</td><td>2</td><td>-1</td><td>-2</td><td>1</td><td>4</td><td> $\delta_{2,1}$ </td><td>0</td><td>1</td><td>-3</td><td> $\delta_1$ </td><td>0</td><td>-1</td><td>-4</td><td>-2</td><td>-2</td><td>1</td><td>0</td><td> $\delta_{2,1}$ </td><td>0</td><td>3</td><td>-1</td><td></td></tr><tr><td> $\delta_2$ </td><td>-3</td><td>0</td><td>-1</td><td>-3</td><td>-4</td><td>-2</td><td>1</td><td> $\delta_{2,2}$ </td><td>-1</td><td>0</td><td>-3</td><td> $\delta_2$ </td><td>1</td><td>0</td><td>-3</td><td>-1</td><td>-2</td><td>2</td><td>1</td><td> $\delta_{2,2}$ </td><td>-3</td><td>0</td><td>-4</td><td></td></tr><tr><td> $\delta_3$ </td><td>-2</td><td>1</td><td>0</td><td>-3</td><td>-3</td><td>-1</td><td>2</td><td> $\delta_{2,3}$ </td><td>3</td><td>3</td><td>0</td><td> $\delta_3$ </td><td>4</td><td>3</td><td>0</td><td>2</td><td>2</td><td>4</td><td>3</td><td> $\delta_{2,3}$ </td><td>1</td><td>4</td><td>0</td><td></td></tr><tr><td> $\delta_4$ </td><td>1</td><td>3</td><td>3</td><td>0</td><td>1</td><td>2</td><td>5</td><td colspan="4">AI = 0.048</td><td></td><td>2</td><td>1</td><td> $\delta_4$ </td><td>0</td><td>0</td><td>3</td><td>2</td><td colspan="3">AI = 0</td><td></td><td></td></tr><tr><td> $\delta_5$ </td><td>2</td><td>4</td><td>3</td><td>-1</td><td>0</td><td>2</td><td>5</td><td> $B_4$ </td><td> $\delta_{4,1}$ </td><td> $\delta_{4,2}$ </td><td> $\delta_{4,3}$ </td><td> $\delta_5$ </td><td>2</td><td>2</td><td>-2</td><td>0</td><td>0</td><td>3</td><td>2</td><td> $B_4$ </td><td> $\delta_{4,1}$ </td><td> $\delta_{4,2}$ </td><td> $\delta_{4,3}$ </td><td></td></tr><tr><td> $\delta_6$ </td><td>-1</td><td>2</td><td>1</td><td>-2</td><td>-2</td><td>0</td><td>3</td><td> $\delta_{4,1}$ </td><td>0</td><td>-2</td><td>1</td><td> $\delta_6$ </td><td>-1</td><td>-2</td><td>-4</td><td>-3</td><td>-3</td><td>0</td><td>-1</td><td> $\delta_{4,1}$ </td><td>0</td><td>-3</td><td>3</td><td></td></tr><tr><td> $\delta_7$ </td><td>-4</td><td>-1</td><td>-2</td><td>-5</td><td>-5</td><td>-3</td><td>0</td><td> $\delta_{4,1}$ </td><td>2</td><td>0</td><td>3</td><td> $\delta_7$ </td><td>0</td><td>-1</td><td>-3</td><td>-2</td><td>-2</td><td>1</td><td>0</td><td> $\delta_{4,1}$ </td><td>3</td><td>0</td><td>5</td><td></td></tr><tr><td colspan="8">AI = 0.057</td><td> $\delta_{4,3}$ </td><td>-1</td><td>-3</td><td>0</td><td colspan="9">AI = 0.050</td><td> $\delta_{4,3}$ </td><td>-3</td><td>-5</td><td>0</td></tr><tr><td colspan="8"></td><td colspan="4">AI = 0</td><td colspan="9"></td><td colspan="3">AI = 0.048</td><td></td></tr><tr><td> $L_3$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td><td></td><td></td><td></td><td> $L_8$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td><td> $L_3$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td><td></td><td></td><td> $L_8$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td></tr><tr><td> $v_1$ </td><td>0</td><td>2</td><td>1</td><td>-1</td><td></td><td></td><td></td><td> $v_1$ </td><td>0</td><td>-1</td><td>2</td><td>1</td><td> $v_1$ </td><td>0</td><td>3</td><td>2</td><td>-2</td><td></td><td></td><td> $v_1$ </td><td>0</td><td>-1</td><td>4</td><td>1</td></tr><tr><td> $v_2$ </td><td>-2</td><td>0</td><td>-1</td><td>-2</td><td></td><td></td><td></td><td> $v_2$ </td><td>1</td><td>0</td><td>3</td><td>2</td><td> $v_2$ </td><td>2</td><td>0</td><td>-1</td><td>-5</td><td></td><td></td><td> $v_2$ </td><td>1</td><td>0</td><td>5</td><td>2</td></tr><tr><td> $v_3$ </td><td>-1</td><td>1</td><td>0</td><td>-3</td><td></td><td></td><td></td><td> $v_3$ </td><td>-2</td><td>-3</td><td>0</td><td>-1</td><td> $v_3$ </td><td>1</td><td>-1</td><td>0</td><td>-4</td><td></td><td></td><td> $v_3$ </td><td>-4</td><td>-5</td><td>0</td><td>-4</td></tr><tr><td> $v_4$ </td><td>1</td><td>2</td><td>3</td><td>0</td><td></td><td></td><td></td><td> $v_4$ </td><td>-1</td><td>-2</td><td>1</td><td>0</td><td> $v_4$ </td><td>-1</td><td>-3</td><td>-2</td><td>0</td><td></td><td></td><td> $v_4$ </td><td>-1</td><td>-2</td><td>4</td><td>0</td></tr><tr><td colspan="8">AI = 0.077</td><td colspan="4">AI = 0</td><td></td><td colspan="8">AI = 0</td><td colspan="3">AI = 0.042</td><td></td></tr><tr><td> $L_1$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td></td><td> $B_3$ </td><td> $\delta_{3,1}$ </td><td> $\delta_{3,2}$ </td><td></td><td> $L_{10}$ </td><td> $v_1$ </td><td> $v_2$ </td><td></td><td> $L_1$ </td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td></td><td></td><td> $B_3$ </td><td> $\delta_{3,1}$ </td><td> $\delta_{3,2}$ </td><td></td><td> $L_{10}$ </td><td> $v_1$ </td></tr><tr><td> $v_1$ </td><td>0</td><td>2</td><td>1</td><td></td><td> $\delta_{3,1}$ </td><td>0</td><td>0</td><td></td><td> $v_1$ </td><td>0</td><td>4</td><td></td><td> $v_1$ </td><td>0</td><td>0</td><td>2</td><td></td><td></td><td> $\delta_{3,1}$ </td><td>0</td><td>5</td><td></td><td> $v_1$ </td><td>0</td></tr><tr><td> $v_2$ </td><td>-2</td><td>0</td><td>1</td><td></td><td> $\delta_{3,2}$ </td><td>0</td><td>0</td><td></td><td> $v_2$ </td><td>-4</td><td>0</td><td></td><td> $v_2$ </td><td>0</td><td>0</td><td>2</td><td></td><td></td><td> $\delta_{3,2}$ </td><td>-5</td><td>0</td><td></td><td> $v_2$ </td><td>0</td></tr><tr><td> $v_3$ </td><td>-1</td><td>-1</td><td>0</td><td></td><td colspan="3">AI = 0</td><td></td><td></td><td colspan="2">AI = 0</td><td></td><td> $v_3$ </td><td>-2</td><td>-2</td><td>0</td><td></td><td></td><td colspan="3">AI = 0</td><td></td><td></td><td></td></tr><tr><td colspan="8">AI = 0.096</td><td></td><td></td><td></td><td></td><td></td><td colspan="11">AI = 0</td><td></td></tr></table>

Table 17 Normalized data matrix D’ of 27 laptops For User A

<table><tr><td>ID</td><td> $L_1$ </td><td> $L_2$ </td><td> $L_3$ </td><td> $L_4$ </td><td> $L_5$ </td><td> $L_6$ </td><td> $L_7$ </td><td> $L_8$ </td><td> $L_9$ </td><td> $L_{10}$ </td><td> $L_{11}$ </td><td> $L_{12}$ </td><td> $L_{13}$ </td></tr><tr><td>1</td><td>0.477</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.169</td><td>0.000</td><td>1.000</td><td>0.809</td><td>0.360</td><td>0.189</td><td>0.500</td><td>0.600</td><td>0.286</td></tr><tr><td>2</td><td>0.967</td><td>0.692</td><td>0.500</td><td>0.000</td><td>0.661</td><td>0.000</td><td>1.000</td><td>0.809</td><td>0.182</td><td>0.347</td><td>0.320</td><td>0.500</td><td>0.333</td></tr><tr><td>3</td><td>0.550</td><td>0.692</td><td>0.250</td><td>0.000</td><td>0.661</td><td>0.000</td><td>1.000</td><td>0.902</td><td>0.182</td><td>0.146</td><td>0.328</td><td>0.600</td><td>0.500</td></tr><tr><td>4</td><td>0.289</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.169</td><td>0.672</td><td>0.000</td><td>0.671</td><td>0.640</td><td>0.051</td><td>0.708</td><td>0.600</td><td>0.250</td></tr><tr><td>5</td><td>0.539</td><td>0.692</td><td>0.500</td><td>0.000</td><td>0.661</td><td>0.672</td><td>0.000</td><td>0.902</td><td>0.182</td><td>0.135</td><td>0.348</td><td>0.400</td><td>0.400</td></tr><tr><td>6</td><td>0.539</td><td>0.692</td><td>0.500</td><td>0.000</td><td>0.661</td><td>0.672</td><td>0.000</td><td>0.902</td><td>0.182</td><td>0.147</td><td>0.379</td><td>0.700</td><td>0.286</td></tr><tr><td>7</td><td>0.367</td><td>0.897</td><td>0.500</td><td>1.000</td><td>0.169</td><td>0.983</td><td>0.000</td><td>0.694</td><td>0.576</td><td>0.052</td><td>0.870</td><td>0.900</td><td>0.222</td></tr><tr><td>8</td><td>0.990</td><td>0.897</td><td>1.000</td><td>1.000</td><td>0.339</td><td>0.983</td><td>0.000</td><td>0.890</td><td>0.900</td><td>0.201</td><td>0.396</td><td>0.900</td><td>0.118</td></tr><tr><td>9</td><td>0.481</td><td>0.897</td><td>0.250</td><td>1.000</td><td>0.085</td><td>0.983</td><td>0.000</td><td>0.769</td><td>0.225</td><td>0.106</td><td>0.593</td><td>0.900</td><td>0.286</td></tr><tr><td>10</td><td>0.618</td><td>0.692</td><td>0.250</td><td>0.000</td><td>0.661</td><td>0.000</td><td>0.829</td><td>0.902</td><td>0.360</td><td>0.347</td><td>0.340</td><td>0.400</td><td>0.400</td></tr><tr><td>11</td><td>0.989</td><td>0.692</td><td>1.000</td><td>0.500</td><td>0.831</td><td>0.000</td><td>0.829</td><td>1.000</td><td>0.360</td><td>1.000</td><td>0.167</td><td>0.300</td><td>0.105</td></tr><tr><td>12</td><td>0.355</td><td>0.692</td><td>0.500</td><td>1.000</td><td>0.169</td><td>0.000</td><td>0.829</td><td>0.769</td><td>0.360</td><td>0.052</td><td>0.667</td><td>1.000</td><td>0.333</td></tr><tr><td>13</td><td>0.477</td><td>0.692</td><td>0.250</td><td>0.000</td><td>0.331</td><td>0.000</td><td>0.732</td><td>0.902</td><td>0.360</td><td>0.347</td><td>0.333</td><td>0.400</td><td>0.400</td></tr><tr><td>14</td><td>0.316</td><td>0.692</td><td>0.125</td><td>0.000</td><td>0.331</td><td>0.000</td><td>0.732</td><td>0.809</td><td>0.182</td><td>0.096</td><td>0.381</td><td>0.400</td><td>1.000</td></tr><tr><td>15</td><td>1.000</td><td>0.692</td><td>0.500</td><td>0.500</td><td>0.704</td><td>0.000</td><td>0.732</td><td>1.000</td><td>0.360</td><td>0.779</td><td>0.267</td><td>0.300</td><td>0.250</td></tr><tr><td>16</td><td>0.477</td><td>0.692</td><td>0.250</td><td>0.000</td><td>0.661</td><td>0.466</td><td>0.000</td><td>0.902</td><td>0.182</td><td>0.347</td><td>0.342</td><td>0.400</td><td>0.400</td></tr><tr><td>17</td><td>0.484</td><td>1.000</td><td>0.500</td><td>0.000</td><td>0.992</td><td>0.466</td><td>0.000</td><td>0.809</td><td>0.250</td><td>0.141</td><td>0.437</td><td>0.900</td><td>0.333</td></tr><tr><td>18</td><td>0.293</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.085</td><td>0.466</td><td>0.000</td><td>0.671</td><td>0.182</td><td>0.051</td><td>0.537</td><td>0.600</td><td>0.400</td></tr><tr><td>19</td><td>0.195</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.085</td><td>0.000</td><td>0.561</td><td>0.769</td><td>0.182</td><td>0.051</td><td>0.556</td><td>0.500</td><td>0.500</td></tr><tr><td>20</td><td>0.353</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.085</td><td>0.000</td><td>0.561</td><td>0.705</td><td>0.711</td><td>0.052</td><td>0.842</td><td>0.700</td><td>0.250</td></tr><tr><td>21</td><td>0.539</td><td>0.692</td><td>0.500</td><td>1.000</td><td>0.169</td><td>0.000</td><td>0.561</td><td>0.769</td><td>1.000</td><td>0.077</td><td>0.748</td><td>0.600</td><td>0.200</td></tr><tr><td>22</td><td>0.237</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.042</td><td>0.328</td><td>0.000</td><td>0.694</td><td>0.540</td><td>0.051</td><td>1.000</td><td>0.900</td><td>0.500</td></tr><tr><td>23</td><td>0.460</td><td>0.692</td><td>0.500</td><td>1.000</td><td>0.339</td><td>0.328</td><td>0.000</td><td>0.694</td><td>0.540</td><td>0.082</td><td>1.000</td><td>0.900</td><td>0.167</td></tr><tr><td>24</td><td>0.329</td><td>0.692</td><td>0.250</td><td>1.000</td><td>0.085</td><td>0.328</td><td>0.000</td><td>0.624</td><td>0.427</td><td>0.051</td><td>0.902</td><td>1.000</td><td>0.500</td></tr><tr><td>25</td><td>0.989</td><td>0.692</td><td>1.000</td><td>0.500</td><td>0.746</td><td>1.000</td><td>0.000</td><td>0.902</td><td>0.360</td><td>0.777</td><td>0.249</td><td>0.400</td><td>0.133</td></tr><tr><td>26</td><td>0.539</td><td>0.692</td><td>0.500</td><td>1.000</td><td>0.254</td><td>1.000</td><td>0.000</td><td>0.769</td><td>0.360</td><td>0.416</td><td>0.389</td><td>0.300</td><td>0.154</td></tr><tr><td>27</td><td>1.000</td><td>0.692</td><td>1.000</td><td>0.500</td><td>1.000</td><td>1.000</td><td>0.000</td><td>1.000</td><td>0.360</td><td>1.000</td><td>0.212</td><td>0.300</td><td>0.095</td></tr></table>

Acknowledgements The research work reported in this paper is partially supported by Research Grants from Shanghai Municipal Science and Technology Major Project (Project Number 2021SHZDZX0103) and National Natural Science Foundation of China (Project Number 61503306).

## Declarations

Conflict of interest The authors declare they have no conflicts of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

## References

3DMARK (2015) 3DMARK. http://www.futuremark.com/bench marks/legacy. Retrieved 3 2015

Adomavicius G, Manouselis N, Kwon Y (2011) Multi-Criteria Recommender Systems. In: Ricci F, Rokach L, Shapira B, Kantor P (eds) Recommender Systems Handbook. Springer, Boston, MA, pp.769–803

Aggarwal CC (2016) Recommender systems. Springer Internationa Publishing, Berlin

Davies DL, Bouldin DW (1979) A cluster separation measure. IEEE Trans Pattern Anal Mach Intell 2:224–227

de Aguiar Neto FS, da Costa AF, Manzato MG, Campello RJ (2020) Pre-processing approaches for collaborative filtering based on hierarchical clustering. Inf Sci 534:172–191

Fre´mal S, Lecron F (2017) Weighting strategies for a recommender system using item clustering based on genres. Expert Syst Appl 77:105–113

Guan C (2018) Evolutionary and swarm algorithm optimized densitybased clustering and classification for data analytics. Ph.D. thesis, University of Liverpool

Guan C, Yuen KK (2015) Towards a hybrid approach of primitive cognitive network process and agglomerative hierarchical clustering for music recommendation. In: Heterogeneous networking for quality, reliability, security and robustness (QSHINE), 2015 11th international conference on. IEEE, pp 206–209

Guan C, Yuen KK, Coenen F (2018) Particle swarm optimized density-based clustering and classification: supervised and unsupervised learning approaches. Swarm Evol Comput 44:876–896

Gupta U, Patil N (2015) Recommender system based on hierarchical clustering algorithm chameleon. In: 2015 IEEE international advance computing conference (IACC)

Han J, Pei J, Kamber M (2011) Data mining: concepts and techniques. Elsevier, Amsterdam

Haruna K, Akmar Ismail M, Suhendroyono S, Damiasih D, Pierewan AC, Chiroma H, Herawan T (2017) Context-aware recommender system: a review of recent developmental process and future research direction. Appl Sci 46:1211

Hinduja A, Pandey M (2018) An intuitionistic fuzzy AHP based multi criteria recommender system for life insurance products. Int J Adv Stud Comput Sci Eng 38(5):1–8

Kaggle (2018) Characteristics and price for 1300 laptop models. (Kaggle Inc.). https://www.kaggle.com/ionaskel/laptop-prices. Retrieved 11 2018

Karthikeyan R, Michael G, Kumaravel A (2017) A housing selection method for design, implementation & evaluation for web based recommended systems. Int J Pure Appl Math 42(3):23–28

Katarya R, Verma OP (2017) An effective web page recommender system with fuzzy c-mean clustering. Multim Tools Appl 34(2):21481–21496

Kotkov D, Wang S, Veijalainen J (2016) A survey of serendipity in recommender systems. Knowl Based Syst 111:180–192

Kunaver M, Pozˇrl T (2017) Diversity in recommender systems—a survey. Knowl-Based Syst 12(4):154–162

Lika B, Kolomvatsos K, Hadjiefthymiades S (2014) Facing the cold start problem in recommender systems. Expert Syst Appl 41(4):2065–2073

Ma YY, Zhang HR, Xu YY, Gao L (2018) Three-way recommendation integrating global and local information. J Eng 16:1397–1401

Murtagh F (1983) A survey of recent advances in hierarchical clustering algorithms. Comput J 26(4):354–359

Nilashi MB (2017) Clustering items for collaborative A recommender system for tourism industry using cluster ensemble and prediction machine learning techniques. Comput Ind Eng 109:357–368

Pamucˇar D, Stevic´ Z<sup>ˇ</sup> , Zavadskas EK (2018) Integration of interval rough AHP and interval rough MABAC methods for evaluating university web pages. Appl Soft Comput 42(3):141–163

Rousseeuw PJ (1987) Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. J Comput Appl Math 20:53–65

Saaty T (1980) Analytic hierarchy process: planning, priority, setting resource allocation. McGraw-Hill, New York

Selvi C, Sivasankar E (2019) A novel optimization algorithm for recommender system using modified fuzzy c-means clustering approach. Soft Comput 23:1901–1916

Song WS (2018) An environmentally conscious PSS recommendation method based on users’ vague ratings: a rough multi-criteria approach. J Clean Prod 26(2):1592–1606

van Capelleveen G, Amrit C, Yazan DM, Zijm H (2019) The recommender canvas: a model for developing and documenting recommender system design. Expert Syst Appl 22(3):97–117

Viktoratos I, Tsadiras A, Bassiliades N (2018) Combining community-based knowledge with association rule mining to alleviate the cold start problem in context-aware recommender systems. Expert Syst Appl 108:78–90. https://doi.org/10.1016/j.eswa. 2018.01.044

Volkovs M, Yu G, Poutanen T (2017) Dropoutnet: addressing cold start in recommender systems. Adv Neural Inf Process Sys 40(3):4957–4966

Wang Y, Tseng MM (2013) Customized products recommendation based on probabilistic relevance model. J Intell Manuf 24(5):951–960

Ward JH Jr (1963) Hierarchical grouping to optimize an objective function. J Am Stat Assoc 58(301):236–244

Yuen KK (2009) Cognitive network process with fuzzy soft computing technique in collective decision aiding. The Hong Kong Polytechnic University

Yuen KK (2012) Pairwise opposite matrix and its cognitive prioritization operators: comparisons with pairwise reciprocal matrix and analytic prioritization operators. J Oper Res Soc 63(3):322–338

Yuen KK (2014a) Fuzzy cognitive network process: comparisons with fuzzy analytic hierarchy process in new product development strategy. IEEE Trans Fuzzy Syst 22(3):597–610

Yuen KK (2014b) The Primitive cognitive network process in healthcare and medical decision making: comparisons with the analytic hierarchy process. Appl Soft Comput 14:109–119

Zhang HR, Min F, Shi B (2017) Regression-based three-way recommendation. Inf Sci 378:444–461. https://doi.org/10.1016 j.ins.2016.03.019

Zhang C, Zhang H, Wang J (2018) Personalized restaurant recommendation method combining group correlations and customer preferences. Inf Sci 454–455:128–143. https://doi.org/10.1016/j. ins.2018.04.061

Zheng L, Li L, Hong W, Li T (2013) PENETRATE: personalized news recommendation using ensemble hierarchical clustering. Expert Syst Appl 6(3):2127–2136

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.