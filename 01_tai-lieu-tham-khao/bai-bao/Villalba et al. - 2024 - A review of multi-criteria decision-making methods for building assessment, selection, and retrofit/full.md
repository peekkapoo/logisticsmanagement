# A REVIEW OF MULTI-CRITERIA DECISION-MAKING METHODS FOR BUILDING ASSESSMENT, SELECTION, AND RETROFIT

Paola VILLALBA <sup>1, 2 </sup> , Antonio J. SÁNCHEZ-GARRIDO <sup>3</sup>, Víctor YEPES <sup>1</sup>

<sup>1</sup>ICITECH, Department of Construction Engineering, Universitat Politècnica de València, Valencia 46022, Spain

<sup>2</sup> Faculty of Engineering and Applied Sciences, Civil Engineering Degree Programme,

Universidad Central del Ecuador, Quito, Ecuador

<sup>3</sup>Department of Construction Engineering, Universitat Politècnica de València, 46022 Valencia, Spain

Article History: ■ received 6 March 2023 ■ accepted 17 March 2024

Abstract. Multiple criteria decision-making (MCDM) has experienced significant growth in recent years, owing to its capacity to integrate even contradictory criteria. This study conducted a comprehensive literature review of MCDM for assessing, selecting, and retrofitting buildings. The bibliometric search used a search algorithm in specialized databases. A filtering and expansion process was done by reviewing references, and 91 relevant articles were selected. The analysis revealed that in a group of studies, socioeconomic criteria were used to assess the vulnerability of buildings. On the other hand, some research integrated the three dimensions of sustainability (economic, social, and environmental) along with safety considerations when identifying optimal retrofit alternatives. Classic MCDMs are prevalent in research within this field. Among the most used methods, the Analytic Hierarchy Process (AHP) was employed for criteria weighting, Simple Additive Weighting (SAW) for constructing vulnerability indices, and Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for building retrofitting. This literature review contributes to the path toward a holistic renovation of the existing building stock, providing recommendations for future research to improve decision-making solutions for integrating the safety and sustainability of existing buildings.

Keywords: decision making, MCDM, multi-criteria, retrofit, structural assessment, sustainability, vulnerability

Corresponding author. E-mail: pxvillalba@uce.edu.ec

## 1. Introduction

The aging of the existing building stock implies that a considerable percentage has been built with obsolete building codes and seismic standards (Palermo et al., 2018). This poses a tremendous social risk; the vulnerability of existing buildings to recent earthquakes caused structural damage, significant economic losses, severe injuries, and loss of human life (Pohoryles et al., 2022). Moreover, as they approach the end of their expected service life, risks related to the durability of materials appear that may decrease the structural capacity of the elements; the economic impact of aging and deterioration processes of structures and infrastructures is exceptionally high (Biondini & Frangopol, 2016). Informal self-managed housing construction carried out by residents or builders without formal construction training and often without permits or building code enforcement accounts for a high percentage of residential construction in low- and middle-income countries (Murray et al., 2023). In extreme conditions, these buildings will be more vulnerable.

The Sustainable Development Goals (SDGs) set out in the 2030 Agenda by the United Nations establish a need for urgent change: the construction sector is responsible for the most significant environmental impacts in terms of energy consumption, waste production, and depletion of raw materials. Sustainable designs and solutions seek to maximize benefits, reducing the negative impacts over time of the three pillars of sustainability: economy, society, and environment (Navarro et al., 2020b). Addressing structural deficiencies in the existing building stock, given the magnitude of the problem, through reconstruction is not a viable option; preference should be given to extending service life through maintenance, repair, and renovation work (Pohoryles et al., 2022). The vulnerability of buildings under extreme conditions is a complex nexus between social, economic, geological, systematic, and physical dimensions (Alam & Haque, 2022). The transition to a more sustainable society envisioned by current policies requires a comprehensive renovation of existing buildings from various perspectives, such as structural safety, energy eficiency, comfort, and architecture (Passoni et al., 2022).

In the field of structural safety and sustainability of existing buildings, authors Menna et al. (2022) analyze the state of the art of sustainable retrofitting, finding a group of research that achieves a combined evaluation of energy consumption and seismic vulnerability, concluding the need for multi-objective evaluations to demonstrate sustainability in both the short and long term. On the other hand, Pohoryles et al. (2022) conducted a state-ofthe-art review of integrated seismic and energy retrofitting and concluded that addressing seismic and energy performance through separate interventions is the standard approach currently adopted. An integrated approach to building retrofit is an emerging topic in the scientific literature. The arguments are suficient to seek methodologies for assessing, selecting, and retrofitting vulnerable buildings that minimize economic, social, and environmental impacts, complying with structural safety standards.

In civil engineering, decision-making may need to consider multiple dimensions and evaluation criteria, some of which may be contradictory. In addition to an exhaustive evaluation of each dimension, decision-making is required from a holistic perspective. Multi-criteria decision-making (MCDM) methods ofer a valuable approach in this regard. MCDMs have evolved as a comprehensive operations research method, integrating computational and mathematical tools to identify suitable solutions (Zavadskas et al., 2016). They facilitate the efective and eficient selection of the best alternatives, ranked according to preferences (Nadkarni & Puthuvayi, 2020), and help in decision-making between competitive alternatives, considering the multidimensional nature of real-world scenarios (Sierra et al., 2018). MCDMs enable the identification of compromise solutions in civil engineering, construction, building technology, and sustainability engineering (Zavadskas et al., 2021). Given the inherent complexity that characterizes the inclusion and integration of the often-contradictory criteria that define safety and sustainability, MCDMs have become a relevant tool that has gained importance in recent years. They allow the conflicting dimensions of sustainability to be evaluated in a multi-stakeholder and long-term context (Navarro et al., 2019).

Notable studies have explored the applications of MCDM in various civil engineering contexts in recent years. Zavadskas et al. (2018), Wen et al. (2021) and Zhu et al. (2021) studied decision-making applications in civil engineering and construction; Navarro et al. (2020b) in bridges; Sierra et al. (2018), Navarro et al. (2019) and Selvan et al. (2023) in sustainable construction, and Nadkarni and Puthuvayi (2020) and Marcher et al. (2020) in buildings. These studies demonstrate that MCDM applications have great potential for decision-making in civil engineering, construction, building technology, and sustainability. However, current trends in MCDM applications in assessing, selecting, and retrofitting vulnerable buildings require a detailed review.

The structural safety and sustainability of existing buildings is a field of knowledge that continues to evolve. However, the safety, economic, social, and environmental parameters used and the degree to which the scientific community has managed to integrate them have not yet been explored. This article provides an updated, detailed review of the use of MCDM for building assessment, selection, and retrofitting to address the previously identified knowledge gap. The main research question of this study is to assess the current trend in the use of MCDMs in integrating the three dimensions of sustainability with structural safety. Two secondary questions have also been posed: to analyze the most used MCDM methods and the relevant criteria considered. This work aims to assess current trends and look for research gaps and possible future directions in assessing, selecting, and retrofitting sustainable and safe buildings.

## 2. Materials and methods

This study used a combined review method that consisted of three stages: bibliometric search, quantitative analysis, and qualitative analysis. This methodology was chosen to efectively capture current trends within the scope of the study, identify research gaps, and outline future research directions. The bibliometric search involves a detailed search algorithm supplemented by a manual review of references and article citations. This process allowed obtaining relevant manuscripts in the study area. The global analysis of the results served as a quantitative criterion, while the qualitative criterion focused on addressing the research questions by examining socioeconomic and environmental considerations, analyzing the MCDM used, and evaluating the integration of structural safety with the three sustainability pillars, as illustrated in Figure 1.

The bibliometric search of this study consisted of three stages: search, filtering, and selection, as shown in Figure 1. The specialized databases Web of Science and SCO-PUS were used in the first stage. A search algorithm was used with three diferentiated terms connected by Boolean operators: research objective, methodology, and type of structure. For the term research objective, keywords defining assessment and retrofitting were used: “retrofit”, “retrofitting”, “reconditioning”, “vulnerability assessment”, “seismic vulnerability”, “seismic evaluation”, and “seismic assessment”. On the other hand, terms related to multicriteria decision-making were used for the methodology, including specific MCDM methods: “Multicriteria decision making”, “multi-criteria decision-making”, “multi-attribute decision making”, “MCDM”, “MADM”, “AHP”, “ANP”, “MAC-BETH”, “TOPSIS”, “VIKOR”, “Simple Additive Weighting”, “COPRAS”, “PROMETHEE”, “ELECTRE”, “MAUT”, “MAVT”, “MIVES”, “DEMATEL”, “CRITIC”, “WASPAS”, “ARAS”, “CBA”, and “SWARA”. The structure type was limited to “building” in the search algorithm’s third term.

In the filtering stage, the search was limited to articles published since 2008 and written in English. In the last stage, the titles and abstract were reviewed, and the articles directly related to the scope of this research were selected. Finally, the references and citations of the most relevant articles were manually reviewed to address any possible limitations of the search algorithms in an expansion process, using the filtering criteria from the second stage, resulting in a final selection of 91 articles.

![](images/0a9d3d64ed0848bab525e1250f24370163f4162ff592c4ea9d20c57b050f4b1b.jpg)  
Figure 1. Research steps of the literature review

## 3. Results

## 3.1. Overall analysis of results

The influence of journals and the co-occurrence of research author keywords were analyzed to highlight the areas explored in the articles based on text mining. Table 1 shows an analysis of the top 10 journals relevant to research. This analysis includes information on the number of articles published, total link strength, and citations. It is important to note that the importance of a journal cannot be determined solely by its volume of publications. The average normalized citation highlights journals with the highest average influence per year, indicating their continued impact and relevance to the research field being examined. According to the analysis, Engineering Structures, Structures, Buildings, and Applied Sciences are the highestranked journals concerning average normalized citations.

Table 2 provides information from the co-occurrence analysis of the keywords used in the articles. Link strength represents the connections between a specific keyword and the other keywords in the data set. Analyzing the groups formed makes it possible to determine the various areas the scientific community explores. In Group C1, the keywords “uncertainty”, “cultural heritage” and “reinforced concrete” stand out. Group C2 includes “risk”, and “seismic risk”, while group C3 “AHP” and “index”. Lastly, Cluster C4 comprises “GIS” and “earthquake”. The co-occurrence analysis generally determined the areas investigated by the scientific community: the safety of buildings, the importance of built cultural heritage, the management of uncertainty for decision-makers, and the utilization of suitable MCDM methods to assess, select, and retrofit buildings.

In the exhaustive review of the selected papers, some researchers focused on selecting vulnerable structures and retrofit strategies for school buildings (18 papers) and historic and heritage buildings (11 papers). Fiore et al. (2020a)

