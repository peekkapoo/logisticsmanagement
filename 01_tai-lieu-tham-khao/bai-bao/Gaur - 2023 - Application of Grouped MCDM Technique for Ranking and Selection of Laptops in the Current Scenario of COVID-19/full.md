# Application of Grouped MCDM Technique for Ranking and Selection of Laptops in the Current Scenario of COVID-19

Avinash Gaur\*

\*Corresponding Author, Ph.D., Department of Engineering, Muscat College of Technology, University of Technology and Applied Sciences, Sultanate of Oman. E-mail: avinash.gaur@utas.edu.om

## Abstract

In the modern technological age, laptops are widely used for doing various day-to-day activities and getting updates all around us. The COVID-19 situation is playing a vital role in a dynamic shift in buyer behavior with multiple personal computing devices at home. Prioritizing and selecting appropriate laptop devices is difficult because there are several options of laptops that are available in the market, and these are equipped with the latest features to do gaming, designing, attending online classes, and performing office and other everyday tasks. Multiple selection criteria are complex. MCDM (Multiple Criteria Decision Making) approaches can handle and analyze these complicated criteria. By using MCDM techniques, decision-making can be done to select the top-ranked alternative from among the available alternatives. This paper exhibits a group of two MCDM techniques; Best Worst Method (BWM) and Analytical Hierarchy Process (AHP), which have been used to evaluate relative weights of considered conflicting criteria such as brand, price, storage capacity, RAM, processor, weight, touch screen, Bluetooth, and screen size, and these weights are used in the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for ranking and selecting the best product of laptops.

Keywords: MCDM, AHP, BWM, TOPSIS, Laptop Selection

## Introduction

The COVID-19 pandemic has increased people's dependency on digital technologies in the last two years. The easiest thing to do in such a scenario is to sit in front of a computer to connect with people, for work, education, enjoyment, or shopping. Everyone spends more time on screens than ever, alternating between smartphones, tablets, television, and computers. The versatility, portability, and adaptability of laptop computers are all important reasons for their widespread use. Last year, the demand for laptops increased drastically. However, the extremely competitive laptop computer market makes it difficult for customers to make an informed decision. All the laptop computer manufacturers provide extensive information on the features and specs of their models. Purchasing a laptop is a difficult and confusing task because you must examine several variables and evaluate various models with the finest features.

According to worldwide laptop shipment figures, 218 million (a 26% increase) laptop devices were sold during the pandemic in 2020. It has reached 225 million in 2021. As a result, there is a large demand for laptops, and it is necessary to research which factors are most important.

Multiple-Criteria Decision-Making (MCDM) methods can deal with such complex and conflicting real-life problems. By using MCDM techniques, decision-making can be done for selecting or ranking available finite alternatives. The Analytical Hierarchy Process (AHP) has been used in a variety of real-world scenarios. This is a structured method to organize and analyze complex decisions. Mathematics is combined with psychology in AHP. (Saaty, 1990, 1994). This refers to a method for calculating the weights of assessment criteria that is fairly accurate. Opinions of the individual experts are used for assessing the comparative weights of factors by making pairwise comparisons. In recent years, several researchers have focused on evaluating the criteria of laptop ranking and selecting the best one. Rezaei (2015) introduced the Best Worst Method (BWM) model as an MCDM method that enables decision-makers to determine the weights of criteria by selecting the best and worst criteria.

The purpose of this study is to use an integrated approach of two MCDM techniques; AHP and BWM, to calculate the relative weights of the criteria for buying laptops; and the Technique for Order Preference by Similarity to the Ideal Solution (TOPSIS), to evaluate and calculate the ranking of laptop models. It is straightforward to distinguish the laptops from one another using the TOPSIS technique on the alternatives. The actual numerical outcomes of the findings have also been shown. This study demonstrated that group MCDM models (AHP-BWM and TOPSIS) can be used to select the best laptop based on a variety of factors such as brand, price, storage capacity, RAM, processor, weight, touch screen, Bluetooth, and screen size.

The list of the paper's remnants is exhibited in Table 1. The related literature review is described in Section 2. The research problem is described in Section 3 along with the steps of the MCDM techniques that were used. Section 4 contains the case study, numerical experiment, and discussion. Section 5 discusses conclusions and recommendations for future research.

## Literature Review

This section is divided into two sub-sections. The first is a brief description of identifying criteria as a fundamental stage in MCDM. Then nine research papers are examined to compile a list of appropriate criteria. A short-term review (Table 1) of recent studies in laptop, computer, or mobile selection is offered in another sub-section, in which these studies are undertaken utilizing various MCDM approaches.

Pekkaya et al. (2014) used DEA, TOPSIS, and VIKOR to perform a comparative study for laptop selection. Goswami et al. (2021) studied in their study to pick the finest laptop model out of six options on the market. In his study, seven factors are used in the selection process (RAM, brand, OS, processor, HDD capacity, screen size, and color). AHP determines the weights of the criteria. A preference ranking order of the six models is provided, indicating the best model to the worst.

Sanyoto et al. (2017) stated that a decision support system is one approach to assist the potential buyer in determining a laptop that will be purchased in line with the criteria. The AHP approach was employed in this decision support system to aid in the laptop selection. Çakır et al. (2020) employed the DEMATEL approach to find interactions not seen in the literature, and fuzzy AHP for setting criteria priority. The price and brand image of a laptop have more interrelated actions than the other main criteria. According to the interaction matrices/diagrams, brand image, together with price, had a major effect on other factors.

