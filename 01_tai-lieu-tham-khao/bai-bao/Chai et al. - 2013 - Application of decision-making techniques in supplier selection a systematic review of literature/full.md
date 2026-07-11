# Application of decision-making techniques in supplier selection: A systematic review of literature

Junyi Chai <sup>a,</sup>⇑, James N.K. Liu <sup>a</sup>, Eric W.T. Ngai <sup>b</sup>

<sup>a</sup> Department of Computing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong Special Administrative Region <sup>b</sup> Department of Management & Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong Special Administrative Region

## a r t i c l e i n f o

Keywords: Supplier selection Decision-making techniques Uncertainty Literature review

## a b s t r a c t

Despite the importance of decision-making (DM) techniques for construction of effective decision models for supplier selection, there is a lack of a systematic literature review for it. This paper provides a systematic literature review on articles published from 2008 to 2012 on the application of DM techniques for supplier selection. By using a methodological decision analysis in four aspects including decision problems, decision makers, decision environments, and decision approaches, we finally selected and reviewed 123 journal articles. To examine the research trend on uncertain supplier selection, these articles are roughly classified into seven categories according to different uncertainties. Under such classification framework, 26 DM techniques are identified from three perspectives: (1) Multicriteria decision making (MCDM) techniques, (2) Mathematical programming (MP) techniques, and (3) Artificial intelligence (AI) techniques. We reviewed each of the 26 techniques and analyzed the means of integrating these techniques for supplier selection. Our survey provides the recommendation for future research and facilitates knowledge accumulation and creation concerning the application of DM techniques in supplier selection.

\- 2012 Elsevier Ltd. All rights reserved.

## 1. Introduction

Supplier selection (SS) has received considerable attention for its significant effect toward successful Logistic and supply chain management (LSCM). At least two valuable academic surveys had well reviewed the literature on SS. Jain, Wadhwa, and Deshmukh (2009) reviewed the main approaches to supplier-related issues including SS, supplier–buyer relationships, and supplier–buyer flexibility in relationships based on a summary of existing research before 2007. Ho, Xu, and Dey (2010) analyzed multicriteria decision making (MCDM) approaches for SS based on journal articles from 2000 to 2008. However, great developments on SS have emerged over the last five years. A large number of new ideas, techniques, and approaches have been contributing to this promising area. Previous surveys are not keeping pace. Therefore, we believe that a new and systematic survey is useful for consolidating the most recent research efforts on this area.

In this paper, we comprehensively collected the literature associated with the descriptors ‘‘supplier selection,’’ ‘‘vendor selection,’’ and ‘‘decision making’’ from academic databases including Science Direct, Emerald, Springer-Link Journals, IEEE Xplore, Academic

Search Premier, and World Scientific Net. After a methodological decision analysis of all collected articles, we reviewed 123 international journal articles published from 2008 to 2012. We attempt to answer the following four questions: (1) Which decision-making (DM) techniques have frequently been applied? (2) What are the relationships and categories among these DM techniques? (3) How can the DM techniques discussed in literature be effectively integrated to achieve complex decision goals? (4) What are the development status and research trends for uncertain SS?

The emerging trend in current research is the integration of DM techniques in constructing an effective decision model to address practical and complex SS problems, particularly for the consideration of multitudinous uncertainty factors. Given the diversity and the complexity of SS research, we particularly use a methodological decision analysis framework for the selection of the collected articles. This framework provides a guide for the analysis of the literature based on four aspects: (1) decision problems, (2) decision makers, (3) decision environments, and (4) decision approaches. First, we confine our survey on structural SS and thus eliminate the literature that discusses semi-structural or non-structural decision problems. Consequently, a total of 123 articles are selected for detailed review. Second, the literature that involves multiple decision makers as a group is specifically indicated as reference for readers. Third, we classify the selected articles into seven categories after a decision environment analysis. Fourth, the emerging decision approaches are investigated in detail. Specifically, 26 DM techniques are independently reviewed from three perspectives: MCDM techniques, mathematical programming (MP) techniques, and artificial intelligence (AI) techniques. Major integrated approaches are separately reviewed. These approaches include the integrated analytic hierarchy process (AHP), integrated analytic network process (ANP), integrated data envelopment analysis (DEA), and integrated uncertain approaches, among others.

The remainder of this paper is organized as follows: Section 2 presents the research methodology. This section describes the methods for selecting the literature. In Section 3, we use a methodological decision analysis model to sort the selected articles and then subsequently form a summary table. Section 4 provides a detailed literature review on the DM techniques. Section 5 gives suggestions for future works. We conclude this paper in Section 6.

## 2. Research methodology

The research methodology of this survey is depicted in Fig. 1. Our initial objective is to investigate the applications of DM techniques in current research on SS. Thus, we define the following conditions to limit our collection of the articles:

1. Only articles that had been published on decision sciences, computer sciences, or business management-related fields were selected because such articles are most possibly in accordance with the focus of this survey. The articles were searched from academic databases including Science Direct, Emerald, Springer-Link Journals, IEEE Xplore, Academic Search Premier, and World Scientific Net.

2. The keywords for our search were ‘‘supplier selection,’’ ‘‘vendor selection,’’ ‘‘decision making,’’ and so on. Only the literature that had been published between 2008 and 2012 was adopted.

3. To achieve the highest level of relevance, only international journal articles were selected to serve the related research communities better. Thus, conference articles, master and doctoral dissertations, textbooks, unpublished articles, and notes are not included in this review.

Based on these considerations, more than 300 articles were collected. These articles refer to (1) structural, semi-structural, and non-structural DM problems; (2) individual and group-involved DM problems; and (3) certain and uncertain DM problems. Each article was carefully reviewed and selected strictly according to our scope by using a methodological decision analysis model (see Section 3). Consequently, a total of 123 articles were identified as suitable for our survey. In the next section, we aim to provide a summarization of the selected articles. The details of the reviews are presented in Section 4.

## 3. Methodological decision analysis

SS is a typical DM activity. Considering its diversity and complexity, we establish a methodological decision analysis model for a standardized analysis of all collected articles. This model contains four analytic aspects: (1) decision problems, (2) decision makers, (3) decision environments, and (4) decision approaches.

## 3.1. Decision problem analysis

The first step in scientific decision analysis is to model the practical decision problem with a clear formulation. In this sense, problems can be modeled as any of the following three types: structural, non-structural, and semi-structural. Structural problems reveal a well-organized formulation, such as highly structured information tables, measurable decision goals, and clear problem boundaries. Both non-structural and semi-structural problems are mostly at the strategic management level. In these problems, decision information usually lacks organization or is non-quantitative. More importantly, human perception and judgment play decisive roles, although such human factors are usually intangible or unmeasurable. These three types of modeled decision problems are often found in the literature.

In this survey, we mainly focus on the application of DM techniques for structural SS. Thus, the literature that discusses nonstructural and semi-structural problems are not considered in this survey. The interested reader can refer to the related literature for details. For example, Shen and Yu (2009), Shen and Yu (2012) formulated SS as a semi-structural problem. Ordoobadi and Wang (2011) as well as Wu (2009c) formulated SS as a non-structural problem.

## 3.2. Decision maker analysis

Decisions can be made by individuals. For example, an investor can decide on which stock to buy by considering the rate of return. Large complex decisions, particularly at high managerial levels, usually involve multiple decision makers who need to work effectively in groups. Therefore, dealing with often conflicting objectives, inconsistent judgments, and incompatible opinions is a challenge in group DM settings.

For structural SS, multiple experts are usually involved as decision makers. The common scenario is that qualified experts need to provide their professional evaluations on alternative suppliers according to given criteria. Different weights are set for each expert according to their profession, expertise, qualification, or experience. In any case, the key step in DM processes is information fusion, for example, the weighted average or the ordered weighted average. In this survey, we specify the literature that involves group DMs as reference for readers (see Table 1).

## 3.3. Decision environment analysis

In a broad sense, decision environments contain decision goals, decision principles, available resources, and possible uncertainties. For SS, a number of studies formulated the addressed DM problems in terms of deterministic conditions without considering any involved uncertainties. Nevertheless, recent research tends to cater to more practical SS problems via uncertainty hybrid approaches. According to our reviews on the selected articles from 2008 to 2012, the dominant method is multitudinous fuzzy hybridization. We can roughly group these methods into the following five categories: (1) basic concept of fuzzy logic, (2) triangular fuzzy sets, (3) trapezoidal fuzzy sets, (4) intuitionistic fuzzy sets, and (5) intervalvalued intuitionistic fuzzy sets. Moreover, a number of non-fuzzy uncertain formulations also emerged, including stochastic and probabilistic formulations as well as incomplete and imprecise decision information.

## 3.4. Decision approaches analysis

A decision approach is understood as a complete problem-solving model (also called scheme or solution) that is capable of effectively achieving the stated decision goals. In today’s global market, SS has become a very important activity in LSCM. Given the complexity of the process in the real world, current research tends to integrate multiple DM techniques in establishing a decision model. Different techniques can separately deal with the corresponding sub-problems, thus improving the performance of the whole decision approach significantly.

Along with the rapid growth of practical demand and the development of information techniques in past decades, current studies have directed more attention to addressing uncertain SS via unconventional means under non-classical assumptions or nondeterministic conditions. For this reason, we roughly classify all selected articles into seven categories based on different decision environments. These categories are defined as follows:

![](images/56215a4a6e30aef92fe04506c02c510fd156ee66aa98f99fe8e5ffade13edab1.jpg)  
Fig. 1. Research methodology of this survey.

(1) Certain DM: This category includes classical assumptions, deterministic conditions, certain decision environments, and conventional means.

(2) Basic fuzzy logic hybridization: This category includes Zadeh’s fuzzy sets, fuzzy logic, basic fuzzy values, and classical fuzzy preference relations.

(3) Triangular fuzzy hybridization: This category includes triangular fuzzy values and triangular fuzzy preference relations.

(4) Trapezoidal Fuzzy Hybridization: This category includes trapezoidal fuzzy values and trapezoidal fuzzy preference relations.

(5) Intuitionistic fuzzy hybridization: This category includes intuitionistic fuzzy values, intuitionistic fuzzy preference relations, and vague values [vague sets are intuitionistic fuzzy sets that had been proven by Bustince and Burillo (1996)].

(6) Interval-valued intuitionistic fuzzy hybridization: This category includes interval-valued intuitionistic fuzzy values and interval-valued intuitionistic fuzzy preference relations.

(7) Non-fuzzy hybrid uncertain DM: This category includes stochastic, probabilistic and grey-valued formulations, as well as incomplete and imprecise decision information.

Summarization of the decision approaches with respect to DM techniques.

