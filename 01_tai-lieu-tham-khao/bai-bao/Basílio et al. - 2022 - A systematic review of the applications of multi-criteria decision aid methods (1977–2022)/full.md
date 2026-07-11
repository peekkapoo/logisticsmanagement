Review

# A Systematic Review of the Applications of Multi-Criteria Decision Aid Methods (1977–2022)

Marcio Pereira Basílio <sup>1,2,</sup>\* , Valdecy Pereira <sup>2</sup> , Helder Gomes Costa <sup>2</sup> , Marcos Santos <sup>3</sup> and Amartya Ghosh <sup>4</sup>

Military Police of the Rio de Janeiro, Rio de Janeiro 21941-901, Brazil

2 Department of Production Engineering, Federal Fluminense University (UFF), Niteroi 24210-240, Brazil; valdecy.pereira@gmail.com (V.P.); heldergc@id.uff.br (H.G.C.)

3 Military Institute of Engineering (IME), Rio de Janeiro 21941-901, Brazil; marcosdossantos\_doutorado\_uff@yahoo.com.b

4 Symbiosis Institute of Business Management (SIBM), Hyderabad 509217, India; amartya.ghosh@sibmhyd.edu.in

米 Correspondence: marcio\_basilio@id.uff.br; Tel.: +55-21996379803

![](images/fb4bf556e56103f4de6244d8d33e474f9e74c19130c471df4daf7e5209d3026a.jpg)

Citation: Basílio, M.P.; Pereira, V.; Costa, H.G.; Santos, M.; Ghosh, A. A Systematic Review of the Applications of Multi-Criteria Decision Aid Methods (1977–2022). Electronics 2022, 11, 1720. https:// doi.org/10.3390/electronics11111720

Academic Editors: Agnieszka Konys and Agnieszka Nowak-Brzezi ´nska

Received: 29 April 2022 Accepted: 25 May 2022 Published: 28 May 2022

Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/87488a53fc285eb69be5a76985baca096f86a8c7580c6947209b440b57c2dc52.jpg)

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

Abstract: Multicriteria methods have gained traction in academia and industry practices for effective decision-making. This systematic review investigates and presents an overview of multi-criteria approaches research conducted over forty-four years. The Web of Science (WoS) and Scopus databases were searched for papers on multi-criteria methods with titles, abstracts, keywords, and articles from January 1977 to 29 April 2022. Using the R Bibliometrix tool, the bibliographic data was evaluated. According to this bibliometric analysis, in 131 countries over the past forty-four years, 33,201 authors have written 23,494 documents on multi-criteria methods. This area’s scientific output increases by 14.18 percent every year. China has the highest percentage of publications at 18.50 percent, followed by India at 10.62 percent and Iran at 7.75 percent. Islamic Azad University has the most publications with 504, followed by Vilnius Gediminas Technical University with 456 and the National Institute of Technology with 336. Expert Systems with Applications, Sustainability, and the Journal of Cleaner Production are the top journals, accounting for over 4.67 percent of all indexed works. In addition, E. Zavadskas and J. Wang have the most papers in the multi-criteria approaches sector. AHP, followed by TOPSIS, VIKOR, PROMETHEE, and ANP, is the most popular multi-criteria decision-making method among the ten nations with the most publications in this field. The bibliometric literature review method enables researchers to investigate the multi-criteria research area in greater depth than the conventional literature review method. It allows a vast dataset of bibliographic records to be statistically and systematically evaluated, producing insightful insights. This bibliometric study is helpful because it provides an overview of the issue of multi-criteria techniques from the past forty-four years, allowing other academics to use this research as a starting point for their studies.

Keywords: systematic review; multicriteria; MCDA; MCDM; MADM; MODM; AHP; TOPSIS; VIKOR; PROMETHEE; ANP

## 1. Introduction

As the transmission of scientific knowledge in its most diverse fields of study expands, literature evaluation becomes a demanding work for the researcher [1]. The challenge is reflected in the volume of research published each month by thousands of academic publication outlets. According to [2]’s theory of limited rationality, a researcher’s rationality is constrained by the knowledge available, the cognitive limitations of the individual mind, and the decision-making time availability.

Human activities require decision-making. All such decisions are based on an evaluation of individual decision options, typically based on the decision maker’s preferences, experience, and other data [3]. Some decisions are simple, while others are complex [4].

According to Kahraman et al. [5] and Govindan and Jepsen [6], some decisions are relatively simple, especially if the consequences of making the wrong decision are minor, whereas others are highly complex and have significant effects. In most cases, real-life problem-solving involves several competing points of view that must be considered to reach a reasonable decision [7]. A decision can be defined formally as a choice made based on available information or a method of action aimed at solving a specific decision problem [8]. In practice, multiple-criteria decision analysis (MCDA) evaluates possible courses of action or options by selecting a preferred option or sorting the options from best to worst [9–12]. In everyday practice, the use of MCDA is critical in signaling the best rational alternative to the decision-maker so that he can allocate finite resources between competing and alternative interests. Whether in an organizational or domestic setting, the decision-maker is constantly confronted with multiple paths and limited resources. Re searchers refer to multiple criteria methods in various ways. Some authors prefer the term multiple-criteria decision aid or aiding (MCDA), while others prefer to use the term multicriteria decision-making or multiple-criteria decision-making (MCDM), multi-objective decision-making (MODM), or multi-attribute decision-making (MADM). Some authors prefer the term multiple-criteria decision aid or aiding (MCDA), while others prefer to use the term multiple-criteria decision analysis [13].

The most often used MCDA approaches, as opined by [3,14], are divided into two “schools”: American and European. The American School of decision-support methods is based on a functional approach, namely the utilization of value or usability. These strategies typically do not account for data inconsistency, ambiguity, or decision-maker preferences. This collection of techniques is closely related to the operational approach based on a single synthesized criterion. MAUT, AHP, ANP, SMART, UTA, MACBETH, and TOPSIS are the critical methods used in the American School. The European School’s techniques are based on a relational concept. As a result, they employ a synthesis of criteria based on outranking relations. Transgression between pairs of decision alternatives characterizes this relationship. Among the European School of decision support methods, the ELECTRE and PROMETHEE groups are the most prominent. NAIADE, ORESTE, REGIME, ARGUS, TACTIC, MELCHIOR, and PAMSSEM are other methodologies from the European MCDA sector. Many multi-criteria decision-making strategies integrate ideas from the American and European decision-making schools. EVAMIX, QUALIFLEX, PCCA, MAPPAC, PRAGMA, PACMAN, IDRA, COMET, and DRSA are a few examples.

Furthermore, as stated by [6,14–16], MCDA methods are used to solve decision-making problems in several areas, including the information and communication technology; business intelligence; environmental risk analysis; environmental impact assessment and envi ronmental sciences; water-resource management; solid-waste management; remote sensing; flood-risk management; health-technology assessment; healthcare; transport; nanotechnology research; climate change; energy; international law and policy; human resources; financial management; performance and benchmarking; supplier selection; e-commerce and m-commerce; agriculture and horticulture; chemical and biochemical engineering; software evaluation; network selection; education and social policy; heating, ventilation, and air conditioning and small-scale energy management systems; and public security.

According to Sałabun et al. [3], despite the numerous MCDA approaches available, it is essential to note that no method is ideal and can be deemed acceptable for use in every decision-making context or for solving every choice problem [17]. As a result, different multi-criteria techniques may yield various choice suggestions [18]. However, if multiple multi-criteria methods produce inconsistent findings, the accuracy of each option is called into doubt [19]. In such a case, selecting a decision-support technique relevant to the given problem [20] becomes essential because only an appropriately chosen approach allows one to acquire the correct answer that reflects the decision maker’s preferences [21].

Humans make decisions regularly, and decision-making is an inherent element of people’s character. Some decisions are simple and have little impact on people’s lives; others, on the other hand, directly impact people’s lives, cities, and nations. In this regard, and given the importance of multi-criteria decision-making methods in assisting decision makers in a variety of fields, the current study aims to answer the following research questions (RQ) and develop a reference framework on academic productivity regarding multi-criteria decision-making methods:

RQ1: Who are the most influential authors and researchers in their scientific productivity in multi-criteria decision-making methods?

RQ2:What is the annual scientific publication growth in multi-criteria decision-making methods? RQ3: Which countries have the most significant production of articles on the multi-criteria methods of decision support?

RQ4: Which journals have the highest number of publications?

RQ5: What are the most used methods, and in which research areas?

RQ6: What are the conceptual structures of the multi-criteria decision-support methods?

Three hundred forty-two systematic literature studies on multi-criteria methods were discovered during the literature survey. The ten largest categories classified by Web of Science using multi-criteria methods were green sustainable science technology [22], energy fuels [23], environmental sciences [24], operations research and management science [25,26], computer science and artificial intelligence [27], management [28], economics [29], engineering environmental [30], computer science and interdisciplinary applications [31], and civil engineering [32].

This article is structured as follows: Section 2 briefly describes the methods and materials. Section 3 presents the preliminary bibliometric results and visualizes the collaborative relationships between countries and authors using R and the VOSviewer software. Keyword co-occurrences are analyzed, and strategic diagrams are constructed in the same section to reveal thematic trends on the multi-criteria decision support theme. The main discussions are summarized in Section 4.

## 2. Materials and Methods

This section presents the fundamental concepts that guided this study. The intention is not to cover all the subjects but rather to provide essential supporting information for understanding the research, the context, and the results.

The volume of academic publications is increasing at an accelerating rate. In this way, keeping up-to-date and knowing a given topic’s state of the art is becoming increasingly difficult. As stated by Aria and Cuccurullo [33], the emphasis on empirical contributions has resulted in voluminous and fragmented research flows, which contributes to the heavy work of the researcher to keep up to date. Researchers affirm that literature reviews are prevalent in the state-of-the-art synthesis of various themes [33,34].

The structured literature review is a traditional way to analyze and review scientific literature. This type of review provides an in-depth analysis according to the content of the literature [35–39]. However, this method suffers from several limitations. For instance, it is very time-consuming, and the number of analyzed papers is limited. It is almost impossible to analyze hundreds of documents through the structured literature-review process. Although the authors carefully select the documents according to several criteria, it is challenging to eliminate subjective factors, and some essential studies may be omitted. With the digitization of scientific journals, the volume of published papers has increased dramatically. A bibliometric analysis effectively handles hundreds, even thousands, of documents and reviews the related literature from a macro perspective [37].

The term bibliometric refers to the quantitative study of bibliographic materials [40,41]. It can characterize the development in a research field or capture the changes in a specific journal. Various techniques have been developed to conduct bibliometric analysis, and the most-used methods are social network analysis and co-word analysis [37].

Social network analysis is based on the premise that the relationships between units can be interpreted as a graph [42]. It is an effective method to evaluate the importance of nodes and reveal the network structure. In the bibliometric networks, different types of networks, such as coauthorship networks [43,44], bibliographic coupling networks [45], and co-citation networks [46], are constructed by bibliometrics [47].

Co-word analysis is a content-analysis technique proposed by [48,49]. It is applied to map the strength of associations between information items in textual data [50]. It involves a co-occurrence analysis of keywords in a selected body of literature. Co-occurrence analysis, a central task of association analysis in data mining, is used to group keywords with high relevance in clusters [51]. Typically, each set corresponds to a search theme. Researchers use co-occurrence analysis to identify established and emerging research themes or tracking patterns [52–54].

Numerous software tools support bibliometric analysis; however, many do not assist scholars in a complete recommended workflow. The most relevant tools are Cit-NetExplorer [55], VOSviewer [56], SciMAT [50], BibExcel [57], Science of Science (Sci2) Tool [58], CiteSpace [59], HistCite, Pajek, Gephi, Bibliometrix [33], and VantagePoint (www.thevantagepoint.com (accessed on 24 April 2022)). In this study, VOSviewer and Bibliometrix were used to conduct a co-citation analysis.

In this study, a topical query on 29 April 2022, was conducted in the Web of Science (WoS) and Scopus database, using the following search query: ((“multi-attribute decision making” or “madm” or “mcda” or “modm” or “mcdm” or “multi-criteria” or “multi-criteria” or “multiplecriteria”) and (“ahp” or “todim” or “topsis” or “promethee” or “electre” or “vikor” or “maut” or “fitradeoff” or “dematel” or “copras” or “multimoora” or “swara” or “analytical network process” or “anp” or “simple multi-attribute rating technique” or “smart” or “goal programming” or “thor” or “cbr” or “saw” or “condorcet” or “drsa” or “macbeth” or “paprika” or “wpm” or “wsm” or “utadis” or “waspas”)). The search was only restricted to titles, abstracts, keywords, and articles published between 1977 and 2022. Additionally, the search in the WoS database was limited to the Core Collection. The search query yielded 35,643 entries from the WoS and Scopus databases. Following the download of the records, the RStudio bibliometrix package version 1.2.1335 was installed on a Win64 operating system. Bibliometric analysis was performed using the Bibliometrix R package. The Bibliometrix tool was used to build the descriptive and co-citation networks. The function convert2df embedded in the Bibliometrix package was used to extract and create a data frame corresponding to the unit of analysis within the exported files from WoS and Scopus databases. After making the data frames from the WoS and Scopus files, the mergeDbSources function merged the WoS and Scopus data frames and excluded duplicate records from both files. Twelve thousand one hundred forty-nine duplicate records were removed, resulting in a data frame with 23,494 records for the bibliometric analysis. The process of obtaining the bibliographic records file can be seen in Figure 1.