Goswami et al. (2020) developed a research strategy for determining the optimum mobile device among a variety of options on the market. Two Multiple Criterion Decision-Making tools (MCDM) have been used for this selection, namely Complex Proportional Assessment (COPRAS) and Additive Ratio Assessment (ARAS). The recommended ranking order is compared using both methods, and it is discovered that the outcome results are the same using both techniques, except for a tiny difference in the ranking of the middle-order options.

Swain et al. (2018) explored the applicability of the popular Analytic Hierarchy Process (AHP) for understanding consumer-buying behavior when shopping for goods. This study is conducted on the purchasing behavior of two popular products, such as a mobile handset and a laptop system. Yunita et al. (2019) emphasized the purpose of buying a laptop depending on the buyer's capabilities and requirements. In his study the Analytical Hierarchy Process (AHP) method was used.

Table 1. Various MCDM applications

<table><tr><td>MCDM Method</td><td>Application</td><td>References</td></tr><tr><td>AHP</td><td>COVID-19/ Laptop selection/Road safety/shopping/ port location/ stock index/ Mining/ Selection of desktop computer/Mobile phone selection/ Computer hardware industry</td><td>Abdillah et al., 2022; Ajrina et al., 2018; Çakır et al., 2020; Chowdhury et al., 2022; Gaur et al., 2021; [13] Goswami et al., 2021; Goswami et al., 2020; Hota et al., 2018; Iqbal et al., 2020; Işıklar et al., 2007; Mitra et al., 2019; Moslem et al., 2020; Ravi, 2012; Yunita et al., 2019</td></tr><tr><td>FAHP</td><td>Laptop/ Car selection/ notebook/ technical institution/ framework</td><td>Çakır et al., 2020; Chang, 1996; Chatterjee et al.,2010;Chou et sl.,2005;Mitra et al.,2019;Mitra S et al.,2019; Singh et al., 2019; Srichetta et al.,2011</td></tr><tr><td>DEMATEL</td><td>Laptop selection</td><td>Çakır et al., 2020</td></tr><tr><td>BWM</td><td>Laptop/ electric vehicle/ mining/ agriculture/ port location/ road safety/ Concept/ Power grid</td><td>Ajrina et al., 2018; Cheraghalipour et al., 2018; Chowdhury et al., 2022; Moslem et al., 2020; Rezaei, 2015; You et al., 2017</td></tr><tr><td>COPRAS</td><td>Mobile selection</td><td>Goswami et al, 2020</td></tr><tr><td>VIKOR</td><td>Agriculture/ airport</td><td>Cheraghalipour et al., 2018</td></tr><tr><td>TOPSIS</td><td>Laptop selection/Car selection/Selection of desktop computer/ Mobile phone selection/ Computer hardware industry/ Healthcare/Power grid</td><td>Adalı et al., 2021; Goswami et al., 2021; Hota et al., 2018; Işıklar et al., 2007; Kecek et al., 2016; Kusnadi et al., 2017; Lakshmi et al., 2015; Mitra et al., 2019; Ravi, 2012; Singh et al., 2019; You et al., 2017</td></tr><tr><td>ARAS</td><td>Mobile selection</td><td>Goswami et al, 2020</td></tr><tr><td>SAW</td><td>Stock index/ Laptop selection</td><td>Harahap et al.,2021; Hota et al.,2018; Keek et al., 2016</td></tr><tr><td>MOORA</td><td>Laptop selection</td><td>Aytaç et al., 2017</td></tr><tr><td>PSI</td><td>Laptop marketing location</td><td>Sahir et al., 2018</td></tr></table>

## Methodology

This section includes a summary of BWM, AHP, and TOSPIS, as well as the specified criteria and sub-criteria. In addition, Figure 1 depicts the proposed methodology for this paper.

![](images/0df75c449885bcc04cdbfd1081fbe5f4c52ccb6f0860b9d0df7ba569e6ae82ca.jpg)  
Figure 1. Proposed framework

## Contribution of the study

• Globally, demand for Laptops has been increased although the supply is affected due to lockdown in unprecedented on-going COVID-19 pandemic situation. In current situation, a common man’s expectation with the laptop device has become higher. They need more specifications in laptops like Bluetooth and touch screen.

• AHP-BWM and TOPSIS as important perceptions of consumer evaluation for decision support systems for selecting laptops are used in this hybrid MCDM approach.

• By using the proposed approach, customers may select the best suited laptop device.

## Analytical hierarchy process

Multi-criteria decision-making (MCDM) approaches are often used in nearly all sectors of life to simulate complicated real-world issues. In complicated and conflicted choice criteria, it refers to the best choice out of all the possible alternatives. The Analytic Hierarchy Process, which determines the relative weights among the multi-level criteria, is one of the very commonly used MCDM methods. The AHP technique is the most commonly employed in MCDM, and it has been effectively applied to a variety of practical decision-making issues. Saaty, 1990; 1994]. The AHP has a 3-layer hierarchy structure, as shown in Figure 2. The steps of the AHP technique are explained in Table 2.

Table 2. Stepwise process of AHP technique

