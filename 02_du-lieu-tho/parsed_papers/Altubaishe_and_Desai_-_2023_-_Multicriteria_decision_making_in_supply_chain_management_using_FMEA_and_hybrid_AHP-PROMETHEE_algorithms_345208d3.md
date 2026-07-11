Article

# Multicriteria Decision Making in Supply Chain Management Using FMEA and Hybrid AHP-PROMETHEE Algorithms

Bandar Altubaishe <sup>1</sup> and Salil Desai <sup>2,3,</sup>\*

Department of Supply Chain Management, University of Business and Technology, University of Business and Technology St, Jeddah 23847, Saudi Arabia; b.altubaishe@ubt.edu.sa

2 Department of Industrial and Systems Engineering, North Carolina Agricultural and Technica State University, Greensboro, NC 27411, USA

3 Center of Excellence in Product Design and Advanced Manufacturing, North Carolina Agricultural and Technical State University, Greensboro, NC 27411, USA

Correspondence: sdesai@ncat.edu; Tel.: +1-(336)-285-3725

![](images/8ddb79d7fd96c2874675dfff539bda4c98f6f5a1b59eb443c94a7606f455cf6a.jpg)

Citation: Altubaishe, B.; Desai, S. Multicriteria Decision Making in Supply Chain Management Using FMEA and Hybrid AHP-PROMETHEE Algorithms. Sensors 2023, 23, 4041. https:// doi.org/10.3390/s23084041

Academic Editor: Longfei Zhou

Received: 8 March 2023 Revised: 8 April 2023 Accepted: 11 April 2023 Published: 17 April 2023

![](images/293baa85ac1c096b4f9c4c4cc071ce6719feeb2375c4f351ddb0d4f95ef596f2.jpg)

Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

Abstract: In today’s global environment, supplier selection is one of the critical strategic decisions made by supply chain management. The supplier selection process involves the evaluation of suppli ers based on several criteria, including their core capabilities, price offerings, lead times, geographical proximity, data collection sensor networks, and associated risks. The ubiquitous presence of internet of things (IoT) sensors at different levels of supply chains can result in risks that cascade to the upstream end of the supply chain, making it imperative to implement a systematic supplier selection methodology. This research proposes a combinatorial approach for risk assessment in supplier selection using the failure mode effect analysis (FMEA) with hybrid analytic hierarchy process (AHP) and the preference ranking organization method for enrichment evaluation (PROMETHEE). The FMEA is used to identify the failure modes based on a set of supplier criteria. The AHP is imple mented to determine the global weights for each criterion, and PROMETHEE is used to prioritize the optimal supplier based on the lowest supply chain risk. The integration of multicriteria decision making (MCDM) methods overcomes the shortcomings of the traditional FMEA and enhances the precision of prioritizing the risk priority numbers (RPN). A case study is presented to validate the combinatorial model. The outcomes indicate that suppliers were evaluated more effectively based on company chosen criteria to select a low-risk supplier over the traditional FMEA approach. This research establishes a foundation for the application of multicriteria decision-making methodology for unbiased prioritization of critical supplier selection criteria and evaluation of different supply chain suppliers.

Keywords: analytical hierarchy process (AHP); failure mode and effects analysis (FMEA); internet of things (IoT) sensors; preference ranking organization method for enrichment evaluation (PROMETHEE); supply chain risk management

## 1. Introduction

With the emergence of new challenges, such as trade wars [1], infectious diseases [2], global warming [3], trade protectionism [4], and rapid technology developments in automation, artificial intelligence [5–8], internet of things (IoT) sensor [9] virtual reality [10], additive manufacturing [11–16], big data [17], and blockchain technology [18], supply chains are evolving to a new dimension. In this context, supplier selection is considered one of the most important strategic decisions to be made by supply chain management (SCM). Manufacturing firms in the U.S. expend substantial financial resources on goods and services. For example, Toyota’s annual purchasing of parts, materials, goods, and services from North American suppliers totaled nearly \$32 billion [19]. This significant purchasing expenditure makes a company’s success depend on its right selection of suppliers. By selecting the right supplier, companies can save material costs, increase profits, gain a competitive advantage, and reduce disruption risks. On the other hand, selecting the wrong supplier can result in a variety of problems, such as long lead–times, stock–outs, and the inability to meet customer demand, thereby incurring additional costs [20]. These problems can negatively impact the financial performance of a firm. The COVID–19 pandemic has unprecedentedly disrupted the supply chains (SCs) across the world and has provided an opportunity to test the resilience of both traditional and green suppliers. The flow of both essential and non–essential goods and services has been severely affected [21]. Therefore, understanding the basic requirements for suppliers and having a meaningful evaluation criteria system for optimal supplier selection is paramount.

The Internet of Things (IoT) technology is the fourth industrial revolution, and the application of IoT sensors across industry is having a significant impact on value creation and revenue streams [22]. An IoT-enabled supply chain is visualized as an intelligent interconnected sensor network that connects multiple tiers of suppliers, contract manu facturers, service providers, distributors, and customers, physically located in different regions of the world [23]. Businesses are using IoT sensors by giving identification tags to their goods/things and connecting relevant information/data from these things to the cloud over the internet [24]. Centrally uploaded data becomes readily available worldwide, and their associated organizations/suppliers/vendors can be contacted for purchase. The IoT sensors and network integration can provide seamless linking between vendors by amassing real-time data, as well as by augmenting visibility of raw materials, finished good, and, finally, by providing real-time quality control on logistics to maximize revenue streams [25]. Thus, IoT–enabled sensor systems drive cost containment, as well as improve time-to-market capabilities in today’s business environment. In essence, the availability of IoT-enabled real-time data can allow stakeholders to make informed decisions at both operational and strategic levels.

However, most supply chain managers agree that there is no one best way to evaluate and select suppliers with the copious amounts of data being collected across different supply chain tiers by IoT sensors [26]. Dickson [27], for instance, identified 23 different criteria for selecting suppliers, including quality, delivery, performance history, warranties, price, technical capability, and financial position. However, he indicated that quality and delivery are more important than the rest of the 21 criteria. On the other hand, Ellram [28] distinguished between the criteria used for a partnership type of relationship with potential suppliers and the criteria used for traditional buyer–supplier relationships. Weber et al. [29] reviewed 74 different articles to classify criteria and analytical methods for vendor selection into three categories: linear weighting methods, mathematical programming models, and statistical approaches. Boran et al. [30] identified four stages for supplier selection, including (1) definition of the problem, (2) formulation of criteria, (3) qualification, and (4) final selection, respectively. Regardless of the method utilized to evaluate and select a supplier, the goal of the selection process is to reduce purchasing risk and maximize overall value to the company [26]. The vendor with the IoT-enabled process eliminates visibility gaps and injects enormous flexibility into the supply chain network. This criterion is a crucial concern nowadays. Supply chain risk management (SCRM), on the other hand, is one of the key components that contribute to the firm’s success. Supply chain risks can be reduced to a great extent by implementing IoT sensors across multiple tiers and assessing the risks associated with the supplier selection process [31]. Therefore, this research aims to model and optimize the risk assessment in supplier selection.

There are several techniques available for risk assessment. In our research, we utilized the failure mode and effects analysis (FMEA). FMEA is a widely used engineering analysis technique for preventing errors. FMEA also is performed to identify, prioritize, and eliminate known and potential failures, problems and errors in systems, and products or processes before they reach customers [32]. Moreover, FMEA is a structured technique that can help in identifying all failure modes within a system. The traditional FMEA is solely based on the risk priority number (RPN). The RPN prioritizes the identified potential failure modes. The RPN is computed by multiplying the scores of risk factors. These factors include severity (S), occurrence (O), and detection (D). FMEA has been utilized in a wide range of fields, such as aerospace, chemical, military, automobile, electrical, mechanical, and semiconductor industries [32]. Although this technique has been widely used across different industries, it has limitations. Chang et al. [33] and Liu et al. [34] introduced five issues encountered with RPN in the FMEA method. A key limitation is that different combinations of risk factors may produce the same value of RPN. For example, two different failure modes with values of 4, 3, and 1 and 6, 1, and 2 for (S), (O), and (D), respectively, will have the same RPN as 12. This can result in ambiguity to prioritize different failure modes in supplier selection. Most managers are concerned about the inconsistencies in the ranking of severity, occurrence, and detection attributes and thus may defer FMEA utilization as an assessment tool in a supply chain. Managers are seeking a systematic procedure for rectifying these problems in the FMEA method to integrate the FMEA process into supply chain risk management [34]. In order to overcome the limitations inherent in the traditional FMEA, this research proposes an integration of multi–criteria decision–making (MCDM) methods with FMEA.