![](images/e4317c2bd8dfed9e856a9507ff7647deec5c043c5a36ac614d59176d54247a03.jpg)  
<sup>h</sup> <sup>strategy</sup> <sup>and</sup> <sup>extraction</sup> <sup>of</sup> <sup>data.</sup> <sup>Source:</sup> <sup>Prepared</sup> <sup>by</sup> <sup>the</sup> <sup>authors</sup> <sup>based</sup> <sup>on</sup> <sup>Basilio</sup> Figure 1. Search strategy and extraction of data. Source: Prepared by the authors based on <sup>hosh</sup> <sup>and</sup> <sup>Prasad</sup> <sup>[61].</sup>Basilio et al. [60] and Ghosh and Prasad [61].

## 3. Results

om the bibliometric analysis show that 33,201 authors produced 23,494 The results from the bibliometric analysis show that 33,201 authors produced 23,494 documents in the period from 1 January 1977, to 29 April 2022. The types of documents identified in the sample, despite the limitations, are described in the methods and data section and further illustrated in Figure 2.

Regarding academic production, studies on multi-criteria decision-support methods had their genesis in 1977. Figure 3 depicts the publishing trajectory until April 2022. The graph shows that the upward trend began in 1986 with a modest inclination. During this time, the average number of publications each year was 7.3. From 1987 to 1996, the average number of papers per year climbed to 28.3 documents. This average increased to 123.2 records per year during the next ten years and finally reached 1265.73 from 2007 to 2021, indicating a strong level of interest in the topic among researchers. Taking the entire period into account, publications on multi-criteria decision-support methods grew at an annual percentage rate of 14.18. Figures 4 and 5 show the average total citations per year (16.06) and the average years from publication (6.36), respectively.

Five peaks are depicted in the graph shown in Figure 4. In 1983, the earliest and most important studies were conducted. In that year, six documents were published. The article by Van Laarhoven and Pedrycz [62], with a total citation count of 2158, had the most impact on citations in 1983. The authors presented a fuzzy variant of Saaty’s pairwise comparison method for deciding between many options when there are competing choice criteria. Eleven publications were included in the sample in 1986. The article by Brans et al. [63] had a significant impact that year, increasing the yearly average of 1609 citations. Brans et al. [63] introduced the PROMETHEE approach in this study. Chen et al. [64] had the most-cited paper in 1994, with 967 citations. Chinese researchers provided novel methods for dealing with fuzzy multi-criteria decision-making based on the theory of fuzzy sets. There were

2454 citations to Chen’s paper [64] in 2000, which affected the average of the 63 articles published that year. Chen [64] extended the TOPSIS model to the fuzzy environment. Furthermore, in 2004, two publications significantly impacted the average number of citations among the 128 papers published: Opricovic and Tzeng [65] had 2590 citations, while Pohekar and Ramachandran [66] had 1270 citations. The VIKOR and TOPSIS approaches were compared by Opricovic and Tzeng [65]. Pohekar and Ramachandran [66] conducted a systematic review of multi-criteria techniques for sustainable energy management. Table 16 of 30 provides a summary of the sample’s most cited articles.

![](images/8ecf18096e6b05d446a929817f2f50b0097f17e8b50b4fd87b61a80df2a93ba4.jpg)  
Figure 2. Graphical representation of the documents contained in the sample.Figure 2. Graphical representation of the documents contained in the sample.

![](images/671cb810a3329d86f3e171eff24fe4139e8721ee8d1e358cffd480deb74da6d2.jpg)  
Figure 3. Graphical representation of the annual scientific production. Note: The data for 2022 Figure 3. Graphical representation of the annual scientific production. Note: The data for 2022 <sup>corresponds</sup> <sup>to</sup> <sup>partial</sup> <sup>values</sup> <sup>quantified</sup> <sup>up</sup> <sup>to</sup> <sup>29</sup> <sup>April</sup> <sup>2022</sup>corresponds to partial values quantified up to 29 April 2022.

![](images/df8e749a660fe4d6fa64008bb362710bbfc61e7a612fc0172318bdf98778ed83.jpg)  
Figure 4. Graphical representation of the average total citations per year.Figure 4. Graphical representation of the average total citations per year.Figure 4. Graphical representation of the average total citations per year.

![](images/5fc733f906dab1b28afcce0665a877a29458a35ea11fb9950ce4b61c1206aab9.jpg)  
Figure 5. Graphical representation of the average article citations per yearFigure 5. Graphical representation of the average article citations per yearFigure 5. Graphical representation of the average article citations per year.

Five peaks are depicted in the grFive peaks are depicted in the grTable 1. Top 10 manuscripts per citations.

<table><tr><td>Rank</td><td>Title</td><td>Journal</td><td>First Author</td><td>Publication Year</td><td>Total Citations</td><td>TC per Year</td></tr><tr><td>1</td><td>A fuzzy extension of Saaty&#x27;s priority theory</td><td>Fuzzy Sets and Systems</td><td>van Laarhoven, PJM</td><td>1983</td><td>1950</td><td>50.0</td></tr><tr><td>2</td><td>Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS</td><td>European Journal of Operational Research</td><td>Opricovic S</td><td>2004</td><td>1834</td><td>101.9</td></tr><tr><td>3</td><td>Extensions of the TOPSIS for group decision-making under fuzzy environment</td><td>Fuzzy Sets and Systems</td><td>Chen CT</td><td>2000</td><td>1815</td><td>82.5</td></tr></table>

Table 1. Cont.

<table><tr><td>Rank</td><td>Title</td><td>Journal</td><td>First Author</td><td>Publication Year</td><td>Total Citations</td><td>TC per Year</td></tr><tr><td>4</td><td>How to select and how to rank projects: The Promethee method</td><td>European Journal of Operational Research</td><td>Brans JP</td><td>1986</td><td>1422</td><td>39.5</td></tr><tr><td>5</td><td>Application of multi-criteria decision making to sustainable energy planning—A review</td><td>Renewable and Sustainable Energy Reviews</td><td>Pohekar SD</td><td>2004</td><td>960</td><td>53.3</td></tr><tr><td>6</td><td>Handling multicriteria fuzzy decision-making problems based on vague set theory</td><td>Fuzzy Sets and Systems</td><td>Chen SM</td><td>1994</td><td>888</td><td>31.8</td></tr><tr><td>7</td><td>A fuzzy approach for supplier evaluation and selection in supply chain management</td><td>International Journal of Production Economics</td><td>Chen CT</td><td>2006</td><td>854</td><td>53.4</td></tr><tr><td>8</td><td>A state-of-the-art survey of TOPSIS applications</td><td>Expert Systems with Applications</td><td>Behzadian M</td><td>2012</td><td>742</td><td>74.2</td></tr><tr><td>9</td><td>A multi-criteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method</td><td>Expert Systems with Applications</td><td>Boran FE</td><td>2009</td><td>732</td><td>56.3</td></tr><tr><td>10</td><td>Extended VIKOR method in comparison with outranking methods</td><td>European Journal of Operational Research</td><td>Opricovic S</td><td>2007</td><td>706</td><td>47.1</td></tr></table>

The year 2022 is shown as an outlier in Figure 5. The average number of papers cited every year was calculated using only the year of publication, which skews the results by overestimating this value. However, there are no distinguishing traits in this year’s sample compared to earlier times. The volume of publications resulted in a total of 472,345 references.

## 3.1. Monitoring of Scientific Production around the World

Figure 6 shows that at least 120 countries or regions contributed to the research on multicriteria methods. China (n = 4327) is the largest contributor to multicriteria methods research, followed by India (n = 2485), Iran (n = 1812), Turkey (n = 1788), Taiwan (n = 1192), United States $\left( \mathbf { n } = 7 9 4 \right)$ , Brazil (n = 752), Spain (n = 608), Italy (n = 555), and Malaysia (n = 493). Regarding citations, Table 2 offers a slightly different order, but China continues to lead scientific production in terms of both knowledge generation and references to the scientific community: China (n = 82,615), Taiwan $\left( \mathbf { n } = 3 2 , 5 3 5 \right)$ , Turkey $\mathbf { ( n = } 2 8 , 7 3 9 )$ , India $( \mathbf { n } = 2 3 , 6 4 3 )$ , Iran (n = 23,613), United States (n = 20,217), Lithuania $( \mathbf { n } = 1 2 , 2 9 2 )$ , United Kingdom $( \mathbf { n } = 1 0 , 9 1 7 )$ , Spain (n = 10,071), and Italy (n = 8601). As shown in Table 1, the top 10 research universities are Islamic Azad University (n = 504), Vilnius Gediminas Technical University (n = 456), National Institute of Technology (n = 336), University of Tehran (n = 334), Indian Institute of Technology (n = 265), and Istanbul Technical University (n = 243), as seen in Table 1.

![](images/d0b633b893507d7ba7fceb583a8261d14dd4c6383a2574888941935ad5ebf6f7.jpg)  
Figure 6.<sup>Figure</sup> <sup>6.</sup> Graphical representation of the top 10 most productive countries.<sup>Graphical</sup> <sup>representation</sup> <sup>of</sup> <sup>the</sup> <sup>top</sup> <sup>10</sup> <sup>most</sup> <sup>productive</sup> <sup>countries</sup>

Figure 7 illustrates the relationships between organizations through the coauthorship analysis, using universities as the unit of analysis. The research was based on the following criteria: (1) the minimum number of documents per organization (n ≥ 50); (2) the minimum number of citations per organization (n ≥ 50). With the established criteria, 50 organizations out of the 7619 analyzed were separated. The nodes represent the universities. The diameter of the nodes represents the number of citations, and the thickness of the connecting lines between the nodes represents the level of cooperation between the institutions. As a result, Islamic Azad University and Vilnius Gediminas Technical University stand out in this analysis.

![](images/377f04e9035fc1bb375c4d94c5f3fdff1aeeb07cb2ad88ceae39dca260aaffc3.jpg)  
<sup>Figure</sup> <sup>7.</sup> <sup>The</sup> <sup>network</sup> <sup>map</sup> <sup>of</sup> <sup>institutions</sup> <sup>involved</sup> <sup>in</sup> <sup>multi-criteria</sup> <sup>methods</sup> <sup>of</sup> <sup>decision-suppor</sup>Figure 7. The network map of institutions involved in multi-criteria methods of decision-support <sup>research.</sup> <sup>Note:</sup> <sup>The</sup> <sup>colors</sup> <sup>of</sup> <sup>the</sup> <sup>circles</sup> <sup>are</sup> <sup>used</sup> <sup>to</sup> <sup>identify</sup> <sup>the</sup> <sup>clusters</sup> <sup>resulting</sup> <sup>from</sup> <sup>the</sup> <sup>analysi</sup>research. Note: The colors of the circles are used to identify the clusters resulting from the analysis of the relations provided by the VOSviewer software

Table 2. The top 10 countries/regions and institutions contributing to publications in multicriteria methods.

<table><tr><td>Rank</td><td>Country/Region</td><td>Article Counts</td><td>Percentage (N/23,394), %</td><td>Total Citations</td><td>Percentage (TNC/373.732) %</td><td>Average Article Citations</td><td>Freq</td><td>SCP</td><td>MCP</td><td>MCP_Ratio</td><td>Institutions</td><td>Country</td><td>Article Counts</td><td>Percentage (N/23,394), %</td></tr><tr><td>1</td><td>China</td><td>4327</td><td>18.50</td><td>82,615</td><td>22.11</td><td>19.09</td><td>0.2035</td><td>3794</td><td>533</td><td>0.1232</td><td>Islamic Azad University</td><td>Iran</td><td>504</td><td>2.15</td></tr><tr><td>2</td><td>India</td><td>2485</td><td>10.62</td><td>23,643</td><td>6.33</td><td>9.51</td><td>0.1169</td><td>2338</td><td>147</td><td>0.0592</td><td>Vilnius Gediminas Technical University</td><td>Lithuania</td><td>456</td><td>1.95</td></tr><tr><td>3</td><td>Iran</td><td>1812</td><td>7.75</td><td>23,613</td><td>6.32</td><td>13.03</td><td>0.0852</td><td>1526</td><td>286</td><td>0.1578</td><td>National Institute of Technology</td><td>India</td><td>336</td><td>1.44</td></tr><tr><td>4</td><td>Turkey</td><td>1788</td><td>7.64</td><td>28,739</td><td>7.69</td><td>16.07</td><td>0.0841</td><td>1701</td><td>87</td><td>0.0487</td><td>University of Tehran</td><td>Iran</td><td>334</td><td>1.43</td></tr><tr><td>5</td><td>Taiwan</td><td>1192</td><td>5.10</td><td>32,535</td><td>8.71</td><td>27.29</td><td>0.0545</td><td>969</td><td>223</td><td>0.1126</td><td>Indian Institute of Technology System</td><td>India</td><td>265</td><td>1.13</td></tr><tr><td>6</td><td>USA</td><td>794</td><td>3.39</td><td>20,217</td><td>5.41</td><td>25.46</td><td>0.0380</td><td>633</td><td>161</td><td>0.2234</td><td>Istanbul Technical University</td><td>Turkey</td><td>243</td><td>1.04</td></tr><tr><td>7</td><td>Brazil</td><td>752</td><td>3.21</td><td>5584</td><td>1.49</td><td>7.43</td><td>0.0365</td><td>697</td><td>55</td><td>0.0861</td><td>University of Belgrade</td><td>Serbia</td><td>180</td><td>0.77</td></tr><tr><td>8</td><td>Spain</td><td>608</td><td>2.60</td><td>10,071</td><td>2.69</td><td>16.56</td><td>0.0294</td><td>496</td><td>112</td><td>0.2169</td><td>Yildiz Technical University</td><td>Turkey</td><td>176</td><td>0.75</td></tr><tr><td>9</td><td>Italy</td><td>555</td><td>2.37</td><td>8601</td><td>2.30</td><td>15.50</td><td>0.0272</td><td>463</td><td>92</td><td>0.1780</td><td>Sichuan University</td><td>China</td><td>157</td><td>0.67</td></tr><tr><td>10</td><td>Malaysia</td><td>493</td><td>2.11</td><td>6482</td><td>1.73</td><td>13.15</td><td>0.0244</td><td>389</td><td>104</td><td>0.2331</td><td>Central South University</td><td>China</td><td>150</td><td>0.64</td></tr><tr><td></td><td>TOTAL</td><td>14,806</td><td>63.29</td><td>242,100</td><td>64.78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2801</td><td>11.97</td></tr></table>