<table><tr><td>Approaches</td><td>Literature</td><td>Core DM techniques</td><td>Additional features of decision approaches</td></tr><tr><td>Certain</td><td>Levary (2008)</td><td>AHP</td><td>Reliability chain</td></tr><tr><td>Decision</td><td>Chan and Chan (2010)</td><td>AHP</td><td>AHP model for apparel industry</td></tr><tr><td rowspan="30">Approaches</td><td>Mafakheri et al. (2011)</td><td>AHP</td><td>Two-stage dynamic programming</td></tr><tr><td>Ishizaka et al. (2012).</td><td>AHP</td><td>AHP-based sorting approach</td></tr><tr><td>Kull and Talluri (2008)</td><td>AHP, GP</td><td>Product life cycle consideration</td></tr><tr><td>Bhattacharya et al. (2010)</td><td>AHP</td><td>Cost factor measure; QFD technique</td></tr><tr><td>Ordoobadi (2010)</td><td>AHP</td><td>Taguchi loss function (TLF)</td></tr><tr><td>Üstün and Demirtas (2008)</td><td>ANP, LP</td><td>Benefit, opportunity, cost, and risk model</td></tr><tr><td>Demirtas and Üstün (2008)</td><td>ANP, LP</td><td>Benefit, opportunity, cost, and risk model</td></tr><tr><td>Demirtas and Üstün (2009)</td><td>ANP, GP, LP</td><td>Benefit, opportunity, cost, and risk model</td></tr><tr><td>Lin et al. (2010)</td><td>ANP</td><td>Interpretive structural modeling for wafer testing</td></tr><tr><td>Lin et al. (2011)</td><td>ANP, TOPSIS, LP</td><td>Case study related to manufacturing enterprise</td></tr><tr><td>Tseng et al. (2009)</td><td>ANP</td><td>Choquet integral</td></tr><tr><td>Razmi and Rafiei (2010)</td><td>ANP, NLP</td><td>Mixed integer NLP</td></tr><tr><td>Ho et al. (2011)</td><td>ANP</td><td>Integrated approach; QFD technique</td></tr><tr><td>Wu (2009a)</td><td>DEA, DT, NN</td><td>A hybrid model for classification and prediction</td></tr><tr><td>Wu and Blackhurst (2009)</td><td>DEA</td><td>An augmented DEA approach</td></tr><tr><td>Toloo and Nalchigar (2011)</td><td>DEA, LP</td><td>Regarding both cardinal and ordinal data</td></tr><tr><td>Falagario et al. (2012)</td><td>DEA</td><td>Regarding the case of public procurement tenders</td></tr><tr><td>Ng (2008)</td><td>LP</td><td>A simple weighted LP</td></tr><tr><td>Feng et al. (2011)</td><td>MOP</td><td>Collaborative utility; Tabu search based algorithm</td></tr><tr><td>Che (2010a)</td><td>GA</td><td>Guided-Pareto GA; Multi-period SS</td></tr><tr><td>Yeh and Chuang (2011)</td><td>GA, MOP, NLP</td><td>Multiobjective mixed integer NLP</td></tr><tr><td>Rezaei and Davoodi (2012)</td><td>GA, MOP, NLP</td><td>Multiobjective mixed integer NLP</td></tr><tr><td>Vahdani et al. (2010)</td><td>ELECTRE</td><td>Extend ELECTRE for interval values</td></tr><tr><td>Liu and Zhang (2011)</td><td>ELECTRE</td><td>Combine entropy weight and ELECTRE-III</td></tr><tr><td>Lee and Ouyang (2009)</td><td>NN</td><td>NN-based predictive model; Negotiation process</td></tr><tr><td>Guo et al. (2009)</td><td>SVM, DT</td><td>Hierarchical potential SVM method</td></tr><tr><td>Chang and Hung (2010)</td><td>RST</td><td>Rule-based approach</td></tr><tr><td>Zhao and Yu (2011)</td><td>CBR</td><td>(Group) Information entropy; Petroleum enterprises</td></tr><tr><td>Lin et al. (2009)</td><td>AR</td><td>Combination of association rule and set theory</td></tr><tr><td>Tsai et al. (2010)</td><td>ACA</td><td>Attribute-based ant colony system</td></tr><tr><td rowspan="16">Basic Fuzzy Hybrid Approaches</td><td>Sevkli et al. (2008)</td><td>AHP, LP</td><td>AHP weighted fuzzy logic hybridization</td></tr><tr><td>Wang and Yang (2009)</td><td>AHP, MOP, LP,</td><td>Fuzzy compromise programming</td></tr><tr><td>Tsai and Hung (2009)</td><td>AHP, GP</td><td>Fuzzy GP; Green SCM</td></tr><tr><td>Labib (2011)</td><td>AHP</td><td>Fuzzy linguistic expression; Fuzzy logic</td></tr><tr><td>Amid, Ghodsypour, and O'Brien (2011)</td><td>AHP</td><td>Weighted max-min fuzzy decision model</td></tr><tr><td>Chen and Chao (2012)</td><td>AHP</td><td>Consistent fuzzy preference relations</td></tr><tr><td>Chamodrakas et al. (2010).</td><td>AHP</td><td>Fuzzy AHP; Interval valued pairwise comparison</td></tr><tr><td>Lin (2012)</td><td>ANP, MOP, LP</td><td>Fuzzy multi-objective LP</td></tr><tr><td>Amid, Ghodsypour, and O'Brien (2009)</td><td>MOP</td><td>A weighted additive fuzzy MOP</td></tr><tr><td>Ozkok and Tiryaki (2011)</td><td>MOP</td><td>Compensatory fuzzy approach</td></tr><tr><td>Keskin et al. (2010)</td><td>NN</td><td>Fuzzy adaptive resonance theory, clustering</td></tr><tr><td>Güneri, Ertay, &amp; Yücel (2011)</td><td>NN</td><td>Utilization of Adaptive neuro-fuzzy inference system</td></tr><tr><td>Wang (2008)</td><td>GA</td><td>Configuration change assessment</td></tr><tr><td>Wu (2009b)</td><td>GST, DST</td><td>(Group) Grey relational analysis</td></tr><tr><td>Crispim and De Sousa (2010)</td><td>TOPSIS</td><td>Fuzzy values; regarding virtual enterprises</td></tr><tr><td>Xu and Yan (2011)</td><td>PSO</td><td>Level-2 fuzzy values</td></tr><tr><td rowspan="24">Triangular Fuzzy Hybrid Approaches</td><td>Chan et al. (2008)</td><td>AHP</td><td>Global supplier selection</td></tr><tr><td>Bottani and Rizzi (2008)</td><td>AHP</td><td>AHP-based clustering technique</td></tr><tr><td>Yang et al. (2008)</td><td>AHP</td><td>Non-additive fuzzy integral</td></tr><tr><td>Lee (2009a)</td><td>AHP</td><td>Benefit, opportunity, cost, and risk model</td></tr><tr><td>Lee (2009b)</td><td>AHP</td><td>Benefit, opportunity, cost, and risk model</td></tr><tr><td>Lee et al. (2009)</td><td>AHP, GP</td><td>Multiple goal programming</td></tr><tr><td>Wang et al. (2009)</td><td>AHP, TOPSIS</td><td>A fuzzy hierarchical TOPSIS</td></tr><tr><td>Che (2010b)</td><td>AHP, PSO</td><td>Green SCM</td></tr><tr><td>Şen et al. (2010)</td><td>AHP</td><td>Max-min method</td></tr><tr><td>Kilinci and Onal (2011)</td><td>AHP</td><td>Fuzzy AHP; Regarding washing machine companies</td></tr><tr><td>Punniyamoorthy et al. (2011)</td><td>AHP</td><td>Structural equation modeling (SEM)</td></tr><tr><td>Yucenur et al. (2011)</td><td>AHP, ANP</td><td>Linguistic variables</td></tr><tr><td>Zeydan et al. (2011)</td><td>AHP, TOPSIS, DEA</td><td>(Group) Integration of multiple techniques</td></tr><tr><td>Shaw et al. (2012)</td><td>AHP, MOP</td><td>Low carbon SCM</td></tr><tr><td>Yu et al. (2012)</td><td>AHP, MOP</td><td>Soft time window</td></tr><tr><td>Razmi et al. (2009a)</td><td>ANP, NLP</td><td>Network formation and pairwise comparisons</td></tr><tr><td>Amin and Razmi (2009)</td><td>ANP</td><td>Case study; QFD technique</td></tr><tr><td>Onüt et al. (2009)</td><td>ANP, TOPSIS</td><td>Regarding telecommunication industries</td></tr><tr><td>Vinodh et al. (2011)</td><td>ANP</td><td>Regarding manufacturing industries</td></tr><tr><td>Buyukozkan and Cifci (2012)</td><td>ANP, TOPSIS, DEMATEL</td><td>Green SCM</td></tr><tr><td>Azadeh and Alem (2010)</td><td>DEA, TOPSIS</td><td>Regarding environmental performance of suppliers</td></tr><tr><td>Chen (2011b)</td><td>DEA, TOPSIS</td><td>Strengths, Weakness, Opportunities, Threats model</td></tr><tr><td>Razmi et al. (2009b)</td><td>TOPSIS, LP</td><td>(Group) fuzzy TOPSIS integrated with fuzzy LP</td></tr><tr><td>Hsu et al. (2010)Singh, Kumar, and Gupta (2010)</td><td>NLPLP</td><td>Fuzzy preference relationsFuzzy statistical method</td></tr><tr><td rowspan="16"></td><td>Haleh and Hamidi (2011)</td><td>MOP, LP</td><td>Regarding multi-period time horizon</td></tr><tr><td>Amin and Zhang (2012)</td><td>MOP, LP</td><td>(Group) Multiobjective mixed integer LP</td></tr><tr><td>Kara (2011)</td><td>SP, TOPSIS</td><td>Fuzzy TOPSIS</td></tr><tr><td>Amin et al. (2011)</td><td>SWOT, LP</td><td>(Group) Fuzzy SWOT model</td></tr><tr><td>Awasthi, Chauhan, and Goyal (2010)</td><td>TOPSIS</td><td>Environmental performance</td></tr><tr><td>Deng and Chan (2011)</td><td>TOPSIS</td><td>(Group) Dempster Shafer Theory of evidence</td></tr><tr><td>Dalalah et al. (2011)</td><td>TOPSIS, DEMATEL</td><td>(Group) Fuzzy DEMATEL; Causal diagram</td></tr><tr><td>Montazer et al. (2009)</td><td>ELECTRE</td><td>Fuzzy ELECTRE-III</td></tr><tr><td>Sevkli (2010)</td><td>ELECTRE</td><td>Linguistic variable</td></tr><tr><td>Chen et al. (2011)</td><td>PROMETHEE</td><td>(Group) Fuzzy PROMETHEE; Case study</td></tr><tr><td>Chang et al. (2011)</td><td>DEMATEL</td><td>Fuzzy DEMATEL; Evaluate performance</td></tr><tr><td>Chen and Wang (2009)</td><td>VIKOR</td><td>Fuzzy VIKOR</td></tr><tr><td>Chou and Chang (2008)</td><td>SMART</td><td>(Group) Fuzzy SMART</td></tr><tr><td>Tseng (2011)</td><td>GST</td><td>Integrating grey degrees and fuzzy system; Green SCM</td></tr><tr><td>Golmohammadi and Mellat-Parast (2012)</td><td>GST</td><td>(Group) Grey relational analysis</td></tr><tr><td>Vahdani and Zandieh (2010)</td><td>***</td><td>A fuzzy balancing and ranking method</td></tr><tr><td>Trapezoidal</td><td>Guneri et al. (2009)</td><td>TOPSIS, LP</td><td>LP model under fuzzy environments</td></tr><tr><td rowspan="9">Fuzzy Hybrid Approaches</td><td>Faez, Ghodsypour, and O'Brien (2009)</td><td>CBR</td><td>Fuzzy CBR approach</td></tr><tr><td>Yucel and Güneri (2011)</td><td>TOPSIS, LP</td><td>(Group) Weighted additive fuzzy programming</td></tr><tr><td>Liao and Kao (2011)</td><td>TOPSIS, GP</td><td>(Group) Multi-choice goal programming</td></tr><tr><td>Sanayei et al. (2010)</td><td>VIKOR</td><td>(Group) Linguistic variables expression</td></tr><tr><td>Shemshadi et al. (2011)</td><td>VIKOR</td><td>(Group) Linguistic terms; Entropy</td></tr><tr><td>Ferreira and Borenstein (2012)</td><td>BN</td><td>(Group) Fuzzy Bayesian model; Influence diagrams</td></tr><tr><td>Wu et al. (2010)</td><td>MOP</td><td>Possibility fuzzy hybridization; Risk analysis</td></tr><tr><td>Ordoobadi (2009)</td><td>***</td><td>Fuzzy arithmetic operators</td></tr><tr><td>Amindoust, Ahmed, Saghafinia, and Bahreininejad (2012)</td><td>***</td><td>(Group) Fuzzy inference system</td></tr><tr><td>Intuitionistic</td><td>Boran, Genç, Kurt, and Akay (2009)</td><td>TOPSIS</td><td>(Group) Intuitionistic fuzzy information aggregation</td></tr><tr><td rowspan="5">Fuzzy Hybrid Approaches</td><td>Chai, Liu, &amp; Xu (2012)</td><td>PROMETHEE</td><td>Extended superiority and inferiority ranking approach</td></tr><tr><td>Chen (2011a)</td><td>LP, GP</td><td>Optimism-pessimism model; Net predisposition; An integrated programming model</td></tr><tr><td>Khaleie, Fasanghari, and Tavassoli (2012)</td><td>***</td><td>(Group) Intuitionistic fuzzy clustering; Intuitionistic fuzzy information fusion</td></tr><tr><td>Zhang, Zhang, Lai, and Lu (2009)</td><td>***</td><td>(Group) Linguistic variables converted to vague sets</td></tr><tr><td>Khaleie and Fasanghari (2012)</td><td>***</td><td>(Group) Intuitionistic fuzzy information entropy; Association coefficient</td></tr><tr><td>Interval valued</td><td>Wang, Li, and Xu (2011)</td><td>TOPSIS, FP</td><td>Quadratic and fractional programming</td></tr><tr><td>Intuitionistic fuzzy hybrid approaches</td><td>Chen et al. (2011)</td><td>LP</td><td>(Group) Interval-valued intuitionistic fuzzy preference relations</td></tr><tr><td>Non-Fuzzy</td><td>Pitchipoo et al. (2012)</td><td>AHP, GST</td><td>Regarding chemical processing industries</td></tr><tr><td>Uncertain</td><td>Wu (2010)</td><td>DEA</td><td>Stochastic DEA</td></tr><tr><td rowspan="14">Hybrid Approaches</td><td>Saen (2008)</td><td>DEA</td><td>Assurance region-imprecise DEA</td></tr><tr><td>Saen (2010)</td><td>DEA</td><td>Regarding undesirable outputs and imprecise data</td></tr><tr><td>Wu and Olson (2008a)</td><td>DEA</td><td>Stochastic DEA; Stochastic uncertainty environments</td></tr><tr><td>Wu and Olson (2008b)</td><td>DEA, MOP</td><td>Chance-constrained programming; Monte Carlo simulation</td></tr><tr><td>Celebi and Bayraktar (2008)</td><td>DEA, NN</td><td>Regarding incomplete information of criteria</td></tr><tr><td>Xu and Ding (2011)</td><td>GA, MOP, LP</td><td>Chance-constrained MOLP model</td></tr><tr><td>Li and Zabinsky (2011)</td><td>SP</td><td>Chance-constrained programming model</td></tr><tr><td>Zhang and Ma (2009)</td><td>NLP</td><td>General algebraic; Regarding demand uncertainty</td></tr><tr><td>Li et al. (2008)</td><td>RST, GST</td><td>(Group) Grey relational analysis</td></tr><tr><td>Bai and Sarkis (2010)</td><td>RST, GST</td><td>(Group) Grey values; Sustainability</td></tr><tr><td>Sadeghieh et al. (2012)</td><td>GA, GST, GP</td><td>(Group) A GA-based grey goal programming approach</td></tr><tr><td>Lin and Yeh (2010)</td><td>GA</td><td>Stochastic logistic network</td></tr><tr><td>Yang et al. (2011)</td><td>GA</td><td>Stochastic model</td></tr><tr><td>Dogan and Aydin (2011)</td><td>BN</td><td>Total cost of ownership</td></tr></table>