<table><tr><td>Step No</td><td>Step</td></tr><tr><td>1</td><td>Problem definition</td></tr><tr><td>2</td><td>Identification of Criteria and alternatives</td></tr><tr><td>3</td><td>Prepare and float questionnaire</td></tr><tr><td>4</td><td>Construct a pairwise comparison based on Saaty&#x27;s scale of relative importance Table 3</td></tr><tr><td>5</td><td>Normalization</td></tr><tr><td>6</td><td>and calculate CI $CI = \frac{\lambda_{max} - n}{n - 1}$ the number of criteria is represented by n and RI (Table 4)</td></tr><tr><td>7</td><td>Calculate CR using the formula $CR = \frac{CI}{RI}$ </td></tr><tr><td>8</td><td>If CR &lt; 0.1 then calculated criteria are accepted otherwise experts revise their opinion until CR &lt; 0.1</td></tr></table>

![](images/d06c646612200cd1f962fda6248cc3561e5c350b996df316a32c915277fd5c0f.jpg)  
Figure 2. Analytical three-layer hierarchy structure

The value of Lambda max (eigenvalue) is the average of criteria weights. The CR is checked to see whether it is less than 0.1 or not. If it is less than 0.1, then do a ranking of criteria and sub-criteria using weights calculated using AHP. If not, then reconsider data by requesting participants to rethink and repeat and get CR until you get the CR < 0.1.

Table 3. Saaty scale of relative importance

<table><tr><td>Scale of importance</td><td>Rating, reciprocal</td></tr><tr><td>Equally</td><td>1,1</td></tr><tr><td>Equally to moderately</td><td>2,1/2</td></tr><tr><td>Moderately</td><td>3,1/3</td></tr><tr><td>Moderately to strongly</td><td>4,1/4</td></tr><tr><td>Strongly</td><td>5,1/5</td></tr><tr><td>Strongly to very strongly</td><td>6,1/6</td></tr><tr><td>Very strongly</td><td>7,1/7</td></tr><tr><td>Very strongly to Extremely</td><td>8,1/8</td></tr><tr><td>Extremely</td><td>9,1/9</td></tr></table>

Table 4. Saaty scale of random index

<table><tr><td>n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>RI</td><td>0</td><td>0</td><td>0.58</td><td>0.9</td><td>1.12</td><td>1.24</td><td>1.32</td><td>1.41</td><td>1.45</td><td>1.49</td><td>1.51</td></tr></table>

## Best- worst method

Rezaeri (2015) introduced the BWM model as an MCDM method that enables decisionmakers to determine the weights of criteria through mathematical models by selecting the best and worst criteria. The criteria for laptop selection were finalized by literature research and a panel discussion with specialists. BWM is a popular MCDM technique that is both powerful and time-consuming. For instance, in the fields of electric vehicles (Van de Kaa, 2017), supply chains (Cheraghalipour et al., 2018), quality assessment (Salimi, 2017), airports (Kumar et al., 2020), online retail shopping (Torkayesh et al., 2020), mining (Ajrina et al., 2018) and road safety (Moslem et al., 2020).

The steps of best-worst method as given by Rezaei (2015; 2016) are explained in Table 5.

## TOPSIS method

TOPSIS is another MCDM technique that was proposed by Hwang and Yoon (1981). Several researchers integrated it with AHP and BWM to solve many real problems. The step-wise procedure of TOPSIS is mentioned in Table 7.

Table 5. Step wise procedure of BWM

<table><tr><td>Step No</td><td colspan="5">Step</td></tr><tr><td>1</td><td colspan="5">Defining set of criteria C={c1, c2, c3,. cn}</td></tr><tr><td>2</td><td colspan="5">Determining best (cbest) and worst (cworst) criterions from C</td></tr><tr><td rowspan="3">3</td><td colspan="5">Construction of pairwise comparison of best criterion with respect to others</td></tr><tr><td>Best to others</td><td>c1</td><td>c2</td><td>...</td><td>cn</td></tr><tr><td>cbest</td><td>aB1</td><td>aB2</td><td>...</td><td>aBn</td></tr></table>

<table><tr><td rowspan="6">4</td><td colspan="2">Constructing a pairwise assessment of others based on the worst criterion</td></tr><tr><td>Others to worst</td><td> $c_{worst}$ </td></tr><tr><td> $c_1$ </td><td></td></tr><tr><td> $c_2$ </td><td></td></tr><tr><td>. .</td><td></td></tr><tr><td> $c_n$ </td><td></td></tr><tr><td>5</td><td colspan="2">In this, optimal weightings of criteria are calculated ( $w_1^*, w_2^*, ..., w_n^*$ )Solve the linear modelmin  $\xi$ s.t $\left| \frac{w_B}{w_j} - a_{Bj} \right| \leq \xi \forall j, \left| \frac{w_j}{w_w} - a_{jB} \right| \leq \xi \forall j$ s.t.  $\sum_j w_j = 1, \forall w_j \geq 0$ </td></tr><tr><td>6</td><td colspan="2">Calculate  $CR = \frac{\xi^*}{CI (Table 6)}$ </td></tr></table>

Table 6. BWM consistency index

<table><tr><td> $a_{BW}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>CI</td><td>0</td><td>0.44</td><td>1</td><td>1.63</td><td>2.3</td><td>3</td><td>3.73</td><td>4.47</td><td>5.23</td></tr></table>

Table 7. Step wise procedure of TOPSIS