Note: SCP: Single-country publications; MCP: Multiple-country publications.

This section provides a quick summary of the bibliometric findings. However, we chose to go beyond a typical bibliometric analysis by stratifying the investigation and providing the reader with specific information about the countries ranked in Figure 2. Table 3 lists the major research topics, universities, research funding organizations, notable authors, and the most relevant papers.

Table 3. Analytic picture of scientific production in the ten best-ranked countries.

<table><tr><td rowspan="2">Country</td><td colspan="4">TOP 5</td><td rowspan="2">Studies</td></tr><tr><td>Research Areas</td><td>Universities</td><td>Research Sponsors (%)</td><td>Authors</td></tr><tr><td>China</td><td>Computer science, engineering, environmental sciences and ecology, operations research and management science, science technology, and other topics</td><td>Sichuan University, Central South University, North China Electric Power University, Hong Kong Polytechnic University, and Chinese Academy of Sciences</td><td>National Natural Science Foundation of China (48.75), Fundamental Research Funds For The Central Universities (7.77), China Postdoctoral Science Foundation (3.6), Ministry of Education China (2.68), and China Scholarship Council (1.9)</td><td>Jian-Qiang Wang, Zeshui Xu, Hu-chang Liao, Pei-De Liu, and Jing Wang</td><td>[67-76]</td></tr><tr><td>India</td><td>Engineering, computer science, environmental sciences and ecology, business economics, science technology, and other topics</td><td>National Institute of Technology, Indian Institute of Technology, Jadavpur University, Birla Institute of Technology Science Pilani, and National Institute of Technology Tiruchirappalli</td><td>Department of Science Technology India (2.097), University Grants Commission India (1.258), Council of Scientific Industrial Research India (0.779), National Natural Science Foundation of China (0.479), and Ministry of Human Resource Development Government of India (0.359).</td><td>Harish Garg, Ashwani Kumar, Sanjay Kumar, Shankar Chakraborty, and Samarjit Kar</td><td>[77-86]</td></tr><tr><td>Iran</td><td>Engineering, computer science, environmental sciences and ecology, business economics, science technology, and other topics</td><td>Islamic Azad University, University of Tehran, Amirkabir University of Technology, Tarbiat Modares University, and Iran University Science Technology</td><td>University of Tehran (0.925), National Natural Science Foundation of China (0.727), Austrian Science Fund (0.661), Islamic Azad University (0.528), and Iran National Science Foundation (0.462)</td><td>Seyed Meysam Mousavi, Maghsoud Amiri, Reza Tavakkoli-Moghaddam, Behnam Vahdani, and Abdolreza Yazdani-Chamzini</td><td>[87-96]</td></tr><tr><td>Turkey</td><td>Computer science; engineering, business economics, operations research and management science, and environmental sciences and ecology</td><td>Istanbul Technical University, Yildiz Technical University, Gazi University, Galatasaray University, and Karadeniz Technical University</td><td>Galatasaray University (3.628), Turkiye Bilimsel Ve Teknolojik Arastirma Kurumu Tubitak (2.243), Bagep Award of The Science Academy in Turkey (0.396), Erciyes University (0.396), and European Commission (0.396)</td><td>Cengiz Kahraman, Gulcin Buyukozkan, Basa Oztaysi, Ihsan Kaya, and Metin Dagdeviren</td><td>[97-106]</td></tr><tr><td>Taiwan</td><td>Computer science; engineering, operations research and management science, business economics, and environmental sciences and ecology</td><td>National Yang Ming Chiao Tung University, Nan Kai University Technology, National Taipei University, National Taipei University of Technology, and National Kaohsiung University of Science Technology</td><td>Ministry of Science and Technology Taiwan (18.635), Chang Gung Memorial Hospital (1.426), National Natural Science Foundation of China (1.426), Taiwan Ministry of Science and Technology (1.120), and Ministry Of Sciences And Technology In Taiwan (1.018)</td><td>Gwo-Hshiung Tzeng, James J. H. Liou, Chi-Yo Huang, Ming-Lang Tseng, and Ting-Yu Chen</td><td>[107-116]</td></tr><tr><td>United States</td><td>Engineering, computer science, operations research and management science, business economics, and environmental sciences and ecology</td><td>State University System of Florida, Pennsylvania Commonwealth System of Higher Education, University of California, University of Memphis, and La Salle University</td><td>National Natural Science Foundation of China (9.138), National Science Foundation (2.464), China Scholarship Council (1.437), Fundamental Research Funds for the Central Universities (1.335), and Portuguese Foundation for Science and Technology (1.027)</td><td>Madjid Tavana, Florentin Smarandache, Surendra M. Gupta, Joseph Sarkis, and Dursun Delen</td><td>[117-126]</td></tr></table>

Table 3. Cont.

<table><tr><td rowspan="2">Country</td><td colspan="4">TOP 5</td><td rowspan="2">Studies</td></tr><tr><td>Research Areas</td><td>Universities</td><td>Research Sponsors (%)</td><td>Authors</td></tr><tr><td>Brazil</td><td>Engineering, computer science, business economics, operations research and management science, and environmental sciences and ecology</td><td>Universidade Federal de Pernambuco, Universidade Federal Fluminense, Universidade Federal do Rio De Janeiro, Universidade de São Paulo, and Universidade Tecnológica Federal do Paraná</td><td>National Council for Scientific and Technological Development (CNPQ) (22.18), Coordination for the Improvement of Higher Education Personnel (CAPES) (15.6), Foundation for Research Support of the State of São Paulo (FAPESP) (2.95), Foundation for the Support of Science and Technology of the State of Pernambuco (FACEPE) (1.39), and Foundation for Research Support of the State of Minas Gerais (FAPEMIG) (1.39)</td><td>Adiel Texeira de Almeida, Luiz Flavio Autran Monteiro Gomes, Danielle Costa Morais, Ana Paula Cabral Seixas Costa, and Helder Gomes Costa</td><td>[127-140]</td></tr><tr><td>Spain</td><td>Computer science, engineering, environmental sciences and ecology, operations research and management science, and business economics</td><td>The Polytechnic University of Valencia, Polytechnic University of Madrid, University of Granada, University of Oviedo, and Polytechnic University of Catalonia</td><td>European Commission (13.422), Spanish Government (8.555), National Natural Science Foundation of China (4.425), Spanish Ministry of Economy and Competitiveness (4.425), and Junta de Andalucia (2.507).</td><td>Morteza Yazdani, Juan Miguel Sanchez-Lozano, Monica Garcia-Melon, Maria Carmen Carnero, and Maria Teresa Lamata</td><td>[141-149]</td></tr><tr><td>Italy</td><td>Engineering, environmental sciences and ecology, computer science, science technology, other topics, and operations research and management science</td><td>University of Catania, University of Naples Federico II, University of Palermo, Polytechnic University of Turin, and University of Cassino</td><td>European Commission (3.303), Ministry of Education Universities and Research (2.385), National Natural Science Foundation of China (0.917), Ministry of Science and Higher Education Poland (0.734), and European Commission Joint Research Centre (0.550).</td><td>Salvatore Greco, Antonella Petrillo, Fabio De Felice, Fausto Cavallaro, and Silvia Carpitella</td><td>[150-159]</td></tr><tr><td>Malaysia</td><td>Engineering, computer science, science technology, other topics, environmental sciences and ecology, and operations research and management science</td><td>Universiti Teknologi Malaysia, Universiti Malaya, University Putra Malaysia, University Pendidikan Sultan Idris, and University Sains Malaysia</td><td>Ministry of Education Malaysia (4.48), University Teknologi Malaysia (2.83), University Sains Malaysia (2.12), University Kebangsaan Malaysia (1.18), and University Malaya (0.94).</td><td>Bilal Bahaa Zaidan, Aos Ala Zaidan, Lazim Abdullah, Osamah Shihab Albahri, and Mardini Abbas</td><td>[160-169]</td></tr></table>

## 3.2. Overview of the Leading Journals and Papers That Disseminate Research on Multi-Criteria Methods

Six thousand one hundred and five journals have published research on multi-criteria methods over the past forty-four years. As seen in Table 3, the top ten journals published 2180 of the total 20,861 studies on multi-criteria techniques (10.40%). Expert Systems with Applications, Sustainability, and Journal of Cleaner Production are the top three journals, accounting for over 4.67 percent of all indexed material. The journal with the highest impact factor (IF) is the Journal of Cleaner Production (7246), followed by Applied Soft Computing (5472), and Expert Systems with Applications (5041). (5.452). Five journals are classified as Q1 by the JCR 2019 standards, two as Q2, and three as Q3. In the eighth column of Table 4, the number of citations for each journal is displayed as an example.

Table 4. Top 10 most-active journals that published research articles on multicriteria methods (sorted by count).

<table><tr><td>Rank</td><td>Journal Title</td><td>Percentage (N/23,394), %</td><td>IF [2019]</td><td>Quartile in Category [2019]</td><td>H-Index</td><td>Article Counts</td><td>Total Number of Citations</td><td>Average Number of Citations</td><td>Percentage (TNC/373.732), %</td><td>Top 5 Countries by Source</td></tr><tr><td>1</td><td>Expert Systems with Applications</td><td>1.70</td><td>5.452</td><td>Q1</td><td>91</td><td>356</td><td>26,410</td><td>74.19</td><td>7.88</td><td>Taiwan, Turkey, China, USA, England</td></tr><tr><td>2</td><td>Sustainability</td><td>1.68</td><td>2.576</td><td>Q3</td><td>25</td><td>352</td><td>2978</td><td>8.46</td><td>0.89</td><td>China, Italy, Spain, Taiwan, Lithuania</td></tr><tr><td>3</td><td>Journal of Cleaner Production</td><td>1.29</td><td>7.246</td><td>Q1</td><td>43</td><td>270</td><td>7627</td><td>28.25</td><td>2.28</td><td>China, India, Iran, USA, Denmark</td></tr><tr><td>4</td><td>European Journal of Operational Research</td><td>1.26</td><td>4.213</td><td>Q1</td><td>76</td><td>264</td><td>22,144</td><td>83.88</td><td>6.61</td><td>France, England, USA, Belgium, Greece</td></tr><tr><td>5</td><td>Journal of Intelligent &amp; Fuzzy Systems</td><td>1.07</td><td>1.851</td><td>Q3</td><td>26</td><td>225</td><td>2508</td><td>11.15</td><td>0.75</td><td>China, Turkey, Pakistan, Iran, India</td></tr><tr><td>6</td><td>Applied Soft Computing</td><td>0.79</td><td>5.472</td><td>Q1</td><td>48</td><td>166</td><td>6557</td><td>39.50</td><td>1.96</td><td>China, Iran, Turkey, Taiwan, India</td></tr><tr><td>7</td><td>Computers &amp; Industrial Engineering</td><td>0.69</td><td>4.135</td><td>Q1</td><td>40</td><td>146</td><td>5165</td><td>35.38</td><td>1.54</td><td>China, Iran, Turkey, USA, Taiwan</td></tr><tr><td>8</td><td>Soft Computing</td><td>0.68</td><td>3.050</td><td>Q2</td><td>22</td><td>142</td><td>1402</td><td>9.87</td><td>0.42</td><td>China, Turkey, India, Iran, Taiwan</td></tr><tr><td>9</td><td>Symmetry-Basel</td><td>0.66</td><td>2.645</td><td>Q2</td><td>21</td><td>138</td><td>1407</td><td>10.20</td><td>0.42</td><td>China, Serbia, Lithuania, Pakistan, Taiwan</td></tr><tr><td>10</td><td>International Journal of Information Technology &amp; Decision Making</td><td>0.58</td><td>1.894</td><td>Q3</td><td>24</td><td>121</td><td>2254</td><td>18.63</td><td>0.67</td><td>China, Taiwan, Turkey, USA, Iran</td></tr><tr><td></td><td>Total</td><td>10.4</td><td></td><td></td><td></td><td>2180</td><td>78,452</td><td></td><td>23.42</td><td></td></tr></table>

Figure 8 depicts the inter-relationship between the Journals, which was developed based on the researchers’ preferences and referencing publications from sources with a high impact factor. The diameter of the circles is directly related to the number of citations, while the colors represent the identified clusters. In the eleventh column of Table 4, we can observe the five countries that published the most in each source. The maximum number of articles is from China, occupying the first position in eight out of the ten journals. The analysis of the highly cited papers shows that Renewable and Sustainable Energy Reviews, Expert Systems with Applications, and the International Journal of Production Economics have an incredible scientific impact on all scholars and have articles with more than 800 citations (Table 1).

## 3.3. Analysis of the Most Influential Authors Who Discuss the Topic of the Multi-Criteria Methods

Zavadskas E, Wang J, Tzeng G, Wang Y, and Kahraman C are among the top ten authors out of 29,050 who have published the most articles on this topic (Table 5). Edmundas Kazimieras Zavadskas is the first vice-rector of Vilnius Gediminas Technical University (VGTU). In addition, he is a member of the VGTU Senate, a professor, and the head of the Department of Construction Technology and Management. He has co-written over fifty novels in Lithuanian, Russian, German, and English. Corporations and academic institutions commissioned over forty research papers. The professor’s primary research interests include building life cycles, decision-support systems, and multi-criteria optimization methods in construction technology and management.

