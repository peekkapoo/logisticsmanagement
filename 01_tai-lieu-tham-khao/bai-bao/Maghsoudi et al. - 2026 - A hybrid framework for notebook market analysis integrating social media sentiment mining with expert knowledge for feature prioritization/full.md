RESEARCH ARTICLE

# A hybrid framework for notebook market analysis: Integrating social media sentiment mining with expert knowledge for feature prioritization

Mehrdad Maghsoudi <sup>1</sup>, Mohammadreza Bakhtiari <sup>2</sup>, Hamidreza Bakhtiari <sup>3</sup>\*

1 Management and Accounting Faculty, Shahid Beheshti University, Tehran, Iran, 2 Department of Electrical and Computer Engineering, University of Tehran, Tehran, Iran, 3 K.N. Toosi University of Technology, Tehran, Iran

![](images/745e314c6d515fc54197d812e073ce530ab3d5a773b49874c43297344efad4b5.jpg)

Check for updates

## OPEN ACCESS

Citation: Maghsoudi M, Bakhtiari M, Bakhtiari H (2026) A hybrid framework for notebook market analysis: Integrating social media sentiment mining with expert knowledge for feature prioritization. PLoS One 21(2): e0342067. https://doi.org/10.1371/journal.pone.0342067

Editor: Ankit Gupta, CCET: Chandigarh College of Engineering and Technology, INDIA

Received: April 2, 2025

Accepted: January 16, 2026

Published: February 9, 2026

Copyright: © 2026 Maghsoudi et al This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data availability statement: The dataset is available on Hugging Face (https://huggingface. co/datasets/MrbBakh/Twitter\_Laptop) and code on GitHub (https://github.com/Bakhtiarii/ hybrid-absa-notebook-analysis).

Funding: The author(s) received no specific funding for this work.

\* hamid.bakhtiary.77@gmail.com

## Abstract

The increasing complexity of consumer preferences in the notebook market requires advanced methodologies to effectively analyze user sentiments and prioritize product features for strategic decision-making. Traditional market research methods often fail to capture real-time, spontaneous consumer feedback while lacking integration with expert knowledge of actual purchasing behavior. This study introduces a novel hybrid framework that systematically combines aspect-based sentiment analysis (ABSA) of social media data with expert evaluations to bridge the gap between expressed consumer preferences and actual purchase drivers. The methodology analyzes 329,091 Twitter posts from January 2023 to June 2024, covering seven major notebook brands. Using the PyABSA framework, consumer sentiments toward 16 key notebook attributes are extracted and analyzed. Expert evaluations, conducted through fuzzy logic defuzzification, assign importance weights based on observed purchasing patterns, with features subsequently ranked using the TOPSIS multi-criteria decision-making method. Findings reveal that price, display quality, CPU performance, RAM capacity, and design constitute the most influential factors in notebook purchasing decisions. Negative sentiments concentrate on cooling systems, battery chargers, and warranty services, indicating critical improvement areas. Brand-specific analysis demonstrates that display quality ranks highest for Lenovo, while price dominates concerns for Dell, HP, and Microsoft, validating distinct market positioning strategies. By integrating machine learning-based sentiment analysis with structured expert knowledge, this research provides manufacturers with a quantifiable, actionable framework for optimizing product development and marketing strategies. The methodology enables companies to prioritize genuinely purchaseinfluencing features while addressing critical pain points, enhancing competitive

Competing interests: NO authors have competing interests.

positioning in dynamic markets. Future research should expand to cross-cultural consumer behavior analysis and real-time sentiment tracking systems.

## 1. Introduction

The notebook computer industry has become a cornerstone of the global technology market, driven by relentless innovation, expanding consumer needs, and intense competition [1,2]. As diverse user groups—including students, professionals, gamers, and creative practitioners—seek devices tailored to their specific requirements, manufacturers are compelled to identify, understand, and prioritize a multitude of product features. These features range from processing power and graphics performance to portability, design aesthetics, battery life, and overall user experience [3].

Recent progress in sentiment analysis has presented novel opportunities to refine our understanding of user preferences, with Aspect-Based Sentiment Analysis (ABSA) emerging as a particularly promising approach [4]. Although ABSA has been employed to examine sentiments in domains such as mobile phones [5] and restaurant reviews [6], its use in the notebook sector remains less explored. Notably, existing research often focuses on a single source of user feedback, such as historical product reviews, and overlooks real-time inputs from social media or the added value of expert judgment. This gap leaves a notable blind spot: manufacturers are unable to systematically integrate both consumer voices and expert evaluations when making decisions about product development and marketing strategies [7].

Furthermore, current market analysis strategies in the notebook industry suffer from three significant shortcomings. First, conventional techniques—such as surveys, focus groups, and basic sentiment assessments—may fail to capture the spontaneous, unstructured, and rapidly changing nature of consumer discourse on social media [8,9]. Second, sentiment analysis approaches commonly operate in isolation from the contextual expertise of industry professionals, resulting in assessments that may overlook the nuanced importance of specific features [10–13]. Third, a lack of comprehensive methodologies that fuse quantitative sentiment analysis with qualitative expert insights has prevented the notebook sector from establishing systematic models for accurate feature prioritization [14].

To address these challenges, a novel hybrid framework merges three essential components: (1) aspect-based sentiment analysis of social media data using the PyABSA framework, (2) expert-based evaluations facilitated by fuzzy logic, and (3) feature prioritization through the TOPSIS method. By integrating these components, the framework provides a robust mechanism for translating unstructured consumer feedback into clear, actionable insights. This data-driven methodology offers a more dynamic understanding of user sentiments and a structured way to incorporate these insights into product development and marketing decisions [15].

Our research makes several distinct contributions to the literature. First, by integrating automated sentiment analysis with expert evaluation, we deliver a more granular perspective on consumer preferences, allowing manufacturers to distinguish between essential and peripheral product features more effectively. Second, we introduce a rigorous process for mapping consumer sentiments—both positive and negative—to purchase intention through the combined application of fuzzy logic and TOPSIS. Third, we present empirical findings that detail how different notebook brands are perceived across multiple product attributes, thereby furnishing practical guidelines for marketing campaigns and research and development efforts.

In line with these insights, our study targets three principal objectives: (1) to identify and analyze user sentiments regarding key notebook components across different brands, (2) to evaluate how these sentiments, when combined with expert knowledge, influence purchase decisions, and (3) to develop a prioritized framework that synthesizes consumer feedback and expert perspectives for guiding both marketing and research and development initiatives. By comprehensively examining consumer discourse and industry expertise, we seek to provide a blueprint for manufacturers aiming to stay ahead in a market shaped by rapidly shifting demands and a broad spectrum of user preferences.

The subsequent sections are structured to facilitate an in-depth understanding of our contribution and its broader implications. Section 2 reviews the existing literature relevant to sentiment analysis, consumer electronics, and multi-criteria decision-making methods, setting the theoretical stage for the hybrid approach. Section 3 describes the methodology and data collection procedures in detail. Section 4 presents the empirical findings, while Section 5 interprets these results and situates them within the context of notebook market strategies. Section 6 concludes with the key insights and contribu tions, and Section 7 discusses limitations and potential avenues for future investigation.

## 2. Literature review

## 2.1. Consumer preferences in the notebook market

Consumer preferences in the notebook market have evolved significantly over the past decade, driven by changing usage patterns and technological advances. Previous research has identified price, performance, and portability as traditional decision factors. However, recent studies suggest that consumers increasingly value specific features differently based on their use cases [16].

Student consumers prioritize battery life and weight, reflecting their need for all-day usage and campus mobility. Professional users focus on display quality and keyboard comfort, essential for extended work sessions and productivity tasks. Gaming enthusiasts emphasize GPU performance and cooling systems, critical for sustained high-performance computing [17].

Market segmentation research reveals distinct preference patterns across demographics. Younger consumers (18–25) show higher sensitivity to design aesthetics and brand image, while older professionals (35–50) prioritize reliability and enterprise features. Geographic variations also influence preferences, with Asian markets showing stronger preference for compact designs compared to North American consumers who favor larger screens. In studies comparing students vs working professionals, [18] show similar base brand and screen-size preferences, though trade-offs among features differ.

Price sensitivity varies significantly across segments. While budget-conscious students demonstrate high price elasticity, business users show willingness to pay premiums for durability and support services [19]. This heterogeneity in price perception challenges manufacturers to develop differentiated pricing strategies across product lines.

Despite these insights, most existing research relies on surveys or sales data, missing the real-time, unsolicited opinions consumers express on social media. Traditional market research methods often suffer from response bias and lack the spontaneity of natural consumer discourse. The recent work [20] applies aspect-based sentiment analysis to laptop commentary and shows how feature-level sentiment differs across markets. Moreover, ABSA has been successfully applied in related smart device domains [21] and in e-commerce review classification [22]. In the methodological literature, advanced techniques such as graph convolutional joint models [23] and attention-over-attention networks [24] further motivate our methodological choice.

This gap motivates our use of aspect-based sentiment analysis to capture authentic consumer preferences from online discussions.

## 2.2. Overview of aspect-based sentiment analysis

Sentiment Analysis (SA), also known as Opinion Mining, is the computational study of people’s opinions, attitudes, and emotions towards entities such as products, events, or topics [4,20]. This field has gained substantial attention due to its ability to extract valuable insights from user-generated content. SA encompasses various techniques and approaches, including machine learning, lexicon-based, and hybrid methods, to classify the polarity of opinions at different levels: document, sentence, and aspect [25,26]. Document-level SA focuses on determining the overall sentiment of a text, while sentence-level SA aims to classify the sentiment of individual sentences [27]. However, these approaches often lack the granularity required for detailed analysis, leading to the development of aspect-level SA, which identifies sentiments towards specific aspects within a text. The applications of SA are vast, ranging from product reviews and stock market analysis to political debates and social media monitoring, making it a crucial tool for businesses and researchers alike to understand and predict trends and consumer behavior [28].

Aspect-based sentiment Analysis (ABSA) is a sophisticated sub-field of sentiment analysis that focuses on identifying and categorizing opinions about specific aspects within text data [29,30]. This methodology has gained significant attention due to its ability to provide detailed insights into user-generated content, making it valuable across various domains. This literature review is divided into two sections: the first discusses the models and methods used in ABSA, while the second explores its real-world applications.

## 2.3. Technical advances in ABSA methods

Aspect-Based Sentiment Analysis (ABSA) has evolved significantly, with various methodologies proposed to enhance its accuracy and efficiency. Traditional supervised learning approaches, such as those by Pannala et al. (2016), leverage machine learning algorithms like Support Vector Machines (SVM) and Maximum Entropy (ME) classifiers to classify sentiments in product reviews [31]. Their research underscores the importance of preprocessing steps, such as normalizing text and handling informal language, to improve sentiment analysis accuracy [32].

Transitioning from traditional methods, deep learning techniques have brought substantial advancements to ABSA [33]. Do et al. (2019) provide a comprehensive review of deep learning models, highlighting the superiority of Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs), including Long Short-Term Memory (LSTM) networks, in capturing both syntactic and semantic features of text [34]. Xue and Li (2018) introduced Gated Convolutional Networks (GCNs) with Aspect Embedding (GCAE), demonstrating higher accuracy and reduced training time compared to LSTMbased models [35].

Pre-trained language models like BERT have also been adapted for ABSA, as shown by Xu et al. (2019). They proposed a methodology to adapt BERT’s pre-trained weights for domain-specific nuances in product reviews, achieving significant improvements in aspect extraction and sentiment classification tasks [36]. Phan and Ogunbona (2020) further enhanced these models by integrating syntactical information into contextualized embeddings, improving both aspect extraction (AE) and aspect sentiment classification (ASC) [37].

Unsupervised and semi-supervised methods have also been explored to address data scarcity in ABSA. Ozyurt and Akcayol (2020) proposed Sentence Segment Latent Dirichlet Allocation (SS-LDA) for short texts, effectively improving the precision, recall, and F-score of aspect extraction tasks without the need for annotated training data [38]. García-Pablos, Cuadros, and Rigau (2017) introduced W2VLDA, a system combining guided topic modeling with continuous word embeddings, showing competitive performance across multiple domains and languages with minimal supervision [39].