Table 1. Analysis of relevant sources

<table><tr><td>Journal</td><td>Total Link</td><td>Documents</td><td>Citations</td><td>Avg. Citations</td><td>Norm. Citations</td><td>Avg. Norm. Citations</td></tr><tr><td>Natural Hazards and Earth System Sciences</td><td>27</td><td>5</td><td>231</td><td>46.20</td><td>14.44</td><td>0.06</td></tr><tr><td>Sustainability</td><td>26</td><td>9</td><td>106</td><td>11.78</td><td>13.25</td><td>0.13</td></tr><tr><td>International Journal of Disaster Risk Reduction</td><td>25</td><td>6</td><td>253</td><td>42.17</td><td>36.14</td><td>0.14</td></tr><tr><td>Natural Hazards</td><td>10</td><td>2</td><td>119</td><td>59.50</td><td>9.15</td><td>0.08</td></tr><tr><td>Applied Sciences</td><td>9</td><td>4</td><td>64</td><td>16.00</td><td>10.67</td><td>0.17</td></tr><tr><td>Journal of Building Engineering</td><td>9</td><td>2</td><td>46</td><td>23.00</td><td>6.57</td><td>0.14</td></tr><tr><td>Structure and Infrastructure Engineering</td><td>9</td><td>3</td><td>80</td><td>26.67</td><td>11.43</td><td>0.14</td></tr><tr><td>Buildings</td><td>8</td><td>4</td><td>17</td><td>4.25</td><td>3.4</td><td>0.20</td></tr><tr><td>Engineering Structures</td><td>8</td><td>3</td><td>53</td><td>17.67</td><td>10.6</td><td>0.20</td></tr><tr><td>Structures</td><td>7</td><td>2</td><td>19</td><td>9.50</td><td>3.8</td><td>0.20</td></tr></table>

Table 2. Summary of the most studied keywords

<table><tr><td>Cluster</td><td>Keyword</td><td>Occurrences</td><td>Link strength</td><td>Cluster</td><td>Keyword</td><td>Occurrences</td><td>Link strength</td></tr><tr><td rowspan="7">C1</td><td>multi-criteria decision-making</td><td>9</td><td>11</td><td rowspan="2">C2</td><td>seismic risk</td><td>4</td><td>6</td></tr><tr><td>seismic retrofit</td><td>9</td><td>10</td><td>multi-criteria decision-analysis</td><td>3</td><td>3</td></tr><tr><td>vulnerability</td><td>6</td><td>10</td><td rowspan="5">C3</td><td>AHP</td><td>15</td><td>17</td></tr><tr><td>reinforced concrete</td><td>3</td><td>5</td><td>risk assessment</td><td>5</td><td>7</td></tr><tr><td>uncertainty</td><td>4</td><td>3</td><td>seismic vulnerability</td><td>4</td><td>7</td></tr><tr><td>cultural heritage</td><td>3</td><td>3</td><td>buildings</td><td>3</td><td>4</td></tr><tr><td>seismic vulnerability assessment</td><td>3</td><td>3</td><td>index</td><td>3</td><td>3</td></tr><tr><td rowspan="3">C2</td><td>retrofit</td><td>8</td><td>15</td><td rowspan="3">C4</td><td>GIS</td><td>14</td><td>24</td></tr><tr><td>decision-making</td><td>5</td><td>8</td><td>earthquake</td><td>8</td><td>15</td></tr><tr><td>risk</td><td>3</td><td>7</td><td>vulnerability assessment</td><td>5</td><td>7</td></tr></table>

point out that more than 60% of school buildings in Italy built in the late 1960s and 1970s need to meet modern technical standards for seismic prevention; these structures present a significant lack of energy eficiency and interior comfort. On the other hand, D’Alpaos and Valluzzi (2020) stress the importance of safeguarding heritage buildings; restoration and conservation decisions must consider the tangible and intangible values of both the building and the art assets. Figure 2 shows the number of annual publications by type of structure analyzed. Although Caterino et al. (2008) were among the first researchers to adopt MCDM methods in this field, research started to have a more prominent representation from 2017 onwards. Notably, 82% of the analyzed papers were published since 2017, indicating a renewed scientific interest in this field. The investigations are carried out mainly with the application of case studies, using information on the vulnerability of buildings in specific areas, with 58 articles on assessing and selecting buildings and 21 investigations on the retrofit of structures.

Figure 3 shows the countries with publications higher than three, highlighting the leading position of Italy, with 29 papers. More than 30% of reinforced concrete structures need to be improved to withstand seismic loads according to current regulations (Formisano et al., 2017). On the other hand, the “Stability Law of 2017” (Caterino & Cosenza, 2018a) introduced tax incentives for owners who invest in structural safety improvements, including earthquake resistance, allowing them to recover up to 85% of the total rehabilitation costs. This policy has resulted in a significant increase in relevant scientific publications from Italy. Another country of note is Iran, with 17 articles. According to Nazmfar (2019), factors responsible for increased earthquake losses in this country include increased population density, lack of alarm systems, inadequate monitoring of building standards, unplanned urbanization, and construction near incompatible users.

The regional vulnerability assessment framework is essential for governments and decision-makers to allocate resources optimally (Alam et al., 2012). Vulnerability assessments facilitate policymakers, planners, and administrators to adopt policies and actions to reduce the impact of risks and natural disasters (Jamal-ud-din et al., 2023). MCDM methods provide rapid identification of vulnerable structures requiring further analysis and prioritization of buildings to be retrofitted since upgrading all vulnerable buildings is not economically feasible (Shahriar et al., 2012). A group of researchers focuses on determining high vulnerability in urban areas (41 papers). Geographic Information Systems (GIS) facilitates vulnerability studies and natural hazards analysis as a valuable tool for managing, controlling, processing, and analyzing spatial data (Rezaie & Panahi, 2015). The combination of GIS and MCDM was used in 35 articles.

![](images/f368efae4eb287b703bd8052a0ed78a90db7c18e81e0cb90b6c2cca7bfc4ad5c.jpg)  
Figure 2. Distribution of contributions per year and structure type

![](images/3120dc93e218070b94a9ab0d5f405ba922fc6e7998a68bcf6b283ed80f653dd2.jpg)  
Figure 3. Distribution of contributions by country

Although a large number of articles study the seismic vulnerability of buildings, a group of researchers evaluates other risks such as tsunami (Dall’Osso et al., 2009; Papathoma-Koehle et al., 2019), floods (Abdrabo et al., 2023; Gacu et al., 2023; Gandini et al., 2020; Usman Kaoje et al., 2021; Mourato et al., 2023; Zhen et al., 2022), and multi-risk: seismic impacts, floods and extreme sea waves (Mladineo et al., 2022). In addition to building assessment, Panahi et al. (2014), Gentile et al. (2019), Alam and Haque (2020), Vona et al. (2017), Anelli et al. (2019), Sangiorgio et al. (2018a, 2018b, 2020b) propose strategies to prioritize retrofit vulnerable school buildings, while Pinero et al. (2017), Uva et al. (2019), D’Alpaos and Valluzzi (2020), Sangiorgio et al. (2020a, 2021), Makoond et al. (2021), and Lallam et al. (2023) prioritize intervention in historic and heritage buildings. On the other hand, J. Choi and J. Choi (2022) propose a technical feasibility study model for renovating aging apartments.

In building retrofitting, three main strategies are identified: retrofitting individual components, adding lateral load-resisting elements, and reducing structural demands through supplementary devices (Clemett et al., 2022). The retrofit techniques applied to a building can vary depending on the type of material, structural stresses, and functionality. The reviewed papers included the incorporation of fibers, concrete, and steel jacketing, the addition of walls, the installation of bracing, the application of base insulation, and the use of dissipators as the most commonly used methods. Among the papers reviewed, 18 researchers focused on selecting the most appropriate retrofit strategy for buildings, ten on school buildings, three on historic buildings, and one on the retrofit of historic adobe constructions.

## 3.2. Socio-economic and environmental considerations

Table 3 contains the most used indicators in evaluating and selecting vulnerable buildings. The height and age of buildings, materials, and construction quality are the indicators most used by researchers to evaluate safety. When prioritizing vulnerable buildings, researchers recognize the need to include social and economic criteria. The social and economic situation of society can afect the vulnerability of buildings (Aliabadi et al., 2015). There has yet to be a consensus among articles about defining the social and economic criteria. The spatial distribution of buildings, which determines the physical distance from roads and the ease of access to emergency services such as hospitals and fire departments, is often called systematic vulnerability and is a crucial consideration for many researchers (Alam & Haque, 2022). At the same time, population density is another important parameter that is considered when assessing the vulnerability of buildings in an emergency. In addition, social factors such as the vulnerability of specific populations based on their age and gender are relevant (Bahadori et al., 2017). Although uneducated populations do not necessarily increase vulnerability, a higher level of education can help increase awareness of hazards and improve emergency response. Therefore, it is considered one of the social factors used (Alizadeh et al., 2018a). The socioeconomic status of a community also has a significant impact on vulnerability. Researchers have examined empirical economic losses based on the estimated value of socioeconomic considerations of each building (Banica et al., 2017) and economic strength (Chu et al., 2021), also considering the employment situation of the population. Other social indicators taken into account by researchers include the identification of heritage or community buildings (Hoang et al., 2021), the evaluation of school buildings based on criteria such as historical and cultural importance, socioeconomic status, and community organization (Anelli et al., 2019), the valuation of artistic assets of historic churches (Sangiorgio et al., 2021), and the capacity to respond through the possibility of using physical, financial and human resources to control and reduce impacts (Mili et al., 2018).

Table 4 contains the indicators most used by researchers in building retrofit. The literature considers cost minimization as a fundamental parameter when selecting retrofit strategies. Costs can be classified into tangible and intangible costs. Tangible costs cover the direct costs of the repair; construction and installation phase costs are the most commonly used by the reviewed publications and include the costs of materials, labor, and equipment. Maintenance costs are also included to ensure the repair’s functionality throughout the building’s life. As a tangible cost, tax incentives from the Italian government are taken into account in the research (Andreolli et al., 2022; Caterino & Cosenza, 2018b; Caterino et al., 2021; Santarsiero et al., 2021). These tax incentives are granted if the remodeled structure improves at least one seismic class concerning the original building, which allows the exact amount of the tax deduction to be calculated; the owner is entitled to up to 85% of the total repair costs. On the other hand, the most used intangible costs are those related to the duration of the works, which are associated with the losses incurred as a consequence of the temporary interruption of the economic activities of a building.

