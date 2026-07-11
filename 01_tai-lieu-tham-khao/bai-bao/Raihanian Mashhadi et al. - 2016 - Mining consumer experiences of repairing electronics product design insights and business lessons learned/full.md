# Mining consumer experiences of repairing electronics: Product design insights and business lessons learned

Ardeshir Raihanian Mashhadi <sup>a</sup>, Behzad Esmaeilian <sup>b</sup>, Willie Cade <sup>c</sup>, Kyle Wiens <sup>d</sup>, Sara Behdad <sup>a,</sup> <sup>\*</sup>

<sup>a</sup> Mechanical and Aerospace Engineering Department, University at Buffalo, SUNY, Buffalo, 14260-1660, NY, USA

<sup>b</sup> Industrial and Systems Engineering Department, Northern Illinois University, DeKalb, IL, 60115, USA

<sup>c</sup> PC Rebuilders & Recyclers, Chicago, IL, 60651, USA

<sup>d</sup> iFixit Inc., San Luis Obispo, CA, 93401, USA

## a r t i c l e i n f o

Article history: Received 27 September 2015 Received in revised form 29 March 2016 Accepted 23 July 2016 Available online 25 July 2016

Keywords: Product end-of-use recovery Product repair Consumer electronics Data mining WEEE

## a b s t r a c t

Despite various efforts to shed light on the different aspects of repair and maintenance processes, our entire understanding of the repair practices done on consumer electronics comes from either the manufactures or professional repair experts. There is a lack of systematic, well-documented studies of repair practices by unprofessional individual consumers. Understanding the factors contributing to unprofessional repair practices is a necessity to lengthen the life span of the product and to promote repair as an eco-behavior among individual consumers. We have investigated 4210 break and <sup>fi</sup>x narratives reported by consumers of electronic devices in a survey conducted by iFixit.com - a wiki-based website for repair manuals - in order to apperceive the most common failures, repair practices and challenges that individual users face in their interactive experiences with product repair. A comprehensive text mining set up has been applied to extract the most frequent product break stories and their causes of failure. Regression analyses have been employed to examine the possible links between consumer experiences of repairing electronics and their future purchase behaviors. The results of analyses indicate that in addition to the consumers' attitude toward repair, various product design features offer different levels of repair convenience, which may eventually impact the consumer's future purchase decisions.

© 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Technology is rapidly changing in the way that new products are designed and manufactured. Examples include material ef<sup>fi</sup>- ciency and miniaturization, glue-based joint mechanism, higher levels of on-chip integration, and new technologies for power storage and printed electronics. While these technologies offer potential for lower environmental impacts, it is not yet clear how these gains might be offset by the overall increases in product design complexity and dif<sup>fi</sup>culty of repair. Increasingly dense structures of products, coupled with manufacturers' policies in insuf<sup>fi</sup>cient sharing of repair information with the public may lead to a decrease in consumer interest and participation in the repair process. However, any increase of public interest in repair will contribute to environmental sustainability by lengthening the product life span (Cooper, 2005). In addition, comparing to other End-of-Use treatments such as remanufacturing, recycling and disposal, repair may be a better candidate because of the lower consumption of energy and resources (Bekin et al., 2007). Moreover, product repairability level and repair policies may reveal secondary economic consequences for OEMs (Sabbaghi et al., 2016).

Despite the importance of empowering consumers to repair, much of our understanding of the repair practices done on consumer electronics comes from either designers or professional repair experts. There is a lack of systematic, well-documented studies of repair practices by unprofessional individual consumers. To overcome this gap, 4210 repair and <sup>fi</sup>x stories reported by consumers of electronic devices in a survey conducted by iFixit website have been examined. iFixit is a wiki-based website that provides free repair manuals; however, the consumers can purchase the required tools and parts from it or similar websites as well. In wiki-based websites such as i<sup>fi</sup>xit, regular users can avail themselves of the manuals to repair their products. The large number of users of these websites can provide a good representation of the market. The consumers' stories have been analyzed in order to derive insights from their actual repair experiences. Text mining techniques have been utilized to extract knowledge from the textual information reported by the survey respondents. The results of such analyses will determine the most frequent products failed, component failure causes and the most common repair practices with the purpose of providing managerial insights regarding the actual challenges that individual consumers face while repairing electronics. In addition, there is evidence in the literature that the failure in unprofessional repairs may alter the consumer attachment to the product (Gregson et al., 2009). Hence, a dataset of consumer stories have been used to connect previous repair experiences to future product purchase decisions in order to clarify the business outcomes of product repairability for manufactures. The contribution of the current paper is to scrutinize consumer repair experiences and opinions in order to <sup>fi</sup>rst, shed light on the actual barriers of unprofessional repair as an ecofriendly, end of life recovery option and second, provide managerial insights about the possible links between such experiences and consumers' future decisions.

The rest of this paper is organized as follows: Section 2 introduces the previous literature on repair and maintenance, as well as previous efforts in utilizing data mining techniques in this area. Section 3 presents the text mining framework and the corresponding extracted information from the stories. Section 4 provides the regression analysis and the linkage between consumer repair experiences and future purchase decisions, and <sup>fi</sup>nally, Section 5 concludes the paper.

## 2. Literature review

## 2.1. Importance of repair as an eco-behavior

Repair is regarded as the most sustainable End of Life (EOL) option (Stahel, 1994). King et al. (King et al., 2006) argued that consumer behavior and the lack of manufacturer responsibility are the main barriers preventing repair from becoming the dominant EOL option. Lower perceived quality of repaired products compared to new products, lower warranty time, high cost of repair and planned obsolescence are among the factors that have been reported for such behavior. While the technical feasibility of product reuse has already been the point of interest in the literature (e.g. (Sena da Fonseca et al., 2015) (Zhou et al., 2012)), there is a lack of research in investigating the business outcomes of reuse and similar EOU options such as repair. Gelbmann and Hammerl (Gelbmann and Hammerl, 2014) emphasized on the need for innovative business models that promote the repair and reuse of unwanted products. They introduced the concept of ecologically oriented work integration social enterprises (re-use ECO-WISEs) as a novel business model toward Sustainable Product Service System (SPSS) movement. Reim et al. (Reim et al., 2014) also discussed the importance of balancing business outcomes and the social and environmental aspects in attracting more consumers. They stressed the point that the long-term relationship with consumers as opposed to short-term market driven strategies will bring more consumer loyalty, especially in SPSS systems. They concluded their study with expressing the need for more empirical studies to reveal the impact of different business strategies on long-term pro<sup>fi</sup>tability of companies.

Understanding the business outcomes of repair policies (e.g.

design for durable and repairable products) requires more information about consumer behavior and their attitude toward repair and reuse activities. A signi<sup>fi</sup>cant number of prior studies aimed at investigating the factors that impact consumer's green and recycling behavior. To name a few, Zhao et al. (Zhao et al., 2014) ran a survey to identify the factors in<sup>fl</sup>uencing the purchase of green products in China and concluded that consumers' attitude toward green activities is one of the main predictors of their purchase behavior. Nnorom et al. (Nnorom et al., 2009) also studied the willingness of consumers to participate in electronic waste recycling in Nigeria. The economic cost of green consumer behavior (Gadenne et al., 2011), the combination of perceived personal bene<sup>fi</sup>ts, and decreased risk and uncertainty are among the factors that lead consumers from positive attitudes to the actual adoption of green behaviors (Hartmann and Apaolaza-Ibanez, 2012). Pine and Gilmore have emphasized on the role of consumer experiences on their future purchase decisions (Pine and Gilmore, 1998). While studying the eco-behavior of consumers is not something new, very little literature research has explored repairing used devices as an eco-behavior. The individuals' environmental behavior covered in the literature so far includes behaviors such as waste avoidance (Li et al., 2013), energy conservation (Chen et al., 2011), and recycling (Koga et al., 2013). There is a need to analyze other eco-behaviors such as sustainable consumption, purchasing refurbished products, product sharing, and repair. The speci<sup>fi</sup>c focus of this research will be on repair activity.