The mark ‘‘⁄⁄⁄’’ means that no particular Core DM Techniques need to be emphasized.  
Details of the abbreviations shown in the third column can be obtained in Table 2

Based on these classifications, we provide the overall summary of 26 DM techniques discussed in the 123 selected journal articles in Table 1. We highlight 26 DM techniques, which are listed in the third column of Table 1, in terms of core DM techniques. In the last column of Table 1, we note the additional remarks on the proposed decision approaches for reference by readers. In addition, we indicate the literature that involved group DMs via the term ‘‘Group.’’ The detailed reviews are presented in the next section.

## 4. Categorical reviews of decision-making techniques

Considering the practical complexity of SS. current research tends to integrate multiple DM techniques into a hybrid decision approach. In the beginning of this section, we systematically summarized the 26 DM techniques that had been integrated into the decision approaches discussed in our reviewed literature. We then separately reviewed six kinds of major integrated approaches. These approaches include the integrated AHP approaches in

Section 4.2, the integrated ANP approaches in Section 4.3, the integrated DEA approaches in Section 4.4, the integrated uncertain decision approaches in Section 4.5, and other integrated approaches in Section 4.6.

## 4.1. Overview of independent DM techniques

Based on our investigation, we summarize 26 DM techniques that had been used for supplier evaluation and selection. We classify these techniques into three categories, namely: Multicriteria decision making (MCDM) techniques (Section 4.1.1), Mathematical programming (MP) techniques (Section 4.1.2), and Artificial intelligence (AI) techniques (Section 4.1.3). In Table 2, we provide the names of the techniques and their abbreviations. We provide one representative article for each independent DM technique. Readers can find the typical usage of these techniques in the corresponding articles. In addition, Table 2 shows the distribution of articles based on DM technique.

## 4.1.1. MCDM techniques

MCDM is a methodological framework that aims to provide decision makers a knowledgeable recommendation amid a finite set of alternatives (also known as actions, objects, solutions, or candidates), while being evaluated from multiple viewpoints, called criteria (also known as attributes, features, or objectives). In the literature, the problem of structural SS is usually regarded as MCDM. Therefore, a number of classical MCDM techniques have been employed in problem-solving processes. Based on the principle behind these MCDM techniques, we can classify them into four categories: (1) multiattribute utility methods such as AHP and ANP, (2) outranking methods such as Elimination and Choice Expressing Reality (ELECTRE) and Preference Ranking Organization Method for Enrichment Evaluation (PROMETHEE); (3) compromise methods such as Technique for Order Performance by Similarity to Ideal Solution (TOPSIS) and Multicriteria Optimization and Compromise Solution (VIKOR), and (4) other MCDM techniques such as Simple

Multiattribute Rating Technique (SMART) and Decision-Making Trial and Evaluation Laboratory (DEMATEL).

4.1.1.1. Multiattribute utility methods: AHP and ANP. Multiattribute utility methods essentially attempt to assign a utility value to each alternative. The utility value represents the preference degree that can be the basis for ranking or choice. Both AHP and ANP are wellknown multiattribute utility methodologies. AHP uses pairwise comparisons along with expert judgments to handle the measurement of qualitative or intangible attributes. As an extension of AHP, ANP is a general theory of relative intangible attribute measurement. AHP and ANP remain the most important and commonly used components that constitute up-to-date decision approaches for SS. AHP and ANP are reviewed in Sections 4.2 and 4.3, respectively.

4.1.1.2. Outranking methods: ELECTRE and PROMETHEE. On the premise of known decision-makers’ preference and evaluation values of alternatives (e.g. suppliers), an outranking relation is a binary relation S defined on the set of potential alternatives such that aSb if sufficient justification exists to decide that alternative a is at least as good as alternative b with no essential justification to disprove such statement (Figueira, Greco, & Ehrgott, 2005). The ELECTRE methods strictly follow this definition. The well-known PROMETHEE methods are further based on the situation of a pairwise comparison of alternatives. Six articles that use these two techniques are reviewed in Section 4.6.

4.1.1.3. Compromise methods: TOPSIS and VIKOR. The foundation of compromise methods was established by Yu (1973). A compromise solution is the closest to the ideal solution, and a compromise denotes an agreement on the basis of mutual concessions. As typical compromise programming methods, both TOPSIS and VIKOR are based on an aggregating function that represents closeness to the ideal. The difference is that TOPSIS uses linear normalization to eliminate the units of criteria function, whereas VIKOR uses vector normalization (Opricovic & Tzeng, 2004). In our review, 22 articles employ these two techniques as part of their decision approaches.

Table 2  
The summarization of the used DM techniques.

<table><tr><td>The used DM techniques</td><td>Abbreviation</td><td>Representative literature</td><td>Amount</td><td>Percentage (%)</td></tr><tr><td colspan="5">Multiattribute decision making (MCDM) techniques</td></tr><tr><td>1. Analytic hierarchy process</td><td>AHP</td><td>Levary (2008)</td><td>30</td><td>24.39</td></tr><tr><td>2. Analytic network process</td><td>ANP</td><td>Lin et al. (2010)</td><td>15</td><td>12.20</td></tr><tr><td>3. Elimination and choice expressing reality</td><td>ELECTRE</td><td>Sevkli (2010)</td><td>4</td><td>3.25</td></tr><tr><td>4. Preference ranking organization method for enrichment evaluation</td><td>PROMETHEE</td><td>Chen et al. (2011)</td><td>2</td><td>1.63</td></tr><tr><td>5. Technique for order performance by similarity to ideal solution</td><td>TOPSIS</td><td>Saen (2010)</td><td>18</td><td>14.63</td></tr><tr><td>6. Multicriteria optimization and compromise solution</td><td>VIKOR</td><td>Chen &amp; Wang (2009)</td><td>3</td><td>2.44</td></tr><tr><td>7. Decision making trial and evaluation laboratory</td><td>DEMATEL</td><td>Chang et al. (2011)</td><td>3</td><td>2.44</td></tr><tr><td>8. Simple multiattribute rating technique</td><td>SMART</td><td>Chou &amp; Chang (2008)</td><td>1</td><td>0.81</td></tr><tr><td colspan="5">Mathematical programming (MP) techniques</td></tr><tr><td>1. Data envelopment analysis</td><td>DEA</td><td>Wu &amp; Blackhurst (2009)</td><td>13</td><td>10.57</td></tr><tr><td>2. Linear Programming</td><td>LP</td><td>Lin et al. 2011</td><td>19</td><td>15.44</td></tr><tr><td>3. Nonlinear programming</td><td>NLP</td><td>Hsu et al. (2010)</td><td>6</td><td>4.88</td></tr><tr><td>4. Multiobjective programming</td><td>MOP</td><td>Yu et al. (2012)</td><td>13</td><td>10.57</td></tr><tr><td>5. Goal programming</td><td>GP</td><td>Kull &amp; Talluri (2008)</td><td>7</td><td>5.69</td></tr><tr><td>6. Stochastic programming</td><td>SP</td><td>Li and Zabinsky (2011)</td><td>2</td><td>1.63</td></tr><tr><td colspan="5">Artificial intelligence (AI) techniques</td></tr><tr><td>1. Genetic algorithm</td><td>GA</td><td>Güneri et al, (2011)</td><td>8</td><td>6.50</td></tr><tr><td>2. Grey system theory</td><td>GST</td><td>Tseng (2011), Wu (2009b)</td><td>6</td><td>4.88</td></tr><tr><td>3. Neural networks</td><td>NN</td><td>Lee &amp; Ouyang (2009)</td><td>5</td><td>4.07</td></tr><tr><td>4. Rough set theory</td><td>RST</td><td>Chang &amp; Hung (2010)</td><td>4</td><td>3.25</td></tr><tr><td>5. Bayesian networks</td><td>BN</td><td>Ferreira &amp; Borenstein (2012)</td><td>2</td><td>1.63</td></tr><tr><td>6. Decision tree</td><td>DT</td><td>Guo et al. (2009)</td><td>2</td><td>1.63</td></tr><tr><td>7. Case-based reasoning</td><td>CBR</td><td>Faez, Ghodsypour, &amp; O&#x27;Brien (2009)</td><td>2</td><td>1.63</td></tr><tr><td>8. Particle swarm optimization</td><td>PSO</td><td>Xu &amp; Yan (2011)</td><td>2</td><td>1.63</td></tr><tr><td>9. Support vector machine</td><td>SVM</td><td>Guo et al. (2009)</td><td>1</td><td>0.81</td></tr><tr><td>10. Association rule</td><td>AR</td><td>Lin et al. (2009)</td><td>1</td><td>0.81</td></tr><tr><td>11. Ant colony algorithm</td><td>ACA</td><td>Tsai et al. (2010)</td><td>1</td><td>0.81</td></tr><tr><td>12. Dempster shafer theory of evidence</td><td>DST</td><td>Wu (2009b)</td><td>1</td><td>0.81</td></tr></table>

4.1.1.4. Other MCDM methods: SMART and DEMATEL. SMART is a basic ranking technique that uses the simple additive weight method to obtain total values as the ranking index. This technique can deal with both quantitative and qualitative criteria, but cannot effectively handle uncertain decision information such as linguistic terms, interval values, and various fuzzy values. Chou and Chang (2008) developed the modified SMART approach for SS. In this work, a fuzzy integrated SMART decision model was proposed for a strategy-aligned SS.