<table><tr><td>Step No</td><td>Step</td><td>Calculation</td></tr><tr><td>1</td><td>Input the aggregated weights received from AHP-BWM</td><td>Geomean of weights calculated using AHP and BWM</td></tr><tr><td>2</td><td>Prepare normalized decision matrix R =[rij] by using numerical scale</td><td> $r_{ij} = \frac{x_{ij}}{\left\{ \sum_{i=1}^{M} x_{ij}{}^2 \right\}^{1/2}}$ </td></tr><tr><td>3</td><td>Mention beneficiary and no-beneficiary criteria</td><td></td></tr><tr><td>4</td><td>Calculate weighted decision matrix</td><td>Multiply each column of R by the corresponding weight</td></tr><tr><td>5</td><td>Compute the ideal best (vi*) and the ideal worst (vi-) solutions from V from last step (no 4)</td><td></td></tr><tr><td>6</td><td>Euclidean distance from ideal best (Si+) and Euclidian distance from ideal worst (Si-)</td><td> $s_{i+} = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j*)^2}, s_{i-} = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j - )^2}$ </td></tr><tr><td>7</td><td>Compute the performance score of each alternative</td><td> $P_i = \frac{S_i}{(S_i^* + S_i^-)}$ </td></tr><tr><td>8</td><td>Ranking the performance scores in descending order</td><td></td></tr></table>

## Case Study and Numerical Experiment

In the year 2020, due to the pandemic, a technological shift has occurred, and people are now more dependent on digital devices. Laptops are a good choice for doing work, attending classes, or doing entertainment. Because of the enhancement in demand and high expectations regarding specifications, it is more complicated and time-consuming to rank and select the most suitable laptop device for individuals. Based on experts and customers from a variety of domains, criteria are selected (Table 8), and a few shortlisted laptop alternatives are listed (Table 9). A hierarchy structure for selecting a laptop is also depicted in Figure 3.

## Data collection

The questionnaire was constructed after discussion with some technical people and customers. Then this questionnaire is floated to 45 experts who either belong to the computer software industry, academicians, or students. The criteria are chosen based on the customers’ requirements for the device. The criteria that are finally considered are listed in Table 8. The data is collected and aggregated using the geometric mean, which is then used to build pairwise comparison matrices for AHP (Table 10) and BWM (Table 11 and 12) calculations.

![](images/9f60faaa5be7ffd92d8b0d962c2284f393fc398b1926a2573ad331f154737dfd.jpg)  
Figure 3. Hierarchy structure of selecting laptop alternative

Table 8. Identified criteria description

<table><tr><td>Criteria</td><td>Criteria index</td><td>Type</td><td>References</td></tr><tr><td>Brand</td><td>Br</td><td>B</td><td>Pekkaya et al., 2014; Adalı et al., 2021; Wichapa et al., 2019</td></tr><tr><td>Price</td><td>P</td><td>NB</td><td>Sumi et al., 2010; Pekkaya et al., 2014; Lakshmi et al., 2015; Stanujkić et al., 2018; Wichapa et al., 2019</td></tr><tr><td>Storage capacity</td><td>S</td><td>B</td><td>Düzakinet al., 2005; Pekkaya et al., 2014; Wichapa et al., 2019; Rayhan et al., 2016; Stanujkić et al., 2018</td></tr><tr><td>RAM</td><td>R</td><td>B</td><td>Düzakinet al., 2005; Pekkaya et al., 2014; Wichapa et al., 2019; Stanujkić et al., 2018</td></tr><tr><td>Processor</td><td>P</td><td>B</td><td>Düzakinet al., 2005; Pekkaya et al., 2014; Wichapa et al., 2019; Stanujkić et al., 2018; Rayhan et al., 2016</td></tr><tr><td>Weight</td><td>W</td><td>NB</td><td>Sumi et al., 2010; Pekkaya et al., 2014; Wichapa et al., 2019; Stanujkić et al., 2018</td></tr><tr><td>Screen size</td><td>Ss</td><td>B</td><td>Sumi et al., 2010; Pekkaya et al., 2014; Lakshmi et al., 2015; Wichapa et al., 2019; Stanujkić et al., 2018</td></tr><tr><td>Bluetooth</td><td>Bt</td><td>B</td><td>-</td></tr><tr><td>Finger scan</td><td>F</td><td>B</td><td>-</td></tr></table>

B-Beneficiary, NB- Non-Beneficiary

Table 9. Shortlisted alternatives of laptops

<table><tr><td>Laptop Alternative</td><td>HP</td><td>Lenovo</td><td>Dell</td><td>Accer</td><td>Asus</td></tr><tr><td>Index</td><td>L1</td><td> $L_2$ </td><td>L3</td><td> $L_4$ </td><td>L5</td></tr><tr><td>Laptop Alternative</td><td>Microsoft</td><td>MSI</td><td>Apple</td><td>Ikon</td><td></td></tr><tr><td>Index</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td></td></tr></table>

## Pairwise comparison matrix for AHP

Following the pairwise comparison, tables have been constructed based on the data collected from respondents. For the calculations, MS Excel worksheets have been used by applying formulas to compute the weights of the criteria and check the consistency. In the table, CR<0.1, which is a threshold value (Saaty, 1990).

Table 10. Pairwise comparison matrix for AHP