Functionality and architectural compatibility are crucial factors when determining the most appropriate retrofit strategy; the aim is to minimize the impact on the everyday activities of the building users while preserving the original aesthetics of the structure; this consideration is widely shared among researchers. The reversibility criterion, that is, allowing the easy elimination of any reinforcement in the case of future interventions, is considered by Juliá et al. (2024), Fiore et al. (2020b), Formisano and Mazzolani (2015), Formisano et al. (2017), Macieira et al. (2022), while Tartaglia et al. (2022) consider the ease of implementation. As an anti-corruption measure, Anelli et al. (2020), Santa-Cruz et al. (2021), and Vázquez-Rowe et al. (2021) use criteria such as modularity, standardization, and industrialization in the search for a strategy to retrofit school buildings on a large scale.

In the detailed review of the articles, 17 investigations considered environmental criteria to determine the best retrofit strategy. Of these, six investigations were related to building retrofits, eight focused on school buildings, and three on historic buildings. The authors Anwar et al.

Table 3. Indicators in the assessment and selection of vulnerable buildings

<table><tr><td>Criteria category</td><td>Indicator</td><td>Assessment</td><td>Documents</td></tr><tr><td rowspan="9">Safety</td><td>Peak ground acceleration value (PGA)</td><td>Quantitative</td><td>14</td></tr><tr><td>Distance to faults</td><td>Quantitative</td><td>17</td></tr><tr><td>Slope</td><td>Quantitative</td><td>17</td></tr><tr><td>Age of buildings</td><td>Qualitative</td><td>31</td></tr><tr><td>Type of buildings</td><td>Qualitative</td><td>17</td></tr><tr><td>Building materials</td><td>Qualitative</td><td>36</td></tr><tr><td>Building height</td><td>Quantitative</td><td>35</td></tr><tr><td>Quality of construction</td><td>Qualitative</td><td>29</td></tr><tr><td>Density of buildings</td><td>Quantitative</td><td>23</td></tr><tr><td rowspan="6">Socio-economic</td><td>Population density</td><td>Quantitative</td><td>24</td></tr><tr><td>Age and gender</td><td>Quantitative</td><td>14</td></tr><tr><td>Level of education</td><td>Qualitative</td><td>12</td></tr><tr><td>Physical distance to emergency facilities</td><td>Quantitative</td><td>24</td></tr><tr><td>Labor situation</td><td>Quantitative</td><td>10</td></tr><tr><td>Economic considerations</td><td>Quantitative</td><td>11</td></tr></table>

Table 4. Indicators in building retrofit

<table><tr><td>Criteria category</td><td>Indicator</td><td>Assessment</td><td>Documents</td></tr><tr><td rowspan="3">Safety/Technical</td><td>Structural performance</td><td>Quantitative</td><td>27</td></tr><tr><td>Intervention in foundations</td><td>Quantitative</td><td>12</td></tr><tr><td>Ease of installation/reversibility</td><td>Qualitative</td><td>13</td></tr><tr><td rowspan="2">Economic</td><td>Construction costs</td><td>Quantitative</td><td>30</td></tr><tr><td>Maintenance costs</td><td>Quantitative</td><td>18</td></tr><tr><td rowspan="3">Social</td><td>Architectural impact/functional compatibility</td><td>Qualitative</td><td>22</td></tr><tr><td>Duration of works/disruption of use</td><td>Quantitative</td><td>27</td></tr><tr><td>Skilled labor</td><td>Qualitative</td><td>10</td></tr><tr><td rowspan="3">Environment</td><td>Carbon emissions</td><td>Quantitative</td><td>8</td></tr><tr><td>Energy performance</td><td>Quantitative</td><td>6</td></tr><tr><td>Other environmental parameters</td><td>Quantitative</td><td>11</td></tr></table>

(2020, 2023), Macieira et al. (2022), and Zuluaga et al. (2022) included embodied energy and carbon emissions, while Fiore et al. (2020a) focused on energy performance and environmental impact through the amount of waste production and recycling. Briz et al. (2023) included the indicators of recyclable, reusable, and ${ \mathsf { C O } } _ { 2 }$ emissions. The impact on human health, global warming potential, energy consumption, and air quality were considered by Santa-Cruz et al. (2021). On the other hand, Fiore et al. (2020b), Gallo et al. (2022), and Clemett et al. (2023) combined traditional retrofit alternatives with energy retrofit strategies to achieve seismic and energy eficiency. The life cycle analysis (LCA) was used by authors Formisano and Mazzolani (2015), Terracciano et al. (2015), Formisano et al. (2017), Carofilis et al. (2021), Vázquez-Rowe et al. (2021), Clemett et al. (2022), and Caruso et al. (2023) consider the environmental impact associated with the diferent phases of a building’s life. Researchers have increasingly strived to include environmental parameters in retrofit strategies in recent years in line with the Sustainable Development Goals (SDG) publication in 2015 to reduce ${ \mathsf { C O } } _ { 2 }$ emissions.

## 3.3. MCDM methods used

In decision-making, MCDM can be classified according to their characteristics, namely direct scoring methods, distance-based methods, those based on pairwise comparisons, outranking methods, and utility/value methods (Hajkowicz & Collins, 2007; de Brito & Evers, 2016). In scoring methods, we have Simple Additive Weighting (SAW) and Complex Proportional Assessment (COPRAS), an evolution of SAW. Among the most widely used distance-based methods are the Technique for Order of Preference by Similarity to the Ideal Solution (TOPSIS), which selects the best alternative by considering the distance to the ideal solution and the non-ideal solution simultaneously, and Multi-criteria Optimization and Compromise Solution (VIKOR) is based on the distance to the ideal solution. Pairwise comparison methods are used to determine the weight of diferent criteria based on decisionmakers’ knowledge; the Analytic Hierarchy Process (AHP) is the first method presented and one of the most widely used in decision-making problems. Other methods are the Analytic Network Process (ANP), which considers the interdependence and feedback relationships between criteria and alternatives, the main problem of the AHP, and the Measuring Attractiveness by a Categorical Based Evaluation Technique (MACBETH), an alternative to the AHP. Outranking methods, such as the Preference Ranking Organization Method for Enrichment of Evaluations (PRO-METHEE) or the Elimination and Choice Expressing Reality Method (ELECTRE), base the decision on establishing a degree of dominance between alternatives. Utility/value methods consider the best alternative as a function of the degree of satisfaction they provide, among them the Multiple Attribute Utility Theory (MAUT), Multi-Attribute Value Theory (MAVT), or MIVES, which is a derivative of the previous ones in which the equations defining the diferent satisfaction functions are provided.

Figure 4a shows the MCDMs used in the final classification, where the distance-based and pairwise comparison methods are the most used in building assessment and retrofit. Researchers use the MCDMs in their original form, as improved versions (5 papers) or combined with other MCDMs (55 papers). Figure 4b shows the specific MCDMs considered in publications. AHP is used in 35% of the articles, combined with TOPSIS in 31% and SAW in 11%. ANP is used by Alizadeh et al. (2018b), Nazmfar (2019), Nazmfar et al. (2019), and Maqsoom et al. (2024). MACBETH by Juliá et al. (2024), PROMETHEE is used by Mladineo et al. (2022), VIKOR by Jena et al. (2020), and MI-VES by Gandini et al. (2020), Pinero et al. (2017), and Briz et al. (2023). Other methods include the ordered weighted average (OWA) (Tesfamariam et al., 2010; Moradi et al., 2015; Ghajari et al., 2017; Nuno Martins et al., 2012); the Spatial Multi-Criteria Analysis and Ranking Tool (SMART) (Sinha et al., 2016), choosing by advantages (CBA) method (Vázquez-Rowe et al., 2021), Simultaneous Evaluation of Criteria and Alternatives (SECA) (Es-haghi et al., 2022) and step-wise weight assessment ratio analysis (SWARA) (Lee et al., 2019).

AHP is one of the most well-known multi-criteria decision-making methods due to its simplicity, accuracy, popularity, and theoretical robustness. This method is used in its original form, with adaptations, or in combination with other methods. An optimized O-AHP to overcome the reliability problems of AHP results due to inconsistency in the judgment matrix, especially in the case of large systems, is used by Sangiorgio et al. (2018a). The G1 method is a subjective assignment improved on AHP used by Zhu et al. (2023). The rough analytical hierarchy process (Rough AHP) proposed by Guo and Kapucu (2020) results from combining a Rough Set (RS) with a conventional AHP.

![](images/45a400161437d1c8c8f302fecfe85c88a3c19a4b4db55a5d9b2df2807329a95b.jpg)

![](images/9d5fbd7f19d98e915085482ad613fef0c91bb371c9be61e4c1f27b39bfa7dc59.jpg)  
Figure 4. MCDM methods used in assessing and retrofitting buildings: a – By category; b – Specific MCDM

Several authors have identified the TOPSIS method as the most suitable approach, given the clarity of its results and the ability of the method to adapt judgment (Requena-Garcia-Cruz et al., 2022). Researchers have compared various options to find the most appropriate MCDM method that will allow them to obtain the best results. For example, Vona et al. (2017) compared TOPSIS and VIKOR and concluded that TOPSIS is more suitable for largescale problems with numerous alternatives, while VIKOR may be more useful when the number of alternatives is limited. The article by Hoang et al. (2021) compared TOP-SIS and VIKOR for retrofit priority ranking and obtained similar results. In another study, multiple methods were used: weighted sum, weighted product, MAUT, ELECTRE, and PROMETHEE, VIKOR, and TOPSIS, concluding that TOPSIS and VIKOR are the most appropriate for building retrofit selection problems due to their ability to cope with diferent judgment criteria, clarity of results and ease of handling parameters and options (Caterino et al., 2009). TOPSIS and CBA methods delivered similar results (Santa-Cruz et al., 2021). On the other hand, Anwar et al. (2020) modified TOPSIS to add a risk attitude.

Artificial neural networks (ANN) models combined with MCDM were used in earthquake vulnerability assessment. For example, ANN was used with ANP (Alizadeh et al., 2018b; Maqsoom et al., 2024), with AHP (Yariyan et al., 2020), and with AHP – TOPSIS (Jena & Pradhan, 2020).

There is great concern about subjectivity in some steps of MCDM methods and how it can afect final decisionmaking. Real-world problems are often not precisely defined, and most engineering decisions are made under conditions of uncertainty. The most subjective step in decision-making is usually the weighing of criteria; conventional logic (crisp numbers) presumes every assignment to be certain and precise (Navarro et al., 2020b). Data sets from real-world problems can have confusing uncertainties, such as ambiguity, vagueness, and imprecision, making it dificult for decision-makers to express their thoughts using exact numbers (Fallahpour et al., 2020). In recent years, alternative mathematical logic has been used to handle linguistic variables and address problems of uncertainty. Fourteen articles that consider decision-making under uncertainty were identified in the publications reviewed in this study.