DEMATEL is a structural model for analyzing the influential relation among complex evaluation criteria. Three articles use this model as part of the whole decision approach. Buyukozkan and Cifci (2012) used DEMATEL as well as the strength of the interdependence to generate the mutual relationships of interdependencies among criteria. Dalalah, Hayajneh, and Batieha (2011) modified DEMATEL to deal with fuzzy rating and evaluations by converting the relationship between the causes and effects of the criteria into an intelligible structural model. Finally, Chang, Chang, and Wu (2011) designed a fuzzy DEMATEL questionnaire for determining the direct and indirect influence among criteria.

## 4.1.2. MP techniques

MP is a general term in DM research. For selections applications, we specify the following six MP techniques for detailed review.

4.1.2.1. Data Envelopment Analysis (DEA). DEA is a nonparametric MP technique for evaluating the relative efficiency of comparable entities in terms of decision-making units (DMUs). A basic DEA model is a performance measurement that can be used to evaluate the relative efficiency of DMUs according to multiple inputs and outputs (Adler, Friedman, & Sinuany-Stern, 2002). Given its effectiveness, DEA can be a valuable complement to various SS decision models. A total of 13 articles refer to this technique in our reviewed literature. Section 4.4 provides the detailed reviews.

4.1.2.2. Linear programming (LP). LP is a mathematical optimization method for determining a way to achieve the best outcome in a given mathematical model under a number of requirements represented as linear relationships. In our review, the use of LP for SS can be classified into four categories: (1) the simple LP employment (Chen, Wang, & Lu, 2011; Guneri, Yucel, & Ayyildiz, 2009; Lin, Chen, & Ting, 2011; Ng, 2008), (2) the fuzzy LP (Amin, Razmi, & Zhang, 2011; Lin, 2012; Sevkli, 2008; Yucel & Güneri, 2011), (3) The multiobjective LP (MOLP) (Ozkok & Tiryaki, 2011; Xu & Ding, 2011; Yucel & Güneri, 2011), and (4) The mixed integer LP (Amin & Zhang, 2012; Demirtas & Üstün, 2008; Demirtas & Üstün, 2009; Razmi, Songhori, & Khakbaz, 2009b; Toloo & Nalchigar, 2011; Wang & Yang, 2009; Üstün & Demirtas, 2008).

4.1.2.3. Nonlinear programming (NLP). A number of studies modeled practical SS processes into NLP problems and then designed various objective functions and constraints for resolution. In contrast to LP, NLP allows for some of the constraints or objective functions to be nonlinear. Based on our survey, two directions can be defined. First is the simple utilization of NLP as a decision tool. Related literature includes Hsu, Chiang, and Shu (2010) and Razmi, Rafiei, and Hashemi (2009a). The second direction is to model problems by using the mixed integer NLP formulations. Related literature includes Zhang and Ma (2009), Razmi and Rafiei (2010), Yeh and Chuang (2011), as well as Rezaei and Davoodi (2012).

4.1.2.4. Multiobjective programming (MOP). MOP is a kind of MP for decision problems characterized by multiple and conflicting objective functions that can be optimized over a set of feasible solutions. From 2008 to 2012, research on fuzzy MOLP for SS was the mainstream direction. Related literature includes Haleh and Hamidi (2011), Ozkok and Tiryaki (2011), Lin (2012), Yu, Goh, and Lin (2012) Shaw, Shankar, Yadav, and Thakur (2012), as well as Amin and Zhang (2012). Nevertheless, Yeh and Chuang (2011) formulated a mixed integer multiobjective NLP (MONLP) model for partner selection. In addition, Wu, Zhang, Wu, and Olson (2010) studied other possible MOP models. Feng, Fan, and Li (2011) introduced a multiobjective 0–1 programming model. Xu and Ding (2011) developed a chance constrained MOLP model with birandom coefficients.

4.1.2.5. Goal programming (GP). GP is a branch of optimization method. This technique can be regarded as an extension or generalization of MOLP that can be used to deal with multiple and conflicting objective measures. Each of these measures is given a goal value to be achieved. In our literature review, seven constructed GP models for selections were found. The most direct employment of GP as a decision tool is in Kull and Talluri (2008). Tsai and Hung (2009) provided a fuzzy GP approach. Demirtas and Üstün (2009) provided a GP and ANP hybrid decision model considering a mul ti-period planning horizon. Chen (2011a) integrated multiple MP techniques, among which GP is an important component. Sadeghieh, Dehghanbaghi, Dabbaghi, and Barak (2012) developed a genetic algorithm (GA)-based grey GP approach. Finally, Lee, Kang, and Chang (2009) and Liao and Kao (2011) reduced real-world SS problems to a formulation of multi-choice GP.

4.1.2.6. Stochastic programming (SP). SP is a framework for modeling uncertainty optimization problems in which probability distributions governing the data are known or can be estimated despite the involvement of a number of unknown parameters. This technique is a suitable mathematical tool for dealing with several real-world SS problems. Based on our survey, two articles refer to SP, including Kara (2011) as well as Li and Zabinsky (2011). Both of these articles developed two-stage SP decision models. The former consolidated SP and fuzzy TOPSIS methods, whereas the latter integrated SP with chance-constrained LP.

## 4.1.3. AI techniques

In this review, 12 techniques can be regarded as AI techniques. Four of these techniques are major ones: GA, neural network (NN), rough set theory (RST), and grey system theory (GST). This section also summarizes the eight other AI techniques, including casebased reasoning (CBR), Bayesian networks (BN), particle swarm optimization (PSO), ant colony algorithm (ACA), Dempster–Shafe theory (DST), association rule (AR), support vector machine (SVM), and decision tree (DT).

4.1.3.1. Major AI techniques: GA, NN, GST, and RST. GA is a kind of global search technique used to identify approximate solutions for complex optimization problems. Conceptually following the steps of the biological process of evolution, GA is considered a heuristic method considering that it cannot guarantee a truly optimal solution. Eight articles refer to this technique. The literature that considered typical GA for SS includes Yang, Wee, Pai, and Tseng (2011) as well as Yeh and Chuang (2011). Moreover, Xu and Ding (2011) designed a bi-random simulation-based GA. Che (2010a) provided a heuristic algorithm combining guided GA and Pareto GA. Rezaei and Davoodi (2012) formulated an MONLP, applying a non-dominated sorting GA. Three articles, including Wang (2008), Lin and Yeh (2010), as well as Sadeghieh et al. (2012), utilized GA as an element to construct their decision model.

An NN is generally a set of connected input or output units, in which each connection has an associated weight. The weights are adjusted during the learning phase to help the network predict the correct class label for the input objects (Han, Kamber, & Pei, 2012). We found five articles that refer to this technique. The typical NN use was found in the studies of Celebi and Bayraktar (2008) and Wu (2009a). The former study employed NN to refine the general evaluation criteria set into a set of common performance measures, whereas the latter adopted the backpropagation NN for feature extraction and classification. Guneri, Ertay, and Yucel (2011) improved the performance of the adaptive neuro-fuzzy inference system for SS. Keskin, Ilhan, and Özkan (2010) developed a decision approach by using adaptive resonance theory NNs. Both works employed the basic fuzzy logic for hybridization. Lee and Ouyang (2009) provided an NN-based predictive model to forecast the supplier’s bid prices.

GST is a mathematical method that is applied to imprecise information in the form of interval values (Deng, 1989). The reviewed literature introduced GST for SS from two perspectives: (1) decision information in the form of grey values (Bai & Sarkis, 2010; Sadeghieh et al., 2012; Tseng, 2011) and (2) grey relational analysis (GRA) (Golmohammadi & Mellat-Parast, 2012; Li et al., 2008; Pitchipoo, Venkumar, & Rajakarunakaran, 2012; Wu, 2009b).

RST can be used to identify structural relationships within imprecise or noisy data. Classical RST is based on binary indiscernibility relations, which result in the establishment of equivalence classes. In our review, three articles refer to the classical RST, including Bai and Sarkis (2010), Li et al. (2008), and Chang and Hung (2010).

4.1.3.2. Minor AI techniques: CBR, BN, PSO, ACA, DST, AR, SVM, and DT. CBR is also referred to as instance-based learners. This approach uses a collection of solutions to solve new problems. The premise is that new problems are often similar to those that were previously encountered. Thus, past successful solutions may be useful in the new situation. Two articles typically utilized this technique for SS, namely, Zhao and Yu (2011) and Faez, Ghodsypour, and O’Brien (2009).

BNs, also known as belief networks and probabilistic networks, are probabilistic graphical models. The premise is that future states of nature can be characterized probabilistically. This technique is effective for dealing with SS problems under uncertainty via probability distributions. Dogan and Aydin (2011) as well as Ferreira and Borenstein (2012) introduced BN for handling existing uncertainty. The latter study was combined with fuzzy logic, which selects suppliers under triangular fuzzy information.

PSO is an evolutionary algorithm (Kennedy & Eberhart, 1995; Kennedy, Eberhart, & Shi, 2001) that simulates the animal social behavior of birds that flock to a desired location in a multi-dimensional space for certain objectives. Che (2010b) and Xu and Yan (2011) integrated PSO as an element into their decision models for solving balanced and defective supply chain problems as well as material supply problems in large-scale water conservancy and hydropower construction projects, respectively.

ACA is a typical AI optimization method (Dorigo & Gambardella, 1997; Dorigo, Maniezzo, & Colorni, 1996) that simulates a colony of artificial ants that aid one another to obtain effective solutions in complex optimization problems. Tsai, Yang, and Lin (2010) aimed to utilize an attribute-based ant colony system for supplier evaluation.

DST is an uncertainty reasoning tool (Thierry, 1997) that can be used to combine unexpected empirical evidence regarding an individual’s opinion and consequently organize a coherent picture of reality. For SS, Wu (2009b) extended the DST to aggregate individual preferences into a collective preference.

AR is a frequent pattern mining technique that utilizes rules in the form of implications to discover the associations among data entities. The study of Lin, Chuang, Liou, and Wu (2009) presents a typical application of AR for SS.

SVM is a classification and prediction tool for both linear and nonlinear data. DT is a widely used technique for classification and prediction. Guo, Yuan, and Tian (2009) developed a potential SVM technique combined with DT for SS. Wu (2009a) attempted to integrate DT with other two techniques, such as NN and DEA, for assessing supplier performance.

## 4.2. Integrated AHP approaches

A total of 30 articles (24.39%) that refer to the AHP technique for SS are listed in Table 1. Four articles independently utilize AHP for decision making. For example, Mafakheri, Breton, and Ghoniem (2011) provided an AHP-based two-stage dynamic programming approach. Towards different application fields, Levary (2008) introduced AHP to rank potential suppliers in manufacturing industries; Chan and Chan (2010) applied AHP in the fast-changing apparel industry; Ishizaka, Pearman, and Nemery (2012) developed a new variant of AHP for the sorting of suppliers into predefined ordered categories.

Three articles built the integrated AHP approaches under deterministic conditions. Kull and Talluri (2008) provided an evaluation model that used AHP for calculating a risk index based on each alternative supplier. Such indexes were then incorporated into a GP model for selecting suppliers. This model was applied to a case on product life cycle. Ordoobadi (2010) provided an integrated decision model using AHP and the Taguchi loss function. In this model, AHP was used to determine the weights that represent the importance of tangible and intangible decision factors. The weighted Taguchi loss scores were calculated for ranking suppliers. Bhattacharya, Geraghty, and Young (2010) provided an integrated AHP and quality function deployment (QFD) for ranking alternative suppliers.

A total of 23 articles refer to the AHP techniques when considering uncertain decision environments. These techniques can be divided into three categories: (1) AHP-based fuzzy logic hybridization approaches, (2) AHP and triangular fuzzy set integrated approaches, and (3) AHP-based non-fuzzy hybridization approaches. In the first category, Labib (2011) introduced a simple decision model that integrated AHP with the basic fuzzy logic. Sevkli, Koh, Zaim, Demirbag, and Tatoglu (2008) provided a hybrid decision model that used AHP to determine the weights of criteria and weighted fuzzy LP to rank suppliers. Amid, Ghodsypour, and O’Brien (2011) provided a weighted max–min fuzzy model that used an AHP technique to determine the weights of criteria. Tsai and Hung (2009) provided a fuzzy goal programming approach that used AHP to determine the objective structure. Chamodrakas, Batis, and Martakos (2010) as well as Chen and Chao (2012) integrated AHP with fuzzy preference relations to construct decision matrices. Finally, Wang and Yang (2009) integrated AHP with fuzzy compromise programming. The proposed decision model is alleged to outperform the conventional mixed integer programming by further considering scaling and subjective weighting issues.