<table><tr><td>Criteria</td><td>Br</td><td>S</td><td>P</td><td>R</td><td>W</td><td>Ss</td><td>P</td><td>T</td><td>Bt</td></tr><tr><td>Br</td><td>1</td><td>1/3</td><td>1/5</td><td>1/7</td><td>1/2</td><td>1/3</td><td>1/4</td><td>2</td><td> $\frac{1}{4}$ </td></tr><tr><td>S</td><td>3</td><td>1</td><td>1/4</td><td>1/8</td><td>1</td><td>1/2</td><td>1/3</td><td>1/2</td><td>1/3</td></tr><tr><td>P</td><td>5</td><td>4</td><td>1</td><td>1</td><td>6</td><td>5</td><td>1</td><td>4</td><td>2</td></tr><tr><td>R</td><td>7</td><td>8</td><td>1</td><td>1</td><td>3</td><td>3</td><td>2</td><td>4</td><td>5</td></tr><tr><td>W</td><td>2</td><td>1</td><td>1/6</td><td>1/3</td><td>1</td><td>1/2</td><td>1/2</td><td>2</td><td> $\frac{1}{2}$ </td></tr><tr><td>Ss</td><td>3</td><td>2</td><td>1/5</td><td>1/3</td><td>2</td><td>1</td><td>1/6</td><td>2</td><td>1/6</td></tr><tr><td>P</td><td>4</td><td>3</td><td>1</td><td> $\frac{1}{2}$ </td><td>2</td><td>6</td><td>1</td><td>2</td><td>1</td></tr><tr><td>T</td><td>1/2</td><td>2</td><td>1/4</td><td> $\frac{1}{4}$ </td><td>1/2</td><td>1/2</td><td>1/2</td><td>1</td><td>1/6</td></tr><tr><td>Bt</td><td>4</td><td>3</td><td>1/2</td><td>1/5</td><td>2</td><td>6</td><td>1</td><td>6</td><td>1</td></tr></table>

## Construction of preference matrices for BWM

First, the best and worst criteria are defined and selected. From the respondent’s survey, preference of the best criteria over others (Table 11) and preference of the worst criteria over others (Table 12) are computed.

Table 11. Best to others vector

<table><tr><td>Best to others</td><td>Br</td><td>S</td><td>P</td><td>R</td><td>W</td><td>Ss</td><td>P</td><td>T</td><td>Bt</td></tr><tr><td>P</td><td>2</td><td>5</td><td>1</td><td>2</td><td>9</td><td>3</td><td>4</td><td>6</td><td>3</td></tr></table>

Table 12. Others to worst vector

<table><tr><td>Others to worst</td><td>Br</td><td>S</td><td>P</td><td>R</td><td>W</td><td>Ss</td><td>P</td><td>T</td><td>Bt</td></tr><tr><td>W</td><td>8</td><td>4</td><td>9</td><td>6</td><td>1</td><td>3</td><td>5</td><td>3</td><td>4</td></tr></table>

## Results

Weights of criteria using AHP and BWM are mentioned in Table 13. Aggregated weights are computed for AHP and BWM by using the geometric mean statistical formula also in the same table.

Table 13. Weights calculated by using AHP and BWM

<table><tr><td>Criteria</td><td>AHP</td><td>BWM</td><td>AHP-BWM</td><td>Rank</td></tr><tr><td>Br</td><td>0.0352</td><td>0.1554</td><td>0.0739</td><td>5</td></tr><tr><td>S</td><td>0.0455</td><td>0.0622</td><td>0.0532</td><td>6</td></tr><tr><td>P</td><td>0.2081</td><td>0.2658</td><td>0.2352</td><td>1</td></tr><tr><td>R</td><td>0.2541</td><td>0.1554</td><td>0.1987</td><td>2</td></tr><tr><td>W</td><td>0.0573</td><td>0.0245</td><td>0.0375</td><td>8</td></tr><tr><td>Ss</td><td>0.0660</td><td>0.1036</td><td>0.0827</td><td>5</td></tr><tr><td>P</td><td>0.1455</td><td>0.0777</td><td>0.1063</td><td>4</td></tr><tr><td>T</td><td>0.0445</td><td>0.0518</td><td>0.0480</td><td>7</td></tr><tr><td>B</td><td>0.1437</td><td>0.1036</td><td>0.1220</td><td>3</td></tr><tr><td>Key indicators</td><td> $\lambda=9.966$ CI=0.1208CR=0.08</td><td> $\xi^{*}=0.04$ CR=0.009</td><td colspan="2"></td></tr></table>

As the CR <0.1 in the case of AHP technique applied to obtain weights of the criteria, calculated weights of the respective criteria are acceptable. The results are showing that criteria R (RAM) is on top of the criteria and the criteria Br (Brand) is at the bottom of the preferences. In the results, using BWM, CR is also near to zero and $\xi ^ { * }$ is 0.04. The final weights of criteria are calculated by aggregating the weights obtained by using AHP and BWM. These aggregated weights (Figure 4) of the criteria are to be used for further analysis for the ranking of laptop alternatives.

![](images/bc40743f818780251dfc72ae86a2d3bf87122156c589e0b13393785c3d9b563e.jpg)  
Figure 4. Computed criteria weights using AHP and BWM

After finalizing the weights of all the criteria, a pairwise normalized decision matrix for laptop alternatives is constructed and the criteria are tagged to be beneficiary (B) or nonbeneficiary (NB).

Table 14. Pairwise comparison of alternatives