Several studies have combined pairwise comparison MCDM methods with fuzzy methodologies to improve the accuracy of decision-making processes: the hierarchical analytic fuzzy method using fuzzy triangular numbers (Hamdia et al., 2018; Lallam et al., 2023; Pashaei & Moghadam, 2018; Vahdat et al., 2014; Yariyan et al., 2020), analytical hierarchy process including fuzzy normalization (Narjabadifam et al., 2021) and ANP for criteria weighting and weighted fuzzy overlay in building vulnerability assessment (Nazmfar, 2019; Nazmfar et al., 2019). Other researchers have explored combining diferent MCDM methods in decision-making under uncertainty: hierarchical fuzzy TOPSIS (Sadrykia et al., 2017; Shahriar et al.,

2012; Ranjbar & Nekooie, 2018) and the fuzzy hierarchical analytical method with OWA (Ghajari et al., 2017). In Maqsoom’s et al. (2021) study, several hybrid models were compared to determine their efectiveness. Weights were generated by averaging the ANP and AHP models; LR and OWA logistic regression were used to run the hybrid A-OWA, A-fuzzy, OWA-LR, and fuzzy-LR models. The most accurate model results were obtained with A-OWA and OWA-LR. The paper by Tesfamariam et al. (2010) considers several cases using Bayesian probability theory, fuzzy sets, and Dempster-Shafer DS (random sets) theory, using OWA in rehabilitation selection for a reinforced concrete building. The proposed MCDM framework is versatile as it allows decision-making under diferent uncertainties.

When assessing the reliability of the results, sensitivity analyses can identify whether there are factors that can significantly alter the decision-making conclusions. The choice of criteria weights is the most significant source of uncertainty in the application of MCDMs and can significantly afect decision-making results (Caruso et al., 2023). Therefore, 29 articles included sensitivity analyses through the variation of criteria weights. Among the procedures most used in the articles are considering established ranges of variation, assuming one or more of the criteria as dominant, creating new scenarios by eliminating criteria, or calculating all possible combinations to determine the most sensitive criteria. On the other hand, 14 investigations consider uncertainties in expert judgments through fuzzy MCDM methods, of which 12 investigations correspond to the evaluation and selection of vulnerable buildings. Another group of authors, as sensitivity checks, consider the verification of the stability of the solution obtained by comparing the results with the application of other MCDMs (13 works). It should be noted that six studies compare the results of TOPSIS with other classical methods.

## 3.4. Integration of safety and sustainability criteria

Ensuring the safety of buildings is a significant concern in the construction industry, making it imperative to base vulnerability assessments and the selection of retrofit strategies on rigorous criteria. The articles reviewed demonstrate the keen interest of researchers in using stateof-the-art tools and methodologies to achieve this goal. Although safety remains paramount, assessing building vulnerability also considers economic and social considerations, as highlighted by several authors. In addition, selecting the best retrofit alternative for buildings requires the simultaneous combination of four dimensions, including safety, economic, social, and environmental criteria, thus allowing the integration of safety and sustainability. Figure 5 provides an overview of the number of publications grouped according to criteria or dimensions, the type of building analyzed, and whether they focus on vulnerability assessment or building retrofitting. Including social criteria in prioritizing vulnerable structures is particularly significant; thus, 20 articles include social criteria, highlighting their importance. In addition, 17 articles simultaneously consider economic and social criteria, making it possible to incorporate three dimensions in identifying vulnerable buildings.

![](images/22c03f0953ff1308f8c2552d66045528be8b6b908e0a9d94e42ce2cbe2655ada.jpg)  
Figure 5. Dimensions considered in the evaluation and reinforcement of buildings

In retrofit buildings, 14 papers, in addition to safety parameters, use economic and social criteria, while two papers consider economic and environmental criteria. However, in 15 papers, the researchers simultaneously integrated the four dimensions, namely safety, economic, social, and environmental, thanks to multi-criteria decision-making (MCDM) techniques. In the case of school buildings, eight papers considered all four dimensions when selecting retrofit strategies; this reflects the interest of researchers in this field and highlights the importance of ensuring the safety of these structures with sustainability criteria.

## 4. Discussion of the results

This literature review highlights the importance of MCDMs in integrating sustainability and safety pillars when assessing, selecting, and retrofitting buildings. The vulnerability of a building to natural hazards, in addition to safety parameters, requires consideration of economic and social aspects, which have been extensively addressed in several articles. On the other hand, when choosing the most effective retrofit option, the current trend calls for a fourdimensional approach encompassing safety, economy, society, and environment. As these criteria are diferent and often conflicting, multi-criteria decision-making methods can efectively resolve these conflicts. This section examines the trends identified in the research in this field through a critical analysis of the results obtained in the quantitative and qualitative analyses. In addition, possible future research directions in evaluating, selecting, and retrofitting buildings with MCDM are suggested, which build on the gaps identified in this study.

## 4.1. Trend analysis

Quantitative analysis reveals the specific areas that the scientific community has explored. It highlights the eforts to incorporate parameters that determine social vulnerability and the need to consider uncertainty in decision-making processes. Although the main focus of the research is on residential buildings, significant attention has also been devoted to studying school buildings, given their fundamental role as public infrastructure and historical heritage buildings. Scientific production has grown significantly in the last seven years, particularly in countries like Italy and Iran; this demonstrates the scientific community’s growing interest in integrating security with economic, social, and environmental parameters.

According to Figure 6, this literature review shows that 34% of the results are equitable, 2% are viable, and 17% meet the criteria for integrating safety and sustainability. Despite the eforts in research to include economic, social, and environmental criteria, it is necessary to establish a consensus on the specific criteria and sub-criteria that should be used for decision-making. Life cycle assessment (LCA) is a powerful and versatile tool that can be used to consider all environmental impacts caused by construction processes during the entire life cycle of the structure (Pons et al., 2018). This literature review highlights that only seven articles on selecting the best retrofit alternative include LCA studies.

The use of AHP dominates research, reaching 71% of the papers, individually or in hybridization with other MCDMs. AHP can handle both qualitative and quantitative criteria and, more importantly, measure the consistency of results (Pour, 2015), so researchers widely recognize and use it. The scientific community widely accepts the joint application of TOPSIS and AHP in this field. It produces a comprehensive ranking of all alternatives for each criterion while requiring the minimum number of parameters to be set by the DM (Gentile & Galasso, 2021). The integrated use of AHP and TOPSIS increases the consistency of the results to reach a consensus in decision-making in vulnerability analysis (Fayaz et al., 2023), giving the best results for seismic vulnerability assessment (Harirchian et al., 2020). This is corroborated in other areas of civil engineering, such as sustainability in civil engineering, construction, and building technology (Zavadskas et al., 2018) in the application of fuzzy criteria in civil engineering (Wen et al., 2021) as well as in the study of MCDMs in construction (Zhu et al., 2021).

Another method used in combination with relevant AHP is SAW. This scoring method is used for its simplicity and ease of interpretation of the results. However, it should be noted that this technique has limitations when it comes to complex problems involving conflicting criteria, such as the integration of safety and sustainability. In these cases, an adequate normalization of the criteria is required to overcome this limitation (Navarro et al., 2020b). Other relevant methods explored in the literature include ANP and OWA. MIVES stands out for decision support using diferent satisfaction or value functions (Sánchez-Garrido & Yepes, 2020).

The correspondence analysis in Figure 7 demonstrates how the MCDM categories used in the articles relate to the objectives of the studies. This analysis provides a twodimensional map that reveals the inertia and association relationships of the variables. IBM SPSS Statistics 25.0 software was used to analyze the results and show how the MCDM categories interact with the study’s objectives. The closer the points of the MCDM category and the target, the higher the correlation. There is a clear correlation between scoring methods and building assessment. Researchers use methods such as SAW to determine vulnerability indices that combine physical, economic, and social criteria. Developing indices that integrate several dimensions allows policymakers to target resources, design appropriate prediction and mitigation strategies, and improve the resilience of cities (Alam & Haque, 2022).

On the other hand, distance-based methods are statistically related to building retrofitting and, to a lesser extent, school building retrofitting. Numerous studies have considered TOPSIS an appropriate method for selecting retrofit alternatives (Caterino et al., 2009; Hoang et al., 2021; Vona et al., 2017). Methods such as OWA, MIVES, PROMETHEE, MACBETH, and others do not have a solid statistical interaction with the analyzed variables.

Of the 91 articles reviewed, 14 (15%) consider nonprobabilistic uncertainty associated with human thinking in decision-making. Fuzzy set theory, in combination with AHP and ANP pairwise weighting methodologies, is used in 8 manuscripts. The hybrid AHP + TOPSIS + fuzzy methodology demonstrates a flexible adaptation when considering uncertainty in decision-making. One paper examined cases with diferent uncertainties using Bayesian probability theory, fuzzy sets, and DS theory of random sets using OWA, demonstrating the versatility of the proposed model.

![](images/9b8a8cadff7ce6e5282e81c84cd6e04e332ed8deeee307b77eae0e89218bc3f2.jpg)  
Figure 6. Integration of safety and sustainability in the evaluation and reinforcement of buildings

![](images/abafab2cfa4d4eefb9fe28bf7ec96153bac94a9b491920b766fd0ee2582e05ac.jpg)  
Figure 7. Simple correspondence analysis for the objective of the studies and the MCDM category used

## 4.2. Future directions

The literature review underscores the necessity of achieving consensus within the scientific community regarding the criteria to be evaluated across various dimensions. Life Cycle Cost (LCC), Environmental Analysis (LCA), and Social Life Cycle Analysis (SLCA) ofer valuable insights toward this objective. Although LCA has been utilized in several articles within this review, social life cycle analyses have been largely overlooked. Notably, studies in civil engineering have incorporated SLCA methodologies in analyzing bridges (Martínez-Muñoz et al., 2022; Navarro et al., 2018) and buildings (Sánchez-Garrido et al., 2022).

