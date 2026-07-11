# Integrating rich and heterogeneous information to design a ranking system for multiple products

Xian Yang, Guangfei Yang ⁎, Jiangning Wu

School of Management Science and Engineering, Dalian University of Technology, Dalian, China

## a r t i c l e i n f o

Article history: Received 1 April 2015 Received in revised form 13 December 2015 Accepted 20 February 2016 Available online 27 February 2016

Keywords: Text sentiments Numeric rating Comparative relationships Product rankings

## a b s t r a c t

The online review plays an important role as electronic word-of-mouth (eWoM) for potential consumers to make informed purchase decisions. However, the large number of reviews poses a considerable challenge because it is impossible for customers to read all of them for reference, Moreover, there are different types of online reviews with distinct features, such as numeric ratings, text descriptions, and comparative words, for example; such heterogeneous information leads to more complexity for customers. In this paper, we propose a method to integrate such rich and heterogeneous information. The integrated information can be classi ed into two categories: descriptive information and comparative information. The descriptive information consists of online opinions directly given by consumers using text sentiments and numeric ratings to describe one specific product. The comparative information comes from comparative sentences that are implicitly embedded in the reviews and online comparative votes that are explicitly provided by third-party websites to compare more than one product. Both descriptive information and comparative information are integrated into a digraph structure, from which an overall eWOM score for each product and a ranking of all products can be derived, We collect both descriptive and comparative information for three different categories of products (mobile phones, laptops, and digital cameras) during a period of 10 days. The results demonstrate that our method can provide improved performance compared with those of existing product ranking methods. A ranking system based on our method is also provided that can help consumers to compare multiple products and make appropriate purchase decisions effortlessly.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rapid development of e-business and Web 2.0, an increasing number of people prefer to shop online and exchange opinions through the Internet. Researchers often refer to theses online opinions in consumer reviews about a product, service, brand, or company as electronic word-of-mouth (eWOM). eWOM is becoming a major source of information for potential buyers to make informed purchase decisions [10,18,20]. Nicosia [39] argues that information search and alternatives evaluation are two of five essential stages of the consumer-purchase decision process: (1) problem recognition, (2) information search, (3) evaluation of alternatives, (4) purchase decisions, and (5) post-purchase behavior. A survey<sup>1</sup> found that 63% of online shoppers consistently search and read reviews before making a purchasing decision. Among these, 64% of the online shoppers spend 10 min reading reviews, whereas 33% spend 30 min or more. Evidently, an increasing number of consumers prefer to evaluate and choose products based on eWOM about products.

The most common online reviews are numeric ratings and text reviews. A numeric rating is merely a score, whereas a text review is one comment with a more detailed description of sentiments. Some studies have found that numeric rating and text review both affect consumers' purchasing decision, but their valences are not consistent [1,24]. However, the available number of consumer reviews is in the tens of thousands and rapidly grows; when potential consumers want to buy a product, it is a great challenge for them to read all the reviews, evaluate eWOM of the alternative products, and choose the one they prefer.

To help consumers compare alternative products, there are some studies that describe methods to extract opinions and sentences from text reviews [23,28,29,34,49]. Some of these studies focus on mining and summarizing customers' opinions and text sentiments from text reviews [23,34], whereas other studies directly mine comparative sentences and relationships from text reviews [28,29,49]. However, comparative sentences are very rare in text reviews, and they are usually not sufficient to evaluate competitive products comprehensively because there are a limited number of comparisons for some products and even no comparison for many (if not most) products. Moreover, comparative sentences only compare several products (usually two or three products), and not all alternative products have been compared simultaneously.

To compare multiple products, some websites provide rankings of products according to simple criteria such as the average numeric rating; however, these rankings do not fully consider the voice of customers, such as the text sentiments and comparative sentences. Recently, several approaches have been proposed to rank multiple products by integrating the text sentiments and comparative sentences [30,32,51,52,54], approaches that have shown promising results to provide effective rankings. However, their applicability is again restricted by the limited number of comparative sentences. Moreover, they omit some important facets of customers' voice, such as the numeric rating which is simple but useful [1,20,36,17].

In this paper, we propose a new ranking method to integrate heterogeneous information including text sentiments, numeric ratings, comparative sentences, and comparative votes. Online comparative votes, directly provided by some third-party review websites, allow customers to compare a pair of products side by side and vote for the one they prefer. In contrast to writing detailed comments to compare products, the online votes can be easily implemented by simple clicks, thus attracting many more people to vote for the products they like. As far as we know, such comparative voting has not been employed in previous related studies.

We classify heterogeneous information into two categories: descriptive information and comparative information. Descriptive information consists of text sentiments and numeric ratings to describe one specific product. Comparative information comes from comparative sentences and online comparative votes that compare more than one product. The previous research usually studied one or two types of information, and little research concentrated on the combination of comprehensive information to aid the customers' decision-making. In addition, the abundant information provided by comparative votes has not been explored by the current research, and its effect remains unclear. In this paper, we integrate the rich and heterogeneous information, including comparative votes, to provide a ranking method that can help consumers to compare multiple products effectively and make appropriate purchase decisions effortlessly.

This paper makes the following contributions:

(1) A unified eWOM ranking model is proposed to integrate the most comprehensive descriptive and comparative information, to the best of our knowledge, to compare multiple products.

(2) In addition to the limited comparative sentences, a huge number of online comparative votes is employed for the first time to enhance the quality of comparative information significantly.

(3) An effective system is provided to help consumers rank multiple products and assist manufacturers to analyze the competitive intelligence of their products and improve product sales.

There are many related research studies of the emerging value from eWOM, and our research follows this rapidly growing frontier. These studies could provide people with critical insights when making decisions, and in our case, a ranking list as well as a comparative graph of products could be developed to help the customers.

The rest of this paper is organized as follows. In Section 2, we review related works about description and comparative information and product ranking methods based on the integrated information. In Section 3, we propose a method to mine and integrate the descriptive and comparative information. In Section 4, we design a unified digraph structure for product comparisons by integrating heterogeneous information and provide the eWOM ranking of multiple products. Section 5 describes the data used for estimating the model, evaluates the proposed ranking method, and discusses a ranking system for decision support. In Section 6, we present our study's conclusions as well as future work.

## 2. Related works

## 2.1. Descriptive information: Numeric rating vs. text sentiments

Several researchers have examined the effect of online reviews on potential consumers' decisions, primarily concentrating on numeric ratings and text sentiments. The numeral rating, which can be considered a succinct summary of opinion and codified assessment on a standardized scale (i.e., the number of stars), is characterized by its simplicity, and it is convenient for potential customers to grasp a general impression. Some researchers have shown that consumers faced with complexity and abundance of information in a limited time often attempt to reduce their cognitive efforts and resort to alternative simplified strategies and heuristics to arrive at a purchasing decision [3,41,47]. Numeric rating, as a type of evaluation information on products that requires less effort to process and is easily aligned, may frequently be used to simplify the considerable set of alternatives [24]. An investigation found that 20% of consumers will rank products based on a numeric rating when searching for product information on an e-ecommerce website [13]. Many studies have found that numeric ratings affect consumer decision-making to a certain extent [6,7,8,12,20,36]. However, the average numeric star rating assigned to a product may not be able to reveal much information about its true underlying quality [16]. Instead, the reader must read actual text reviews to examine more detailed and specific evaluation of products.

Different from numeric ratings, text reviews that are full of objective and subjective descriptions of products can provide more explanations of reviewers' feelings, experiences, and emotions. Text sentiments, which are derived from text reviews by text mining techniques, can be assigned specific polarity such as positive, neutral, or negative emotions with varying degrees. Such sentiments provide rich information to their readers and are likely to provide them with an understanding that goes beyond the scope of a numeric rating. Some studies have revealed that text sentiments containing speci c opinions on products have important effects on consumers' decision-making [1,14,24,36,38]. However, on the other side of the coin, the huge amount of text content, which is also mixed with much noise [18] and complex patterns, is extremely tedious and costly to read [6] [36].

Numeric ratings and text sentiments as online eWOM both affect consumers' evaluation of candidate products, and the two distinct types of information can complement one another. The rating scores are allowed to be only, for example, an integer from 1 to 5, which may not provide enough information to assist the decision-makers. Due to the rich information provided in the text, it is able to alleviate the discreteness problem of numeric ratings. For example, some reviews with a score of 4 read like reviews with a score of 3, whereas others read like reviews with a score of 5. Furthermore, it has been shown that ratings and sentiments may have different proximities to the nal choice [24]. It is noteworthy that the text review, rather than numeric rating, has attracted most of the attention in the existing research on product comparisons; the numeric rating is even completely excluded in some studies. In fact, because it requires less effort to read and align [53], the numeric rating should not be ignored. In our study, we also find that, by integrating the information from both text sentiment and numeric rating, the performance of product ranking can be better than that by merely considering text sentiment. Therefore, numeric rating and text sentiments are two different types of evaluation of products. To reduce bias and strengthen robustness, these two factors should be integrated to evaluate products' eWOM simultaneously.

The numeric rating and text sentiment are considered descriptive information in this paper because each describes some nature, feeling, or assessment of one single entity (product). The proposal of naming such content descriptive information is to distinguish it from comparative information, which focuses on comparing more than one product.

## 2.2. Comparative information: Comparative sentences vs. comparative votes

In contrast to evaluating a product in isolation, one of the most convincing ways to directly compare its relative superiority or weakness is against that of similar one [28,22]. The comparison is useful for potential customers to make better purchasing decisions, and informative for manufacturers to identify competitors and mine competitive intelligence to discover potential risks [49].

Generally, customers or manufacturers can compare products by reading the comparative sentences that are implicitly embedded in the huge number of text reviews. A comparative sentence is extracted from a text review to express a comparative opinion between two or more entities (products). For example, a comparative sentence may be similar to “Mobile phone X is much better than Mobile Y”. Jindal and Liu [28,29] employed a text mining method based on rules and a Naïve Bayes classifier to identify comparative sentences in text and applied label sequential rules to further extract comparative relationships. Xu et al. [49] proposed a graphical model to extract and visualize comparative relationships between products from consumer reviews to help users acquire more competitive intelligence.

Although we can acquire comparative relationships between products based on comparative sentences, the number of comparative sentence in consumer reviews is very small and the number of product entities that appear in comparative text is limited. We summarize some related studies in Table 1; it shows that the percentage of comparative sentences in reviews is very low. Usually, fewer than 10% of the sentences in the review contain comparative opinions [28,29], and some studies indicate that the percentage is even less than 2% [51]. The data collected in our research show that it is only 1.32%. Many (if not most) of the products are not compared with any other products; moreover, even when there are a few comparisons between a certain pair of products, the rare comparisons may increase risk of bias or fake reviews. Thus, the limited number of available comparative sentences greatly restricts their applicability to providing sufficient assistance to either consumers or manufacturers.

Fortunately, a new form of data can solve the above problem. With the rapid development of Chinese e-business and Web 2.0, various websites provide huge numbers of consumer reviews, for example on retailers' websites (e.g., Jd.com<sup>2</sup> and Taobao.com<sup>3</sup> et al.), third-party review websites (e.g., Zol.com.cn and Pconline.com.cn<sup>4</sup> et al.), online communities, and blogs. In particular, some third-party review sites can provide online comparative votes for products. Taking Zol.com.cn as an example as shown in Fig. 1, consumers can compare two products and vote for the product they prefer. Unlike writing comments, which is time consuming, it is much more convenient and simple to click a button to vote for favorite products. Therefore, in contrast to comparative sentences, comparative votes are more easily implemented and more comprehensive for establishing comparative relationships for many products. Thus, online comparative votes can iron out the drawback of comparative sentences because the number of comparative votes is much larger and they cover almost all of the online products and most pairs of products.

Table 1  
Number of comparative sentences statistical table.