Hierarchical models have proven effective in leveraging contextual dependencies. Ruder et al. (2016) proposed a hierarchical bidirectional LSTM model to capture interdependencies of sentences within a review, improving sentiment classification accuracy compared to non-hierarchical baselines [40]. Liu et al. (2018) introduced Cabasc, a content attention-based model that incorporates sentence-level and context attention mechanisms, achieving higher accuracy in sentiment classification tasks [41].

Innovative frameworks have been developed to enhance ABSA. Jiang et al. (2019) introduced the Multi-Aspect Multi-Sentiment (MAMS) dataset and models like CapsNet-BERT, which leverage capsule networks to model complex relationships between aspects and contexts [42]. Peng et al. (2020) proposed Aspect Sentiment Triplet Extraction (ASTE) to extract comprehensive sentiment information, including aspect, sentiment polarity, and opinion reason, using Bidirectional LSTM and Graph Convolutional Networks (GCN) [43]. Several surveys provide a detailed overview of ABSA meth odologies. Nazir et al. (2020) and Zhang et al. (2023) offer comprehensive reviews of tasks, methods, and challenges in ABSA, highlighting the advancements brought by pre-trained language models and proposing future research directions [44,45]. Fig 1 shows a summary of these methods.

## 2.4. Applications and domain-specific implementations

Aspect-based sentiment Analysis (ABSA) has found extensive applications across various domains, offering nuanced insights into user-generated content and enhancing decision-making processes. In the hospitality industry, Sann and Lai [46] leveraged ABSA to explore service failures in hotel reviews, uncovering significant cultural differences in guest complaints. This study highlighted the utility of ABSA in identifying areas for service improvement and tailoring responses to meet diverse guest expectations, thereby enhancing overall customer satisfaction. Similarly, Tran, Ba [47] employed ABSA to analyze hotel reviews in Ho Chi Minh City, Vietnam, combining aspect term extraction and polarity classification

![](images/c32f4343b016dea8b298958e9b7cb79b0d251d76c1900f51f694b52b20b764f9.jpg)  
Fig 1. ABSA Models and Methods.

https://doi.org/10.1371/journal.pone.0342067.g001

with topic modeling. Their findings provided actionable insights for hotel managers to improve service quality by targeting specific areas identified through sentiment analysis.

In the public sector, Alqaryouti, Siyam [48] demonstrated the potential of ABSA in enhancing smart government applications. By integrating domain-specific lexicons and rule-based techniques with Support Vector Machine (SVM) models, they effectively extracted significant aspects from user feedback, offering valuable insights for improving public services. The healthcare domain has also benefited from ABSA, as evidenced by Gräßer, Kallumadi [49], who analyzed drug reviews to enhance pharmacovigilance and clinical decision support systems. Their approach facilitated the monitoring of drug safety and efficacy through user-generated content, highlighting the importance of patient feedback in the pharmaceutica industry.

In the realm of mobile applications, Alturaief, Alturaief, Aljamaan [50] introduced the AWARE dataset, designed for requirements elicitation from app reviews. Their work demonstrated the practical applications of ABSA in the mobile app industry by providing detailed insights into user experience, which in turn supports continuous app quality enhancement and user-centered development. Similarly, in the e-commerce sector, Rodrigues and Chiplunkar [51] explored ABSA on product reviews, focusing on electronic gadgets. Their system effectively identified relevant aspects and classified sentiments, providing granular insights into customer opinions that drive product development and enhance customer satisfaction.

The education sector has also seen applications of ABSA, as Sivakumar and Reddy [52] utilized this technique to analyze student feedback, aiming to improve educational services. By categorizing opinions based on various aspects such as teaching and facilities, their study provided actionable insights for educational institutions to enhance the overall student experience. In the context of Arabic language resources, Al-Ayyoub, Gigieh [53] developed the Arabic Laptop Reviews (ALR) dataset, highlighting the challenges and potential of ABSA in analyzing Arabic user-generated content. Their work contributed significantly to the advancement of Arabic Natural Language Processing (NLP) and sentiment analysis.

Gupta and Ekbal [6] participated in the SemEval-2014 shared task, focusing on ABSA for restaurant and laptop reviews. Their approach employed various machine learning algorithms to extract aspect terms and classify sentiments, demonstrating the effectiveness of ABSA in mining relevant information from online reviews and providing insights into customer opinions on specific product features. Yiran and Srivastava [5] further applied ABSA to mobile phone reviews particularly focusing on the iPhone X. Their framework, which combined ABSA with Latent Dirichlet Allocation (LDA) for topic modeling, effectively extracted and weighed various product aspects, offering valuable implications for both consumers and manufacturers in the e-commerce domain.

Finally, Li, Bruce [54] applied ABSA to predict restaurant survival using customer-generated content from Yelp reviews. Their study demonstrated that aspect-based sentiment significantly improves the accuracy of survival predictions compared to models using only overall sentiment. This research provided valuable insights for restaurant owners and managers, suggesting that focusing on specific aspects of customer experience can enhance survival prospects and inform better strategic decisions in the highly competitive restaurant industry. Table 1 shows the Summary of ABSA applications in previous studies.

## 2.5. Multi-criteria decision making: Fuzzy logic and TOPSIS

While ABSA provides granular insights into consumer sentiments, translating these sentiments into actionable business priorities requires robust decision-making frameworks capable of handling multiple criteria simultaneously. Multi-Criteria Decision Making (MCDM) methods have emerged as essential tools for synthesizing diverse inputs into prioritized recommendations [55].

Fuzzy logic, introduced by [56], offers a mathematical framework for handling uncertainty and imprecision inherent in human judgments. Unlike classical binary logic, fuzzy logic allows variables to have degrees of membership across multiple categories, making it particularly suitable for capturing expert opinions expressed in linguistic terms such as “high,” “medium,” or “low” [57]. In the context of market analysis, fuzzy logic enables the systematic conversion of qualitative expert assessments into quantitative values through defuzzification techniques such as the Center of Gravity method [58]. This capability is especially valuable when integrating subjective expert knowledge with objective data-driven insights, as demonstrated in applications ranging from risk assessment to product evaluation [59].

Table 1. Summary of ABSA applications in previous studies.

<table><tr><td>Domain</td><td>Year</td><td>Application</td><td>Key Findings</td></tr><tr><td>Restaurants</td><td>2014</td><td>SemEval-2014 ABSA for restaurant and laptop reviews</td><td>Employed machine learning algorithms to extract aspect terms and classify sentiments, demonstrating effectiveness in mining relevant information from reviews.</td></tr><tr><td>Education</td><td>2017</td><td>Student feedback analysis</td><td>Categorized opinions based on aspects like teaching and facilities, offering actionable insights to improve educational services.</td></tr><tr><td>Arabic NLP</td><td>2017</td><td>Arabic Laptop Reviews (ALR) dataset</td><td>Advanced Arabic Natural Language Processing (NLP) and sentiment analysis by addressing challenges in analyzing Arabic user-generated content.</td></tr><tr><td>E-commerce</td><td>2017</td><td>Product reviews analysis for electronic gadgets</td><td>Identified relevant aspects and classified sentiments, offering granular insights into customer opinions to drive product development and satisfaction.</td></tr><tr><td>Healthcare</td><td>2018</td><td>Analyzing drug reviews</td><td>Enhanced pharmacovigilance and clinical decision support systems by monitoring drug safety and efficacy through user feedback.</td></tr><tr><td>Public Sector</td><td>2019</td><td>Enhancing smart government applications</td><td>Integrated domain-specific lexicons and SVM models to extract significant aspects from user feedback, improving public services.</td></tr><tr><td>Mobile Phones</td><td>2019</td><td>iPhone X reviews</td><td>Combined ABSA with LDA for topic modeling, extracting, and weighing various product aspects, providing valuable implications for consumers and manufacturers.</td></tr><tr><td>Hospitality</td><td>2020</td><td>Analyzing service failures in hotel reviews</td><td>Identified cultural differences in complaints, highlighting areas for service improvement and tailored responses to enhance customer satisfaction.</td></tr><tr><td>Hospitality</td><td>2020</td><td>Hotel reviews analysis in Ho Chi Minh City</td><td>Combined aspect term extraction, polarity classification, and topic modeling to provide actionable insights for improving service quality.</td></tr><tr><td>Mobile Applications</td><td>2021</td><td>AWARE dataset for app reviews</td><td>Provided insights into user experience, supporting continuous app quality enhancement and user-centered development.</td></tr><tr><td>Restaurants</td><td>2023</td><td>Predicting restaurant survival using Yelp reviews</td><td>Demonstrated that aspect-based sentiment improves the accuracy of survival predictions, offering insights for enhancing customer experience and strategic decision-making.</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t001

The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS), developed by Hwang and Yoon [60], has become one of the most widely adopted MCDM methods due to its computational simplicity and intuitive logic. TOPSIS ranks alternatives based on their geometric distance from positive and negative ideal solutions, effectively balancing multiple criteria to identify optimal choices [61]. The method has been successfully applied across diverse domains, including supplier selection, project prioritization, and consumer product evaluation [62]. Its ability to incorporate both benefit and cost criteria makes it particularly suitable for analyzing consumer preferences, where both positive sentiments (motivating purchase) and negative sentiments (deterring purchase) must be considered simultaneously.

Recent research has demonstrated the effectiveness of integrating sentiment analysis with MCDM approaches. [63] combined ABSA with graph-based classification to analyze consumer segmentation, showing how sentiment-driven insights can inform product development strategies. Similarly, hybrid frameworks that merge natural language processing with structured decision-making methods have proven valuable for transforming unstructured social media data into strategic recommendations [64]. These integrations address a fundamental limitation of standalone sentiment analysis: while ABSA captures what consumers express, MCDM methods help determine which expressions should guide business decisions based on their relative importance and impact.

The complementary nature of these methodologies forms the theoretical foundation for our hybrid framework. ABSA extracts feature-specific sentiments from consumer discourse, fuzzy logic captures and quantifies expert knowledge about purchase behavior, and TOPSIS synthesizes these inputs to generate prioritized recommendations that balance consumer voice with market realities.

Building upon the established understanding of consumer preferences in the notebook market, the proven capabilities of ABSA methodology, and the robust decision-making frameworks provided by fuzzy logic and TOPSIS, this article presents a novel integration that addresses critical gaps in current research. Unlike previous studies that either focus solely on stated preferences through surveys, rely on sentiment analysis without market context, or apply MCDM methods without real-time consumer input, our approach synthesizes these complementary methodologies into a unified framework. By combining ABSA’s ability to capture authentic consumer voice, fuzzy logic’s capacity to quantify expert knowledge, and TOPSIS’s systematic prioritization capabilities, we provide a more nuanced and actionable framework for notebook manufacturers. This hybrid methodology not only identifies what consumers say they want but also determines which expressed preferences genuinely drive purchasing decisions, offering a comprehensive blueprint for product development and marketing strategies in the competitive notebook market.

## 3. Research methodology

The methodology for this research involves a multi-step process to analyze marketing priorities and research and development of notebook items using sentiment analysis of social networks. While ABSA captures what consumers express online, expert evaluations provide crucial context about which expressed sentiments translate into actual purchasing behavior, based on their direct observation of thousands of customer decisions. The entire process is depicted in Fig 2, which illustrates the integrated framework comprising two parallel analytical streams that converge to produce prioritized recommendations.

The left stream represents the Social Media Analysis pipeline, consisting of three sequential stages: (1) Collecting Data, gathering notebook-related tweets from X, detailed in Section 3.1; (2) Data Pre-Processing, cleaning and filtering the collected tweets by removing URLs, hashtags, links, and usernames, excluding posts with fewer than 5 words, and omitting posts shorter than 50 characters, as described in Section 3.2; and (3) Sentiment Analysis, applying Aspect-Based Sentiment Analysis using the PyABSA framework to extract feature-specific sentiments, elaborated in Section 3.3.

The right stream represents the Experts Analysis component, where industry professionals evaluate the impact of sen timents on notebook selection using fuzzy logic linguistic scales, as detailed in Section 3.4. This stream captures expert knowledge about which consumer sentiments translate into actual purchasing behavior.

The two streams converge at the Identify Priorities stage, where the TOPSIS multi-criteria decision-making method synthesizes consumer sentiments with expert-validated importance weights to produce a prioritized ranking of notebook features, as described in Section 3.4 (Identifying Priorities subsection). This integration ensures that the final recommen dations reflect both authentic consumer voice and market-validated purchase drivers.