![](images/8c8ff712257d7d364a396c63e14c2f2eb020c93359bea09ee2d841545e267052.jpg)  
Figure 8. The network map of co-cited journals. Note: The colors of the circles are used to identify Figure 8. The network map of co-cited journals. Note: The colors of the circles are used to identify the clusters resulting from the analysis of the relations produced by the VOSviewer software. the clusters resulting from the analysis of the relations produced by the VOSviewer software.

Table 4. Top 10 most-active journals that published research articles on multicriteria methods<sub>Table</sub> <sub>5. Ranking</sub> <sub>of</sub> <sub>authors</sub> <sub>with</sub> <sub>the</sub> <sub>highest</sub> <sub>scientific</sub> <sub>production</sub> <sub>on</sub> <sub>multicriteria</sub> <sub>methods.</sub>

<table><tr><td>Rank</td><td>Authors</td><td>Country</td><td>University</td><td>H_Index</td><td>G_Index</td><td>Article Counts</td><td>Total Number of Citations</td><td>Average Number of Citations</td><td>First Author Counts</td><td>First Author Citations Counts</td><td>Average First Author Citations Counts</td></tr><tr><td>1</td><td>ZAVADSKAS E</td><td>Lithuania</td><td>Vilnius Gediminas Technical University</td><td>57</td><td>87</td><td>240</td><td>9955</td><td>41.48</td><td>50</td><td>1806</td><td>36.12</td></tr><tr><td>2</td><td>WANG J</td><td>China</td><td>Central South University</td><td>46</td><td>68</td><td>211</td><td>5785</td><td>27.42</td><td>65</td><td>1946</td><td>29.93</td></tr><tr><td>3</td><td>TZENG G</td><td>Taiwan</td><td>National Taipei University</td><td>44</td><td>97</td><td>191</td><td>9814</td><td>51.38</td><td>5</td><td>1621</td><td>324.2</td></tr><tr><td>4</td><td>WANG Y</td><td>China</td><td>Qinghai Normal University</td><td>28</td><td>57</td><td>161</td><td>3419</td><td>21.24</td><td>75</td><td>2222</td><td>29.62</td></tr><tr><td>5</td><td>KAHRAMAN C</td><td>Turkey</td><td>Istanbul Technical University</td><td>34</td><td>68</td><td>145</td><td>4980</td><td>34.34</td><td>39</td><td>1939</td><td>49.71</td></tr><tr><td>6</td><td>CHEN Y</td><td>China</td><td>Chongqing University</td><td>29</td><td>53</td><td>124</td><td>3036</td><td>24.48</td><td>42</td><td>1173</td><td>27.92</td></tr><tr><td>7</td><td>ZHANG H</td><td>China</td><td>Central South University</td><td>37</td><td>59</td><td>104</td><td>3620</td><td>34.81</td><td>27</td><td>552</td><td>20.44</td></tr><tr><td>8</td><td>XU Z</td><td>China</td><td>Sichuan University</td><td>31</td><td>64</td><td>95</td><td>4178</td><td>43.98</td><td>12</td><td>832</td><td>69.33</td></tr><tr><td>9</td><td>WANG X</td><td>China</td><td>Central South University</td><td>20</td><td>33</td><td>94</td><td>1321</td><td>14.05</td><td>28</td><td>526</td><td>18.78</td></tr></table>

Table 5. Cont.

<table><tr><td>Rank</td><td>Authors</td><td>Country</td><td>University</td><td>H_Index</td><td>G_Index</td><td>Article Counts</td><td>Total Number of Citations</td><td>Average Number of Citations</td><td>First Author Counts</td><td>First Author Citations Counts</td><td>Average First Author Citations Counts</td></tr><tr><td>10</td><td>TURSKIS Z</td><td>Lithuania</td><td>Vilnius Gediminas Technical University</td><td>34</td><td>63</td><td>93</td><td>4264</td><td>45.85</td><td>10</td><td>273</td><td>27.3</td></tr><tr><td>Total</td><td></td><td></td><td></td><td></td><td></td><td>1458</td><td>50,372</td><td>34.54</td><td>353</td><td>12,890</td><td>36.51</td></tr></table>