<table><tr><td>Studies</td><td>Sample data</td><td>Comparative sentences</td><td>Percentage</td></tr><tr><td>Jindal and Liu [28]</td><td>3165</td><td>308</td><td>9.73%</td></tr><tr><td>Jindal and Liu [29]</td><td>3248</td><td>279</td><td>8.59%</td></tr><tr><td>Zhang et al. [51]</td><td>1,930,550</td><td>36,522</td><td>1.89%</td></tr><tr><td>Our studies</td><td>23,488</td><td>310</td><td>1.32%</td></tr><tr><td>Average</td><td>490,112.75</td><td>9354.75</td><td>5.38%</td></tr></table>

Comparative sentences and votes are considered comparative information in this paper, from which comparative relationships between products can be inferred. Descriptive information evaluates an object in isolation, making it difficult to reflect relative utility. Consequently, comparative information can better reflect consumers' preferences for alternative products, and they are expected to be more effective in evaluating products.

## 2.3. Integration of descriptive information and comparative information

The advantage of descriptive information is that it contains detailed objective and subjective descriptions of products; however, the disadvantage is that the products are described in isolation. The advantage of comparative information is that it provides a comparison of products' relative superiority or weakness, but the disadvantage is that the abstract comparison may lack sufficient concrete and emotional words as references to touch people's feelings. Thus, it is natural to combine both descriptive and comparative information to provide a better evaluation of products. The problem is how to combine heterogeneous information because descriptive information is one-dimensional and comparative information is two-dimensional. Another problem is how to evaluate multiple (e.g., dozens or hundreds of) products simultaneously because the above information usually provides only an evaluation of either a single product or a pair of products.

The recently proposed graph structure can be applied to solve the aforementioned two problems. Zhang et al. proposed a method to rank multiple products based on text of consumer reviews by combining text sentiments and comparative sentences through a graph to find top-ranked products [51,52]. Li et al. developed a unified graph model to rank multiple products after mining comparative relationships between products from both review websites and community-based question–answer pairs [32]. By combining comparative sentences with network analysis, Zhang et al. also proposed a product comparison network for products ranking [54].

Although the above graph-based methods have shown promising results, they should be enhanced further to address the following two aspects.

(1) Due to the shortage of comparative sentences, they cannot establish sufficient comparative relationships for the majority of products and cannot establish a global comparison or obtain reliable rankings of multiple products.

(2) Both numeric rating and text reviews have important effects on consumers' evaluations and decisions; the existing graph-based methods all ignore the numeric rating without incorporating the advantages of the two types of descriptive information.

Table 2  
![](images/9ea04dbbc3f56c4e7b3b294f58cb29df5120dd283373c6560b5b14f5aa0285eb.jpg)  
Fig. 1. Example of comparative votes for mobile phones (Zol.com.cn).

Product comparison methods based on information integration.

<table><tr><td rowspan="2">Studies</td><td rowspan="2">Rating</td><td colspan="2">Text</td><td rowspan="2">Votes</td><td rowspan="2">eWOM comparison</td><td rowspan="2">Results evaluation</td></tr><tr><td>Text sentiments</td><td>Comparative sentence</td></tr><tr><td>Liu et al. [34]</td><td></td><td>√</td><td></td><td></td><td>A pair of products</td><td></td></tr><tr><td>Hu and Liu [23]</td><td></td><td>√</td><td></td><td></td><td>A pair of products</td><td></td></tr><tr><td>Tian et al. [46]</td><td></td><td>√</td><td></td><td></td><td>Multiple products</td><td></td></tr><tr><td>Zhang et al. [50]</td><td></td><td>√</td><td></td><td></td><td>Multiple products</td><td>Sales rank</td></tr><tr><td>Jindal and Liu [28]</td><td></td><td></td><td>√</td><td></td><td>A pair of products</td><td></td></tr><tr><td>Jindal and Liu [29]</td><td></td><td></td><td>√</td><td></td><td>A pair of products</td><td></td></tr><tr><td>Xu et al. [49]</td><td></td><td></td><td>√</td><td></td><td>A pair of products</td><td></td></tr><tr><td>Zhang et al. [54]</td><td></td><td></td><td>√</td><td></td><td>Multiple products</td><td>Sales rank</td></tr><tr><td>Zhang et al. [51]</td><td></td><td>√</td><td>√</td><td></td><td>Multiple products</td><td>Sales rank</td></tr><tr><td>Zhang et al. [52]</td><td></td><td>√</td><td>√</td><td></td><td>Multiple products</td><td></td></tr><tr><td>Li et al. [32]</td><td></td><td>√</td><td>√</td><td></td><td>Multiple products</td><td>Subjective</td></tr><tr><td>Kong et al. [30]</td><td></td><td>√</td><td>√</td><td></td><td>Multiple products</td><td>Subjective</td></tr><tr><td>Our research</td><td>√</td><td>√</td><td>√</td><td>√</td><td>Multiple products</td><td>Sales rank</td></tr></table>

## 3. Integration of heterogeneous information

## 3.1. The concept

To make full use of reviews to generate rankings of eWOM for multiple products, a novel method is proposed to integrate the rich and heterogeneous information, including numeric rating, sentiment from reviews, comparative sentences, and votes. The flowchart is shown in Fig. 2. First, a crawler is implemented to collect products data from Zol.com.cn. The dataset we acquired is from the mobile phone category and comprises three types of consumer reviews: numeric rating, text reviews, and comparative online votes. By mining text reviews, the sentiment of reviews and comparative sentences can be obtained. Consequently, the two types of information can be derived, i.e., descriptive information including numeric rating or sentiment of reviews and comparative information including comparative sentences and votes.

To consider descriptive information and comparative information simultaneously, a graph structure is applied in which the nodes are the given prod ucts, the weights of nodes are derived from descriptive information, and the edges represent pairwise comparative relationships. A benefit from the graph structure is that we can calculate the integrated eWOM score and generate an overall ranking of the given set of products.

## 3.2. Mining of descriptive information

## 3.2.1. Descriptive information from text reviews

The sentiment embedded in the text content can be classified as positive or negative, which is widely studied by sentiment analysis [4,9,31,35,43]. For mining Chinese text, HowNet<sup>5</sup> HowNet (http://www.keenage.com) was released on October 22, 2007. provides fundamental sentiment datasets consisting of a list of sentiment-labeled words and phrases from which two seed word lists can be derived, including 4566 positive words and 4370 negative words. By incorporating the two lists of seed words into a user-de ned dictionary, we rst utilize computer-based words tagger tool (ICTCLAS<sup>6</sup> ICTCLAS (http://ictclas.nlpir.org/); the beta version was released in 2014.) to label the polarities of sentiment terms in text reviews of each product. Then, the total number of positive or negative terms is counted to obtain the sentiment score of the text review. The positive and negative terms are assigned explicit polarity values 1 and −1, respectively. For example, given a product i at time t (denoted as $P _ { i t } )$ and a text review about $P _ { i t }$ (denoted as $T R _ { i t } )$ , the text review is labeled with a set of sentiment terms, i.e., $T R _ { i t } = \{ t r _ { i t 1 } , t r _ { i t 2 } , . . . , t r _ { i t n } \}$ . The overall sentiment score of $P _ { i t } ,$ denoted as $T \_ S c o r e ( P _ { i t } )$ , can be computed as follows:

![](images/e0ef76f8647b793f04ea778e0261dde21ec304c93374e068b0adea16adab2506.jpg)  
Fig. 2. Flowchart of integrating heterogeneous information for products eWOM ranking.

$$
T \_ S c o r e (P _ {i t}) = \frac {P O _ {i t} (T R _ {i t}) - N O _ {i t} (T R _ {i t})}{P O _ {i t} (T R _ {i t}) + N O _ {i t} (T R _ {i t})}\tag{1}
$$

where the prefix T of T $S c o r e ( P _ { i t } )$ indicates that the score is calculated from a text review, $P O _ { i t }$ is the number of occurrences of positive terms in all text reviews for $P _ { i t } ,$ and $N O _ { i t }$ is the number of negative terms.

To validate the method, we randomly selected a set of 500 product reviews from the collected review datasets, and three human annotators were employed to carefully analyze the text sentiment. The annotators were asked to manually annotate and classify the polarities of sentiment terms as positive terms or negative terms. The final annotating results needed to reach agreement among at least two persons. In summary, the dataset consisted of 448 positive terms and 267 negative terms that were manually annotated. We used the labeled results from human annotators as the baseline to evaluate the performance of the sentiment classifying technique. The precision and recall values of the technique were 81.83% and 88.81%, respectively.

We also tested whether the text sentiment score we estimated was accurate and reflected the overall sentiments expressed in the text review. We had the three annotators read the sample of 500 reviews and assign a score on a scale of 1–5 based on their assessment of how positive or negative the review was. The coefficient of the Pearson correlation between the three annotators' average scores and the text sentiment score derived by our method was 0.707.

## 3.2.2. Descriptive information from numeric rating

In addition to the implicit scores in text content, another form of score is readily available, i.e., the ratings in numeric values following each piece of text review. For product i at time t with a set of numeric ratings, denoted as $N R _ { i t } = \{ n r _ { i t 1 } , n r _ { i t 2 } , . . . , n r _ { i t m } \}$ , the average score rating for $P _ { i t } ,$ denoted as $R \_ S c o r e ( P _ { i t } )$ , is calculated by:

$$
R \_ S c o r e (P _ {i t}) = \frac {\sum_ {j = 1} ^ {m} r a t e (n r _ {i t j})}{m}\tag{2}
$$

where prefix R of $R \_ S c o r e ( P _ { i t } )$ means that the score is obtained from a rating value, and rate $\mathbf { \bar { \rho } } _ { n r _ { i t j } } ) \in \{ r _ { m i n } , . . . , r _ { m a x } \}$ is a discrete rating value within the range of $r _ { m i n }$ and $r _ { m a x } .$ . The numeric ratings are usually on a 1–5 star scale on most review websites, i.e., $r _ { m i n } = 1$ and $r _ { m a x } = 5$ , wherein a 1-star rating shows the least satisfaction, and a 5-star rating indicates the most satisfaction

The T\_Score from text review, with a rage of [−1, 1], will be integrated with the R\_Score from numeric rating; however, a problem is that they do not share the same scale. To facilitate the integration, T\_Score is scaled up to the range of 1–5, which is also adopted in other studies [24]. For example, if the originally obtained T\_Score value i $: x = - 0 . 5$ , the value transformed into [1,5] is calculated by $f ( x ) = 2 x + 3 = 2$ . For the product without reviews, the sentiment score is set to be a neutral score of 3 by default. The $f ( x )$ function is designed from min-max normalization

$$
f (x) = \frac {x - m i n}{m a x - m i n} (n e w _ {-} m a x - n e w _ {-} m i n) + n e w _ {-} m i n\tag{3}
$$

where min and max are the original minimum and maximum values of an attribute x. Min–max normalization maps a value by $f ( x )$ into the new range [new\_min, new\_max]. When we want to restrict value within [1,5], the equation could be rewritten as the function we have applied. In addition to min–max normalization, there are other methods for data normalization, such as: z-score normalization and normalization by decimal scaling [21]. However, certain normalization schemes can change the original data quite a bit, particularly the z-score normalization and normalization by decimal scaling. The min–max normalization is the preferred method that preserves the relationship among the raw data values [21].

The overall score of $P _ { i t } ,$ denoted as $S c o r e ( P _ { i t } )$ , is calculated by combining $T _ { - } S c o r e ( P _ { i t } )$ and $R \_ S c o r e ( P _ { i t } ) { : }$

$$
S c o r e (P _ {i t}) = \alpha T \_ S c o r e (P _ {i t}) + (1 - \alpha) R \_ S c o r e (P _ {i t})\tag{4}
$$

where $\alpha \in ( 0 , 1 )$ is an adjustment factor to balance the effects of T\_Score and R\_Score.

## 3.3. Mining of comparative information

## 3.3.1. Comparative information from text reviews

Comparative information can be expressed as comparative sentences extracted from text reviews, which are identified via comparative keyword, sentence semantics, and sentence structure [25, 44], as well as fuzzy linguistics [33]. In our research, comparative keywords,<sup>7</sup> labeled in a keyword list, are scanned in the text reviews to tag comparative sentences. Given a set of sentences comparing two products $P _ { i }$ and $P _ { j } ,$ denoted as ${ \cal S } = \{ s _ { 1 } , s _ { 2 } ,$ $\ldots s _ { h } \} ,$ the information of a comparative relationship derived from one text sentence $s _ { k } \in S$ is described as a quadruple:

$$
T \_ R e l a t i o n _ {i j} (s _ {k}) = (P _ {i}, P _ {j}, V o t e ^ {T} _ {k} (P _ {i} | P _ {i}, P _ {j}), V o t e ^ {T} _ {k} (P _ {j} | P _ {i}, P _ {j})),
$$

where the prefix T indicates that the information is obtained from text. $V o t e _ { \ k } ^ { T } ( P _ { i } | P _ { i } , P _ { j } )$ equals 1 if the product $P _ { i }$ is commented on as better than $P _ { j }$ in sentence $s _ { k } ;$ otherwise, it is 0. For example, if there is a comparative sentence $s _ { k } = \cdot$ “mobile phone A is less than mobile phone $B , "$ the corresponding quadruple T\_Relatio $\iota _ { i j } ( s _ { k } )$ can be written as $( \mathsf { A } , \mathsf { B } , 0 , 1 )$ . When considering all the comparative sentences, the overall $V o t e ^ { T } ( P _ { i } | P _ { i } , P _ { j } )$ , which denotes the total number of sentences in S preferring P to P is computed as follows:

$$
\operatorname{Vote} ^ {T} \left(P _ {i} \mid P _ {i}, P _ {j}\right) = \sum_ {k = 1} ^ {h} \operatorname{Vote} _ {k} ^ {T} \left(P _ {i} \mid P _ {i}, P _ {j}\right)\tag{5}
$$

The annotators were also invited to extract comparative sentences in the selected product reviews. In total, 10 comparative sentences were manually annotated and were used to evaluate the performance of comparative sentences tagging method. The precision and recall were 72.73% and 80% respectively.

## 3.3.2. Comparative information from online votes

The comparative votes can supply direct comparative relationships, also denoted as a quadruple:

$$
V \_ R e l a t i o n _ {i j} = (P _ {i}, P _ {j}, V o t e ^ {V} (P _ {i} | P _ {i}, P _ {j}), V o t e ^ {V} (P _ {j} | P _ {i}, P _ {j})),
$$

where the prefix V means that the information is derived from votes, and $V o t e ^ { V } ( P _ { i } | P _ { i } , P _ { j } )$ is the number of votes preferring $P _ { i }$ to $P _ { j }$ when comparing both of them.

Roughly speaking, T\_Relation focuses more on local comparisons because the limited descriptive words usually concentrate on a few product with some detailed feelings or judgements. V\_Relation can provide global information because the comparison is made among a large number of candidate products. The limitation of T\_Relation is partially caused by the fact that writing comments is very time consuming. In contrast, it is much more convenient and simple to click a button to vote for the favorite products.

The two sorts of comparative information, T\_Relation and V\_Relation, can be combined to provide a more comprehensive description of the rela tionships between different products. The combined relationship is denoted as follows:

Relati $\begin{array} { r } { n _ { i j } = ( P _ { i } , P _ { j } , V o t e ( P _ { i } | P _ { i } , P _ { j } ) , V o t e ( P _ { j } | P _ { i } , P _ { j } ) ) } \end{array}$ ,

where $V o t e ( P _ { i } | P _ { i } , P _ { j } )$ is the full-scale information measuring the preference for $P _ { i }$ to $P _ { j } ,$ calculated by