In the second category, we found 15 articles that referred to AHP and constructed the decision approaches under triangular fuzzy environments. Two articles (Chan, Kumar, Tiwari, Lau, and Choy (2008), Bottani & Rizzi, 2008) utilized the AHP technique and linguistic pairwise comparisons for ranking suppliers under triangular fuzzy environments. Kilincci and Onal (2011) introduced a simple AHP decision model converting the linguistic variables into decision information by using triangular fuzzy values. Yucenur, Vayvay, and Demirel (2011) integrated AHP with ANP, wherein triangular fuzzy values are employed to form pairwise comparison matrices. Zeydan, Çolpan, and Çobanoglu (2011) integrated multiple techniques, including AHP, TOPSIS, and DEA. In this previous work, the authors considered multiple persons as a decision group. Two similar articles by Lee (2009a), Lee (2009b) constructed an uncertain AHP decision model that utilizes the concept of benefits, opportunities, costs, and risks (BOCR). Apart from AHP, Wang, Cheng, and Huang (2009) employed hierarchical TOPSIS; Lee et al. (2009) employed multiple goal programming; and Che (2010b) employed the PSO for green SS. S-en, S-en, and Bas-lgil (2010) integrated AHP with the max–min method. Punniyamoorthy, Mathiyalagan, and Parthiban (2011) integrated AHP with the structural equation modeling model. Yang, Chiu, Tzeng, and Yeh (2008) provided a multi-stage hybrid approach that involves preference expression, interpretive structural modeling, AHP, and non-additive fuzzy integral for the selection of the best supplier. Yu et al. (2012) and Shaw et al. (2012) attempted to integrate AHP with MOLP. The former study considered the time factor via a soft time-window mechanism, whereas the latter focused on the issue of carbon emission during supplier evaluation.

In the third category, Pitchipoo et al. (2012) developed a hybrid decision model via the integration of the AHP technique with GRA. In this model, AHP was used to determine the weights of the evaluation criteria, whereas GRA was used to identify the best supplier.

## 4.3. Integrated ANP Approaches

A total of 15 articles (12.20%) that refer to the ANP technique for SS are shown in Table 1. Eight articles utilized ANP under a certain decision environment. Lin, Lin, Yu, and Tzeng (2010) introduced a simple hybrid approach, in which ANP is used to determine the weights of criteria. Razmi and Rafiei (2010) provided an ANP-integrated mixed-integer non-linear decision model. Ho, Dey, and Lockström (2011) integrated ANP and QFD. In the integrated model of Tseng, Chiang, and Lan (2009), ANP is used for criteria analysis, whereas the Choquet integral is used for the optimization of decision makers’ subjective judgments. Lin et al. (2011) integrated ANP, TOPSIS, and LP for the enterprise resource planning system used for the applications of a manufacturing enterprise. Three articles from the same authors (Demirtas & Üstün, 2008; Demirtas & Üstün, 2009; Üstün & Demirtas, 2008) constructed integrated decision models that involve the ANP technique, the mixed integer LP, and the concept of BOCR.

Considering ANP and fuzzy logic hybrid approaches, Lin (2012) integrated the ANP techniques with fuzzy LP for selecting the best suppliers and handling the inherent uncertainty. Six articles constructed ANP-related models under triangular fuzzy environments. Onüt, Kara, and Is-ik (2009) provided a case study regarding telecommunication companies, in which ANP and TOPSIS were utilized. Razmi et al. (2009a) independently utilized ANP and NLP for SS. Amin and Razmi (2009) investigated a specific case of Internet service provider selection and evaluation, in which ANP and QFD were employed independently. Vinodh, Anesh Ramiya, and Gautham (2011) introduced a simple fuzzy ANP approach regarding manufacturing companies. Yucenur et al. (2011) integrated AHP with ANP. Buyukozkan and Cifci (2012) integrated three techniques: DEMATEL, TOPSIS, and ANP, for green SS.

## 4.4. Integrated DEA Approaches

DEA is among the most used techniques for SS. Of our reviewed articles, 14 applied DEA as an element for the construction of decision approaches. According to different decision environments, these works can be classified into three categories. In the first category, four articles employed DEA with certain decision information. Wu and Blackhurst (2009) provided an augmented DEA approach for supplier ranking. Wu (2009a) introduced a hybrid model using DEA, DT, and NN for supplier classification and prediction. Toloo and

Nalchigar (2011) considered decision environments involving both cardinal and ordinal data. Falagario, Sciancalepore, Costantino, and Pietroforte (2012) integrated DEA with the cross efficiency evaluation for a specific application of public procurement tenders.

In the second category, three articles (Azadeh & Alem, 2010; Chen, 2011b; Zeydan et al., 2011) constructed DEA-related models considering a triangular fuzzy environment. These works simultaneously employed DEA and TOPSIS in the SS process. Apart from fuzzy decision environments, six articles under the third category discussed the utilization of DEA in handling other types of uncertainty. Wu & Olson (2008a), Wu & Olson (2008b) discussed the stochastic DEA simulation models for conflicting criteria analysis, risk evaluation, and SS. Wu (2010) provided a DEA-based stochastic analysis model for dealing with imbedded uncertainty. Saen (2008), Saen (2010) proposed effective DEA-based decision models to handle imprecise data in the SS process. Saen (2010) further considered such undesirable outputs as the uncertainty factor. Celebi and Bayraktar (2008) proposed a novel integration of DEA with NN under the condition of incomplete information within evaluation criteria.

## 4.5. Integrated uncertain decision approaches

Apart from the formulated SS problem under deterministic conditions, current studies address practical problems under different types of uncertainties. According to our reviews, fuzzy formulations dominated other types of uncertainties in recent studies. Table 3 presents the summary of the uncertain decision approaches based on fuzzy formulations and highlights a corre sponding representative article.

Apart from multitudinous fuzzy formulations, we can roughly group the emerging types of other uncertainties into five categories. We summarize the categories based on the relatedness of the study as follows: (1) Stochastic formulations: Wu & Olson (2008a), Wu & Olson (2008b), Wu (2010), Lin and Yeh (2010), Li and Zabinsky (2011), and Yang et al. (2011); (2) Probabilistic formulations: Zhang and Ma (2009), Dogan and Aydin (2011), and Xu and Ding (2011); (3) Formulations with incomplete data: Celebi and Bayraktar (2008); (4) Formulations with imprecise data: Saen (2008), Saen (2010) and (5) Formulations with grey values: Li et al. (2008), Bai and Sarkis (2010), Pitchipoo et al. (2012), and Sadeghieh et al. (2012).

## 4.6. Other Integrated Decision Approaches

Apart from the widely used integrated approaches regarding AHP, ANP, and DEA, we provide other integrated approaches regarding (1) MCDM techniques: ELECTRE, PROMETHEE, and VI-KOR as well as (2) AI techniques: RST and GST.

4.6.1. Integrated approaches regarding ELECTRE, PROMETHEE, and VIKOR

Four articles provided the ELECTRE integrated decision models. Liu and Zhang (2011) integrated the extension of ELECTRE, called ELECTRE-III, with entropy weights. Vahdani, Jabbari, Roshanaei, and Zandieh (2010) considered interval values as decision information in the application of ELECTRE. Montazer, Saremi, and Ramezani (2009) and Sevkli (2010) extended ELECTRE for SS when triangular fuzzy values provided the decision information. The former study employed ELECTRE III, whereas the latter integrated the conventional ELECTRE with fuzzy concepts.

Considering other outranking methods, Chen, Wang, and Wu (2011) integrated PROMETHEE with the extended fuzzy concept and studied a case of information system (IS) outsourcing under triangular fuzzy environments. Chai, Liu, and Xu (2012) developed a novel superiority and inferiority ranking (SIR) group decision approach for SS under intuitionistic fuzzy environments, in which the

Table 4  
Table 3  
Representatives of the integrated fuzzy decision approaches.

<table><tr><td colspan="2">The integrated fuzzy decision approaches</td><td>Representative articles</td></tr><tr><td>Integrated</td><td>Fuzzy AHP</td><td>Amid et al. (2011)</td></tr><tr><td>Fuzzy</td><td>Fuzzy ANP</td><td>Vinodh et al. (2011)</td></tr><tr><td>MCDM</td><td>Fuzzy ELECTRE</td><td>Montazer et al. (2009)</td></tr><tr><td rowspan="5">Approaches</td><td>Fuzzy PROMETHEE</td><td>Chen et al. (2011)</td></tr><tr><td>Fuzzy TOPSIS</td><td>Wang et al. (2009)</td></tr><tr><td>Fuzzy VIKOR</td><td>Chen and Wang (2009)</td></tr><tr><td>Fuzzy DEMATEL</td><td>Chang et al. (2011)</td></tr><tr><td>Fuzzy SMART</td><td>Chou and Chang (2008)</td></tr><tr><td>Integrated</td><td>Fuzzy DEA</td><td>Azadeh and Alem (2010)</td></tr><tr><td>Fuzzy</td><td>Fuzzy LP</td><td>Lin (2012)</td></tr><tr><td>MP</td><td>Fuzzy NLP</td><td>Razmi et al. (2009a)</td></tr><tr><td rowspan="4">Approaches</td><td>Fuzzy GP</td><td>Tsai and Hung (2009)</td></tr><tr><td>Fuzzy MOP</td><td>Amid et al. (2009)</td></tr><tr><td>Fuzzy MOLP</td><td>Yu et al. (2012)</td></tr><tr><td>Fuzzy MONLP</td><td>Yeh and Chuang (2011)</td></tr><tr><td>Integrated</td><td>Fuzzy GA</td><td>Wang (2008)</td></tr><tr><td>Fuzzy</td><td>Fuzzy NN</td><td>Guneri et al. (2011)</td></tr><tr><td>AI</td><td>Fuzzy GST</td><td>Tseng (2011), Wu (2009b)</td></tr><tr><td rowspan="4">Approaches</td><td>Fuzzy BN</td><td>Ferreira and Borenstein (2012)</td></tr><tr><td>Fuzzy CBR</td><td>Faez et al. (2009)</td></tr><tr><td>Fuzzy PSO</td><td>Xu and Yan (2011)</td></tr><tr><td>Fuzzy DST</td><td>Deng and Chan (2011)</td></tr><tr><td>Other</td><td>Fuzzy preference relations</td><td>Chen and Chao (2012)</td></tr><tr><td>Fuzzy</td><td>Fuzzy inference system</td><td>Amindoust et al. (2012)</td></tr><tr><td>Hybridization</td><td>Fuzzy adaptive resonance theory</td><td>Keskin et al. (2010)</td></tr><tr><td rowspan="3">Approaches</td><td>Fuzzy integral</td><td>Yang et al. (2008)</td></tr><tr><td>Fuzzy SWOT</td><td>Amin et al. (2011)</td></tr><tr><td>Fuzzy BOCR</td><td>Lee (2009a; 2009b)</td></tr></table>

SIR method can be regarded as an extension of the conventional PROMETHEE method.

We found three articles referring to the VIKOR method. Chen and Wang (2009) provided a fuzzy VIKOR for the application of IS/information technology (IT) outsourcing projects. This study simulated linguistic variables as decision information and then converted such variables into triangular fuzzy values. Sanayei, Farid, and Yazdankhah (2010) and Shemshadi, Shirazi, Toreihi, and Tarokh (2011) also integrated the VIKOR method with fuzzy concepts. The former study converted linguistic variables by using the tools of triangular and trapezoidal fuzzy values, whereas the latter considered the possible application of the Shannon entropy concept in the proposed fuzzy VIKOR decision model.

Distribution of the selected articles by journal.