The supplier selection process involves evaluating a large number of suppliers with different capabilities, inherent limitations, geographical locations, intelligent sensor net works, modes of communication, and associated risks. In addition, this selection process generally relies significantly on subjective judgment. Since the supplier selection process involves the evaluation of different criteria and supplier attributes, it can be considered as a multiple criteria decision-making (MCDM) problem [35]. According to Heller [36], using MCDM in risk assessment has proved its effectiveness and reported many advantages, such as supporting the compression of alternatives by using decision matrices and developing a structured method to rank the alternatives. Among different types of MCDM approaches, the analytic hierarchy process (AHP) and the preference ranking organization method for enrichment evaluation (PROMETHEE) are used to enhance the precision of prioritizing failure modes. AHP is used to determine the global weights for each criterion, and the PROMETHEE is implemented to rank suppliers based on the highest net outranking value (lowest supply chain risk). This research establishes a foundation for the application of a multi-criteria decision-making methodology for unbiased prioritization of critical supplier selection criteria and evaluation of different supply chain suppliers. In addition, it provides a supply chain risk assessment tool with high flexibility for supplier selection.

## 2. The Literature Review

The supplier selection process is considered as one of the most important responsibili ties of supply chain management within a corporation, especially with the introduction of IoT-based sensing systems [37]. This process has been subject to widespread concep tual and empirical studies in the business management literature [38]. Generally, when a supplier selection decision needs to be made, supply chain management focuses on two aspects. The first aspect focuses on identifying key criteria to be used to evaluate potential suppliers. The second aspect involves determining the evaluation methods to be used to compare different suppliers [39]. The criteria considered in supplier evaluation are industry-specific [40]. In other words, the selection of criteria can be adapted based on the requirements of each industry with data acquisition and augmentation using edge-based sensors. Thus, the following literature review focuses on different methods used to resolve the supplier selection problem.

## Supplier Selection Method

Several studies have been conducted for supplier selection using multicriteria decisionmaking (MCDM) [41]. In addition, supplier selection problems have been approached by other techniques, including the analytic hierarchy process (AHP), analytic network process (ANP), data envelopment analysis (DEA), fuzzy sets theory (FST), genetic algorithm (GA), goal programming (GP), and simple multi-attribute rating technique (SMART) [42].

However, few researchers have proposed the integration of FMEA with MCDM methods to solve supplier selection problems as a risk mitigation strategy.

Braglia [43] proposed a new method based on AHP. This method is a multi-attribute failure mode analysis (MAFMA). In this work, FMEA risk factors, such as severity, occurrence, detectability, and expected cost, are considered as decision attributes. Additionally, the causes of failure are considered as alternatives, and the selection of the causes of failure are considered the main objective. Both attributes and alternatives constitute a hierarchical structure of three levels. A comparison matrix was used to calculate the weight of these attributes and the priorities of the causes based on the respective expected cost. In addition, Braglia et al. [44] introduced a new method to estimate the risk priority number (RPN) based on the fuzzy approach of the technique for order preference by similarity to ideal solution (TOPSIS). In Braglia et al.’s [44] study, TOPSIS was used because it allows measurement of the Euclidean distance of an alternative from an ideal objective to improve the risk assessment processes in traditional FMEA. Moreover, a fuzzy logic of TOPSIS was developed to directly evaluate the crisp linguistic assessment of FMEA risk factors (O, S, D) by eliminating the possible errors and uncertainty.

Chin et al. [45] suggested a new FMEA technique using a group-based evidential reasoning approach in order to capture the diversity, incompleteness, and uncertainty of information provided by FMEA team members. This technique allows FMEA team members to assess risk factors independently and present their ideas individually. This method aggregates risk factors using belief structure at individual levels to generate risk scores in a comprehensive manner. Chamodrakas et al. [46] used a fuzzy analytic hierarchy process (F-AHP) approach for supplier selection in electronic marketplaces. In this study, enforcement of hard constraints on the selection criteria and an application of a modified F-AHP performed on supplier selection were introduced in order to reduce computational complexity. In addition, the use of the F-AHP method facilitates an easier elicitation of user preferences through the reduction of necessary user input.

Yang et al. [47] introduced a modified evidence theory that deals with the multiple evaluations of the risk conducted by experts. This technique deals with different opinions of the FEMA team and multiple failure modes. It also provides simplified discernment frames according to practical engineering applications. The risk factors were fused together as discrete random variables, wherein the RPN was a function of their probabilities. The failure modes were prioritized for their risks based on the mean value of the RPN. This proposed technique was applied to aircraft turbine rotor blades, in which the information of eight failures was evaluated by three different expertises and aggregated together. The result indicated that the risk ranking of the failure modes was consistent with the practical engineering background.

Shaw et al. (2012) used a combination of fuzzy AHP and fuzzy objective linear programming to select the best supplier in order to develop a low-carbon supply chain. The top criteria included in Shaw et al.’s study were cost, demand, gas emission, quality, rejection percentage, the percentage of late delivery, and the greenhouse effect. F–AHP was used to determine the weights of predetermined criteria, and fuzzy objective linear programming was used to select the best supplier.

Chen and Wu [48] proposed a modified failure mode and effects analysis method for selection problems in the supply chain risk environment (MFMEA). They applied the AHP method to determine the weight of each criterion and sub-criterion for supplier selection. FMEA was used to determine the risk priority number of each failure mode to determine the risk priority for an IC assembly company. The result indicated that a corporation could categorize its suppliers more effectively and select a low-risk supply chain partner.

While several studies have been conducted for supplier selection with different approaches that combine decision support methods, limited research has been carried out for supplier risk assessment that combines the MCDM with the FMEA method. Our research proposes a combinatorial approach for risk assessment in supplier selection using the FMEA and the hybrid AHP–PROMOTHEE algorithm. This methodology aims to enhance the precision of the FMEA method, thereby eliminating limitations of the traditional FMEA for choosing optimal criteria and suppliers.

Modern products often incorporate critical components or sophisticated materials that require specialized technical skills and associated core competencies. Original equipment manufacturers (OEMs) typically resort to vertical integration by outsourcing component assemblies to Tier 2 and Tier 3 suppliers. Thus, suppliers play an important role at every stage of the product lifecycle, ranging from sourcing raw materials and ramping up production to order fulfillment. In the contemporary world, the supply chain economy has become more vulnerable to wars, diseases, and natural disasters. Recent events, such as the COVID–19 pandemic, have caught companies off-guard and resulted in a constant state of disruption, wherein companies are looking for reliable supplier alternatives [49]. Similarly, the Ukraine war [50] and the US–China trade war [51] have forced companies to reevaluate their existing suppliers and add more suppliers to their existing pool. In addition, the industry 4.0 revolution has shifted corporate focus on aligning with digitally vetted suppli ers beyond the conventional supplier base [52]. The above–stated supply chain dynamics have resulted in a renewed interest in evaluating suppliers on a relatively frequent interval as compared to the traditional supplier evaluation outlook, which occurred over years. Moreover, the presence of IoT sensors in the supply chains and associated data collection tools can automate information gathering and analysis of new and existing suppliers [53]. Our proposed supplier evaluation strategy can address the above-said issues for both new and existing suppliers.

## 3. Methodology

Though attempts have been made to eliminate the shortcomings of the traditional FMEA process, further enhancements need to be investigated. In this research, a proposed hybrid AHP-PROMOTHEE-based FMEA [54] method is validated on a case study for automotive products [39]. Three criteria were considered, which include: cost, quality, and deliverability based on an IoT sensor network, and nine sub–criteria were employed for supplier selection problems. These criteria were selected based on an exhaustive survey of automotive OEMs and multi-tiered suppliers from the European, American, and Asian auto manufacturers [55].

The authors used the new failure mode and effects analysis (NFMEA) method, which integrates the fuzzy analytic hierarchy process and FMEA approach. In order to illustrate our methodology, three criteria and nine sub-criteria were selected. Three potential suppliers (A, B, and C) were considered with varying levels of attributes. The proposed combinatorial model integrates FMEA with the AHP–PROMOTHEE approach and consists of four stages for prioritization of the risks identified in the supplier selection process. Figure 1 below shows the four-stage framework for risk assessment and the selection of suppliers.

![](images/181cc08ee18eadc07950645a31f4349287bafa6bcf4cd8e78999a9c937b633cf.jpg)  
Figure 1. Framework for the combinatorial FMEA and hybrid AHP-PROMETHEE methodol-Figure 1. Framework for the combinatorial FMEA and hybrid AHP-PROMETHEE methodology.

## 3.1. STAGE (I) Selection of Criteria and Sub-Criteria

. STAGE (I) Selection of Criteria and Sub-Criteria In this step, the supplier selection team identifies a set of criteria and sub-criteria to evaluate potential suppliers. Each industry sector, as well as corporation, will have a unique set of criteria based on its supply chain sensor network. Based on the tier level in the supply chain, it may be important to include upstream-tier corporations to determine the selection criteria. The criteria and sub-criteria for supplier selection in our research are shown in Table 1. In this paper, we evaluate three suppliers referred to as Supplier A,