$$
V o t e (P _ {i} | P _ {i}, P _ {j}) = \left\{ \begin{array}{l l} \frac {V o t e ^ {T} (P _ {i} | P _ {i} , P _ {j}) + V o t e ^ {V} (P _ {i} | P _ {i} , P _ {j})}{V o t e ^ {T} (P _ {i} | P _ {i} , P _ {j}) + V o t e ^ {V} (P _ {i} | P _ {i} , P _ {j}) + V o t e ^ {T} (P _ {j} | P _ {i} , P _ {j}) + V o t e ^ {V} (P _ {j} | P _ {i} , P _ {j})}, & i \neq j, V o t e ^ {T} (P _ {i} | P _ {i}, P _ {j}) \neq 0 \\ \text { or } V o t e ^ {V} (P _ {i} | P _ {i}, P _ {j}) \neq 0 \text { or } V o t e ^ {T} (P _ {j} | P _ {i}, P _ {j}) \neq 0 \text { or } V o t e ^ {V} (P _ {j} | P _ {i}, P _ {j}) \neq 0 \\ \frac {1}{2}, & i \neq j, V o t e ^ {T} (P _ {i} | P _ {i}, P _ {j}) = 0, V o t e ^ {V} (P _ {i} | P _ {i}, P _ {j}) = 0, V o t e ^ {T} (P _ {j} | P _ {i}, P _ {j}), V o t e ^ {V} (P _ {j} | P _ {i}, P _ {j}) = 0 \\ 0 & i = j \end{array} \right.\tag{6}
$$

For paired products without any comparative sentence and online vote, we set one vote to each product to avoid the denominator being 0.

Table 3  
Rating scores and vote numbers for the five products.

<table><tr><td> $P_i$ </td><td> $P_1$ </td><td> $P_2$ </td><td> $P_3$ </td><td> $P_4$ </td><td> $P_5$ </td></tr><tr><td> $T\_Score(P_i)$ </td><td>3.6</td><td>2.8</td><td>3.4</td><td>3.8</td><td>3.7</td></tr><tr><td> $R\_Score(P_i)$ </td><td>3.4</td><td>3.2</td><td>3.6</td><td>4.4</td><td>3.3</td></tr><tr><td> $Vote^T(P_1|P_1,P_i)$ </td><td>0</td><td>6</td><td>6</td><td>8</td><td>3</td></tr><tr><td> $Vote^T(P_2|P_2,P_i)$ </td><td>4</td><td>0</td><td>5</td><td>1</td><td>5</td></tr><tr><td> $Vote^T(P_3|P_3,P_i)$ </td><td>2</td><td>7</td><td>0</td><td>9</td><td>5</td></tr><tr><td> $Vote^T(P_4|P_4,P_i)$ </td><td>6</td><td>1</td><td>6</td><td>0</td><td>2</td></tr><tr><td> $Vote^T(P_5|P_5,P_i)$ </td><td>7</td><td>3</td><td>10</td><td>4</td><td>0</td></tr><tr><td> $Vote^V(P_1|P_1,P_i)$ </td><td>0</td><td>5</td><td>1</td><td>2</td><td>1</td></tr><tr><td> $Vote^V(P_2|P_2,P_i)$ </td><td>2</td><td>0</td><td>3</td><td>0</td><td>1</td></tr><tr><td> $Vote^V(P_3|P_3,P_i)$ </td><td>3</td><td>4</td><td>0</td><td>4</td><td>2</td></tr><tr><td> $Vote^V(P_3|P_3,P_i)$ </td><td>2</td><td>2</td><td>3</td><td>0</td><td>1</td></tr><tr><td> $Vote^V(P_4|P_4,P_i)$ </td><td>2</td><td>4</td><td>2</td><td>1</td><td>0</td></tr></table>

## 4. Integrate heterogeneous information based on graph structure

## 4.1. Directed and weighted digraph structure

In this section, both descriptive information and comparative information are integrated by a directed and weighted graph structure.

The graph structure is formally defined as a quadruple, $G = ( V , E , W ^ { V }$ $W ^ { E } )$ , where V is the set of vertices or nodes, E is the set of directed edges (i.e., the ordered pairs of vertices), $W ^ { V }$ is the weight associated with each node, and $W ^ { E }$ is the weight labeled on each directed edge. The weight for node $P _ { i }$ is normalized from Score(P ):

$$
W ^ {V} (P _ {i}) = \frac {\operatorname{Score} (P _ {i})}{\sum_ {k = 1} ^ {n} \operatorname{Score} (P _ {k})}\tag{7}
$$

and the weight on a directed edge from $P _ { j }$ to $P _ { i }$ is normalized from $V o t e ( P _ { i } | P _ { i } , P _ { j } )$ :

$$
W ^ {E} \left(P _ {i} \mid P _ {i}, P _ {j}\right) = \frac {\operatorname{Vote} \left(P _ {i} \mid P _ {i} , P _ {j}\right)}{\sum_ {l = 1} ^ {n} \operatorname{Vote} \left(P _ {l} \mid P _ {l} , P _ {j}\right)}\tag{8}
$$

where n is the total number of candidate products under comparison and $P _ { l }$ is the product that has comparative relationship with product $P _ { j } .$

The following is a simple example to illustrate how to build the weighted digraph structure. Suppose there are five products $( P _ { 1 } , P _ { 2 } , P _ { 3 } ,$ $P _ { 4 } , P _ { 5 } )$ to be ranked, and the rating scores and vote numbers are shown in Table 3. According to Eq. 4 and Eq. 6, we can compute the integrated scores and votes in Table 4. Then, a weighted digraph across five products can be obtained in which the weight of nodes and directed edges can be calculated using Eq. 7 and Eq. 8. For example, the weight of node $P _ { 1 } \mathrm { i } s W ^ { V } ( P _ { 1 } ) = 3 . 5 / ( 3 . { \bar { 5 } } + 3 . 0 + 3 . 5 + 4 . 1 + 3 . 5 ) = 0 . 1 9 9 ,$ and the weight of edge from P to P is $W ^ { E } ( P _ { 1 } | P _ { 1 } , P _ { 2 } ) = 0 . 6 4 7 /$ $( 0 . 6 4 7 + 0 . 5 7 9 + 0 . 7 5 0 + 0 . 5 3 8 ) = 0 . 2 5 7$ . Based on the calculated weights, the weighted digraph can be derived as shown in Fig. 3.

## 4.2. Overall eWOM score calculation

Benefiting from the structure of the weighted digraph, we develop a scalar overall eWOM score with which to rank products. The overall eWOM of each product consists of two elements: inherent eWOM derived from its overall score of the product, and extrinsic eWOM accumulated from its comparative relationships with other products.

Product scores and votes for the five products $( \alpha = 0 . 5 ) .$

<table><tr><td> $P_i$ </td><td> $P_1$ </td><td> $P_2$ </td><td> $P_3$ </td><td> $P_4$ </td><td> $P_5$ </td></tr><tr><td> $Score(P_i)$ </td><td>3.5</td><td>3.0</td><td>3.5</td><td>4.1</td><td>3.5</td></tr><tr><td> $Vote(P_1|P_1,P_i)$ </td><td>0</td><td>0.647</td><td>0.583</td><td>0.556</td><td>0.308</td></tr><tr><td> $Vote(P_2|P_2,P_i)$ </td><td>0.353</td><td>0</td><td>0.421</td><td>0.250</td><td>0.462</td></tr><tr><td> $Vote(P_3|P_3,P_i)$ </td><td>0.417</td><td>0.579</td><td>0</td><td>0.591</td><td>0.368</td></tr><tr><td> $Vote(P_4|P_4,P_i)$ </td><td>0.444</td><td>0.750</td><td>0.409</td><td>0</td><td>0.375</td></tr><tr><td> $Vote(P_5|P_5,P_i)$ </td><td>0.692</td><td>0.538</td><td>0.632</td><td>0.625</td><td>0</td></tr></table>

![](images/81823b6900f763fa37076875b9f9d6ecbda64c74ab46ed345eec620f4b3b4b6d.jpg)  
Fig. 3. Example of weighted digraph for five products.

Roughly speaking, whether a product $P _ { i }$ should be ranked high is affected by three conditions:

(1) If a product has a high score from descriptive information (i.e. $S c o r e ( P _ { i } )$ is high), it should be ranked high.

(2) If a product P<sub>i</sub> has many votes from other products, $P _ { i }$ should be ranked high.

(3) If a product $P _ { i }$ has more votes than P<sub>j</sub> whose ranking is high, P<sub>i</sub> should be ranked even higher.

Based on the above analysis, the overall eWOM score of product $P _ { i } ,$ W\_Score(P ), is calculated by

$$
W \_ S c o r e (P _ {i}) = (1 - \beta) W ^ {V} (P _ {i}) + \beta W \_ S c o r e ^ {C} (P _ {i})\tag{9}
$$

where $\beta \in ( 0 , 1 )$ is an adjustment factor to balance the effects of $W ^ { V } ( P _ { i } )$ and $W \_ S c o r e ^ { C } ( P _ { i } )$ , and W\_Score<sup>C</sup>(P<sub>i</sub>) is calculated by:

$$
W \_ S c o r e ^ {C} (P _ {i}) = \sum_ {j = 1} ^ {n} W \_ S c o r e (P _ {j}) W ^ {E} (P _ {i} | P _ {i}, P _ {j})\tag{10}
$$

$W ^ { V } ( P _ { i } )$ measures the inherent eWOM, whereas $W _ { - } S c o r e ^ { C } ( P _ { i } )$ denotes the extrinsic eWOM. By incorporating Eq. 10 into Eq. 9, the overall eWOM score W\_Score(P ) can be derived:

$$
W \_ S c o r e (P _ {i}) = (1 - \beta) W ^ {V} (P _ {i}) + \beta \sum_ {j = 1} ^ {n} W \_ S c o r e (P _ {j}) W ^ {E} (P _ {i} | P _ {i}, P _ {j})\tag{11}
$$

## 4.3. Ranking generation

Ranking generation is a calculation of the eigenvector of the matrix to compute $W { \_ } S c o r e ( P _ { i } )$ value using Eq. 11. The equation can be expressed as the following matrix function:

$$
W \_ S c o r e = (1 - \beta) * W ^ {V} + \beta * A * W \_ S c o r e\tag{12}
$$

<table><tr><td>Algorithm Products Ranking ( $W^{V}$ ,  $A$ ,  $\beta$ )</td></tr><tr><td>1  $W\_Score_{0} \leftarrow W^{V}$ ;</td></tr><tr><td>2  $k \leftarrow 1$ ;</td></tr><tr><td>3 repeat;</td></tr><tr><td>4  $W\_Score_{k} \leftarrow \beta * W^{V} + (1-\beta) * A * W\_Score_{k-1}$ ;</td></tr><tr><td>5  $k \leftarrow k+1$ ;</td></tr><tr><td>6 until  $\| W\_Score_{k} - W\_Score_{k+1} \| < \varepsilon$ ;</td></tr><tr><td>7 Ranking list = Sort( $W\_Score_{k}$ );</td></tr><tr><td>8 return P_List;</td></tr></table>

## Fig. 4. Pseudo-code of the ranking algorithm.

where W\_Score = [W\_Score $\left( P _ { 1 } \right)$ , W\_Score $( P _ { 2 } ) , . . . , W _ { . }$ \_Score $\left( P _ { \mathrm { n } } \right)$ ]<sup>T</sup>, $W ^ { V } = [ W ^ { V } ( P _ { 1 } ) , W ^ { V } ( \bar { P } _ { 2 } ) , . . . , W ^ { V } ( P _ { i } ) ] ^ { \mathrm { T } }$ , and A is a n × n comparison relationship adjacent matrix:

$$
\boldsymbol {A} = \left( \begin{array}{c c c c} 0 & W ^ {E} (P _ {1} | P _ {1}, P _ {2}) & \dots & W ^ {E} (P _ {1} | P _ {1}, P _ {n}) \\ W ^ {E} (P _ {2} | P _ {2}, P _ {1}) & 0 & \dots & W ^ {E} (P _ {2} | P _ {2}, P _ {n}) \\ \vdots & \vdots & & \vdots \\ W ^ {E} (P _ {n} | P _ {n}, P _ {1}) & W ^ {E} (P _ {n} | P _ {n}, P _ {2}) & \dots & 0 \end{array} \right).
$$

Lemma 1. Suppose $\sum _ { i = 1 } ^ { n } W S c o r e ( \mathrm { P } _ { i } ) = 1$ . Then, Eq. 12 can be expressed by $W \_ S c o r e = B ^ { * } W \_ S c o r e ,$ and $\pmb { { \cal B } } = ( 1 - \beta ) ^ { * } { \cal W } ^ { V * } e ^ { \mathrm { T } } + \beta ^ { * } \pmb { A } .$

According to the Ergodic theorem of Markov chains [19], we can obtain following result:

Proposition 1. Matrix $\pmb { B } ^ { T }$ is an irreducible,<sup>8</sup> aperiodic,<sup>9</sup> and stochastic<sup>10</sup> transition matrix. W\_Score will converge to a stationary probability distribution π. Formally, lim W Sco $e _ { k } = \pi .$

All the proofs are provided in Appendix A.

Consequently, the overall eWOM score for products can be computed by iterative algorithm. Then, the product ranking can be produced accordingly. The pseudo-code of the ranking process is shown in Fig. 4.

## 5. Experiments

## 5.1. Collected datasets

In general, there are two types of products, namely, vertically differentiated products and horizontally differentiated products [2,15]. Vertically differentiated products can be ordered according to their objective quality from highest to lowest, and it is possible to say that one is “better” than another is. Electronics such as mobile phones and digital cameras are good examples. However, horizontally ordering differentiated products objectively is difficult, for instance books and foods, in which the matching between consumer taste and product feature is the major reason for evaluations and purchasing decisions. In this paper, we first select mobile phones as the object of our study. The mobile phone is a vertically differentiated product, and its sales volume is the highest in the electronics consumer market. Moreover, the mobile phone includes a variety of items, and market competition is fierce. We collected data from Zol.com.cn, a third-party electronics consumer reviews website in China. There are several reasons to choose Zol.com. cn. First, it is one of largest third-party consumer reviews websites in China. Third-party review websites usually enjoy better reputation and recognition as product information sources for consumers than retailer-hosted reviews websites do [20,45]. They are more specialized and offer more insightful information than online retailers do, who sell products in thousands of categories. Some studies show that third-party consumer reviews websites also have greater influence on sales of electronics than do retailer-hosted reviews websites [20]. Second, it is a very popular online reviews website for users evaluating and comparing electronics, with 40 million + registered users and 150 million + daily visits.<sup>11</sup> Furthermore, it contains the largest number of consumer reviews for various mobile phones, and provides a new type of comparative information, online comparative votes, on nearly every pair of comparative products. Due to the rich information provided by Zol.com.cn, it is used by many academic research [11,41].

Table 5  
Statistics of the collected data.

<table><tr><td></td><td>Number</td><td>Range</td><td>Statistic</td></tr><tr><td>Consumer reviews</td><td>23,488</td><td></td><td></td></tr><tr><td>Positive terms</td><td>20,659</td><td></td><td></td></tr><tr><td>Negative terms</td><td>14,805</td><td></td><td></td></tr><tr><td>Comparative sentences</td><td>310</td><td></td><td></td></tr><tr><td>Comparative Votes</td><td>139,641</td><td></td><td></td></tr><tr><td>R_Score</td><td>96</td><td>[2.100,4.800]</td><td>3.748 ± 0.436</td></tr><tr><td>T_Score</td><td>96</td><td>[1.190,4.200]</td><td>3.249 ± 0.432</td></tr></table>

During a 10-day period<sup>12</sup> (May 2014), we selected 96 unique mobile phones and collected product IDs, number of reviews, numeric ratings, entire text reviews, and comparative votes from Zol.com.cn websites.

First, we extracted sentiment and comparative sentences from text reviews. Then, we computed the R\_Score and T\_Score by numeric rating and text reviews, respectively. The statistics for the data are described in Table 5. The total number of comparative votes is 139,641, which is much greater than the number of comparative sentences (i.e., only 310). We count the numbers of comparative sentences and comparative votes for each of the 96 products in Fig. 5. From the figure, we can see that every product has more than 1000 comparative votes. In contrast, there are only 34 products owning comparative sentences, and the number of them is far less than the number of votes.

In addition, the numbers of comparative sentences and votes for each pair of products are illustrated in Fig. 6. From the figure, there are only 79 pairs of products owning comparative relationships derived by sentences, but the number of sentences about each pair of products is less than 30. In contrast, there are 4556 pairs of products owning comparative relationships resulting from comparative votes, covering almost all pairs of products. Moreover, 1785 pairs of products have more than 30 online votes. Based on the above statistics, it is clear that comparative sentences cannot provide sufficient information to support comparisons among a large number of candidate products. However, the number of comparative votes is considerable, and the rich data provide much more sufficient information for establishing comparative relationships, which will make multiple product comparisons more reliable.

## 5.2. Evaluation and discussion

## 5.2.1. Evaluation of our method

The online eWOM has been recognized widely as an important factor in product sales [5,6,20]. Some studies use sales rank as an indicator of product eWOM ranking [50,54], an approach also adopted in this paper. For each product, the e-commerce websites $J d . c o \dot { m } ^ { 1 3 }$ in China provides sales rank in descending order, in which a rank of 1 represents the bestselling product. We use the correlation between our ranking results and $J d ^ { \prime } s$ sales rank to measure the performance of our ranking method. The Spearman ranking correlation coefficient is defined as the correlation coefficient between the two ranks that is given by:

![](images/696270426761014ac2f4a22824174542f55fcebc546eec2fd5629a7628db22ed.jpg)  
Fig. 5. Number of comparative sentences and votes for each individual product.

$$
\rho \left(\overrightarrow {R _ {x _ {i}}} - \overrightarrow {R _ {y _ {i}}}\right) = 1 - \frac {6 \sum_ {i = 1} ^ {n} \left(R _ {x _ {i}} - R _ {y _ {i}}\right) ^ {2}}{n (n ^ {2} - 1)}\tag{13}
$$

where $\overrightarrow { R _ { x _ { i } } }$ and $\overrightarrow { R _ { y _ { i } } }$ are the rank by our approach and the rank from sales performance, respectively. The correlation coefficient ${ } ^ { \cdot \rho }$ is between −1 and $1 . \rho$ closer to 1 implies a more positive correlation between calculated products rank and Jd's sales rank.

The methods most related to our research include Zhang and Guo's product comparison networks (denoted as Z&G's method for short) [54] and Zhang and Narayanan's product comparison graph model [51. 52] (denoted as Z&N's method for short). Both Z&G's method and Z&N′s method are inspired by PageRank algorithm [40]. Although we share the fundamental graph structure, there are some major differences between our method and the above two methods.

In Z&G's method, they introduced a directed and weighted edge that indicates a comparative relationship between two products, and the weight on each edge was computed from comparative sentences. However, there was no weight for each node in their graph structure [54]. In short, Z&G's method only use comparative sentences, and they ignore the other useful information such as ratings, sentiments or votes. Unfortunately, comparative sentences in consumer reviews are very rare. Among the 96 products we collected, there are only 34 products linked with edges. In other words, there are (a few) comparative sentences for only 34 products, and there is not a single comparative sentence for the other 62 products. As a result, only 34 products could be compared in a ranking; the others will have no ranking.

Z&N′s method was proposed to take both node and edge weights into account when ranking products [51,52], and the method has been applied in some other studies [30,32]. They only used two types of information: text sentiment and comparative sentences, which correspond to the node and edge in the graph structure, respectively.

![](images/6f59c3568e4ce78587f3054e2e54f44221fcadba0567175fb0844346293bd81a.jpg)

However, the definitions of edge, weight of edge and weight of node in Z&N′s graph are different from ours. In their graph structure, if there is a comparative sentence existing in the review for product $P _ { i }$ comparing it with product $P _ { j } ,$ there will be an edge from P to $P _ { j } .$ Then, if the number of positive and negative sentences among all the comparative sentences is $N _ { p c s }$ and $N _ { n c s } ,$ respectively, the weight on the edge is

(a) Number of pariwise products with comparative sentences  
![](images/3e2b1e40633a1d4e703332031f72bdbd90abb60e229b396710b4877e6ce69d79.jpg)  
(b) Number of pairwise products with comparative votes  
Fig. 6. Number of comparative sentences and votes for each pair of products

ρ b 0.05.