The use of classical decision-making methods dominates research. Despite the emergence of newer and more sophisticated methods, they have yet to be given due attention or application in the field. Given the proliferation of new decision-making methods in recent years, there is the potential for these approaches to ofer greater accuracy and applicability, thus presenting viable solutions to current challenges. Among the pairwise comparison methods, the Best-worst method (BWM) proposed by Rezaei (2015) ofers better results. It is easier to apply than AHP and ANP, thus proving its superiority (Zhu et al., 2021). Although several researchers have validated the use of TOP-SIS by comparing the results with other classical MCDMs, newer methods could be used: Integrated Simple Weighted Simple Sum-Product (WISP) (Stanujkic et al., 2023), Combinative Distance-based Assessment (CODAS) (Keshavarz Ghorabaee et al., 2016); comprehensive distance-based ranking (COBRA) (Krstic et al., 2022); Evaluation based on Distance from Average Solution (EDAS) (Keshavarz Ghorabaee et al., 2015), among others. The term “deferral efect” summarizes the current status of the analyzed studies, indicating the lag in this field in terms of MCDM research and application (Zhu et al., 2021).

Most traditional MCDMs operate under criteria independence; several interactions among criteria might occur in real-life situations, so more sophisticated/intelligent techniques are required to deal with the needs of the problem in decision-making (Golcuk & Baykasoglu, 2016). A common criticism against ANP is its complexity, which hampers practical application. The Decision-Making Trial and Evaluation Laboratory (DEMATEL) technique can build the influential relation matrix to construct the influential network relations map (INRM) and determine the influential weights of DANP (DEMATEL-based ANP) using the basic concepts of ANP (Penadés-Plà et al., 2016). The DANP methodology is used to model criteria interactions in the research of numerous fields such as tourism, commerce and finance, industry, information technology, and construction (Nguyen, 2023).

The exploration and utilization of fuzzy MCDM models remain relatively limited within the scope of this literature review. However, several practical tools for expressing fuzzy information have emerged recently and gained widespread adoption. These include linguistics terms set neutrosophic, hesitant fuzzy probabilistic linguistic, and continuous interval-valued (Wen et al., 2021). Notably, linguistics terms neutrosophic techniques have been increasingly employed in civil engineering applications. They have been utilized in assessing the sustainability of bridges (Navarro et al., 2020a), single-family houses (Sánchez-Garrido et al., 2021), and prioritizing maintenance in sanitary facilities (Ahmed et al., 2021). Such methodologies ofer valuable support in managing uncertainty inherent in the evaluation and reinforcement of buildings.

## 5. Conclusions

This study reviews 91 articles published since 2008 focusing on assessing, selecting, and retrofitting buildings using multi-criteria decision-making methods. The overall analysis suggests that this topic has recently generated considerable interest in the scientific community. There is evidence of many investigations studying public buildings, particularly schools and historic buildings. A review of the criteria reveals that researchers assess and select vulnerable buildings with economic and social considerations. Regarding building retrofitting, the current approach emphasizes the integration of four dimensions: safety, economic, social, and environmental. However, there has yet to be a consensus on the specific criteria for each dimension. Given the complexity of integrating the pillars of sustainability and safety, the MCDM proves to be a helpful tool. Despite research eforts, only 15 of 32 articles selected the best retrofit option integrating safety and sustainability, with limited involvement of life cycle analysis studies.

The hierarchical analytical process (AHP) is the most widely used method for criteria weighting and is used in adapted or hybrid versions with other MCDM techniques. Given the complexity of the relationships between sustainability and safety criteria, the scientific community widely accepts the TOPSIS method. This conclusion is supported by the results of the statistical correspondence analysis performed on the MCDM category variables and the research objective, in which the correlation between building retrofit and TOPSIS is evident. In addition, the literature explores other relevant methods, such as SAW, ANP, MI-VES, and OWA.

The main problem with traditional MCDM is the subjective nature of the decision-maker’s involvement phase. This literature review revealed that most of the articles use a crisp approach. However, 15% of the articles incorporate decision-making under uncertainty, using hybrid MCDM criteria with fuzzy methods, such as AHP, ANP, TOPSIS, and OWA. Only one article explores other methods, such as Bayesian networks and random ensembles, highlighting a knowledge gap. Based on the results, further research is needed to address the subjectivity and bias inherent in expert judgments, using current methodologies to assess the pillars of sustainability and allow for real integration with safety.

This literature review makes a significant contribution to the field of research for a holistic renovation of the existing building stock. It critically examines current trends and proposes new research directions for integrating safety and sustainability into existing buildings using MCDM. The key findings of this research can be succinctly outlined as follows: Firstly, it identifies the most utilized criteria across safety, economic, social, and environmental dimensions by researchers. This identification fosters consensus-building for future studies, highlighting the significance of incorporating life cycle analysis in assessing building pathologies and retrofit strategies. Secondly, a critical discussion of existing research trends reveals a predominant use of traditional single or hybrid MCDMs to integrate structural safety with sustainability in existing buildings. Lastly, the study pinpoints research gaps, laying the groundwork for future research directions. These recommendations advocate for the exploration of new and sophisticated MCDMs, the consideration of criterion interactions, and the management of uncertainty in expert judgments. Lines of research are promising in the search for improved solutions in integrating safety and sustainability in the assessment, selection, and retrofitting of existing buildings.

## Funding

The authors acknowledge the financial support of Grant PID2020-117056RB-I00 funded by MCIN/AEI/ 10.13039/501100011033 and by “ERDF A way of making Europe”.

The first author is grateful to the Universidad Central del Ecuador for funding to pursue a doctoral program at the Universitat Politècnica de València.

## Author contributions

This paper represents a result of teamwork. The authors jointly designed the research. P. V. developed the methodology, investigated, and drafted the original manuscript. P. V., A. J. S.-G. and V. Y. edited and improved the manuscript until all authors were satisfied with the final version. All authors have read and agreed to the published version of the manuscript.

## Disclosure statement

The authors declare that there are no conflicts of interest regarding the publication of this article.

## References

Abdrabo, K. I., Kantoush, S. A., Esmaiel, A., Saber, M., Sumi, T., Almamari, M., Elboshy, B., & Ghoniem, S. (2023). An integrated indicator-based approach for constructing an urban flood vulnerability index as an urban decision-making tool using the PCA and AHP techniques: A case study of Alexandria, Egypt. Urban Climate, 48, Article 101426. https://doi.org/10.1016/j.uclim.2023.101426

Ahmed, R., Nasiri, F., & Zayed, T. (2021). A novel Neutrosophicbased machine learning approach for maintenance prioritization in healthcare facilities. Journal of Building Engineering, 42, Article 102480. https://doi.org/10.1016/j.jobe.2021.102480

Alam, M. S., & Haque, S. M. (2020). Seismic vulnerability evaluation of educational buildings of Mymensingh city, Bangladesh using rapid visual screening and index based approach. International Journal of Disaster Resilience in the Built Environment, 11(3), 379–402, https://doi,org/10.1108/IJDRBE-07-2019-0043

Alam, M. S., & Haque, S. M. (2022). Multi-dimensional earthquake vulnerability assessment of residential neighborhoods of Mymensingh City, Bangladesh: A spatial multi-criteria analysis based approach. Journal of Urban Management, 11(1), 37–58. https://doi.org/10.1016/i.ium.2021.09.001

Alam, N., Alam, M. S., & Tesfamariam, S. (2012). Buildings’ seismic vulnerability assessment methods: a comparative study. Natural Hazards, 62(2), 405–424. https://doi.org/10.1007/s11069-011-0082-4

Aliabadi, S. F., Sarsangi, A., & Modiri, E. (2015). The social and physical vulnerability assessment of old texture against earth-

quake (case study: Fahadan district in Yazd City). Arabian Journal of Geosciences, 8(12), 10775–10787. https://doi.org/10.1007/s12517-015-1939-8

Alizadeh, M., Hashim, M., Alizadeh, E., Shahabi, H., Karami, M. R., Pour, A. B., Pradhan, B., & Zabihi, H. (2018a). Multi-criteria decision making (MCDM) model for seismic vulnerability assessment (SVA) of urban residential buildings. ISPRS International Journal of Geo-Information, 7(11), Article 444. https://doi.org/10.3390/ijgi7110444

Alizadeh, M., Ngah, I., Hashim, M., Pradhan, B., & Pour, A. B. (2018b). A Hybrid Analytic Network Process and Artificial Neural Network (ANP-ANN) model for urban earthquake vulnerability assessment. Remote Sensing, 10(6), Article 975. https://doi.org/10.3390/rs10060975

Andreolli, F., Bragolusi, P., D’Alpaos, C., Faleschini, F., & Zanini, M. A. (2022). An AHP model for multiple-criteria prioritization of seismic retrofit solutions in gravity-designed industrial buildings. Journal of Building Engineering, 45, Article 103493. https://doi.org/10.1016/j.jobe.2021.103493

Anelli, A., Santa-Cruz, S., Vona, M., Tarque, N., & Laterza, M. (2019). A proactive and resilient seismic risk mitigation strategy for existing school buildings. Structure and Infrastructure Engineering, 15(2), 137–151. https://doi.org/10.1080/15732479.2018.1527373

Anelli, A., Vona, M., & Hidalgo, S. S.-C. (2020). Comparison of different intervention options for massive seismic upgrading of essential facilities. Buildings, 10(7), Article 125. https://doi.org/10.3390/buildings10070125

Anwar, G. A., Dong, Y., & Li, Y. (2020). Performance-based decision-making of buildings under seismic hazard considering long-term loss, sustainability, and resilience. Structure and Infrastructure Engineering, 17(4), 454–470. https://doi.org/10.1080/15732479.2020.1845751

Anwar, G. A., Hussain, M., Akber, M. Z., Khan, M. A., & Khan, A. A. (2023). Sustainability-oriented optimization and decision making of community buildings under seismic hazard. Sustainability, 15(5), Article 4385. https://doi.org/10.3390/su15054385

Bahadori, H., Hasheminezhad, A., & Karimi, A. (2017). Development of an integrated model for seismic vulnerability assessment of residential buildings: Application to Mahabad City, Iran. Journal of Building Engineering, 12, 118–131. https://doi.org/10.1016/j.jobe.2017.05.014

Banica, A., Rosu, L., Muntele, I., & Grozavu, A. (2017). Towards urban resilience: A multi-criteria analysis of seismic vulnerability in Iasi City (Romania). Sustainability, 9(2), Article 270. https://doi.org/10.3390/su9020270

Biondini, F., & Frangopol, D. M. (2016). Life-cycle performance of deteriorating structural systems under uncertainty: Review. Journal of Structural Engineering, 142(9), Article F4016001. https://doi.org/10.1061/(ASCE)ST.1943-541X.0001544

Briz, E., Garmendia, L., Marcos, I., & Gandini, A. (2023). Improving the resilience of historic areas coping with natural and climate change hazards: Interventions based on multi-criteria methodology. International Journal of Architectural Heritage. https://doi.org/10.1080/15583058.2023.2218311