## 3.1. Data collection

In the initial phase of this research, we collect user-generated opinions about notebook products from the social media platform X (formerly Twitter). This platform is chosen due to its extensive user base and the richness of real-time content it provides [65,66]. Using the official X API and a structured, query-based approach, we retrieve English-language tweets posted over the past two years, focusing on seven major notebook brands analyzed in this study. A predefined set of feature-specific keywords is applied to ensure that only relevant tweets are extracted. let T denote the complete set of col lected tweets, where each t∈T includes notebook-related feature terms along with corresponding timestamp information. These data represent spontaneous consumer feedback and sentiment toward various notebook attributes.

To ensure reproducibility and transparency, the entire dataset is made publicly available on Hugging Face (https:// huggingface.co/datasets/MrbBakh/Twitter\_Laptop), and all data processing and analytical scripts are shared on GitHub (https://github.com/Bakhtiarii/hybrid-absa-notebook-analysis). This open-access approach aligns with open science princi ples while complying with both the platform’s terms of service and ethical research standards.

![](images/fa285a8a7a68053320f9766c1f89dc64497eccf918325acdf016c5cee09fcd96.jpg)  
Fig 2. Research methodology.  
https://doi.org/10.1371/journal.pone.0342067.g002

## 3.2. Data pre-processing

The collected data undergoes a thorough pre-processing phase to ensure its quality and relevance for subsequent analysis. The steps involved in data pre-processing are:

• Removal of URLs, hashtags, links, and usernames: This step eliminates non-essential elements that do not contribute to sentiment analysis [67,68].

• Posts with fewer than 5 words are excluded to remove non-informative content, spam, and bot-generated posts that typically lack substantive information for sentiment analysis [68,69]. Short posts often contain only hashtags, mentions, or fragmented phrases that do not provide meaningful insights into user sentiment toward specific product features [70]. This 5-word threshold ensures that only posts with adequate contextual information are included for aspect-based sentiment analysis [20].

• Omission of posts shorter than 50 characters: This further ensures that only substantial and informative posts are considered for analysis [68].

These measures refine the dataset, making it a robust input for sentiment analysis.

## 3.3. Sentiment analysis

The sentiment analysis phase employs the PyABSA framework to analyze the pre-processed tweets. PyABSA is an open-source tool specifically designed for Aspect-Based Sentiment Analysis (ABSA), with extensive validation in research applications [71–73]. The implementation follows a three-stage process comprising aspect term extraction, sentiment classification, and model optimization.

In the aspect term extraction stage, the framework utilizes a fine-tuned BERT-based sequence labeling model to identify relevant features. Each tweet t is processed to extract aspect terms $A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { n } \}$ , where a represents specific notebook features mentioned. The extraction model leverages domain-specific vocabulary and contextual embeddings to improve accuracy in identifying relevant aspects within the text.

The sentiment classification stage processes each identified aspect individually, performing targeted sentiment analysis through contextual evaluation. For each identified aspect a , the framework classifies sentiment polarity as either positive (1) or negative (−1). This classification process utilizes sophisticated attention mechanisms to focus on aspect-relevant contexts within tweets.

PyABSA’s modular architecture supports up to 40 built-in models, enabling comprehensive sentiment analysis through sophisticated model ensemble techniques [71]. The framework demonstrates state-of-the-art performance in both aspect extraction and sentiment classification tasks. According to Yang and Li (2022), PyABSA’s efficient architecture provides quick training and instant inference while maintaining high accuracy, outperforming traditional models in multilingual and multi-domain scenarios [74,75].

To validate PyABSA’s performance on our specific notebook review dataset, we conducted evaluation on a held-out sample of 1,000 tweets randomly selected from our corpus. This subset was manually annotated by two independent researchers with expertise in sentiment analysis, achieving an inter-annotator agreement of 0.87 (Cohen’s kappa). The manual annotation process involved identifying aspect terms and their corresponding sentiment polarities (positive, neg ative) for each tweet. PyABSA’s performance on this validation set demonstrated strong results with a precision of 0.85, recall of 0.82, and F1-score of 0.83 for aspect-based sentiment classification. These metrics confirm the framework’s effectiveness in accurately extracting and classifying sentiments toward specific notebook features within our Twitter dataset, ensuring the reliability of our subsequent analysis.

## 3.4. Expert analysis

To understand the impact of positive and negative sentiments on notebook selection, we incorporate the opinions of industry experts. These experts serve as informed intermediaries who observe actual consumer purchasing behavior daily [76,77]. Unlike survey respondents who might state preferences theoretically, sales experts witness which features actually drive or prevent purchases. Their evaluations are based on thousands of real customer interactions, complaints, returns, and successful sales. Research has shown that sales professionals develop sophisticated mental models of consumer preferences through repeated exposure to purchase decisions, making them valuable proxies for understand ing market behavior [78,79]. For instance, they observe customers willing to compromise on features they complain about (like fans) but unwilling to purchase when price or display don’t meet expectations. This experiential knowledge bridges the gap between stated preferences (captured by ABSA) and revealed preferences in actual purchasing decisions [80,81]. Experts evaluate the significance of each notebook feature by rating them based on the strengths and weaknesses observed from user sentiments. This evaluation is done using fuzzy logic, where features are rated on a five-point scale: “very low, low, medium, high, and very high.”

Fuzzy logic provides a robust mechanism to capture expert opinions, especially when dealing with subjective assessments [57]. In fuzzy logic, a variable can have a degree of membership in multiple sets simultaneously, described by membership functions [82]. These functions map the input space to a membership value between 0 and 1 [59].

In fuzzy logic, the aggregation of expert opinions results in fuzzy sets for each notebook feature. Defuzzification is the process of converting these fuzzy sets into crisp values [83]. The Center of Gravity (CoG) method, also known as the centroid method, is a commonly used defuzzification technique [58]. It calculates the center of the area under the curve of the membership function [84]. The formula for the CoG method is:

$$
\mathrm{COG} = \frac {\sum (\mu (x) * x)}{\sum (\mu (x))}
$$

where: $\mu ( { \boldsymbol { x } } )$ is the membership function of the fuzzy set at value x and x is a value within the domain of the fuzzy set [85]. This method provides a single crisp value that represents the center of the area under the membership function curve, giving a balanced representation of the fuzzy set.

Identifying Priorities

In the final step, we prioritize the features of notebooks based on their impact on consumer purchase decisions using the TOPSIS method (Technique for Order of Preference by Similarity to Ideal Solution). TOPSIS is a powerful multi-criteria decision-making method that considers both positive and negative factors for prioritization [61,62].

The steps involved in the TOPSIS method are:

Step 1: make a fuzzy decision matrix with dimensions m\*n to capture the perspectives of the individuals

$$
D = \left[ \begin{array}{c c c} x _ {1 1} & x _ {1 2} & x _ {1 n} \\ . & . & . \\ x _ {m 1} & x _ {m 2} & x _ {m n} \end{array} \right]
$$

Step 2: Normalization of the decision matrix:

$$
r _ {i j} = \frac {X _ {i j}}{\sqrt {\sum_ {i = 1} ^ {m} X _ {i j} ^ {2}}}
$$

Step 3: make a weighted normalized Fuzzy Matrix V .

The creation of weighted matrices involves multiplying the normalized matrix by the weight of $\begin{array} { r } { V _ { i j } = r _ { i r } \times w _ { \mathrm { j . } } } \end{array}$ . The matrix is as follows:

$$
V = \left[ \begin{array}{c c c} v _ {1 1} & v _ {1 2} & v _ {1 n} \\ . & . & . \\ v _ {m 1} & v _ {m 2} & v _ {m n} \end{array} \right]
$$

Step 4: Calculate Positive Ideal solution $A ^ { * }$ and Negative Ideal solution $A ^ { - }$

$$
A ^ {*} = \left(\left(\text {Max} v _ {i j} \mid i = 1, 2, \dots , m, \forall_ {j} \in J _ {+}\right), \left(\text {Min} v _ {i j} \mid i = 1, 2, \dots , m, \forall_ {j} \in J _ {-}\right)\right)
$$

$$
A ^ {-} = \left(\left(\text {Max} v _ {i j} \mid i = 1, 2, \dots , m, \forall_ {j} \in J _ {+}\right), \left(\text {Min} v _ {i j} \mid i = 1, 2, \dots , m, \forall_ {j} \in J _ {-}\right)\right)
$$

Step 5: Calculate the sum of components distance from the positive ideal and negative ideal values.

$$
d _ {i} ^ {+} = \sum_ {j = 1} ^ {n} d (v _ {i j}, v _ {j} ^ {*}), \quad i = 1, 2, \dots , m
$$

$$
d _ {i} ^ {-} = \sum_ {j = 1} ^ {n} d (v _ {i j}, v _ {j} ^ {-}), i = 1, 2, \dots , m
$$

Step 6: Calculate the similarity to the ideal option. To achieve this, the Closeness coefficient (CCi) should be calculated The option with the highest CCi is better.

$$
C _ {i} ^ {*} = \frac {d _ {i} ^ {-}}{d _ {i} ^ {-} + d _ {i} ^ {+}}
$$

This method helps in identifying which features are most influential in driving purchase decisions and which negative aspects deter consumers from buying, thereby providing a clear set of priorities for marketing and R&D efforts.

## 3.5. Participant consent

This study did not involve direct human participation, clinical trials, or the collection of personal or sensitive information from individuals. All data analyzed were derived from publicly available, anonymized Twitter posts and non-identifiable expert responses collected through a voluntary online questionnaire. Expert participants contributed general, non-personal evaluations related to product features and were not asked to provide any personal or sensitive information. As such, no written or verbal informed consent was required or obtained, and no minors were involved in the study. The study complies with ethical guidelines for research using anonymized and non-identifiable data, and the nature of the data collection did not necessitate ethical review or consent procedures.

## 4. Results

## 4.1. Data collection

The primary dataset for this study comprises laptop reviews collected from Twitter, covering seven well-known laptop brands: Asus, Acer, Apple, Dell, HP, Lenovo, and Microsoft. The aim is to gather a comprehensive set of user opinions and sentiments regarding various laptop models and features. To compile the dataset, a query-based search methodology was utilized. This involved creating a list of keywords relevant to laptops in general and specific to each brand. By leveraging these query lists, tweets containing at least one of the specified keywords were identified. For instance, keywords such as “laptop,” “Asus,” “MacBook,” and “CPU” were used to filter relevant reviews. For each brand, specific product names and model identifiers were included to ensure a broad and representative sample of reviews. The query lists for each brand are as Table 2.

Table 2. Query list.

<table><tr><td>Brand</td><td>Query List</td></tr><tr><td>Asus</td><td>“Asus AND laptop,” “zenbook,” “vivobook,” “Flow AND Asus,” “Zephyrus AND Asus,” “TUF AND laptop,” “Chromebook AND Asus,” “ProArt StudioBook,” “asus x,” “ExpertBook,” “ROG AND laptop”</td></tr><tr><td>Acer</td><td>“Acer AND laptop,” “Aspire AND laptop,” “ConceptD,” “Extensa AND acer,” “Swift AND acer,” “Spin AND acer,” “Nitro AND acer,” “Predator AND laptop,” “TravelMate AND acer,” “Chromebook AND acer,” “Ferrari AND acer”</td></tr><tr><td>Apple</td><td>“Apple AND laptop,” “MacBook”</td></tr><tr><td>Dell</td><td>“Dell AND laptop,” “Studio AND Dell,” “Inspiron AND Dell,” “XPS AND Dell,” “Vostro AND Dell,” “Latitude AND Dell,” “Precision AND Dell,” “Alienware AND Dell,” “Chromebook AND Dell,” “Dell G”</td></tr><tr><td>HP</td><td>“HP AND laptop,” “Victus AND laptop,” “Stream AND HP,” “Spectre AND HP,” “Envy AND HP,” “Pavilion AND HP,” “Omen AND laptop,” “EliteBook,” “Pro-Book,” “ZBook,” “Chromebook AND HP,” “Dragonfly AND HP,” “Elite Dragonfly,” “Dev One”</td></tr><tr><td>Lenovo</td><td>“Lenovo AND laptop,” “ThinkPad,” “IdeaPad,” “Legion AND Lenovo,” “Yoga AND Lenovo,” “ThinkBook,” “Chromebook AND Lenovo”</td></tr><tr><td>Microsoft</td><td>“Surface Pro 10,” “Surface Pro 11,” “Surface Laptop 6,” “Surface Laptop Go 3,” “Surface Laptop Studio 2,” “Surface Laptop 7,” “Surface Studio,” “Surface Duo,” “Surface Go,” “Surface Book,” “Surface &amp; neo,” “Surface &amp; pro,” “Surface AND laptop,” “Microsoft AND surface”</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t002