The importance of after-sale repair services has been unequivocal in the literature. The idea of improving the buyer-seller relationship through enhancing the repair and quality of after-sale services is a well-known concept (Zeithaml, 2000). Rigopoulou et al. (Rigopoulou et al., 2008) showed that installation and delivery, as two examples of after-sale service, can in<sup>fl</sup>uence consumer satisfaction. Cohen and Whang (Cohen and Whang, 1997) believed that the quality of after-sale services is a policy that manufacturers adopt to improve the perceived quality of their products. They also pointed out that in some industries such as construction equipment, farm equipment, mainframe computers and automobiles, the pro<sup>fi</sup>t margin from after-sale services far exceeds the transaction pro<sup>fi</sup>t of selling the actual goods. In addition, in electronics and communication industries, the after-sale service revenue can be up to 30% of the product revenue (Cohen et al., 1997).

While reviewing the economic bene<sup>fi</sup>ts of the repair services, the corresponding challenges in the repair practices should be noted. Generally, the major issue in the EoL recovery processes (i.e., repair, reuse, remanufacture and refurbish) is the presence of various sources of uncertainty (Mashhadi et al., 2015). The uncertainty in the quality of the to-be-repaired products can intensively affect the performance of the repair practices and is in<sup>fl</sup>uenced by the consumers' usage behavior (Sabbaghi et al., 2015). Rosner and Ames (Rosner and Ames, 2014) pointed out a set of material, infrastructural, gendered, political and socio-economic factors that affect consumers' success in repair practices. They also noted that it is challenging to consider these factors in the product design phase. It has been shown that as the dif<sup>fi</sup>culty of repair for an individual increases, so does the severity of their dissatisfaction. As a result, the tendency of consumer to participate in the negative word of mouth may increase as well (Richins, 1983).

Such topics have received suf<sup>fi</sup>cient attention from the research community. There are quite a large number of studies available in the literature that aim to investigate the warranty data, minimize the warranty cost and analyze different warranty policies. To give an example, Jack et al. (Jack et al., 2009) proposed a servicing strategy on repair-replace under warranty to minimize warranty cost. Their model can be applied to single-component products, multi-component products or the components themselves. They tried to determine whether to repair or replace a product based on its age at the time of claim. The idea of extending the repair market opportunities to manufacturers has been discussed by Zhu et al. (Zhu et al., 2012). They proposed a web-based product-service system for maintenance, repair and the overhaul of aircrafts. Several review studies can also be found on the warranty and maintenance topic: (Sha<sup>fi</sup>ee and Chukova, 2013), (Garg and Deshmukh, 2006) and (Sharma et al., 2011) are a few examples.

Murthy and Djamaludin (Murthy and Djamaludin, 2002) categorized the studies under six different topics: Warranty Policies, Warranty Cost Analysis, Warranty and Engineering, Warranty and Marketing, Warranty and Logistics and Warranty Management. Among these studies, those related to repair and its impact on product design are of more interest to this paper. These studies cover the relationship between warranty and product reliability and the implications of product design on warranty policies. The signi<sup>fi</sup>cance of reparability and the use of warranty data to modify the design have been recognized. Ease of reparability has been raised as one of the potential bene<sup>fi</sup>ts of modular design (Kusiak, 1998), (Stoll, 1986). Anastas and Zimmerman (Anastas and Zimmerman, 2003) emphasized on the impact of maintenance on preserving the designed life of a product with minimal addition of material and energy. Hatcher et al. (Hatcher et al., 2013) raised the importance of integrating ‘design for remanufacture’ (DfRem) concepts into the design process. Ajukumar and Gandhi (Ajukumar and Gandhi, 2013) also pointed out the need for green maintenance initiatives in the product design stage and developed an evaluation tool to rank different design alternatives in terms of their ease-of-maintenance.

Not only the product repairability is important, but also it has some signi<sup>fi</sup>cant impacts on other product recovery practices. Sundin and Bras (Sundin and Bras, 2005) showed that cleaning and repairing are the most critical steps in the remanufacturing processes. Similarly, Behdad and Thurston (Behdad and Thurston, 2010) reckoned maintenance and component upgrades as pivotal steps in remanufacturing processes and conducted a disassembly sequence planning corresponding to them. Due to the critical role of reparability, utilizing repair data to modify the product design seems a promising approach. Majeskeat et al. (Majeskeat et al., 1997) analyzed the warranty data in the automobile industry and proposed that the results of analysis can enhance the engineering design. Yang and Cekecek (Yang and Cekecek, 2004) also pointed out the role of warranty data to capture the most frequent failed parts, and the failure time and cost in automotive industry. They used a design vulnerability analysis to prioritize the design improvements. In addition, many researchers have tried to propose optimal designs and maintenance schemes considering the overall lifecycle cost of the product including the repair cost (Singh et al., 2010; Thomsen et al., 2015; Pandey et al., 2013).

Despite the importance of repair as an eco-friendly activity and the recent efforts to emphasize its role in the economy and the society, there is limited literature on this matter. Dant (Dant, 2004) claimed that the changing economics of repair now motivates the consumers to apply such practices to high-cost products such as personal computers. Graham and Thrift (Graham and Thrift, 2007) analyzed repair and maintenance from a sociological perspective and emphasized their signi<sup>fi</sup>cance as an everyday life activity. More interestingly, Gregson et al. (Gregson et al., 2009) showed that incompetence in home objects repair and maintenance can act as a critical driver for future purchase decisions. Scott and Weaver (Scott and Weaver, 2014) have investigated the factors related to repair propensity among consumers and introduced three groups of product, consumer and market related factors that can motivate consumers toward repair. The mentioned studies reveal the gravity of consumer repairs, both as technical and cultural point of views and yet, research on studying repair practices by unprofessional individual consumers is very limited. So far, no study has examined the actual consumer experiences of repairing electronics and the challenges they may face.

The objective of this paper is to mine the consumers' prior repair experiences with the aim of extracting product design strategies that empower consumers to repair; and <sup>fi</sup>nally, understanding the impact of repair experiences on consumers' future purchase decisions.

## 2.2. Data mining in repair domain

Since the emergence of data mining methods, such algorithms have been utilized in many applications; repair and maintenance are no exceptions. In a review paper, Harding et al. (Harding et al., 2006) argued that maintenance was one of the <sup>fi</sup>rst areas of manufacturing in which data mining methods were used. However, there are not enough studies reported in this domain. To name a few: Letorneau et al. ( Letorneau et al., 1999 ) employed data mining techniques on sensor data to <sup>fi</sup>nd the proper preventive maintenance policies. Romanowski and Nagi (Romanowski and Nagi, 2001) used the concept of decision trees to identify the best preventive maintenance schedule based on the product's maintenance history and sensor data. Batanov et al. (Batanov et al., 1993) also worked on <sup>fi</sup>nding a proper maintenance schedule by analyzing historical failure data using data mining tools. In addition, Hsu et al. (Hsu and Kuo, 1995) applied data driven approaches to design and optimize the maintenance policies.

Generally speaking, data mining methods strive to use a vast spectrum of techniques to capture and discover hidden patterns and knowledge in large data sets (Harding et al., 2006). As a result, such methods can be applied to any domain whenever large volumes of data are involved. Accordingly, analyzing large data sets of consumer feedbacks and the information generated by them (i.e. consumer reviews) has been getting more and more attention in the research community. Particularly, many studies have investigated the impact of consumer reviews on the sales based on the volume and valence of the reviews (Godes and Mayzlin, 2004; Duan et al., 2008; Chevalier and Mayzlin, 2006; Liu, 2006; Dellarocas et al., 2007; Ghose et al., 2012). In addition, some studies have explored the textual content of reviews with the aim of extracting product design features (Archak et al., 2011). The current paper involves a relatively large and unique data set of consumer generated information regarding unprofessional repair experiences. The nature of the study suggests that data mining approaches can pave the way to retrieve hidden patterns in consumer repair behavior and the corresponding relationships with the purchase behavior. Extraction of such knowledge can provide fruitful managerial insights.

To summarize, the review of literature illustrates that data mining is a promising tool to study the consumer repair stories generated from the under-study survey. The data mining techniques help us derive the consumer attitude toward repair, the most frequent repair and <sup>fi</sup>x stories and further the degree of reparability of different electronics.

## 3. Text analytics

Although there is still ongoing research on the correlation between semantic structure of the user-generated textual information and users' actual effective states (Munoz and Tucker, 2016), the usefulness of the consumer-generated information has been already proved in the literature (Ghose and Ipeirotis, 2011), (Forman et al., 2008). Quite recently, some research has focused on extracting knowledge from the textual content of this information. These studies obtained different types of information from the consumer product reviews and investigated their corresponding impact on updating consumers' beliefs and product sales (Archak et al., 2011). The same approach is utilized in this study. We aim to analyze the individual consumer's experience of repair and reparability via examining consumer narratives about actual break or <sup>fi</sup>x stories. Upon successful extraction of useful information, the consumers' experience has been connected to their purchase decisions.