<table><tr><td>B/NB</td><td>B</td><td>B</td><td>B</td><td>B</td><td>NB</td><td>B</td><td>NB</td><td>B</td><td>B</td></tr><tr><td>AHP-BWM</td><td>0.0739</td><td>0.0532</td><td>0.2352</td><td>0.1987</td><td>0.0375</td><td>0.0827</td><td>0.1063</td><td>0.0480</td><td>0.1220</td></tr><tr><td>Laptops</td><td>Br</td><td>S</td><td>P</td><td>R</td><td>W</td><td>Ss</td><td>P</td><td>T</td><td>Bt</td></tr><tr><td>L1</td><td>3</td><td>512</td><td>3</td><td>4</td><td>2</td><td>14</td><td>107</td><td>3</td><td>3</td></tr><tr><td>L2</td><td>4</td><td>1000</td><td>3</td><td>4</td><td>1.5</td><td>14</td><td>152</td><td>4</td><td>4</td></tr><tr><td>L3</td><td>4</td><td>512</td><td>7</td><td>16</td><td>1.5</td><td>14</td><td>440</td><td>4</td><td>4</td></tr><tr><td>L4</td><td>2</td><td>512</td><td>3</td><td>4</td><td>1.5</td><td>15</td><td>150</td><td>2</td><td>2</td></tr><tr><td>L5</td><td>3</td><td>512</td><td>7</td><td>4</td><td>1.5</td><td>14</td><td>280</td><td>4</td><td>3</td></tr><tr><td>L6</td><td>3</td><td>1000</td><td>5</td><td>8</td><td>1.5</td><td>14</td><td>350</td><td>2</td><td>4</td></tr><tr><td>L7</td><td>2</td><td>1000</td><td>5</td><td>8</td><td>1.5</td><td>15</td><td>349</td><td>2</td><td>3</td></tr><tr><td>L8</td><td>5</td><td>1000</td><td>7</td><td>8</td><td>1.5</td><td>13</td><td>490</td><td>4</td><td>4</td></tr><tr><td>L9</td><td>1</td><td>512</td><td>3</td><td>4</td><td>2</td><td>13</td><td>100</td><td>2</td><td>2</td></tr></table>

In the next step of the TOPSIS procedure, by multiplying each column by the corresponding weight of criteria, then computation is done for ideal best and ideal worst, and then the Euclidean distance from ideal best and ideal worst is calculated. Performance scores are also calculated using the formula mentioned in Table 15.

Table 15. Ranking of laptops using AHP-BWM-TOPSIS

<table><tr><td rowspan="2">Laptops</td><td>Euclidean distance from ideal best</td><td>Euclidean distance from ideal worst</td><td>Performance Score</td><td rowspan="2">Rank</td></tr><tr><td>Si+</td><td>Si-</td><td>Pi</td></tr><tr><td> $L_1$ </td><td>0.1252</td><td>0.0500</td><td>0.2855</td><td>7</td></tr><tr><td> $L_2$ </td><td>0.1231</td><td>0.0558</td><td>0.3117</td><td>6</td></tr><tr><td> $L_3$ </td><td>0.0426</td><td>0.1284</td><td>0.7509</td><td>1</td></tr><tr><td> $L_4$ </td><td>0.1288</td><td>0.0414</td><td>0.2430</td><td>9</td></tr><tr><td> $L_5$ </td><td>0.1101</td><td>0.0716</td><td>0.3941</td><td>4</td></tr><tr><td> $L_6$ </td><td>0.0847</td><td>0.0598</td><td>0.4137</td><td>3</td></tr><tr><td> $L_7$ </td><td>0.0875</td><td>0.0538</td><td>0.3809</td><td>5</td></tr><tr><td> $L_8$ </td><td>0.0841</td><td>0.0846</td><td>0.5015</td><td>2</td></tr><tr><td> $L_9$ </td><td>0.1306</td><td>0.0460</td><td>0.2606</td><td>8</td></tr></table>

The weight of the laptop L3 (Dell) puts it at the top of the list. In case the best one is not available in the market, then customers can move to the next ranked laptop (Apple) from the sequence $\mathrm { L 3 } { < } \mathrm { L } 8 { < } \mathrm { L } 6 { < } \mathrm { L } 5 { < } \mathrm { L } 7 { < } \mathrm { L } 2 { < } \mathrm { L } 1 { < } \mathrm { L } 9 { < } \mathrm { L } 4$ with respect to the rank (Figure 5).

![](images/b7b8620216d1eab494b488bf740bc3db2d8cc0f5d9e5d3a9aeb853430e67b7ce.jpg)  
Figure 5. Ranking of laptops using TOPSIS

## Conclusion

Global digitalization is the key factor driving the huge demand for laptop devices. The same reason is behind the change in the preference criteria of customers for selecting the most appropriate and suitable device. Prioritization of laptop alternates based on preferred criteria weights is a complex and time-consuming task for buyers.

In this paper, by analyzing available literature (Table 1), an attempt has been made to successfully identify laptop selection criteria. The criteria's relative weights are calculated using a combination of two MCDM techniques (AHP and BWM). These weights are exported to another MCDM technique; TOPSIS, for obtaining the ranks of alternatives. Finally, the best suitable laptop is selected.

This work can be enhanced by including more categories or by splitting categories into more layers of hierarchy. The decision support system may be developed by integrating other MCDM techniques.