The tweets were collected over a period spanning from January 1, 2023, to June 22, 2024. This range was chosen to ensure the data reflects recent trends and opinions about the laptops from the specified brands. Initially, a total of 422,649 tweets were collected. To ensure the quality and reliability of the dataset, only tweets that had at least one “like” were included. This criterion helped in filtering out potentially less relevant or less impactful reviews. To visualize the frequency of reviews over the specified period, a time trend chart was created. Fig 3 illustrates the frequency of reviews from January 2023 to June 2024, revealing several distinct temporal patterns. The low volume observed in early January 2023 (approximately 350–400 daily tweets) reflects the typical post-holiday period when consumer discussions about technology purchases temporarily decline following the peak shopping season. Activity gradually stabilized to approximately 700–800 daily tweets throughout the first half of 2023. A notable peak occurred around November 2023, reaching approximately 1,500 daily tweets, nearly double the baseline activity. This surge coincides with the major shopping events of Black Friday and Cyber Monday, when consumer interest in notebook purchases intensifies significantly due to promotional pricing and holiday gift-buying. Secondary peaks visible around June 2023 and May-June 2024 align with back-toschool shopping periods and mid-year product refresh cycles. These temporal patterns validate the representativeness of our dataset, as it captures both routine consumer discourse and peak purchasing consideration periods.

## 4.2. Data pre-processing

Data pre-processing is a crucial step in ensuring the quality and reliability of the dataset. For this study, the primary focus was on cleaning and refining the data collected from Twitter to remove noise and enhance its usability for Aspect-Based Sentiment Analysis (ABSA). The initial dataset consisted of 422,649 tweets, which were subsequently filtered and cleaned to produce a final dataset of 329,091 reviews. The pre-processing of the dataset involved several key steps:

1. Conversion to String Format: All entries in the reviews were converted to strings to maintain consistency and facilitate further processing.

2. Handling Missing Values: Any missing values (NaNs) in the reviews were replaced with empty strings to prevent issues during text analysis.

Frequency of Reviews Over Time

![](images/3c29d827a11beafe79b477f605d3a5080699fcd32ae1592dfddb875c04bc9a4d.jpg)  
Fig 3. Tweet collection frequency from 329,091 notebook reviews spanning January 2023 to June 2024. https://doi.org/10.1371/journal.pone.0342067.g003

3. Removal of Duplicates: Duplicate reviews, where the same review appeared more than once, were identified and removed to ensure that each review was unique. This step helped in reducing redundancy in the dataset.

4. Text Cleaning: The text of the reviews underwent several cleaning processes:

a) Lowercasing: All text was converted to lowercase to maintain uniformity.

b) Removal of URLs: Links within the tweets were removed to eliminate irrelevant content.

c) Removal of Mentions and Hashtags: Mentions (e.g., @username) and hashtags (e.g., #laptop) were removed to focus on the substantive content of the reviews.

5. Filtering Short Reviews: To enhance the quality of the dataset, reviews with fewer than 5 words or fewer than 50 characters were filtered out. This criterion ensured that only reviews with sufficient content were included for analysis.

The elimination of reviews was guided by specific criteria to improve the dataset’s relevance and quality. Short reviews that were too brief were deemed less informative and were excluded, while redundant reviews were removed to avoid skewing the analysis. After the data pre-processing steps, the dataset was refined to 329,091 reviews. This cleaned dataset provided a robust foundation for performing ABSA, ensuring that the analysis was based on relevant and high-quality data.

Following the data pre-processing steps, we conducted a dataset quality assessment to ensure balanced representation across key dimensions. The final dataset demonstrates reasonable distribution across the seven notebook brands with no significant brand bias that could skew sentiment analysis results. Temporal distribution analysis reveals consistent data collection across the study period, ensuring that our findings are not influenced by seasonal variations or specific events. The aspect-based sentiment distribution shows balanced representation across the identified features, with core performance features accounting for the majority of sentiment expressions, which aligns with expected consumer focus areas. Our current assessment demonstrates sufficient data quality and representativeness for reliable aspect-based sentiment analysis across notebook brands and features.

## 4.3. Aspect analysis implementation

Aspect-Based Sentiment Analysis (ABSA) is a fine-grained technique used to determine the sentiment expressed towards specific aspects or features within a text. Unlike general sentiment analysis, which provides an overall sentiment for a piece of text, ABSA identifies sentiments related to particular entities or attributes mentioned. This level of detail is usefu in understanding user opinions about various features of a product. In this study, ABSA was employed to analyze user reviews of laptops from Twitter, aiming to extract sentiments associated with specific aspects such as “battery,” “screen,” and “price” to gain insights into user satisfaction across seven major brands.

The implementation of ABSA was facilitated by the PyABSA library, a Python-based framework that provides pretrained models and utilities for aspect extraction and sentiment prediction. The analysis was conducted using Google Colab, a cloud-based platform offering free computational resources, supporting Python code execution, and providing the necessary tools for machine learning tasks.

Applying the ABSA methodology allowed the identification of various aspects mentioned in reviews and the classification of sentiments associated with each as positive, negative, or neutral. This granular sentiment analysis provided a detailed understanding of user opinions about different laptop features, essential for the subsequent steps of the study.

Aspect extraction, a fundamental step in ABSA, involves identifying specific attributes or features mentioned in reviews and determining the associated sentiment. This detailed analysis offers insights into user opinions about features such as “battery,” “RAM,” and “price.” For instance, in the review “Super great laptop even though it had 8 GB of RAM, it is also very thin and lightweight, and the battery lasts a long time,” the identified aspects were “RAM,” “weight,” and “battery,” with corresponding sentiments being “Neutral,” “Positive,” and “Positive,” respectively.

The aspect extraction process involved using the PyABSA library to extract aspects and associated sentiments from each review, analyzing the frequency of each aspect to determine the most commonly mentioned features, and creating a target aspect list based on frequency analysis. The final list of target aspects included [‘ram’, ‘display’, ‘keyboard’, ‘price’, ‘battery’, ‘storage’, ‘gpu’, ‘cpu’, ‘charger’, ‘warranty’, ‘design’, ‘webcam’, ‘port’, ‘size’, ‘fan’, ‘weight’].

Challenges such as synonyms and variants were addressed by normalizing terms to ensure consistency. The final aspect list served as a basis for analyzing sentiments associated with each aspect in the reviews, providing a comprehensive analysis of user opinions regarding critical laptop features and forming the foundation for understanding user satisfaction and identifying areas for improvement.

The result involved summarizing the sentiments associated with each extracted aspect, focusing on the most frequently mentioned ones to gain a comprehensive understanding of user opinions about different laptop features. Sentiments were categorized as positive or negative, and radar and butterfly charts were plotted to visualize the overall sentiment distribu tion for each aspect, allowing for a quick comparison of sentiment intensity across different aspects.

Fig 4 offers a comprehensive visualization of user sentiments across various laptop features. High positive sentiment is noted in aspects such as design, with 82.2% positive feedback, weight at 72.5%, GPU with 70.7%, and CPU at 69.0%. Conversely, the fan shows an 85.1% negativity rate, and the charger faces 68.33% negative reviews, indicating common issues with cooling efficiency, battery charging.

Balanced sentiments are observed in features like RAM, with 61.4% positive feedback, display at 55.7%, keyboard at 56.6%, and storage at 56.2%. These features generally meet user expectations but suggest areas where small improvements could enhance satisfaction. The display and battery, which attract the most reviews, are crucial features for users, underscoring their significant role in the overall user experience. Additionally, the price, with a 65.3% positivity rate, reflects user sensitivity to cost versus value, emphasizing the importance of competitive pricing strategies.

Distribution of Positive and Negative Reviews  
![](images/4b6242dc07849bb61f2c7e9906279ef18c79d8819a0bc39af502549d768dd1ea.jpg)  
Fig 4. Distribution of Positive and Negative reviews.  
https://doi.org/10.1371/journal.pone.0342067.g004

After conducting a comprehensive analysis of the overall dataset, we now shift our focus to a more detailed examination of individual laptop brands. By analyzing user sentiments for each brand, we can uncover unique insights and brand-specific trends that might not be visible in the aggregate data. This targeted analysis will deepen our understanding of consumer preferences and pain points for each brand, providing valuable guidance for targeted improvements and strategic marketing initiatives.

1. Asus: Asus laptops have garnered significant user sentiment, highlighting both strengths and areas for improvement. The design stands out with an impressive 92.3% positive feedback, underscoring its aesthetic appeal and ergonomic excellence (Fig 5). Users also highly appreciate the lightweight and portable designs (87.9% positive sentiment). In terms of performance, Asus laptops receive strong approval for their CPU (78.7% positive) and GPU (68.5% positive), showcasing robust processing and graphics capabilities. However, there are notable concerns regarding the fan system (78.4% negative sentiment), potentially affecting cooling efficiency. The charger (57.6% negative) also drew criticism, primarily due to battery charging reliability issues. Warranty services received considerable negative feedback (79.6% negative), indicating room for improvement in customer support.

![](images/5438c2ee1af6244b7f2562a97c5613e5d71546abd80cd59e353aab9676a92b64.jpg)

![](images/544b68bd30413073c369bddfee9c6c0ecb10d4244adeb84de28b9e0791a9f4c6.jpg)

![](images/841acb98f6d2fee77e826c5853d5e8a5e6b685a2d7cd48e1de703102f3aafc7a.jpg)

![](images/2255f67d24f59bfa08c9f1d07539c076b1ed69aaf9ddfdf1cbe5b20669c43b64.jpg)

![](images/0eada5b752f9d6a30d72397bf673e33f1845050ffdbf9790badbeaf7768b9e8f.jpg)

![](images/e6e80aaacae4b4e9efa71eb34311a91f8320e22b0f584354ccfc5d554e304c18.jpg)

![](images/f41053233333bb04bf9c75e60a20d2c5b6fceb573b5e6adb24c8678be4f3d75d.jpg)  
Fig 5. Brand-specific sentiment patterns across seven notebook manufacturers revealing unique strengths and weaknesses per brand.

2. Acer: User sentiments towards Acer laptops reveal a mixed bag of strengths and challenges. Battery life stands out with a prominent 70.4% positive sentiment, reflecting high user satisfaction (Fig 5). The display quality is another highlight, praised for its visual excellence (76.2% positive). Acer excels in GPU (81.4% positive) and CPU (80.5% positive) performance, demonstrating powerful processing capabilities. However, concerns about the fan system are prevalent (almost 100% negative sentiment), indicating significant cooling issues. Dissatisfaction with the charger (64.7% negative) and warranty (56.5% negative) further highlights reliability issues. The keyboard also receives notable criticism (57.8% negative), affecting usability and comfort.

3. Apple: Apple laptops are celebrated for their distinct features, though not without critical feedback. Design is a standout feature with a notable 67.5% positivity rate, emphasizing aesthetics and ergonomic appeal (Fig 5). Weight is also positively received (68.1% positive), contributing to the laptops’ portability. However, concerns about the fan (84.6% negative sentiment), charger (73.4% negative), keyboard (60.5% negative), and warranty (61.0% negative) indicate significant areas for improvement.

4. Dell: Dell laptops are well-regarded for their overall performance and design appeal (Fig 5). Design receives an impres sive 88.0% positive feedback, reflecting its aesthetic and ergonomic strengths. Weight is another positive aspect (81.0% positive), contributing to its portability. Performance-wise, Dell laptops excel in GPU (76.3% positive) and CPU (74.7% positive) capabilities. However, concerns about the fan system (87.7% negative sentiment), and charger (56.7% negative) underscore areas needing improvement.

5. HP: HP laptops earn high praise for their design (95.4% positive sentiment), emphasizing aesthetic and ergonomic qualities (Fig 5). Weight is also positively received (75.0% positive), contributing to their portability. Performance aspects such as CPU (81.7% positive) and GPU (84.3% positive) capabilities are well-regarded. However, critical feedback regarding the fan (93.3% negative sentiment) indicates areas needing attention.

6. Lenovo: User sentiments towards Lenovo laptops highlight strong design appeal (89.0% positive sentiment), emphasizing aesthetics and ergonomic considerations (Fig 5). Weight is also positively received (80.0% positive), contributing to their portability. Performance-wise, Lenovo excels in CPU (81.0% positive) and GPU (72.0% positive) capabilities. However, concerns about the fan system (90.2% negative sentiment) indicate potential areas for improvement.

7. Microsoft: Microsoft laptops receive commendation for their design (75.7% positive sentiment), highlighting aesthetic and ergonomic features (Fig 5). Performance aspects such as CPU (64.7% positive) and GPU (57.4% positive) capabilities show strong approval. However, there are significant concerns about the charger (86.5% negative sentiment), and warranty (70.0% negative), indicating areas needing improvement.

## 4.4. Determining the importance of sentiments in notebook selection

After identifying users’ sentimental responses to various features and aspects of notebooks, it is crucial to understand how these sentiments influence the selection and purchase of laptops. To gain an accurate and practical understanding of this phenomenon, we consulted industry experts with direct experience in notebook sales. These experts don’t replace consumer preferences but rather interpret them through their accumulated experience with actual purchase patterns. They understand the difference between features consumers complain about online versus features that make them walk away from a purchase. This practical knowledge helps weight the importance of sentiments in real purchasing contexts. Using the snowball sampling method, we selected 10 notebook sales experts from diverse backgrounds. Table 3 presents the demographic and professional profiles of these experts.

As shown in Table 3, our expert panel comprises professionals in key decision-making positions including Sales Managers, Marketing Managers, and Senior Sales personnel who directly influence and observe consumer purchasing patterns. These positions provide them with unique insights into the gap between expressed consumer sentiments and actual purchase behaviors. The diversity in their roles, from frontline salespersons who interact directly with customers to marketing managers who analyze purchase trends, ensures comprehensive coverage of the consumer decision-making process.

Table 3. Profile of experts.

<table><tr><td>ID</td><td>Gender</td><td>Country</td><td>Experience (years)</td><td>Position</td><td>Store Type</td></tr><tr><td>E1</td><td>Male</td><td>Germany</td><td>16</td><td>Sales Manager</td><td>Laptop store</td></tr><tr><td>E2</td><td>Female</td><td>Canada</td><td>10</td><td>Salesperson</td><td>Laptop store</td></tr><tr><td>E3</td><td>Male</td><td>South Korea</td><td>12</td><td>Marketing Manager</td><td>Laptop store</td></tr><tr><td>E4</td><td>Female</td><td>Spain</td><td>8</td><td>Salesperson</td><td>Laptop store</td></tr><tr><td>E5</td><td>Male</td><td>Japan</td><td>11</td><td>Senior Sales Manager</td><td>Digital goods store</td></tr><tr><td>E6</td><td>Male</td><td>France</td><td>14</td><td>Marketing Manager</td><td>Digital goods store</td></tr><tr><td>E7</td><td>Female</td><td>Brazil</td><td>9</td><td>Salesperson</td><td>Digital goods store</td></tr><tr><td>E8</td><td>Female</td><td>China</td><td>10</td><td>Sales Manager</td><td>Digital goods store</td></tr><tr><td>E9</td><td>Female</td><td>England</td><td>11</td><td>Marketing Manager</td><td>Digital goods store</td></tr><tr><td>E10</td><td>Male</td><td>Australia</td><td>13</td><td>Sales Manager</td><td>Laptop store</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t003

The objective of this stage is to determine, through industry experts, the extent to which positive sentiments towards specific notebook features motivate purchase decisions, and conversely, how negative sentiments may deter customers from buying a particular product. To achieve this, we designed an online questionnaire for our panel of experts. The survey asked them to rate, using linguistic terms commonly employed in fuzzy logic for data collection (very low, low, medium, high, very high), the impact of both positive and negative sentiments across 16 notebook features. Specifically, they were asked to evaluate how positive sentiments create motivation for purchase and how negative sentiments create barriers to purchase. Table 4 presents the consolidated results of this questionnaire.

To defuzzify the expert opinions provided in Table 4, the center of gravity (COG) method was employed. This method converts linguistic terms into precise numerical values using fuzzy logic principles, facilitating a quantitative analysis of qualitative data. The fuzzy numbers assigned to each linguistic term are as Table 5:

By applying these values, the linguistic ratings from Table 4 were transformed into numerical values. Subsequently, the average score for each notebook feature was calculated for both positive and negative sentiments. The resulting averages for each feature are presented in Table 6, which indicates the degree to which positive and negative sentiments influence the purchase decision for each feature:

The results of the defuzzification process, derived from the expert opinions of notebook sales professionals, provide valuable insights into which notebook features significantly influence purchase decisions through positive and negative sentiments. Features such as price, display, and RAM exhibit high average scores for both positive and negative sentiments (0.9167, 0.8833, and 0.8333 respectively), indicating that these features are crucial in motivating customers to buy notebooks and, conversely, can act as significant barriers if perceived negatively. The high scores for these features suggest that customers place considerable importance on the performance and cost-effectiveness of the notebook, and any dissatisfaction in these areas can greatly deter potential buyers. On the other hand, features such as the charger, and fan have notably lower average scores for both positive and negative sentiments (both 0.25, 0.25), implying that these aspects are less critical in influencing purchase decisions. This suggests that while these features are part of the overall product package, they do not play a major role in the customer’s motivation to purchase a notebook. Additionally, the relatively moderate scores for features like the keyboard, webcam, and port (0.5, 0.3583, and 0.5 respectively) indicate that while these factors are important, they are not as pivotal as the core performance and design features.

Table 4. The results of expert opinions.

<table><tr><td rowspan="17">Positive Sentiment</td><td>Laptop Feature</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E9</td><td>E10</td></tr><tr><td>RAM</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td></tr><tr><td>Display</td><td>High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>High</td><td>Very High</td><td>Very High</td><td>High</td><td>Very High</td><td>High</td></tr><tr><td>Keyboard</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Price</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td></tr><tr><td>Battery</td><td>High</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>Storage</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>GPU</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td></tr><tr><td>CPU</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td></tr><tr><td>Charger</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Warranty</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>High</td></tr><tr><td>Design</td><td>Medium</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td></tr><tr><td>Webcam</td><td>Low</td><td>Medium</td><td>Medium</td><td>Low</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Low</td></tr><tr><td>Port</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Size</td><td>Medium</td><td>High</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>Medium</td></tr><tr><td>Fan</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Weight</td><td>Medium</td><td>High</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>Medium</td></tr><tr><td rowspan="16">Negative Sentiment</td><td>RAM</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td></tr><tr><td>Display</td><td>High</td><td>Very High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td></tr><tr><td>Keyboard</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Price</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td><td>Very High</td></tr><tr><td>Battery</td><td>High</td><td>High</td><td>High</td><td>Medium</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>Storage</td><td>High</td><td></td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>GPU</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td></tr><tr><td>CPU</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>Very High</td><td>High</td><td>High</td><td>Very High</td><td>High</td><td>High</td></tr><tr><td>Charger</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Warranty</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>High</td></tr><tr><td>Design</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td></tr><tr><td>Webcam</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Port</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Size</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Fan</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Weight</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t004

## 4.5. TOPSIS-based prioritization of notebook features

The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) represents the synthesis stage of our hybrid framework, where consumer sentiments and expert knowledge converge to generate strategic priorities. This integration addresses a fundamental challenge in market analysis: the disconnect between sentiment intensity and purchase influence.