Carofilis, W. W., Clemett, N., Gabbianelli, G., O’Reilly, G., & Monteiro, R. (2021). Selection of optimal seismic retrofitting for existing school buildings through multi-criteria decision making. In Eccomas Proceedia COMPDYN (pp. 1223–1241). https://doi.org/10.7712/120121.8558.19257

Caruso, M., Couto, R., Pinho, R., & Monteiro, R. (2023). Decisionmaking approaches for optimal seismic/energy integrated retrofitting of existing buildings. Frontiers in Built Environment, 9. https://doi.org/10.3389/fbuil.2023.1176515

Caterino, N., & Cosenza, E. (2018a). A multi-criteria approach for selecting the seismic retrofit intervention for an existing structure accounting for expected losses and tax incentives in Italy. Engineering Structures, 174, 840–850. https://doi.org/10.1016/j.engstruct.2018.07.090

Caterino, N., & Cosenza, E. (2018b). A multi-criteria approach for selecting the seismic retrofit intervention for an existing structure accounting for expected losses and tax incentives in Italy. Engineering Structures, 174, 840–850. https://doi.org/10.1016/j.engstruct.2018.07.090

Caterino, N., Iervolino, I., Manfredi, G., & Cosenza, E. (2008). Multi-criteria decision making for seismic retrofitting of RC structures. Journal of Earthquake Engineering, 12(4), 555–583. https://doi.org/10.1080/13632460701572872

Caterino, N., Iervolino, I., Manfredi, G., & Cosenza, E. (2009). Comparative analysis of multi-criteria decision-making methods for seismic structural retrofitting. Computer-Aided Civil and Infrastructure Engineering, 24(6), 432–445. https://doi.org/10.1111/j.1467-8667.2009.00599.x

Caterino, N., Nuzzo, I., Ianniello, A., Varchetta, G., & Cosenza, E. (2021). A BIM-based decision-making framework for optimal seismic retrofit of existing buildings. Engineering Structures, 242, Article 112544. https://doi.org/10.1016/j.engstruct.2021.112544

Choi, J., & Choi, J. (2022). Technical feasibility study model of aged apartment renovation applying Analytic Hierarchy Process. Journal of Civil Engineering and Management, 28(1), 39–50. https://doi.org/10.3846/jcem.2021.16013

Chu, J., Zhang, Q., Wang, A., & Yu, H. (2021). A hybrid intelligent model for urban seismic risk assessment from the perspective of possibility and vulnerability based on Particle Swarm Optimization. Scientific Programming, 2021, Article 2218044. https://doi.org/10.1155/2021/2218044

Clemett, N., Gallo, W. W. C., O’Reilly, G. J., Gabbianelli, G., & Monteiro, R. (2022). Optimal seismic retrofitting of existing buildings considering environmental impact. Engineering Structures, 250, Article 113391. https://doi.org/10.1016/j.engstruct.2021.113391

Clemett, N., Carofilis Gallo, W. W., Gabbianelli, G., O’Reilly, G. J., & Monteiro, R. (2023). Optimal combined seismic and energy eficiency retrofitting for existing buildings in Italy. Journal of Structural Engineering, 149(1), Article 04022207. https://doi.org/10.1061/(ASCE)ST.1943-541X.0003500

Dall’Osso, F., Gonella, M., Gabbianelli, G., Withycombe, G., & Dominey-Howes, D. (2009). A revised (PTVA) model for assessing the vulnerability of buildings to tsunami damage. Natural Hazards and Earth System Sciences, 9(5), 1557–1565. https://doi.org/10.5194/nhess-9-1557-2009

D’Alpaos, C., & Valluzzi, M. R. (2020). Protection of cultural heritage buildings and artistic assets from seismic hazard: A hierarchical approach. Sustainability, 12(4), Article 1608. https://doi.org/10.3390/su12041608

de Brito, M. M., & Evers, M. (2016). Multi-criteria decision-making for flood risk management: a survey of the current state of the art. Natural Hazards and Earth System Sciences, 16(4), 1019– 1033. https://doi.org/10.5194/nhess-16-1019-2016

Es-haghi, M. S., Barkhordari, M. S., Huang, Z., & Ye, J. (2022). Multicriteria decision-making methods in selecting seismic upgrading strategy of high-rise RC wall buildings. Journal of Structural Engineering, 148(4), Article 04022015. https://doi.org/10.1061/(ASCE)ST.1943-541X.0003304

Fallahpour, A., Wong, K. Y., Rajoo, S., Olugu, E. U., Nilashi, M., & Turskis, Z. (2020). A fuzzy decision support system for sustainable construction project selection: an integrated FPP-FIS

model. Journal of Civil Engineering and Management, 26(3), 247–258. https://doi.org/10.3846/jcem.2020.12183

Fayaz, M., Romshoo, S. A., Rashid, I., & Chandra, R. (2023). Earthquake vulnerability assessment of the built environment in the city of Srinagar, Kashmir Himalaya, using a geographic information system. Natural Hazards and Earth System Sciences, 23(4), 1593–1611. https://doi.org/10.5194/nhess-23-1593-2023

Fiore, P., Donnarumma, G., Falce, C., D’Andria, E., & Sicignano, C. (2020a). An AHP-based methodology for decision support in integrated interventions in school buildings. Sustainability, 12(23), Article 10181. https://doi.org/10.3390/su122310181

Fiore, P., Sicignano, E., & Donnarumma, G. (2020b). An AHP-based Methodology for the evaluation and choice of integrated interventions on historic buildings. Sustainability, 12(14), Article 5795. https://doi.org/10.3390/su12145795

Formisano, A., & Mazzolani, F. M. (2015). On the selection by MCDM methods of the optimal system for seismic retrofitting and vertical addition of existing buildings. Computers & Structures, 159, 1–13. https://doi.org/10.1016/j.compstruc.2015.06.016

Formisano, A., Castaldo, C., & Chiumiento, G. (2017). Optimal seismic upgrading of a reinforced concrete school building with metal-based devices using an eficient multi-criteria decisionmaking method. Structure and Infrastructure Engineering, 13(11), 1373–1389. https://doi.org/10.1080/15732479.2016.1268174

Gacu, J. G., Monjardin, C. E. F., de Jesus, K. L. M., & Senoro, D. B. (2023). GIS-based Risk assessment of structure attributes in flood zones of Odiongan, Romblon, Philippines. Buildings, 13(2), Article 506. https://doi.org/10.3390/buildings13020506

Gallo, W. W. C., Clemett, N., Gabbianelli, G., O’Reilly, G., & Monteiro, R. (2022). Seismic resilience assessment in optimally integrated retrofitting of existing school buildings in Italy. Buildings, 12(6), Article 845. https://doi.org/10.3390/buildings12060845

Gandini, A., Garmendia, L., Prieto, I., Alvarez, I., & San-Jose, J.-T. (2020). A holistic and multi-stakeholder methodology for vulnerability assessment of cities to flooding and extreme precipitation events. Sustainable Cities and Society, 63, Article 102437. https://doi.org/10.1016/j.scs.2020.102437

Gentile, R., & Galasso, C. (2021). Simplified seismic loss assessment for optimal structural retrofit of RC buildings. Earthquake Spectra, 37(1), 346–365. https://doi.org/10.1177/8755293020952441

Gentile, R., Galasso, C., Idris, Y., Rusydy, I., & Meilianda, E. (2019). From rapid visual survey to multi-hazard risk prioritisation and numerical fragility of school buildings. Natural Hazards and Earth System Sciences, 19(7), 1365–1386. https://doi.org/10.5194/nhess-19-1365-2019

Ghajari, Y. E., Alesheikh, A. A., Modiri, M., Hosnavi, R., & Abbasi, M. (2017). Spatial modelling of urban physical vulnerability to explosion hazards using GIS and fuzzy MCDA. Sustainability, 9(7), Article 1274. https://doi.org/10.3390/su9071274

Golcuk, I., & Baykasoglu, A. (2016). An analysis of DEMATEL approaches for criteria interaction handling within ANP. Expert Systems with Applications, 46, 346–366. https://doi.org/10.1016/j.eswa.2015.10.041

Guo, X., & Kapucu, N. (2020). Assessing social vulnerability to earthquake disaster using rough analytic hierarchy process method: A case study of Hanzhong City, China. Safety Science, 125, Article 104625. https://doi.org/10.1016/j.ssci.2020.104625

Hajkowicz, S., & Collins, K. (2007). A review of multiple criteria analysis for water resource planning and management. Water Resources Management, 21(9), 1553–1566. https://doi.org/10.1007/s11269-006-9112-5

Hamdia, K. M., Arafa, M., & Alqedra, M. (2018). Structural damage assessment criteria for reinforced concrete buildings by using a Fuzzy Analytic Hierarchy process. Underground Space, 3(3), 243–249. https://doi.org/10.1016/j.undsp.2018.04.002

Harirchian, E., Jadhav, K., Mohammad, K., Aghakouchaki Hosseini, S. E., & Lahmer, T. (2020). A comparative study of MCDM methods integrated with rapid visual seismic vulnerability assessment of existing RC structures. Applied Sciences, 10(18), Article 6411. https://doi.org/10.3390/app10186411

Hoang, T., Noy, I., Filippova, O., & Elwood, K. (2021). Prioritising earthquake retrofitting in Wellington, New Zealand. Disasters, 45(4), 968–995. https://doi.org/10.1111/disa.12450

Jamal-ud-din, Ainuddin, S., Murtaza, G., Faiz, S., Muhammad, A. S., Raheem, A., & Khan, S. (2023). Earthquake vulnerability assessment through spatial multi-criteria analysis: a case study of Quetta city, Pakistan. Environmental Earth Sciences, 82(11), Article 262. https://doi.org/10.1007/s12665-023-10967-3

Jena, R., & Pradhan, B. (2020). Integrated ANN-cross-validation and AHP-TOPSIS model to improve earthquake risk assessment. International Journal of Disaster Risk Reduction, 50, Article 101723. https://doi.org/10.1016/j.ijdrr.2020.101723

Jena, R., Pradhan, B., & Beydoun, G. (2020). Earthquake vulnerability assessment in Northern Sumatra province by using a multi-criteria decision-making model. International Journal of Disaster Risk Reduction, 46, Article 101518. https://doi.org/10.1016/j.ijdrr.2020.101518

Juliá, P. B., Stellacci, S., & Poletti, E. (2024). Evaluation of retrofitting techniques for historical adobe constructions using a multi-criteria decision analysis: The case study of Chile. International Journal of Architectural Heritage, 18(1), 40–63. https://doi.org/10.1080/15583058.2022.2103476