## 3.1. Dataset: consumer narratives of repair experience

A unique data set of 4210 consumer experiences of repairing electronics collected by iFixit.com has been examined. The consumers' stories of breaking or <sup>fi</sup>xing products have been captured through a survey. The following question has been asked from iFixit users:

What is your craziest <sup>fi</sup>x story? (A crazy break story is OK as well)

The fact that people were asked about their crazy stories and not typical ones has several consequences. It motivates them to express more personal experiences that reveal actual challenges and issues in the product repair and avoid typical failure-warranty information. On the other hand, this makes data processing more dif<sup>fi</sup>cult, since the proportion of unrelated and useless information increases in the survey.

Several analyses have been undertaken with the aim of answering the following questions:

What are the top failure stories reported by consumers (e.g. broken screen in iPad and iPhone 4s)?

What was the cause of failures (product failed, broken accidentally, water damage)?

What are the common repair practices and the spare parts needed and how do they correlate with design features?

What are the consumers' attitudes toward <sup>fi</sup>xing different types of products, types of failure, or the availability of spare parts?

The general steps of analysis to be run on the dataset include: 1) code the narratives into four categories of break stories, break then <sup>fi</sup>x stories, <sup>fi</sup>x stories and break while <sup>fi</sup>xing stories, 2) conduct word count analyses to identify the vocabulary used by consumers, 3) identify the frequency distribution of different terms in the vocabulary across the stories, 4) construct speci<sup>fi</sup>c hypotheses and then explore the presence or absence of evidence to test those hypotheses. Part of speech tagging (POS) and text classi<sup>fi</sup>cation are among data mining techniques that have been employed for text categorization.

After cleaning the data and eliminating the missing values, 3328 unique stories were selected. We read and examined the stories to differentiate them based on the subject. Four distinct categories have been identi<sup>fi</sup>ed: 1- Break: stories that directly express a product failure. 2- Break then <sup>fi</sup>x: stories that present a product failure and a subsequent <sup>fi</sup>x. 3- Fix: stories that directly describe a product <sup>fi</sup>x. 4- Break while <sup>fi</sup>xing: stories that present a product failure while the subject was <sup>fi</sup>xing or upgrading a product. Table 1 represents the frequency of each story type.

Table 1  
Frequency of each story.

<table><tr><td>Story type</td><td>Frequency</td></tr><tr><td>Break</td><td>1461</td></tr><tr><td>Fix</td><td>1183</td></tr><tr><td>Break then fix</td><td>552</td></tr><tr><td>Break while fixing</td><td>132</td></tr><tr><td>Total stories</td><td>3328</td></tr></table>

## 3.2. Textual information extraction

The next step is to extract the products, components, failure causes (or types) and the repair activities from each story. One of the most popular methods to extract the products and their features from a text is to use a Part Of Speech (POS) tagger (Archak et al., 2011; Liu et al., 2005). This method provides different ratios for each word to identify whether the word is a verb, noun, or adjective. While nouns would be good candidates for products and components, verbs can represent activities. Another method is to examine the frequency of each word in the text to <sup>fi</sup>nd the statistical patterns and to further identify product features (Archak et al., 2011). A hybrid method has been used in this study to extract our target information from the narratives. First a POS tagger has been applied to separate nouns and verbs. Then, the occurrence frequency of each term has been calculated to identify the products, components and their corresponding story in the text. It should be noted that, in practice, people use a vast variety of words, phrases and structures to express the same opinion. For instance, the words “shattered”, “smashed” and “cracked” convey the same meaning. Another case can be the tense of verbs. The two stories “I had broken my phone and I <sup>fi</sup>xed it” and “My phone broke and I repaired it” basically reveal the same information. In addition, different components of a product can be categorized into the same group, even though they are technically different. “Screen”, “display” and “digitizer” can be used interchangeably, although they are not the exact same component. Therefore, a dictionary has been constructed based on the frequent terms in order to cluster similar components or opinions into the same groups.

After preprocessing the texts to eliminate the stop words (e.g. ‘the’, ‘who’), pronouns etc., a dictionary has been created to prune the unnecessary words from each story. The dictionary contains 3904 terms that do not convey useful information or do not occur frequently in the stories. The stories are <sup>fi</sup>ltered based on the terms in the dictionary. In addition, one word has been chosen from tokens with similar meaning and the terms have been replaced accordingly. Therefore, after preprocessing, each story is converted to several key words that de<sup>fi</sup>ne the product, component and what happened to them. Finally, we kept a total of 30 terms including different products, product features and activities that occurred frequently in the stories. Table 2 represents the <sup>fi</sup>nal most frequent features.

The result of analysis reveals that the most frequent failure types or causes of failure were either that the product was dropped or cracked or had some sort of water damage. On the other hand, the most frequent repair activities done by the consumers were part replacement, disassembling or cleaning the product. Table 2 represents the results of analysis.

The performance of information retrieval process from the user-generated stories has been evaluated through employing precision, recall and F-measure metrics. In order to do so, 100 random stories have been examined from the dataset and the corresponding values for the attributes (i.e. product, component, failure cause, and repair activity) have been compared to the result of our information retrieval technique. These metrics have

Extracted features and their frequency in each story type.

<table><tr><td rowspan="2" colspan="2">Story type</td><td colspan="5">Occurrence</td></tr><tr><td>Break</td><td>Fix</td><td>Break and fix</td><td>Break while fixing</td><td>All stories</td></tr><tr><td rowspan="9">Product</td><td>iPhone</td><td>272</td><td>107</td><td>127</td><td>34</td><td>540</td></tr><tr><td>mac</td><td>112</td><td>137</td><td>109</td><td>14</td><td>372</td></tr><tr><td>phone</td><td>168</td><td>40</td><td>76</td><td>12</td><td>296</td></tr><tr><td>laptop</td><td>93</td><td>75</td><td>55</td><td>10</td><td>233</td></tr><tr><td>iPod</td><td>110</td><td>51</td><td>40</td><td>17</td><td>218</td></tr><tr><td>computer</td><td>52</td><td>37</td><td>26</td><td>4</td><td>119</td></tr><tr><td>iPad</td><td>68</td><td>18</td><td>18</td><td>6</td><td>110</td></tr><tr><td>camera</td><td>26</td><td>19</td><td>13</td><td>5</td><td>63</td></tr><tr><td>tv</td><td>20</td><td>29</td><td>3</td><td>1</td><td>53</td></tr><tr><td rowspan="10">Component</td><td>screen</td><td>335</td><td>141</td><td>177</td><td>55</td><td>708</td></tr><tr><td>part</td><td>51</td><td>121</td><td>65</td><td>10</td><td>247</td></tr><tr><td>board</td><td>42</td><td>99</td><td>42</td><td>17</td><td>200</td></tr><tr><td>battery</td><td>45</td><td>62</td><td>47</td><td>17</td><td>171</td></tr><tr><td>power</td><td>56</td><td>61</td><td>24</td><td>6</td><td>147</td></tr><tr><td>case</td><td>57</td><td>34</td><td>33</td><td>7</td><td>131</td></tr><tr><td>cable</td><td>25</td><td>43</td><td>14</td><td>17</td><td>99</td></tr><tr><td>button</td><td>20</td><td>32</td><td>15</td><td>17</td><td>84</td></tr><tr><td>keyboard</td><td>23</td><td>16</td><td>39</td><td>3</td><td>81</td></tr><tr><td>fan</td><td>18</td><td>28</td><td>8</td><td>2</td><td>56</td></tr><tr><td rowspan="3">Failure cause</td><td>drop</td><td>342</td><td>29</td><td>118</td><td>9</td><td>498</td></tr><tr><td>water damage</td><td>150</td><td>46</td><td>98</td><td>1</td><td>295</td></tr><tr><td>crack</td><td>173</td><td>29</td><td>66</td><td>15</td><td>283</td></tr><tr><td rowspan="3"> $Repair\ activity^a$ </td><td>Replace</td><td>75</td><td>249</td><td>140</td><td>28</td><td>492</td></tr><tr><td>disassemble</td><td>41</td><td>100</td><td>72</td><td>19</td><td>232</td></tr><tr><td>clean</td><td>18</td><td>49</td><td>45</td><td>4</td><td>116</td></tr></table>