The TOPSIS methodology serves three critical functions in our framework. First, it transforms multi-dimensional sentiment data into a unified decision matrix by incorporating both positive and negative sentiment percentages for each feature. Second, it weights these sentiments according to expert-validated importance scores, acknowledging that consumer emotions do not uniformly translate into purchase behaviors. Third, it calculates the relative closeness of each feature to ideal and negative-ideal solutions, producing a comprehensive ranking that balances consumer preferences with market realities.

Table 5. Linguistic scales.

<table><tr><td>Linguistic Scale</td><td>Fuzzy Number</td><td>Defuzzification values</td></tr><tr><td>Very low (VL)</td><td>(0, 0, 0.25)</td><td>0.0833</td></tr><tr><td>Low (L)</td><td>(0, 0.25, 0.5)</td><td>0.25</td></tr><tr><td>Medium (M)</td><td>(0.25, 0.5, 0.75)</td><td>0.5</td></tr><tr><td>High (H)</td><td>(0.5, 0.75, 1)</td><td>0.75</td></tr><tr><td>Very high (VH)</td><td>(0.75, 1, 1)</td><td>0.9167</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t005

Table 6. Average Defuzzification values.

<table><tr><td>notebook Feature</td><td>Positive Sentiment Average</td><td>Negative Sentiment Average</td></tr><tr><td>RAM</td><td>0.8333</td><td>0.8333</td></tr><tr><td>Display</td><td>0.8833</td><td>0.85</td></tr><tr><td>Keyboard</td><td>0.5</td><td>0.5</td></tr><tr><td>Price</td><td>0.9167</td><td>0.9167</td></tr><tr><td>Battery</td><td>0.75</td><td>0.75</td></tr><tr><td>Storage</td><td>0.75</td><td>0.75</td></tr><tr><td>GPU</td><td>0.6083</td><td>0.6</td></tr><tr><td>CPU</td><td>0.8333</td><td>0.8333</td></tr><tr><td>Charger</td><td>0.25</td><td>0.25</td></tr><tr><td>Warranty</td><td>0.6667</td><td>0.6667</td></tr><tr><td>Design</td><td>0.7833</td><td>0.6</td></tr><tr><td>Webcam</td><td>0.3583</td><td>0.25</td></tr><tr><td>Port</td><td>0.5</td><td>0.5</td></tr><tr><td>Size</td><td>0.6333</td><td>0.5</td></tr><tr><td>Fan</td><td>0.25</td><td>0.25</td></tr><tr><td>Weight</td><td>0.6333</td><td>0.55</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t006

This methodological integration reveals that features generating strong emotional responses may not necessarily drive purchase decisions, while features with moderate sentiments can be critical determinants of consumer choice. The TOP-SIS analysis thus bridges the gap between what consumers express (captured through ABSA) and what actually influences their purchasing behavior (validated through expert knowledge), providing manufacturers with actionable priorities that reflect both market sentiment and purchase psychology.

Preparation and Implementation of TOPSIS Analysis:

1. Decision Matrix Construction: A matrix was created with notebook features (e.g., RAM, Display, CPU) as rows and four columns:

a) Positive sentiment scores from social media analysis

b) Negative sentiment scores from social media analysis

c) Positive sentiment weights from expert evaluations

d) Negative sentiment weights from expert evaluations

This structure allows for a holistic view of each feature, considering both consumer opinions and expert assessments.

2. Normalization: To ensure fair comparison across different scales, the decision matrix was normalized. This step is crucial as it converts all values to a common scale, typically between 0 and 1.

3. Weighted Normalization: The normalized matrix was then weighted using the expert-derived importance scores. This step emphasizes the relative importance of each criterion as determined by industry professionals.

4. Ideal Solutions Identification: Two hypothetical solutions were defined:

• Positive Ideal Solution (PIS): Representing the best possible scenario with maximized positive sentiments and minimized negative sentiments.

• Negative Ideal Solution (NIS): Representing the worst possible scenario with minimized positive sentiments and maximized negative sentiments.

5. Distance Calculation: Euclidean distances were calculated from each notebook feature to both the PIS and NIS. This step quantifies how close each feature is to the ideal and worst-case scenarios.

6. Relative Closeness Calculation: The relative closeness of each feature to the ideal solution was computed. This value, ranging from 0 to 1, indicates how well a feature performs overall, considering both its proximity to the ideal solution and its distance from the worst solution.

7. Ranking: Finally, notebook features were ranked based on their relative closeness values. Features with higher values are considered more desirable, as they are closer to the ideal solution and farther from the negative ideal solution.