<table><tr><td>Journal title</td><td>Amount</td><td>Percentage (%)</td></tr><tr><td>1. Expert systems with applications</td><td>55</td><td>44.7</td></tr><tr><td>2. International Journal of Production Research</td><td>18</td><td>14.6</td></tr><tr><td>3. International Journal of Production Economics</td><td>15</td><td>12.2</td></tr><tr><td>4. International Journal of Advanced Manufacturing Technology</td><td>8</td><td>6.6</td></tr><tr><td>5. Applied Soft Computing Journal</td><td>5</td><td>4.1</td></tr><tr><td>6. Computers and Industrial Engineering</td><td>5</td><td>4.1</td></tr><tr><td>7. European Journal of Operational Research</td><td>4</td><td>3.3</td></tr><tr><td>8. Information Sciences</td><td>3</td><td>2.4</td></tr><tr><td>9. Industrial Management and Data Systems</td><td>2</td><td>1.6</td></tr><tr><td>10. Supply Chain Management</td><td>2</td><td>1.6</td></tr><tr><td>11. Omega</td><td>2</td><td>1.6</td></tr><tr><td>12. International Journal of Logistics Systems and Management</td><td>1</td><td>0.8</td></tr><tr><td>13. IEEE Transactions on Engineering Management</td><td>1</td><td>0.8</td></tr><tr><td>14. International Journal of Uncertainty, Fuzziness and Knowledge-based Systems</td><td>1</td><td>0.8</td></tr><tr><td>15. Soft Computing</td><td>1</td><td>0.8</td></tr><tr><td>Total</td><td>123</td><td>100</td></tr></table>

## 4.6.2. Integrated approaches regarding RST and GST

GST and RST are recently introduced techniques for SS. In GST, Wu (2009b) and Golmohammadi and Mellat-Parast (2012) employed GRA to deal with interval-valued decision information. Tseng (2011) employed triangular fuzzy numbers to express linguistic preferences while utilizing a grey degree to calculate the incomplete information in the green SS process. Bai and Sarkis (2010) and Li et al. (2008) used both GRT and RST methods for SS. For the typical application of RST, Chang and Hung (2010) provided a rule-based decision model.

## 5. Some Observations Remarks

## 5.1. Distribution of Articles by Journal

Table 4 provides the distribution of the articles based on the journal in which they appeared. The articles related to the application of DM techniques for SS are distributed across 15 journals that cover a wide array of disciplines, including IS, operation research, soft computing, and production management. The journal Expert Systems with Applications contains the most relevant articles, comprising 55 out of the 123 articles reviewed (44.7%). Two journals with similar scopes, International Journal of Production Research and International Journal of Production Economics, contributed a combined 33 articles (26.8%) to this research field. Since the current research tends towards uncertain SS, seven articles (5.7%) have been reported in the related journals, including Applied Soft Computing Journal, Soft Computing, and International Journal of Uncertainty, Fuzziness and Knowledge-based Systems.

![](images/e41f3f5d830f1b899502b9a154df7e39d973555c79e904db362ecdc4f46a0764.jpg)  
Fig. 2. Chronological distribution of some major DM techniques.

![](images/2e455cd78d13ee862b2033582c838d162b885c36447450c141259868882bddfe.jpg)  
Fig. 3. Chronological distribution of the uncertainty categories.

## 5.2. Statistical Analysis on Popular DM Techniques

A generally accepted methodological framework for operating an effective SS is not been to be determined because of the complexity and diversity of the real world. According to our survey, the overwhelming majority of reviewed articles attempted to integrate multiple techniques into an effective decision model for dealing with different SS issues such as group aggregation, uncertain information fusion, classification, prediction, and clustering. Therefore, we highlight the first current study trend: Multiple techniques integrated decision approaches.

Table 2 indicates that the most frequently used technique is AHP (24.39%), followed by LP (15.44%), TOPSIS (14.63%), ANP (12.20%), DEA (10.57%), and multiobjective optimization (10.57%). Fig. 2 provides the distribution of a number of major techniques that appeared during the period. The multiattribute utility methods, including AHP and ANP, dominate other techniques because of their effectiveness in ranking and task choices. TOPSIS and DEA remain significant in the construction of decision models. AI techniques, including GA and GST, are receiving considerable research attention. Several emerging AI techniques, including SVM, AR, ACA, and DST, necessitate more transfer learning on future works.

Table 1 presents the 75 articles (60.98%) that provide multitudinous fuzzy hybrid approaches, followed by certain decision approaches (26.01%) and non-fuzzy uncertain decision approaches (13.01%). Therefore, we highlight the second current study trend: Multitudinous uncertain decision approaches. Fig. 3 provides the distribution of each uncertainty category based on the year in which they appeared. Based on this analysis, SS under triangular fuzzy environments is the main stream between 2008 and 2012. Certain decision approaches and basic fuzzy hybrid approaches were regularly reported. Two branches of basic fuzzy theory, such as trapezoidal fuzzy sets and (interval-valued) intuitionistic fuzzy sets, became the new directions toward flexible and practical SS processes.

## 5.3. Other Remarks

1. Preference relations are the tools used by the decision makers to provide their preference information in the decision-making processes. Based on our reviewed articles, the first important trend is that from the certain preference relation to the uncertain preference relation. In this case, we summarize four kinds of preference relations that had been used by previous studies as follows: (1) multiplicative preference relation (also known as pairwise comparison relation): Levary (2008); (2) linguistic reference relation: Tan, Wu, and Ma (2011); (3) fuzzy preference relation: Chen and Chao (2012); and (4) incomplete preference relation: Tseng (2011). The second important trend is that from the singleton preference relation to the hybrid preference relations, which is summarized as follows: (1) interval valued multiplicative preference relation: Chamodrakas, Batis, & Martakos (2010); (2) triangular fuzzy multiplicative preference relation: Golmohammadi and Mellat-Parast (2012); (3) fuzzy linguistic preference relation: Bottani and Rizzi (2008); (4) triangular fuzzy preference relation: Chan et al. (2008); (5) intui tionistic fuzzy preference relation: Chai, Liu, and Xu (2012); and (6) interval valued intuitionistic fuzzy preference relation: Chen et al. (2011). Considering that current studies mainly consider static preference relations, future works should focus on SS with dynamic preference relations when considering the time factor.

2. The methodologies of the hybridization of fuzzy sets and rough sets have been comprehensively studied in the data mining context. Several mature methodologies include rough fuzzy sets (Dubois & Prade, 1990), fuzzy rough sets (Yeung et al., 2005), and intuitionistic fuzzy rough sets (Chai, Liu, & Li, 2012). Such methods had been successfully applied for attribute reduction (Tsang, Chen, Yeung, Wang, & Lee, 2008), feature selection (Jensen & Shen, 2009), classification and prediction (Chai & Liu, 2012). The application of fuzzy-rough hybrid methodologies for solving real-world SS problems must be investigated.

3. We have witnessed the rapid development of the generalization of Zadeh’s fuzzy set over the past several decades. Several developments including interval-valued, triangular, trapezoidal, intuitionistic, and interval-valued intuitionistic fuzzy sets were employed in the current study for SS. A new generalization of fuzzy sets called hesitant fuzzy sets has recently been proposed by Torra (2010), it’s the theoretical basis of which has received considerable attention (e.g. Rodriguez, Martinez, & Herrera, 2012; Wei, 2012; Xu & Xia, 2011; Xu & Xia, 2012). Therefore, evaluating suppliers under hesitation fuzzy environments along with the trend of uncertain SS can be a very promising direction in the future studies.

## 6. Conclusion

This paper provides a systematic literature review on articles published from 2008 to 2012 on the application of DM techniques for SS. We aim to analyze the collected articles from four analytical aspects: decision problems, decision makers, decision environments, and decision approaches. A total of 123 journal articles were carefully selected and reviewed in detail. We systematically summarized 26 applied DM techniques from three perspectives: MCDM, MP, and AI. The techniques that integrated decision models in the literature were particularly reviewed in terms of AHP, ANP, DEA, and so on. This paper provides valuable knowledge accumulation on current studies and recommendations for future works.

This study has two major limitations. First, our review focuses on the application of DM techniques for SS. Other important aspects such as criteria analysis and evaluation in SS processes, were not involved in this survey because of our limited research scope. Second, the reviewed articles were published from 2008 to 2012 and searched based on the keywords ‘‘supplier selection,’’ ‘‘vendor selection,’’ and ‘‘decision making.’’ A number of articles published in late 2012, if any, may not be included in this survey because of the limitation of reporting time. A future review could be expanded in scope.

## Acknowledgments

The authors are grateful for the partial support of CRG grants G-U756, G-YL14 of The Hong Kong Polytechnic University.

## References

Adler, N., Friedman, L., & Sinuany-Stern, Z. (2002). Review of ranking methods in the data envelopment analysis context. European Journal of Operational Research, 140(2), 249–265.

Amid, A., Ghodsypour, S. H., & O’Brien, C. (2009). A weighted additive fuzzy multiobiective model for the supplier selection problem under price breaks in a supply chain. International Journal of Production Economics, 121(2), 323–332.

Amid, A., Ghodsypour, S. H., & O’Brien, C. (2011). A weighted max-min model for fuzzy multi-objective supplier selection in a supply chain. International Journal of Production Economics. 131(1). 139–145.

Amin, S. H., & Razmi, J. (2009). An integrated fuzzy model for supplier management: A case study of ISP selection and evaluation. Expert Systems with Applications, 36(4), 8639–8648.

Amin, S. H., Razmi, J., & Zhang, G. (2011). Supplier selection and order allocation based on fuzzy SWOT analysis and fuzzy linear programming. Expert Systems with Applications, 38(1), 334–342.

Amin, S. H., & Zhang, G. (2012). An integrated model for closed-loop supply chain configuration and supplier selection: Multi-objective approach. Expert Systems and Applications, 39(8), 6782–6791.

Amindoust, A., Ahmed, S., Saghafinia, A., & Bahreininejad, A. (2012). Sustainable supplier selection: A ranking model based on fuzzy inference system. Applied Soft Computing Journal, 12(6), 1668–1677.

Awasthi, A., Chauhan, S. S., & Goyal, S. K. (2010). A fuzzy multicriteria approach for evaluating environmental performance of suppliers. International Journal of Production Economics, 126(2), 370–378.

Azadeh, A., & Alem, S. M. (2010). A flexible deterministic, stochastic and fuzzy data envelopment analysis approach for supply chain risk and vendor selection problem: Simulation analysis. Expert Systems with Applications, 37(12), 7438-7448

Bai, C., & Sarkis, J. (2010). Integrating sustainability into supplier selection with grey system and rough set methodologies. International Journal of Production Economics, 124(1), 252–264.

Bhattacharya, A., Geraghty, J., & Young, P. (2010). Supplier selection paradigm: An integrated hierarchical QFD methodology under multiple-criteria environment. Applied Soft Computing Journal, 10(4), 1013–1027.

Boran, F. E., Genç, S., Kurt, M., & Akay, D. (2009). A multi-criteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method. Expert Systems with Applications, 36(8), 11363–11368.

Bottani, E., & Rizzi, A. (2008). An adapted multi-criteria approach to suppliers and products selection-an application oriented to lead-time reduction. International Journal of Production Economics, 111(2), 763–781

Bustince, H., & Burillo, P. (1996). Vague sets are intuitionistic fuzzy sets. Fuzzy Sets and Systems, 79, 403–405.

Buyukozkan, G., & Cifci, G. (2012). A novel hybrid MCDM approach based on fuzzy DEMATEL, fuzzy ANP and fuzzy TOPSIS to evaluate green suppliers. Expert Systems with Applications, 39(3), 3000–3011

Celebi, D., & Bayraktar, D. (2008). An integrated neural network and data envelopment analysis for supplier evaluation under incomplete information. Expert Systems with Applications, 35(4), 1698–1710.

Chai, J. Y., & Liu, J. N. K. (2012). A new believable rough set decision model for supplier selection, Expert Systems with Applications, in press.

Chai, J. Y., Liu, J. N. K., & Li, A. M. (2012). A new intuitionistic fuzzy rough set approach for decision supports. In International Conference on Rough Sets and Knowledge Technology (RSKT). LNCS (Vol. 7414, pp. 71–80). Springer.

Chai, J. Y., Liu, J. N. K., & Xu, Z. S. (2012). A new rule-based SIR approach to supplier selection under intuitionistic fuzzy environments. International Journal of Uncertainty, Fuzziness and Knowledge-based Systems, 20(3), 451–471.

Chamodrakas, I., Batis, D., & Martakos, D. (2010). Supplier selection in electronic marketplaces using satisficing and fuzzy AHP. Expert Systems with Applications 37(1), 490–498.