Keshavarz Ghorabaee, M., Zavadskas, E. K., Olfat, L., & Turskis, Z. (2015). Multi-criteria inventory classification using a new method of evaluation based on Distance from Average Solution (EDAS). Informatica, 26(3), 435–451. https://doi.org/10.15388/Informatica.2015.57

Keshavarz Ghorabaee, M., Zavadskas, E. K., Turskis, Z., & Antucheviciene. L. (2016). A new combinative distance-based assessment (CODAS) method for multi-criteria decision-making. Economic Computation and Economic Cybernetics Studies and Research, 50(3), 25–44.

Krstic, M., Agnusdei, G. P., Miglietta, P. P., Tadic, S., & Roso, V. (2022). Applicability of Industry 4.0 technologies in the reverse logistics: A circular economy approach based on COmprehensive Distance Based RAnking (COBRA) method. Sustainability, 14(9), Article 5632. https://doi.org/10.3390/su14095632

Lallam, M., Djebli, A., & Mammeri, A. (2023). Fuzzy analytical hierarchy process for assessing damage in old masonry buildings: A case study. International Journal of Architectural Heritage. https://doi.org/10.1080/15583058.2023.2295885

Lee, S., Panahi, M., Pourghasemi, H. R., Shahabi, H., Alizadeh, M., Shirzadi, A., Khosravi, K., Melesse, A. M., Yekrangnia, M., Rezaie, F., Moeini, H., Pham, B. T., & Bin Ahmad, B. (2019). SEVUCAS: A novel GIS-based machine learning software for seismic vulnerability assessment. Applied Sciences, 9(17), Article 3495. https://doi.org/10.3390/app9173495

Macieira, M., Mendonca, P., Guedes, J. M., & Tereso, A. (2022). Evaluating the eficiency of membrane’s refurbishment solutions to perform vertical extensions in old buildings using a multicriteria decision-support model. Architectural Engineering and Design Management, 18(1), 1–25. https://doi.org/10.1080/17452007.2019.1656597

Makoond, N., Pela, L., & Molins, C. (2021). A risk index for the structural diagnosis of masonry heritage (RISDiMaH). Construc-

tion and Building Materials, 284, Article 122433. https://doi.org/10.1016/j.conbuildmat.2021.122433

Maqsoom, A., Aslam, B., Awais, M., Hassan Usman and Alaloul, W. S., Musarat, M. A., & Qureshi, M. I. (2021). Eficiency of multiple hybrid techniques for the earthquake physical susceptibility mapping: the case of Abbottabad District, Pakistan. Environmental Earth Sciences, 80, Article 678. https://doi.org/10.1007/s12665-021-09964-1

Maqsoom, A., Aslam, B., Khalil, U., Mehmood, M. A., Ashraf, H., & Siddique, A. (2024). An integrated approach based earthquake risk assessment of a seismically active and rapidly urbanizing area in Northern Pakistan. Geocarto International, 37(27), 16043–16073. https://doi.org/10.1080/10106049.2022.2105404

Marcher, C., Giusti, A., & Matt, D. T. (2020). Decision support in building construction: A systematic review of methods and application areas. Buildings, 10(10), Article 170. https://doi.org/10.3390/buildings10100170

Martínez-Muñoz, D., Martí, J. V, & Yepes, V. (2022). Social impact assessment comparison of composite and concrete bridge alternatives. Sustainability, 14(9), Article 5186. https://doi.org/10.3390/su14095186

Menna, C., Felicioni, L., Negro, P., Lupisek, A., Romano, E., Prota, A., & Hajek, P. (2022). Review of methods for the combined assessment of seismic resilience and energy eficiency towards sustainable retrofitting of existing European buildings. Sustainable Cities and Society, 77, Article 103556. https://doi.org/10.1016/j.scs.2021.103556

Mili, R. R., Hosseini, K. A., & Izadkhah, Y. O. (2018). Developing a holistic model for earthquake risk assessment and disaster management interventions in urban fabrics. International Journal of Disaster Risk Reduction, 27, 355–365. https://doi.org/10.1016/j.ijdrr.2017.10.022

Mladineo, N., Mladineo, M., Benvenuti, E., Kekez, T., & Nikolic, Z. (2022). Methodology for the assessment of multi-hazard risk in urban homogenous zones. Applied Sciences, 12(24), Article 12843. https://doi.org/10.3390/app122412843

Moradi, M., Delavar, M. R., & Moshiri, B. (2015). A GIS-based multi-criteria decision-making approach for seismic vulnerability assessment using quantifier-guided OWA operator: a case study of Tehran, Iran. Annals of GIS, 21(3), 209–222. https://doi.org/10.1080/19475683.2014.966858

Mourato, S., Fernandez, P., Pereira, L. G., & Moreira, M. (2023). Assessing vulnerability in flood prone areas using Analytic Hierarchy Process-Group decision making and geographic information system: A case study in Portugal. Applied Sciences, 13(8), Article 4915. https://doi.org/10.3390/app13084915

Murray, P. B., Feliciano, D., Goldwyn, B. H., Liel, A. B., Arroyo, O., & Javernick-Will, A. (2023). Seismic safety of informally constructed reinforced concrete houses in Puerto Rico. Earthquake Spectra, 39(1), 5–33. https://doi.org/10.1177/87552930221123085

Nadkarni, R. R., & Puthuvayi, B. (2020). A comprehensive literature review of multi-criteria decision making methods in heritage buildings. Journal of Building Engineering, 32, Article 101814. https://doi.org/10.1016/j.jobe.2020.101814

Narjabadifam, P., Hoseinpour, R., Noori, M., & Altabey, W. (2021). Practical seismic resilience evaluation and crisis management planning through GIS-based vulnerability assessment of buildings. Earthquake Engineering and Engineering Vibration, 20(1), 25–37. https://doi.org/10.1007/s11803-021-2003-1

Navarro, I. J., Yepes, V., & Martí, J. V. (2018). Social life cycle assessment of concrete bridge decks exposed to aggressive environments. Environmental Impact Assessment Review, 72, 50–63. https://doi.org/10.1016/j.eiar.2018.05.003

Navarro, I. J., Yepes, V., & Martí, J. V. (2019). A review of multicriteria assessment techniques applied to sustainable infrastructure design. Advances in Civil Engineering, 2019, Article 6134803. https://doi.org/10.1155/2019/6134803

Navarro, I. J., Yepes, V., & Martí V, J. (2020a). Sustainability assessment of concrete bridge deck designs in coastal environments using neutrosophic criteria weights. Structure and Infrastructure Engineering, 16(7), 949–967. https://doi.org/10.1080/15732479.2019.1676791

Navarro, I. J., Penadés-Plà, V., Martínez-Muñoz, D., Rempling, R., & Yepes, V. (2020b). Life cycle sustainability assessment for multicriteria decision making in bridge design: a review. Journal of Civil Engineering and Management, 26(7), 690–704. https://doi.org/10.3846/jcem.2020.13599

Nazmfar, H. (2019). An integrated approach of the analytic network process and fuzzy model mapping of evaluation of urban vulnerability against earthquake. Geomatics Natural Hazards & Risk, 10(1), 1512–1528. https://doi.org/10.1080/19475705.2019.1588791

Nazmfar, H., Saredeh, A., Eshgi, A., & Feizizadeh, B. (2019). Vulnerability evaluation of urban buildings to various earthquake intensities: a case study of the municipal zone 9 of Tehran. Human and Ecological Risk Assessment, 25(1–2, SI), 455–474. https://doi.org/10.1080/10807039.2018.1556086

Nguyen, M. V. (2023). Drivers of innovation towards sustainable construction: A study in a developing country. Journal of Building Engineering, 80, Article 107970. https://doi.org/10.1016/j.jobe.2023.107970

Nuno Martins, V., e Silva, D., & Cabral, P. (2012). Social vulnerability assessment to seismic risk using multicriteria analysis: the case study of Vila Franca do Campo (So Miguel Island, Azores, Portugal). Natural Hazards, 62(2), 385–404. https://doi.org/10.1007/s11069-012-0084-x

Palermo, V., Tsionis, G., & Sousa, M. L. (2018). Building stock inventory to assess seismic vulnerability across Europe. Publications Ofice of the European Union. https://doi.org/10.2760/530683

Panahi, M., Rezaie, F., & Meshkani, S. A. (2014). Seismic vulnerability assessment of school buildings in Tehran city based on AHP and GIS. Natural Hazards and Earth System Sciences, 14(4), 969–979. https://doi.org/10.5194/nhess-14-969-2014

Papathoma-Koehle, M., Cristofari, G., Wenk, M., & Fuchs, S. (2019). The importance of indicator weights for vulnerability indices and implications for decision making in disaster management. International Journal of Disaster Risk Reduction, 36, Article 101103. https://doi.org/10.1016/j.ijdrr.2019.101103

Pashaei, R., & Moghadam, A. S. (2018). Fuzzy AHP method for selection of a suitable seismic retrofitting alternative in low-rise buildings. Civil Engineering Journal-Tehran, 4(5), 1074–1086. https://doi.org/10.28991/cej-0309157

Passoni, C., Caruso, M., Marini, A., Pinho, R., & Landolfo, R. (2022). The role of life cycle structural engineering in the transition towards a sustainable building renovation: Available tools and research needs. Buildings, 12(8), Article 1107. https://doi.org/10.3390/buildings12081107

Penadés-Plà, V., García-Segura, T., Martí, J. V, & Yepes, V. (2016). A review of multi-criteria decision-making methods applied to the sustainable bridge design. Sustainability, 8(12), Article 1295. https://doi.org/10.3390/su8121295

Pinero, I., San-Jose, J. T., Rodriguez, P., & Losanez, M. M. (2017). Multi-criteria decision-making for grading the rehabilitation of heritage sites. Application in the historic center of La Habana. Journal of Cultural Heritage, 26, 144–152. https://doi.org/10.1016/j.culher.2017.01.012

Pohoryles, D. A., Bournas, D. A., Da Porto, F., Caprino, A., Santarsiero, G., & Triantafillou, T. (2022). Integrated seismic and energy retrofitting of existing buildings: A state-of-the-art review. Journal of Building Engineering, 61, Article 105274. https://doi.org/10.1016/j.jobe.2022.105274

Pons, J. J., Penadés-Plà, V., Yepes, V., & Martí, J. V. (2018). Life cycle assessment of earth-retaining walls: An environmental comparison. Journal of Cleaner Production, 192, 411–420. https://doi.org/10.1016/j.jclepro.2018.04.268

Pour, M. T. (2015). Prioritization of methods for seismic retrofitting of structures. Journal of Engineering Science and Technology, 10(SI), 64–80.