## Conflict of interest

The authors declare no potential conflict of interest regarding the publication of this work. In addition, the ethical issues including plagiarism, informed consent, misconduct, data fabrication and, or falsification, double publication and, or submission, and redundancy have been completely witnessed by the authors.

## Funding

The author(s) received no financial support for the research, authorship, and/or publication of this article

## References

Abdillah, A. (2022). Implementation of the Analytical Hierarchy Process (AHP) Method in the Laptop Election Decision Support System for Students and Community in Medan City. ZERO: Jurnal Sains, Matematika dan Terapan, 5(2). DOI: http://dx.doi.org/10.30829/zero.v5i2.11123 recorded

Adalı, E. A., & Tuş, A. (2021). Hospital site selection with distance-based multi-criteria decisionmaking methods. International Journal of Healthcare Management, 14(2), 534-544.

Ajrina, A. S., Sarno, R., & Ginardi, R. H. (2018, September). Comparison of AHP and BWM methods based on geographic information system for determining potential zone of Pasir Batu mining. In 2018 International Seminar on Application for Technology of Information and Communication 453-457. IEEE.

Aytaç Adalı, E., & Tuş Işık, A. (2017). The multi-objective decision-making methods based on MULTIMOORA and MOOSRA for the laptop selection problem. Journal of Industrial Engineering International, 13(2), 229-237. https://doi.org/10.1007/s40092-016-0175-5

Çakır, F. S., & Pekkaya, M. (2020). Determination of interaction between criteria and the criteria priorities in laptop selection problem. International Journal of Fuzzy Systems, 22(4), 1177-1190.

Chang, D. Y. (1996). Applications of the extent analysis method on fuzzy AHP. European journal of operational research, 95(3), 649-655.

Chatterjee, D., & Mukherjee, B. (2010). Study of fuzzy-AHP model to search the criterion in the evaluation of the best technical institutions: a case study. International journal of engineering science and technology, 2(7), 2499-2510.

Cheraghalipour, A., Paydar, M. M., & Hajiaghaei-Keshteli, M. (2018). Applying a hybrid BWM-VIKOR approach to supplier selection: a case study in the Iranian agricultural implements industry. International Journal of Applied Decision Sciences, 11(3), 274-301.

Chou, T.Y. & Chan, M. C. (2005). An application of fuzzy multi-criteria decision making model for notebook purchasing, Corporate Banking Quarterly, 28(3), 183-207

Chowdhury, M. M. H., & Haque Munim, Z. (2022). Dry port location selection using a fuzzy AHP-BWM-PROMETHEE approach. Maritime Economics & Logistics, 1-29. DOI: 10.35940/ijrte.B1291.0782S319.

DÜZAKIN, Y. D. D. E., & Demirtaş, S. (2005). EN UYGUN PERFORMANSA SAHİP KİŞİSEL BİLGİSAYARLARIN OLUŞTURULMASINDA VERİ ZARFLAMA ANALİZİNİN KULLANIMI. Çukurova Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, 14(2), 265-280.

Gaur Avinash et al., (2021). Analytical hierarchy process technique to minimize the COVID-19 risk in various day-day-day activities. Global Review of Business and Technology (GBRT), 1(2), 39-51.

Goswami, S. S., & Behera, D. K. (2021). Best laptop model selection by applying integrated ahptopsis methodology. International Journal of Project Management and Productivity Assessment (IJPMPA), 9(2), 29-47. DOI: 10.4018/IJPMPA.2021070102

Goswami, S., & Mitra, S. (2020). Selecting the best mobile model by applying AHP-COPRAS and AHP-ARAS decision making methodology. International Journal of Data and Network Science, 4(1), 27-42.

Harahap, N. H. S., & Zahraini, A. (2021). Laptop selection decision support system according to buyer criteria with the simple additive weighting method. Journal of Soft Computing Exploration, 2(2), 127-134. https://doi.org/10.52465/joscex.v2i2.49

Hota, H. S., Awasthi, V. K., & Singhai, S. K. (2018). Comparative analysis of AHP and its integrated techniques applied for stock index ranking. In Progress in Intelligent Computing Techniques: Theory, Practice, and Applications.127-134. Springer, Singapore.

Hwang, C. L. and Yoon, K. S. (1981). Multiple Attribute Decision Making: Methods and Applications, Springer-Verlag, New York.

Iqbal, M., & Simangunsong, A. (2020). Laptop Selection Decision Support System Using Analytical Hierarchy Process Method. Login: Jurnal Teknologi Komputer, 14(2), 170-175.

Işıklar, G., & Büyüközkan, G. (2007). Using a multi-criteria decision making approach to evaluate mobile phone alternatives. Computer Standards & Interfaces, 29(2), 265-274.

Kecek, G., & Demirağ, F. (2016). A comparative analysis of TOPSIS and MOORA in laptop selection. Research on Humanities and Social Sciences, 6(14), 1-9.

Kumar, A., Aswin, A., & Gupta, H. (2020). Evaluating green performance of the airports using hybrid BWM and VIKOR methodology. Tourism Management, 76, 103941.

Kusnadi, A., & Kurniawan, E. (2017). Implementation of topsis method in web based system recommendations for student’s laptop selection (case study: Bhinneka. com). IJNMT (International Journal of New Media Technology), 4(1), 42-45.