Supplier B, and Supplier C, respectively, and the supplier deliverability criteria are based on the IoT–enabled system.

Table 1. Criteria and sub-criteria for supplier selection.

<table><tr><td>Criterion</td><td>Sub-Criterion</td></tr><tr><td>Cost</td><td>1. Product cost2. Inbound transportation cost3. Charge of support service</td></tr><tr><td>Quality</td><td>1. Input quality control2. Reliability3. Durability</td></tr><tr><td>Deliverability</td><td>1. Traceability2. On-time delivery3. Delivery lead time</td></tr></table>

## 3.2. Development of FMEA Documents

In this paper, the FMEA document is constructed for each supplier to record the corresponding risk priority number (RPN). The supplier selection team identifies the probable failure modes based on the selection criteria. A failure mode is referred to the deviation of the criterion from the expected level. By focusing on the selection criteria and sub-criteria, the failure modes are further classified through what–if questions. This step defines how the criteria performance deviates to record all failures.

## 3.3. STAGE (II): Determine the Risk Factors with Respect to Failure Modes

Once all possible failure modes are recorded, the supply chain selection team gave their feedback based on the scale rating of failures. The scale rating consists of a severity (S) rating, which is assigned to evaluate the impact of failure mode, an occurrence (O) rating, which is assigned to reflect the frequency of failures, and a detection (D) rating, which is assigned to reflect the difficulty of detecting the cause of a failure mode. Scale ratings of failures for all factors are given below in Tables 2–4.

Table 2. Severity (S) scales of criteria.

<table><tr><td>Severity</td><td>Rating</td><td>Description</td></tr><tr><td>Extreme</td><td>5</td><td>Cost: supplier offers very expensive raw materialQuality: supplier offers high level of defective materialDeliverability: supplier always misses on-time delivery</td></tr><tr><td>high</td><td>4</td><td>Cost: supplier offers high-priced raw materialQuality: supplier offers many defective materialsDeliverability: supplier misses on-time delivery most of the time</td></tr><tr><td>Moderate</td><td>3</td><td>Cost: supplier offers slightly high-priced raw materialQuality: supplier offers some defective materialDeliverability: supplier misses some on-time delivery</td></tr><tr><td>Low</td><td>2</td><td>Cost: supplier offers medium-priced raw materialQuality: supplier offers small amount of defective materialDeliverability: supplier rarely misses on-time delivery</td></tr><tr><td>Minor</td><td>1</td><td>Cost: supplier offers cheap raw materialQuality: supplier offers very few defective materialDeliverability: supplier very rarely misses on-time delivery</td></tr></table>

Table 3. Occurrence (O) Scales of Criteria.

<table><tr><td>Occurrence</td><td>Rating</td><td>Description</td></tr><tr><td>Extreme</td><td>5</td><td>Cost: supplier always offers very expensive raw materialQuality: supplier always offers high level of defective materialDeliverability: supplier always misses on-time delivery</td></tr><tr><td>high</td><td>4</td><td>Cost: supplier usually high-priced the raw materialQuality: supplier often offers many defective materialsDeliverability: supplier misses on-time delivery most of the time</td></tr><tr><td>Moderate</td><td>3</td><td>Cost: supplier often offers slightly high-priced raw materialQuality: supplier offers some defective amount of materialDeliverability: supplier misses some of the on-time delivery</td></tr><tr><td>Low</td><td>2</td><td>Cost: supplier rarely offers expensive raw materialQuality: supplier rarely offers defective materialDeliverability: supplier rarely misses the on-time delivery</td></tr><tr><td>Minor</td><td>1</td><td>Cost: supplier very rarely offers expensive raw materialQuality: supplier very rarely offers defective materialDeliverability: supplier very rarely misses on-time delivery</td></tr></table>

Table 4. Detection (D) scales of criteria.

<table><tr><td>Detection</td><td>Rating</td><td>Description</td><td>Probability of Detection (%) for All Criteria</td></tr><tr><td>Remote</td><td>5</td><td>No/limited collaboration and information exchange</td><td>0–5</td></tr><tr><td>Low</td><td>4</td><td>Low collaboration and information exchange</td><td>6–25</td></tr><tr><td>Moderate</td><td>3</td><td>Moderate collaboration and information exchange</td><td>26–50</td></tr><tr><td>High</td><td>2</td><td>High collaboration and information exchange</td><td>51–75</td></tr><tr><td>Very high</td><td>1</td><td>Very high collaboration and information exchange</td><td>76–100</td></tr></table>

Table 4 below shows the detection scale based on the degree of collaboration and information exchange within the supply chain departments. The implementation of IoT sensors can aid in identifying failures remotely. More collaboration and information exchange increases the probability of detection [56]

## Calculation of Risk Priority Number (RPN) Values

The RPNs for failure modes are calculated from expert feedback using the equation $\mathrm { R P N } = \mathsf { S } \times \mathsf { O } \times \mathsf { D }$ . Based on the RPN values, the failure modes are prioritized as per the traditional FMEA method. The highest RPN value corresponds to a higher priority and lowers RPN value corresponds to a lower priority. Table 5 below shows the calculated RPN values for all suppliers.

It is important to note that, in the traditional FMEA, the RPN value of each failure mode is considered to establish priority for decision-making. According to Table 5, it is clear that the RPN value of 6 occurs for several criteria (failure modes) for each supplier. Thus, it is difficult and ambiguous for the decision-maker to determine the priority of failure modes. This is one of the major limitations of the conventional FMEA method. To overcome this limitation, we propose the hybrid AHP-PROMETHEE methodology that augments the traditional FMEA approach. In this new approach, the AHP algorithm is used to determine the global weights for each criterion, and PROMETHEE is used to rank the RPN based on the global weights.

Table 5. Calculation of RPN for Supplier A, B, and C.

<table><tr><td colspan="2"></td><td colspan="4">Supplier A</td><td colspan="4">Supplier B</td><td colspan="4">Supplier C</td></tr><tr><td>Criterion</td><td>Sub-criterion</td><td>S</td><td>O</td><td>D</td><td>RPN</td><td>S</td><td>O</td><td>D</td><td>RPN</td><td>S</td><td>O</td><td>D</td><td>RPN</td></tr><tr><td rowspan="3">Cost</td><td>Product cost</td><td>2</td><td>2</td><td>1</td><td>4</td><td>3</td><td>2</td><td>1</td><td>6</td><td>3</td><td>2</td><td>1</td><td>6</td></tr><tr><td>Inbound transportation cost</td><td>3</td><td>2</td><td>1</td><td>6</td><td>2</td><td>3</td><td>1</td><td>6</td><td>2</td><td>3</td><td>1</td><td>6</td></tr><tr><td>Charge of support service</td><td>3</td><td>2</td><td>1</td><td>6</td><td>2</td><td>2</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>4</td></tr><tr><td rowspan="3">Quality</td><td>Input quality control</td><td>2</td><td>3</td><td>1</td><td>6</td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>1</td><td>4</td></tr><tr><td>Reliability</td><td>3</td><td>2</td><td>1</td><td>6</td><td>2</td><td>3</td><td>1</td><td>6</td><td>3</td><td>3</td><td>1</td><td>9</td></tr><tr><td>Durability</td><td>2</td><td>4</td><td>1</td><td>8</td><td>3</td><td>1</td><td>1</td><td>3</td><td>4</td><td>3</td><td>1</td><td>12</td></tr><tr><td rowspan="3">Deliverability</td><td>Traceability</td><td>4</td><td>2</td><td>1</td><td>8</td><td>3</td><td>2</td><td>1</td><td>6</td><td>3</td><td>2</td><td>1</td><td>6</td></tr><tr><td>On time delivery</td><td>2</td><td>3</td><td>1</td><td>6</td><td>1</td><td>3</td><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td></tr><tr><td>Delivery lead time</td><td>3</td><td>2</td><td>1</td><td>6</td><td>2</td><td>2</td><td>1</td><td>4</td><td>3</td><td>3</td><td>1</td><td>9</td></tr><tr><td></td><td>Total</td><td></td><td></td><td></td><td>56</td><td></td><td></td><td></td><td>40</td><td></td><td></td><td></td><td>58</td></tr><tr><td></td><td>Average</td><td></td><td></td><td></td><td>9.3</td><td></td><td></td><td></td><td>6.7</td><td></td><td></td><td></td><td>9.7</td></tr></table>

## 3.4. STAGE (III): Use AHP to Calculate the Weights for Each Criterion