The results obtained from TOPSIS calculations are detailed in Table 7, which delineates a distinct hierarchy of con sumer preferences. Key findings highlight that price, design, display, CPU, and RAM are paramount factors influencing consumer choice in notebooks. These top-ranked attributes underscore consumer preferences for a blend of affordability, aesthetic appeal, visual quality, and core performance when selecting their purchases.

To capitalize on these insights, companies should tailor their marketing strategies to accentuate competitive pricing, stylish designs, high-quality displays, and robust processing capabilities. By emphasizing these strengths, marketing campaigns can effectively communicate the value propositions of their products, showcasing how they excel in critical areas that resonate most with consumers. Conversely, features such as webcam, fan, and charger ranked lowest in priority, indi cating their minimal impact on consumer decision-making. While essential components, their lower ranking suggests they do not significantly differentiate products in the current market. Nonetheless, this highlights an opportunity for innovation. Companies can invest in research and development to reimagine these features, potentially enhancing overall product appeal by adding unexpected value to the user experience.

Aligning strategies with these findings enables notebook manufacturers to optimize resource allocation. They can focus marketing efforts on highlighting strengths in high-priority areas, potentially boosting market appeal and sales. Simultaneously, directing R&D towards improving lower-ranked features can lead to innovative solutions that differentiate products in a competitive market landscape.

## 5. Discussion

The integration of ABSA and TOPSIS methodologies in this study provides a more nuanced understanding of the notebook market than either approach could achieve independently. While ABSA captures the raw emotional responses of consumers toward specific features, it cannot distinguish between sentiments that merely express preferences and those that drive actual purchase decisions. TOPSIS addresses this limitation by incorporating expert knowledge to weight the relative importance of different sentiments. This methodological synthesis reveals critical market insights: features that generate strong emotional responses do not necessarily influence purchase decisions proportionally, and conversely, features with moderate sentiment scores may be decisive factors in consumer choice. This integrated approach enables manufacturers to avoid misallocating resources based solely on sentiment intensity and instead focus on features that genuinely drive market behavior.

Table 7. TOPSIS-based prioritization ranking of 16 notebook features.

<table><tr><td>Rank</td><td>Notebook Feature</td><td>TOPSIS Score</td></tr><tr><td>1</td><td>Price</td><td>0.6266</td></tr><tr><td>2</td><td>Design</td><td>0.5894</td></tr><tr><td>3</td><td>Display</td><td>0.589</td></tr><tr><td>4</td><td>CPU</td><td>0.5731</td></tr><tr><td>5</td><td>RAM</td><td>0.561</td></tr><tr><td>6</td><td>Storage</td><td>0.4998</td></tr><tr><td>7</td><td>Battery</td><td>0.4996</td></tr><tr><td>8</td><td>Warranty</td><td>0.4598</td></tr><tr><td>9</td><td>Weight</td><td>0.4292</td></tr><tr><td>10</td><td>GPU</td><td>0.4118</td></tr><tr><td>11</td><td>Size</td><td>0.3906</td></tr><tr><td>12</td><td>Port</td><td>0.3271</td></tr><tr><td>13</td><td>Keyboard</td><td>0.3122</td></tr><tr><td>14</td><td>Webcam</td><td>0.2208</td></tr><tr><td>15</td><td>Fan</td><td>0.1723</td></tr><tr><td>16</td><td>Charger</td><td>0.1359</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t007

The complementary nature of these methodologies becomes evident when examining specific findings. ABSA identified genuine consumer pain points such as cooling systems and battery chargers with predominantly negative sentiments, while TOPSIS contextualized these findings by revealing that despite strong negative responses, these features have minimal impact on purchase decisions compared to core attributes like price and display quality. This dual-perspective analysis prevents manufacturers from overinvesting in addressing issues that, while generating user frustration, do not significantly influence purchasing behavior.

The TOPSIS prioritization results presented in Table 8 reveal important insights about brand-specific strengths and market positioning. Rather than suggesting all brands should pursue identical strategies, these results highlight each brand’s unique competitive advantages and natural differentiation opportunities.

For premium positioning, Apple and Microsoft show distinct patterns where design and display quality rank highly, aligning with their focus on creative professionals and business users. Apple’s lower emphasis on price (ranking 2nd) reflects its established premium brand equity, while Microsoft’s similar pattern supports its Surface line’s positioning as productivity-focused devices.

In the value segment, brands like Acer and Asus show price and RAM as top priorities, consistent with their strategy of offering performance-oriented machines at competitive prices. Acer’s top ranking of RAM reflects its gaming laptop focus, while Asus balances price with display quality to serve both budget-conscious and enthusiast markets.

For business-oriented brands, Lenovo’s unique prioritization of display quality over price aligns with its ThinkPad heritage of serving professional users who value screen quality for extended work sessions. Dell and HP show similar patterns with price leading, reflecting their broad market approach spanning from entry-level to premium segments.

These brand-specific patterns suggest that rather than converging on a single “ideal” notebook profile, manufacturers should leverage their existing strengths. Lenovo should continue emphasizing its superior displays, Apple should maintain its design excellence, and value brands should focus on delivering performance at attractive price points. The data supports differentiation rather than homogenization.

Table 8. The results of TOPSIS prioritization by brands.

<table><tr><td>Rank</td><td>Acer</td><td>Apple</td><td>Asus</td><td>Dell</td><td>HP</td><td>Lenovo</td><td>Microsoft</td></tr><tr><td>1</td><td>RAM</td><td>Price</td><td>Price</td><td>Price</td><td>Price</td><td>Display</td><td>Price</td></tr><tr><td>2</td><td>Display</td><td>Display</td><td>Display</td><td>Display</td><td>Display</td><td>Price</td><td>Display</td></tr><tr><td>3</td><td>Price</td><td>CPU</td><td>RAM</td><td>CPU</td><td>RAM</td><td>RAM</td><td>CPU</td></tr><tr><td>4</td><td>CPU</td><td>RAM</td><td>CPU</td><td>RAM</td><td>CPU</td><td>CPU</td><td>RAM</td></tr><tr><td>5</td><td>Storage</td><td>Storage</td><td>Storage</td><td>Battery</td><td>Battery</td><td>Battery</td><td>Storage</td></tr><tr><td>6</td><td>Battery</td><td>Battery</td><td>Battery</td><td>Storage</td><td>Storage</td><td>Storage</td><td>Battery</td></tr><tr><td>7</td><td>Warranty</td><td>Warranty</td><td>Warranty</td><td>Warranty</td><td>Design</td><td>Design</td><td>Warranty</td></tr><tr><td>8</td><td>Design</td><td>Design</td><td>Design</td><td>Design</td><td>Warranty</td><td>Warranty</td><td>Design</td></tr><tr><td>9</td><td>Size</td><td>GPU</td><td>Weight</td><td>Weight</td><td>Weight</td><td>Weight</td><td>GPU</td></tr><tr><td>10</td><td>Weight</td><td>Weight</td><td>GPU</td><td>Size</td><td>GPU</td><td>GPU</td><td>Weight</td></tr><tr><td>11</td><td>GPU</td><td>Size</td><td>Size</td><td>GPU</td><td>Size</td><td>Size</td><td>Size</td></tr><tr><td>12</td><td>Keyboard</td><td>Port</td><td>Keyboard</td><td>Port</td><td>Port</td><td>Port</td><td>Keyboard</td></tr><tr><td>13</td><td>Port</td><td>Keyboard</td><td>Port</td><td>Keyboard</td><td>Keyboard</td><td>Keyboard</td><td>Port</td></tr><tr><td>14</td><td>Fan</td><td>Fan</td><td>Fan</td><td>Fan</td><td>Webcam</td><td>Webcam</td><td>Charger</td></tr><tr><td>15</td><td>Webcam</td><td>Charger</td><td>Webcam</td><td>Webcam</td><td>Fan</td><td>Fan</td><td>Webcam</td></tr><tr><td>16</td><td>Charger</td><td>Webcam</td><td>Charger</td><td>Charger</td><td>Charger</td><td>Charger</td><td>Fan</td></tr></table>

https://doi.org/10.1371/journal.pone.0342067.t008

In conclusion, the TOPSIS prioritization results offer a data-driven framework for notebook manufacturers to align their marketing and R&D strategies with consumer preferences. By emphasizing their strengths in high-priority areas through targeted marketing campaigns and addressing weaknesses through focused innovation, companies can potentially enhance their market position. However, this approach should be complemented by a holistic understanding of market dynamics, consumer behavior, and brand-specific factors to develop truly effective and sustainable strategies in the highly competitive notebook industry.

## 5.1. Managerial Insights and Implementation

The findings of this research offer valuable insights for notebook manufacturers and marketers, providing a data-driven approach to enhance their competitive positioning in the market. The TOPSIS prioritization results, coupled with sentiment analysis from social media and expert evaluations, present a comprehensive framework for strategic decision-making within each brand’s unique market context.

The analysis reveals that while certain features consistently rank highly across brands, such as price, display quality, and core performance components, the specific prioritization patterns align with and validate each brand’s existing market positioning. This differentiation is not a weakness to be corrected but rather a strength that reflects the diverse needs of the notebook market. For instance, Apple’s emphasis on design excellence serves creative professionals, Lenovo’s display quality focus aligns with business users’ extended work sessions, while Acer’s RAM prioritization supports gaming enthusiasts’ performance needs.

Given these brand-specific patterns, manufacturers should interpret our findings as optimization guidance within their chosen market segments rather than universal prescriptions. The following insights should be adapted to each brand’s strategic context:

Regarding pricing strategies, while price ranks consistently high, its implementation varies by segment. Premium brands like Apple can maintain higher price points justified by design and ecosystem integration, while value-focused brands like Acer and Asus should continue optimizing cost structures to offer competitive pricing without compromising their performance advantages.

For display technology, the high consumer priority suggests all brands should invest in this area, but through different approaches. Business-oriented brands might focus on color accuracy and eye-comfort technologies, gaming brands on refresh rates and response times, while creative-focused brands on color gamut and resolution.

Core performance features (RAM, CPU) remain fundamental, but their emphasis should align with use cases. Gaming and performance brands should pursue cutting-edge specifications, while ultrabook manufacturers might balance performance with efficiency and thermal management.

The consistently low ranking of features like webcams, fans, and chargers presents differentiation opportunities precisely because they are overlooked. A brand could distinguish itself by transforming these “hygiene factors” into compet itive advantages, for instance, superior cooling enabling sustained performance, or professional-grade webcams for the remote work era.

To effectively implement these strategies within their market positions, manufacturers should:

I. Regularly conduct sentiment analysis on social media platforms, filtering insights by their target demographic rather than the general market.

II. Establish cross-functional teams that understand both the brand’s strategic positioning and evolving consumer prefer ences within their segment.

III. Develop product roadmaps that strengthen existing brand advantages while selectively addressing weaknesses that matter to their specific consumer base.

IV. Create marketing campaigns that resonate with their target segment’s priorities rather than attempting to appeal to all consumers.

V. Monitor both direct competitors within their segment and potential disruptors from adjacent segments.

By leveraging these insights through the lens of their established market positions, notebook manufacturers can strengthen their differentiation, better serve their target consumers, and maintain sustainable competitive advantages in distinct market segments.

## 6. Conclusion

This research successfully developed and validated a novel hybrid framework for analyzing consumer preferences in the notebook market by integrating three key components: aspect-based sentiment analysis of social media data, expert evaluations through fuzzy logic, and feature prioritization using TOPSIS methodology. The framework effectively addressed the primary research objectives by establishing a systematic approach for real-time analysis of consumer sentiments across multiple notebook features, quantifying expert knowledge through fuzzy logic implementation, and developing a reproducible method for feature prioritization across different brands.

The study’s empirical validation, analyzing 329,091 tweets across seven major brands (Asus, Acer, Apple, Dell, HP, Lenovo, and Microsoft), demonstrated the framework’s effectiveness in identifying and ranking consumer preferences. The ABSA component successfully extracted sentiments toward 16 key notebook attributes, revealing that design, weight, GPU, and CPU received predominantly positive feedback, while cooling systems and battery chargers emerged as primary pain points across brands. The integration of expert evaluations through fuzzy logic provided crucial context about which sentiments translate into actual purchasing behavior, bridging the gap between stated and revealed consumer preferences.