Lakshmi T. Miranda, T., . L., V., P. V., & A., M. (2015). Identification of a Better Laptop with Conflicting Criteria Using TOPSIS. International Journal of Information Engineering and Electronic Business, 7(6), 28–36.

Mitra, S. O. U. P. A. Y. A. N., & Goswami, S. S. (2019). Selection of the desktop computer model by AHP-TOPSIS hybrid MCDM methodology. International Journal of Research and Analytical Reviews, 6(1), 784-790.

Mitra, S., Goswami, S. S., & Parvej, M. (2019). Selection of the best laptop model by the application of fuzzy-ahp methodology. i-Manager's Journal on Management, 14(1), 33.

Moslem, S., Farooq, D., Ghorbanzadeh, O., & Blaschke, T. (2020). Application of the AHP-BWM model for evaluating driver behavior factors related to road safety: A case study for Budapest. Symmetry, 12(2), 243.

PEKKAYA, M., & Aktogan, M. (2014). Laptop Selection: A comparative analysis with DEA, TOPSIS and VIKOR. Ekonomik ve Sosyal Araştırmalar Dergisi.

Ravi, V. (2012). Selection of third-party reverse logistics providers for End-of-Life computers using TOPSIS-AHP based approach. International Journal of Logistics Systems and Management, 11(1), 24-37.

Rayhan, D. S. A. (2016). Selection of best laptop for educational purpose by using ANP. World Journal of Social Sciences, 6(2), 167-181.

Rezaei, J. (2015). Best-worst multi-criteria decision-making method. Omega, 53, 49-57.

Rezaei, J. (2016). Best-worst multi-criteria decision-making method: Some properties and a linear model. Omega, 64, 126-130.

Saaty, T. L. (1990). How to make a decision: the analytic hierarchy process. European journal of operational research, 48(1), 9-26.

Saaty, T. L. (1994). How to make a decision: the analytic hierarchy process. Interfaces, 24(6), 19-43.

Sahir, S. H., Afriani, J., Ginting, G., Fachri, B., Siregar, D., Simbolon, R., ... & Simarmata, J. (2018). The Preference Selection Index method in determining the location of used laptop marketing. Int. J. Eng. Technol, 7(3.4), 260-263.

Salimi, N. (2017). Quality assessment of scientific outputs using the BWM. Scientometrics, 112(1), 195-213.

Sanyoto, G. P., Handayani, R. I., & Widanengsih, E. (2017). Sistem Pendukung Keputusan Pemilihan Laptop Untuk Kebutuhan Operasional Dengan Metode AHP (Studi Kasus: Direktorat Pembinaan Kursus Dan Pelatihan Kemdikbud). Jurnal Pilar Nusa Mandiri, 13(2), 167-174.

Singh, R., & Avikal, S. (2019). A MCDM-Based Approach for Selection of a Sedan Car from Indian Car Market. In Harmony Search and Nature Inspired Optimization Algorithms (pp. 569-578). Springer, Singapore.

Srichetta, P., & Thurachon, W. (2011). Group Decision Analysis for the Product Selection Problem of Notebook Computers using Fuzzy AHP. In Proc. Int. Conf. Computer and Computational Intelligence.185-190.

Stanujkić, D., Jevtić, M., & Ivanov, B. (2018). An approach for laptop computers evaluation using multiple-criteria decision analysis. In Proc. of International Scientific Conference UNITECH (pp. 263-267).

Sumi, R. S., & Kabir, G. (2010). Analytical hierarchy process for higher effectiveness of buyer decision process. Global Journal of Management and Business Research, 10(2), 2-9.

Swain, A. K., & Dhurkari, R. K. (2018, May). Shopping Goods and Consumer Buying Behavior: An AHP Perspective. In Proceedings of the 2018 International Conference on Computers in Management and Business. 9-13.

Torkayesh, S. E., Iranizad, A., Torkayesh, A. E., & Basit, M. N. (2020). Application of BWM-WASPAS model for digital supplier selection problem: A case study in online retail shopping. Journal of Industrial Engineering and Decision Making, 1(1), 12-23.

Van de Kaa, G., Scholten, D., Rezaei, J., & Milchram, C. (2017). The battle between battery and fuel cell powered electric vehicles: A BWM approach. Energies, 10(11), 1707.

Application of Grouped MCDM Technique for Ranking and Selection…

Wichapa, N., Khokhajaikiat, P., Sarawan, K., & Gonwirat, S. (2019). Selection of the best laptop for educational purposes using hybrid decision making technique. วารสาร วิจัย มหาวิทยาลัย เทคโนโลยี ราช มงคล ศรี วิชัย, 10(3), 368

You, P., Guo, S., Zhao, H., & Zhao, H. (2017). Operation performance evaluation of power grid enterprise using a hybrid BWM-TOPSIS method. Sustainability, 9(12), 2329.

Yunita, D., Ayshwarya, B., Ridhawati, E., Huda, M., Hashim, A., Teh, K. S. M., ... & Maseleno, A. (2019). Application of analytical hierarchy process method in laptop selection. International Journal of Recent Technology and Engineering (IJRTE), 8(1603-1607).

Bibliographic information of this paper for citing:

Gaur, Avinash (2023). Application of Grouped MCDM Technique for Ranking and Selection of Laptops in the Current Scenario of COVID-19. Journal of Information Technology Management, 15 (3), 1-16. https://doi.org/ 10.22059/jitm.2023.93620