<sup>a</sup> Although replacement and cleaning may also need disassembly to some extent, users have used these terms separately in their stories.  
been de<sup>fi</sup>ned as follows:

## precision

Number of attributes correctly extraxted to be present 二 Total number of attributes extracted to be present

(1)

## recall

Number of attributes correctly extraxted to be present Number of actual attributes present

(2)

$$
F - \text { measure } = \frac {2 * \text { precision } * \text { recall }}{\text { precision } + \text { recall }}\tag{3}
$$

While precision determines how many of the extracted attributes are actually relevant, recall shows how many of the actual present attributes have been extracted. F-measure represents the harmonic balance between the two metrics. The resulting values for the above mentioned metrics are as follows: Precision 76.8, Recall 77.2, F-measure 76.0.

It has already been shown in the literature that these values can be accepted as good scores in the textual content information retrieval domain (Archak et al., 2011). Unlike cases in which respondents answer survey questions with numeric responses, automatically capturing information from free text format is signi<sup>fi</sup>cantly more dif<sup>fi</sup>cult as people use a variety of <sup>fi</sup>gures of speech to express their experiences. Our case is especially more dif<sup>fi</sup>cult compared to studies focused on text mining of product reviews such as Archak et al. (2011), Ghose and Ipeirotis (2011), Forman et al. (2008), as in those cases the contents of the texts were directly about speci<sup>fi</sup>c product features. However, in consumers' narratives of product break or repair experiences, we observed more implicit speaking and sarcasm. For example “Fixed a supposed broken camera. It was a very small one, with “millions” of very small screws!!!” implies that the consumer disassembled the product. However, no POS tagger, parser or other technique can capture that.

Fig. 1 illustrates the frequency of each extracted attribute per each story type. As can be seen in Fig. 1 and Table 2, the most frequent failed product is “iPhone”; however, the most frequent <sup>fi</sup>xed item is “Mac”, which represents MacBook, MacBook Pro, etc. This can be due to the design features of these products, for instance the openability of the devices and their ease of repair. However, the results imply that the majority of respondents were iPhone users and it does not necessarily show the comparison of ease-of-repair between iPhone and other types of phone. In addition, it can be drawn from Fig. 1 that the terms ‘screen’, ‘drop’ and ‘replace’ or their equivalents have been repeated many times in the break and <sup>fi</sup>x stories respectively. This repetition may indicate that screen breaks due to dropping the product and replacing the broken parts are the most common.

In order to identify the corresponding pairs of productcomponent failure and pairs of failure type-repair activity, the ngrams have been generated. Table 3 represents the most frequent 2-grams in the stories.

Figs. 2 and 3 compare the failure types and the most common repair practices for the top <sup>fi</sup>ve most frequent products. Interestingly, Fig. 2 implies that while ‘drop and subsequent cracking’ is more common among smaller handheld devices, water damage is relatively more common in larger products, such as computers and laptops.

![](images/8eefa58b01180ffa716ee80d0b91fdcfc5c07364fd1b66b5542d95a991dddef5.jpg)  
(a)

![](images/28f22f16b9d03e55bcaab110b9a1af42c83555473a4f4dff3598f48b599cca5e.jpg)

![](images/81fa679bd35716e7b21df2d18b7de2599353f3eba2b88c729fd3acc50f346668.jpg)  
(c)

![](images/18cc416a56fa87efb8350d7b1891747651c6f494f755594bc6709c87e8ab1987.jpg)  
(d)  
Fig. 1. Frequency of extracted attributes per each story type. (a) Products (b) Components (c) Failure type (d) Repair activity.

Fig. 3 represents the fact that the most common repair practice by individuals is replacement. This may imply that complicated component repairs are beyond the expertise of unprofessional individuals. Moreover, disassembly and cleaning seems to be more often done for larger devices such as computers, which require less complex disassembly.

Fig. 4 shows the most frequent failed/<sup>fi</sup>xed components of the top <sup>fi</sup>ve most frequent products. It can be seen that despite the recent technology advancements in screen and battery design, still, they are the most commonly failed components. In addition, we observe a drastic increase in failed boards in more complex products such as laptops and computers. Since the most common repair practice by unprofessional individuals is replacement, these results imply that upon availability of a robust supply chain for spare parts, the consumers' participation in repair may increase.

Table 3  
High frequency 2-grams in each story type.

<table><tr><td rowspan="2">2-gram</td><td colspan="5">Occurrence</td></tr><tr><td>Break</td><td>Fix</td><td>Break and fix</td><td>Break while fixing</td><td>Total</td></tr><tr><td>Screen_crack</td><td>51</td><td>5</td><td>16</td><td>4</td><td>76</td></tr><tr><td>Drop_iphone</td><td>45</td><td>1</td><td>21</td><td>0</td><td>67</td></tr><tr><td>Drop_phone</td><td>43</td><td>0</td><td>13</td><td>0</td><td>56</td></tr><tr><td>Replace_screen</td><td>9</td><td>17</td><td>18</td><td>6</td><td>50</td></tr><tr><td>iPhone_drop</td><td>31</td><td>4</td><td>14</td><td>0</td><td>49</td></tr><tr><td>Drop_screen</td><td>30</td><td>1</td><td>6</td><td>1</td><td>38</td></tr><tr><td>Laptop_screen</td><td>14</td><td>11</td><td>10</td><td>1</td><td>36</td></tr><tr><td>iPod_screen</td><td>14</td><td>6</td><td>10</td><td>3</td><td>33</td></tr><tr><td>Screen_replace</td><td>8</td><td>7</td><td>15</td><td>2</td><td>32</td></tr><tr><td>iPad_screen</td><td>17</td><td>5</td><td>6</td><td>3</td><td>31</td></tr><tr><td>Screen_iphone</td><td>10</td><td>6</td><td>7</td><td>6</td><td>29</td></tr></table>

![](images/626046d29e236a7ae9d7028b8ff7c21292bfe5ba178c610848bd4474bb990187.jpg)  
Fig. 2. Frequency of the cause of failure for the most frequent products.

![](images/5dc52b372ef11466f48e13fa2c1aed40fe40ad9c02138e008f5f0f0aa59da4df.jpg)  
Fig. 3. Frequency of different repair activities for the most frequent products.

![](images/80f46e250ef90e3ce9367ce570dcd0c439aad77b2060ebc67c7ae6de81dce87d.jpg)  
Fig. 4. Failed/<sup>fi</sup>xed components frequency per product.

## 4. Impact of consumer experiences of repair on future purchase decisions

The information extracted from consumer narratives has been further employed to study the impact of individuals' repair experiences on their future purchase decisions. Speci<sup>fi</sup>cally, we are interested to see if there are any correlations between successful repair experiences and decisions regarding repurchasing from the same brand or recommending it to others. In order to obtain this information, two questions have been asked in the survey:

(1) Have your experiences <sup>fi</sup>xing your own products impacted the purchasing recommendations you give to your friends?

(2) If you successfully repaired a product, are you more likely to buy new products from the same company in the future?

Note that the second question asks about future purchasing decisions from the same brand and not necessarily the same product. This relates to the point that the reparability of a product can be a proper indicator of reliability, which in<sup>fl</sup>uences consumer loyalty to the brand.

To test whether there is a correlation between the consumers' previous repair experiences and the new product purchase decisions, four hypotheses have been derived:

It would be rational to expect a correlation between the repair expenses and consumers' attitude toward that repair experience. The repair experience can also affect the future purchase decisions accordingly. Thus, H<sub>1</sub>: Repair expenses spent by the consumers have significant impact on future purchase decisions or recommendations.

Repair can be a time consuming and dif<sup>fi</sup>cult procedure, which may affect consumer's attitude toward a certain product or brand. For instance, repairing a glue-based design may take much longer compared with a screw-based design. Such experiences may bring unwillingness to consumers in regard to possible future purchases. Hence, the ease of repair should be an important factor for consumers' future purchase and recommendation decisions. Since different products can be different in convenience of repair and the product type can be an indication of repair convenience, H : The type of repaired product has a significant impact on consumers' future purchase or recommendation decisions.

Even for the same product, the convenience of repair can vary over the components due to complexities in disassembly, replacement etc. Thus, H : The type of component repaired has a significant impact on consumers' future purchase or recommendation decisions.

Dif<sup>fi</sup>culty of repair can be a subjective matter. Users' propensity toward repair may change the perceived inconvenience of repair. Hence, H : Consumers' attitude toward repair has a significant impact on consumers' future purchase or recommendation decisions.