The TOPSIS-based prioritization revealed that price, display quality, CPU performance, RAM capacity, and design constitute the most influential factors in notebook purchasing decisions. Importantly, the brand-specific analysis demonstrated distinct prioritization patterns that align with each manufacturer’s market positioning: Lenovo’s emphasis on display quality reflects its business-oriented focus, Apple’s design prominence aligns with its creative professional target market, and

value-focused brands like Acer and Asus show price and RAM as top priorities consistent with their performance-oriented strategies.

The methodology provides manufacturers with a quantifiable, actionable framework for optimizing product development and marketing strategies. By synthesizing consumer voice captured through social media with expert knowledge of purchase behavior, the framework enables companies to prioritize genuinely purchase-influencing features while addressing critical pain points. The open availability of the dataset on Hugging Face and analytical code on GitHub ensures reproducibility and facilitates future research extensions.

This hybrid approach contributes to both academic literature and industry practice by demonstrating how machine learning-based sentiment analysis can be systematically integrated with structured expert knowledge and multi-criteria decision-making methods. The framework offers a comprehensive blueprint for understanding consumer preferences in dynamic technology markets and can serve as a foundation for similar analyses in other consumer electronics sectors.

## 7. Limitations and future research

While this research provides valuable insights into consumer preferences and brand positioning in the notebook market, several limitations warrant acknowledgment. The study primarily relied on social media data from X (formerly Twitter), which may not fully represent the entire consumer base. Users of this platform may have specific demographic characteristics or usage patterns that could skew the results. Twitter users tend to be younger, more technologically engaged, and potentially more vocal about their opinions compared to the broader consumer population [86,87]. This demographic concentration could introduce selection bias, potentially overrepresenting certain viewpoints while underrepresenting others, such as older consumers or those less active on social media platforms. Furthermore, the non-deterministic nature of the X API presents inherent limitations, as different data collection iterations may yield varying tweet samples even with identical search parameters. However, our large sample size (329,091 tweets) and extended collection period (18 months) help mitigate the impact of such variations on overall findings.

The research focused on a specific time frame (January 2023 to June 2024), which may not capture long-term trends or seasonal variations in consumer sentiment. The notebook market is characterized by rapid technological advancement, with new product releases, operating system updates, and component innovations occurring frequently. Consumer preferences may shift substantially in response to disruptive innovations such as the introduction of new processor architectures, display technologies, or form factors. Additionally, seasonal patterns related to academic calendars, holiday shopping periods, and corporate purchasing cycles may influence sentiment expressions in ways not fully captured by ou study period.

The TOPSIS method, while robust and widely validated in multi-criteria decision-making contexts, assumes independence among criteria. However, notebook features such as CPU performance, RAM capacity, and overall system responsiveness are inherently interrelated [88]. Similarly, design aesthetics and weight considerations often involve trade-offs, as do battery life and processing power. This assumption of independence represents a theoretical simplification that may not fully capture the complex interdependencies and compensatory relationships among notebook attributes. The expert panel, while diverse in terms of geographic representation and professional roles, was limited to 10 professionals. Although this sample size aligns with established practices in fuzzy multi-criteria decision-making studies, it may constrain the breadth of industry insights, particularly regarding specialized market segments such as gaming, professional creative workstations, or enterprise deployments.

Future research could address these limitations through several approaches. A more comprehensive study could incorporate data from multiple social media platforms, specialized technology forums, and e-commerce review sites to provide a more representative sample of consumer opinions. This multi-source approach would capture diverse demographic segments and usage contexts while enabling comparative analysis across different platforms and communities. Longitudinal studies tracking sentiment evolution over extended periods (3–5 years) would enable identification of long-term trends and technological adoption patterns, while real-time sentiment monitoring systems could provide dynamic insights for rapid response to emerging issues or opportunities.

Methodologically, exploring alternative multi-criteria decision-making methods that explicitly model feature interdependencies, such as Analytic Network Process (ANP) or Decision-Making Trial and Evaluation Laboratory (DEMATEL), would address the independence assumption limitation. Integration of machine learning techniques for dynamic feature weighting based on evolving market conditions could enhance adaptability, while hybrid approaches combining conjoint analysis with sentiment analysis could provide deeper insights into feature trade-offs and compensatory decision-making patterns. Enlarging and diversifying the expert panel to include product designers, user experience researchers, and supply chain professionals would enrich the knowledge base, while incorporating direct consumer interviews or focus groups would strengthen the validation of social media findings.

Cross-cultural studies examining how consumer preferences vary across different geographic markets and economic development levels would reveal global patterns, while research segmenting consumers by use case (students, professionals, gamers, content creators) would enable more targeted strategies. Investigating consumer sentiments toward emerging notebook features such as AI-enhanced capabilities, sustainability considerations, modular designs, and repair ability would prepare manufacturers for future market shifts. Finally, validation studies comparing sentiment-based predictions with actual sales data and market share changes would establish the predictive validity of this framework, while benchmarking against traditional market research methods would clarify the relative advantages and limitations of socia media-based approaches.

Through systematic investigation of these directions, researchers can enhance our understanding of consumer preferences in rapidly evolving technology markets while addressing the inherent limitations of current methodologies and developing more robust frameworks for strategic decision-making.

## Author contributions

Conceptualization: Mehrdad Maghsoudi.

Data curation: Mohammadreza Bakhtiari, Hamidreza Bakhtiari.

Formal analysis: Mohammadreza Bakhtiari, Hamidreza Bakhtiari.

Investigation: Mohammadreza Bakhtiari.

Methodology: Mehrdad Maghsoudi.

Project administration: Mehrdad Maghsoudi.

Software: Mohammadreza Bakhtiari.

Validation: Mohammadreza Bakhtiari, Hamidreza Bakhtiari.

Visualization: Mehrdad Maghsoudi, Mohammadreza Bakhtiari.

Writing – original draft: Mehrdad Maghsoudi, Mohammadreza Bakhtiari, Hamidreza Bakhtiari.

Writing – review & editing: Mehrdad Maghsoudi, Mohammadreza Bakhtiari, Hamidreza Bakhtiari.

## References

1. Kozinets RV, Ferreira DA, Chimenti P. How Do Platforms Empower Consumers? Insights from the Affordances and Constraints of Reclame Aqui. J Consum Res. 2021;48(3):428–55. https://doi.org/10.1093/jcr/ucab014

2. Idrees MA, Khan MA, Khan A. Factors Affecting Consumer Buying Behavior For Electronic Notebook. Eur J Bus Manag Res. 2020;5(3).

3. Vera-Martínez J. Consumer technology brands and the source of their performance. Cog Bus Manag. 2021;8(1). https://doi.org/10.1080/23311975.2 021.1969632

4. Sánchez-Núñez P, et al. Opinion mining, sentiment analysis and emotion understanding in advertising: a bibliometric analysis. IEEE Access. 2020;8:134563–76.

5. Yiran Y, Srivastava S. Aspect-based Sentiment Analysis on mobile phone reviews with LDA. In: Proceedings of the 2019 4th International Confer ence on Machine Learning Technologies. 2019.

6. Gupta DK, Ekbal A. IITP: Supervised Machine Learning for Aspect based Sentiment Analysis. In: Proceedings of the 8th International Workshop on Semantic Evaluation (SemEval 2014). 2014.

7. Graham C, Stough R. Consumer perceptions of AI chatbots on Twitter (X) and Reddit: an analysis of social media sentiment and interactive marketing strategies. J Res Inter Market. 2025;19(7):1096–124. https://doi.org/10.1108/jrim-05-2024-0237

8. Roelen-Blasberg T, Habel J, Klarmann M. Automated inference of product attributes and their importance from user-generated content: Can we replace traditional market research?. Int J Res Market. 2023;40(1):164–88. https://doi.org/10.1016/j.ijresmar.2022.04.004

9. Jones JE, Jones LL, Calvert MJ, Damery SL, Mathers JM. A Literature Review of Studies that Have Compared the Use of Face-To-Face and Online Focus Groups. Int J Qual Methods. 2022;21. https://doi.org/10.1177/16094069221142406

10. Zhang H, Zang Z, Zhu H, Uddin MI, Amin MA. Big data-assisted social media analytics for business model for business decision making system competitive analysis. Inform Process Manag. 2022;59(1):102762. https://doi.org/10.1016/j.ipm.2021.102762

11. Nauhaus S, Luger J, Raisch S. Strategic Decision Making in the Digital Age: Expert Sentiment and Corporate Capital Allocation. J Manag Stud. 2021;58(7):1933–61. https://doi.org/10.1111/joms.12742

12. Mariani MM, Fosso Wamba S. Exploring how consumer goods companies innovate in the digital age: The role of big data analytics companies. Journal of Business Research. 2020;121:338–52. https://doi.org/10.1016/j.jbusres.2020.09.012

13. Jeong SC, Choi B-J. Moderating Effects of Consumers’ Personal Innovativeness on the Adoption and Purchase Intention of Wearable Devices. Sage Open. 2022;12(4). https://doi.org/10.1177/21582440221134798

14. Languré ADL, Zareei M. Breaking Barriers in Sentiment Analysis and Text Emotion Detection: Toward a Unified Assessment Framework. IEEE Access. 2023;11:125698–715. https://doi.org/10.1109/access.2023.3331323

15. Graham CM, Lu Y. Skills Expectations in Cybersecurity: Semantic Network Analysis of Job Advertisements. J Comput Inform Syst. 2022;63(4):937– 49. https://doi.org/10.1080/08874417.2022.2115954

16. Maheshwari G. Factors affecting students’ intentions to undertake online learning: an empirical study in Vietnam. Educ Inf Technol (Dordr). 2021;26(6):6629–49. https://doi.org/10.1007/s10639-021-10465-8 PMID: 33686331

17. Yan X. Investigating consumer preferences for laptop computers using Choice-Based Conjoint (CBC) Analysis. SACAD Schol Activit. 2025;2025(2025):32.

18. Prasad RK, Venkatesh S. Understanding customer preferences on laptop variants and models for students and working professionals. Acad Market Stud J. 2022;26(S4).

19. Ren J, Yang J, Liu E, Huang F. Consumers’ willingness to pay premium under the influence of consumer community culture: From the perspective of the content creator. Front Psychol. 2022;13:1009724. https://doi.org/10.3389/fpsyg.2022.1009724 PMID: 36248545

20. Maghsoudi M, Bakhtiari M, Bakhtiari H. Global Perspectives on Laptop Features: A Sentiment Analysis of User Preferences in Developed and Developing Countries. IEEE Access. 2025;13:9102–19. https://doi.org/10.1109/access.2025.3528324

21. Alghamdi S, Alhasawi Y. Aspect-based sentiment analysis in smart devices: A comprehensive and specialized dataset. Data Brief. 2024;55:110642. https://doi.org/10.1016/j.dib.2024.110642 PMID: 39669762

22. Davoodi L, Mezei J, Heikkilä M. Aspect-based sentiment classification of user reviews to understand customer satisfaction of e-commerce plat forms. Electron Commer Res. 2025. https://doi.org/10.1007/s10660-025-09948-4

23. Han H, et al. Aspect-Based Sentiment Analysis Through Graph Convolutional Networks and Joint Task Learning. Information. 2025;16(3):201.

24. Huang B, Ou Y, Carley KM. Aspect level sentiment classification with attention-over-attention neural networks. In: International conference on social computing, behavioral-cultural modeling and prediction and behavior representation in modeling and simulation. Springer; 2018.

25. Li S, Liu F, Zhang Y, Zhu B, Zhu H, Yu Z. Text Mining of User-Generated Content (UGC) for Business Applications in E-Commerce: A Systematic Review. Mathematics. 2022;10(19):3554. https://doi.org/10.3390/math10193554

26. Sykora M, Elayan S, Hodgkinson IR, Jackson TW, West A. The power of emotions: Leveraging user generated content for customer experience management. Journal of Business Research. 2022;144:997–1006. https://doi.org/10.1016/j.jbusres.2022.02.048

27. Žitnik S, Blagus N, Bajec M. Target-level sentiment analysis for news articles. Knowl-Based Syst. 2022;249:108939. https://doi.org/10.1016/j. knosys.2022.108939

28. Medhat W, Hassan A, Korashy H. Sentiment analysis algorithms and applications: A survey. Ain Shams Eng J. 2014;5(4):1093–113. https://doi. org/10.1016/j.asej.2014.04.011

29. van Zyl BJ. A generic framework for aspect-based sentiment analysis. 2023.