Correlations of sales rank and products rank generated by different methods for mobile phones.

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>T&amp;L&#x27;s method</td><td>Z&amp;G&#x27;s method</td><td>Z&amp;N&#x27;s method</td><td colspan="3">Our method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2014-5-9</td><td>0.327***</td><td>0.277**</td><td>0.133</td><td>0.270**</td><td>0.252*</td><td>0.342***</td><td>0.568***</td></tr><tr><td>2014-5-10</td><td>0.327***</td><td>0.289**</td><td>0.133</td><td>0.283**</td><td>0.282**</td><td>0.317**</td><td>0.592***</td></tr><tr><td>2014-5-11</td><td>0.339***</td><td>0.277**</td><td>0.091</td><td>0.269**</td><td>0.273**</td><td>0.285**</td><td>0.578***</td></tr><tr><td>2014-5-12</td><td>0.330***</td><td>0.252*</td><td>0.092</td><td>0.246*</td><td>0.293**</td><td>0.278**</td><td>0.558***</td></tr><tr><td>2014-5-13</td><td>0.324***</td><td>0.260*</td><td>0.093</td><td>0.271**</td><td>0.254*</td><td>0.290**</td><td>0.544***</td></tr><tr><td>2014-5-14</td><td>0.277**</td><td>0.232*</td><td>0.153</td><td>0.222*</td><td>0.270**</td><td>0.332**</td><td>0.542***</td></tr><tr><td>2014-5-15</td><td>0.244*</td><td>0.212*</td><td>0.152</td><td>0.208*</td><td>0.310**</td><td>0.346***</td><td>0.543***</td></tr><tr><td>2014-5-16</td><td>0.235*</td><td>0.211*</td><td>0.152</td><td>0.207*</td><td>0.250*</td><td>0.311**</td><td>0.518***</td></tr><tr><td>2014-5-17</td><td>0.235*</td><td>0.214*</td><td>0.152</td><td>0.210*</td><td>0.304**</td><td>0.273**</td><td>0.575***</td></tr><tr><td>2014-5-18</td><td>0.266**</td><td>0.273**</td><td>0.112</td><td>0.269**</td><td>0.252*</td><td>0.242*</td><td>0.539***</td></tr><tr><td>Average</td><td>0.290 ± 0.043</td><td>0.249 ± 0.030</td><td>0.126 ± 0.027</td><td>0.246 ± 0.030</td><td>0.274 ± 0.023</td><td>0.302 ± 0.034</td><td>0.556 ± 0.022</td></tr></table>

There are 96 products.  
⁎⁎ ρ b 0.01.  
⁎⁎⁎ ρ b 0.001.

Correlations of sales rank and products rank generated within a price range (¥0, ¥1000).

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>T&amp;L&#x27;s method</td><td>Z&amp;G&#x27;s method</td><td>Z&amp;N&#x27;s method</td><td colspan="3">Our method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2014-5-9</td><td>0.440**</td><td>0.365*</td><td>/</td><td>0.355*</td><td>0.368*</td><td>0.415*</td><td>0.501**</td></tr><tr><td>2014-5-10</td><td>0.440**</td><td>0.372*</td><td>/</td><td>0.366*</td><td>0.375*</td><td>0.406*</td><td>0.502**</td></tr><tr><td>2014-5-11</td><td>0.451**</td><td>0.356*</td><td>/</td><td>0.366*</td><td>0.375*</td><td>0.406*</td><td>0.502**</td></tr><tr><td>2014-5-12</td><td>0.434**</td><td>0.303</td><td>/</td><td>0.296</td><td>0.337*</td><td>0.381*</td><td>0.471**</td></tr><tr><td>2014-5-13</td><td>0.430**</td><td>0.317</td><td>/</td><td>0.309</td><td>0.374*</td><td>0.359*</td><td>0.456**</td></tr><tr><td>2014-5-14</td><td>0.241</td><td>0.205</td><td>/</td><td>0.184</td><td>0.333*</td><td>0.495**</td><td>0.461**</td></tr><tr><td>2014-5-15</td><td>0.159</td><td>0.138</td><td>/</td><td>0.132</td><td>0.175</td><td>0.328</td><td>0.487**</td></tr><tr><td>2014-5-16</td><td>0.156</td><td>0.145</td><td>/</td><td>0.137</td><td>0.345*</td><td>0.523***</td><td>0.486**</td></tr><tr><td>2014-5-17</td><td>0.156</td><td>0.138</td><td>/</td><td>0.132</td><td>0.199</td><td>0.294</td><td>0.519***</td></tr><tr><td>2014-5-18</td><td>0.310</td><td>0.253</td><td>/</td><td>0.246</td><td>0.303</td><td>0.395*</td><td>0.556***</td></tr><tr><td>Average</td><td>0.322 ± 0.132</td><td>0.259 ± 0.097</td><td>/</td><td>0.252 ± 0.099</td><td>0.318 ± 0.073</td><td>0.400 ± 0.069</td><td>0.494 ± 0.029</td></tr></table>

There are 35 products within the price range.  
⁎ ρ b 0.05.  
\*\* ρ b 0.01.  
⁎⁎⁎ ρ b 0.001.

assigned as the ratio $N _ { p c s } / N _ { n c s } . \ A s$ for the weight of node, it is the ratio of number of positive $( N _ { p s } )$ and negative sentences $( N _ { n s } ) , \mathrm { i } . \mathrm { e } . , N _ { p s } / N _ { n s }$ [51]. In contrast, we generalize comparative information and descriptive information on an edge and a node, respectively; whether a comparative sentence comes from the review for P or from the review for $P _ { j } ,$ it contributes to comparative information. Such generalization would reduce the potential bias in the review for each specific product and bring the convenience of integrating the comparative votes easily because the comparative votes provided by a third party are associated with both rather than only one of the two comparable products. As for the node, instead of considering a whole sentence directly, the decomposed sentiment terms recognized within a sentence, which can provide more detailed and sensitive opinions, are employed as descriptive information in our research. In addition, the rating scores are integrated to supplement the descriptive information. Furthermore, our proposed digraph structure is fully connected, and we can prove the convergence of eWOM score and compute it by an iteration algorithm.

Correlations of sales rank and products rank generated within a price range [1000, ¥2000).

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>T&amp;L&#x27;s method</td><td>Z&amp;G&#x27;s method</td><td>Z&amp;N&#x27;s method</td><td colspan="3">Our method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2014-5-9</td><td>0.511**</td><td>0.351</td><td>0.025</td><td>0.343</td><td>0.353</td><td>0.570***</td><td>0.844***</td></tr><tr><td>2014-5-10</td><td>0.511**</td><td>0.357*</td><td>0.025</td><td>0.349</td><td>0.365*</td><td>0.572***</td><td>0.848***</td></tr><tr><td>2014-5-11</td><td>0.508**</td><td>0.367*</td><td>0.013</td><td>0.359*</td><td>0.369*</td><td>0.596***</td><td>0.834***</td></tr><tr><td>2014-5-12</td><td>0.513**</td><td>0.326</td><td>0.020</td><td>0.319</td><td>0.371*</td><td>0.594***</td><td>0.835***</td></tr><tr><td>2014-5-13</td><td>0.456**</td><td>0.344</td><td>0.030</td><td>0.336</td><td>0.236</td><td>0.627***</td><td>0.767***</td></tr><tr><td>2014-5-14</td><td>0.394*</td><td>0.390*</td><td>0.031</td><td>0.371*</td><td>0.411*</td><td>0.596***</td><td>0.702***</td></tr><tr><td>2014-5-15</td><td>0.301</td><td>0.355*</td><td>0.031</td><td>0.346</td><td>0.399*</td><td>0.610***</td><td>0.740***</td></tr><tr><td>2014-5-16</td><td>0.301</td><td>0.373*</td><td>0.031</td><td>0.366*</td><td>0.417*</td><td>0.602***</td><td>0.730***</td></tr><tr><td>2014-5-17</td><td>0.301</td><td>0.369*</td><td>0.031</td><td>0.362*</td><td>0.229</td><td>0.671***</td><td>0.740***</td></tr><tr><td>2014-5-18</td><td>0.324</td><td>0.296</td><td>0.031</td><td>0.290</td><td>0.416*</td><td>0.632***</td><td>0.820***</td></tr><tr><td>Average</td><td>0.412 ± 0.098</td><td>0.353 ± 0.026</td><td>0.027 ± 0.006</td><td>0.344 ± 0.024</td><td>0.357 ± 0.069</td><td>0.607 ± 0.030</td><td>0.786 ± 0.056</td></tr></table>

⁎ ρ b 0.05.  
⁎⁎⁎ ρ b 0.001.  
There are 31 products within the price range.

Table 10  
Table 9  
Correlations of sales rank and products rank generated within a price range [¥2000, ¥3000).

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>T&amp;L&#x27;s Method</td><td>Z&amp;G&#x27;s Method</td><td>Z&amp;N&#x27;s Method</td><td colspan="3">Our Method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2014-5-9</td><td>0.406</td><td>0.408</td><td>0.264</td><td>0.465</td><td>0.428</td><td>0.484*</td><td>0.736***</td></tr><tr><td>2014-5-10</td><td>0.395</td><td>0.408</td><td>0.264</td><td>0.465</td><td>0.428</td><td>0.490*</td><td>0.725***</td></tr><tr><td>2014-5-11</td><td>0.445</td><td>0.361</td><td>0.244</td><td>0.412</td><td>0.484*</td><td>0.459</td><td>0.707***</td></tr><tr><td>2014-5-12</td><td>0.443</td><td>0.299</td><td>0.248</td><td>0.406</td><td>0.404</td><td>0.461</td><td>0.728***</td></tr><tr><td>2014-5-13</td><td>0.439</td><td>0.335</td><td>0.219</td><td>0.370</td><td>0.420</td><td>0.447</td><td>0.668**</td></tr><tr><td>2014-5-14</td><td>0.468*</td><td>0.324</td><td>0.259</td><td>0.356</td><td>0.387</td><td>0.418</td><td>0.641**</td></tr><tr><td>2014-5-15</td><td>0.468*</td><td>0.324</td><td>0.259</td><td>0.356</td><td>0.387</td><td>0.418</td><td>0.641**</td></tr><tr><td>2014-5-16</td><td>0.435</td><td>0.324</td><td>0.259</td><td>0.356</td><td>0.387</td><td>0.418</td><td>0.641**</td></tr><tr><td>2014-5-17</td><td>0.435</td><td>0.295</td><td>0.259</td><td>0.323</td><td>0.385</td><td>0.434</td><td>0.647**</td></tr><tr><td>2014-5-18</td><td>0.428</td><td>0.256</td><td>0.465</td><td>0.356</td><td>0.446</td><td>0.451</td><td>0.668**</td></tr><tr><td>Average</td><td>0.436 ± 0.023</td><td>0.333 ± 0.048</td><td>0.274 ± 0.068</td><td>0.387 ± 0.049</td><td>0.416 ± 0.032</td><td>0.448 ± 0.026</td><td>0.680 ± 0.040</td></tr></table>

There are 18 products within the price range.

$$
\rho <   0. 0 5.
$$

\*\* $\mathrm { \rho } < 0 . 0 1 .$

\*\*\* $\mathrm { \rho } < 0 . 0 0 1 .$