The second question refers to successful repairs. For consistency, we have selected the stories representing successful <sup>fi</sup>xes (Fix and Break then <sup>fi</sup>x stories) in order to study the impact of consumer repair experiences on future purchase decisions. A total 1735 observations have been <sup>fi</sup>nally selected. Fig. 5 represents a histogram of the respondents' answers to the above mentioned questions on future purchase and recommendation decisions (dependent variables). The respondents had three ordered options to choose from. Not at all, Somewhat and Absolutely for the <sup>fi</sup>rst question and Never, Sometimes and Often for the second question.

To test the above mentioned hypotheses, a regression model has been constructed. The following <sup>fi</sup>elds of data are needed: types of repaired products, components and repair activities. In addition to the attributes extracted from the stories, data for repair cost and consumers' attitude toward repair have been collected in the survey in order to capture the heterogeneity of observations. The question ‘Would you ever consider starting your own repair business?’ captures the consumers' attitude toward return. Table 4 summarizes the questions and parameters in the model.

Both dependent variables have an ordinal nature. The relationship between the response variables has been tested using $\iota \chi ^ { 2 }$ test. The outcome p-value and $\chi ^ { 2 }$ value were found to be 0.000 and 233.133 respectively. These results endorse a strong correlation between recommendations and repurchase decisions. Hence, a bivariate analysis is required to infer the data. Therefore, due to the ordinal categorical nature of the responses, consumers' future recommendation and purchase decisions can be estimated using a bivariate ordered probit regression model (Greene and Hensher, 2010):

$$
y _ {i, 1} = \beta_ {i, 1} X _ {i, 1} + \varepsilon_ {i, 1}, y _ {i, 1} = p \text {   if   } t _ {p - 1} <   y _ {i, 1} <   t _ {p}, p = 0, 1, 2\tag{4}
$$

![](images/1cfcd38b31db8874beb924b80804522a6d24281b90bb93ecf68eb040c2a0dc21.jpg)  
Fig. 5. Histogram of the dependent variables. (1) Recommend (2) Repurchase.

Table 4  
Descriptive Statistics of model variables.

<table><tr><td>Variables</td><td>Mean</td><td>Standard deviation</td></tr><tr><td colspan="3">Repair cost</td></tr><tr><td>How much did you spend on repairs last year?</td><td></td><td></td></tr><tr><td>Group 1 (1 if cost &lt;$20, 0 otherwise)</td><td>0.065</td><td>0.247</td></tr><tr><td>Group 2 (1 if $20 &lt; cost &lt;$200, 0 otherwise)</td><td>0.383</td><td>0.486</td></tr><tr><td>Group 3 (1 if $200 &lt; cost &lt;$500, 0 otherwise, 0 otherwise)</td><td>0.235</td><td>0.424</td></tr><tr><td>Group 4 (1 if %500 &lt; cost &lt;$1000, 0 otherwise, 0 otherwise)</td><td>0.103</td><td>0.304</td></tr><tr><td>Group 5 (1 if the cost &gt;$1000, 0 otherwise)</td><td>0.118</td><td>0.323</td></tr><tr><td colspan="3">Repair propensity</td></tr><tr><td>Would you ever consider starting your own repair business? (1 if Yes, 0 otherwise)</td><td>0.537</td><td>0.499</td></tr><tr><td colspan="3">Product</td></tr><tr><td>Camera (1 repaired product was camera, 0 otherwise)</td><td>0.018</td><td>0.135</td></tr><tr><td>Computer (1 repaired product was computer, 0 otherwise)</td><td>0.036</td><td>0.187</td></tr><tr><td>iPad (1 repaired product was iPad, 0 otherwise)</td><td>0.021</td><td>0.143</td></tr><tr><td>iPhone (1 repaired product was iPhone, 0 otherwise)</td><td>0.135</td><td>0.342</td></tr><tr><td>iPod (1 repaired product was iPod, 0 otherwise)</td><td>0.052</td><td>0.223</td></tr><tr><td>Laptop (1 repaired product was Laptop, 0 otherwise)</td><td>0.075</td><td>0.263</td></tr><tr><td>Phone (1 repaired product was Phone, 0 otherwise)</td><td>0.067</td><td>0.250</td></tr><tr><td>TV (1 repaired product was TV, 0 otherwise)</td><td>0.018</td><td>0.135</td></tr><tr><td>Mac (1 repaired product was Mac, 0 otherwise)</td><td>0.142</td><td>0.349</td></tr><tr><td colspan="3">Component</td></tr><tr><td>Battery (1 repaired component was battery, 0 otherwise)</td><td>0.063</td><td>0.243</td></tr><tr><td>Board (1 repaired component was board, 0 otherwise)</td><td>0.081</td><td>0.273</td></tr><tr><td>Button (1 repaired component was button, 0 otherwise)</td><td>0.027</td><td>0.162</td></tr><tr><td>Cable (1 repaired component was cable, 0 otherwise)</td><td>0.033</td><td>0.178</td></tr><tr><td>Case (1 repaired component was case, 0 otherwise)</td><td>0.039</td><td>0.193</td></tr><tr><td>Fan (1 repaired component was fan, 0 otherwise)</td><td>0.021</td><td>0.143</td></tr><tr><td>Keyboard (1 repaired component was keyboard, 0 otherwise)</td><td>0.032</td><td>0.175</td></tr><tr><td>Power (1 repaired component was power, 0 otherwise)</td><td>0.049</td><td>0.216</td></tr><tr><td>Screen (1 repaired component was screen, 0 otherwise)</td><td>0.183</td><td>0.387</td></tr><tr><td>Unknown part (1 repaired component was unknown part, 0 otherwise)</td><td>0.107</td><td>0.309</td></tr><tr><td colspan="3">Repair activity type</td></tr><tr><td>Cleaning (1 repair activity included cleaning, 0 otherwise)</td><td>0.054</td><td>0.226</td></tr><tr><td>Disassembly (1 repair activity included disassembly, 0 otherwise)</td><td>0.099</td><td>0.299</td></tr><tr><td>Replace (1 repair activity included replacement, 0 otherwise)</td><td>0.224</td><td>0.417</td></tr></table>

$$
y _ {i, 2} = \beta_ {i, 2} X _ {i, 2} + \varepsilon_ {i, 2}, y _ {i, 2} = p \text {   if   } T _ {p - 1} <   y _ {i, 1} <   T _ {p}, p = 0, 1, 2\tag{5}
$$

where X is the vector of input variables, b is the vector of estimate parameters, t and T are thresholds which de<sup>fi</sup>ne the dependent variables, y represents the integer ordering, p is the ordered choice and <sup>ε</sup> is the error term. The error terms for the dependent variables are cross-correlated:

$$
\binom{\varepsilon_ {i, 1}}{\varepsilon_ {i, 2}} \sim N \bigg [ \binom{0}{0}, \left( \begin{array}{c c} 1 & \rho \\ \rho & 1 \end{array} \right) \bigg ]\tag{6}
$$

Then the probability of each outcome is de<sup>fi</sup>ned as:

(f is the standard normal cumulative distribution function)

$$
\begin{array}{c} P \Big (y _ {i, 1} = p, y _ {i, 2} = q | X _ {i, 1}, X _ {i, 2} \Big) \\ = \left[ \begin{array}{c} \phi_ {2} \big [ (T _ {j} - \beta_ {i, 1} X _ {i, 1}), (t _ {k} - \beta_ {i, 2} X _ {i, 2}), (\rho) \big ] \\ - \phi_ {2} \big [ (T _ {j - 1} - \beta_ {i, 1} X _ {i, 1}), (t _ {k} - \beta_ {i, 2} X _ {i, 2}), (\rho) \big ] \end{array} \right] \\ - \left[ \begin{array}{c} \phi_ {2} \big [ (T _ {j} - \beta_ {i, 1} X _ {i, 1}), (t _ {k - 1} - \beta_ {i, 2} X _ {i, 2}), (\rho) \big ] \\ - \phi_ {2} \big [ (T _ {j - 1} - \beta_ {i, 1} X _ {i, 1}), (t _ {k - 1} - \beta_ {i, 2} X _ {i, 2}), (\rho) \big ] \end{array} \right] \end{array}\tag{7}
$$