30. Bensoltane R, Zaki T. Aspect-based sentiment analysis: an overview in the use of Arabic language. Artif Intell Rev. 2022;56(3):2325–63. https://doi. org/10.1007/s10462-022-10215-3

31. de León Languré A, Zareei M. Evaluating the Effect of Emotion Models on the Generalizability of Text Emotion Detection Systems. IEEE Access. 2024;12:70489–500. https://doi.org/10.1109/access.2024.3401203

32. Pannala NU, Nawarathna CP, Jayakody JTK, Rupasinghe L, Krishnadeva K. Supervised Learning Based Approach to Aspect Based Sentiment Analysis. In: 2016 IEEE International Conference on Computer and Information Technology (CIT). IEEE; 2016.

33. Zareei M, et al. A comprehensive review of automatic methods for suicidal ideation detection. 2025.

34. Do HH, Prasad P, Maag A, Alsadoon A. Deep Learning for Aspect-Based Sentiment Analysis: A Comparative Review. Expert Syst Appl. 2019;118:272–99. https://doi.org/10.1016/j.eswa.2018.10.003

35. Xue W, Li T. Aspect based sentiment analysis with gated convolutional networks. arXiv preprint arXiv:1805.07043. 2018.

36. Xu H, et al. BERT post-training for review reading comprehension and aspect-based sentiment analysis. arXiv preprint arXiv:1904.02232. 2019.

37. Phan MH, Ogunbona PO. Modelling Context and Syntactical Features for Aspect-based Sentiment Analysis. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. 2020.

38. Ozyurt B, Akcayol MA. A new topic modeling based approach for aspect extraction in aspect based sentiment analysis: SS-LDA. Expert Syst Appl. 2021;168:114231. https://doi.org/10.1016/j.eswa.2020.114231

39. García-Pablos A, Cuadros M, Rigau G. W2VLDA: Almost unsupervised system for Aspect Based Sentiment Analysis. Expert Syst Appl. 2018;91:127–37. https://doi.org/10.1016/j.eswa.2017.08.049

40. Ruder S, Ghaffari P, Breslin JG. A hierarchical model of reviews for aspect-based sentiment analysis. arXiv preprint arXiv:1609.02745. 2016.

41. Liu Q, et al. Content attention model for aspect based sentiment analysis. In: Proceedings of the 2018 World Wide Web Conference. 2018.

42. Jiang Q, et al. A challenge dataset and effective models for aspect-based sentiment analysis. In: Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP). 2019.

43. Peng H, Xu L, Bing L, Huang F, Lu W, Si L. Knowing What, How and Why: A Near Complete Solution for Aspect-Based Sentiment Analysis. AAAI. 2020;34(05):8600–7. https://doi.org/10.1609/aaai.v34i05.6383

44. Nazir A, Rao Y, Wu L, Sun L. Issues and Challenges of Aspect-based Sentiment Analysis: A Comprehensive Survey. IEEE Trans Affective Comput. 2022;13(2):845–63. https://doi.org/10.1109/taffc.2020.2970399

45. Zhang W, Li X, Deng Y, Bing L, Lam W. A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, and Challenges. IEEE Trans Knowl Data Eng. 2023;35(11):11019–38. https://doi.org/10.1109/tkde.2022.3230975

46. Sann R, Lai P-C. Understanding homophily of service failure within the hotel guest cycle: Applying NLP-aspect-based sentiment analysis to the hospitality industry. Int J Hosp Manag. 2020;91:102678. https://doi.org/10.1016/j.ijhm.2020.102678

47. Tran T, Ba H, Huynh V-N. Measuring hotel review sentiment: An aspect-based sentiment analysis approach. In: International symposium on integrated uncertainty in knowledge modelling and decision making. Springer; 2019.

48. Alqaryouti O, Siyam N, Abdel Monem A, Shaalan K. Aspect-based sentiment analysis using smart government review data. ACI. 2020;20(1/2):142– 61. https://doi.org/10.1016/j.aci.2019.11.003

49. Gräßer F, Kallumadi S, Malberg H, Zaunseder S. Aspect-Based Sentiment Analysis of Drug Reviews Applying Cross-Domain and Cross-Data Learning. In: Proceedings of the 2018 International Conference on Digital Health. 2018.

50. Alturaief N, Aljamaan H, Baslyman M. AWARE: Aspect-Based Sentiment Analysis Dataset of Apps Reviews for Requirements Elicitation. In: 2021 36th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW). IEEE; 2021.

51. Rodrigues AP, Chiplunkar NN. Aspect Based Sentiment Analysis on Product Reviews. In: 2018 Fourteenth International Conference on Information Processing (ICINPRO). IEEE; 2018.

52. Sivakumar M, Reddy US. Aspect based sentiment analysis of students opinion using machine learning techniques. In: 2017 International Conference on Inventive Computing and Informatics (ICICI). 2017. 726–31. https://doi.org/10.1109/icici.2017.8365231

53. Al-Ayyoub M, et al. Aspect-based sentiment analysis of Arabic laptop. In: ACIT’2017, The International Arab Conference on Information Technology. 2017.

54. Li H, Yu BXB, Li G, Gao H. Restaurant survival prediction using customer-generated content: An aspect-based sentiment analysis of online reviews. Tour Manag. 2023;96:104707. https://doi.org/10.1016/j.tourman.2022.104707

55. Zavadskas EK, Turskis Z, Kildienė S. State of art surveys of overviews on mcdm/madm methods. Technol Econ Dev Econom. 2014;20(1):165–79. https://doi.org/10.3846/20294913.2014.892037

56. Zadeh LA. Fuzzy sets. Inform Contr. 1965;8(3):338–53. https://doi.org/10.1016/s0019-9958(65)90241-x

57. Serrano-Guerrero J, Romero FP, Olivas JA. Fuzzy logic applied to opinion mining: A review. Knowl-Based Syst. 2021;222:107018. https://doi. org/10.1016/j.knosys.2021.107018

58. Naimi M, Tahayori H, Sadeghian A. A fast and accurate method for calculating the center of gravity of polygonal interval type-2 fuzzy sets. IEEE Trans Fuzzy Syst. 2020;29(6):1472–83.

59. Peckol JK. Introduction to fuzzy logic. John Wiley & Sons; 2021.

60. Hwang CL, Yoon K. Methods for multiple attribute decision making. Multiple attribute decision making: methods and applications a state-of-the-art survey. Springer; 1981. p. 58–191.

61. Kumar P, Sarkar P. A comparison of the AHP and TOPSIS multi-criteria decision-making tools for prioritizing sub-watersheds using morphometric parameters’ analysis. Model Earth Syst Environ. 2022;8(3):3973–83. https://doi.org/10.1007/s40808-021-01334-x

62. Tamošaitienė J, Khosravi M, Cristofaro M, Chan DWM, Sarvari H. Identification and Prioritization of Critical Risk Factors of Commercial and Recreational Complex Building Projects: A Delphi Study Using the TOPSIS Method. Appl Sci. 2021;11(17):7906. https://doi.org/10.3390/app11177906

63. Maghsoudi M, Mohammadi N, Bakhtiari M. A novel approach to customer segmentation for product development on social media data: integrating aspect-based sentiment analysis and text mining. Knowl-Based Syst. 2025;328:114269. https://doi.org/10.1016/j.knosys.2025.114269

64. Maghsoudi M, Mohammadi N, Bakhtiari M. Artificial Intelligence and Sustainable Development: Public Concerns and Governance in Developed and Developing Nations. Clean Environ Syst. 2025;100340.

65. Roma P, Aloini D. How does brand-related user-generated content differ across social media? Evidence reloaded. J Bus Res. 2019;96:322–39. https://doi.org/10.1016/j.jbusres.2018.11.055

66. Zhuang W, Zeng Q, Zhang Y, Liu C, Fan W. What makes user-generated content more helpful on social media platforms? Insights from creato interactivity perspective. Inform Processi Manag. 2023;60(2):103201. https://doi.org/10.1016/j.ipm.2022.103201

67. Ikwu R, Giommoni L, Javed A, Burnap P, Williams M. Digital fingerprinting for identifying malicious collusive groups on Twitter. J Cybersecur. 2023;9(1). https://doi.org/10.1093/cybsec/tyad014

68. Shahidzadeh MH, Shokouhyar S. Shedding light on the reverse logistics’ decision-making: a social-media analytics study of the electronics industry in developing vs developed countries. Int J Sustain Eng. 2022;15(1):161–76. https://doi.org/10.1080/19397038.2022.2101706

69. Müller K, Schwarz C. From Hashtag to Hate Crime: Twitter and Antiminority Sentiment. Am Econ J Appl Econ. 2023;15(3):270–312. https://doi. org/10.1257/app.20210211

70. Zhang L, Wang S, Liu B. Deep learning for sentiment analysis: A survey. WIREs Data Mining Knowl. 2018;8(4):e1253.

71. Yang H, Zhang C, Li K. PyABSA: A Modularized Framework for Reproducible Aspect-based Sentiment Analysis. In: Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, 2023. 5117–22. https://doi.org/10.1145/3583780.3614752

72. Ballas V, et al. Automating mobile app review user feedback with aspect-based sentiment analysis. In: International Conference on Human-Computer Interaction. Springer; 2024.

73. Tudi MR, et al. Aspect-Based Sentiment Analysis of Racial Issues in Singapore: Enhancing Model Performance Using ChatGPT. In: International Conference on Asian Digital Libraries. Springer; 2023.

74. Yang H, Li K. PyABSA: open framework for aspect-based sentiment analysis. arXiv preprint arXiv:2208.01368. 2022. 475 p.

75. Nanba H, Fukuda S. Automatic detection of geotagged food-related videos using aspect-based sentiment analysis. In: RecTour@ RecSys. 2023.

76. Gilly MC, Graham JL, Wolfinbarger MF, Yale LJ. A Dyadic Study of Interpersonal Information Search. J Acad Market Sci. 1998;26(2):83–100. https://doi.org/10.1177/0092070398262001

77. Solomon MR. The Missing Link: Surrogate Consumers in the Marketing Chain. J Market. 1986;50(4):208–18. https://doi. org/10.1177/002224298605000406

78. Weitz BA, Sujan H, Sujan M. Knowledge, Motivation, and Adaptive Behavior: A Framework for Improving Selling Effectiveness. J Market. 1986;50(4):174–91. https://doi.org/10.1177/002224298605000404

79. Homburg C, Wieseke J, Bornemann T. Implementing the Marketing Concept at the Employee–Customer Interface: The Role of Customer Need Knowledge. J Market. 2009;73(4):64–81. https://doi.org/10.1509/jmkg.73.4.64

80. Kahneman D, Tversky A. Prospect theory: An analysis of decision under risk. In: Handbook of the fundamentals of financial decision making: Part I. World Scientific; 2013. p. 99–127.

81. Bettman JR, Luce MF, Payne JW. Constructive Consumer Choice Processes. J Consum Res. 1998;25(3):187–217. https://doi.org/10.1086/209535

82. Zadeh LA. Fuzzy logic. In: Granular, Fuzzy, and Soft Computing. Springer; 2023. p. 19–49.

83. Román-Flores H, Chalco-Cano Y, Figueroa-García JC. A note on defuzzification of type-2 fuzzy intervals. Fuzzy Sets Syst. 2020;399:133–45.

84. Wu P, Zhou L, Chen H, Zhou H. An improved fuzzy risk analysis by using a new similarity measure with center of gravity and area of trapezoidal fuzzy numbers. Soft Comput. 2019;24(6):3923–36. https://doi.org/10.1007/s00500-019-04160-7

85. Arman H. A simple noniterative method to accurately calculate the centroid of an interval type‐2 fuzzy set. Int J Intelligent Sys. 2022;37(12):12057– 84. https://doi.org/10.1002/int.23076

86. Blank G. The Digital Divide Among Twitter Users and Its Implications for Social Research. Soc Sci Comput Rev. 2016;35(6):679–97. https://doi. org/10.1177/0894439316671698

87. Mellon J, Prosser C. Twitter and Facebook are not representative of the general population: Political attitudes and demographics of British social media users. Res Pol. 2017;4(3). https://doi.org/10.1177/2053168017720008

88. Chen S-J, Hwang C-L. Fuzzy multiple attribute decision making methods and applications. книга. 1992.