The analytic hierarchy process (AHP) has found a widespread application in decisionmaking problems, which involves criteria at multi-tier levels [57–59]. AHP was developed by Saaty in 1980 to assist decision-makers to reach a consensus decision when conflicting objectives exist [60]. The AHP has the ability to organize the basic rationality by break ing down a problem into smaller parts at different hierarchy levels. Further, a simple pairwise comparison of judgments is conducted to develop priorities in each hierarchy level. In the following section, we describe the AHP hierarchy and calculate the pairwise comparison matrix.

## 3.4.1. Building the AHP Model and Computing the Weights

The AHP model for supplier selection consists of four levels: the goal, the criteria, the sub-criteria, and alternatives. (Figure 2). The first level includes the goal, which is selecting the best supplier. The second level (criteria) contains cost, quality, and deliverability. The third level of the hierarchy consists of nine sub–criteria: product cost, inbound transportation cost, the charge of support service, input quality control, reliability, durabil ity, traceability, on–time delivery, and delivery lead time. The last level of the hierarchy consists of alternatives, which are the different suppliers to be evaluated.

To evaluate the AHP model, the priority weight of each criterion at each level should be calculated. The following steps are implemented to calculate the weight of each criterion: perform a pair–wise comparison matrix. The pair-wise comparison matrix $( \mathrm { X _ { i j } } )$ is based on the expert’s estimation of the relative importance between each criterion. The supply chain team assigns preferences for pairwise comparisons based on the Saaty preference scale values shown in Table 6.

The preferences of each decision maker are averaged if there is more than one supplier. The pair-wise comparison matrix of the main criteria and sub-criteria based on estimations of the supply chain team is represented in Table 7.

![](images/9d5ff97c4fab849cbabe89d6f13f31b016c3efd8e3c0eb2a4e9a1e1db178df86.jpg)  
Figure 2. Decision hierarchy for supplier selection.

Table 6. Saaty preference scale values for pairwise comparison.

<table><tr><td>Preference</td><td>Rating Score</td></tr><tr><td>Extremely Preferred</td><td>9</td></tr><tr><td>Very, Very Strong</td><td>8</td></tr><tr><td>Very Strongly Preferred</td><td>7</td></tr><tr><td>Strong Plus</td><td>6</td></tr><tr><td>Strongly Preferred</td><td>5</td></tr><tr><td>Moderate Plus</td><td>4</td></tr><tr><td>Moderately Preferred</td><td>3</td></tr><tr><td>Weak or Slight</td><td>2</td></tr><tr><td>Equally Preferred</td><td>1</td></tr></table>

Table 7. Pair-wise comparison matrix of the main criteria and sub-criteria.

<table><tr><td colspan="4">Pair-wise comparison matrix of the main criteria</td></tr><tr><td>Criterion</td><td>Cost</td><td>Quality</td><td>Deliverability</td></tr><tr><td>Cost</td><td>1</td><td>2</td><td>7</td></tr><tr><td>Quality</td><td>1/2</td><td>1</td><td>9</td></tr><tr><td>Deliverability</td><td>1/7</td><td>1/9</td><td>1</td></tr><tr><td colspan="4">Pair-wise comparison matrix of the sub-criteria with respect to cost</td></tr><tr><td>Sub-criterion</td><td>Product cost</td><td>Inbound transportation cost</td><td>Charge for support service</td></tr><tr><td>Product cost</td><td>1</td><td>5</td><td>7</td></tr><tr><td>Inbound transportation cost</td><td>1/5</td><td>1</td><td>3</td></tr><tr><td>Charge of support service</td><td>1/7</td><td>1/3</td><td>1</td></tr></table>

Table 7. Cont.

<table><tr><td colspan="4">Pair-wise comparison matrix of the sub-criteria with respect to quality</td></tr><tr><td>Sub-criterion</td><td>Input quality control</td><td>Reliability</td><td>Durability</td></tr><tr><td>Input quality control</td><td>1</td><td>1/7</td><td>1/7</td></tr><tr><td>Reliability</td><td>7</td><td>1</td><td>2</td></tr><tr><td>Durability</td><td>7</td><td>1/2</td><td>1</td></tr><tr><td colspan="4">Pair-wise comparison matrix of the sub-criteria with respect to deliverability</td></tr><tr><td>Sub-criterion</td><td>Traceability</td><td>On time delivery</td><td>Delivery lead time</td></tr><tr><td>Traceability</td><td>1</td><td>1/5</td><td>1</td></tr><tr><td>On time delivery</td><td>5</td><td>1</td><td>7</td></tr><tr><td>Delivery lead time</td><td>1</td><td>1/7</td><td>1</td></tr></table>

In Table 7 above, each criterion is compared against the other, with the diagonals representing self-comparison of the criteria. For example, the cost criterion in the main criteria matrix is slightly preferred (2) to quality and very strongly preferred (7) to deliverability. Similarly, the criterion of quality is extremely preferred (9) to deliverability. The decision maker (supply chain team) needs to populate the upper half of the matrix, and the lower half is the reciprocal of the upper half. The pair-wise comparison matrices of the sub-criteria with respect to cost, quality, and deliverability are calculated similarly to the main criteria matrix.

A vector of priorities or weighing of criteria and sub-criteria in the matrix are calculated by Equation (1) shown below, where, $\mathrm { X _ { i j } }$ refers to the importance of criterion i with respect to criterion j, and n refers to the number of criteria.

$$
\text { Wi } = \frac {\left(\sqcap_ {j = 1} ^ {n} X _ {i j}\right) ^ {1 / n}}{\sum_ {i = 1} ^ {n} \left(\sqcap_ {j = 1} ^ {n} X _ {i j}\right) ^ {1 / n}} \forall \mathrm{i} = 1, 2, \dots , \mathrm{n}\tag{1}
$$

## 3.4.2. Consistency Check for Each Matrix

The consistency check is one of the important features of the AHP method. Consistency check tests the consistency ratio (CR) in each pairwise matrix. CR aims to eliminate any inconsistencies that may occur when assigning the criteria weights due to errors in judgment of the decision makers. A C.R. ≤ 0.10 is considered acceptable, and a perfect consistent ratio is zero. However, if C.R.>0.1, serious inconsistencies may exist, and the pairwise matrix needs to be updated to meet the minimum threshold for further analysis. CRs were obtained for the criteria pairwise matrix and for each sub-criterion by using Equations (2)–(5), shown below, respectively. A consistent matrix $\left( \lambda _ { \operatorname* { m a x } } \right)$ is the largest eigenvalue of a reciprocal matrix of order n. $\lambda _ { \mathrm { m a x } }$ is calculated by Equations (2) and (3).

$$
\mathrm {V_ {i}} = \frac {\sum_ {j = 1} ^ {n} W _ {j} X _ {i j}}{W _ {i}} \quad \forall_ {\mathrm{i}} = 1, 2, \ldots , \mathrm{n}\tag{2}
$$

$$
\lambda \max = \frac {\sum_ {i = 1} ^ {n} V _ {i}}{n}\tag{3}
$$

Consistency index (CI) is calculated by Equation (4).

$$
C. I. = \frac {\lambda_ {\max} - n}{n - 1}\tag{4}
$$

$$
\mathrm{CR} = \mathrm{CI} / \mathrm{RI}\tag{5}
$$

RI stands for random index. RI is based on the number of criteria $( \boldsymbol { \mathrm { n _ { p } } } )$ in each pairwise comparison, as shown in Table 8. In this paper, $\mathrm { n } _ { \mathrm { p } } { = } 3$ for all levels of hierarchy.

Table 8. Random index for number of criteria $( \boldsymbol { \mathrm { n _ { p } } } )$ in pairwise comparison [60].

<table><tr><td> $n_p$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>RI</td><td>0</td><td>0</td><td>0.52</td><td>0.89</td><td>1.11</td><td>1.25</td><td>1.35</td><td>1.4</td><td>1.45</td></tr></table>

## 3.4.3. Calculation of Global Weight

The global weights are calculated by multiplying the weights of the main criteria with the weights of its sub-criteria. The global weight will be used at the end of the prioritization process to obtain the aggregate preference function.

## 3.5. STAGE (IV): Using PROMETHEE Method

The preference ranking organization method for enrichment evaluation (PROMETHEE) method is one of the MCDM methods developed by Brans [61]. PROMETHEE is an outranking method for alternatives while considering several criteria, which may be conflicting [54]. The PROMETHEE family of outranking methods include the PROMETHEE I for partial ranking of the alternatives, as well as the PROMETHEE II for the complete ranking of the alternatives. In this research, we implement the PROMETHEE II method, which is intended to provide a complete ranking of a finite set of feasible alternatives from the best to the worst.

A stepwise procedure for implementing PROMETHEE is presented in Figure 3 below. The first step involves constructing a normalized matrix by taking into consideration the beneficial and non–beneficial criteria. In step 2, the relevant preference function is applied to each criterion. Further, the aggregated preference index is calculated considering the global weights (Step 3). In step 4, the positive and negative outranking flows for each $\bar { ( \mathbf { i } ^ { \mathrm { t h } } ) }$ alternative are calculated. The procedure is completed with the calculation of net outranking flow for each alternative. The ranking of the alternatives depends on the values of ф (i). The alternative with the highest value of ф (i) is the most preferred and vice versa.