The model has been tested for all the variables. All the possible variable interactions and the statistically signi<sup>fi</sup>cant variables with 90% con<sup>fi</sup>dence level are presented in Table 5. Repurchase has 6 different signi<sup>fi</sup>cant explanatory parameters, while Recommend has 9. Among the total 15 signi<sup>fi</sup>cant variables, 4 of them are common between the two models.

Note that a positive value for the corresponding coef<sup>fi</sup>cients indicates that increasing X increases the probability of the last outcome. In addition to model estimation results, sample meanmarginal effects are also calculated for signi<sup>fi</sup>cant variables in order to illustrate the impact of each of them on the dependent variables (Table 6).

$$
\frac {\partial P (y = n = 0 , 1 , 2)}{\partial X} = \beta [ \phi (\tau_ {n - 1} - \beta X) - \phi (\tau_ {n} - \beta X) ]\tag{8}
$$

which t represents the thresholds.

Referring back to the <sup>fi</sup>rst hypothesis, surprisingly, in the repair cost category, only the <sup>fi</sup>rst group (<\$20) is found to have a signi<sup>fi</sup>cant impact on the individuals' recommendations. In addition, the so-called variable carried signi<sup>fi</sup>cance with opposite sign to the dependent variable. This may be due to the fact that the answers to the repair cost question may not be necessarily related to the exact <sup>fi</sup>xed stories used in the analysis. The question asks for the repair costs spent in the last year; however, the narrative may be for another time and product. In addition, this group (<\$20) may also be capturing those individuals who spend nothing related to repair cost, because of the fact that they are not willing to repair; thus, they would not recommend the product to others.

Both the repaired product and the repaired component are found to be signi<sup>fi</sup>cant parameters for the model. Therefore, we cannot reject the second and third hypotheses. Based on the results of the model, those individuals who have a successful experience repairing iPhone, iPod and Laptop are more likely to recommend them. This is in line with the fact that successful repair experiences can improve the perceived reliability level of the product. Moreover, the variable representing board is signi<sup>fi</sup>cant with opposite sign. Since, in the electronics industry, the circuit board is one of the most advanced components that usually require a high level of disassembly, this variable may be capturing the component with

Table 5  
Model estimation results.