Chan, F. T. S., & Chan, H. K. (2010). An AHP model for selection of suppliers in the fast changing fashion market. International Journal of Advanced Manufacturing Technology, 51(9–12), 1195–1207.

Chan, F. T. S., Kumar, N., Tiwari, M. K., Lau, H. C. W., & Choy, K. L. (2008). Global supplier selection: A fuzzy-AHP approach. International Journal of Production Research, 46(14), 3825–3857.

Chang, B., Chang, C., & Wu, C. (2011). Fuzzy DEMATEL method for developing supplier selection criteria. Expert Systems with Applications, 38(3), 1850– 1858.

Chang, B., & Hung, H. (2010). A study of using RST to create the supplier selection model and decision-making rules. Expert Systems with Applications, 37(12), 8284–8295.

Che, Z. H. (2010a). A genetic algorithm-based model for solving multi-period supplier selection problem with assembly sequence. International Journal of Production Research, 48(15), 4355–4377.

Che, Z. H. (2010b). Using fuzzy analytic hierarchy process and particle swarm optimisation for balanced and defective supply chain problems considering WEEE/RoHS directives. International Journal of Production Research, 48(11), 3355–3381.

Chen, T. (2011a). Bivariate models of optimism and pessimism in multi-criteria decision-making based on intuitionistic fuzzy sets. Information Sciences, 181(11), 2139–2165.

Chen, Y. (2011b). Structured methodology for supplier selection and evaluation in a supply chain. Information Sciences, 181(9), 1651–1670.

Chen, Y., & Chao, R. (2012). Supplier selection using consistent fuzzy preference relations. Expert Systems with Applications, 39(3), 3233–3240.

Chen, L. Y., & Wang, T. (2009). Optimizing partners’ choice in IS/IT outsourcing projects: The strategic decision of fuzzy VIKOR. International Journal of Production Economics, 120(1), 233–242.

Chen, T., Wang, H., & Lu, Y. (2011). A multicriteria group decision-making approach based on interval-valued intuitionistic fuzzy sets: A comparative perspective. Expert Systems with Applications, 38(6) 7647–7658.

Chen, Y., Wang, T., & Wu, C. (2011). Strategic decisions using the fuzzy PROMETHEE for IS outsourcing. Expert Systems with Applications, 38(10), 13216–13222.

Chou, S., & Chang, Y. (2008). A decision support system for supplier selection based on a strategy-aligned fuzzy SMART approach. Expert Systems with Applications 34(4), 2241–2253.

Crispim, J. A., & De Sousa, J. P. (2010). Partner selection in virtual enterprises. International Journal of Production Research, 48(3), 683–707.

Dalalah, D., Hayajneh, M., & Batieha, F. (2011). A fuzzy multi-criteria decision making model for supplier selection. Expert Systems with Applications, 38(7), 8384–8391.

Demirtas, E. A., & Üstün, O. (2008). An integrated multi-objective decision making process for supplier selection and order allocation. Omega, 36(1), 76–90.

Demirtas. E. A., & Üstün, O. (2009), Analytic network process and multi-period goal programming integration in purchasing decisions. Computers and Industrial Engineering, 56(2), 677–690.

Deng, J. L. (1989). Introduction to grey system theory. The Journal of Grey System 1(1), 1–24.

Deng, Y., & Chan, F. T. S. (2011). A new fuzzy dempster MCDM method and its application in supplier selection. Expert Systems with Applications, 38(8), 9854–9861.

Dogan, I., & Aydin, N. (2011). Combining bayesian networks and total cost of ownership method for supplier selection analysis. Computers and Industrial Engineering, 61(4), 1072–1085.

Dorigo, M., & Gambardella, L. M. (1997). Ant colony system: A cooperative learning approach to the traveling salesman problem. IEEE Transaction on Evolutionary Computation, 1(1), 53–66.

Dorigo, M., Maniezzo, V., & Colorni, A. (1996). Ant system: Optimization by a colony of cooperating agents. IEEE Transactions on System, Man, and Cybernetics-Part B, 26(1), 29–41.

Dubois, D., & Prade, H. (1990). Rough fuzzy sets and fuzzy rough sets. International Journal of General Systems, 17(2–3), 191–209.

Faez, F., Ghodsypour, S. H., & O’Brien, C. (2009). Vendor selection and order allocation using an integrated fuzzy case-based reasoning and mathematical programming model. International Journal of Production Economics, 121(2), 395–408.

Falagario, M., Sciancalepore, F., Costantino, N., & Pietroforte, R. (2012). Using a DEAcross efficiency approach in public procurement tenders. European Journal of Operational Research, 218(2), 523–529.

Feng, B., Fan, Z., & Li, Y. (2011). A decision method for supplier selection in multiservice outsourcing. International Journal of Production Economics, 132(2), 240–250.

Ferreira, L., & Borenstein, D. (2012). A fuzzy-bayesian model for supplier selection. Expert Systems with Applications, 39(9), 7834–7844.

Figueira, J., Greco, S., & Ehrgott, M. (2005). Multiple Criteria Decision Analysis: State of the Art Surveys. London: Springer-Verlag

Golmohammadi, D., & Mellat-Parast, M. (2012). Developing a grey-based decisionmaking model for supplier selection. International Journal of Production Economics, 137(2), 191–200.

Guneri, A. F., Ertay, T., & Yucel, A. (2011). An approach based on ANFIS input selection and modeling for supplier selection problem. Expert Systems with Applications, 38(12), 14907–14917.

Guneri, A. F., Yucel, A., & Ayyildiz, G. (2009). An integrated fuzzy-lp approach for a supplier selection problem in supply chain management. Expert Systems with Applications, 36(5), 9223–9228.

Guo, X., Yuan, Z., & Tian, B. (2009). Supplier selection based on hierarchical potential support vector machine. Expert Systems with Applications, 36(3 PART 2), 6978–6985.

Haleh, H., & Hamidi, A. (2011). A fuzzy MCDM model for allocating orders to suppliers in a supply chain under uncertainty over a multi-period time horizon. Expert Systems with Applications, 38(8), 9076–9083.

Han, J. W., Kamber, M., & Pei, J. (2012). Data Mining Concepts and Techniques (Third ed.). Springer.

Ho, W., Dey, P. K., & Lockström, M. (2011). Strategic sourcing: A combined QFD and AHP approach in manufacturing. Supply Chain Management, 16(6), 446–461.

Ho, W., Xu, X., & Dey, P. K. (2010). Multi-criteria decision making approaches for supplier evaluation and selection: A literature review. European Journal of Operational Research, 202(1), 16–24.

Hsu, B., Chiang, C., & Shu, M. (2010). Supplier selection using fuzzy quality data and their applications to touch screen. Expert Systems with Applications, 37(9), 6192–6200.

Ishizaka, A., Pearman, C., & Nemery, P. (2012). AHPSort: An AHP-based method for sorting problems. International Journal of Production Research, 50(17), 4767–4784.

Jain, V., Wadhwa, S., & Deshmukh, S. G. (2009). Select supplier-related issues in modelling a dynamic supply chain: Potential, challenges and direction for future research. International Journal of Production Research, 47(11), 3013– 3039.

Jensen, R., & Shen, Q. (2009). New approaches to fuzzy-rough feature selection. IEEE Transactions on Fuzzy Systems, 17(4), 824–838.

Kara, S. S. (2011). Supplier selection with an integrated methodology in unknown environment. Expert Systems with Applications, 38(3), 2133–2139.

Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. IEEE International Conference on Neural Networks, 4, 1942–1948.

Kennedy, J., Eberhart, R., & Shi, Y. (2001). Swarm intelligence. San Francisco: Morgan Kaufmann Publishers

Keskin, G. A., Ilhan, S., & Özkan, C. (2010). The fuzzy ART algorithm: A categorization method for supplier evaluation and selection. Expert Systems with Applications, 37(2), 1235–1240.

Khaleie, S., & Fasanghari, M. (2012). An intuitionistic fuzzy group decision making method using entropy and association coefficient. Soft Computing, 16(7), 1197-1211.

Khaleie, S., Fasanghari, M., & Tavassoli, E. (2012). Supplier selection using a novel intuitionist fuzzy clustering approach. Applied Soft Computing Journal, 12(6), 1741–1754.

Kilincci, O., & Onal, S. A. (2011). Fuzzy AHP approach for supplier selection in a washing machine company. Expert Systems with Applications, 38(8), 9656– 9664.

Kull, T. J., & Talluri, S. (2008). A supply risk reduction model using integrated multicriteria decision making. IEEE Transactions on Engineering Management, 55(3), 409–419.

Labib, A. W. (2011). A supplier selection model: A comparison of fuzzy logic and the analytic hierarchy process. International Journal of Production Research, 49(21), 6287–6299.

Lee, A. H. I. (2009a). A fuzzy AHP evaluation model for buyer-supplier relationships with the consideration of benefits, opportunities, costs and risks. International Journal of Production Research, 47(15), 4255–4280.

Lee, A. H. I. (2009b). A fuzzy supplier selection model with the consideration of benefits, opportunities, costs and risks. Expert Systems with Applications, 36(2), 2879–2893.

Lee, A. H. I., Kang, H., & Chang, C. (2009). Fuzzy multiple goal programming applied to TFT-LCD supplier selection by downstream manufacturers. Expert Systems with Applications, 36(3), 6318–6325.

Lee, C. C., & Ouyang, C. (2009). A neural networks approach for forecasting the supplier’s bid prices in supplier selection negotiation process. Expert Systems with Applications, 36(2), 2961–2970.

Levary, R. R. (2008). Using the analytic hierarchy process to rank foreign suppliers based on supply risks. Computers and Industrial Engineering, 55(2), 535–542.

Li, G., Yamaguchi, D., & Nagai, M. (2008). A grey-based rough decision-making approach to supplier selection. International Journal of Advanced Manufacturing Technology, 36(9–10), 1032–1040.

Li, L., & Zabinsky, Z. B. (2011). Incorporating uncertainty into a supplier selection problem. International Journal of Production Economics, 134(2), 344–356.

Liao, C., & Kao, H. (2011). An integrated fuzzy TOPSIS and MCGP approach to supplier selection in supply chain management. Expert Systems with Applications, 38(9), 10803–10811.

Lin, R. (2012). An integrated model for supplier selection under a fuzzy situation. International Journal of Production Economics, 138(1), 55–61.

Lin, C., Chen, C., & Ting, Y. (2011). An ERP model for supplier selection in electronics industry. Expert Systems with Applications, 38(3), 1760–1765.

Lin, R., Chuang, C., Liou, J. J. H., & Wu, G. (2009). An integrated method for finding key suppliers in SCM. Expert Systems with Applications, 36(3 PART 2), 6461–6465.

Lin, Y., Lin, C., Yu, H., & Tzeng, G. (2010). A novel hybrid MCDM approach for outsourcing vendor selection: A case study for a semiconductor company in taiwan. Expert Systems with Applications. 37(7) 4796–4804

Lin, Y., & Yeh, C. (2010). Optimal carrier selection based on network reliability criterion for stochastic logistics networks. International Journal of Production Economics, 128(2), 510–517.

Liu, P., & Zhang, X. (2011). Research on the supplier selection of a supply chain based on entropy weight and improved ELECTRE-III method. International Journal of Production Research, 49(3), 637–646.

Mafakheri, F., Breton, M., & Ghoniem, A. (2011). Supplier selection-order allocation: A two-stage multiple criteria dynamic programming approach. International Journal of Production Economics, 132(1), 52–57.

Montazer, G. A., Saremi, H. Q., & Ramezani, M. (2009). Design a new mixed expert decision aiding system using fuzzy ELECTRE III method for vendor selection. Expert Systems with Applications. 36(8), 10837–10847.

Ng, W. L. (2008). An efficient and simple model for multiple criteria supplier selection problem. European Journal of Operational Research, 186(3), 1059–1067.

Onüt, S., Kara, S. S., & Is-ik, E. (2009). Long term supplier selection using a combined fuzzy MCDM approach: A case study for a telecommunication company. Expert Systems with Applications, 36(2), 3887–3895.

Opricovic, S., & Tzeng, G. H. (2004). Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. European Journal of Operational Research, 156, 445–455.

Ordoobadi, S. M. (2009). Development of a supplier selection model using fuzzy logic. Supply Chain Management, 14(4), 314–327.