Figure 9 depicts a group of 160 authors grouped into six clusters based on two essential<sup>16</sup> <sup>of</sup> <sup>30</sup> criteria about the authors’ academic output: the minimum number of citations (n ≥ 500) and the minimum number of documents (n ≥ 10). Each cluster, identified by a distinct color, indicates the authors’ and co-authors’ iterations. The number of links and the totaldistinct color, indicates the authors’ and co-authors’ iterations. The number of links and links strength (TLS) are employed to determine the strength of the relationships. Each cluster’s featured author is the author with the most links and the highest TLS. In this way, each cluster’s information is presented: Cluster 1 (red) contains 37.5% of the sample, with an emphasis on authors Wang Y (Links = 112, TLS = 540) and Cheng Y (Links = 103, TLS = 394); Cluster 2 (green) contains 26.9% of the sample, with an emphasis on authors <sup>Wang</sup> <sup>J</sup> <sup>(Links</sup> <sup>=</sup> <sup>140,</sup> <sup>TLS</sup> <sup>=</sup> <sup>315),</sup> <sup>Xu</sup> <sup>Z</sup> <sup>(Links</sup> <sup>=</sup> <sup>141,</sup> <sup>TLS</sup> <sup>=</sup> <sup>2048),</sup> <sup>Zhang</sup> <sup>H</sup> <sup>(Links</sup> <sup>=</sup> <sup>144,</sup>authors Wang J (Links = 140, TLS = 315), Xu Z (Links = 141, TLS = 2048), Zhang H (Links TLS = 1935), and Wang X (Links = 121, TLS = 658); Cluster 3 (blue) contains 10.6% of the sample, with an emphasis on author Kahraman C (Links = 143, TLS = 2548); Cluster 4 (yellow) contains 10% of the sample, with an emphasis on authors Zavadskas E (Links = 153, TLS = 9165) and Turskis Z (Links = 138, TLS = 4074); Cluster 5 (purple) contains 7.5% of the sample, and author Liu H stands out (Links = 122, TLS = 1395); Cluster 6 (light blue) has 7.5% of the sample, highlighting the author Tzeng G (Links = 139, TLS = 2167).

![](images/aa49e73925d9919519a9c0fd72a5437639a1e57a7a1354be3247a0923a450b38.jpg)

## 3.4. Main Research Areas for the Application of Multi-Criteria Methods

The distribution of scientific production by research areas is depicted in Table 6. It is observed that there has been a shift in the preferences of academics in research fields over the past four decades. Table 7 displays the top five study areas by period. There was no change in the first five areas observed in the first two periods. From 1982 to 2002, research and applications of multi-criteria methods focused mainly on the following areas: operations research (1st), business economics (2nd), computer Science (3rd), engineering (4th), and mathematics (5th). With the increase in the volume of works published in the third decade under study, as shown in Figure 2, there was also a change in the research areas. From 2003 to 2012, the mathematics field was surpassed by environmental sciences ecology, which ranked fifth with 288 papers. Operations research, which held the numberone spot for two decades, was ranked third. The field of business economics lost its second place to computer science and fell to fourth place, followed by the ascent of engineering from fourth to first place. The most recent period analyzed was marked by a substantial increase in the number of published works. However, regarding the areas of interest of researchers, there has been a clear preference for engineering (1st) and computer science (2nd), followed by a change in preference as the traditional area of operations research has given way to environmental sciences ecology (3rd). In the fourth position, we find science technology, which has emerged with a greater level of interest from researchers due to the advancement of recent changes. The fifth place was occupied by business economics, a field in which scholars’ interest has diminished over the past four decades.

Table 6. Distribution of scientific production by research areas.

<table><tr><td>Research Areas</td><td>Recorded Count</td><td>% of 26,376</td></tr><tr><td>Engineering</td><td>5101</td><td>19.34</td></tr><tr><td>Computer science</td><td>4706</td><td>17.84</td></tr><tr><td>Environmental sciences ecology</td><td>2133</td><td>8.09</td></tr><tr><td>Business economics</td><td>2122</td><td>8.05</td></tr><tr><td>Operations research</td><td>2010</td><td>7.62</td></tr><tr><td>Science technology</td><td>1635</td><td>6.20</td></tr><tr><td>Energy fuels</td><td>915</td><td>3.47</td></tr><tr><td>Mathematics</td><td>869</td><td>3.30</td></tr><tr><td>Water resources</td><td>579</td><td>2.20</td></tr><tr><td>Materials science</td><td>511</td><td>1.94</td></tr><tr><td>Total</td><td>20,581</td><td>78.02</td></tr></table>

Note: It is necessary to clarify the value indicated in the third column. "26,376" this is the total pumber of articles in the sample associated with the research areas. Each article can be related to more than one search area.

Table 7. Evolution of scientific production according to research areas in the analyzed periods.

<table><tr><td>Research Areas</td><td colspan="4">Periods</td></tr><tr><td></td><td>1982 to 1992</td><td>1993 to 2002</td><td>2003 to 2012</td><td>2013 to 2022 (April 29)</td></tr><tr><td></td><td>Ranking</td><td>Ranking</td><td>Ranking</td><td>Ranking</td></tr><tr><td>Engineering</td><td>4th</td><td>4th</td><td>1st</td><td>1st</td></tr><tr><td>Computer science</td><td>3rd</td><td>3rd</td><td>2nd</td><td>2nd</td></tr><tr><td>Environmental sciences ecology</td><td>-</td><td>-</td><td>5th</td><td>3rd</td></tr><tr><td>Science technology</td><td>-</td><td>-</td><td>-</td><td>4th</td></tr><tr><td>Business economics</td><td>2nd</td><td>2nd</td><td>4th</td><td>5th</td></tr><tr><td>Operations research</td><td>1st</td><td>1st</td><td>3rd</td><td>-</td></tr><tr><td>Mathematics</td><td>5th</td><td>5th</td><td>-</td><td>-</td></tr></table>

Note: Only data corresponding to the fifth position in each period were recorded.

In Section 3.1, a global overview of the scientific output on multi-criteria methods is provided, highlighting the significant countries and classifying each production. However, as seen in the case of research domains, the hegemony of the scientific output has also evolved differently between nations. The shift in emphasis in specific scientific fields and the consolidation of others directly impact the hegemony of nations. If we analyze Table 2, we can see the consolidation of engineering and computer science as prominent areas in the production of the ten countries explored and the emergence of interest in science and technology.

## 3.5. Most-Used Methods

Table 8 lists the 26 methods examined throughout the sample period. The publishing period in WoS/Scopus concerning the investigated method is recorded in column 3. The chronology was produced based on the evolution of multi-criteria approaches, as shown in Figure 10, using information from the starting period of each method’s scientific output. The chronology depicts techniques that have been embedded in the literature and that continue to evolve, such as AHP, TOPSIS, PROMETHEE, ELECTRE, and others, such as SWARA, WASPAS, and FITRADEOFF, that have been published for up to ten years but are not yet well-known in academia. The publications of each studied technique are then noted in column 4. The AHP, TOPSIS, and VIKOR approaches have the most publications in the four decades studied. They are also the most commonly employed methods by professionals in solving multi-criteria related issues. Column 5 indicates the research areas wherein the specialists used the method the most. Computer science stands out among others because 47% of the researched methods address issues related to these areas, with the TOPSIS method being used the most. Engineering follows, with 35% of the methods, with the AHP method being the second most-used method. Business economics takes 11%, and operations research 8% respectively. In column 7, we build on the study to show a trend toward developing solutions that include one or more methodologies and the creation of hybrid models based on the data acquired. This section concludes by emphasizing that, despite the small number of applications, the scenario depicts the integration of multicriteria methods with some machine learning techniques, which could be the beginning of a new trend in the coming years (see column 8).

Table 8. Characteristics of the methods most used by researchers.

<table><tr><td>N</td><td>Method</td><td>Publication Time</td><td>Recorded Count</td><td>Research Areas</td><td>Publication Time (Integrated/Hybrid Model)</td><td>Hybrid Model</td><td>New Technologies (Machine Learning)</td></tr><tr><td>1</td><td>AHP</td><td>1990–2021</td><td>6.835</td><td>Engineering (2.329)</td><td>1995–2021</td><td>1.388</td><td>38</td></tr><tr><td>2</td><td>TOPSIS</td><td>1991–2021</td><td>4.907</td><td>Computer science (1.797)</td><td>2003–2021</td><td>1.024</td><td>47</td></tr><tr><td>3</td><td>VIKOR</td><td>2002–2021</td><td>1.475</td><td>Computer science (519)</td><td>2009–2021</td><td>416</td><td>5</td></tr><tr><td>4</td><td>PROMETHEE</td><td>1989–2021</td><td>1.382</td><td>Engineering (445)</td><td>2001–2021</td><td>202</td><td>16</td></tr><tr><td>5</td><td>ANP</td><td>2000–2021</td><td>1.262</td><td>Engineering (428)</td><td>2006–2021</td><td>488</td><td>10</td></tr><tr><td>6</td><td>ELECTRE</td><td>1991–2021</td><td>1.005</td><td>Computer science (331)</td><td>2003–2021</td><td>120</td><td>6</td></tr><tr><td>7</td><td>DEMATEL</td><td>2007–2021</td><td>888</td><td>Computer science (289)</td><td>2007–2021</td><td>476</td><td>5</td></tr><tr><td>8</td><td>GOAL PRO-GRAMMING</td><td>1983–2021</td><td>553</td><td>Operations research (202)</td><td>1993–2021</td><td>147</td><td>3</td></tr><tr><td>9</td><td>SAW</td><td>1997–2021</td><td>403</td><td>Engineering (137)</td><td>2007–2021</td><td>67</td><td>5</td></tr><tr><td>10</td><td>TODIM</td><td>1999–2021</td><td>306</td><td>Computer science (171)</td><td>2013–2021</td><td>56</td><td>2</td></tr><tr><td>11</td><td>COPRAS</td><td>2006–2021</td><td>294</td><td>Business economics (83)</td><td>2011–2021</td><td>100</td><td>2</td></tr><tr><td>12</td><td>WASPAS</td><td>2012–2021</td><td>214</td><td>Engineering (68)</td><td>2013–2020</td><td>67</td><td>0</td></tr><tr><td>13</td><td>MULTIMOORA</td><td>2011–2021</td><td>198</td><td>Computer science (75)</td><td>2011–2021</td><td>43</td><td>0</td></tr><tr><td>14</td><td>SWARA</td><td>2011–2021</td><td>181</td><td>Business economics (46)</td><td>2011–2021</td><td>90</td><td>1</td></tr><tr><td>15</td><td>MAUT</td><td>1984–2021</td><td>164</td><td>Engineering (56)</td><td>2007–2021</td><td>19</td><td>0</td></tr><tr><td>16</td><td>MACBETH</td><td>1999–2021</td><td>162</td><td>Computer science (47)</td><td>1999–2021</td><td>27</td><td>0</td></tr><tr><td>17</td><td>WSM</td><td>1994–2021</td><td>87</td><td>Engineering (29)</td><td>2014–2021</td><td>17</td><td>2</td></tr><tr><td>18</td><td>DRSA</td><td>2002–2021</td><td>85</td><td>Computer science (51)</td><td>2012–2021</td><td>20</td><td>4</td></tr><tr><td>19</td><td>WPM</td><td>1997–2021</td><td>57</td><td>Computer science (23)</td><td>2014–2021</td><td>7</td><td>0</td></tr><tr><td>20</td><td>CBR</td><td>1996–2021</td><td>40</td><td>Computer science (25)</td><td>2006–2020</td><td>10</td><td>1</td></tr></table>

Table 8. Cont.

<table><tr><td>N</td><td>Method</td><td>Publication Time</td><td>Recorded Count</td><td>Research Areas</td><td>Publication Time (Integrated/Hybrid Model)</td><td>Hybrid Model</td><td>New Technologies (Machine Learning)</td></tr><tr><td>21</td><td>CONDORCET</td><td>1999–2021</td><td>35</td><td>Business economics (9)</td><td>-</td><td>0</td><td>1</td></tr><tr><td>22</td><td>FITRADEOFF</td><td>2016–2021</td><td>29</td><td>Computer science (14)</td><td>-</td><td>0</td><td>0</td></tr><tr><td>23</td><td>UTADIS</td><td>1998–2020</td><td>27</td><td>Operations research (14)</td><td>2005–2016</td><td>2</td><td>0</td></tr><tr><td>24</td><td>SMART</td><td>1996–2021</td><td>22</td><td>Engineering (9)</td><td>2021</td><td>2</td><td>0</td></tr><tr><td>25</td><td>PAPRIKA</td><td>2014–2021</td><td>12</td><td>Computer science (4)</td><td>2020</td><td>1</td><td>0</td></tr><tr><td>26</td><td>THOR</td><td>2008–2021</td><td>5</td><td>Engineering (2)</td><td>-</td><td>0</td><td>0</td></tr></table>

![](images/e683a3df50e8840fb74cead2fa48ae34223dabe9f75fcbccccc9fade92463616.jpg)  
<sup>ion</sup> <sup>of</sup> <sup>scientific</sup> <sup>production</sup> <sup>classified</sup> <sup>by</sup> <sup>method</sup> <sup>over</sup> <sup>the</sup> <sup>period</sup> <sup>analyzed.</sup> Figure 10. Evolution of scientific production classified by method over the period analyzed.

## 3.6. Mapping the Evolution of Themes

Cobo et al. [170] assert the set of identified themes of the subperiod t, with $\mathrm { U } \in \mathrm { T } { \mathfrak { t } }$ representing each detected theme in the subperiod t. Let $\mathsf { V } \in \Gamma \hat { \mathsf { \Omega } } ( \mathsf { t } + 1 )$ represent each theme found in the subsequent subperiod t + 1. It is argued that there is a thematic progression from topic U to theme V if both related thematic networks contain the same keywords. Thus, V can be considered a development of U. Additionally, the keyword cluster $\mathbf { k } \in \mathbf { U } \cap \mathbf { V }$ is regarded as a “thematic nexus” or “conceptual nexus”.

Figure 11 was created using the “thematicEvolution” function of the Bibliometrix R package. The evolution of themes associated with multi-criteria methods is depicted in Figure 11 across the five time periods. In the first period, i.e., between 1977 to 1986, three themes are recorded. As the rectangles represented the same region during this period, it may be deduced that there was a balance in disseminating topics. In the second phase (1987–1995), there are twelve topics, of which eight had no foundation in the first period, such as “AHP”, “TOPSIS”, and “fuzzy set theory”. These methods have their earliest publication record in 1990/1991 (Table 8). Still, researchers favor them, as in the case of TOPSIS, which has the same rectangular area as “GOAL PROGRAMMING”, one of the three primary subjects of the program. During the third era (1996–2004), we recorded fourteen themes that originated in or branched from the preceding period. In this third period, the focus is on the AHP method, which is the most influential subject, as indicated by a distinct set of four keywords (“ahp”, “analytic hierarchy process”, and “analytical hierarchy process (ahp)”). It is important to note that the “GOAL PROGRAMMING” theme has become less popular and that the PROMETHEE and ELECTRE methods have become more popular. Despite being published for the first time in 1989/1991, they did not emerge as a topic until the third period. The themes decreased from fourteen to nine for the fourth phase (2005–2013). Two AHP-related concepts continue to hold the apex of importance. In addition to the PROMETHEE method, the TOPSIS methods, which did not emerge in the third era, reappeared distinctly. The final period evaluated between 2014–2022 continues with a reduction from nine to six themes presented in a balanced way, reflecting the preference for topics associated with the AHP and TOPSIS methods. The use of the theme-evolution map allowed us to graphically confirm the choice of specialists in solving multi-criteria problems using original tools in the AHP and TOPSIS methods during the study period.

![](images/6f6fadb462ef65ca6a4161f04219d27561e280cc8a3f2576f910c88511eae60f.jpg)  
Figure 11. The evolution of themes built with the authors’ keywords.

## 4. Discussion

This research article presents a bibliometric analysis of the multi-criteria methods from 1977 to 29 April 2022. The bibliographic data was obtained from the Scopus and Web of <sup>rom</sup> <sup>1977</sup> <sup>to</sup> <sup>29</sup> <sup>April</sup> <sup>2022.</sup> <sup>The</sup> <sup>bibliographic</sup> <sup>data</sup> <sup>was</sup> <sup>obtained</sup> <sup>from</sup> <sup>the</sup> <sup>Scopus</sup> <sup>and</sup> <sup>Web</sup> Science (WoS) databases. The bibliometric analysis was conducted using the Bibliometrix R <sup>f</sup> <sup>Science</sup> <sup>(WoS)</sup> <sup>databases.</sup> <sup>The</sup> <sup>bibliometric</sup> <sup>analysis</sup> <sup>was</sup> <sup>conducted</sup> <sup>using</sup> <sup>the</sup> tool and the VOSviewer software to investigate the essential characteristics of the studies done so far, including publications; citations, citation structure; influential authors; cocitation contributors and burst detection analysis; author-keywords; co-occurrence analyses; and timeline-view analysis. The ability to make judgments is a distinguishing character istic of a person. Man makes spontaneous and intuitive decisions based on his brain’s information-processing skills. We judge the color of our ties for a business meeting as to whether or not to invest millions of dollars in a specific project. We realize that we face two distinct types of decisions: simple and complex. We can make straightforward decisions with few variables and little trouble. However, when the problem involves a matrix (n × m) variable, we require methodologies and computer capabilities to systematize, arrange, and rank the best options to aid decision-making. Accordingly, the objective of this study was to comprehend the global evolution of research on the creation and use of multi-criteria decision methods.

With a scientific production growth rate of 14.18% each year, it is clear that the academic community is interested in researching and publishing publications on multi-criteria decision-making approaches. Moreover, 60.93% of all publications were concentrated in only ten nations, with China leading the way with 18.50%, India coming in second with 10.62%, and Iran coming in third with 7.75%. In addition, the remaining 39% of publica tions have an average production rate of less than 1%, suggesting that the dissemination of multi-criteria approach research in such nations could enhance academic output. The top 10 countries in terms of citations follow a consistent pattern, accounting for 62.48% of all citations made during the research period. Among the top 10 countries in terms of multi-country collaboration (MCP) in publications, Turkey has the lowest MCP ratio with 0.0487, indicating a limited partnership with researchers from other nations, followed by India (0.0592) and Brazil (0.0861). Malaysia leads multi-country collaboration, with an MCP ratio of 0.2331, followed by the United States (0.2234) and Spain (0.2169).

Regarding sites that publish articles on multi-criteria techniques, the study reveals the top ten journals that have published approximately 10.4% of the subject’s total publications. China, India, Iran, and Turkey, the four nations with the most publications on multi-criteria techniques, account for around 80% of the university-based publications on multi-criteria methods. These universities account for 11.79% of academic output, with the Islamic Azad University of Iran contributing 2.14% and Vilnius Gediminas Technical University of Lithuania accounting for 2.18%. Surprisingly, Lithuania is not among the top ten nations regarding scientific output. However, among the other authors in this survey, Prof. Edmundas Kazimieras Zavadskas of Lithuania ranks first with 240 articles on multicriteria approaches.

The journal Expert Systems with Applications has published 1.70% of all articles to date, followed by Sustainability with 1.68 percent and the Journal of Cleaner Production with 1.30%. The leading journals in terms of citations are Expert Systems with Applications, with an average of 7.88 citations per paper, followed by the European Journal of Operational Research, with 6.61 citations per article. Regarding the origin of publications, eight of the top ten countries publish most of their articles in the ten highest-ranked journals. In contrast, the European Journal of Operational Research ratio is 2 out of 10.

Regarding the most influential authors in this field, approximately 0.034% of 33,201 authors are responsible for 6.98% of publications over the past forty-four years, with ZAVAD-SKAS E having the most publications, with 240, followed by WANG J with 211 articles and TZENG G with 191 articles. This bibliometric analysis reveals that six of the top ten authors are Chinese, with the Central South University author affiliation standing out.

In addition to identifying writers with higher academic production, this study includes a comprehensive summary of the countries, funding sources, and the five multi-criteria approaches, i.e., AHP, TOPSIS, VIKOR PROMETHEE, and ANP, most frequently utilized by the authors in their respective studies. Engineering and computer science are the most prominent subjects in terms of research fields. One trend identified was the expansion of multi-criteria technique integration and the formation of hybrid models.

This paper gives a complete overview of multi-criteria methods through a bibliometric study, enabling scholars to comprehend the current state and future development patterns of multi-criteria decision-making methods research. As an indication for prospective research, we can emphasize the need to understand the emergence and regionalization of specific techniques and their variations, expand research within the identified countries to gain a deeper understanding of their scientific production on the issue investigated, apply topic modeling to find latent themes in the researched database, and systematize method variants and their interfaces with other research areas, such as machine learning.

Author Contributions: Conceptualization, M.P.B.; data curation, V.P.; formal analysis, M.S.; investi gation, V.P.; methodology, M.P.B.; project administration, M.S.; supervision, H.G.C.; validation, V.P.; writing—original draft, M.P.B.; writing—review and editing, M.P.B. and A.G. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: https://github.com/marciobasilio/bibliometric\_multicriteria (accessed on 24 April 2022).

Conflicts of Interest: The authors declare no conflict of interest.

## Abbreviations

The following abbreviations are used in this manuscript:

<table><tr><td>AHP</td><td>Analytic Hierarchy Process</td></tr><tr><td>ANP</td><td>Analytical Network Process</td></tr><tr><td>COMET</td><td>Characteristic Objects Method</td></tr><tr><td>COPRAS</td><td>Complex Proportional Assessment</td></tr><tr><td>DRSA</td><td>Dominance-based Rough Set Approach</td></tr><tr><td>ELECTRE</td><td>ÉLimination et Choix Traduisant la REalité (French)</td></tr><tr><td>MACBETH</td><td>Measuring Attractiveness by a Categorical Based Evaluation Technique</td></tr><tr><td>MCDA</td><td>Multi-Criteria Decision Analysis</td></tr><tr><td>MCDM</td><td>Multi-Criteria Decision Making</td></tr><tr><td>MODM</td><td>MultiObjective Decision Making</td></tr><tr><td>MOORA</td><td>Multi-Objective Optimization by Ratio Analysis</td></tr><tr><td>MULTIMOORA</td><td>MOORA plus the full Multiplicative Form</td></tr><tr><td>NAIADE</td><td>Novel Approach to Imprecise Assessment and Decision Environment</td></tr><tr><td>PCCA</td><td>Pairwise Criterion Comparison Approach</td></tr><tr><td>PROMETHEE</td><td>Preference Ranking Organization Method for Enrichment of Evaluation</td></tr><tr><td>WASPAS</td><td>Weighted Aggregated Sum Product Assessment</td></tr><tr><td>TODIM</td><td>Tomada de Decisão Interativa Multicritério (Portuguese)</td></tr><tr><td>TOPSIS</td><td>Technique for Order of Preference by Similarity to Ideal Solution</td></tr><tr><td>VIKOR</td><td>VlseKriterijumska Optimizacija I Kompromisno Resenje (Serbian)</td></tr></table>

## References

1. Basilio, M.P.; Pereira, V.; de Oliveira, M.W.C.M.; da Costa Neto, A.F.; de Moraes, O.C.R.; Siqueira, S.C.B. Knowledge discovery in research on domestic violence: An overview of the last fifty years. Data Technol. Appl. 2021, 55, 480–510. [CrossRef]

2. Simon, H.A. A Behavioral Model of Rational Choice. Q. J. Econ. 1955, 69, 99–118. [CrossRef]

3. Sałabun, W.; W ˛atróbski, J.; Shekhovtsov, A. Are MCDA Methods Benchmarkable? A Comparative Study of TOPSIS, VIKOR, COPRAS, and PROMETHEE II Methods. Symmetry 2020, 12, 1549. [CrossRef]

4 Behzadian, M.; Otaghsara, S.K.; Yazdani, M.; Ignatius, J. A state-of the-art survey of TOPSIS applications. Expert Syst. Appl. 2012, 39, 13051–13069. [CrossRef]

5. Kahraman, C.; Onar, S.C.; Oztaysi, B. Fuzzy Multicriteria Decision-Making: A Literature Review. Int. J. Comput. Intell. Syst. 2015, 8, 637–666. [CrossRef]

6 Govindan, K.; Jepsen, M.B. ELECTRE: A comprehensive literature review on methodologies and applications. Eur. J. Oper. Res. 2016, 250, 1–29. [CrossRef]

7. Wang, J.-J.; Jing, Y.-Y.; Zhang, C.-F.; Shi, G.-H.; Zhang, X.-T. A fuzzy multi-criteria decision-making model for trigeneration system. Energy Policy 2008, 36, 3823–3832. [CrossRef]

8. Greco, S.; Figueira, J.; Ehrgott, M. Multiple Criteria Decision Analysis; Springer: Berlin/Heidelberg, Germany, 2016.

9. Basilio, M.P.; Pereira, V.; Costa, H.G. Classifying the integrated public safety areas (IPSAs): A multi-criteria based approach. J. Model. Manag. 2019, 14, 106–133. [CrossRef]

10. Basilio, M.; Pereira, V. Operational research applied in the field of public security: The ordering of policing strategies such as the ELECTRE IV. J. Model. Manag. 2020, 15, 1227–1276. [CrossRef]

11. Basilio, M.P.; Pereira, V.; de Oliveira, M.W.C.; da Costa Neto, A.F. Ranking policing strategies as a function of criminal complaints: Application of the PROMETHEE II method in the Brazilian context. J. Model. Manag. 2020, 16, 1185–1207. [CrossRef]

12. Moreira, M.L.; Gomes, C.F.S.; dos Santos, M.; Basilio, M.P.; Costa, I.P.D.A.; Junior, C.d.S.R.; Jardim, R.R.-A.J. Evaluation of drones for public security: A multicriteria approach by the PROMETHEE-SAPEVO-M1 systematic. Procedia Comput. Sci. 2022, 199, 125–133. [CrossRef]

13. Roy, B. Decision-aid and decision-making. Eur. J. Oper. Res. 1990, 45, 324–331. [CrossRef]

14. Youd, S.; Fuchs-Hanusch, D. A bibliometric-based survey on AHP and TOPSIS techniques. Expert Syst. Appl. 2017, 78, 158–181. [CrossRef]

15. de Almeida, I.D.P.; Corriça, J.V.P.; Costa, A.P.A.; Costa, I.P.A.; Maêda, S.M.N.; Gomes, C.F.S.; Santos, M. Study of the Location of a Second Fleet for the Brazilian Navy: Structuring and Mathematical Modeling Using SAPEVO-M and VIKOR Methods. In Production Research. ICPR-Americas 2020. Communications in Computer and Information Science; Rossit, D.A., Tohmé, F., Mejía Delgadillo, G., Eds.; Springer: Cham, Switzerland, 2021; Volume 1408. [CrossRef]

16. Basilio, M.P.; Pereira, V.; Costa, H.G. Review of the Literature on Multicriteria Methods Applied in the Field of Public Security. Univers. J. Manag. 2017, 5, 549–562. [CrossRef]

17. Guitouni, A.; Martel, J.-M. Tentative guidelines to help choosing an appropriate MCDA method. Eur. J. Oper. Res. 1998, 109, 501–521. [CrossRef]

18. Zanakis, S.H.; Solomon, A.; Wishart, N.; Dublish, S. Multi-attribute decision making: A simulation comparison of select methods. Eur. J. Oper. Res. 1998, 107, 507–529. [CrossRef]

19. Gershon, M. The role of weights and scales in the application of multiobjective decision making. Eur. J. Oper. Res. 1984, 15, 244–250. [CrossRef]

20. W ˛atróbski, J.; Jankowski, J.; Ziemba, P.; Karczmarczyk, A.; Zioło, M. Generalised framework for multi-criteria method selection. Omega 2019, 86, 107–124. [CrossRef]

21. Cinelli, M.; Kadzi ´nski, M.; Gonzalez, M.; Słowi ´nski, R. How to support the application of multiple criteria decision analysis? Let us start with a comprehensive taxonomy. Omega 2020, 96, 102261. [CrossRef]

22. Fossile, D.K.; Frej, E.A.; da Costa, S.E.G.; de Lima, E.P.; de Almeida, A.T. Selecting the most viable renewable energy source for Brazilian ports using the FITradeoff method. J. Clean. Prod. 2020, 260, 121107. [CrossRef]

23. Siksnelyte-Butkiene, I.; Zavadskas, E.K.; Streimikiene, D. Multi-Criteria Decision-Making (MCDM) for the Assessment of Renewable Energy Technologies in a Household: A Review. Energies 2020, 13, 1164. [CrossRef]

24. Akhtar, N.; Ishak, M.; Ahmad, M.; Umar, K.; Yusuff, M.M.; Anees, M.; Qadir, A.; Almanasir, Y.A. Modification of the Water Quality Index (WQI) Process for Simple Calculation Using the Multi-Criteria Decision-Making (MCDM) Method: A Review. Water 2021.13 905 [CrossRef

25. Syan, C.S.; Ramsoobag, G. Maintenance applications of multi-criteria optimization: A review. Reliab. Eng. Syst. Saf. 2019, 190, 106520. [CrossRef]

26. Costa, I.P.A.; Basilio, M.P.; Maeda, S.M.N.; Rodrigues, M.V.G.; Moreira, M.A.L.; Gomes, C.F.S.; Santos, M. Bibliometric Studies on Multi-Criteria Decision Analysis (MCDA) Applied in Personnel Selection. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 119–125. [CrossRef]

27. Salih, M.; Zaidan, B.; Zaidan, A.; Ahmed, M. Survey on fuzzy TOPSIS state-of-the-art between 2007 and 2017. Comput. Oper. Res. 2019, 104, 207–227. [CrossRef]

28. Pelissari, R.; Oliveira, M.C.; Abackerli, A.J.; Ben-Amor, S.; Assumpção, M.R.P. Techniques to model uncertain input data of multi-criteria decision-making problems: A literature review. Int. Trans. Oper. Res. 2021, 28, 523–559. [CrossRef]

29. Moreno-Calderón, A.; Tong, T.S.; Thokala, P. Multi-criteria Decision Analysis Software in Healthcare Priority Setting: A Systematic Review. Pharmacoeconomics 2020, 38, 269–283. [CrossRef]

30. Heidari, M.D.; Gandasasmita, S.; Li, E.; Pelletier, N. Proposing a framework for sustainable feed formulation for laying hens: A systematic review of recent developments and future directions. J. Clean. Prod. 2021, 288, 125585. [CrossRef]

31. Cunha, V.H.C.; Caiado, R.G.G.; Corseuil, E.T.; Neves, H.F.; Bacoccoli, L. Automated compliance checking in the context of Industry 4.0: From a systematic review to an empirical fuzzy multi-criteria approach. Soft Comput. 2021, 25, 6055–6074. [CrossRef]

32. Serugga, J.; Kagioglou, M.; Tzortzopoulos, P. A Utilitarian Decision—Making Approach for Front End Design—A Systematic Literature Review. Buildings 2020, 10, 34. [CrossRef]

33. Aria, M.; Cuccurullo, C. bibliometrix: An R-tool for comprehensive science mapping analysis. J. Informetr. 2017, 11, 959–975. [CrossRef]

34. Rousseau, D.M. The Oxford Handbook of Evidence-Based Management; Oxford University Press: Oxford, UK; New York, NY, USA, 2012.

35. Dervi¸s, H. Bibliometric Analysis using Bibliometrix an R Package. J. Scientometr. Res. 2019, 8, 156–160. [CrossRef]

36. Wang, C.; Ghadimi, P.; Lim, M.K.; Tseng, M.-L. A literature review of sustainable consumption and production: A comparative analysis in developed and developing economies. J. Clean. Prod. 2019, 206, 741–754. [CrossRef]

37. Wang, C.; Lim, M.K.; Zhao, L.; Tseng, M.-L.; Chien, C.-F.; Lev, B. The evolution of Omega-The International Journal of Management Science over the past 40 years: A bibliometric overview. Omega 2020, 93, 102098. [CrossRef]

38. Ghadimi, P.; Wang, C.; Lim, M.K. Sustainable supply chain modeling and analysis: Past debate, present problems, and future challenges. Resour. Conserv. Recycl. 2019, 140, 72–84. [CrossRef]

39. Inamdar, Z.; Raut, R.; Narwane, V.S.; Gardas, B.; Narkhede, B.; Sagnak, M. A systematic literature review with bibliometric analysis of big data analytics adoption from period 2014 to 2018. J. Enterp. Inf. Manag. 2020, 34, 101–139. [CrossRef]

40. Merigó, J.M.; Yang, J.-B. A bibliometric analysis of operations research and management science. Omega 2017, 73, 37–48. [CrossRef]

41. Ratten, V.; Manesh, M.F.; Pellegrini, M.M.; Dabic, M. The Journal of Family Business Management: A bibliometric analysis. J. Fam. Bus. Manag. 2020, 11, 137–160. [CrossRef]

42. Borgatti, S.P.; Mehra, A.; Brass, D.J.; Labianca, G. Network analysis in the social sciences. Science 2009, 323, 892–895. [CrossRef]

43. Barabási, A.L.; Jeong, H.; Néda, Z.; Ravasz, E.; Schubert, A.; Vicsek, T. Evolution of the social net-work of scientific collaborations. Phys. A Stat. Mech. Its Appl. 2002, 311, 590–614. [CrossRef]

44. González-Alcaide, G.; Pinargote, H.; Ramos, J.M. From cut-points to key players in coauthorship networks: A case study in ventilator-associated pneumonia research. Scientometrics 2020, 123, 707–733. [CrossRef]

45. Yan, E.; Ding, Y. Scholarly network similarities: How bibliographic coupling networks, citation networks, co-citation networks, topical networks, coauthorship networks, and co-word networks relate to each other. J. Am. Soc. Inf. Sci. Technol. 2012, 63, 1313–1326. [CrossRef]

46. Hernández, J.M.; Dorta-González, P. Interdisciplinarity Metric Based on the Co-Citation Network. Mathematics 2020, 8, 544. [CrossRef]

47. Perianes-Rodriguez. A.: Waltman, L.: van Eck, N.J. Constructing bibliometric networks: A comparison between full and fractional counting. J. Informetr. 2016, 10, 1178–1195. [CrossRef]

48. Callon, M.; Courtial, J.-P.; Turner, W.A.; Bauin, S. From translations to problematic networks: An introduction to co-word analysis. Soc. Sci. Inf. 1983, 22, 191–235. [CrossRef]

49. Dai, S.; Duan, X.; Zhang, W. Knowledge map of environmental crisis management based on key-words network and co-word analysis, 2005–2018. J. Clean. Prod. 2020, 262, 121168. [CrossRef]

50. Cobo, M.J.; López-Herrera, A.G.; Herrera-Viedma, E.; Herrera, F. SciMAT: A new science mapping analysis software tool. J. Am. Soc. Inf. Sci. Technol. 2012, 63, 1609–1630. [CrossRef]

51. Cheng, B.; Wang, M.; Mørch, A.I.; Chen, N.S.; Spector, J.M. Research on e-learning in the workplace 2000–2012: A bibliometric analysis of the literature. Educ. Res. Rev. 2014, 11, 56–72. [CrossRef]

52. Leung, X.Y.; Sun, J.; Bai, B. Bibliometrics of social media research: A co-citation and co-word analysis. Int. J. Hosp. Manag. 2017, 66, 35–45. [CrossRef]

53. Ravikumar, S.; Agrahari, A.; Singh, S.N. Mapping the intellectual structure of scientometrics: A co-word analysis of the journal Scientometrics (2005–2010). Scientometrics 2015, 102, 929–955. [CrossRef]

54. De la Hoz-Correa, A.; Muñoz-Leiva, F.; Bakucz, M. Past themes and future trends in medical tour-ism research: A co-word analysis. Tour. Manag. 2018, 65, 200–211. [CrossRef]

55. Van Eck, N.J.; Waltman, L. CitNetExplorer: A new software tool for analyzing and visualizing citation networks. J. Informetr. 2014, 8, 802–823. [CrossRef]

56. Van Eck, N.J.; Waltman, L. Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics 2010, 84, 523–538. [CrossRef] [PubMed]

57. Persson, O.; Danell, R.; Schneider, J.W. How to use Bibexcel for various types of bibliometric analysis. In Celebrating Scholarly Communication Studies: A Festschrift for Olle Persson at His 60th Birthday; Astrom, F., Danell, R., Eds.; 2009; pp. 9–24. Available online: https://www.researchgate.net/publication/285473885\_How\_to\_use\_Bibexcel\_for\_various\_types\_of\_bibliometric\_analysis (ac cessed on 29 April 2022).

58. Sci2 Team. Science of Science (Sci2) Tool. Indiana University and SciTech Strategies. 2009. Available online: https://sci2.cns.iu.edu (accessed on 24 April 2022).

59. Chen, C. CiteSpace II: Detecting and visualizing emerging trends and transient patterns in scientific literature. J. Assoc. Inf. Sci. Technol. 2006, 57, 359–377. [CrossRef]

60. Basilio, M.P.; Pereira, V.; de Oliveira, M.W.C.M. Knowledge discovery in research on policing strategies: An overview of the past fifty years. J. Model. Manag. 2021. [CrossRef]

61. Ghosh, A.; Prasad, V.K.S. Off-grid Solar energy systems adoption or usage—A Bibliometric Study using the Bibliometrix R tool. Libr. Philos. Pract. 2021, 5673. Available online: https://digitalcommons.unl.edu/libphilprac/5673 (accessed on 24 April 2022).

62. van Laarhoven, P.; Pedrycz, W. A fuzzy extension of Saaty’s priority theory. Fuzzy Sets Syst. 1983, 11, 229–241. [CrossRef]

63. Brans, J.P.; Vincke, P.; Mareschal, B. How to select and how to rank projects: The Promethee method. Eur. J. Oper. Res. 1986, 24, 228–238. [CrossRef]

64. Chen, S.-M.; Tan, J.-M. Handling multicriteria fuzzy decision-making problems based on vague set theory. Fuzzy Sets Syst. 1994, 67, 163–172. [CrossRef]

65. Opricovic, S.; Tzeng, G.-H. Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. Eur. J. Oper. Res. 2004, 156, 445–455. [CrossRef]

66. Pohekar, S.D.; Ramachandran, M. Application of multi-criteria decision making to sustainable energy planning—A review. Renew. Sustain. Energy Rev. 2004, 8, 365–381. [CrossRef]

67. Wu, X.; Liao, H.; Xu, Z.; Hafezalkotob, A.; Herrera, F. Probabilistic Linguistic MULTIMOORA: A Multicriteria Decision Making Method Based on the Probabilistic Linguistic Expectation Function and the Improved Borda Rule. IEEE Trans. Fuzzy Syst. 2018, 26, 3688–3702. [CrossRef]

68. Yuan, Y.; Xu, Z.; Zhang, Y. The DEMATEL–COPRAS hybrid method under probabilistic linguistic environment and its application in Third Party Logistics provider selection. Fuzzy Optim. Decis. Mak. 2021, 21, 137–156. [CrossRef]

69. Wang, J.-Q.; Wu, J.-T.; Wang, J.; Zhang, H.-Y.; Chen, X.-H. Multi-criteria decision-making methods based on the Hausdorff distance of hesitant fuzzy linguistic numbers. Soft Comput. 2016, 20, 1621–1633. [CrossRef]

70. Liao, H.; Xu, Z.; Zeng, X.-J. Hesitant Fuzzy Linguistic VIKOR Method and Its Application in Qualitative Multiple Criteria Decision Making. IEEE Trans. Fuzzy Syst. 2014, 23, 1343–1355. [CrossRef]

71. Liu, X.; Ma, Y. A method to analyze the rank reversal problem in the ELECTRE II method. Omega 2021, 102, 102317. [CrossRef]

72. Nie, R.-X.; Tian, Z.-P.; Wang, J.-Q.; Zhang, H.-Y.; Wang, T.-L. Water security sustainability evaluation: Applying a multistage decision support framework in industrial region. J. Clean. Prod. 2018, 196, 1681–1704. [CrossRef]

73. Liang, X.; Chen, T.; Ye, M.; Lin, H.; Li, Z. A hybrid fuzzy BWM-VIKOR MCDM to evaluate the service level of bike-sharing companies: A case study from Chengdu, China. J. Clean. Prod. 2021, 298, 126759. [CrossRef]

74. Peng, J.-J.; Wang, J.-Q.; Zhang, H.-Y.; Chen, X.-H. An outranking approach for multi-criteria decision-making problems with simplified neutrosophic sets. Appl. Soft Comput. 2014, 25, 336–346. [CrossRef]

75. Wang, P.; Zhu, Z.; Wang, Y. A novel hybrid MCDM model combining the SAW, TOPSIS and GRA methods based on experimental design. Inf. Sci. 2016, 345, 27–45. [CrossRef]

76. Xu, Z.; Zhang, X. Hesitant fuzzy multi-attribute decision making based on TOPSIS with incomplete weight information. Knowl.- Based Syst. 2013, 52, 53–64. [CrossRef]

77. Luthra, S.; Govindan, K.; Kannan, D.; Mangla, S.K.; Garg, C.P. An integrated framework for sustainable supplier selection and evaluation in supply chains. J. Clean. Prod. 2017, 140, 1686–1698. [CrossRef]

78. Pati, R.K.; Vrat, P.; Kumar, P. A goal programming model for paper recycling system. Omega 2008, 36, 405–417. [CrossRef]

79. Jaiswal, P.; Singh, A.; Misra, S.C.; Kumar, A. Barriers in implementing lean manufacturing in Indian SMEs: A multi-criteria decision-making approach. J. Model. Manag. 2021, 16, 339–356. [CrossRef]

80. Kumar, A.; Sah, B.; Singh, A.R.; Deng, Y.; He, X.; Kumar, P.; Bansal, R.C. A review of multi criteria decision making (MCDM) towards sustainable renewable energy development. Renew. Sustain. Energy Rev. 2017, 69, 596–609. [CrossRef]

81. Choudhary, D.; Shankar, R. An STEEP-fuzzy AHP-TOPSIS framework for evaluation and selection of thermal power plant location: A case study from India. Energy 2012, 42, 510–521. [CrossRef]

82. Chatterjee, P.; Chakraborty, S. Material selection using preferential ranking methods. Mater. Des. 2012, 35, 384–393. [CrossRef]

83. Chakraborty, S.; Zavadskas, E.K. Applications of WASPAS Method in Manufacturing Decision Making. Informatica 2014, 25, 1–20. [CrossRef]

84. Vinodh, S.; Prasanna, M.; Prakash, N.H. Integrated Fuzzy AHP–TOPSIS for selecting the best plastic recycling method: A case study. Appl. Math. Model. 2014, 38, 4662–4672. [CrossRef]

85. Garg, H. Novel intuitionistic fuzzy decision making method based on an improved operation laws and its application. Eng. Appl. Artif. Intell. 2017, 60, 164–174. [CrossRef]

86. Chatterjee, K.; Kar, S. A multi-criteria decision making for renewable energy selection using Z-numbers in uncertain environment. Technol. Econ. Dev. Econ. 2018, 24, 739–764. [CrossRef]

87. Hatefi, M.A. BRAW: Block-wise Rating the Attribute Weights in MADM. Comput. Ind. Eng. 2021, 156, 107274. [CrossRef]

88. Shemshadi, A.; Shirazi, H.; Toreihi, M.; Tarokh, M. A fuzzy VIKOR method for supplier selection based on entropy measure for objective weighting. Expert Syst. Appl. 2011, 38, 12160–12167. [CrossRef]

89. Kadhim, M.H.; Mardukhi, F. A Novel IoT Application Recommendation System Using Metaheuristic Multi-Criteria Analysis. Comput. Syst. Sci. Eng. 2021, 37, 149–158. [CrossRef]

90. Govindan, K.; Khodaverdi, R.; Jafarian, A. A fuzzy multi criteria approach for measuring sustainability performance of a supplier based on triple bottom line approach. J. Clean. Prod. 2013, 47, 345–354. [CrossRef]

91. Rezaeisaray, M.; Ebrahimnejad, S.; Khalili-Damghani, K. A novel hybrid MCDM approach for outsourcing supplier selection. J. Model. Manag. 2016, 11, 536–559. [CrossRef]

92. Ghasemi, P.; Mehdiabadi, A.; Spulbar, C.; Birau, R. Ranking of Sustainable Medical Tourism Destinations in Iran: An Integrated Approach Using Fuzzy SWARA-PROMETHEE. Sustainability 2021, 13, 683. [CrossRef]

93. Jahanshahloo, G.; Lotfi, F.H.; Izadikhah, M. An algorithmic method to extend TOPSIS for decision-making problems with interval data. Appl. Math. Comput. 2006, 175, 1375–1384. [CrossRef]

94. Hashemi, S.H.; Karimi, A.; Tavana, M. An integrated green supplier selection approach with analytic network process and improved Grey relational analysis. Int. J. Prod. Econ. 2015, 159, 178–191. [CrossRef]

95. Behzadian, M.; Kazemzadeh, R.; Albadvi, A.; Aghdasi, M. PROMETHEE: A comprehensive literature review on methodologies and applications. Eur. J. Oper. Res. 2010, 200, 198–215. [CrossRef]

96. Hashemi, H.; Mousavi, S.M.; Zavadskas, E.K.; Chalekaee, A.; Turskis, Z. A New Group Decision Model Based on Grey Intuitionistic Fuzzy-ELECTRE and VIKOR for Contractor Assessment Problem. Sustainability 2018, 10, 1635. [CrossRef]

97. Boran, F.E.; Genç, S.; Kurt, M.; Akay, D. A multi-criteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method. Expert Syst. Appl. 2009, 36, 11363–11368. [CrossRef]

98. Özceylan, E.; Erba¸s, M.; Çetinkaya, C.; Kabak, M. Analysis of Potential High-Speed Rail Routes: A Case of GIS-Based Multicriteria Evaluation in Turkey. J. Urban Plan. Dev. 2021, 147, 04021012. [CrossRef]

99. Durak, I.; Arslan, H.M.; Özdemir, Y. Application of AHP–TOPSIS methods in technopark selection of technology companies: Turkish case. Technol. Anal. Strat. Manag. 2021, 1–15. [CrossRef]

100. Önüt, S.; Soner, S. Transshipment site selection using the AHP and TOPSIS approaches under fuzzy environment. Waste Manag. 2008, 28, 1552–1559. [CrossRef]

101. Kahraman, C.; Ruan, D.; Dogan, I. Fuzzy group decision-making for facility location selection.ˇ Inf. Sci. 2003, 157, 135–153. [CrossRef]

102. Kaya, T.; Kahraman, C. Multicriteria renewable energy planning using an integrated fuzzy VIKOR & AHP methodology: The case of Istanbul. Energy 2010, 35, 2517–2527. [CrossRef]

103. Gencer, C.; Gürpinar, D. Analytic network process in supplier selection: A case study in an electronic firm. Appl. Math. Model. 2007, 31, 2475–2486. [CrossRef]

104. Da ˘gdeviren, M.; Yavuz, S.; Kılınç, N. Weapon selection using the AHP and TOPSIS methods under fuzzy environment. Expert Syst. Appl. 2009, 36, 8143–8151. [CrossRef]

105. Büyüközkan, G.; Güleryüz, S. An integrated DEMATEL-ANP approach for renewable energy resources selection in Turkey. Int. J. Prod. Econ. 2016, 182, 435–448. [CrossRef]

106. Colak, E.H.; Memisoglu, T.; Gercek, Y. Optimal site selection for solar photovoltaic (PV) power plants using GIS and AHP: A case study of Malatya Province, Turkey. Renew. Energy 2020, 149, 565–576. [CrossRef]

107. Chen, C.-T. Extensions of the TOPSIS for group decision-making under fuzzy environment. Fuzzy Sets Syst. 2000, 114, 1–9. [CrossRef]

108. Lin, Y.-F. Construction of Consistent Comparison Matrix by Macharis’ Method Revisit. Math. Probl. Eng. 2021, 2021, 5585662. [CrossRef]

109. Chiu, W.-Y.; Manoharan, S.H.; Huang, T.-Y. Weight Induced Norm Approach to Group Decision Making for Multiobjective Optimization Problems in Systems Engineering. IEEE Syst. J. 2020, 14, 1580–1591. [CrossRef]

110. Opricovic, S.; Tzeng, G.-H. Extended VIKOR method in comparison with outranking methods. Eur. J. Oper. Res. 2007, 178, 514–529. [CrossRef]

111. Chen, T. Enhancing the efficiency and accuracy of existing FAHP decision-making methods. EURO J. Decis. Process. 2020, 8, 177–204. [CrossRef]

112. Yang, C.-C.; Shen, C.-C.; Lin, Y.-S.; Lo, H.-W.; Wu, J.-Z. Sustainable Sports Tourism Performance Assessment Using Grey-Based Hybrid Model. Sustainability 2021, 13, 4214. [CrossRef]

113. Tzeng, G.-H.; Chiang, C.-H.; Li, C.-W. Evaluating intertwined effects in e-learning programs: A novel hybrid MCDM model based on factor analysis and DEMATEL. Expert Syst. Appl. 2007, 32, 1028–1044. [CrossRef]

114. Chen, F.-H.; Hsu, T.-S.; Tzeng, G.-H. A balanced scorecard approach to establish a performance evaluation and relationship model for hot spring hotels based on a hybrid MCDM model combining DEMATEL and ANP. Int. J. Hosp. Manag. 2011, 30, 908–932. [CrossRef]

115. Liou, J.J.; Tamošaitiene, J.; Zavadskas, E.K.; Tzeng, G.-H. New hybrid COPRAS-G MADM Model for improving and selecting˙ suppliers in green supply chain management. Int. J. Prod. Res. 2015, 54, 114–134. [CrossRef]

116. Chen, T.-Y. Comparative analysis of SAW and TOPSIS based on interval-valued fuzzy sets: Discussions on score functions and weight constraints. Expert Syst. Appl. 2012, 39, 1848–1861. [CrossRef]

117. Hong, D.H.; Choi, C.-H. Multicriteria fuzzy decision-making problems based on vague set theory. Fuzzy Sets Syst. 2000, 114, 103–113. [CrossRef]

118. Dymova, L.; Kaczmarek, K.; Sevastjanov, P.; Sułkowski, Ł.; Przybyszewski, K. An Approach to Generalization of the Intuitionistic Fuzzy Topsis Method in the Framework of Evidence Theory. J. Artif. Intell. Soft Comput. Res. 2021, 11, 157–175. [CrossRef]

119. Mousavi, M.M.; Lin, J. The application of PROMETHEE multi-criteria decision aid in financial decision making: Case of distress prediction models evaluation. Expert Syst. Appl. 2020, 159, 113438. [CrossRef]

120. Tam, M.C.; Tummala, V. An application of the AHP in vendor selection of a telecommunications system. Omega 2001, 29, 171–182. [CrossRef]

121. Pires. A.: Chang. N.-B.: Martinho. G. An AHP-based fuzzy interval TOPSIS assessment for sustainable expansion of the solid waste management system in Setúbal Peninsula, Portugal. Resour. Conserv. Recycl. 2011, 56, 7–21. [CrossRef]

122. Rani, P.; Mishra, A.R.; Pardasani, K.R.; Mardani, A.; Liao, H.; Streimikiene, D. A novel VIKOR approach based on entropy and divergence measures of Pythagorean fuzzy sets to evaluate renewable energy technologies in India. J. Clean. Prod. 2019, 238.117936.[CrossRef]

123. Saaty, T.L. The Modern Science of Multicriteria Decision Making and Its Practical Applications: The AHP/ANP Approach. Oper. Res. 2013, 61, 1101–1118. [CrossRef]

124. Saaty, T.L.; Ergu, D. When is a Decision-Making Method Trustworthy? Criteria for Evaluating Multi-Criteria Decision-Making Methods. Int. J. Inf. Technol. Decis. Mak. 2015, 14, 1171–1187. [CrossRef]

125. Abdel-Basset, M.; Saleh, M.; Gamal, A.; Smarandache, F. An approach of TOPSIS technique for developing supplier selection with group decision making under type-2 neutrosophic number. Appl. Soft Comput. 2019, 77, 438–452. [CrossRef]

126. Tavana, M.; Li, Z.; Mobin, M.; Komaki, M.; Teymourian, E. Multi-objective control chart design optimization using NSGA-III and MOPSO enhanced with DEA and TOPSIS. Expert Syst. Appl. 2016, 50, 17–39. [CrossRef]

127. Gaviao, L.O.; Sant’Anna, A.P.; Lima, G.B.A.; Garcia, P.A.D.A.; Kostin, S.; Asrilhant, B. Selecting a Cargo Aircraft for Humanitarian and Disaster Relief Operations by Multicriteria Decision Aid Methods. IEEE Trans. Eng. Manag. 2020, 67, 631–640. [CrossRef]

128. Maêda, S.M.D.N.; Basílio, M.P.; Costa, I.P.D.A.; Moreira, M.L.; dos Santos, M.; Gomes, C.F.S.; de Almeida, I.D.P.; Costa, A.P.D.A. Investments in Times of Pandemics: An Approach by the SAPEVO-M-NC Method. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 162–168. [CrossRef]

129. Drumond, P.; Basílio, M.P.; Costa, I.P.D.A.; Pereira, D.A.D.M.; Gomes, C.F.S.; dos Santos, M. Multicriteria Analysis in Additive Manufacturing: An ELECTRE-MOr Based Approach. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 126–132. [CrossRef]

130. Costa, I.P.D.A.; Basílio, M.P.; Maêda, S.M.D.N.; Rodrigues, M.V.G.; Moreira, M.L.; Gomes, C.F.S.; dos Santos, M. Algorithm Selection for Machine Learning Classification: An Application of the MELCHIOR Multicriteria Method. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 154–161. [CrossRef]

131. Basilio, M.; Brum, G.S.; Pereira, V. A model of policing strategy choice: The integration of the Latent Dirichlet Allocation (LDA) method with ELECTRE I. J. Model. Manag. 2020, 15, 849–891. [CrossRef]

132. Maêda, S.M.D.N.; Basílio, M.P.; Costa, I.P.D.A.; Moreira, M.L.; dos Santos, M.; Gomes, C.F.S. The SAPEVO-M-NC Method. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 89–95. [CrossRef]

133. Krohling, R.A.; de Souza, T.T. Combining prospect theory and fuzzy numbers to multi-criteria decision making. Expert Syst. Appl. 2012, 39, 11487–11493. [CrossRef]

134. Silva, M.D.C.; Gavião, L.O.; Gomes, C.F.S.; Lima, G.B.A. Global Innovation Indicators analysed by multicriteria decision. Braz. J. Oper. Prod. Manag. 2020, 17, 1–17. [CrossRef]

135. Soares, L.d.M.B.; Moreira, M.L.; Basilio, M.P.; Gomes, C.F.S.; dos Santos, M.; Costa, I.P.D.A. Strategic Analysis for the Installation of Field Hospitals for COVID-19 Control: An Approach Based on P-Median Model. In Modern Management Based on Big Data II and Machine Learning and Intelligent Systems III—Proceedings of MMBD 2021 and MLIS 2021; Tallón-Ballesteros, A.J., Ed.; IOS Press: Amsterdam, The Netherlands, 2021; Volume 341, pp. 112–118. [CrossRef]

136. de Almeida, A.T. Multicriteria decision model for outsourcing contracts selection based on utility function and ELECTRE method. Comput. Oper. Res. 2007, 34, 3569–3574. [CrossRef]

137. Morais, D.C.; de Almeida, A.T. Group decision making on water resources based on analysis of individual rankings. Omega 2012, 40, 42–52. [CrossRef]

138. Barata, J.F.F.; Quelhas, O.L.G.; Costa, H.G.; Gutierrez, R.H.; Lameira, V.D.J.; Meiriño, M.J. Multi-Criteria Indicator for Sustainability Rating in Suppliers of the Oil and Gas Industries in Brazil. Sustainability 2014, 6, 1107–1128. [CrossRef]

139. Pereira, V.; Costa, H.G. Nonlinear programming applied to the reduction of inconsistency in the AHP method. Ann. Oper. Res. 2015, 229, 635–655. [CrossRef]

140. Basilio, M.; De Freitas, J.G.; Kämpffe, M.G.F.; Rego, R. Investment portfolio formation via multicriteria decision aid: A Brazilian stock market study. J. Model. Manag. 2018, 13, 394–417. [CrossRef]

141. Liu, H.; Rodríguez, R.M. A fuzzy envelope for hesitant fuzzy linguistic term set and its application to multicriteria decision making. Inf. Sci. 2014, 258, 220–238. [CrossRef]

142. Jato-Espino, D.; Castillo-Lopez, E.; Rodriguez-Hernandez, J.; Canteras-Jordana, J.C. A review of application of multi-criteria decision making methods in construction. Autom. Constr. 2014, 45, 151–162. [CrossRef]

143. Cárdenas-Gómez, J.; Gonzales, M.B.; Lazo, C.D. Evaluation of Reinforced Adobe Techniques for Sustainable Reconstruction in Andean Seismic Zones. Sustainability 2021, 13, 4955. [CrossRef]

144. Casas-Rosal, J.C.; Segura, M.; Maroto, C. Food market segmentation based on consumer preferences using outranking multicriteria approaches. Int. Trans. Oper. Res. 2021. [CrossRef]

145. Luna, M.; Llorente, I.; Cobo, A. A fuzzy approach to decision-making in sea-cage aquaculture production. Int. Trans. Oper. Res. 2020, 29, 1025–1047. [CrossRef]

146. Romero, C. Extended lexicographic goal programming: A unifying approach. Omega 2001, 29, 63–71. [CrossRef]

147. Sánchez-Lozano, J.; García-Cascales, M.; Lamata, M. GIS-based onshore wind farm site selection using Fuzzy Multi-Criteria Decision Making methods. Evaluating the case of Southeastern Spain. Appl. Energy 2016, 171, 86–102. [CrossRef]

148. Bilbao-Terol, A.; Arenas-Parra, M.; Cañal-Fernández, V.; Antomil-Ibias, J. Using TOPSIS for assessing the sustainability of government bond funds. Omega 2014, 49, 1–17. [CrossRef]

149. Bana e Costa, C.A.; Carnero, M.C.; Oliveira, M.D. A multi-criteria model for auditing a Predictive Maintenance Programme. Eur. J. Oper. Res. 2012, 217, 381–393. [CrossRef]

150. Braglia, M.; Frosolini, M.; Montanari, R. Fuzzy TOPSIS approach for failure mode, effects and criticality analysis. Qual. Reliab. Eng. Int. 2003, 19, 425–443. [CrossRef]

151. La Fata, C.; Giallanza, A.; Micale, R.; La Scalia, G. Ranking of occupational health and safety risks by a multi-criteria perspective: Inclusion of human factors and application of VIKOR. Saf. Sci. 2021, 138, 105234. [CrossRef]

152. Bottero, M.; Comino, E.; Riggio, V. Application of the Analytic Hierarchy Process and the Analytic Network Process for the assessment of different wastewater treatment systems. Environ. Model. Softw. 2011, 26, 1211–1224. [CrossRef]

153. Zoghi, M.; Rostami, G.; Khoshand, A.; Motalleb, F. Material selection in design for deconstruction using Kano model, fuzzy-AHP and TOPSIS methodology. Waste Manag. Res. J. Sustain. Circ. Econ. 2021, 40, 410–419. [CrossRef] [PubMed]

154. Corrente, S.; Greco, S.; Leonardi, F.; Słowi ´nski, R. The hierarchical SMAA-PROMETHEE method applied to assess the sustainability of European cities. Appl. Intell. 2021, 51, 6430–6448. [CrossRef]

155. Beccali, M.; Cellura, M.; Mistretta, M. Decision-making in energy planning. Application of the Electre method at regional level for the diffusion of renewable energy technology. Renew. Energy 2003, 28, 2063–2087. [CrossRef]

156. Formisano, A.; Mazzolani, F.M. On the selection by MCDM methods of the optimal system for seismic retrofitting and vertical addition of existing buildings. Comput. Struct. 2015, 159, 1–13. [CrossRef]

157. Norese, M.F. ELECTRE III as a support for participatory decision-making on the localisation of waste-treatment plants. Land Use Policy 2006, 23, 76–85. [CrossRef]

158. Barrios, M.A.O.; De Felice, F.; Negrete, K.P.; Romero, B.A.; Arenas, A.Y.; Petrillo, A. An AHP-Topsis Integrated Model for Selecting the Most Appropriate Tomography Equipment. Int. J. Inf. Technol. Decis. Mak. 2016, 15, 861–885. [CrossRef]

159. Cavallaro, F. Fuzzy TOPSIS approach for assessing thermal-energy storage in concentrated solar power (CSP) systems. Appl. Energy 2010, 87, 496–503. [CrossRef]

160. Azadnia, A.H.; Saman, M.Z.M.; Wong, K.Y. Sustainable supplier selection and order lot-sizing: An integrated multi-objective decision-making process. Int. J. Prod. Res. 2015, 53, 383–408. [CrossRef]

161. Umer, R.; Touqeer, M.; Omar, A.H.; Ahmadian, A.; Salahshour, S.; Ferrara, M. Selection of solar tracking system using extended TOPSIS technique with interval type-2 pythagorean fuzzy numbers. Optim. Eng. 2021, 22, 2205–2231. [CrossRef]

162. Mardani, A.; Jusoh, A.; MD Nor, K.; Khalifah, Z.; Zakwan, N.; Valipour, A. Multiple criteria decision-making techniques and their applications—A review of the literature from 2000 to 2014. Econ. Res.-Ekon. Istraž. 2015, 28, 516–571. [CrossRef]

163. Khoso, A.R.; Yusof, A.M.; Khahro, S.H.; Abidin, N.I.A.B.; Memon, N.A. Automated two-stage continuous decision support model using exploratory factor analysis-MACBETH-SMART: An application of contractor selection in public sector construction. J. Ambient Intell. Humaniz. Comput. 2021, 1–31. [CrossRef]

164. Rostamzadeh, R.; Govindan, K.; Esmaeili, A.; Sabaghi, M. Application of fuzzy VIKOR for evaluation of green supply chain management practices. Ecol. Indic. 2015, 49, 188–203. [CrossRef]

165. Abdullah, L.; Najib, L. A new type-2 fuzzy set of linguistic variables for the fuzzy analytic hierarchy process. Expert Syst. Appl. 2014, 41, 3297–3305. [CrossRef]

166. Mardani, A.; Jusoh, A.; Zavadskas, E.K. Fuzzy multiple criteria decision-making techniques and applications—Two decades review from 1994 to 2014. Expert Syst. Appl. 2015, 42, 4126–4148. [CrossRef]

167. Zaidan, A.; Zaidan, B.; Al-Haiqi, A.; Kiah, M.; Hussain, M.; Abdulnabi, M. Evaluation and selection of open-source EMR software packages based on integrated AHP and TOPSIS. J. Biomed. Inform. 2015, 53, 390–404. [CrossRef] [PubMed]

168. Mir, M.A.; Ghazvinei, P.T.; Sulaiman, N.M.N.; Basri, N.E.A.; Saheri, S.; Mahmood, N.Z.; Jahan, A.; Begum, R.A.; Aghamohammadi, N. Application of TOPSIS and VIKOR improved versions in a multi-criteria decision analysis to develop an optimized municipal solid waste management model. J. Environ. Manag. 2016, 166, 109–115. [CrossRef]

169. Adiat, K.A.N.; Nawawi, M.N.M.; Abdullah, K. Assessing the accuracy of GIS-based elementary multi-criteria decision analysis as a spatial prediction tool—A case of predicting potential zones of sustainable groundwater resources. J. Hydrol. 2012, 440–441, 75–89. [CrossRef]

170. Cobo, M.J.; López-Herrera, A.G.; Herrera-Viedma, E.; Herrera, F. An approach for detecting, quantifying, and visualizing the evolution of a research field: A practical application to the Fuzzy Sets Theory field. J. Informetr. 2011, 5, 146–166. [CrossRef]