Correlations of sales rank and products rank generated with a price not less than ¥3000.

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>T&amp;L&#x27;s Method</td><td>Z&amp;G&#x27;s method</td><td>Z&amp;N&#x27;s method</td><td colspan="3">Our method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2014-5-9</td><td>0.280</td><td>0.313</td><td>/</td><td>0.245</td><td>0.287</td><td>0.552</td><td>0.615*</td></tr><tr><td>2014-5-10</td><td>0.280</td><td>0.391</td><td>/</td><td>0.322</td><td>0.427</td><td>0.629*</td><td>0.622*</td></tr><tr><td>2014-5-11</td><td>0.273</td><td>0.386</td><td>/</td><td>0.420</td><td>0.573</td><td>0.631*</td><td>0.645*</td></tr><tr><td>2014-5-12</td><td>0.231</td><td>0.580*</td><td>/</td><td>0.545</td><td>0.650*</td><td>0.629*</td><td>0.769**</td></tr><tr><td>2014-5-13</td><td>0.266</td><td>0.591*</td><td>/</td><td>0.545</td><td>0.650*</td><td>0.629*</td><td>0.769**</td></tr><tr><td>2014-5-14</td><td>0.252</td><td>0.506</td><td>/</td><td>0.538</td><td>0.622*</td><td>0.643*</td><td>0.762**</td></tr><tr><td>2014-5-15</td><td>0.252</td><td>0.506</td><td>/</td><td>0.538</td><td>0.622*</td><td>0.643*</td><td>0.762**</td></tr><tr><td>2014-5-16</td><td>0.301</td><td>0.426</td><td>/</td><td>0.538</td><td>0.622*</td><td>0.643*</td><td>0.720**</td></tr><tr><td>2014-5-17</td><td>0.301</td><td>0.426</td><td>/</td><td>0.538</td><td>0.622*</td><td>0.643*</td><td>0.720**</td></tr><tr><td>2014-5-18</td><td>0.210</td><td>0.563</td><td>/</td><td>0.503</td><td>0.678*</td><td>0.552</td><td>0.741**</td></tr><tr><td>Average</td><td>0.265 ± 0.029</td><td>0.469 ± 0.094</td><td>/</td><td>0.473 ± 0.108</td><td>0.575 ± 0.123</td><td>0.619 ± 0.036</td><td>0.713 ± 0.062</td></tr></table>

There are 12 products within the price range.

$$
\rho <   0. 0 5.
$$

\*\* $\mathrm { \rho } ^ { \mathrm { - } } < 0 . 0 1 .$

There are four different types of approaches compared with our approaches in Table 6.

The first approach is to rank products using numeric ratings. Mary et al. applied average rating to rank products and it could perform better than various aggregate quality metrics [37]. The first approach based on numeric rating (R) is represented as M&N′s method, briefly, in the second column in Table 6. The advantage of numeric rating is its simplicity, and it is convenient for potential customers to grasp a general impression when searching for products [13]. The disadvantage is that numeric ratings may not be able to reveal much information regarding the true underlying quality for an effective ranking [16]. Due to the limited granularity of the numeric rating, this approach could not discriminate the products for in-depth comparison because many products share the same rating scores. For example, among the 96 mobile phones in our research, there are 21 scores to measure all of them. In other words, the true evaluation behind the same score assigned for different products may be distinct from each other, which makes it difficult to generate an effective ranking.

generate a ranking of products. The disadvantage is that the products are described in isolation [18], and it could not provide sufficiently an evaluation of products' relative superiority or weakness or a global ranking based on explicit relations between different products.

The second approach is to rank products by text sentiments. Liu et al. extracted the opinions from text reviews to obtain the evaluation of product features for pairwise comparison [23,34], and Tian et al. extended the approach for multiple products ranking [46]. The ranking approach based on text sentiment (T) is denoted as L&T's method, briefly, in the third column in Table 6. The advantage is that text sentiments provide rich information and a deep understanding that extends beyond the scope of a numeric rating, which is potentially useful to

![](images/7f57dabb88970825536dd1a49e31d34802ed77c840efc57eae399a8a763ed984.jpg)  
Fig. 7. Change of coefficient when changing the number of products with comparative relationships.

ρ b 0.05.

Table 12  
Table 13  
Table 11  
Statistics of the collected data.

<table><tr><td>Products categories</td><td>Mobile phones</td><td>Laptops</td><td>Digital camera</td></tr><tr><td>Number of products</td><td>96</td><td>75</td><td>60</td></tr><tr><td>Number of consumer reviews</td><td>23,488</td><td>5345</td><td>1597</td></tr><tr><td>Number of comparative sentences</td><td>310</td><td>26</td><td>22</td></tr><tr><td>Number of comparative votes</td><td>139,641</td><td>42,960</td><td>25,706</td></tr></table>

The third approach is to rank products by comparative sentences. Zhang et al. proposed a ranking approach based on comparative sentences (S) based on a product comparison network [21], which is denoted as Z&G's method, briefly, in the fourth column in Table 6. The advantage of comparative sentence is that it is one of the most convincing means to directly compare the relative superiority or weakness of a product against that of a similar one [28,49,22]. The disadvantage is that the number of comparative sentences in consumer reviews is very small [28,29,51]. The limited number of available comparative sentences greatly restricts their applicability to providing sufficient comparison or comprehensive ranking for many of the products. In addition, in Z&G's method [54], there was no weight for each node in the graph structure, which will ignore the other useful information such as ratings, sentiments.

The fourth approach is to rank products by combining text sentiments and comparative sentences from text reviews. Zhang et al. considered both node and edge weights when ranking products in a product comparison graph model [52], which is denoted as Z&N′s method, briefly, in the fifth column in Table 1. The two types of information, text sentiments and comparative sentences (T + S), correspond to the node and edge in the graph structure, respectively. The advantage of a combination is that it provides a solution to allow text sentiments and comparative sentences to complement each other based on a graph model with both node and edge weights. The disadvantage is that due to the shortage of comparative sentences, a combination still cannot establish sufficient comparative relationships for the majority of products. In addition, there is no generalization for the comparative information and descriptive information on an edge and a node in the graph structure, which may lead to potential bias in the review for each specific product and thus, reduce the ranking effect.

In Table 6, the 6th–8th columns provide the performance of our approach. The abbreviations T, S, R, and V indicate that the used information is derived from Text sentiment (T), comparative Sentence (S), numeric Rating (R), and comparative Votes (V), respectively. The following findings can be derived from Table 6:

(1) The average coefficient of our approach with all $\mathtt { R } + \mathtt { T } + \mathtt { S } + \mathtt { V } ;$ is 0.556, twice that of Z&N′s method. It is also noteworthy that when using the same information, i.e., T + S, our approach is also slightly better (approximately 10% higher) than theirs, implying that the generalized procedures of generating nodes and edges can enhance the performance of the graph structure.

(2) The average coefficient of the proposed method with R + T + S is greater than that of the proposed method with T + S. This fact shows that numeric rating R is undeniably an element of eWOM affecting customers' purchase decisions, and it suggests that we should not ignore numeric rating data when building a product ranking model. It could also be confirmed by comparing the 2nd and the 3rd–6th columns. However, it should be clari ed that, due to the limited expressiveness of numeric rating, many products are assigned with the same rating scores, which makes it difficult to distinguish from each other; in addition, such difficulty could be alleviated by integrating other types of information.

Correlations of sales rank and products rank generated by different methods for laptops.

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>L&amp;T&#x27;s method</td><td>Z&amp;G&#x27;s method</td><td>Z&amp;N&#x27;s method</td><td colspan="3">Our method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2015-8-18</td><td> $0.274^*$ </td><td>0.222</td><td>0.120</td><td>0.189</td><td> $0.233^*$ </td><td> $0.302^{**}$ </td><td> $0.429^{***}$ </td></tr><tr><td>2015-8-19</td><td> $0.274^*$ </td><td> $0.231^*$ </td><td>0.120</td><td>0.210</td><td> $0.235^*$ </td><td> $0.306^{**}$ </td><td> $0.414^{***}$ </td></tr><tr><td>2015-8-20</td><td> $0.267^*$ </td><td> $0.259^*$ </td><td>0.141</td><td> $0.249^*$ </td><td> $0.287^*$ </td><td> $0.354^{**}$ </td><td> $0.456^{***}$ </td></tr><tr><td>2015-8-21</td><td> $0.289^*$ </td><td> $0.247^*$ </td><td>0.140</td><td> $0.272^*$ </td><td>0.222</td><td> $0.345^{**}$ </td><td> $0.458^{***}$ </td></tr><tr><td>2015-8-22</td><td> $0.250^*$ </td><td> $0.257^*$ </td><td>0.130</td><td> $0.246^*$ </td><td> $0.256^*$ </td><td> $0.337^{**}$ </td><td> $0.445^{***}$ </td></tr><tr><td>2015-8-23</td><td> $0.265^*$ </td><td> $0.264^*$ </td><td>0.126</td><td> $0.245^*$ </td><td> $0.255^*$ </td><td> $0.336^{**}$ </td><td> $0.434^{***}$ </td></tr><tr><td>2015-8-24</td><td> $0.261^*$ </td><td> $0.242^*$ </td><td>0.120</td><td> $0.238^*$ </td><td> $0.251^*$ </td><td> $0.327^{**}$ </td><td> $0.465^{***}$ </td></tr><tr><td>2015-8-25</td><td> $0.258^*$ </td><td> $0.244^*$ </td><td>0.114</td><td>0.218</td><td> $0.270^*$ </td><td> $0.298^{**}$ </td><td> $0.448^{***}$ </td></tr><tr><td>2015-8-26</td><td>0.208</td><td> $0.249^*$ </td><td>0.111</td><td> $0.248^*$ </td><td>0.225</td><td> $0.288^*$ </td><td> $0.396^{***}$ </td></tr><tr><td>2015-8-27</td><td> $0.234^*$ </td><td> $0.231^*$ </td><td>0.161</td><td>0.207</td><td> $0.244^*$ </td><td> $0.290^*$ </td><td> $0.415^{***}$ </td></tr><tr><td>Average</td><td> $0.258 ± 0.023$ </td><td> $0.245 ± 0.014$ </td><td> $0.128 ± 0.015$ </td><td> $0.232 ± 0.025$ </td><td> $0.248 ± 0.021$ </td><td> $0.318 ± 0.024$ </td><td> $0.436 ± 0.022$ </td></tr></table>

ρ b 0.05,  
\*\* ρ b 0.01.  
\*\*\* ρ b 0.001.

Correlations of sales rank and products rank generated by different methods for digital cameras.

<table><tr><td rowspan="2">Time</td><td>M&amp;G&#x27;s method</td><td>L&amp;T&#x27;s Method</td><td>Z&amp;G&#x27;s Method</td><td>Z&amp;N&#x27;s Method</td><td colspan="3">Our Method</td></tr><tr><td>R</td><td>T</td><td>S</td><td>T + S</td><td>T + S</td><td>R + T + S</td><td>R + T + S + V</td></tr><tr><td>2015–8-18</td><td>0.192</td><td>0.217</td><td>0.007</td><td>0.179</td><td>0.228</td><td>0.261*</td><td>0.344**</td></tr><tr><td>2015–8-19</td><td>0.193</td><td>0.201</td><td>0.025</td><td>0.179</td><td>0.231</td><td>0.261*</td><td>0.343**</td></tr><tr><td>2015–8-20</td><td>0.217</td><td>0.258*</td><td>0.023</td><td>0.205</td><td>0.235</td><td>0.265*</td><td>0.403***</td></tr><tr><td>2015–8-21</td><td>0.208</td><td>0.215</td><td>0.017</td><td>0.206</td><td>0.235</td><td>0.245</td><td>0.330**</td></tr><tr><td>2015–8-22</td><td>0.205</td><td>0.245</td><td>0.017</td><td>0.246</td><td>0.254*</td><td>0.288*</td><td>0.353**</td></tr><tr><td>2015–8-23</td><td>0.200</td><td>0.248</td><td>0.054</td><td>0.189</td><td>0.248</td><td>0.277*</td><td>0.357**</td></tr><tr><td>2015–8-24</td><td>0.221</td><td>0.213</td><td>0.040</td><td>0.192</td><td>0.199</td><td>0.223</td><td>0.405***</td></tr><tr><td>2015–8-25</td><td>0.176</td><td>0.180</td><td>0.018</td><td>0.174</td><td>0.180</td><td>0.239</td><td>0.377**</td></tr><tr><td>2015–8-26</td><td>0.169</td><td>0.187</td><td>0.016</td><td>0.186</td><td>0.195</td><td>0.222</td><td>0.389**</td></tr><tr><td>2015–8-27</td><td>0.193</td><td>0.219</td><td>0.075</td><td>0.219</td><td>0.248</td><td>0.252</td><td>0.370**</td></tr><tr><td>Average</td><td>0.197 ± 0.016</td><td>0.218 ± 0.026</td><td>0.029 ± 0.021</td><td>0.198 ± 0.0022</td><td>0.225 ± 0.025</td><td>0.253 ± 0.022</td><td>0.367 ± 0.026</td></tr></table>