Ranjbar, H. R., & Nekooie, M. A. (2018). An improved hierarchical fuzzy TOPSIS approach to identify endangered earthquakeinduced buildings. Engineering Applications of Artificial Intelligence, 76, 21–39. https://doi.org/10.1016/j.engappai.2018.08.007

Requena-Garcia-Cruz, M. V, Morales-Esteban, A., & Durand-Neyra, P. (2022). Assessment of specific structural and groundimprovement seismic retrofitting techniques for a case study RC building by means of a multi-criteria evaluation. Structures, 38, 265–278. https://doi.org/10.1016/j.istruc.2022.02.015

Rezaei, J. (2015). Best-worst multi-criteria decision-making method. Omega, 53, 49–57. https://doi.org/10.1016/j.omega.2014.11.009

Rezaie, F., & Panahi, M. (2015). GIS modeling of seismic vulnerability of residential fabrics considering geotechnical, structural, social and physical distance indicators in Tehran using multicriteria decision-making techniques. Natural Hazards and Earth System Sciences, 15(3), 461–474. https://doi.org/10.5194/nhess-15-461-2015

Sadrykia, M., Delavar, M. R., & Zare, M. (2017). A GIS-based fuzzy decision making model for seismic vulnerability assessment in areas with incomplete data. ISPRS International Journal of Geo-Information, 6(4), Article 119. https://doi.org/10.3390/ijgi6040119

Sánchez-Garrido, A. J., & Yepes, V. (2020). Multi-criteria assessment of alternative sustainable structures for a self-promoted, single-family home. Journal of Cleaner Production, 258, Article 120556.

Sánchez-Garrido, A. J., Navarro, I. J., & Yepes, V. (2021). Neutrosophic multi-criteria evaluation of sustainable alternatives for the structure of single-family homes. Environmental Impact Assessment Review, 89, Article 106572. https://doi.org/10.1016/j.eiar.2021.106572

Sánchez-Garrido, A. J., Navarro, I. J., & Yepes, V. (2022). Multi-criteria decision-making applied to the sustainability of building structures based on modern methods of construction. Journal of Cleaner Production, 330, Article 129724. https://doi.org/10.1016/j.jclepro.2021.129724

Sangiorgio, V., Uva, G., & Fatiguso, F. (2018a). Optimized AHP to overcome limits in weight calculation: Building performance application. Journal of Construction Engineering and Management, 144(2), Article 04017101. https://doi.org/10.1061/(ASCE)CO.1943-7862.0001418

Sangiorgio, V., Uva, G., & Fatiguso, F. (2018b). User reportingbased semeiotic assessment of existing building stock at the regional scale. Journal of Performance of Constructed Facilities, 32(6), Article 04018079. 94227

Sangiorgio, V., Martiradonna, S., Fatiguso, F., & Uva, G. (2020a). AHP-based methodology integrating modern information

technologies for historical masonry churches diagnosis. Archeologia e Calcolatori, 31(2), 257–268. https://doi.org/10.19282/ac.31.2.2020.24

Sangiorgio, V., Uva, G., & Aiello, M. A. (2020b). A multi-criteriabased procedure for the robust definition of algorithms aimed at fast seismic risk assessment of existing RC buildings. Structures, 24, 766–782. https://doi.org/10.1016/j.istruc.2020.01.048

Sangiorgio, V., Uva, G., & Adam, J. M. (2021). Integrated seismic vulnerability assessment of historical masonry churches including architectural and artistic assets based on macro-element approach. International Journal of Architectural Heritage, 15(11), 1609–1622. https://doi.org/10.1080/15583058.2019.1709916

Santa-Cruz, S., Cordova-Arias, C., Brioso, X., & Vazquez-Rowe, I. (2021). Transparency-based protocol for decision-making regarding seismic rehabilitation projects of public buildings. International Journal of Disaster Risk Reduction, 55, Article 102116. https://doi.org/10.1016/j.ijdrr.2021.102116

Santarsiero, G., Masi, A., Manfredi, V., & Ventura, G. (2021). Requalification of RC frame apartment buildings: Comparison of seismic retrofit solutions based on a multi-criteria approach. Sustainability, 13(17), Article 9962. https://doi.org/10.3390/su13179962

Selvan, S. U., Saroglou, S. T., Joschinski, J., Calbi, M., Vogler, V., Barath, S., & Grobman, Y. J. (2023). Toward multi-species building envelopes: A critical literature review of multi-criteria decisionmaking for design support. Building and Environment, 231, Article 110006. https://doi.org/10.1016/j.buildenv.2023.110006

Shahriar, A., Modirzadeh, M., Sadiq, R., & Tesfamariam, S. (2012). Seismic induced damageability evaluation of steel buildings: a Fuzzy-TOPSIS method. Earthquakes and Structures, 3(5), 695– 717. https://doi.org/10.12989/eas.2012.3.5.695

Sierra, L. A., Yepes, V., & Pellicer, E. (2018). A review of multi-criteria assessment of the social sustainability of infrastructures. Journal of Cleaner Production, 187, 496–513. https://doi.org/10.1016/j.jclepro.2018.03.022

Sinha, N., Priyanka, N., & Joshi, P. K. (2016). Using Spatial multicriteria analysis and ranking tool (SMART) in earthquake risk assessment: A case study of Delhi region, India. Geomatics Natural Hazards & Risk, 7(2), 680–701. https://doi.org/10.1080/19475705.2014.945100

Stanujkic, D., Popovic, G., Karabasevic, D., Meidute-Kavaliauskiene, I., & Ulutas, A. (2023). An integrated simple weighted sum product method-WISP. IEEE Transactions on Engineering Management, 70(5), 1933–1944. https://doi.org/10.1109/TEM.2021.3075783

Tartaglia, R., Milone, A., D’Aniello, M., & Landolfo, R. (2022). Retrofit of non-code conforming moment resisting beam-to-column joints: A case study. Journal of Constructional Steel Research, 189, Article 107095. https://doi.org/10.1016/j.jcsr.2021.107095

Terracciano, G., Di Lorenzo, G., Formisano, A., & Landolfo, R. (2015). Cold-formed thin-walled steel structures as vertical addition and energetic retrofitting systems of existing masonry buildings. European Journal of Environmental and Civil Engineering, 19(7), 850–866. https://doi.org/10.1080/19648189.2014.974832

Tesfamariam, S., Sadiq, R., & Najjaran, H. (2010). Decision making under uncertainty – An example for seismic risk management. Risk Analysis, 30(1), 78–94. https://doi.org/10.1111/j.1539-6924.2009.01331.x

Usman Kaoje, I., Abdul Rahman, M. Z., Idris, N. H., Razak, K. A., Wan Mohd Rani, W. N. M., Tam, T. H., & Mohd Salleh, M. R. (2021). Physical flood vulnerability assessment using geospatial indicator-based approach and participatory analytical hi-

erarchy process: A case study in Kota Bharu, Malaysia. Water, 13(13), Article 1786. https://doi.org/10.3390/w13131786

Uva, G., Sangiorgio, V., Ruggieri, S., & Fatiguso, F. (2019). Structural vulnerability assessment of masonry churches supported by user-reported data and modern Internet of Things (IoT). Measurement, 131, 183–192. https://doi.org/10.1016/j.measurement.2018.08.014

Vahdat, K., Smith, N. J., & Amiri, G. G. (2014). Fuzzy multicriteria for developing a risk management system in seismically prone areas. Socio-Economic Planning Sciences, 48(4), 235–248. https://doi.org/10.1016/j.seps.2014.05.002

Vázquez-Rowe, I., Córdova-Arias, C., Brioso, X., & Santa-Cruz, S. (2021). A method to include life cycle assessment results in Choosing by Advantage (CBA) multicriteria decision analysis. A case study for seismic retrofit in Peruvian primary schools. Sustainability, 13(15), Article 8139. https://doi.org/10.3390/su13158139

Vona, M., Anelli, A., Mastroberti, M., Murgante, B., & Santa-Cruz, S. (2017). Prioritization strategies to reduce the seismic risk of the public and strategic buildings. Disaster Advances, 10(4), 1–15.

Wen, Z., Liao, H., Zavadskas, E. K., & Antuchevicienc, J. (2021). Applications of fuzzy multiple criteria decision making methods in civil engineering: A state-of-the-art survey. Journal of Civil Engineering and Management, 27(6), 358–371. https://doi.org/10.3846/jcem.2021.15252

Yariyan, P., Zabihi, H., Wolf, I. D., Karami, M., & Amiriyan, S. (2020). Earthquake risk assessment using an integrated fuzzy analytic hierarchy process with artificial neural networks based on GIS: A case study of Sanandaj in Iran. International Journal of Disaster Risk Reduction, 50, Article 101705. https://doi.org/10.1016/j.ijdrr.2020.101705

Zavadskas, E. K., Govindan, K., Antucheviciene, J., & Turskis, Z. (2016). Hybrid multiple criteria decision-making methods: A review of applications for sustainability issues. Economic Research-Ekonomska Istrazivanja, 29(1), 857–887. https://doi.org/10.1080/1331677X.2016.1237302

Zavadskas, E. K., Antucheviciene, J., Vilutiene, T., & Adeli, H. (2018). Sustainable decision-making in civil engineering, construction and building technology. Sustainability, 10(1), Article 14. https://doi.org/10.3390/su10010014

Zavadskas, E. K., Antucheviciene, J., Hosseini, M. R., & Martek, I. (2021). Sustainable construction engineering and management. Sustainability, 13(23), Article 13028. https://doi.org/10.3390/su132313028

Zhen, Y., Liu, S., Zhong, G., Zhou, Z., Liang, J., Zheng, W., & Fang, Q. (2022). Risk assessment of flash flood to buildings using an indicator-based methodology: A case study of mountainous rural settlements in Southwest China. Frontiers in Environmental Science, 10. https://doi.org/10.3389/fenvs.2022.931029

Zhu, X., Meng, X., & Zhang, M. (2021). Application of multiple criteria decision making methods in construction: A systematic literature review. Journal of Civil Engineering and Management, 27(6), 372–403. https://doi.org/10.3846/jcem.2021.15260

Zhu, J., Zhang, Y., Zhang, J., Chen, Y., Liu, Y., & Liu, H. (2023). Multicriteria seismic risk assessment based on Combined Weight-TOPSIS model and CF-Logistic regression model – A case study of Songyuan City, China. Sustainability, 15(14), Article 11216. https://doi.org/10.3390/su151411216

Zuluaga, S. S., Kallioras, S., & Tsiavos, A. (2022). Optimization of synergetic seismic and energy retrofitting based on timber beams and bio-based infill panels: Application to an existing masonry building in Switzerland. Buildings, 12(8), Article 1126. https://doi.org/10.3390/buildings12081126