![](images/7b6b4b1bfdf42ab537ec94e597d95947d7b27831204707d417b6546bec672ae4.jpg)  
Figure 3. Stepwise procedure for PROMETHEE [62,6Figure 3. Stepwise procedure for PROMETHEE [62,63].

## 4. Results

Our proposed combinatorial risk assessment method using FMEA and hybrid AHP-PROMOTHEE is applied to a case study, as discussed in the methodology section. Using the pairwise comparison matrices, priority weights are calculated for both the main criteria and sub-criteria using Equation (1). Table 9 shows the computation of priority weights for the main criteria and sub-criteria. The supply chain team gives more priority weight to cost (55.5%), followed by quality (38.5%) and deliverability (6%).

Table 9. Calculation of priority weights for the main criteria and sub-criteria.

<table><tr><td colspan="9">Priority weights for the main criteria</td></tr><tr><td>Criterion</td><td>Cost</td><td>Quality</td><td>Deliverability</td><td>Cost weight</td><td>Quality weight</td><td>Deliverability weight</td><td>Total weight</td><td>Priority weight</td></tr><tr><td>Cost</td><td>1</td><td>2</td><td>7</td><td>0.609</td><td>0.643</td><td>0.412</td><td>1.663</td><td>0.555</td></tr><tr><td>Quality</td><td>0.500</td><td>1</td><td>9</td><td>0.304</td><td>0.321</td><td>0.529</td><td>1.155</td><td>0.385</td></tr><tr><td>Deliverability</td><td>0.143</td><td>0.111</td><td>1</td><td>0.087</td><td>0.036</td><td>0.059</td><td>0.181</td><td>0.060</td></tr><tr><td>Total</td><td>1.643</td><td>3.111</td><td>17</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td colspan="9">Priority weights with respect to cost</td></tr><tr><td>Criterion</td><td>Product cost</td><td>Inbound transportation cost</td><td>Charge of support service</td><td>Product cost weight</td><td>Inbound transportation cost weight</td><td>Charge of support service weight</td><td>Total weight</td><td>Priority weight</td></tr><tr><td>Product cost</td><td>1</td><td>5</td><td>7</td><td>0.745</td><td>0.789</td><td>0.636</td><td>2.171</td><td>0.724</td></tr><tr><td>Inbound transportation cost</td><td>0.2</td><td>1</td><td>3</td><td>0.149</td><td>0.158</td><td>0.273</td><td>0.580</td><td>0.193</td></tr><tr><td>Charge of support</td><td>0.143</td><td>0.333</td><td>1</td><td>0.106</td><td>0.053</td><td>0.091</td><td>0.250</td><td>0.083</td></tr><tr><td>Total</td><td>1.343</td><td>6.333</td><td>11</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td colspan="9">Priority weights with respect to quality</td></tr><tr><td>Criterion</td><td>Input quality control</td><td>Reliability</td><td>Durability</td><td>Input quality control weight</td><td>Reliability weight</td><td>Durability weight</td><td>Total weight</td><td>Priority weight</td></tr><tr><td>Input quality control</td><td>1</td><td>0.143</td><td>0.143</td><td>0.067</td><td>0.087</td><td>0.045</td><td>0.199</td><td>0.066</td></tr><tr><td>Reliability</td><td>7</td><td>1</td><td>2</td><td>0.467</td><td>0.609</td><td>0.636</td><td>1.712</td><td>0.571</td></tr><tr><td>Durability</td><td>7</td><td>0.5</td><td>1</td><td>0.467</td><td>0.304</td><td>0.318</td><td>1.089</td><td>0.363</td></tr><tr><td>Total</td><td>15</td><td>1.643</td><td>3.143</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td colspan="9">Priority weights with respect to deliverability</td></tr><tr><td>Criterion</td><td>Traceability</td><td>On time delivery</td><td>Delivery lead time</td><td>Traceability weight</td><td>On time delivery weight</td><td>Delivery lead time weight</td><td>Total weight</td><td>Priority weight</td></tr><tr><td>Traceability</td><td>1</td><td>0.200</td><td>1</td><td>0.143</td><td>0.149</td><td>0.111</td><td>0.403</td><td>0.134</td></tr><tr><td>On time delivery</td><td>5</td><td>1</td><td>7</td><td>0.714</td><td>0.745</td><td>0.778</td><td>2.237</td><td>0.746</td></tr><tr><td>Delivery lead time</td><td>1</td><td>0.143</td><td>1</td><td>0.143</td><td>0.106</td><td>0.111</td><td>0.360</td><td>0.120</td></tr><tr><td>Total</td><td>7</td><td>1.343</td><td>9</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td></tr></table>

The consistency ratios (C.R.) for all pairwise comparisons among the criteria and sub-criteria above are calculated using Equations (2)–(5). The results of C.R. indicated that all pairwise matrices are valid with a consistency ratio < 0.1, as shown in Table 10.

Table 10. Summary of C.R results.

<table><tr><td>Pairwise Comparison</td><td>λmax</td><td>C.I</td><td>R.I for 3</td><td>C.R &lt; 0.1</td></tr><tr><td>Main criteria</td><td>3.10</td><td>0.05</td><td>0.52</td><td>0.097</td></tr><tr><td>Sub-criteria with respect to cost</td><td>3.07</td><td>0.03</td><td>0.52</td><td>0.06</td></tr><tr><td>Sub-criteria with respect to quality</td><td>3.05</td><td>0.03</td><td>0.52</td><td>0.05</td></tr><tr><td>Sub-criteria with respect to deliverability</td><td>3.01</td><td>0.01</td><td>0.52</td><td>0.1</td></tr></table>

Before using the PROMETHEE method to rank the supply chain risks, PROMETHEE assumes that the decision-maker is able to weigh the criteria appropriately. Therefore, the global weights are calculated by multiplying the weight of the main criteria with its respective sub-criteria weights. Table 11 shows the global weights. In this case study, the product cost has the highest weight (39.8%) followed by reliability (22.3%), durability (14.2%), and inbound transportation cost (10.6%), respectively.

Table 11. Global weight of sub-criteria.

<table><tr><td>Main Criterion</td><td>Weight of the Main Criterion (1)</td><td>Sub-Criterion</td><td>Weight of Sub-Criterion (2)</td><td>Global Weight (3) = (1) × (2)</td></tr><tr><td rowspan="3">Cost</td><td rowspan="3">0.55</td><td>Product cost</td><td>0.724</td><td>0.398</td></tr><tr><td>Inbound transportation cost</td><td>0.193</td><td>0.106</td></tr><tr><td>Charge of support service</td><td>0.083</td><td>0.046</td></tr><tr><td rowspan="3">Quality</td><td rowspan="3">0.39</td><td>Input quality control</td><td>0.066</td><td>0.026</td></tr><tr><td>Reliability</td><td>0.571</td><td>0.223</td></tr><tr><td>Durability</td><td>0.363</td><td>0142</td></tr><tr><td rowspan="3">Deliverability</td><td rowspan="3">0.06</td><td>Traceability</td><td>0.134</td><td>0.008</td></tr><tr><td>On-time delivery</td><td>0.746</td><td>0.045</td></tr><tr><td>Delivery lead time</td><td>0.120</td><td>0.007</td></tr><tr><td></td><td></td><td></td><td>Total Weight</td><td>1.000</td></tr></table>

Assigning priority to each failure mode is a non-trivial problem, which can be addressed by the preference ranking organization method for enrichment evaluation (PROMETHEE) method. The decision matrix for all suppliers $( \mathrm { A } , \mathrm { B } , \mathrm { C } )$ is shown in Table 12. This matrix was populated from the RPN values in Table 5.

Table 12. Decision matrix for suppliers in the PROMETHEE.

<table><tr><td>Supplier</td><td>Product Cost</td><td>Inbound Transportation Cost</td><td>Charge of Support Service</td><td>Input Quality Control</td><td>Reliability</td><td>Durability</td><td>Traceability</td><td>On Time Delivery</td><td>Delivery Lead Time</td></tr><tr><td>A</td><td>4</td><td>6</td><td>6</td><td>6</td><td>6</td><td>8</td><td>8</td><td>6</td><td>6</td></tr><tr><td>B</td><td>6</td><td>6</td><td>4</td><td>2</td><td>6</td><td>3</td><td>6</td><td>3</td><td>4</td></tr><tr><td>C</td><td>6</td><td>6</td><td>4</td><td>4</td><td>9</td><td>12</td><td>6</td><td>2</td><td>9</td></tr></table>

The decision matrix is normalized by using the appropriate normalization formula in step 1 from Figure 3. Table 13 shows the normalized decision matrix using the nonbeneficial criteria, wherein the lower value of the performance measure is desirable. In our case, the objective is to select a supplier with the lowest supply chain risk, thus the non-beneficial criteria are considered for normalization.

Table 13. Normalized decision matrix for supplier selection.

<table><tr><td>RPN of Supplier</td><td>Product Cost</td><td>Inbound Transportation Cost</td><td>Charge of Support Service</td><td>Input Quality Rate</td><td>Reliability</td><td>Durability</td><td>Traceability</td><td>On Time Delivery</td><td>Delivery Lead Time</td></tr><tr><td>A</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.556</td><td>0</td><td>1</td><td>0.6</td></tr><tr><td>B</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.25</td><td>1</td></tr><tr><td>C</td><td>0</td><td>0</td><td>1</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr></table>

A paired comparison (Step 2, Figure 3) was conducted for all the supplier pairs using the normalized decision matrix, and the preference function was calculated using the Vijay and Shankar formulas, as shown in Table 14 below.

Table 14. Preference functions for all supplier pairs.

<table><tr><td>RPN of Supplier</td><td>Product Cost</td><td>Inbound Transportation Cost</td><td>Charge of Support Service</td><td>Input Quality Rate</td><td>Reliability</td><td>Durability</td><td>Traceability</td><td>On Time Delivery</td><td>Delivery Lead Time</td></tr><tr><td>(A,B)</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.555556</td><td>0</td><td>0.75</td><td>0</td></tr><tr><td>(A,C)</td><td>1</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.6</td></tr><tr><td>(B,A)</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.4</td></tr><tr><td>(B,C)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.25</td><td>1</td></tr><tr><td>(C,A)</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0.444444</td><td>1</td><td>0</td><td>0</td></tr><tr><td>(C,B)</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

The aggregated preference function for suppliers was calculated by using the appropriate formula (Step 3, Figure 3). Table 15 shows the aggregated preference matrix, which takes into account the global weights (Table 11).

Table 15. Aggregated preference function for suppliers.

<table><tr><td>RPN of Supplier</td><td>A</td><td>B</td><td>C</td></tr><tr><td>A</td><td>Nil</td><td>0.536024</td><td>0.459927</td></tr><tr><td>B</td><td>0.05676</td><td>Nil</td><td>0.018391</td></tr><tr><td>C</td><td>0.339333</td><td>0.37706</td><td>Nil</td></tr></table>

In the final stage, the entering and leaving flow values were calculated using the appropriate formula (Step 4, Figure 3). Further, the net outranking flow for each alternative was computed (Step 5, Figure 3). The outranking flows for each supplier are based on attaining the lowest supply chain risk. In PROMOTHEE, the higher value of the net outranking corresponds to a preferred alternative. Thus, the best supplier is the one having the highest net outranking value. Table 16 shows the entering flow, leaving flow, and net outranking flow values.

Table 16. Outranking flows in PROMOTHEE for suppliers.

<table><tr><td>Supplier</td><td>Leaving Flow</td><td>Entering Flow</td><td>Net Outranking</td></tr><tr><td>A</td><td>0.543</td><td>0.153</td><td>0.389</td></tr><tr><td>B</td><td>0.289</td><td>0.205</td><td>0.085</td></tr><tr><td>C</td><td>0.0614</td><td>0.536</td><td>-0.475</td></tr></table>

## 5. Discussion

## 5.1. Contrasting Supplier Selection Methodologies

A comparative analysis was performed to evaluate the supplier selection methodologies. Table 5 shows the risk priority numbers for each sub-criterion for all suppliers calculated using the traditional FMEA model as [31]. As can be seen in Table 5, supplier B has the lowest total (40) and average (6.7) for the RPN among all suppliers. Thus, based on the traditional FMEA model, supplier B is the preferred choice of supplier for the corporation due to its lowest risk potential. In this case study, the failure modes with RPN equal or greater than 6 need improvement. For supplier B, the sub-criteria input quality control, durability, and on-time delivery have a lower RPN as compared to other suppliers. However, the traditional FMEA method has ambiguity when deciding which sub-criteria to improve upon based on a threshold RPN (6), as multiple sub-criteria can have the same RPN. This exacerbates the decision-making of the supply chain team to determine the priorities among sub-criteria for further improvement. This is one of the critical limitations of traditional FMEA, which is addressed in our new approach.

Our combinatorial methodology of FMEA and hybrid AHP-PROMETHEE is a vital tool in solving the supplier selection problem. The proposed methodology allows decisionmakers to rank the supplier alternatives effectively and provide valuable guidance in framing supplier selection strategies. An important aspect of the new methodology is the inclusion of weights for supplier selection criteria based on the company policy and preference. Table 17 below depicts a comparative analysis between the traditional FMEA and the proposed methodology for supplier rankings. In the proposed methodology, supplier A is the most preferred supplier with the highest net outranking value of 0.389 (lowest risk). This outcome is in alignment with the company’s product cost reduction strategy (global weighted preference for product cost \~40%). Supplier B was the preferred choice according to the traditional FMEA model. However, supplier B is weak with respect to the product cost (RPN = 6), which contradicts the corporate cost reduction strategy. The second highest global weight was assigned to reliability (22.3%). Taking this weight into consideration, both suppliers A and B had equal RPN = 6. However, the cumulative contribution of these two highest criteria exceed 60% of the global weights, which drive the strategic decision making of the enterprise. Accordingly, supplier A is in alignment with the company’s priorities, which are further evaluated using the PROMETHEE algorithm.

Table 17. Benchmarking of comparative supplier rankings methodologies.

<table><tr><td colspan="3">Traditional FMEA</td><td colspan="2">ISO 9000/TS16949 Method</td><td colspan="2">Proposed Method</td></tr><tr><td>Supplier</td><td>Traditional total RPN</td><td>Rank</td><td>Performance Score</td><td>Rank</td><td>Net Outranking</td><td>Rank</td></tr><tr><td>A</td><td>56</td><td>2</td><td>0.61</td><td>2</td><td>0.389</td><td>1</td></tr><tr><td>B</td><td>40</td><td>1</td><td>0.65</td><td>1</td><td>0.085</td><td>2</td></tr><tr><td>C</td><td>58</td><td>3</td><td>0.53</td><td>3</td><td>-0.475</td><td>3</td></tr></table>

We also compared our results with a recent automotive supplier selection methodology, as per the ISO 9000/TS16949 standards [64]. Herein, each supplier was allocated a weighted sum of the three main criteria, and the supplier with the highest performance score was selected and ranked over the others. As can be seen from Table 17, the highest performance score was attributed to supplier B, followed by supplier A and supplier C. Supplier C was rated the lowest and consistent across all methods. It is evident that inconsistencies for supplier B have been rectified in our proposed method. Thus, the incorporation of the hybrid AHP-PROMETHEE enables the corporation to prioritize failure modes based on the global weight of all criteria and rank each supplier based on lowest supply chain disruption.

## 5.2. Implications for Supply Chain Risk Management

The application of the proposed methodology to real-world scenarios could include a large number of criteria and sub-criteria. This would involve evaluating several data sets obtained through IoT sensors and pairwise comparisons constituting big data analytics. The proposed method can be coded into a sub-routine source code, which can conveniently be adopted and implemented by any industry. Each of the sub-systems (FMEA, AHP, and PROMETHEE) has been coded into commercial software packages. However, the integration and customization of these methods, as demonstrated in this paper, would be a valuable asset to supply chain risk management. Moreover, our approach provides flexibility to include user-chosen supplier selection criteria that can be tailored to different industry sectors that are now enabled with multi–tiered IoT sensors.

## 5.3. IoT Sensors in Supply Chain Risk Management

IoT sensors enable a digitally connected seamless supply chain environment with multiple sensors on edge-networks that acquire, process, and transmit data pertaining to various aspects of SCM [65]. In our case study, these IoT sensors provide useful data metrics to evaluate each supplier criteria based on the industry type. The sensors mentioned in Table 18 provide parameter ranges encountered by materials, devices, and products within a supply chain. These quantifiable data sets assist in making judicious decisions with regards to cost, quality, and deliverability criteria chosen for our case study. However, these parameters and data acquisition sensors can be varied to suit other applications and industry segments.

Table 18. Impact of IoT sensors on supply chain logistics.

<table><tr><td>IoT Sensor</td><td>Sensor Modality</td><td>Parameter Tracked</td><td>SCM Impact</td></tr><tr><td>Thermal Sensors</td><td>Thermistor, Infrared, In situ thermocouple</td><td>Temperature range and exposure limits</td><td>Quality of perishable or temperature sensitive shipment</td></tr><tr><td>Moisture sensors</td><td>Psychrometer, hair tension</td><td>Humidity range and exposure limits</td><td>Quality of hygroscopic materials/products</td></tr><tr><td>Light sensors</td><td>Photoresistor, photodiode</td><td>Exposure to UV, Visible and infrared spectrum</td><td>Light sensitive materials/products</td></tr><tr><td>Acoustic sensors</td><td>Hydrophone, geophone</td><td>Frequency range and exposure limits</td><td>Vibration sensitive devices and products</td></tr><tr><td>Pressure and proximity sensors</td><td>Doppler radar, occupancy detector</td><td>Multidimensional force/torque loading</td><td>Load sensitive fragile materials/products</td></tr><tr><td>Image sensors</td><td>Active pixel sensor, charge-coupled device</td><td>Dimensional accuracy, Particle counter</td><td>Quality of materials/products manufactured and shipped</td></tr><tr><td>Chemical sensors</td><td>Electrochemical nose, Impedance array</td><td>Trace particulate content (ppm/ppb)</td><td>Toxicity and impurities in materials/products</td></tr><tr><td>Gyroscope sensors</td><td>Accelerometers</td><td>Angular velocity gradients</td><td>Stability of devices/products in shipment</td></tr><tr><td>Motion sensors</td><td>Ultrasonic, infrared, radar, LIDAR</td><td>GPS coordinates with time stamps</td><td>Assembly operations and shipment tracking</td></tr></table>

## 6. Conclusions

With globalization, supply chains have been transformed due to the internet of things (IoT)-based sensors across different tiers. Thus, they have become increasingly vulnerable to cyber disruptions, as organizations lose millions of dollars because of cost instability, supply disruption, and non-compliance fines that negatively impact the organizational brand. Supply chain risk management (SCRM) is one of the key components for an effective supply chain. This research develops a combinatorial approach for risk assessment in supplier selection using FMEA with hybrid AHP-PROMETHEE methods. A fourstage framework is developed and applied to a case study with three suppliers and nine sub-criteria. The supplier selection team identified company-specific criteria to evaluate potential suppliers. FMEA rubrics for severity (S), occurrence (O), and detection (D) ratings were developed. Each supplier was evaluated to determine the risk priority number for the sub-criteria based on expert opinion. A multi-tier hierarchy of criteria and sub-criteria were generated based on the company-specific preferences by the supply chain team. The AHP method was applied for pairwise comparisons on a vector of priorities to generate global weights for the sub-criteria. The consistency check for criteria and sub-criteria matrices indicated an acceptable consistency ratio of less than 0.1. The AHP generated weights were implemented in the PROMETHEE algorithm to rank suppliers based on the lowest risk of supply chain disruption. The proposed method was contrasted against the traditional FMEA method and showed significant improvements while considering company-specific criteria for risk management. Moreover, our approach offers a feedback mechanism for suppliers to improve on their core competencies in order to meet these criteria and minimize their risk to the supply chain. This method provides the decision makers (supply chain team) an efficient tool to rank candidate suppliers based on their risk potential. In addition, it entails guidance for framing supplier selection risk mitigation strategies.

Author Contributions: B.A. and S.D. contributed to the conceptualization and thematic content of the manuscript, which was the basis of this review. B.A. conducted the literature review and the initial draft preparation. S.D. contributed to reviewing and editing the draft, the supervision, and the fund acquisition. All authors have read and agreed to the published version of the manuscript.

Funding: The authors express their gratitude for funding support from the National Science Foundation and the Center of Excellence in Product Design and Advanced Manufacturing at North Carolina A&T State University.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study, in the collection, analyses, or interpretation of data, in the writing of the manuscript, or in the decision to publish the results.

## References

1. Handfield, R.B.; Graham, G.; Burns, L. Corona virus, tariffs, trade wars and supply chain evolutionary design. Int. J. Oper. Prod. Manag. 2020, 40, 1649–1660. [CrossRef]

2. Bloom, D.E.; Cadarette, D. Infectious disease threats in the twenty–first century: Strengthening the global response. Front. Immunol. 2019, 10, 549. [CrossRef] [PubMed]

3. Ghadge, A.; Wurtmann, H.; Seuring, S. Managing climate change risks in global supply chains: A review and research agenda. Int. J. Prod. Res. 2020, 58, 44–64. [CrossRef]

4. Vargas–Hernández, J.G. Relocation Strategy of Global Supply Chain and Value Chain under Deglobalization. Manag. Inflat. Supply Chain Disrupt. Glob. Econ. 2023, 1, 62–80.

5. Almakayeel, N.; Desai, S.; Alghamdi, S.; Qureshi, M.R.N.M. Smart Agent System for Cyber Nano–Manufacturing in Industry 4.0. Appl. Sci. 2022, 12, 6143. [CrossRef]

6. Almakaeel, H.; Albalawi, A.; Desai, S. Artificial neural network based framework for cyber nano manufacturing. Manuf. Lett. 2018, 15, 151–154. [CrossRef]

7. Akter, T.; Desai, S. Developing a predictive model for nanoimprint lithography using artificial neural networks. Mater. Des. 2018, 160, 836–848. [CrossRef]

8. Elhoone, H.; Zhang, T.; Anwar, M.; Desai, S. Cyber–Based Design for Additive Manufacturing Using Artificial Neural Networks for Industry 4.0. Int. J. Prod. Res. 2019, 58, 2841–2861. [CrossRef]

9. Ben–Daya, M.; Hassini, E.; Bahroun, Z. Internet of Things and supply chain management: A literature review. Int. J. Prod. Res. 2019, 57, 4719–4742. [CrossRef]

10. Ogunsanya, M.; Isichei, J.; Parupelli, S.K.; Desai, S.; Cai, Y. In–situ Droplet Monitoring of Inkjet 3D Printing Process Using Image Analysis and Machine Learning Models. Procedia Manuf. 2021, 53, 427–434. [CrossRef]

11. Olowe, M.; Parupelli, S.K.; Desai, S. A Review of 3D–Printing of Microneedles. Pharmaceutics 2022, 14, 2693. [CrossRef] [PubMed]

12. McKenzie, J.; Desai, S. Investigating Sintering Mechanisms for Additive Manufacturing of Conductive Traces. Am. J. Eng. Appl. Sci. 2018, 11, 652–662. [CrossRef]

13. Parupelli, S.K.; Desai, S. Hybrid additive manufacturing (3D printing) and characterization of functionally gradient materials via in situ laser curing. Int. J. Adv. Manuf. Technol. 2020, 110, 543–556. [CrossRef]

14. Parupelli, S.K.; Desai, S. A Comprehensive Review of Additive Manufacturing (3D Printing): Processes, Applications and Future Potential. Am. J. Appl. Sci. 2019, 16, 244–272. [CrossRef]

15. Desai, S.; Parupelli, S. Additive Manufacturing (3D Printing). In Maynard’s Industrial and Systems Engineering Handbook, 6th ed.; Springer International Publishing: Berlin/Heidelberg, Germany, 2022; ISBN 1260461564.

16. Parupelli, S.K.; Desai, S. Understanding Hybrid Additive Manufacturing of Functional Devices. Am. J. Eng. Appl. Sci. 2017, 10, 264–271. [CrossRef]

17. Zhong, R.Y.; Newman, S.T.; Huang, G.Q.; Lan, S. Big Data for supply chain management in the service and manufacturing sectors: Challenges, opportunities, and future perspectives. Comput. Ind. Eng. 2016, 101, 572–591. [CrossRef]

18. Queiroz, M.M.; Telles, R.; Bonilla, S.H. Blockchain and supply chain management integration: A systematic review of the literature. Supply Chain Manag. Int. J. 2019, 25, 241–254. [CrossRef]

19. Toyota Suppliers Recognized for Superior Performance. Annual Event. Available online: https://pressroom.toyota.com/toyotasuppliers-2016-awards/ (accessed on 11 April 2023).

20. Levy, D.L. International Sourcing and Supply Chain Stability. J. Int. Bus. Stud. 1995, 26, 343–360. [CrossRef]

21. Cavinato, J.L. Supply chain logistics risks: From the back room to the board room. Int. J. Phys. Distrib. Logist. Manag. 2004, 34, 383–387. [CrossRef]

22. Phase, A.; Mhetre, N. Using IoT in supply chain management. Int. J. Eng. Tech. 2018, 4, 973–979.

23. De Vass, T.; Shee, H.; Miah, S.J. Iot in supply chain management: A narrative on retail sector sustainability. Int. J. Logist. Res. Appl. 2021, 24, 605–624. [CrossRef]

24. Yang, K.; Forte, D.; Tehranipoor, M.M. Protecting endpoint devices in IoT supply chain. In Proceedings of the IEEE/ACM International Conference on Computer–Aided Design, Austin, TX, USA, 2–6 November 2015; pp. 351–356.

25. Hopkins, J.; Hawking, P. Big data analytics and IoT in logistics: A case study. Int. J. Logist. Manag. 2018, 29, 575–591. [CrossRef]

26. Monczka, R.M.; Handfield, R.B.; Giunipero, L.C.; Patterson, J.L. Purchasing and Supply Chain Management; South–Western Cengage Learning: Mason, OH, USA, 2009.

27. Dickson, G.W. An analysis of vendor selection systems and decisions. J. Purch. 1966, 2, 5–17. [CrossRef]

28. Ellram, L.M. The supplier selection decision in strategic partnerships. J. Supply Chain Manag. 1990, 26, 8–14. [CrossRef]

29. Weber, C.A.; Current, J.R.; Benton, W. Vendor selection criteria and methods. Eur. J. Oper. Res. 1991, 50, 2–18. [CrossRef]

30. Boran, F.E.; Genc, S.; Kurt, M.; Akay, D. A multi–criteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method. Expert Syst. Appl. 2009, 36, 11363–11368. [CrossRef]

31. Li, S.; Zeng, W. Risk analysis for the supplier selection problem using failure modes and effects analysis (FMEA). J. Intell. Manuf. 2016, 27, 1309–1321. [CrossRef]

32. Matsumoto, K.; Matsumoto, T.; Goto, Y. Reliability Analysis of Catalytic Converter as an Automotive Emission Control System. SAE Trans. 1975, 84, 728–738.

33. Chang, C.; Liu, P.; Wei, C. Failure mode and effects analysis using grey theory. Integr. Manuf. Syst. 2001, 12, 211–216. [CrossRef]

34. Curkovic, S.; Scannell, T.; Wagner, B. Managing Supply Chain Risk: Integrating with Risk Management; CRC Press: Boca Raton, FL, USA, 2015.

35. Liao, C.N.; Kao, H.P. An integrated fuzzy TOPSIS and MCGP approach to supplier selection in supply chain management. Expert Syst. Appl. 2011, 38, 10803–10811. [CrossRef]

36. Heller, S. Managing industrial risk—Having a tested and proven system to prevent and assess risk. J. Hazard. Mater. 2006, 130, 58–63. [CrossRef] [PubMed

37. Tan, W.C.; Sidhu, M.S. Review of RFID and IoT integration in supply chain management. Oper. Res. Perspect. 2022, 9, 100229. [CrossRef]

38. Ng, W.L. An efficient and simple model for multiple criteria supplier selection problem. Eur. J. Oper. Res. 2008, 186, 1059–1067.

39. Islam, S.; Rahman, M.M.; Sanwar–Ul–Quadir, M. A New Failure Mode and Effects Analysis (NFMEA) Approach for Supplier Selection in Risk Environment. Glob. Sci. Technol. J. 2016, 4, 43–57. [CrossRef]

40. Altubaishe, B.; Clarke, J.; McWilliams, C.; Desai, S. Comparative Analysis of Risk Management Strategies for Additive Manufac turing Supply Chains. Am. J. Appl. Sci. 2019, 16, 273–282. [CrossRef]

41. Dahel, N.E. Vendor selection and order quantity allocation in volume discount environments. Supply Chain Manag. 2003, 8, 335–342. [CrossRef]

42. Shahgholian, K.; Shahraki, A.; Vaezi, Z.; Hajihosseini, H. A model for supplier selection based on fuzzy multicriteria group decision making. Afr. J. Bus. Manag. 2012, 6, 6254–6265.

43. Braglia, M. MAFMA: Multi-attribute failure mode analysis. Int. J. Qual. Reliab. Manag. 2000, 17, 1017–1033. [CrossRef]

44. Braglia, M.; Frosolini, M.; Montanari, R. Fuzzy TOPSIS Approach for Failure Mode, Effects and Criticality Analysis. Qual. Reliab. Eng. Int. 2003, 19, 425–443. [CrossRef]

45. Chin, K.-S.; Wang, Y.-M.; Poon, G.K.; Yang, J.-B. Failure mode and effects analysis using a group-based evidential reasoning approach. Comput. Oper. Res. 2009, 36, 1768–1779. [CrossRef]

46. Chamodrakas, I.; Batis, D.; Martakos, D. Supplier selection in electronic marketplaces using satisficing and fuzzy AHP. Expert Syst. Appl. 2009, 37, 490–498. [CrossRef]

47. Yang, J.; Huang, H.; He, L.; Zhu, S.; Wen, D. Risk evaluation in failure mode and effects analysis of aircraft turbine rotor blades using Dempster–Shafer evidence theory under uncertainty. Eng. Fail. Anal. 2011, 18, 2084–2092. [CrossRef]

48. Chen, P.; Wu, M. A modified failure mode and effects analysis method for supplier selection problems in the supply chain risk environment: A case study. Comput. Ind. Eng. 2013, 66, 634–642. [CrossRef]

49. Shao, Y.; Barnes, D.; Wu, C. Sustainable supplier selection and order allocation for multinational enterprises considering supply disruption in COVID–19 era. Aust. J. Manag. 2022, 48, 031289622110669.

50. Frederico, G.F. Rethinking strategic sourcing during disruptions: A resilience–driven process contribution to knowledge on supply chains. Knowl. Process Manag. 2023, 30, 83–86.

51. Fan, D.; Yeung, A.C.; Tang, C.S.; Lo, C.K.; Zhou, Y. Global operations and supply–chain management under the political economy. J. Oper. Manag. 2022, 68, 816–823. [CrossRef]

52. Fallahpour, A.; Wong, K.Y.; Rajoo, S.; Fathollahi-Fard, A.M.; Antucheviciene, J.; Nayeri, S. An Integrated Approach for a Sustainable Supplier Selection Based on Industry 4.0 Concept. Environ. Sci. Pollut. Res. Int. 2021, 1–19.

53. Abdel-Basset, M.; Manogaran, G.; Mohamed, M. Internet of Things (IoT) and its impact on supply chain: A framework for building smart, secure and efficient systems. Futur. Gener. Comput. Syst. 2018, 86, 614–628.

54. Maheswaran, K.; Loganathan, T. A novel approach for prioritization of failure modes in FMEA using MCDM. Int. J. Eng. Res. Appl. 2013, 3, 733–739.

55. Zainal, N.N.; Rahim, A.; Hassam, S.F.; Ripin, Z.A.M. Supplier Selection Criterion in Auto–Motive Infotainment Industry: EFA Model. J. Educ. Soc. Sci. 2016, 3, 118–122.

56. Blackhurst, J.; Christopher, W.C.; Debra, E.; Robert, B.H. An empirically derived agenda of critical research issues for managing supply-chain disruptions. Int. J. Prod. Res. 2005, 43, 4067–4081. [CrossRef]

57. Desai, S.; De, P.; Gomes, F. Design for Nano/Micro Manufacturing: A Holistic Approach towards Achieving Manufacturing Excellence. J. Udyog Pragati 2015, 39, 18–25.

58. Liu, F.H.F.; Hai, H.L. The voting analytic hierarchy process method for selecting supplier. Int. J. Prod. Econ. 2005, 97, 308–317. [CrossRef]

59. Desai, S.; Bidanda, B.; Lovell, M.R. Material and process selection in product design using decision-making technique (AHP). Eur. J. Ind. Eng. 2012, 6, 322–346. [CrossRef]

60. Saaty, T.L. The Analytic Hierarchy Process: Planning, Priority Setting & Resource Allocation; McGraw-Hill: New York, NY, USA, 1980.

61. Brans, J.P. Lingenierie de la Decision. Elaboration Dinstruments Daide a la Decision, Methode PROMETHEE. In Laide a la Decision: Nature, Instruments et Perspectives Davenir; Nadeau, R., de Landry, M., Eds.; Universite Laval: Quebec, QC, Canada, 1982; pp. 183–214.

62. Nirmal, N.P.; Bhatt, M.G. Selection of automated guided vehicle using single valued neutrosophic entropy based novel multi attribute decision making technique. In New Trends in Neutrosophic Theory and Applications; Smarandache, F., Pramanik, S., Eds.; Pons Publishing House/Pons asbl: Bruxelles, Belgium, 2016; p. 105.

63. Vijay, M.A.; Shankar, C. Facility Location Selection Using PROMETHEE II Method. In Proceedings of the 2010 International Conference on Industrial Engineering and Operations Management, Dhaka, Bangladesh, 9–10 January 2010; pp. 59–64.

64. Gaikwad, L.; Sunnapwar, V. Supplier Evaluation and Selection in Automobile Industry. Ind. Eng. 2019, 1, 84383

65. Hussain, M.; Javed, W.; Hakeem, O.; Yousafzai, A.; Younas, A.; Awan, M.J.; Nobanee, H.; Zain, A.M. Blockchain-Based IoT Devices in Supply Chain Management: A Systematic Literature Review. Sustainability 2021, 13, 13646. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.