⁎⁎ ρ b 0.01.  
⁎⁎⁎ ρ b 0.001.

![](images/567d15f75e98901b6bb29e514a9a49c4f5854672a17ec6041f783a5de5c61f93.jpg)  
Fig. 8. Screen shot of a comparative correlation graph for given products.

(3) Among all the ranking methods, the ranking list obtained by the proposed method with R + T + S + V has the highest coefficient with sales rank on average. It is notable that, by adding the online vote V as comparative information, the performance is improved significantly, proving the importance of incorporating this new form of eWOM.

(4) The average coefficients of the methods with S are not satisfying, which is mainly caused by the fact that there are insufficient comparative sentences embedded in the review. Among the 96 products we collected, there are (a few) comparative sentences for only 34 products, and the other 62 products have no ranking, which is insufficient for comparison and deteriorates the ranking performance.

When customers shop online, it is impossible for them to check all possible alternatives, and they usually identify a subset of the most promising ones [22], such as the price range. The price of products is also an important antecedent affecting eWOM communication, which is often mentioned in the text review and discussed in virtual consumer communities [26,27]. Some researchers have determined that price has a significant influence on consumers' purchase of products, and products with lower prices will receive more consumers' favor [1,20]. Before purchasing products, consumers tend to first set a price range, and then compare products' eWOM within the price range. Hence, we analyze the products from different price ranges, with results given in Tables 7–10. From the tables, it is obvious that our method with R + T + S + V always returns the best performance, and no matter which price range to which the products belong, our method can steadily provide satisfying ranking results.

One contribution of this paper is that we introduce much more comparative information to assist the ranking of multiple products, and its effectiveness must be verified with more evidence. In Fig. 7 are five scenarios of experiments designed to the approach's effectiveness, in which the x axis is the number of products randomly selected to keep their comparative relationships with other products. The detailed statistics of results are described in Fig. 7. For example, when x = 0, there is no comparative information for any product and the ranking solely relies on the descriptive information. Not surprisingly, the performance is the worst, with the coefficient less than 0.3. When x = 24, there are 24 products randomly selected to keep their comparative information, while comparative information of the remaining products is all removed. It is obvious from Fig. 7 that with more comparative information, the performance of ranking is gradually improved, and the improvement curve seems to present a nonlinear function with an increasing growth rate during the early stage and a decreasing growth rate during the later stage. The nonlinear curve may be caused by that effect; although comparative information can undoubtedly improve the performance significantly, it does not mean that the increased amount of comparative information can always lead to an equal amount of improvement. When comparative information exists for most of the products, its effectiveness tends to converge gradually.

The public media as well as prior adopters will share the descriptive as well as comparative information, which usually influences the potential customers' preferences or purchase decisions. The comparative votes may express the previous experience by those who really tried different types of phones, or indicate the future demand by those who compared the products using external information. Regardless of where the voting information originates from, it will generally agree with the behaviors in the markets and thus help us improve the ranking performance if it is included in the ranking approach.

## 5.2.2. Scalability study

In addition to the one category of data (i.e., mobile phone) studied in the above section, in order to study the scalability of our approach, there are two other categories of data analyzed, which include laptop and digital camera.

Table 11 shows certain statistics regarding the three categories. The collection period for laptops and digital cameras was in August 2015. The three categories of products collected in our research were always available and not sold out on online retailer websites during the collection period.

The experimental results of laptop and digital camera are listed in Table 12 and Table 13, respectively, where there are seven different ranking approaches for each category. The following could be observed from the results:

(1) The major findings observed from Table 6 (mobile phone) are reproduced in Table 12 (laptop) and Table 13 (digital camera). For example, the combination of four types of information could achieve the highest ranking performance, whereas the simple rating is undeniable because it could improve the results to a certain extent.

(2) If we closely examine the last two columns in Table 6, Table 12 and Table 13, it is obvious that, when the comparative vote is applied, the ranking performance of mobile phone is improved the most. By connecting such phenomena with the largest number of comparative votes for mobile phone shown in Table 11, generally it could be inferred that more comparative votes could lead to better performance. This finding agrees with our finding when studying effects of the number of comparative votes.

## 5.2.3. A ranking system to support decision-makers

In this section, we will discuss how to build a prototype system for ranking multiple products based on the above methods. By the ranking system, consumers can compare the alternative products side-by-side that they want to add into their wish lists or shopping carts. Manufacturers can analyze competitive products by ranking the overall eWOM gathered from heterogeneous information sources and understand better the exact position where their own products stand.

There are usually two stages for customers to make purchasing decisions. They first screen a set of alternatives and subsequently evaluate candidates in more depth [22]. To illustrate, a customer first selects five candidates $( P _ { 1 } , P _ { 2 } , P _ { 3 } , P _ { 4 } , P _ { 5 } )$ after setting a price range; then, our ranking system can assist the customer to perform an in-depth comparison by ranking the five alternatives and providing some useful comparisons. As shown in Fig. 8, the eWOM ranking is $\mathrm { P } _ { 5 }  \mathrm { P } _ { 4 }  \mathrm { P } _ { 1 }  \mathrm { P } _ { 3 }  \mathrm { P } _ { 2 } .$ The corresponding weighted comparative digraph is also given in the figure. In the digraph, there are primarily three types of visualized representations:

(1) Color of node. The color of a node denotes the overall value of the eWOM score. For the higher overall eWOM score of a product, the color of the corresponding node will be darker.

(2) Size of node. The size of a node means the value of its node weight, which is derived from the descriptive information of the corresponding product. For a higher node weight, the node size will be larger.

(3) Edge. When there is an edge linking product $P _ { i }$ to $P _ { j } ,$ , there are more votes for P than for $P _ { i } .$

From the graph, it is noteworthy that although the node weight of $P _ { 5 }$ is slightly smaller than $P _ { 4 } , P _ { 5 }$ has more votes than do any of the other products, and such superiority helps $P _ { 5 }$ to obtain a higher overall eWOM score than the others do. The result may be a little surprising at first glance because the information from heterogeneous sources seems conflictive. However, during the shopping process, this situation does occasionally occur. For a product with high anticipation, we may feel some disappointment after the purchase due to various reasons (i.e., low node weight in the digraph), but after comparing it with the other alternatives, we find that this product remains much better (i.e., more votes in the digraph). This is the advantage of comparison shopping to make an informed choice, and our system can provide the capability to simplify the comparison.

![](images/8368efc441ea288f6d782920cf582bf3cbbef0cf39c11f9bdef61fd4d5460aaa.jpg)  
Fig. 9. The structure of prototype system

Another notable phenomenon is that although $P _ { 1 } , P _ { 3 } ,$ and $P _ { 5 }$ have the same size nodes, the votes they attracted are distinctive, resulting in significant differences in overall eWOM. The size of a node is determined by descriptive information, and such information is widely adopted in various studies of online opinion mining. However, if customers rely solely on the descriptive information in this case, it would be difficult for them to discriminate the aforementioned three products. The introduction of comparative information can remedy the limitation of descriptive information and help customers not to deviate from the true eWOM.

In summary, by the ranking system, consumers can learn the summarized eWOM for alternative products, including both inherent eWOM derived from descriptive information and extrinsic eWOM that accumulated from their comparative relationships with other products. The illustration also shows that the ranking system is an intuitive and effective means of aiding consumers to compare the eWOM across multiple products and improve their efficiency in making appropriate purchasing decisions.

Additionally, the ranking system also has important practical implications for manufacturers. From the ranking results, they can see the eWOM positions of their own products among competitive products clearly. There is another advantage; that is, not only the ranking can be provided but also some implicit causes of the resulting ranking can be analyzed, which may help manufacturers to target problems with their products.

For example, if the descriptive information content is low $( \mathrm { i . e . , } \mathsf { a }$ smaller node in Fig. 8) and comparative information content is high (i.e., more edges in Fig. 8) for a product, as in the case of $P _ { 5 }$ in Fig. 8, there are both negative sentiments and positive votes from customers' feedback. The negative sentiments might be caused by excessive propaganda, and the customers would feel some disappointment or even antipathy. The positive votes show that the quality of the product is sufficiently fair to keep a favorable position. In this case, it would be a good policy for the manufacturer to reduce extra advertisements and to encourage more users to experience and compare the products.

In contrast, if the descriptive information content is high (i.e., a larger node in Fig. 8) and comparative information content is low (i.e., fewer edges in Fig. 8) for a product, the situation might be that, although customers provide some positive sentiments, they find some other products even better after the comparison. It is a dangerous signal because the customers could easily abandon this product and switch to another, superior alternative. The manufacturer must catch up with competitors; otherwise, it will lose its market share.

The prototype system is built for ranking multiple products based on the proposed methods, and its structure is illustrated in Fig. 9.

There are three layers in the structure, including a data layer, a process layer, and a user layer. In the data layer, the raw data are collected from an e-commerce portal and decomposed into various types of information, which are integrated into the process layer. The ranking approach proposed in this paper is applied to generate the product ranking results. The users, including potential customers and manufacturers, could select a subset of products for comparison and analyze the returned ranking graph via the system interface in the user layer, which is also demonstrated in Fig. 8.

## 6. Conclusions and future work

Recent trends have indicated that before making purchasing decisions, consumers prefer to compare the eWOM of products involved in online reviews. In this paper, we design a novel eWOM ranking method to help consumers compare multiple products by integrating the rich information from heterogeneous sources including numeric ratings, text reviews, comparative sentences and comparative votes. We find that with more information integrated, the ranking method can return better performance. In particular, comparative votes, which have attracted little attention in previous studies, contribute significantly to the ranking quality. An effective system is also demonstrated to help customers make informed choices when comparison shopping and assist manufacturers to maintain awareness of the exact positions of their products and to target implicit problems underlying the data.

In spite of the contributions made in this research, there are limitations which need further exploration. Although our approach exhibits a promising performance from experimental results, the current research could be enhanced by a more solid theoretical foundation to deeply analyze the working principle. For example, it could help improve the performance if the precise role or relative importance of each type of information could be determined theoretically.

There are certain studies that investigate the property of one type of information, such as rating [20], text sentiments [38] and comparative sentences [29], and several studies have noted a comparison between multiple types of information. Archak et al. [1] have addressed the question of whether text sentiments have more influence on product sales beyond the numeric ratings, and they observed that the absolute value of the coefficient on the average review rating goes down when textual data are incorporated into the model. Hu et al. [24] found that ratings have an indirect impact through sentiments, whereas sentiments have a direct significant impact on sales. Wang et al. proposed a general assumption that the reviewer assigns a rating by evaluating many aspects of the product based on the sentiments of words he used to discuss that aspect, and the overall rating depends on the weighted sum of all the aspect ratings [48]. In addition, Liu discovered that the impact of WOM is dynamic and its pattern could evolve over time [36], which makes it more difficult to determine a stable underlying mechanism. Furthermore, there is also certain negative evidence. For example, Dave et al. discovered that similar qualitative descriptions can yield very different quantitative reviews from reviewers, and in the some extreme cases, reviewers even do not understand the rating system [9]. In a word, the existing research has not presented any consistent conclusion, which could hardly provide a solid theoretical foundation but reward research direction for the future work.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (71001016, 71271036, 71471028, 71421001), Humanity and Social Science Foundation of Ministry of Education of China (15YJCZH198), and Economic and Social Development Foundation of Liaoning (2016lslktzizzx-01).

## Appendix A. Proof

A.1. Proof of Lemma 1

$$
\text {   Supposed   } \sum_ {i = 1} ^ {n} W S c o r e (P _ {i}) = 1, \text {   we   have   }
$$

$$
\begin{array}{r l} W \_ S c o r e & = (1 - \beta) * W ^ {V} + \beta * A * W \_ S c o r e \\ & = (1 - \beta) * W ^ {V} * e ^ {\mathrm{T}} * W \_ S c o r e + \beta * A * W \_ S c o r e \\ & = \left[ (1 - \beta) * W ^ {V} * e ^ {\mathrm{T}} + \beta * A \right] * W \_ S c o r e \\ & = B * W \_ S c o r e \end{array}
$$