<table><tr><td rowspan="2">Variables</td><td colspan="2">Repurchase</td><td colspan="2">Recommend</td></tr><tr><td>Coefficient</td><td>P-value</td><td>Coefficient</td><td>P-value</td></tr><tr><td colspan="5">Repair cost</td></tr><tr><td>How much did you spend on repairs last year?</td><td></td><td></td><td></td><td></td></tr><tr><td>Group 1 (1 if the cost is less than $20, 0 otherwise)</td><td></td><td></td><td>-0.302</td><td>0.004</td></tr><tr><td>Group 2 (1 if the cost is more than $20 but less than $200, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Group 3 (1 if the cost is more than $200 but less than $500, 0 otherwise, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Group 4 (1 if the cost is more than $500 but less than $1000, 0 otherwise, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Group 5 (1 if the cost is more than $1000, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Repair propensity</td></tr><tr><td>Would you ever consider starting your own repair business? (1 if Yes, 0 otherwise)</td><td>0.178</td><td>0.002</td><td>0.416</td><td>&lt;0.0001</td></tr><tr><td colspan="5">Product</td></tr><tr><td>Camera (1 repaired product was camera, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Computer (1 repaired product was computer, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>iPad (1 repaired product was iPad, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>iPhone (1 repaired product was iPhone, 0 otherwise)</td><td></td><td></td><td>0.133</td><td>0.090</td></tr><tr><td>iPod (1 repaired product was iPod, 0 otherwise)</td><td></td><td></td><td>0.273</td><td>0.023</td></tr><tr><td>Laptop (1 repaired product was Laptop, 0 otherwise)</td><td></td><td></td><td>0.251</td><td>0.015</td></tr><tr><td>Phone (1 repaired product was Phone, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>TV (1 repaired product was TV, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Mac (1 repaired product was Mac, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Component</td></tr><tr><td>Battery (1 repaired component was battery, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Board (1 repaired component was board, 0 otherwise)</td><td>-0.189</td><td>0.052</td><td></td><td></td></tr><tr><td>Button (1 repaired component was button, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Cable (1 repaired component was cable, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Case (1 repaired component was case, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Fan (1 repaired component was fan, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Keyboard (1 repaired component was keyboard, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Power (1 repaired component was power, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Screen (1 repaired component was screen, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Unknown part (1 repaired component was unknown part, 0 otherwise)</td><td>0.226</td><td>0.012</td><td></td><td></td></tr><tr><td colspan="5">Repair activity type</td></tr><tr><td>Cleaning (1 repair activity included cleaning, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Disassembly (1 repair activity included disassembly, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr><tr><td>Replace (1 repair activity included replacement, 0 otherwise)</td><td></td><td></td><td></td><td></td></tr></table>

## Table 6

Sample-mean marginal effects.

<table><tr><td rowspan="2">Variables</td><td colspan="3">Repurchase</td><td colspan="3">Recommend</td></tr><tr><td>Not at all</td><td>Somewhat</td><td>Absolutely</td><td>Never</td><td>Sometimes</td><td>Often</td></tr><tr><td colspan="7">Repair cost</td></tr><tr><td>How much did you spend on repairs last year?</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Group 1 (1 if the cost is less than $20, 0 otherwise)</td><td></td><td></td><td></td><td>0.049</td><td>0.063</td><td>-0.112</td></tr><tr><td colspan="7">Repair propensity</td></tr><tr><td>Would you ever consider starting your own repair business? (1 if Yes, 0 otherwise)</td><td>-0.017</td><td>-0.053</td><td>0.070</td><td>-0.067</td><td>-0.087</td><td>0.154</td></tr><tr><td colspan="7">Product</td></tr><tr><td>iPhone (1 repaired product was iPhone, 0 otherwise)</td><td></td><td></td><td></td><td>-0.021</td><td>-0.028</td><td>0.049</td></tr><tr><td>iPod (1 repaired product was iPod, 0 otherwise)</td><td></td><td></td><td></td><td>-0.044</td><td>-0.057</td><td>0.101</td></tr><tr><td>Laptop (1 repaired product was Laptop, 0 otherwise)</td><td></td><td></td><td></td><td>-0.041</td><td>-0.052</td><td>0.093</td></tr><tr><td colspan="7">Component</td></tr><tr><td>Board (1 repaired component was board, 0 otherwise)</td><td>0.018</td><td>0.057</td><td>-0.075</td><td></td><td></td><td></td></tr><tr><td>Unknown part (1 repaired component was unknown part, 0 otherwise)</td><td>-0.022</td><td>-0.068</td><td>0.090</td><td></td><td></td><td></td></tr></table>

the lowest level of repair convenience. Thus, those individuals who repaired a circuit board may have endured a dif<sup>fi</sup>cult procedure and are not willing to buy from the same brand again.

Interestingly, the variable representing those respondents with more willingness toward repair (i.e. participants who consider starting a repair business) results in a signi<sup>fi</sup>cant parameter with positive sign for both models. This will validate our fourth hypothesis: the more an individual is willing to repair a product, the more likely he is to recommend or repurchase from the same brand upon successful repair.

Moving to the variables representing the type of actual repair activities (cleaning, disassembly, replace), we see no signi<sup>fi</sup>cant effect on the dependent variables. However, this may imply the point that despite the consumers' perceived distinction between common repair activities, they mostly describe the same scenario (i.e. to open, then disassemble, then clean/replace etc.) and have the same impact.

## 5. Discussion

This paper strives to gain managerial insights on consumer repair practices and their economic consequences via directly analyzing consumer narratives about their experiences of repairing electronics. The results will shed light on the actual repair challenges in consumer electronics and consumers' viewpoints toward them.

Among consumer electronics, more popular items such as cell phones, personal computers and laptops were found to be more frequent to fail/be repaired. The <sup>fi</sup>ndings disclose that the majority of consumer oriented failures happen by some sort of impact or water damage. The policy makers who are concerned with sustainability or warranty issues have the opportunity to improve lengthening the life span of products by supporting durable designs with respect to impact and water damage. In addition, the results of the study suggest that disassembly inconvenience and spare parts shortage are among the dominant barriers toward consumer repairs. Therefore, consideration of design-fordisassembly, coupled with a robust network of spare parts supply, may alleviate the current shortcoming and facilitate repair. This fact is in line with the <sup>fi</sup>ndings in Rosner and Ames (2014). The pro<sup>fi</sup>le of failed/replaced components suggest that some components are more prone to be failed (i.e., screen) due to consumers misuse. Therefore, the subsequent demand for the corresponding spare parts will be higher.

The type of failure/repair practices also shows some extent of correspondence to the product size. Dropping/breaking was found to be more frequent in the handheld devices, while larger proportions were observed for the water damage in bigger products like computers. Similarly, simple cleaning were found to be more operational and effective in larger products. This may capture the point that the repair convenience has a negative correlation with the product size.

Furthermore, possible links between consumer repair experiences and their future purchase behaviors have been analyzed via regression analysis. Empirical repair expense, repair propensity, types of repaired products and components, failure and repair activities have been considered as possible variables affecting the future purchase decisions. The results suggest that consumers who have not spent much on the repair during the past year are less likely to recommend the repaired product to others. We believe that this may represent the behavior of those who are not willing to spend on repair, and therefore, the failure of the product acts as a signal of product unreliability for them before any repair practices take place. On the other hand, the results are aligned with the hypothesis regarding the product type. Those consumers who have successfully repaired a product appear to be likely to recommend it to others, as the repairability of the product may increase its perceived quality and reliability for the consumer.

Previous literature suggests that non-monetary costs of repair, such as repair convenience, may in<sup>fl</sup>uence the consumer propensity to repair (Scott and Weaver, 2014). Our results are keeping up with the literature, such that we observe those who have repaired more complex components (i.e., board) are less likely to purchase the same product again. In contrast, those who have mentioned to have had repaired a general type of components show willingness to repurchase the product. The comparison suggests that the convenience of repair can signi<sup>fi</sup>cantly affect the consumers' decision.

It should be acknowledged that the current structure of the conducted survey may limit the generalization of the results. The future work can improve the insights extracted from the results of this work in the following aspects:

Including the socio-demographic information in the survey design may elevate the performance of any subsequent regression analyses. Particularly, it can improve the generality of the results and the predictive ability of the proposed models.

Designing more direct questions regarding the consumers repair experiences and purchase behavior obviates the challenges in information extraction from free-form textual narratives and therefore improve the quality of the applied analyses.

Targeting different consumer populations allows for more interpopulation comparisons, in contrast to the current intrapopulation analyses, of the linkages between repair experiences and the future purchase behavior.

## 6. Conclusion

Consumer participation in repair may increase the total life span of electronics and ameliorate the worrying increase in e-waste generation rate. Therefore, it is necessary to gain a clear understanding of the in<sup>fl</sup>uential factors that shape individual consumer's repair propensity. In addition, manufacturers might be interested to see the economic impact of consumers' successful experience of repair on their future purchase decisions.

In this study, a total of 4210 repair and break narratives reported by individuals who had been surveyed by iFixit.com has been investigated so as to extract some insights regarding the most frequent failed products and components in the electronics industry and further identify the factors that shape consumers' repair experience and future purchase and recommendation decision. A text mining procedure has been applied on the stories to derive information on the top failure stories, most common repair practices by individuals, and most failed components and products. It has been shown that handheld electronic devices, personal computers and laptops are the most common failed products. The reasons behind these failures are mostly consumer oriented; for instance, dropping them and accidentally cracking or spilling water on them were found to be frequently cited reasons. Accordingly, the most failed component was found to be the screen. However, there is evidence that other factors such as design issues are important in the failure of components like the battery and the main board. The common repair activities operated by unprofessional individuals were found to be replacement, disassembly and cleaning. The results of frequency analysis show that upon parts availability many damaged products can be repaired by the inexperienced individuals; since, the most common repair practice seems to be replacement. Thus, a robust spare parts supply chain design will eventually contribute to more consumer participation in repair, which eventually lengthens the life span of electronics.

In addition, the possible connections between the repair experiences and consumers' future purchase behavior have been studied. It has been shown that consumers' attitude toward repair, elements which change the convenience of repair such as different product types, components and repair cost are signi<sup>fi</sup>- cant factors that contribute to the decision making process of consumers upon repurchasing or recommending speci<sup>fi</sup>c products or brands.

This work can be improved in different ways. The challenges regarding implicit <sup>fi</sup>gures of speech and sarcasm can be reduced by a more ef<sup>fi</sup>cient and more direct data collection method. Designing a well-targeted survey to collect data will increase the performance of text mining procedure utilized in this work. In addition, although prior research reveals a consistency between iFixit users and regular consumers in terms of the repair propensity (Scott and Weaver, 2014), it is still admissible to say iFixit users generally represent higher levels of repair propensity. Targeting other groups of individuals will increase the generality of the results.

## Acknowledgment

This material is based upon work supported by the National Science Foundation e USA under grant # CMMI-1435908. Any opinions, <sup>fi</sup>ndings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily re<sup>fl</sup>ect the views of the National Science Foundation.

## References

Ajukumar, V.N., Gandhi, O.P., Jul. 2013. Evaluation of green maintenance initiatives in design and development of mechanical systems using an integrated approach. J. Clean. Prod. 51, 34e46.

Archak, N., Ghose, A., Ipeirotis, P.G., 2011. Deriving the pricing power of product features by mining consumer reviews. Manage. Sci. 57 (no. 8), 1485e1509.

Anastas, P.T., Zimmerman, J.B., 2003. Design through the twelve principles of green engineering. Environ. Sci. Tech. 37 (5), 94Ae101A.

Batanov, D., Nagarur, N., Nitikhunkasem, P., 1993. EXPERT-MM: a knowledge-based system for maintenance management. Artif. Intell. Eng. 8, 283e291.

Behdad, S., Thurston, D., 2010. Disassembly process planning tradeoffs for product maintenance. In: ASME 2010 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference, pp. 427-434.

Bekin, C., Carrigan, M., Szmigin, I., 2007. Beyond recycling:‘commons-friendly waste reduction at new consumption communities. J. Consum. Behav. 6 (no. 5), 271e286.

Chen, J., Taylor, J.E., Wei, H.-H., 2011. Toward a Building Occupant Network Agentbased Model to Simulate Peer Induced Energy Conservation Behavior, pp. 883e890.

Chevalier, J.A., Mayzlin, D., 2006. The effect of word of mouth on sales: online book reviews. J. Mark. Res. 43, 345e354.

Cohen, M.A., Whang, S., 1997. Competing in product and service: a product life-cycle model. Manage. Sci. 43, 535.

Cohen, M.A., Zheng, Y.-S., Agrawal, V., Aug. 1997. Service parts logistics: a benchmark analysis. IIE Trans. 29 (no. 8), 627e639.

Cooper, T., 2005. Slower consumption. J. Ind. Ecol. 9 (no. 1e2), 51e68.

Dant, T., 2004. Materiality and Society. McGraw-Hill Education (UK).

Dellarocas, C., Zhang, X., Awad, N.F., 2007. Exploring the value of online product reviews in forecasting sales: the case of motion pictures I. Interact Mark 21 23e45.

Duan, W., Gu, B., Whinston, A.B., 2008. Do online reviews matter? - an empirical investigation of panel data. Decis. Support Syst. 45, 1007e1016.

Forman, C., Ghose, A., Wiesenfeld, B., 2008. Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets. Inf. Syst. Res. 19, 291e313.

Gadenne, D., Sharma, B., Kerr, D., Smith, T., Dec. 2011. The in<sup>fl</sup>uence of consumers environmental beliefs and attitudes on energy saving behaviours. Energy Policy 39 (no. 12), 7684e7694.

Garg, A., Deshmukh, S.G., 2006. Maintenance management: literature review and directions. J. Qual. Maint. Eng. 12 (no. 3), 205e238.

Gelbmann, U., Hammerl, B., Feb. 2014. Integrative re-use systems as innovative business models for devising sustainable producteservice-systems. J. Clean. Prod. 97, 50e60.

Ghose, A., Ipeirotis, P.G., 2011. Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics. IEEE Trans. Knowl. Data Eng. 23, 1498e1512.

Ghose, A., Ipeirotis, P.G., Li, B., 2012. Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Mark. Sci. 31, 493e520.

Pine II, B.J., Gilmore, J.H., 1998. Welcome to the experience economy. Harv. Bus. Rev. 76 (no. 4). 97–105.

Godes, D., Mayzlin, D., 2004. Using online conversations to study word-of-mouth communication Mark, Sci 23 545–560

Graham, S., Thrift, N., 2007. Out of order understanding repair and maintenance. Theory Cult. Soc. 24 (no. 3), 1e25.

Greene, W.H., Hensher, D.A., 2010. Modeling Ordered Choices: a Primer. Cambridge University Press.

Gregson, N., Metcalfe, A., Crewe, L., 2009. Practices of object maintenance and repair how consumers attend to consumer objects within the home. J. Consum. Cult. 9 (no. 2). 248–272.

Harding, J.a., Shahbaz, M., Kusiak, A., 2006. Data mining in manufacturing: a review. J. Manuf. Sci. Eng. 128 (no. 4), 969

Hartmann, P., Apaolaza-Ibanez, V., 2012. Consumer attitude and purchase intention toward green energy brands: the roles of psychological bene<sup>fi</sup>ts and environmental concern. J. Bus. Res. 65 (9), 1254e1263

Hatcher, G.D., Ijomah, W.L., Windmill, J.F.C., Jan. 2013. Integrating design for remanufacture into the design process: the operational factors. J. Clean. Prod. 39, 200e208.

Hsu, L.-F., Kuo, S., 1995. Design of optimal maintenance policies based on on-line sampling plans. Eur. J. Oper. Res. 86 (no. 2), 345e357.

Jack, N., Iskandar, B.P., Murthy, D.N.P., Feb. 2009. A repairereplace strategy based on usage rate for items sold with a two-dimensional warranty. Reliab. Eng. Syst.

Saf. 94 (no. 2), 611e617.

King, A.M., Burgess, S.C., Ijomah, W., McMahon, C.A., 2006. Reducing waste: repair, recondition, remanufacture or recycle? Sustain. Dev. 14 (no. 4), 257e267.

Koga, G.A., Maccari, E.A., Kniess, C.T., Ruiz, M.S., 2013. Consumer's Perception Regarding Recycling of Mobile Phones: a Prospective Assessment in the State of Sao Paulo, Brazil, pp. 2005e2016.

Kusiak, A., 1998. Modularity in design of products and systems. IEEE Trans. Syst. Man. Cybern. Part A Syst. Humans 28 (no. 1), 66e77.

Letorneau, S., Famili, F., Matwin, S., 1999. Data mining for prediction of aircraft component replacement. IEEE Intell. Syst. 14, 59e66.

Li, X., Jin, C., Ge, X., Wangying, 2013. Study of in<sup>fl</sup>uencing factors of household waste reduction behaviors in Beijing. Int. J. Appl. Environ. Sci. 8 (no. 5), 615e624.

Liu, Y., 2006. Word of mouth for movies: its dynamics and impact on box of<sup>fi</sup>ce revenue. J. Mark. 70, 74e89.

Liu, B., Hu, M., Cheng, J., 2005. Opinion observer: analyzing and comparing opinions on the web. In: Proceedings of the 14th International Conference on World Wide Web, pp. 342e351.

Majeskeat, K.D., Lynch-carisb, T., Herrinb, G., 1997. Production economics Evaluating product and process design changes with warranty data. Int. J. Prod. Econ. 50, 79e89.

Mashhadi, A.R., Esmaeilian, B., Behdad, S., 2015. Uncertainty management in remanufacturing decisions: a consideration of uncertainties in market demand, quantity, and quality of returns. ASCE-ASME J. Risk Uncertain. Eng. Syst. Part B Mech. Eng. 1 (no. 2), 21007.

Munoz, D., Tucker, C.S., Feb. 2016. Modeling the semantic structure of textually derived learning content and its impact on recipients' response states. J. Mech. Des. 138 (no. 4), 42001.

Murthy, D.N., Djamaludin, I., Oct. 2002. New product warranty: a literature review. Int. J. Prod. Econ. 79 (no. 3), 231e260.

Nnorom, I.C., Ohakwe, J., Osibanjo, O., Dec. 2009. Survey of willingness of residents to participate in electronic waste recycling in Nigeria e a case study of mobile phone recycling. J. Clean. Prod. 17 (no. 18), 1629e1637.

Pandey, V., Skowronska, A.G., Mourelatos, Z.P., Gorsich, D., Castanier, M., 2013. “Reliability and functionality of repairable systems using a minimal set of metrics: design and maintenance of a smart charging microgrid. In: ASME 2013 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. V03BT03A050eV03BT03A050.

Reim, W., Parida, V., Ortqvist, D., Jul. 2014. Product<sup>€</sup> eService Systems (PSS) business models and tactics e a systematic literature review. J. Clean. Prod. 97, 61e75.

Richins, M.L., 1983. Negative word-of-mouth by dissatis<sup>fi</sup>ed consumers: a pilot study. J. Mark. 68e78.

Rigopoulou, I.D., Chaniotakis, I.E., Lymperopoulos, C., Siomkos, G.I., 2008. After-sales service quality as an antecedent of customer satisfaction: the case of electronic appliances. Manag. Serv. Qual. 18, 512e527.

Romanowski, C.J., Nagi, R., 2001. Analyzing maintenance data using data mining methods. In: Data Mining for Design and Manufacturing. Springer, pp. 235e254.

Rosner, D.K., Ames, M., 2014. Designing for repair?: infrastructures and materialities of breakdown. In: Proceedings of the 17th ACM Conference on Computer Supported Cooperative Work & Social Computing, pp. 319e331.

Sabbaghi, M., Esmaeilian, B., Raihanian Mashhadi, A., Cade, W., Behdad, S., Oct. 2015. Reusability assessment of lithium-ion laptop batteries based on consumers actual usage behavior. J. Mech. Des. 137 (no. 12), 124501.

Sabbaghi, M., Esmaeilian, B., Cade, W., Wiens, K., Behdad, S., May 2016. Business outcomes of product repairability: a survey-based study of consumer repair experiences. Resour. Conserv. Recycl. 109, 114e122.

Scott. K.A., Weaver. S.T., 2014. To repair or not to repair: what is the motivation? I. Res. Consum. (no. 26). 1.

Sena da Fonseca, B., Galhano, C., Seixas, D., Feb. 2015. Technical feasibility of reusing coal combustion by-products from a thermoelectric power plant in the manufacture of fired clay bricks. Appl, Clay Sci., 104 189–195

Shafiee, M., Chukova. S., Sep. 2013. Maintenance models in warranty: a literature review. Eur. J. Oper. Res. 229 (no. 3), 561e572.

Sharma, A., Yadava, G.S., Deshmukh, S.G., 2011. A literature review and future perspectives on maintenance optimization. J. Qual. Maint. Eng. 17 (no. 1), 5e25.

Singh, A., Mourelatos, Z.P., Li, J., 2010. Design for lifecycle cost and preventive maintenance using time-dependent reliability. Adv. Mater. Res. 118, 10e16

Stahel, W., 1994. The utilization-focused service economy: resource ef<sup>fi</sup>ciency and product-life extension. Green. Ind. Ecosyst. 178e190.

Stoll, H.W., Sep. 1986. Design for manufacture: an overview. Appl. Mech. Rev. 39 (no. 9).1356-1364

Sundin, E., Bras, B., Jul. 2005. Making functional sales environmentally and economically bene<sup>fi</sup>cial through product remanufacturing. J. Clean. Prod. 13 (no. 9), 913e925.

Thomsen, B., Kokkolaras, M., Månsson, T., Isaksson, O., 2015. Component li<sup>fi</sup>ng decisions and maintenance strategies in the context of aeroengine productservice systems design. In: ASME 2015 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. V02BT03A045eV02BT03A045.

Yang, K., Cekecek, E., Mar. 2004. Design vulnerability analysis and design improvement by using warranty data Oual Reliab Eng Int 20 (no 2) 121–133

Zeithaml, V., 2000. Service quality, pro<sup>fi</sup>tability, and the economic worth of customers: what we know and what we need to learn. J. Acad. Mark. Sci. 28 (no. 1), 67e85.

Zhao, H., Gao, Q., Wu, Y., Wang, Y., Zhu, X., Jan. 2014. What affects green consumer

Zhou, J., Huang, P., Zhu, Y., Deng, J., Nov. 2012. A quality evaluation model of reuse parts and its management system development for end-of-life wheel loaders. J. Clean. Prod. 35, 239e249.

behavior in China? A case study from Qingdao. J. Clean. Prod. 63, 143e151.

Zhu, H., Gao, J., Li, D., Tang, D., May 2012. A web-based Product Service System for aerospace maintenance, repair and overhaul services. Comput. Ind. 63 (no. 4), 338e348.