Ordoobadi, S. M. (2010). Application of AHP and taguchi loss functions in supply chain. Industrial Management and Data Systems, 110(8), 1251–1269.

Ordoobadi, S. M., & Wang, S. (2011). A multiple perspectives approach to supplier selection. Industrial Management and Data Systems, 111(4), 629–648.

Ozkok, B. A., & Tiryaki, F. (2011). A compensatory fuzzy approach to multi-objective linear supplier selection problem with multiple-item. Expert Systems with Applications. 38(9).11363–11368.

Pitchipoo, P., Venkumar, P., & Rajakarunakaran, S. (2012). A distinct decision model for the evaluation and selection of a supplier for a chemical processing industry. International Journal of Production Research, 50(16), 4635–4648.

Punniyamoorthy, M., Mathiyalagan, P., & Parthiban, P. (2011). A strategic model using structural equation modeling and fuzzy logic in supplier selection. Expert Systems with Applications, 38(1), 458–474.

Razmi, J., & Rafiei, H. (2010). An integrated analytic network process with mixedinteger non-linear programming to supplier selection and order allocation. International Journal of Advanced Manufacturing Technology, 49(9–12), 1195–1208.

Razmi, J., Rafiei, H., & Hashemi, M. (2009a). Designing a decision support system to evaluate and select suppliers using fuzzy analytic network process. Computers and Industrial Engineering, 57(4), 1282–1290.

Razmi, J., Songhori, M. J., & Khakbaz, M. H. (2009b). An integrated fuzzy group decision making/fuzzy linear programming (FGDMLP) framework for supplier evaluation and order allocation. International Journal of Advanced Manufacturing Technology, 43(5–6), 590–607.

Rezaei, J., & Davoodi, M. (2012). A joint pricing, lot-sizing, and supplier selection model. International Journal of Production Research, 50(16), 4524–4542.

Rodriguez, R. M., Martinez, L., & Herrera, F. (2012). Hesitant fuzzy linguistic term sets for decision making. IEEE Transactions on Fuzzy Systems, 20(1), 109–119.

Sadeghieh, A., Dehghanbaghi, M., Dabbaghi, A., & Barak, S. (2012). A genetic algorithm based grey goal programming (G 3) approach for parts supplier evaluation and selection. International Journal of Production Research, 50(16) 4612–4630.

Saen, R. F. (2008). Supplier selection by the new AR-IDEA model. International Journal of Advanced Manufacturing Technology, 39(11–12), 1061–1070.

Saen, R. F. (2010). Developing a new data envelopment analysis methodology for supplier selection in the presence of both undesirable outputs and imprecise data. International Journal of Advanced Manufacturing Technology, 51(9–12), 1243–1250.

Sanayei, A., Farid, M. S., & Yazdankhah, A. (2010). Group decision making process for supplier selection with VIKOR under fuzzy environment. Expert Systems with Applications, 37(1), 24–30.

S-en, C. G., S-en, S., & Bas-lgil, H. (2010). Pre-selection of suppliers through an integrated fuzzy analytic hierarchy process and max-min methodology. International Journal of Production Research, 48(6), 1603–1625.

Sevkli, M. (2010). An application of the fuzzy ELECTRE method for supplier selection. International Journal of Production Research, 48(12), 3393–3405.

Sevkli, M., Koh, S. C. L., Zaim, S., Demirbag, M., & Tatoglu, E. (2008). Hybrid analytical hierarchy process model for supplier selection. Industrial Management and Data Systems, 108(1), 122–142.

Shaw, K., Shankar, R., Yadav, S. S., & Thakur, L. S. (2012). Supplier selection using fuzzy AHP and fuzzy multi-objective linear programming for developing low carbon supply chain. Expert Systems with Applications, 39(9), 8182–8192.

Shemshadi, A., Shirazi, H., Toreihi, M., & Tarokh, M. J. (2011). A fuzzy VIKOR method for supplier selection based on entropy measure for objective weighting. Expert Systems with Applications, 38(10), 12160–12167.

Shen, C., & Yu, K. (2009). Enhancing the efficacy of supplier selection decisionmaking on the initial stage of new product development: A hybrid fuzzy approach considering the strategic and operational factors simultaneously. Expert Systems with Applications, 36(8), 11271–11281.

Shen, C., & Yu, K. (2012). An integrated fuzzy strategic supplier selection approach for considering the supplier integration spectrum. International Journal of Production Research, 50(3), 817–829.

Singh, R. K., Kumar, P., & Gupta, V. (2010). Fuzzy statistical approach for vendor selection in supply chain. International Journal of Logistics Systems and Management, 7(3), 286–301.

Tan, C., Wu, D. D., & Ma, B. (2011). Group decision making with linguistic preference relations with application to supplier selection. Expert Systems with Applications, 38(12), 14382–14389.

Thierry, D. (1997). Analysis of evidence-theoretic decision rules for pattern classification. Pattern Recognition, 30(7), 1095–1107.

Toloo, M., & Nalchigar, S. (2011). A new DEA method for supplier selection in presence of both cardinal and ordinal data. Expert Systems with Applications, 38(12), 14726–14731.

Torra, V. (2010). Hesitant fuzzy sets. International Journal of Intelligent Systems, 25, 529–539.

Tsai, W., & Hung, S. (2009). A fuzzy goal programming approach for green supply chain optimisation under activity-based costing and performance evaluation with a value-chain structure. International Journal of Production Research, 47(18), 4991–5017.

Tsai, Y. L., Yang, Y. J., & Lin, C. H. (2010). A dynamic decision approach for supplier selection using ant colony system. Expert Systems with Applications, 37(12), 8313–8321.

Tsang, E. C. C., Chen, D. G., Yeung, D. S., Wang, X. Z., & Lee, J. W. T. (2008). Attributes reduction using fuzzy rough sets. IEEE Transactions on Fuzzy Systems, 16(5), 1130–1141.

Tseng, M. (2011). Green supply chain management with linguistic preferences and incomplete information. Applied Soft Computing Journal, 11(8), 4894–4903.

Tseng, M., Chiang, J. H., & Lan, L. W. (2009). Selection of optimal supplier in supply chain management strategy with analytic network process and choquet integral. Computers and Industrial Engineering, 57(1), 330–340.

Üstün, O., & Demirtas, E. A. (2008). An integrated multi-objective decision-making process for multi-period lot-sizing with supplier selection. Omega, 36(4), 509-521

Vahdani, B., Jabbari, A. H. K., Roshanaei, V., & Zandieh, M. (2010). Extension of the ELECTRE method for decision-making problems with interval weights and data. International Journal of Advanced Manufacturing Technology, 50(5–8), 793–800.

Vahdani, B., & Zandieh, M. (2010). Selecting suppliers using a new fuzzy multiple criteria decision model: The fuzzy balancing and ranking method. International Journal of Production Research, 48(18), 5307–5326.

Vinodh, S., Anesh Ramiya, R., & Gautham, S. G. (2011). Application of fuzzy analytic network process for supplier selection in a manufacturing organisation. Expert Systems with Applications, 38(1), 272–280.

Wang, H. S. (2008). Configuration change assessment: Genetic optimization approach with fuzzy multiple criteria for part supplier selection decisions. Expert Systems with Applications. 34(2). 1541–1555.

Wang, J., Cheng, C., & Huang, K. (2009). Fuzzy hierarchical TOPSIS for supplier selection. Applied Soft Computing Journal, 9(1), 377–386.

Wang, Z., Li, K. W., & Xu, J. (2011). A mathematical programming approach to multiattribute decision making with interval-valued intuitionistic fuzzy assessment information. Expert Systems with Applications, 38(10), 12462–12469.

Wang, T., & Yang, Y. (2009). A fuzzy model for supplier selection in quantity discount environments. Expert Systems with Applications, 36(10), 12179– 12187.

Wei, G. (2012). Hesitant fuzzy prioritized operators and their application to multiple attribute decision making. Knowledge-Based Systems, 31, 176–182

Wu, D. (2009a). Supplier selection: A hybrid model using DEA, decision tree and neural network. Expert Systems with Applications, 36(5), 9105–9112.

Wu, D. (2009b). Supplier selection in a fuzzy group setting: A method using grey related analysis and dempster-shafer theory. Expert Systems with Applications, 36(5), 8892–8899.

Wu, L. (2009c). Supplier selection under uncertainty: A switching options perspective. Industrial Management and Data Systems, 109(2), 191–205.

Wu, D. D. (2010). A systematic stochastic efficiency analysis model and application to international supplier performance evaluation. Expert Systems with Applications, 37(9), 6257–6264.

Wu, T., & Blackhurst, J. (2009). Supplier evaluation and selection: An augmented DEA approach. International Journal of Production Research, 47(16), 4593– 4608.

Wu, D., & Olson, D. L. (2008a). A comparison of stochastic dominance and stochastic DEA for vendor evaluation. International Journal of Production Research, 46(8), 2313–2327.

Wu, D., & Olson, D. L. (2008b). Supply chain risk, simulation, and vendor selection. International Journal of Production Economics, 114(2), 646–655.

Wu, D. D., Zhang, Y., Wu, D., & Olson, D. L. (2010). Fuzzy multi-objective programming for supplier selection and risk modeling: A possibility approach. European Journal of Operational Research. 200(3). 774–787

Xu, J., & Ding, C. (2011). A class of chance constrained multiobjective linear programming with birandom coefficients and its application to vendors selection. International Journal of Production Economics, 131(2), 709–720.

Xu, Z., & Xia, M. (2011). Distance and similarity measures for hesitant fuzzy sets. Information Sciences, 181(11), 2128–2138.

Xu, Z., & Xia, M. (2012). Hesitant fuzzy entropy and cross-entropy and their use in multiattribute decision-making. International Journal of Intelligent Systems, 27(9), 799–822.

Xu, J., & Yan, F. (2011). A multi-objective decision making model for the vendor selection problem in a bifuzzy environment. Expert Systems with Applications 38(8), 9684–9695.

Yang, J. L., Chiu, H. N., Tzeng, G. H., & Yeh, R. H. (2008). Vendor selection by integrated fuzzy MCDM techniques with independent and interdependent relationships. Information Sciences, 178(21), 4166–4183.

Yang, P. C., Wee, H. M., Pai, S., & Tseng, Y. F. (2011). Solving a stochastic demand multi-product supplier selection model with service level and budget constraints using genetic algorithm. Expert Systems with Applications, 38(12), 14773–14777.

Yeh, W., & Chuang, M. (2011). Using multi-objective genetic algorithm for partne selection in green supply chain problems. Expert Systems with Applications 38(4), 4244–4253.

Yeung, D. S., Chen, D. G., Tsang, E. C. C., Lee, J. W. T., & Wang, X. Z. (2005). On the generalization of fuzzy rough sets. IEEE Transactions on Fuzzy Systems, 13(3), 343–361.

Yu, P. L. (1973). A class of solutions for group decision problems. Management Science, 19(8), 936–946.

Yu, M., Goh, M., & Lin, H. (2012). Fuzzy multi-objective vendor selection under lean procurement. European Journal of Operational Research, 219(2), 305–311.

Yucel, A., & Güneri, A. F. (2011). A weighted additive fuzzy programming approach for multi-criteria supplier selection. Expert Systems with Applications, 38(5), 6281–6286.

Yucenur, G. N., Vayvay, Ö., & Demirel, N. Ç. (2011). Supplier selection problem in global supply chains by AHP and ANP approaches under fuzzy environment. International Journal of Advanced Manufacturing Technology, 56(5–8), 823– 833.

Zeydan, M., Çolpan, C., & Çobanoglu, C. (2011). A combined methodology for supplier selection and performance evaluation. Expert Systems with Applications 38(3), 2741–2751.

Zhang, G., & Ma, L. (2009). Optimal acquisition policy with quantity discounts and uncertain demands. International Journal of Production Research, 47(9), 2409-2425.

Zhang, D., Zhang, J., Lai, K., & Lu, Y. (2009). An novel approach to supplier selection based on vague sets group decision. Expert Systems with Applications, 36(5), 9557–9563.

Zhao, K., & Yu, X. (2011). A case based reasoning approach on supplier selection in petroleum enterprises. Expert Systems with Applications, 38(6), 6839–6847.