Therefore, $\pmb { { \cal B } } = ( 1 - \beta ) ^ { * } { \cal W } ^ { V * } e ^ { \operatorname { T } } + \beta ^ { * } \pmb { A }$ . W\_Score is the eigenvector of matrix B, and the eigenvalue is 1.

## A.2. Proof of Proposition 1

First, when considering $W ^ { V } ( P _ { i } ) > 0$ and $a _ { i j } @ \ ' ) = 0 , i , j = 1 , . . . , n$ , we can know that $b _ { i j } = ( 1 { - } \beta ) ^ { * } W ^ { V } ( P _ { i } ) + \beta ^ { * } a _ { i j } > 0$ , and $b _ { \ i j } ^ { \mathrm { T } } > 0$ . Based on the theorem that a positive transfer matrix is irreducible and aperiodic, we can prove $\pmb { B } ^ { \mathrm { T } }$ is an irreducible and aperiodic matrix.

Then,

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \boldsymbol {B} _ {i j} = \sum_ {i = 1} ^ {n} \left[ (1 - \beta) * W ^ {V} * e ^ {\mathrm{T}} + \beta * \boldsymbol {A} \right] _ {i j} \\ = (1 - \beta) * \sum_ {i = 1} ^ {n} W ^ {V} + \beta * \sum_ {i = 1} ^ {n} \boldsymbol {A} _ {i j} \\ = (1 - \beta) * \sum_ {i = 1} ^ {n} \frac {\text { Score } (P _ {i})}{\sum_ {k = 1} ^ {n} \text { Score } (P _ {k})} + \beta * \sum_ {i = 1} ^ {n} \boldsymbol {A} _ {i j} \end{array}
$$

$$
\text { Here, } \sum_ {k = 1} ^ {n} S c o r e (P _ {k}) = S c o r e (P _ {1}) + S c o r e (P _ {2}) + \dots + S c o r e (P _ {n}) \text {   is   a   con- }
$$

stant. Given $c = \sum _ { k = 1 } ^ { n } S c o r e ( { \mathrm { P } _ { k } } ) .$ , then.

$$
\sum_ {i = 1} ^ {n} \frac {\text { Score } (\mathrm{P} _ {i})}{\sum_ {k = 1} ^ {n} \text { Score } (\mathrm{P} _ {k})} = \sum_ {i = 1} ^ {n} \frac {\text { Score } (\mathrm{P} _ {i})}{c} = \frac {1}{c} * \sum_ {i = 1} ^ {n} \text { Score } (\mathrm{P} _ {i}) = \frac {1}{c} * c = 1.
$$

$$
\text { Similarly }, \sum_ {i = 1} ^ {n} \boldsymbol {A} _ {i j} = \sum_ {i = 1} ^ {n} \frac {W ^ {E} (P _ {i} | P _ {i} , P _ {j})}{\sum_ {l = 1} ^ {n - 1} W ^ {E} (P _ {l} | P _ {l} , P _ {j})} = 1.
$$

Therefore, $\sum _ { j = 1 } ^ { n } \pmb { B } _ { i j } ^ { \operatorname { T } } = ( 1 - \beta ) * 1 + \beta * 1 = 1 , \pmb { B } ^ { \operatorname { T } }$ is a stochastic matrix and W\_Score converge to a stationary probability distribution.

## References

[1] N. Archak, A. Ghose, G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Management Science 57 (8) (2011) 1485–1509.

[2] S. Avneri, S. John, Product differentiation and industrial structure, The Journal of Industrial Economics 36 (2)(1987) 131–146

[3] J. Bettman, E. Johnson, J. Payne, A componential analysis of cognitive effort in choice, Organizational Behavior and Human Decision Processes 45 (1) (1990) 111–139.

[4] H. Chen, Intelligence and security informatics: information systems perspective, Decision Support Systems 41 (3) (2006) 555–559.

[5] Y. Chen, J. Xie, Online consumer reviews: word-of-mouth as a new element of marketing communication mix, Management Science 54 (3) (2008) 477–491.

[6] J. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[7] P. Chintagunta, S. Gopinath, S. Venkataraman, The effects of online user reviews on movie box office performance: accounting for sequential rollout and aggregation across local markets, Marketing Science 29 (5) (2010) 944–957.

[8] E. Clemons, G. Gao, L. Hitt, When online reviews meet hyper differentiation: a study of the craft beer industry, Journal of Management Information Systems 23 (2) (2006) 149–171.

[9] K. Dave, S. Lawrence, D. Pennock, Mining the peanut gallery: opinion extraction and semantic classification of product reviews, Proceedings of the 12th International Conference on World Wide Web, 2003.

[10] C. Dellarocas, The digitization of word-of-mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 1407–1424.

[11] W. Du, S. Tan, Building domain-oriented sentiment lexicon by improved information bottleneck, Proceeding of the 18th ACM Conference on Information and Knowledge Management(CIKM) 2009 pp. 1749–1752

[12] W. Duan, B. Gu, A. Whinston, Do online reviews matter? An empirical investigation of panel data Decision Support System 45 (4) (2008) 1007–1016

[13] W. Duan, B. Gu, A. Whinston, Informational Cascades and software adoption on the Internet: an empirical investigation, Management Information System Ouarterly 33 (1) (2009) 23–48.

[14] J. Eliashberg, S. Hui, Z. Zhang, From story line to box office: a new approach for green-lighting movie scripts, Management Science 53 (6) (2007) 881–893.

[15] J. Feng, X. Li, Rising or dropping: the consumer review oriented pricing paradox, Proceedings of International Conference on Information System, 2011 paper 13.

[16] A. Ghose, P. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 10 (23) (2011) 1498–1512.

[17] A. Ghose, P. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Marketing Science 31 (3) (2012) 493–520.

[18] D. Godes, D. Mayzlin, Using online conversation to study word of mouth communications, Marketing Science 23 (4) (2004) 545–560.

[19] G. Grimmett, D. Stirzaker, Probability and Random Process, Oxford University, 1989.

[20] B. Gu, J.H. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales for high involvement products, Information Systems Research 1 (23) (2012) 182–196.

[21] J. Han, M. Kamber, Data Mining: Concepts and Techniques, third ed. Morgan Kaufmann, 2011 July.

[22] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4–21.

[23] M. Hu, B. Liu, Opinion extraction and summarization on the web, Proceedings of International Conference on American Association for Artificial Intelligence 2006, pp. 1621–1624.

[24] N. Hu, N. Koh, S. Reddy, Rating lead you to the product, reviews help you clinch it? The Mediating Role of Online Review Sentiments on Product Sales, Decision Support System 57 (2014) 42–53.

[25] X. Huang, X. Wan, J. Yang, J. Xiao, Learning to identify Chinese comparative sentences, Journal of Chinese Information Processing 5 (22) (2008) 30–38.

[26] K. Hung, S. Li, The influence of eWOM on virtual consumer communities: social capital, consumer learning, and behavioral outcomes, Journal of Advertising Research 47 (4) (2007) 485–495.

[27] E. Jeonga, S. Jang, Restaurant experiences triggering positive electronic word-ofmouth (eWOM) motivations, International Journal of Hospitality Management 30 (2) (2011) 356–366.

[28] N. Jindal, B. Liu, Identifying comparative sentences in text documents, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development on Information Retrieval 2006, pp. 244–251.

[29] N. Jindal, B. Liu, Mining comparative sentences and relations, Proceedings of the 21th National Conference on Artificial Intelligence 2006, pp. 1331–1336.

[30] R. Kong, Y. Wang, W. Xin, T. Yang, J. Hu, Z. Chen, Customer Reviews for Individual Product Feature-Based Ranking, Proceedings of International Conference on Instrumentation, Measurement, Computer, Communication and Control 2011, pp. 449–453.

[31] N. Li, D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support System 48 (2) (2010) 354–368.

[32] S. Li, Z. Zha, Z. Ming, Product comparison using comparative relations, Proceedings of 11th International Conference on Special Interest Group on Information Retrieval 2011, pp. 1151–1152.

[33] H. Liao, Z. Xu, X. Zeng, Hesitant fuzzy linguistic VIKOR method and its application in qualitative multiple criteria decision making, IEEE Transactions on Fuzzy Systems 23 (5) (2015) 1343–1355.

[34] B. Liu, M. Hu, J. Cheng, Opinion observer: Analyzing and comparing opinions on the web, Proceedings of the 14th International Conference on World Wide Web 2005, pp. 342-351.

[35] B. Liu, Sentiment Analysis and Subjectivity, Handbook of Natural Language Processing, second ed., 2010.

[36] Y. Liu, Word of mouth for movies: its dynamics and impact on box office revenue, Journal of Marketing 70 (3) (2006) 74–89

[37] M. Mary, G. Natalie, R. Zach, Star quality: Aggregating reviews to rank products and merchants, Proceedings of the 4th International AAAI Conference on Weblogs and Social Media 2010, pp. 114–121.

[38] O. Netzer, R. Feldman, J. Goldenberg, M. Fresko, Mine your own business: marketstructure surveillance through text mining, Marketing Science 31 (3) (2012) 521-543

[39] F. Nicosia, Consumer Decision Process, Prentice Hall, Engle wood Cliffs, NJ, 1996.

[40] L. Page, S. Brin, R. Motwani, T. Winograd, The PageRank Citation Ranking: Bring Order to the Web, Stanford University, 1999.

[41] S. Park, W. Vanhonacker, The challenge for multinational corporations in China: think local, act global, MIT Sloan Management Review 48 (2007) 8–15.

[43] T. Raghu, H. Chen, Cyberinfrastructure for homeland security: advances in information sharing, data mining, and collaboration systems, Decision Support Systems 43 (4) (2007) 1321–1323.

[44] R. Song, H. Lin, F. Chang, Chinese comparative sentences identification and comparative relations extraction, Journal of Chinese Information Processing 2 (23) (2009) 102–107.

[45] B. Tedeschi, Help for the merchant in navigating a sea of shopper opinions, The New York Times (September 6). (http://www.nytimes.com/2006/09/04/technology/ 04ecom.html).

[46] P. Tian, Y. Liu, M. Liu, S. Zhu, Research of product ranking technology based on opinion mining, Proceedings of Second International Conference on Intelligent Computation Technology and Automation 2009 pp. 239–243.

[47] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (1974) 1124–1131

[48] H. Wang, Y. Lu, C. Zhai, Latent aspect rating analysis on review text data: A rating regression approach, Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2010, pp. 783–792.

[49] K. Xu, S. Liao, J. Li., Y. Song, Mining comparison opinions from consumer reviews for competitive intelligence, Decision Support System 50 (4) (2011) 743–754.

[50] K. Zhang, Y. Cheng, W. Liao, A. Choudhary, Mining millions of review: a technique to rank products based on importance of reviews, Proceedings of Association for the Advancement of Artificial Intelligence, 2011.

[51] K. Zhang, R. Narayanan, A. Choudhary, Mining Online Consumer Reviews for Ranking Products, Technical Report, EECS department, Northwestern University, 2009.

[52] K. Zhang, R. Narayanan, A. Choudhary, Voice of the customers: mining online customer reviews for product feature-based ranking, Proceedings of 3rd Workshop on Online Social Networks. 2010

[53] S. Zhang, A. Markman, Processing product unique features: alignability and in volvement in preference construction, Journal of Consumer Psychology 11 (2001) 13–27.

[54] Z. Zhang, C. Guo, P. Goes, Product comparison networks for competitive analysis of online word of mouth, ACM Transactions on Management Information System 3 (4) (2013) 1–22.

Xian Yang is a graduate student at Institute of Systems Engineering in Dalian University of Technology. Her research is about sentiment analysis

Guangfei Yang is an associate professor at Institute of Systems Engineering in Dalian University of Technology. He received his doctoral degree in engineering at Waseda University in 2009. His research is about data mining, knowledge management, and computational intelligence.

Jiangning Wu is a professor at Institute of Systems Engineering in Dalian University of Technology. She received her PhD at The University of Hong Kong. Her research is about knowledge management, web mining, and text mining.