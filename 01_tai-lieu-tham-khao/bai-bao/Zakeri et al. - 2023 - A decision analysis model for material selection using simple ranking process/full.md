OPEN

Check for updates

# A decision analysis model for material selection using simple ranking process

Shervin Zakeri<sup>1\*</sup>, Prasenjit Chatterjee<sup>2</sup>, Dimitri Konstantas<sup>1</sup> & Fatih Ecer<sup>3</sup>

A large number of materials and various criteria fashion material selection problems as complex multi criteria decision-making (MCDM) problems. This paper proposes a new decision-making method called the simple ranking process (SRP) to solve complex material selection problems. The accuracy of the criteria weights has a direct impact on the outcomes of the new method. In contrast to current MCDM methods, the normalization step has been eliminated from the SRP method as a potential source of producing incorrect results. The application of the method is appropriate for situations with high levels of complexity in material selection because it only considers the ranks of alternatives in each criterion. The frst scenario of vital-immaterial mediocre method (VIMM) is used as a tool to derive criteria weights based on expert assessment. The result of SRP is compared with a number of MCDM methods. In order to evaluate the fndings of analytical comparison, a novel statistical measure known as compromise decision index (CDI) is proposed in this paper. CDI revealed that the MCDM methods’ outputs for solving the material selection could not be theoretically proven and requires to be evaluated through practice. As a result, the dependency analysis-an additional innovative statistical measure is introduced to demonstrate the reliability of MCDM methods by assessing its dependency on criteria weights. The fndings demonstrated that SRP is extremely reliant on criteria weights and its reliability rises with the number of criteria, making it a perfect tool for solving challenging MCDM problems.

Material selection problems and multi-criteria decision-making (MCDM) methods have strong relationships. Selecting suitable materials is the most challenging task in designing and developing new products<sup>1</sup>. Engineering design revolves around the objectives of achieving high performance, minimizing costs, and being environmentally conscious, which are ofen constrained by materials. Terefore, one of the key goals of optimal product design is the selection of materials that fulfill the design criteria while delivering the highest level of performance at the most economical cost<sup>2,3</sup>. Material selection is a complex decision-making process that involves the selection of the most suitable materials from a range of available alternatives based on multiple criteria. Multi-Criteria Decision Making (MCDM) refers to a class of mathematical methods used to solve such complex decisionmaking problems. Tese problems ofen arise in real-world situations where decision-makers has to select from a set of alternatives that differ across several criteria or dimensions. The goal of MCDM is to identify the best possible alternative or set of alternatives based on the decision-makers’ preferences and priorities. MCDM problems are typically represented in a matrix format, where each row represents an alternative and each column represents a criterion. Te elements of the matrix correspond to the performance of each alternative on each criterion. Te decision-makers are then asked to provide weights or priorities for each criterion, indicating the relative importance of each criterion in the decision-making process. Material selection problems also involve the evaluation and selection of the most suitable material from a set of alternatives based on multiple criteria. Tis type of problem requires a decision-maker to weigh the importance of each criterion and to evaluate the alternatives accordingly. Material selection decisions typically involve multiple conficting criteria, such as cost, performance, durability, physical and engineering properties, environmental factors, cost, and manufacturability, among others. Tese criteria may have diferent units of measurement, making it challenging to compare and evaluate alternatives using a single metric. Since the material selection could be converted into an MCDM problem-form problem, MCDM methods are suitable solutions to fnd the best material to meet the needs of the design and development of products. Many researchers have drawn attention to the connection between

MCDM methods and material selection problems. According to<sup>4</sup>, among various methods and techniques that are employed to select the most suitable material for diferent projects, MCDM methodologies are among the most popular approaches. Reference<sup>5</sup> call material selection problems MCDM dilemmas, and<sup>6</sup> believe that MCDM methods are the only solution for the material selection problems that incorporate a large number of competing performance characteristics and are involved with many decision-makers. Similar to the latter authors<sup>7</sup>, argues that MCDM methods are efcient tools for efectively managing material selection problems incorporating various material properties and varied criteria. Reference<sup>8</sup> also mentioned that MCDM methods aid in achieving the desired results from a product since the methods evaluate the materials’ performance under conficting criteria. Te use of MCDM methods in material selection problems has several advantages. First, it provides a systematic and objective approach to evaluate and rank materials based on multiple criteria. Second, it helps decision-makers to identify the critical criteria that have the most signifcant impact (having highest weight value) on the decision. Tird, it enables decision-makers to evaluate and compare the performance of diferent materials under diferent scenarios. Finally, it provides a transparent and structured approach to the decision making process, which can help to build consensus and improve communication among stakeholders. MCDM methods are widely used in material selection problems for computing the criteria weights and determining the rank of materials. Diferent scholars have proposed various categories for these two tasks. MCDM weighting methods can generally be classifed into two categories: subjective weighting methods and objective weighting methods. Te subjective weighting methods rely solely on human opinions, expectations, and judgments to assign weights to the criteria, whereas the objective weighting methods extract the criteria weights from the matrix of the decision-making problem. Te ranking methods are divided into four subcategories, including th outranking methods, compromise ranking methods, distance-based methods, and the methods that use pairwise comparison. Te complexity of an MCDM problem is associated with:

1. Te complexity of input, involving objective and subjective values,

2. Diferent numbers of goals involved in the evaluation process of the alternatives,

3. Confiction between the nature of the criteria in the MCDM problems with multiple layers of criteria,

4. Te number of non-benefcial criteria,

5. Te number of criteria.

In this case, material selection problems always involve many alternatives and criteria, where with increasing the number of criteria, the reliability of the MCDM methods used for ranking the material decreases. To solve this problem, this paper proposes new MCDM method, called simple ranking process (SRP) which is based on ranking the alternatives against each criterion. Te precision of criteria weight estimation directly afects the efectiveness of SRP algorithm. Te new method is designed to deal with complex decision-making problems using simple processes compared to the existing MCDM methods. In this paper, the new method is applied to solve a material selection problem. Criteria weights of the problem are reassessed by the seven experts through a group decision-making process, followed by the application of vital-immaterial mediocre method (VIMM) to provide accurate weights. VIMM, which was proposed by<sup>9</sup>, is a subjective weighting method that was developed to bridge the structural and processual gaps in AHP and BWM. Te paper presents several contributions centered around a new MCDM method that can efectively address complex decision-making problems. Reliability of the method is also shown to increase as the complexity of the problem increases. Additionally, the paper introduces two new statistical measures for validating results of MCDM methods. Te paper is structured as follows: the second section presents the literature review, while the third section describes the proposed method and VIMM. Te fourth section applies the methods to a real-world material selection problem. Te ffh section discusses the results and introduces a new statistical measure to validate complex MCDM solutions. Te paper concludes in the sixth section with a summary of the fndings and suggestions for future research.

## Literature review

Dissimilar mathematical treatments are employed by diferent MCDM methods based on the categories they are members of to derive the best material, consequently ofering diferent materials as the most suitable option for the same problem. With an extensive literature review, this section aims to provide a scientifc perspective for the readers regarding the MCDM methods application in material selection problems and the gaps in the current course of MCDM methods and material selection engagement. Specifcally, this section seeks to demonstrate the following:

1. Te investigation of the relationship between MCDM methods in the diferent categories with the diferent complex material selection problems,

2. Te prevalent problem of dissimilarities between the outputs of the MCDM methods in solving materia selection problems that are revealed by diferent studies, which emerges as the results validation issues,

3. Solutions the studies employed to overcome the dissimilarities.

Tese gaps will be later addressed in the paper. To visualize the literature review section’s composition, its structure has been illustrated in Fig. 1.

MCDM methods for material selection problems. Appropriate material selection results in improved quality and enhanced product life cycle, while inaccurate selection leads to increased design cost, lack of productivity, poor end product performance, critical component damage, and eventually untimed product failure<sup>10</sup>.

![](images/4a84721e33515e96cb08957fcdd80d7dffc34215b52f5edc020861b2a5682259.jpg)  
Figure 1. Te literature review structure.

Tus, it is critical to exert a method that optimizes material selection decisions and minimizes the risk of poor selection. Tis paper proposes a new MCDM method to solve this problem. So far, several MCDM methods for material selection problems have been developed and applied. Te technique for order of preference by similarity to ideal solution (TOPSIS) developed by Hwang and Yoon<sup>11</sup>, analytic hierarchy process (AHP) by Saaty<sup>12</sup>, analytical network process (ANP) proposed by Saaty<sup>13,</sup> simple additive weighted (SAW) (MacCrimmon & Rand.<sup>14,</sup> data envelopment analysis (DEA) proposed by Charnes<sup>15</sup>, Vise Kriterijumska Optimizacija I Kompromisno Resenje (VIKOR) developed by Opricovic and Tzeng<sup>16</sup>, decision making trial and evaluation laboratory (DEMATEL) developed by Fontela and Gabus17, preference ranking organization method for enrichment evalu ations (PROMETHEE)<sup>18</sup> and ELimination Et Choix Traduisant la REalité or ELimination and Choice expressing reality (ELECTRE) proposed and advocated by Roy<sup>19</sup> are some of the most popular MCDM methods for material selection problems. Some of the recent developments in MCDM methods are ranking based on optima points multi-criteria decision-making method (RBOP) by Zakeri.<sup>20,</sup> step-wise weight assessment ratio analysis (SWARA) frst developed by Keršulienė & Turskis<sup>21</sup>, subjective weighting method using continuous interva scale by Toloie-Eshlaghy et al.<sup>22,</sup> superiority and inferiority ranking (SIR) method by Xu<sup>23</sup>, multi-attribute evaluation using imprecise weight estimates (IMP) method proposed by Jessop<sup>24</sup>, and best–worst method (BWM) introduced by Rezaei<sup>25</sup>.

In some problems, the outputs of MCDM methods are dissimilar<sup>26,27</sup>. Te comparison of MCDM methods and their outputs can be found in Refs.<sup>28,29</sup>. To evaluate alternative hydropower systems on the “Drina River,” Opricovic & Tzeng28compared the extended VIKOR method with TOPSIS, PROMETHEE, and ELECTRE, where the TOPSIS and VIKOR generated the same ranking for the two best alternatives while the ratio was diferent. By utilizing Kendall's tau-b test and Spearman's rho test to determine the significance of rank correlation between the compared methods, the sensitivity of final ranks to selected fuzziness intervals, and the sensitivity of simi larities and dissimilarities of different decision ranking methods to the dimensions of the decision matrix, the appropriate MCDM method was selected in the work of Zamani-Sabzi et al.<sup>29</sup>. Tey evaluated the performances of ten popular MCDM methods including SAW, weighted product method (WPM), compromise programming (CP), TOPSIS, AHP, VIKOR, and ELECTRE under a fuzzy environment. According to Ref.<sup>30</sup>, the inconsistency that occurred in generating dissimilar results by MCDM methods is due to four reasons:

1. Te methods use weights diferently in their calculations.

2. Algorithms difer in their approach to selecting the ‘best’ solution.

3. Many algorithms attempt to scale the objectives, which afects the weights already chosen.

4. Some algorithms introduce additional parameters that afect the selection of the solution.

Te most important reasons that directly afect the fnal output of the MCDM methods are 1. Determining criteria weights; and 2. Policies/philosophies for evaluating alternatives. Te application of these two items to material selection problems has been discussed in the following sections.

MCDM methods for criteria weighting. One of the main challenges in MCDM problems is to determine the relative importance of each criterion. Criteria weighting methods are used to assign weights to the criteria, refecting their relative importance in the decision-making process. Criteria weighting methods in MCDM environment are mostly divided into subjective and objective methods. Tere is also a third type of weighting method, popularly known as combinative weighting method, which utilizes hybridization or integration of diferent subjective and objective methods using multiplication and additive synthesis<sup>31</sup>. Subjective weighting methods depend on DMs’ judgments, levels of knowledge, perception, and intentions,and these methods do not use a formal mathematical approach to determine the weights, but rather rely on the experience and expertise of the decision-makers. Subjective weighting methods are ofen used when there is a lack of data or when the criteria are difcult to quantify. On the other hand, objective weighting methods extract weights directly from decision matrix using mathematical algorithms without considering human judgments to avoid inaccuracies and imprecisions. In order to reduce errors and ambiguities in the decision-making process, hybrid weighting methods (subjective and objective methods) have also been developed. Some of the most popular subjective methods are Digital Logic and Modifed Digital Logic methods<sup>32</sup>, Pairwise Comparison (e.g. AHP), Best–worst Method, Ratio method<sup>33</sup> Swing method<sup>34</sup>, Simple multi-attribute ranking technique (SMART) and SIMOS method<sup>35</sup>. Some of the most popular objective weighting methods are Shannon’s entropy<sup>36</sup> and CRITIC (Te CRiteria Importance Trough Intercriteria Correlation) methods<sup>37</sup>. An overview of MCDM weighting methods for material selection problems has been presented briefy in the following sections.

Subjective weighting methods in materials selection. Some examples of the subjective weighting methods in the complex material selection problems to evaluate the importance of the selected criteria are shown in Table 1. AHP and BWM methods are observed to be very popular methods for criteria weighting in material selection problems. AHP provides a systematic and structured approach to decision-making and helps to organize complex decision problems in a hierarchical structure, making it easier for decision-makers to understand the problem and the relationships between the criteria. On the other hand, BWM is a straightforward method that requires decision-makers to select the best and worst criteria from a set of options, making it easy to understand and apply.

Objective weighting methods in materials selection. Shannon’s entropy method is one of the most popular objective methods for computing criteria weights for material selection applications. Compared to other objective weighting methods, most studies employed Shannon’s entropy to compute the criteria weights in this category. Apart from Entropy method, there are other recently developed objective weighting methods like method based on the removal efects of criteria (MEREC) and logarithmic percentage change driven objective weighting (LOPCOW). Table 2 shows instances of using objective weighting methods in material selection problems.

MCDM methods for ranking alternatives. MCDM methods are generally developed for ranking alternatives based on four main concepts:

<table><tr><td>Author(s)</td><td>Case application</td><td>Criteria</td><td>Subjective weighting method</td></tr><tr><td>Das et al.38</td><td>Material selection case study of spur gear reduction unit</td><td>1. The pressure angle, 2. Module, 3. Number of teeth to avoid interference, 4. Gear width, and 5. Gear material</td><td>AHP</td></tr><tr><td>Mahmoudkelaye et al.39</td><td>To select sustainable materials for building enclosures</td><td>Economic, technical, environmental, and socio-cultural and their corresponding sub-criteria</td><td>ANP</td></tr><tr><td>Patnaik et al.10</td><td>To select the best composite materials for wear-resistant applications</td><td>1. Physical properties, 2. Mechanical properties, 3. Slurry abrasion, 4. Wear properties</td><td>AHP</td></tr><tr><td>Prasad et al.40</td><td>Coating material for magnesium alloy</td><td>1. Density, 2. Thermal conductivity, 3. Thermal expansion coefficient hardness, 4. Young's modulus elastic recovery, 5. Critical load, 6. Yield stress, 7. Melting temperature, 8. H/E ratio H3/E2 ratio, 10. Wear resistance, 11. Coefficient of friction, 12. Radiation sensitivity, 13. Workability, 14. Appearance, 15. Oxidation resistance, 16. Oxidation rate constant, 17. Impact resistance, 18. The possibility of surface treatment material, 19. Manufacturing, 20. Availability, 13. Accessibility, 14. Toxicity, 15. Adhesion to the substrate, 16. Bond strength, 17. Durability, 18. Brittleness, 19. Compatibility of the material, 20. Matrix, 21. Framed, 22. Mixed, 23. The aging tendency, 24. Porosity, 25. Geographical location, 26/political stability &amp; foreign policy, 27. Exchange rate &amp; economic position</td><td>Fuzzy AHP</td></tr><tr><td>Palanisamy et al.41</td><td>Additive manufacturing machine and materials</td><td>1. Cost, 2. Visual and aesthetic modeling, 3. Tensile strength, 4. Shore hardness, 5. Mixing number, 6. Number of digital materials, 7. Frequent order, and 8. Elongation at break</td><td>BWM</td></tr><tr><td>Maghsoodi et al.42</td><td>Phase change material selection for interior building surface application</td><td>1. Melting temperature, 2. Latent heat storage capacity, 3. Thermal conductivity, 4. Specific heat capacity, 5. Energy density and 6. Cost</td><td>BWM</td></tr><tr><td>Yang et al.43</td><td>Phase change material selection for solar domestic hot water system</td><td>1. Latent heat, 2. Density, 3. Specific heat for solid, 4. Specific heat for liquid, 5. Thermal conductivity and 6. Cost</td><td>AHP</td></tr><tr><td>Kumar et al.44</td><td>Coating material selection in tooling industries</td><td>1. Indentation hardness, 2. Young's modulus, 3. Wear resistance, 4. Plastic Deformation, 5. Strain hardening exponent, 6. Coefficient of thermal expansion, 7. Surface roughness, 8. Coefficient of friction 9. Wear rate</td><td>BWM</td></tr><tr><td>Aksakal et al.4</td><td>Thermal insulation material selection</td><td>1. Thermal conductivity, 2. Periodic thermal transmittance, 3. Specific heat, 4. Density, 5. Decrement factor, 6. Surface mass, 7. Thermal transmittance, 8. Thermal wave shift</td><td>Fuzzy BWM</td></tr><tr><td>Grachev et al.45</td><td>Dental material selection in manufacturing removable dentures</td><td>1. Mechanical properties, 2. Biological properties, 3. Tribo-logical properties, 4. Technological properties and 5. Cost</td><td>AHP</td></tr><tr><td>Author(s)</td><td>Case application</td><td>Criteria</td><td>Objective weighting method</td></tr><tr><td>Bhowmik et al.46</td><td>Energy-efficient materials</td><td>1. Density, 2. Bulk Modulus, 3. Compressive Strength, 4. Thermal Conductivity, 5. Thermal Expansion, 6. Resistivity, 7. Cost, 8. Energy Production, and 9. CO2 Emission</td><td>Entropy</td></tr><tr><td>Oluah et al.47</td><td>Latent heat storage materials for optimal performance of a Trombe wall</td><td>1. Heat of Fusion, 2. Thermal Conductivity, 3. Density, and 4. Cost</td><td>Entropy</td></tr><tr><td>Aksakal et al.4</td><td>Thermal insulation material</td><td>1. Thermal Conductivity, 2. Periodic Thermal Transmittance, 3. Specific Heat, 4. Density, 5. Decrement Factor, 6. Surface Mass, 7. Thermal Transmittance, and 8. Thermal Wave Shift</td><td>CRITIC</td></tr><tr><td>Mahajan et al.48</td><td>Natural Fiber for Sustainable Composite</td><td>1. Aspect Ratio, 2. Strain at break, 3. Specific strength, 4. Specific modulus, 5. Moisture Absorption, and 6. Cost</td><td>Entropy and CRITIC</td></tr><tr><td>Akgün et al.49</td><td>Selection of most appropriate carbon-based nanomaterials</td><td>1. Melting Point Temperature Change, 2. Latent Heat Change, 3. Thermal Conductivity Enhancement, 4. Leakage, 5. Greenhouse Gas, 6. Cost, and 7. Agglomeration</td><td>Entropy</td></tr><tr><td>Haq et al.50</td><td>Material selection for wing-spar of human-powered aircraft</td><td>1. Price, 2. Tensile Strength, 3. Young's Modulus, 4. Density, 5. Compressive Strength, 6. Creep Resistance, 7. Fatigue Resistance, 8. Machinability, 9. Recyclability and 10. Carbon Footprint During Manufacture</td><td>Entropy</td></tr><tr><td>Ulutaş et al.51</td><td>Building insulation material selection</td><td>1. vapour diffusion resistance factor, 2. sound absorption coefficient, 3. embodied carbon, 4. embodied energy, 5. cost, 6. reaction to fire, 7. specific heat capacity, 8. thermal conductivity, and 9. density</td><td>MEREC and LOPCOW</td></tr></table>

Table 1. Subjective weighting methods and their applications in materials selection.

Table 2. Objective weighting methods and their applications in materials selection.

1. Outranking methods such as ELECTRE, PROMETHEE, and GLDS (Gain and Lost Dominance Score).

2. Compromise ranking policies such as VIKOR, GRA.

3. Distance-based methods such as TOPSIS, Evaluation based on Distance from Average Solution (EDAS), Multi-Attributive Border Approximation Area Comparison (MABAC) and Combinative Distance-based Assessment Method (CODAS).

4. Pairwise comparison such as AHP and ANP.

Tere are other categorizations suggested by scholars, e.g. the classifcation of the MCDM methods into fve classes<sup>52,</sup> including the quantitative methods, qualitative methods, mixed techniques, heuristics, and metaheuristics, and simulation,or categorizing them into the three main groups<sup>53</sup> including the utility value-based methods, the outranking methods, preference ordering based methods. Except for the pairwise comparison methods which have been discussed earlier, in the following sections, the application of MCDM methods to materia selection problems has been briefy reviewed based on the three MCDM categories comprising outranking, compromise ranking, and distance-based ranking methods.

Material selection using outranking methods. Diferent forms of ELECTRE method have been applied to material selection problems. Using a hybrid method and the opinions of four experts in a group decision-making framework<sup>54</sup>, employed ELECTRE III to solve the ofce fooring selection problem, in which the ease of cleaning and maintenance, durability, quietness, style and comfort, sustainability, and cost-efectiveness have been used as criteria. Singh et al.<sup>55</sup> employed a hybrid model of ELECTRE II and entropy to solve the friction composite selection problem consisting of seven attributes and nine alternatives. ELECTRE and PROMETHEE methods have also been used to solve material selection problems. Gul et al.<sup>56</sup> proposed a solution for an automotive instrument panel material selection problem using fuzzy PROMETHEE method while considering Styrene Maleic Anhydride, Polycarbonate, Polypropylene, and Acrylonitrile Butadiene Styrene as the potential materia alternatives, and maximum temperature limit, recyclability, elongation, weight, thermal conductivity, tensile strength, cost, and toxicity level as the criteria. Using six criteria containing creep strength, resistance to oxida: tion, thermal expansion coefficient, vield strength, limit strain, and toughness against five alternatives, Zindani & Kumar<sup>57</sup> designed a PROMETHEE-GAIA method to fnd the best material suitable for the labyrinth seal strips. Exconde et al.58 focused on the selection of materials for use in 3D printer filaments using ELECTRE method. Singh et al.<sup>55</sup> employed a hybrid ELECTRE II-entropy model for selecting natural fbers for use in brake friction composites. Te results revealed that 10 wt% banana fber emerged as the best alternative among all fbers that were considered. Mahajan et al.<sup>48</sup> investigated the selection process of natural fbers for sustainable composites. Tey proposed a hybrid MCDM model that utilized the Entropy and CRITIC methods to calculate the criteria weights, and the PROMETHEE II, TOPSIS, and VIKOR methods to rank the materials under consideration. Bhaskar and Khan<sup>1</sup> evaluated seven materials based on ten material selection criteria to identify the best polymer-based biomaterial for dental applications using ELECTRE, PROMTHEE, VIKOR, TOPSIS, and MOORA methods. Ranjith and Vimalkumar (2022) developed a hybrid MCDM method that integrated ELECTRE and MOORA methods for selecting the best electrode material from five available alternatives for electrical discharge machining of magnesium composites. Kirişci et  al.<sup>59</sup> extended the ELECTRE I model to the Fermatean fuzzy ELECTRE I model for group decision-making using Fermatean fuzzy human assessments for material selection of the femoral component of the hip joint prosthesis. Zhou<sup>60</sup> adopted ELECTRE method to select an optimal recycled material for 3D printer flament from a waste plastic stream containing a mixture of polymers. Te results indicated that recycled polyethylene terephthalate outperformed all other considered plastic materials.

Material selection using compromise ranking methods. Te literature suggests that GRA and VIKOR are the most widely used compromise ranking methods for material selection applications. Jayakrishna and Vinodh<sup>61</sup> proposed an integrated approach that employed GRA to rank materials based on cost, material properties, and environmental impact. Zhang et al.<sup>62</sup> used GRA in combination with other methods, such as DEMATEL, ANP, and TOPSIS, to select the optimal green material for sustainable rubbish bins based on multiple criteria. Sanghvi et al.63 adopted a combined framework of GRA and fuzzy logic to leverage the benefits of both methods for bone staples material selection problem. Similarly, Wang & Li<sup>64</sup> employed GRA in conjunction with a hybrid weighting method that integrated AHP, Fuzzy AHP, and quality function deployment (QFD) methods to solv the lightweight automotive body material selection problem. Dwivedi & Sharma<sup>65</sup> applied an integrated entropy-CoCoSo method to identify the most suitable sustainable material for an engineering application. Maidin et al.<sup>66</sup> developed a systematic evaluation framework using GRA to rank natural fber materials as reinforcement composites for cyclist helmets, with pineapple identifed as the most suitable candidate for optimal safety. In another study, Maidin et al.<sup>67</sup> applied 6 Sigma and GRA methods to select the most suitable thermoplastic matrix for natural fber composites in cyclist helmets, integrating qualitative and quantitative approaches to identify ther moplastic polyethylene as the ideal matrix.

Ishak et al.<sup>68</sup> applied fuzzy VIKOR method to select the optimal natural fber type for fber-reinforced composites to be utilized in the manufacture of a fber-metal laminate for car front hoods. Te objective of this analysis was to achieve a reduction in transportation weight, which is crucial for improving fuel efciency and reducing environmental impact. Dev et al.<sup>69</sup> utilized an Entropy-VIKOR model to determine the optimal composite material for an automobile piston application case study. Entropy method was applied to compute the relative weights of various evaluation criteria, while VIKOR method was employed to rank the composite materials under consideration. Te approach ensured a comprehensive and objective evaluation of the available alternative materials, leading to a well-informed decision regarding the most suitable composite material for the intended application. Gadhave et al.<sup>70</sup> conducted a study on the selection of phase change material using three MCDM methods and utilized AHP—entropy methods to determine the criteria weights. VIKOR, TOPSIS and EXPROM2 methods were used to rank the alternative materials. Te ranking was based on the compromised weight obtained through AHP and entropy methods. Bhaskar & Khan<sup>1</sup> showcased the efectiveness of fve different hybrid MCDM methods in identifying the optimal polymer-based biomaterial for use in dentistry. Tey evaluated seven materials based on ten criteria and utilized AHP to determine criteria weights. Te materials were ranked using AHP-VIKOR, AHP-TOPSIS, AHP-MOORA, AHP-ELECTRE, and AHP-PROMTHEE methods. Grachev et al.<sup>45</sup> developed a formalized method for selecting dental materials in the production of removable dentures. Teir approach combined AHP-Extended VIKOR method and involved analyzing interval quantitative estimations. Bhuiyan & Hammad<sup>71</sup> developed a decision support system to assist with selecting the most sustainable structural material using a hybrid MCDM method that combined AHP, TOPSIS, and VIKOR in a fuzzy environment.

Material selection using distance-based methods. Applications of distance-based MCDM methods are wel popular in solving material selection problems. Xue et al.<sup>72</sup> introduced a new method based on interval-valued intuitionistic fuzzy sets and MABAC to address the issue of incomplete weight information in automotive instrument panel material selection problems. Tian et al.<sup>73</sup> proposed a hybrid MCDM approach that combined AHP and grey correlation TOPSIS (GC-TOPSIS) methods to select the optimal green decoration materials from a pool of 10 diferent types of solid woods. Ahmed et al.<sup>74</sup> proposed a decision support framework taking into account technical, environmental, social, and economic criteria for ranking concrete materials. Te framework comprised of an optimal scoring method (OSM) that shortlisted the materials, followed determination of ranking orders using AHP-TOPSIS method. Deshmukh & Angira.<sup>75</sup>, used VIKOR and TOPSIS to solve the material selection problem for radio-frequency microelectromechanical system (RF-MEMS) shunt capacitive switches considering Young’s Modulus, Electrical resistivity, Termal conductivity, Fracture strength as the criteria. Maghsoodi et al.<sup>76</sup> addressed a material selection problem in the context of dam construction projects by proposing a hybrid decision-making approach that combined SWARA and CODAS methods. Te proposed approach considered target-based attributes to facilitate the evaluation process. Roy et al.<sup>77</sup> developed an evaluation framework for solving sustainable material selection problems in construction projects with incomplete weight information. Te approach extended CODAS method by incorporating interval-valued intuitionistic fuzzy numbers. Yadav et al.<sup>78</sup> proposed a novel MCDM approach based on TOPSIS-PSI for choosing the best alternative material in marine conditions. Dhanalakshmi et  al.<sup>79</sup> employed a comprehensive MCDM-based approach, combining Fuzzy AHP, TOPSIS, and EDAS methods, for the selection of pyrolysis materials. Te criteria were defned based on the objective of achieving maximum bio-oil yield during pyrolysis. Kar & Jha<sup>80</sup> proposed a novel approach that integrates material management with construction schedule to prioritize construction materials using ANP-TOPSIS method. Te criteria weights were determined using ANP, while TOPSIS was used to calculate material criticality of the alternative materials. Te result of the study showed that structural steel was the best material. Another hybrid method of VIKOR and TOPSIS could be found in Ref.<sup>81</sup>, where it is used to select the best dielectric material for RF-MEMS switches with low power consumption. Yang et al.<sup>82</sup> developed a method for selecting an appropriate normalization method in TOPSIS when choosing the optima tribological coating material. Tey also introduced entropy-based and variation coefcient-based performance scores to evaluate the efectiveness of the normalization method. Kumar et  al.<sup>83</sup> applied TOPSIS method to optimize the selection of glazing materials for solar thermal applications with multiple response characteristics.

Te study considered seven alternative materials and six criteria for material selection in the optimal design. Te results showed that Polysulfone material was the best choice for solar thermal applications. Aires & Ferreira<sup>84</sup> developed a decision-making framework for selecting the most suitable thermal insulation material for enhancing energy efciency, by integrating Fuzzy BWM, CRITIC, and Mixed Aggregation by Comprehensive Normalization Technique (MACONT). Among the considered alternatives, Polyisocyanurate was identifed as the optimal material based on the defned criteria. Abishini & Karthikeyan<sup>85</sup> investigated the use of AHP, TOPSIS, EDAS, VIKOR, and Taguchi-based super ranking concepts to select the optimal aluminum alloy material for the sheet metal forming process. Te study revealed that AA2024 aluminum was the best-ranked material among the alternatives considered. Kazemian et al.<sup>86</sup> conducted a comprehensive evaluation of ten diferent materials used for intraoral stents in head and neck cancer patients. Te study aimed to identify the most suitable materia using the TOPSIS method, and the results showed that Ethylene Vinyl Acetate was the best material. Sharma et al.<sup>87</sup> investigated the optimal material selection problem for railway wagons using VIKOR, TOPSIS, PROM-ETTHEE, and WASPAS methods and also compared the relative performances. Te study revealed aluminum alloy Al 6005-T6 as the most suitable material. Remadi & Frikha<sup>88</sup> proposed a model for ranking green materials using CODAS method and utilized intuitionistic fuzzy sets within an uncertain group decision-making environment. Wankhede et al.<sup>89</sup> focused on selection of natural fber for long lasting composites using CODAS method. Basalt was found as the best natural for long lasting composites followed by fax and Kenaf respectively. Ranking performance of CODAS was also compared with MOORA method. Table 3 summarizes the distance-based studies which used the aforementioned methods. Based on the literature review as presented above, a number of MCDM methods have been employed to solve material selection problems. Tis leads us to the next part of the literature review, which focuses on the diferences between the results of diferent MCDM methods. Tis section poses the question: "Which MCDM method is most suitable for solving complex material selection problems with a large number of alternatives and criteria?".

Dissimilarities in ranking results for material selection problems. Tis section discusses the application of various MCDM methods to the same material selection problems, which reveal that decision-makers may have diferent rankings using diferent methods. For instance, Singh et al.<sup>55</sup> used ELECTRE II to select the best material and compared the rankings derived using COPRAS, TOPSIS, VIKOR, SAW, MOORA, and PSI to validate the outputs. While all the methods identifed a similar alternative as the best, the rankings were slightly diferent. Similarly, Hafezalkotob & Hafezalkotob<sup>91</sup> compared the rankings produced by Target-based MULTI-MOORA method with two diferent modes and their aggregate ranking of with other methods including Targetbased TOPSIS, Target-based VIKOR and Interval target-based VIKOR methods. Despite generating diferent rankings, all methods, except for Target-based MULTIMOORA with an integrated signifcant coefcient (Mod 2), suggested the same material for the considered problem. However, the aggregate ranking methodology pro posed two materials as the best. To analyze the similarity of MCDM outputs, Spearman rank correlation coeffcient was also used which revealed diferences in the obtained rankings. Mousavi-Nasab & Sotoudeh-Anvari<sup>92</sup> presented fve material selection examples and compared the rankings using DEA, VIKOR, TOPSIS, ELECTRE II, and COPRAS methods. In the frst example, a signifcant diference in material ranking between DEA and other methods was observed, while in the second example, the results were more similar. Although the same material was selected by most methods, the rankings of the remaining materials varied signifcantly. Te authors also concluded that for material selection problems, it is more reliable to use multiple MCDM methods instead of relying on a single technique. In example 3, diferences were observed in the generated rankings and the selected materials. Similarly, the application of MCDM methods in the subsequent two examples demonstrated diferent ranking results and slight diferences in the selected materials. Te authors concluded that TOPSIS and COPRAS are more consistent, but using multiple MCDM methods to solve material selection problems is preferable. Another attempt to optimize decision-making in material selection problems can be found in the work of Zhang et al.<sup>93,</sup> where they proposed a new MCDM method. It was evident that changes in methods for computing a component of the decision-making process, such as criteria weights, could signifcantly impact the fnal results. Fuzzy BWM and fuzzy G-VIKOR methods were employed by Zhang et al.<sup>94</sup> to solve a material selection problem. To validate the results, a sensitivity analysis was conducted to explore the infuence of criteria weights on the fnal ranking. In<sup>54</sup> study, a sustainable building material selection problem was solved using ELECTRE III. Te results obtained from ELECTRE III were compared with SAW, TOPSIS, COPRAS, and MULTIMOORA. Additionally, sensitivity analysis was performed to demonstrate the superior performance of ELECTRE III compared to other MCDM methods. Consequently, if other MCDM methods are utilized by DMs for any reason, a poor material selection result might have been obtained. Another signifcant diference between the rankings of materials generated by diferent MCDM methods is highlighted in the work conducted by Chatterjee et al.<sup>95</sup>. COPRAS and EVAMIX methods were employed for solving material selection problems, and the results obtained from these methods were compared with TOPSIS, VIKOR, and AHP in terms of calculation time, simplicity, transparency, possibility of graphical interpretation, and information type, instead of using sensitivity analysis or Spearman’s rank correlation coefcient. Trough two examples, it was concluded that COPRAS and EVAMIX methods are applicable, capable, and accurate for solving material selection problems.

<table><tr><td>Author</td><td>Case application</td><td>Distance-based MCDM method</td></tr><tr><td>Xue et al.72</td><td>Automotive instrument panel</td><td>Interval-valued intuitionistic fuzzy MABAC</td></tr><tr><td>Tian et al.73</td><td>Building decoration material selection (Solid wood)</td><td>Grey correlation-TOPSIS</td></tr><tr><td>Ahmed et al.74</td><td>Ranking concrete supplementary material</td><td>TOPSIS</td></tr><tr><td>Deshmukh &amp; Angira75</td><td>Material selection problem for the bridge of RF-MEMS shunt capacitive switches</td><td>TOPSIS</td></tr><tr><td>Maghsoodi et al.76</td><td>Dam construction material selection</td><td>CODAS</td></tr><tr><td>Roy et al.77</td><td>Sustainable material selection in construction projects</td><td>Interval-valued intuitionistic fuzzy CODAS</td></tr><tr><td>Yadav et al.78</td><td>Material selection in marine applications</td><td>TOPSIS-PSI</td></tr><tr><td>Zhang et al.90</td><td>Bone transplant replacement material selection</td><td>TOPSIS</td></tr><tr><td>Dhanalakshmi et al.79</td><td>Pyrolysis material selection</td><td>TOPSIS and EDAS</td></tr><tr><td>Kar &amp; Jha80</td><td>Construction material selection</td><td>TOPSIS</td></tr><tr><td>Yang et al.82</td><td>Tribological coating material selection</td><td>TOPSIS</td></tr><tr><td>Kumar et al.83</td><td>Glazing material for solar thermal application</td><td>TOPSIS</td></tr><tr><td>Aires &amp; Ferreira84</td><td>Flywheel material selection</td><td>R-TOPSIS</td></tr><tr><td>Abishini &amp; Karthikeyan85</td><td>Aluminum alloy material selection for sheet metal forming process</td><td>EDAS</td></tr><tr><td>Kazemian et al.86</td><td>Material selection of intraoral stents</td><td>TOPSIS</td></tr><tr><td>Sharma et al.87</td><td>Lightweight material for railway vehicles</td><td>TOPSIS</td></tr><tr><td>Remadi &amp; Frikha88</td><td>Green material selection</td><td>Intuitionistic fuzzy CODAS</td></tr><tr><td>Wankhede et al.89</td><td>Selection of natural fiber for long lasting composites</td><td>CODAS</td></tr></table>

Table 3. Distance-based MCDM methods in materials selection.

## Research methodology

Te research methodology is constructed on three main procedures, 1. Computing the criteria weights; 2. Selecting the best material; and 3. Validating the obtained results. Te methodological process and the tools used in this paper are shown in Fig. 2.

![](images/d7656a85653020b505c6c435c2433103929598fab1561c736014e7b11d55ffab.jpg)  
Figure 2. Te methodological workfow.

Research tools. Tis section presents two main tools used to solve the material selection problem. It is divided into two sub-sections that address the issues mentioned previously. Te frst sub-section presents the new MCDM method called SRP. Te second sub-section presents VIMM, which is a subjective weighting method used in the frst scenario algorithm.

SRP. SRP method is a novel approach developed to solve MCDM problems. It is based on the ranks of alternatives in each criterion, which allows it to provide accurate and reliable outputs while avoiding the complexities of existing MCDM methods. Unlike other methods, SRP does not require a normalization process as it directly works with criteria weights. SRP has the following simple steps:

Step 1 Defning criteria for the evaluation of the alternatives where $A _ { i }$ signifes the alternatives, $c _ { j }$ states the criteria, and $i = \{ \bar { 1 } , \dots , m \}$ and $j = \{ 1 , \ldots , n \}$

Step 2 Establishing the decision matrix, where $X _ { i j }$ denote the decision matrix and $r _ { i j }$ expresses the score of i th alternative against jth criterion.

$$
X _ {i j} = r _ {i j}.\tag{1}
$$

Step 3 Determining the ranks of alternatives in each criterion where the ranking process is based on the higher value $\mathrm { o f } r _ { i j }$ in the benefcial criteria $( \operatorname* { m a x } _ { 1 \leq i \leq m } r _ { i j } )$ and lower value of $r _ { i j }$ in the non-benefcial criteria ( min $r _ { i j } )$ . Te 1≤i≤m following equation Eq. (2) demonstrates the new ranking matrix where $X _ { i j } ^ { ' }$ is the ranking matrix and $\mathbf { \chi } _ { R _ { i } } ^ { j }$ is the rank of i th alternative against jth criterion.

$$
X _ {i j} ^ {'} = R _ {i} ^ {j},\tag{2}
$$

Step 4 Te fourth step is the construction of the weighted ranking matrix according to Eq. (3), where $W _ { j }$ stands for the importance wrights of criteria and $X _ { i j } ^ { " }$ shows the weighted ranking matrix.

$$
X _ {i j} ^ {"} = W _ {j} R _ {i} ^ {j},\tag{3}
$$

Step 5 Computing the total ranking score of the alternatives as follows:

$$
S R _ {i} = \sum_ {j = 1} ^ {n} W _ {j} R _ {i} ^ {j},\tag{4}
$$

Step 6 Finally, prioritizing alternatives based on the higher value of $\Re _ { i } ,$ where m is the number of alternatives

$$
\mathfrak {R} _ {i} = m - S R _ {i}.\tag{5}
$$

VIMM: frst scenario algorithm. VIMM is a subjective weighting method that is developed to use less pair wise comparison and also distance-based computations to extract the most accurate weights from the decisionmakers’ opinions and judgments. VIMM is designed based on three main elements called vital, immaterial, and mediocre criteria. Te vital criterion plays the role of the most important criterion, which has the most impact in achieving the decision-making’s goal(s). It receives the highest value through computation. On the other hand, the immaterial criterion plays the opposite role and has the lowest impact on reaching the goal(s). Te frst vita and immaterial criteria select by the decision-maker(s), while the algorithm determines the following vital and immaterial criteria. Tere exists a third criterion, called the mediocre criterion. It refers to a criterion that afects reaching the decision-making goal to a lesser extent than the vital criteria and higher than the immaterial criterion. VIMM generates high-accuracy results and is more reliable than the popular MCDM weighting methods such as AHP.

Te following phases are proposed by Zakeri et al.<sup>9</sup> for the classic VIMM: the frst scenario to calculate the weights of criteria in a one-goal decision-making problem.

Step 1  The algorithm begins with determining the vital, immaterial, and mediocre criteria by the decision-makers.

Step 2 Afer selecting the vital and immaterial criteria, the second step is to allocate fve and one as the corresponding values for the vital and immaterial criteria, respectively.

Step 3 Comparing the remaining criteria against the vital and immaterial criteria following the numericallinguistic scale. To conduct the comparison, VIMM uses a scale to convert decision-makers’ subjective opinions into numbers within an interval of [2, 5, 9], in which decision-maker is able to select any rational number between these three numbers. Te scale is illustrated in Fig. 3.

![](images/a4d0decf80e39f9ec5821150d615e8597de47c0162f813af9814b572080e6311.jpg)  
Figure 3. Te linguistic/numeric variables scale.

Step 4 Establishing the distance matrix by calculating the distances between each criterion and the vital and immaterial criteria according to the linguistic/numeric scale in (Fig. 2) is the fourth step of the VIMM algorithm Tis step includes two steps:

Step 4.1 Normalizing the distance matrix by following Eqs. (6), (7), where $d _ { x y } ^ { + }$ and $d _ { x y } ^ { - }$ stand for distances between the yth criterion in the xth comparison, and the immaterial and vital criteria respectively, x states the number of comparison process, and y stands for the number of criteria.

$$
d^{+}{}^{\prime}_{xy} = c_{y / \max \limits_{y\in j}d^{+}_{xy}},y\in j,\tag{6}
$$

$$
d _ {x y} ^ {- \prime} = \min _ {y \in j} d _ {x y / d _ {x y} ^ {-}} ^ {-}, y \in j,\tag{7}
$$

Step 4.2 Computing the frst score Eq. (8), where $S _ { x y }$ denotes the score of the yth criterion in the xth comparison.

$$
S _ {x y} = d _ {x y} ^ {+ ^ {\prime}} + d _ {x y} ^ {- ^ {\prime}}.\tag{8}
$$

Phase 5 Re-executing steps 3 and 4 until the number of remaining criteria reaches 2 for an even number of criteria or 1 for an odd number of criteria.

Phase 6 Computing the weights of criteria according to Eqs. (9), (10), where $\begin{array} { r } { ( \sum _ { j = 1 } ^ { n } W _ { j } = 1 ) } \end{array}$

$$
\mathbb {S} _ {j} = \sum_ {y \in j} ^ {x} S _ {x y},\tag{9}
$$

$$
W _ {j} = \sum_ {j = 1} ^ {y} \mathbb {S} _ {j} y \in j.\tag{10}
$$

## Material selection via SRP and VIMM: the frst scenario methods

This section is divided into four sub-sections. In this first sub-section, the case study and the information on the materials, their properties, and the weights of the criteria for the evaluation of the materials are represented. In the second section, a group decision-making process conducted by seven experts is represented to select the vital and material criteria as the input for the VIMM method. VIMM method is applied to the case to compute the weights of criteria in the third section. Te evaluation process of the material is represented in the fourth sub-section, in which the SRP method is applied to select the best material.

Case study. <sup>96</sup> to store solar energy. Criteria taken in consideration are Latent Heat $J / \mathrm { K g } \left( c _ { 1 } \right) ,$ , Density Kg/m3 (c ), Specifc Heat kJ/kg ${ \mathrm { K } } ( c _ { 3 } ) ;$ , Specifc Heat kJ/kg K $( c _ { 4 } ) _ { : }$ , Termal Conductivity W/m K (c ) and Cost $\left( c _ { 6 } \right)$ . Among all the criterion Latent Heat, Density, Specifc Heat (solid), Specifc Heat (liquid) and Termal Conductivity are benefcial criterion i.e. higher the value better the alternative. Cost is non-benefcial criterion i.e. lower the value better the alternative. Nine alternatives are considered as the phase change material such as Calcium chloride hexa-hydrate (A1), Stearic acid (A2), p116 (A3), RT 60 (A4), Parafn wax RT 30 (A5), n-Docosane (A6), n-Octadecane (A7), n-Nonadecane (A8) and n-Eicosane (A9). Te information on the properties of the materials and the material selection’s decision matrix, including the materials and the criteria for the evaluation, is demonstrated in Tables 4 and 5 respectively. Te weights of the criteria are also illustrated in Table 6.

<table><tr><td rowspan="2">Phase change material (PCM)</td><td colspan="6">Material selection criteria</td></tr><tr><td>Latent heat J/Kg ( $c_1$ )</td><td>Density Kg/m3( $c_2$ )</td><td>Specific heat kJ/kg K (Cp(s))( $c_3$ )</td><td>Specific heat kJ/kg K (Cp(l))( $c_4$ )</td><td>Thermal conductivity W/m K ( $c_5$ )</td><td>Cost ( $c_6$ )</td></tr><tr><td>Calcium chloride hexahydrate (A1)</td><td>169.98</td><td>1560.0</td><td>1.4600</td><td>2.1300</td><td>1.0900</td><td>Very low</td></tr><tr><td>Stearic acid (A2)</td><td>186.50</td><td>903.00</td><td>2.8300</td><td>2.3800</td><td>0.1800</td><td>Very high</td></tr><tr><td>p116 (A3)</td><td>190.00</td><td>830.00</td><td>2.1000</td><td>2.1000</td><td>0.2100</td><td>Low</td></tr><tr><td>RT 60 (A4)</td><td>214.40</td><td>850.00</td><td>0.9000</td><td>0.9000</td><td>0.2000</td><td>Very low</td></tr><tr><td>Paraffin wax RT 30 (A5)</td><td>206.00</td><td>789.00</td><td>1.8000</td><td>2.4000</td><td>0.1800</td><td>Low</td></tr><tr><td>n-Docosane (A6)</td><td>194.60</td><td>785.00</td><td>1.9300</td><td>2.3800</td><td>0.2200</td><td>Low</td></tr><tr><td>n-Octadecane (A7)</td><td>245.00</td><td>773.22</td><td>0.3767</td><td>2.2670</td><td>0.1400</td><td>Low</td></tr><tr><td>n-Nonadecane (A8)</td><td>222.00</td><td>775.80</td><td>1.7189</td><td>1.9210</td><td>0.1420</td><td>High</td></tr><tr><td>n-Eicosane (A9)</td><td>247.00</td><td>776.33</td><td>0.7467</td><td>2.3770</td><td>0.1380</td><td>Low</td></tr></table>

Table 4. Properties of PCMs for solar energy devices.

<table><tr><td rowspan="2">PCM</td><td colspan="6">Material selection criteria</td></tr><tr><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td></tr><tr><td>A1</td><td>169.98</td><td>1560.0</td><td>1.4600</td><td>2.1300</td><td>1.0900</td><td>0.2550</td></tr><tr><td>A2</td><td>186.50</td><td>903.00</td><td>2.8300</td><td>2.3800</td><td>0.1800</td><td>0.7450</td></tr><tr><td>A3</td><td>190.00</td><td>830.00</td><td>2.1000</td><td>2.1000</td><td>0.2100</td><td>0.3350</td></tr><tr><td>A4</td><td>214.40</td><td>850.00</td><td>0.9000</td><td>0.9000</td><td>0.2000</td><td>0.2550</td></tr><tr><td>A5</td><td>206.00</td><td>789.00</td><td>1.8000</td><td>2.4000</td><td>0.1800</td><td>0.3350</td></tr><tr><td>A6</td><td>194.60</td><td>785.00</td><td>1.9300</td><td>2.3800</td><td>0.2200</td><td>0.3350</td></tr><tr><td>A7</td><td>245.00</td><td>773.22</td><td>0.3767</td><td>2.2670</td><td>0.1400</td><td>0.3350</td></tr><tr><td>A8</td><td>222.00</td><td>775.80</td><td>1.7189</td><td>1.9210</td><td>0.1420</td><td>0.6650</td></tr><tr><td>A9</td><td>247.00</td><td>776.33</td><td>0.7467</td><td>2.3770</td><td>0.1380</td><td>0.3350</td></tr></table>

Table 5. Material selection decision matrix.

<table><tr><td>Criteria</td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td></tr><tr><td>Weight</td><td>0.4901</td><td>0.1674</td><td>0.0528</td><td>0.0528</td><td>0.2109</td><td>0.0261</td></tr></table>

Table 6. Criteria weights for the considered material selection case study.

The group decision‑making process. In this section, in order to determine the vital and immaterial criteria as the main elements of VIMM algorithm, seven experts are employed to re-evaluate the material selection criteria weights. Te original criteria weights are exhibited in Table 6.

Te number of pairwise comparisons in VIMM for the even number of criteria is (n/2), where n is the number of criteria. Terefore, in this case, there are two comparison processes. Te seven experts are asked to select three criteria as the vital and immaterial criterion for each comparison based on the criteria priority of being the best choice to meet the properties of the vital or immaterial criteria. Table 7 demonstrates expert responses, where $\mathbb { Z } _ { \alpha _ { x } } ^ { y } { \mathrm { a n d } } \mathbb { Z } _ { \beta _ { \mathrm { } } } ^ { y }$ represent diferent choice of decision-makers in the selection of vital and immaterial criteria in each comparison, y shows the priority of the selected criterion, x indicates the number of comparison process, <sup>N</sup> is the set of natural numbers, and $\psi _ { \mathbb { Z } _ { \alpha } ^ { y } . }$ and $\psi _ { \mathbb { Z } _ { \beta _ { 1 } } ^ { y } }$ are the cardinal numbers, representing the frequency of the criteria that decision-makers selected as the vital and immaterial criteria respectively see Eqs. (11) and (12).

$$
\psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {1}} \leq \psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {2}} \leq \psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {3}}, 1 \leq y \leq 3, y \in \mathbb {N}, x = n / 2, (n - 1) / 2, n \in j,\tag{11}
$$

$$
\psi_ {\mathbb {Z} _ {\beta_ {x}} ^ {1}} \leq \psi_ {\mathbb {Z} _ {\beta_ {x}} ^ {2}} \leq \psi_ {\mathbb {Z} _ {\beta_ {x}} ^ {3}}, 1 \leq y \leq 3, y \in \mathbb {N}, x = n / 2, (n - 1) / 2, n \in j.\tag{12}
$$

Table 8 shows the response distribution, where $F _ { c _ { j } }$ denotes the frequency of the criterion in each choice for the selection of the vital and immaterial criterion in the comparison processes. According to the distribution of responses of DMs (Table 8), the vital and immaterial selected by DMs criteria are shown in Tables 9 and 10.

<table><tr><td></td><td colspan="3"> $\alpha_1$ </td><td colspan="3"> $\beta_1$ </td><td colspan="3"> $\alpha_2$ </td><td colspan="3"> $\beta_2$ </td></tr><tr><td>Expert</td><td> $\mathbb{Z}_{\alpha_1}^1$ </td><td> $\mathbb{Z}_{\alpha_1}^2$ </td><td> $\mathbb{Z}_{\alpha_1}^3$ </td><td> $\mathbb{Z}_{\beta_1}^1$ </td><td> $\mathbb{Z}_{\beta_1}^2$ </td><td> $\mathbb{Z}_{\beta_1}^3$ </td><td> $\mathbb{Z}_{\alpha_2}^1$ </td><td> $\mathbb{Z}_{\alpha_2}^2$ </td><td> $\mathbb{Z}_{\alpha_2}^3$ </td><td> $\mathbb{Z}_{\beta_2}^1$ </td><td> $\mathbb{Z}_{\beta_2}^2$ </td><td> $\mathbb{Z}_{\beta_2}^3$ </td></tr><tr><td>1</td><td> $c_1$ </td><td> $c_1$ </td><td> $c_1$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_5$ </td><td> $c_2$ </td><td> $c_2$ </td><td> $c_4$ </td><td> $c_4$ </td><td> $c_3$ </td></tr><tr><td>2</td><td> $c_1$ </td><td> $c_1$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_6$ </td></tr><tr><td>3</td><td> $c_5$ </td><td> $c_5$ </td><td> $c_1$ </td><td> $c_4$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $c_4$ </td><td> $c_4$ </td></tr><tr><td>4</td><td> $c_1$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_6$ </td><td> $c_4$ </td><td> $c_2$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $c_4$ </td><td> $c_3$ </td></tr><tr><td>5</td><td> $c_1$ </td><td> $c_5$ </td><td> $c_2$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_1$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_4$ </td></tr><tr><td>6</td><td> $c_1$ </td><td> $c_1$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_3$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_3$ </td><td> $c_3$ </td><td> $c_6$ </td></tr><tr><td>7</td><td> $c_1$ </td><td> $c_1$ </td><td> $c_1$ </td><td> $c_4$ </td><td> $c_6$ </td><td> $c_6$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_5$ </td><td> $c_4$ </td><td> $c_3$ </td><td> $c_6$ </td></tr></table>

Table 7. Responses of decision-makers for selection of vital and immaterial criteria in the two comparison processes.

<table><tr><td rowspan="2">Criteria</td><td colspan="12"> $F_{cj}$ </td></tr><tr><td> $\psi_{\mathbb{Z}_{\alpha_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^3}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^3}$ </td></tr><tr><td> $c_1$ </td><td>6</td><td>5</td><td>3</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_2$ </td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_3$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3</td><td>2</td><td>2</td></tr><tr><td> $c_4$ </td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>5</td><td>2</td></tr><tr><td> $c_5$ </td><td>1</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>4</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_6$ </td><td>0</td><td>0</td><td>0</td><td>4</td><td>6</td><td>4</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>3</td></tr></table>

Table 8. Distribution of decision-makers’ responses.

<table><tr><td>Criteria</td><td> $\psi_{\mathbb{Z}_{\alpha_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^3}$ </td></tr><tr><td> $c_1$ </td><td>6</td><td>5</td><td>3</td><td>2</td><td>0</td><td>0</td></tr><tr><td> $c_2$ </td><td>0</td><td>0</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td> $c_3$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_4$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_5$ </td><td>1</td><td>2</td><td>2</td><td>4</td><td>5</td><td>5</td></tr><tr><td> $c_6$ </td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 9. Distribution of decision-makers’ responses regarding the vital criterion.

<table><tr><td>Criteria</td><td> $\psi_{\mathbb{Z}_{\beta_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^3}$ </td></tr><tr><td> $c_1$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_2$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_3$ </td><td>1</td><td>1</td><td>1</td><td>3</td><td>2</td><td>2</td></tr><tr><td> $c_4$ </td><td>2</td><td>0</td><td>2</td><td>2</td><td>5</td><td>2</td></tr><tr><td> $c_5$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $c_6$ </td><td>4</td><td>6</td><td>4</td><td>2</td><td>0</td><td>3</td></tr></table>

Table 10. Distribution of decision-makers’ responses regarding the immaterial criterion.

Determining the vital and immaterial criteria. Te collected data in the previous section are evaluated in this section to determine the vital and immaterial criteria. Te evaluation comprises two steps as follows:

Step 1 Te frst step of the evaluation process of decision-makers’ opinions is to compute the value of frequency of vital and immaterial criteria. Te step is conducted using Eqs. (13), (14), (15), (16) and (17).

$$
V _ {F _ {c _ {j}}} ^ {\alpha_ {x}} = (y \pm \xi) \psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {1}} + ((y - 1) \pm \mu) \psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {2}} + ((y - 2) \pm \nu) \psi_ {\mathbb {Z} _ {\alpha_ {x}} ^ {3}};\tag{13}
$$

$$
V _ {F _ {c _ {j}}} ^ {\beta_ {x}} = (y \pm \xi) \psi_ {\mathbb {Z} _ {\beta_ {1}} ^ {1}} + ((y - 1) \pm \mu) \psi_ {\mathbb {Z} _ {\beta_ {1}} ^ {2}} + ((y - 2) \pm \nu) \psi_ {\mathbb {Z} _ {\beta_ {1}} ^ {3}};\tag{14}
$$

$$
\xi = \left\{ \begin{array}{c} 0 \leq \xi \leq y, y + \xi \\ 0 <   \xi , y - \xi \end{array} ; \right.\tag{15}
$$

$$
\mu = \left\{ \begin{array}{l} 0 \leq \mu \leq y, (y - 1) - \mu \\ y > \mu + 1, (y - 1) - \mu \end{array} ; \right.\tag{16}
$$

$$
\nu = \left\{ \begin{array}{l} 0 \leq \nu \leq y, (y - 2) + \nu \\ y > \nu + 2, (y - 2) - \nu \end{array} ; \right.\tag{17}
$$

where the values of $\xi , \mu$ , and ν are determined by decision-makers.

Step 2 Te second step is to determine the vital and immaterial criteria in each comparison which is computed with the selection of the maximum value of Eqs. (13), (14), where.max $V _ { F _ { i _ { j } } } ^ { \alpha _ { x } }$ and $\underset { 1 \leq j \leq 6 } { m a x } \dot { V } _ { F _ { j } } ^ { \beta _ { x } }$ are the vital and imma-1≤j≤6 terial in xth comparison.

<table><tr><td>Criteria</td><td> $\psi_{\mathbb{Z}_{\alpha_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\alpha_2}^3}$ </td><td> $V_{F_{cj}}^{\alpha_1}$ </td><td> $V_{F_{cj}}^{\alpha_2}$ </td><td> $\max_{1 \leq j \leq 6} V_{F_{cj}}^{\alpha_1}$ </td><td> $\max_{1 \leq j \leq 6} V_{F_{cj}}^{\alpha_2}$ </td></tr><tr><td> $c_1$ </td><td>9</td><td>7</td><td>4</td><td>5</td><td>2</td><td>1</td><td>20</td><td>8</td><td></td><td rowspan="4"></td></tr><tr><td> $c_2$ </td><td>3</td><td>2</td><td>3</td><td>4</td><td>4</td><td>3</td><td>8</td><td>11</td><td rowspan="5"></td></tr><tr><td> $c_3$ </td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>6</td><td>6</td></tr><tr><td> $c_4$ </td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>6</td><td>6</td></tr><tr><td> $c_5$ </td><td>4</td><td>4</td><td>3</td><td>7</td><td>7</td><td>6</td><td>11</td><td>20</td><td></td></tr><tr><td> $c_6$ </td><td>3</td><td>2</td><td>5</td><td>3</td><td>2</td><td>1</td><td>10</td><td>6</td><td></td></tr></table>

Table 11. Te vital criteria selection for two comparison processes based on expert opinions.

<table><tr><td>Criteria</td><td> $\psi_{\mathbb{Z}_{\beta_1}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_1}^3}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^1}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^2}$ </td><td> $\psi_{\mathbb{Z}_{\beta_2}^3}$ </td><td> $V_{F_{cj}}^{\beta_1}$ </td><td> $V_{F_{cj}}^{\beta_2}$ </td><td> $\max_{1 \leq j \leq 6} V_{F_{cj}}^{\beta_1}$ </td><td> $\max_{1 \leq j \leq 6} V_{F_{cj}}^{\beta_2}$ </td></tr><tr><td> $c_1$ </td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>6</td><td>6</td><td rowspan="5"></td><td></td></tr><tr><td> $c_2$ </td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>6</td><td>6</td><td></td></tr><tr><td> $c_3$ </td><td>4</td><td>3</td><td>2</td><td>6</td><td>4</td><td>3</td><td>9</td><td>13</td><td></td></tr><tr><td> $c_4$ </td><td>5</td><td>2</td><td>3</td><td>5</td><td>7</td><td>3</td><td>10</td><td>15</td><td></td></tr><tr><td> $c_5$ </td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>6</td><td>6</td><td rowspan="2"></td></tr><tr><td> $c_6$ </td><td>7</td><td>8</td><td>5</td><td>5</td><td>2</td><td>4</td><td>20</td><td>11</td><td></td></tr></table>

Table 12. Te immaterial criteria selection for two comparison processes based on the experts’ opinion.

In this case, we consider $\xi , \mu , \nu = 0$ for the selection of the immaterial and vital criteria. According to Eqs. (13) and (14), results of the evaluation of the decision-makers’ opinions are demonstrated in Tables 11 and 12 where c1 (Latent Heat) is determined as the vital in the first comparison, and $c _ { 5 }$ (Thermal Conductivity) is determined as the second vital criterion in the second comparison. Criterion $c _ { 6 } \left( \mathrm { C o s t } \right)$ plays the immaterial criterion role and $c _ { 4 }$ (Specifc Heat) is selected by the experts to afect the criteria weighting process as the second immaterial criterion in the second comparison, as shown in Table 12 of the frst comparison.

Computing weights of criteria. Te prerequisite of VIMM algorithm is the goal defnition, where if there is one goal for the decision-making problem, the frst scenario ought to be employed; otherwise, VIMM: the second scenario must be used. Tis paper’s case follows one goal: selecting the most proper phase change material to store solar energy.

Since the weights were computed $\mathrm { i n } ^ { 9 6 }$ work, in contrast to the classic VIMM and instead of using the algorithm for the computation of the vital and immaterial criteria, we relied on the experts’ opinions and the vital and immaterial criteria in the second comparison are selected by them. In our case, there are no mediocre criteria selected by decision-makers.

Te frst step of computing weights of criteria is to allocate 5 and 1 to the frst selected vital and immaterial criteria which are $c _ { 1 } ,$ the Latent Heat, and $c _ { 6 } ,$ the Cost, then:

$$
c _ {1} = 5
$$

$$
c _ {6} = 1
$$

Te seven experts are asked to give their expert opinions to run the comparison. Te frst two comparisons of the remaining criteria and the selected vital and immaterial are shown in Tables 13 and 14, where the scale as illustrated in Fig. 2 is used to conduct the comparison. Te next phase is to compute the distances between all criteria, and the vital and immaterial criteria are shown in Table 15, where $d ^ { + }$ stands for the distance between the criteria and the immaterial criterion, while d<sup>−</sup> displays the distance between the criteria and the vital criterion. To display the computation of $d ^ { + }$ and $d ^ { - }$ , the following examples are provided. Te normalized distance matrix, as shown in Table 16, is derived using Eqs. 6, and 7, where $d ^ { + \prime }$ and $d ^ { - \prime }$ indicate the normalized distances

<table><tr><td>Criteria</td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td></tr><tr><td> $c_1$ </td><td>6.166</td><td>3.882</td><td>3.827</td><td>7.053</td></tr><tr><td>Criteria</td><td> $c_{2}$ </td><td> $c_{3}$ </td><td> $c_{4}$ </td><td> $c_{5}$ </td></tr><tr><td> $c_{6}$ </td><td>6.414</td><td>2.126</td><td>2.023</td><td>8.080</td></tr></table>

Table 13. Comparison of latent heat (vital criterion) with other criteria.

Table 14. Comparison of cost (immaterial criterion) against other criteria.

<table><tr><td>Criteria</td><td> $d^{+'}$ </td><td> $d^{-'}$ </td></tr><tr><td> $c_2$ </td><td>5.414</td><td>3.834</td></tr><tr><td> $c_3$ </td><td>1.126</td><td>6.118</td></tr><tr><td> $c_4$ </td><td>1.023</td><td>6.173</td></tr><tr><td> $c_5$ </td><td>7.080</td><td>2.947</td></tr><tr><td>Max</td><td>7.080</td><td></td></tr><tr><td>Min</td><td></td><td>6.173</td></tr></table>

Table 15. Distances between the criteria and frst vital and immaterial criteria.

$$
d _ {\mathrm{Density}} ^ {+} = 6. 4 1 4 - 1
$$

$$
d _ {\mathrm{Density}} ^ {-} = 1 0 - 6. 1 6 6
$$

Te next step is to compute the frst criteria’ scores and identify the second vital and immaterial using the VIMM algorithm’s “step no $4 . 2 ^ { \dag }$ and Eq. (8).

Similar to what have been selected by decision-makers (shown in Tables 11 and 12), as displayed in Table 17, Specifc Heat and Termal Conductivity are calculated as the immaterial and vital criteria, respectively. In the next step, the remaining criteria are compared with the second vital and immaterial criteria, the Termal Conductivity and the Specifc Heat. Te comparisons are conducted by decision-makers as presented in Tables 16

<table><tr><td>Criteria</td><td> $d^{+}$ </td><td> $d^{-}$ </td></tr><tr><td> $c_{2}$ </td><td>0.765</td><td>1.610</td></tr><tr><td> $c_{3}$ </td><td>0.159</td><td>1.009</td></tr><tr><td> $c_{4}$ </td><td>0.144</td><td>1.000</td></tr><tr><td> $c_{5}$ </td><td>1.000</td><td>2.095</td></tr></table>

Table 16. Normalized distance matrix.

<table><tr><td>Criteria</td><td> $d^{+'}$ </td><td> $d^{-'}$ </td><td> $S_x$ </td><td>Vital</td><td>Immaterial</td></tr><tr><td> $c_2$ </td><td>0.513</td><td>0.753</td><td>2.374</td><td></td><td></td></tr><tr><td> $c_3$ </td><td>1</td><td>0.455</td><td>1.168</td><td></td><td></td></tr><tr><td> $c_4$ </td><td>0.965</td><td>0.460</td><td>1.144</td><td></td><td></td></tr><tr><td> $c_5$ </td><td>0.466</td><td>1</td><td>3.095</td><td></td><td></td></tr></table>

Table 17. Te frst scores, and the second vital and immaterial criteria.

<table><tr><td>Criteria</td><td> $c_{2}$ </td><td> $c_{3}$ </td></tr><tr><td> $c_{5}$ </td><td>0.1674</td><td>0.0555</td></tr><tr><td> $c_{4}$ </td><td>0.1674</td><td>0.0555</td></tr></table>

Table 18. Comparison of the vital criterion c5(thermal conductivity) with the remaining criteria.

Table 19. Comparison of the immaterial criterion, c4(specifc heat, (Cp(l)), against the remaining criteria.

<table><tr><td>Criteria</td><td> $d^{+}$ </td><td> $d^{-}$ </td><td> $d^{+'}$ </td><td> $d^{-'}$ </td><td> $S_{x}$ </td></tr><tr><td> $c_{2}$ </td><td>2.170</td><td>2.063</td><td>1</td><td>1</td><td>2.000</td></tr><tr><td> $c_{3}$ </td><td>0.051</td><td>7.368</td><td>0.024</td><td>0.280</td><td>0.303</td></tr><tr><td>Max</td><td>2.170</td><td></td><td rowspan="2" colspan="3"></td></tr><tr><td>Min</td><td></td><td>2.063</td></tr></table>

Table 20. Normalized distance matrix and second scores of criteria.

<table><tr><td>Criteria</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td>Vital</td><td>Immaterial</td></tr><tr><td> $c_1$ </td><td>5</td><td>5</td><td>5</td><td></td><td rowspan="2">The vital criterion extracted from  $S_2$ </td></tr><tr><td> $c_2$ </td><td>2.374</td><td>2.000</td><td>5</td><td></td></tr><tr><td> $c_3$ </td><td>1.168</td><td>0.303</td><td>1</td><td></td><td></td></tr><tr><td> $c_4$ </td><td>1.144</td><td>1</td><td>0</td><td></td><td></td></tr><tr><td> $c_5$ </td><td>3.095</td><td>5</td><td>5</td><td></td><td></td></tr><tr><td> $c_6$ </td><td>1</td><td>0</td><td>0</td><td></td><td></td></tr></table>

Table 21. Final comparison process. Signifcant values are in bold.

<table><tr><td>Criteria</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $\mathbb{S}_j$ </td><td> $W_j$ </td></tr><tr><td> $c_1$ </td><td>5</td><td>5</td><td>5</td><td>15</td><td>0.348</td></tr><tr><td> $c_2$ </td><td>2.374</td><td>2.000</td><td>5</td><td>9.374</td><td>0.218</td></tr><tr><td> $c_3$ </td><td>1.168</td><td>0.303</td><td>1</td><td>2.471</td><td>0.057</td></tr><tr><td> $c_4$ </td><td>1.144</td><td>1</td><td>0</td><td>2.144</td><td>0.050</td></tr><tr><td> $c_5$ </td><td>3.095</td><td>5</td><td>5</td><td>13.095</td><td>0.304</td></tr><tr><td> $c_6$ </td><td>1</td><td>0</td><td>0</td><td>1</td><td>0.023</td></tr></table>

Table 22. Derived criteria weights.

and 17, and the corresponding scores are given in Tables 18 and 19, and the normalized distance matrix is illustrated in Table 20.

Te fnal phase is the computation of the weights, which are extracted from the scores. To do that, frst, the scores need to be calculated. Te fnal comparison is shown in (Table 21) in which Density is the fnal vital criterion and the Specifc Heat (Cp(s)) is the last immaterial criterion. Te scoring continues until all criteria received their fnal 5 and 1 values. Te allocation of value to the vital criteria continues to the last comparison, while the immaterial criteria receive merely one time their corresponding value. Te criteria weights as derived using Eqs. (9) and (10) are the displayed in Table 22.

<table><tr><td> $W_j$ </td><td>0.348</td><td>0.218</td><td>0.057</td><td>0.050</td><td>0.304</td><td>0.023</td><td colspan="6"></td></tr><tr><td>PCM</td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td></tr><tr><td>A1</td><td>9</td><td>1</td><td>6</td><td>5</td><td>1</td><td>1</td><td>3.132</td><td>0.218</td><td>0.342</td><td>0.25</td><td>0.304</td><td>0.023</td></tr><tr><td>A2</td><td>8</td><td>2</td><td>1</td><td>2</td><td>5</td><td>5</td><td>2.784</td><td>0.436</td><td>0.057</td><td>0.1</td><td>1.52</td><td>0.115</td></tr><tr><td>A3</td><td>7</td><td>4</td><td>2</td><td>6</td><td>3</td><td>2</td><td>2.436</td><td>0.872</td><td>0.114</td><td>0.3</td><td>0.912</td><td>0.046</td></tr><tr><td>A4</td><td>4</td><td>3</td><td>7</td><td>8</td><td>4</td><td>1</td><td>1.392</td><td>0.654</td><td>0.399</td><td>0.4</td><td>1.216</td><td>0.023</td></tr><tr><td>A5</td><td>5</td><td>5</td><td>4</td><td>1</td><td>5</td><td>2</td><td>1.74</td><td>1.09</td><td>0.228</td><td>0.05</td><td>1.52</td><td>0.046</td></tr><tr><td>A6</td><td>6</td><td>6</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2.088</td><td>1.308</td><td>0.171</td><td>0.1</td><td>0.608</td><td>0.046</td></tr><tr><td>A7</td><td>2</td><td>9</td><td>9</td><td>4</td><td>7</td><td>2</td><td>0.696</td><td>1.962</td><td>0.513</td><td>0.2</td><td>2.128</td><td>0.046</td></tr><tr><td>A8</td><td>3</td><td>8</td><td>5</td><td>7</td><td>6</td><td>4</td><td>1.044</td><td>1.744</td><td>0.285</td><td>0.35</td><td>1.824</td><td>0.092</td></tr><tr><td>A9</td><td>1</td><td>7</td><td>8</td><td>3</td><td>8</td><td>3</td><td>0.348</td><td>1.526</td><td>0.456</td><td>0.15</td><td>2.432</td><td>0.069</td></tr></table>

Table 23. Weighted ranking matrix using group decision-making and VIMM: the frst scenario.

<table><tr><td>PCM</td><td> $SR_i$ </td><td> $\mathfrak{R}_i$ </td><td>Rank by SRP</td></tr><tr><td>A1</td><td>4.269</td><td>4.731</td><td>2</td></tr><tr><td>A2</td><td>5.012</td><td>3.988</td><td>7</td></tr><tr><td>A3</td><td>4.68</td><td>4.32</td><td>5</td></tr><tr><td>A4</td><td>4.084</td><td>4.916</td><td>1</td></tr><tr><td>A5</td><td>4.674</td><td>4.326</td><td>4</td></tr><tr><td>A6</td><td>4.321</td><td>4.679</td><td>3</td></tr><tr><td>A7</td><td>5.545</td><td>3.455</td><td>9</td></tr><tr><td>A8</td><td>5.339</td><td>3.661</td><td>8</td></tr><tr><td>A9</td><td>4.981</td><td>4.019</td><td>6</td></tr></table>

Table 24. Total ranking scores of materials along with derived ranking.

Ranking materials. Te fnal step in evaluating the materials is to derive the ranking orders of the alternatives using SRP which is based on ranking each alternative in relation to each criterion. Te weighted ranking matrix, obtained from the material evaluation decision matrix of Table 5 using Eqs. (2) and (3), is shown in Table 23. Te ranking order, as presented in Table 24, is determined using the total ranking scores of the alternatives, calculated in the ffh stage of SRP method using Eq. (4). Te ranks of the materials are fnally shown in the same table employing Eq. (6) which indicates RT 60 (A4) as the best material to choose for the considered application.

## Discussion

Tis paper introduced SRP to solve material selection problems. In this new method, the importance weights of criteria play the leading role in evaluating the decision-making problems’ alternatives. Since the new method algorithm’s process is mainly grounded on the ranks of each alternative against each criterion, it heavily relies on the weights of each criterion.

SRP is applied to a material selection problem to evaluate a set of materials used to store solar energy. Although the criteria weights have already been determined by Rathod and Kanzaria<sup>96</sup>, yet we asked seven experts to re-evaluate the criteria. VIMM, a reliable MCDM subjective weighting method, is used for extracting opinions of the decision-makers. Te original criteria weights, as determined by Rathod and Kanzaria<sup>96</sup>, are also utilized to compare the diferences between the produced results in order to show how sensitive the SRP is to the criteria weights (see Table 25).

Te diference between the two rankings is illustrated in Fig. 4. To better understand the sensitivity of SRP to criteria weights, diferent weight sets computed by two most popular MCDM objective weighting methods namely Shannon’s entropy and CRITIC are considered here. Te set of weights computed by Entropy and CRITIC methods are as follows:

$$
W _ {j} ^ {\text { entropy }} = \{0. 0 1 2, 0. 0 5 0, 0. 1 9 4, 0. 0 4 6, 0. 5 7 1, 0. 1 2 8 \},
$$

$$
W _ {j} ^ {\text { CRITIC }} = \{0. 2 2 7, 0. 1 3 4, 0. 1 7 6, 0. 1 5 1, 0. 1 3 1, 0. 1 8 0 \}.
$$

Figure 5 shows considerable diferences between the ranks of the results afected by distinctive weights derived by diferent MCDM weighting methods, including objective and subjective approaches. Tis fgure also demonstrates high sensitivity of SRP to criteria weighting. Reliability of SRP is directly related to the reliability

Ranking with the CRITIC weights Ranking with the Entropy weights

<table><tr><td> $W_j$ </td><td>0.4901</td><td>0.1674</td><td>0.0528</td><td>0.0528</td><td>0.2109</td><td>0.0261</td><td colspan="3">SRP calculations</td></tr><tr><td>PCM</td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $SR_i$ </td><td> $\mathfrak{R}_i$ </td><td>Ranking</td></tr><tr><td>A1</td><td>9</td><td>1</td><td>6</td><td>5</td><td>1</td><td>1</td><td>5.3961</td><td>3.6039</td><td>9</td></tr><tr><td>A2</td><td>8</td><td>2</td><td>1</td><td>2</td><td>5</td><td>5</td><td>5.599</td><td>3.401</td><td>8</td></tr><tr><td>A3</td><td>7</td><td>4</td><td>2</td><td>6</td><td>3</td><td>2</td><td>5.2076</td><td>3.7924</td><td>7</td></tr><tr><td>A4</td><td>4</td><td>3</td><td>7</td><td>8</td><td>4</td><td>1</td><td>4.1243</td><td>4.8757</td><td>2</td></tr><tr><td>A5</td><td>5</td><td>5</td><td>4</td><td>1</td><td>5</td><td>2</td><td>4.6582</td><td>4.3418</td><td>3</td></tr><tr><td>A6</td><td>6</td><td>6</td><td>3</td><td>2</td><td>2</td><td>2</td><td>4.683</td><td>4.317</td><td>4</td></tr><tr><td>A7</td><td>2</td><td>9</td><td>9</td><td>4</td><td>7</td><td>2</td><td>4.7017</td><td>4.2983</td><td>5</td></tr><tr><td>A8</td><td>3</td><td>8</td><td>5</td><td>7</td><td>6</td><td>4</td><td>4.8129</td><td>4.1871</td><td>6</td></tr><tr><td>A9</td><td>1</td><td>7</td><td>8</td><td>3</td><td>8</td><td>3</td><td>4.0082</td><td>4.9918</td><td>1</td></tr></table>

Table 25. New ranking orders obtained using the original weights, estimated by Rathod and Kanzaria<sup>96</sup>.

![](images/bb3eb872e3633f9405a258e8c463993991c86d6b6d73017585195baa3c8d5b53.jpg)  
Figure 4. Comparative analysis of rankings afected by the criteria weights computed by the VIMM method and the original criteria weights.

![](images/1d6a561adb7fb7da1c74aced50a1b642107e08a5309e2dd3053c5e64832c10da.jpg)  
Figure 5. Comparative analysis of rankings afected by diferent weights computed by VIMM, CRITIC, Entropy, and original methods.

of weighting method used to assess the criteria under investigation. In this paper, VIMM method is used as a subjective weighting tool to derive criteria weights from decision-makers’ opinions. Tis goal-oriented MCDM weighting method is more reliable than classic forms of BWM and AHP. According to Zakeri et al.<sup>9</sup>, there are three main advantages of VIMM over the mentioned weighting methods including fewer number pairwise com parison, where n(n − 1)/2 and 2n − 3 number of comparisons are required for AHP and BWM respectively, while VIMM needs merely (n − 1)/2 and n/2 number of comparisons for even and odd numbers of criteria in the evaluation process. In contrast to AHP method, VIMM is not limited to the number of criteria since it re-evaluates the criteria in every process. VIMM is designed to consider the decision-making goal(s) by proposing two scenarios, where the frst scenario is developed to evaluate the weights of criteria in a decision-making problem with one goal, and the second scenario is developed to consider more than one goal in its process of the computation of the criteria weights. Tus, it is a proper pair for SRP in ranking alternatives to a decision-making problem.

Four MCDM methods, including WPM, VIKOR, and TOPSIS have also been applied to compare the results obtained from SRP. Te diference between rankings is pictured in Fig. 6.

Figure 6 demonstrates that there is no compromise in ranking among the four methods. Tus, the comparison of MCDM results in the previous section cannot be used to validate the fndings, leading to the next section.

The compromise decision index (CDI). In complex MCDM problems with several alternatives and criteria, irregularity in the result of comparing the generated rankings is inevitable. As shown in the previous section, there is an irregularity in the rankings generated by the MCDM methods; therefore, for these types of situations, we have proposed an index called CDI to interpret the comparison between the outputs of MCDM methods in the processes that at least four MCDM methods are applied to solve an MCDM problem $( \mathrm { K } \geq 4 ) _ { : }$ where K denotes the number of MCDM methods, the number of alternatives equals $m \geq 2 \mathrm { K }$ , and the number of criteria equals $n \geq ( 2 k - 2 )$ , which is the limitation of AHP in the evaluation of criteria where it is restricted to seven $( + / - 2 )$ criteria<sup>9</sup>.

![](images/1ead99bdc198a9089d7cca044d24bace1ca92f0f06b2ffa75bd0a2bb841dbb8f.jpg)  
Figure 6. Comparison between rankings generated by four MCDM methods

Te following steps shows the computation process of CDI.

Step 1 Computing the performance of each alternative in accordance with Eqs. (18) and (19) respectively, where $\delta _ { i }$ is the performance of i th alternative, $\zeta _ { \mathbb { R } }$ denotes weight of each rank, <sup>R</sup> stands for each rank, and $A _ { i }$ states the i th alternative.

$$
\delta_ {i} = \zeta_ {\mathbb {R} _ {i}} F _ {A _ {i}} ^ {\mathbb {R} _ {i}}, i = \{1, 2, \ldots , m \}, F _ {A _ {i}} ^ {\mathbb {R} _ {i}} \leq \mathrm{K},\tag{18}
$$

$$
\zeta_ {\mathbb {R} _ {i}} = \left(\sum \zeta_ {\mathbb {R} _ {i}}\right) ^ {- 1} (m - \mathbb {R} _ {i} + 1),\tag{19}
$$

Step 2 Ranking alternatives according to the higher value of $\cdot _ { \delta _ { i } . }$

Step 3 Calculating the deviation of each ranking fashioned by each MCDM method to the performance of alternative, according to (Eq. (20)).

$$
\sigma_ {i} = \sqrt {\sum_ {K = 1} ^ {z} \left(X _ {i} - Y _ {i} ^ {K}\right) ^ {2}}, K = \{1,.., z \}, i = \{1, \dots , m \},\tag{20}
$$

Step 4 Te fnal step is the computation of CDI values using Eq. (21).

$$
C D I = 1 / 1 0 0 \sum_ {i = 1} ^ {m} \sigma_ {i}.\tag{21}
$$

CDI puts the results of MCDM methods in four types of compromises: Pragmatic compromise, Rational compromise, Fair compromise, and Rotten compromise. Te results are interpreted concerning these compromises according to the defned categories provided by Wendt<sup>97</sup>.

Te pragmatic compromise. When there is a pragmatic reason for compromise, the pragmatic compromise makes. When CDI shows the ranks have pragmatic compromise, results of the MCDM method are considered to be reliable.

Te rational compromise. According to Wendt.<sup>97</sup>, a compromise is rational when it is rational for all parties to agree on the compromise. When CDI interprets the comparison of ranks as the rational compromise, ranking produced by the MCDM method is reliable to some extent. However, it is better to add another MCDM method to reach a pragmatic compromise.

Te fair compromise. When a fair compromise is made in the comparison analysis, decision-makers could decide whether to consider the compromise as a rational compromise or rely on the practical results

Te rotten compromise. According to Wendt.<sup>97</sup>, the purpose of introducing the concept of a "rotten compromise" is to have a term that signifes compromises that are morally dubious or unethical. When CDI interprets the results as a rotten compromise, it means that the results of MCDM methods cannot be validated theoreti cally, and practical results must be evaluated and validated.

![](images/bad6fb369b586e535c9e231ec74a8fdfb35024599f18e406e8abb09a41ce2822.jpg)  
Figure 7. Interpretation of the MCDM results comparison based on the CDI.

![](images/af210cf4a1baaa5fdd1756dc77036686261c5a5ee167cfe56a07f877d5f30986.jpg)  
Figure 8. Distribution of each material rank according to the MCDM methods.

To interpret the results in accordance with the categories, frst the maximum deviation needs to be computed. Te minimum deviation equals to zero, where all the applied MCDM methods generated the same results. Te interpretation of the results is based on Fig. 7, where

$$
C D I _ {1} = \max _ {1 \leq i \leq m} \sigma_ {i} / 4,\tag{22}
$$

$$
C D I _ {2} = \max _ {1 \leq i \leq m} \sigma_ {i} / 2,\tag{23}
$$

$$
C D I _ {3} = \max _ {1 \leq i \leq m} \sigma_ {i}.\tag{24}
$$

To interpret the obtained results from the comparison between the MCDM results with CDI, the distribution of the materials’ rankings generated by the four MCDM methods needs to be calculated (see Fig. 8). According to Eqs. (18) and (19), performance of the materials is shown in Table 26. According to Eqs. (20), (21), CDI = 0.430705. According to Eqs. (22), (23), (24), the interpretation of CDI is the fair compromise (see Fig. 9), where max $\sigma _ { i } = 0 . 6 4 .$ 1≤i≤m

$$
C D I _ {1} = 0. 1 6
$$

<table><tr><td rowspan="2"> $\zeta_{\mathbb{R}_{i}}$ </td><td> $\mathbb{R}_{1}$ </td><td> $\mathbb{R}_{2}$ </td><td> $\mathbb{R}_{3}$ </td><td> $\mathbb{R}_{4}$ </td><td> $\mathbb{R}_{5}$ </td><td> $\mathbb{R}_{6}$ </td><td> $\mathbb{R}_{7}$ </td><td> $\mathbb{R}_{8}$ </td><td> $\mathbb{R}_{9}$ </td><td rowspan="3"> $\delta_{i}$ </td><td rowspan="3">Rank</td></tr><tr><td>0.200</td><td>0.178</td><td>0.156</td><td>0.133</td><td>0.111</td><td>0.089</td><td>0.067</td><td>0.044</td><td>0.022</td></tr><tr><td>PCM</td><td> $F_{A_1}^{\mathbb{R}_1}$ </td><td> $F_{A_2}^{\mathbb{R}_2}$ </td><td> $F_{A_3}^{\mathbb{R}_3}$ </td><td> $F_{A_4}^{\mathbb{R}_4}$ </td><td> $F_{A_5}^{\mathbb{R}_5}$ </td><td> $F_{A_6}^{\mathbb{R}_6}$ </td><td> $F_{A_7}^{\mathbb{R}_7}$ </td><td> $F_{A_8}^{\mathbb{R}_8}$ </td><td> $F_{A_9}^{\mathbb{R}_9}$ </td></tr><tr><td>A1</td><td>2</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.689</td><td>1</td></tr><tr><td>A2</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0.533</td><td>2</td></tr><tr><td>A3</td><td>0</td><td>0</td><td>2</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0.511</td><td>3</td></tr><tr><td>A4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0.444</td><td>4</td></tr><tr><td>A5</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.400</td><td>5</td></tr><tr><td>A6</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0.511</td><td>3</td></tr><tr><td>A7</td><td>0</td><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td>0.244</td><td>8</td></tr><tr><td>A8</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>0.311</td><td>7</td></tr><tr><td>A9</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0.356</td><td>6</td></tr></table>

Table 26. Performance of materials.

![](images/39eebdb5d7f3856673f8d7c9cae653c7baf2bf1e267addf4d8679027cbfb0a43.jpg)  
Figure 9. Te fair compromise of CDI for the material selection problem.

![](images/52d4c0f6bcd381082cd04845aba46ca73f0948bb64f8b3273f05e2611dce10be.jpg)  
Figure 10. Ranking of alternative materials using diferent MCDM methods.

$$
C D I _ {2} = 0. 3 2
$$

$$
C D I _ {3} = 0. 6 4
$$

The comparative rankings analysis ‑the performance analysis. Similar to SRP, AHP is also highly sensitive to criteria weights. This section uses the Zakeri-Konstantas performance correlation coefficient and the dependency analysis to evaluate the SRP performance. ARAS and COPRAS (see Goswami et al.<sup>6</sup> are also added to the list for the similarity evaluation. Te rankings generated by the mentioned methods are illustrated in Fig. 10. Te Zakeri-Konstantas performance correlation coefcient has been employed to execute the comparative performance analysis of the MCDM methods, and the dependency analysis is used to validate the new MCDM method

![](images/e4e59db3682bb709584f8ac0a86325c07c6baeff1a8a37411de3bf8eb45b9bc8.jpg)  
Figure 11. Performance similarity evaluation of ARPAS, COPRAS, and AHP with SRP using Zakeri Konstantas performance correlation coefcient.

Zakeri‑Konstantas performance correlation coefcient. Zakeri-Konstantas performance correlation coefcient a new tool to evaluate the similarities of the outputs of the MCDM methods. Introduced $\mathsf { b y } ^ { 9 8 }$ , Zakeri-Konstan tas performance correlation coefcient is a new nonparametric measure of rank correlation that measures the similarities between the rankings generated by diferent MCDM methods. In order to provide the similarity degree of the two MCDM methods, the new coefcient computes each decision option’s performance based on its corresponding rank in the data sets generated by the two MCDM methods. Equations (24) and (25) depict the computation of similarity conducted by Zakeri-Konstantas performance correlation coefcient, where ZK stands for the Zakeri-Konstantas performance correlation coefcient, <sup>N</sup> denotes the natural numbers, and $R _ { i } ^ { l }$ and $R _ { i } ^ { h }$ show the rank of ith alternative generated by l th MCDM algorithm and the rank of i th alternative generated by hth MCDM algorithm respectively. Zakeri-Konstantas performance correlation coefcient is architected on two main bases, 1. signifcance of each option using Eqs. (26),and (2). performance of each option in each rank using Eq. (27), and the total performance using Eq. (28). Te performance analysis results are exhibited in Fig. 11, where COPRAS showed the most similar results to SRP, and ARAS has the slightest similarity in the performance according to the results obtained from the Zakeri-Konstantas performance correlation coefcient. Te results also show that AHP and SRP are diferent in generating results.

$$
\mathrm{ZK} _ {(l: h)} = \frac {1 0 0}{m} \sum_ {i = 1} ^ {m} \frac {\min _ {1 \leq i \leq m} \left(\frac {m ^ {2} + m - m R _ {i} ^ {l}}{R _ {i} ^ {l} \sum_ {i = 1} ^ {m} i} ; \frac {m ^ {2} + m - m R _ {i} ^ {h}}{R _ {i} ^ {h} \sum_ {i = 1} ^ {m} i}\right)}{\max _ {1 \leq i \leq m} \left(\frac {m ^ {2} + m - m R _ {i} ^ {l}}{R _ {i} ^ {l} \sum_ {i = 1} ^ {m} i} ; \frac {m ^ {2} + m - m R _ {i} ^ {h}}{R _ {i} ^ {h} \sum_ {i = 0} ^ {m} i}\right)},\tag{25}
$$

where

$$
\mathrm{ZK} _ {(l: h)} = \left\{ \begin{array}{c} 0, \sum_ {i = 1} ^ {m} \langle (R _ {i} ^ {l} - R _ {i} ^ {h}) ^ {2} \rangle^ {0. 5} = \frac {m ^ {2}}{2}, m = 2 \kappa , \kappa \in N, \kappa \neq 0, 1 \\ 0, \sum_ {i = 1} ^ {m} \langle (R _ {i} ^ {l} - R _ {i} ^ {h}) ^ {2} \rangle^ {0. 5} = \frac {m ^ {2} - 1}{2}, m = 2 \kappa + 1, \kappa \in N, \kappa \neq 0 \end{array} \right.,\tag{26}
$$

$$
U _ {i} ^ {F} = \big ((m + 1) - R _ {i} ^ {F} \big) \sum_ {i = 1} ^ {m} i ^ {- 1}, i = \{1, \ldots , m \},\tag{27}
$$

$$
\Gamma_ {i} ^ {F} = R _ {i} ^ {F} \langle \big ((m + 1) - R _ {i} ^ {F} \big) \sum_ {i = 1} ^ {m} i ^ {- 1} \rangle , i = \{1, \ldots , m \},\tag{28}
$$

$$
\mathrm{ZK} _ {(l: h)} ^ {t} = \mathrm{ZK} _ {(l: h)} (m - 1) ^ {- 1}, i = \{1, \dots , m \},\tag{29}
$$

Te dependency analysis. Te comparison process was conducted in the previous section to determine how dependent each method is on the weights of criteria. As a result, a new statistical measure called dependency analysis was proposed instead of using sensitivity analysis. Te dependency analysis measures the dependency of a ranking on the information embedded in a criterion’s corresponding data set. Greater dependency leads to an increased sensitivity of the method to changes in criteria weights, which in turn results in greater reliability. Te dependency analysis is grounded on three central concepts: fair vital importance, real importance, and fair feeble importance. It measures changes in a ranking based on the impact of the mentioned concepts to estimate the dependency of a ranking on each criterion. Te following equations show its process, where $\theta _ { j } ^ { c _ { x } } , \lambda _ { j } ^ { c _ { x } } , \beta _ { j } ^ { c _ { x } }$ , and $w _ { j } ^ { c _ { F } }$ stand for the real importance, the fair vital importance, fair feeble importance of xth criteria, and weights of the rest criteria, respectively. Te constant values of $\lambda _ { j } ^ { c _ { x } } , \beta _ { j } ^ { c _ { x } }$ , and $w _ { j } ^ { c _ { F } }$ have been provided in Tables 27 and 28.

In Eqs. (33) and (34), $R _ { A _ { i } } ^ { \beta _ { j } ^ { c x } } , R _ { A _ { i } } ^ { \lambda _ { j } ^ { c x } }$ , and $R _ { A _ { i } } ^ { \theta _ { j } ^ { c x } }$ denote the rank ith alternative $( A _ { i } ) _ { : }$ , afected by the fair vital importance, fair feeble importance, and the real importance. $\Omega _ { c _ { 1 } }$ also demonstrates the overall dependency of the rank generated by an MCDM method to a criterion.  stands for the dependency of a ranking to the criteria, where $\dot { \Omega } \le 0 . 5$ expresses the reliability of the generator, in our case an MCDM method. In fact, in a comparison process of the generators, MCDM methods, the one that its corresponding  is closer to 1 shows the more reliability and the more dependency to the criteria. In contrast, $\Omega \geq 0 . 5$ portrays the unreliability of the generator, or the MCDM method in the evaluation of the alternatives.

<table><tr><td rowspan="2"></td><td colspan="16">n</td></tr><tr><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td> $\lambda_{j}^{cx}$ </td><td>0.800</td><td>0.833</td><td>0.857</td><td>0.875</td><td>0.889</td><td>0.900</td><td>0.909</td><td>0.917</td><td>0.923</td><td>0.929</td><td>0.933</td><td>0.938</td><td>0.941</td><td>0.944</td><td>0.947</td><td>0.950</td></tr><tr><td> $w_{j}^{CF}$ </td><td>0.050</td><td>0.033</td><td>0.024</td><td>0.018</td><td>0.014</td><td>0.011</td><td>0.009</td><td>0.008</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.003</td></tr><tr><td> $\varsigma$ </td><td colspan="2"></td><td colspan="3">0.01 ≤  $\varsigma$  ≤ 0.05</td><td colspan="6">0.05 ≤  $\varsigma$  ≤ 0.1</td><td colspan="5">0.06 ≤  $\varsigma$  ≤ 0.11</td></tr></table>

Table 27. Constant values of the fair vital importance based on the number of criteria, 20 criteria, $\operatorname* { m a x } _ { 1 \le j \le n } j = 2 0 .$

<table><tr><td rowspan="2"></td><td colspan="16">n</td></tr><tr><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td> $\beta_{j}^{C_x}$ </td><td>0.250</td><td>0.217</td><td>0.193</td><td>0.175</td><td>0.161</td><td>0.150</td><td>0.081</td><td>0.073</td><td>0.067</td><td>0.061</td><td>0.057</td><td>0.053</td><td>0.049</td><td>0.046</td><td>0.043</td><td>0.040</td></tr><tr><td> $w_{j}^{CF}$ </td><td>0.188</td><td>0.157</td><td>0.135</td><td>0.118</td><td>0.105</td><td>0.094</td><td>0.092</td><td>0.084</td><td>0.078</td><td>0.072</td><td>0.067</td><td>0.063</td><td>0.059</td><td>0.056</td><td>0.053</td><td>0.051</td></tr><tr><td>ξ</td><td colspan="6">0 &lt;ξ≤ 0.05</td><td colspan="10">0 &lt;ξ≤ 0.025</td></tr></table>

Table 28. Constant values of the fair feeble importance based on the number of criteria, 20 criteria, $\operatorname* { m a x } _ { 1 \le j \le n } j = 2 0 .$

$$
\theta_ {j} ^ {c _ {x}} = w _ {x}, j = \{1, \ldots , n \}, x \in j, x \leq n,\tag{30}
$$

$$
\lambda_ {j} ^ {c _ {x}} = \left\{ \begin{array}{l} n ^ {- 1} (n - 1) \sum w _ {j}, j = \{1, \ldots , n \}, x \in j, x \leq n, n \leq 6 \\ \langle n ^ {- 1} (n - 1) \sum w _ {j} \rangle - \varsigma , j = \{1, \ldots , n \}, x \in j, x \leq n, 7 \leq n \leq 9, 0. 0 1 \leq \varsigma \leq 0. 0 5 \\ \langle n ^ {- 1} (n - 1) \sum w _ {j} \rangle - \varsigma , j = \{1, \ldots , n \}, x \in j, x \leq n, 1 0 \leq n \leq 1 5, 0. 0 6 \leq \varsigma \leq 0. 0 9 \\ \langle n ^ {- 1} (n - 1) \sum w _ {j} \rangle - \varsigma , j = \{1, \ldots , n \}, x \in j, x \leq n, 1 5 \leq n \leq 2 0, 0. 0 6 \leq \varsigma \leq 0. 1 1 \end{array} \right.,\tag{31}
$$

$$
\beta_ {j} ^ {c _ {x}} = \left\{ \begin{array}{l} \langle n ^ {- 1} \sum w _ {j} \rangle + \xi , j = \{1, \ldots , n \}, x \in j, 0 <   \xi \leq 0. 0 5, x \leq n, 5 \leq n \leq 1 0 \\ \langle n ^ {- 1} \sum w _ {j} \rangle + \xi , j = \{1, \ldots , n \}, x \in j, 0 <   \xi \leq 0. 0 2 5, x \leq n, 1 1 \leq n \leq 2 0 \end{array} \right.,\tag{32}
$$

$$
w _ {j} ^ {c _ {F}} = \left\{ \begin{array}{l} \frac {1 - \lambda_ {j} ^ {c _ {x}}}{n - 1}, j = \{1, \ldots , n \}, x \in j, x \leq n, F = j - \{x \} \\ \frac {1 - \beta_ {j} ^ {c _ {x}}}{n - 1}, j = \{1, \ldots , n \}, x \in j, x \leq n, F = j - \{x \} \end{array} \right.,\tag{33}
$$

$$
\Omega_ {c _ {j}} ^ {A _ {i}} = \frac {R _ {A _ {i}} ^ {\beta_ {j} ^ {c _ {x}}} - R _ {A _ {i}} ^ {\lambda_ {j} ^ {c _ {x}}}}{R _ {A _ {i}} ^ {\theta_ {j} ^ {c _ {x}}}} \times 1 0 0, i = \{1, \ldots , m \}, j = \{1, \ldots , n \}, x \in n, F = j - \{x \},\tag{34}
$$

Proof:

$$
\Omega_ {c _ {j}} ^ {A _ {i}} = \langle \frac {R _ {A _ {i}} ^ {\theta_ {j} ^ {c x}} - R _ {A _ {i}} ^ {\lambda_ {j} ^ {c x}}}{R _ {A _ {i}} ^ {\theta_ {j} ^ {c x}}} \times 1 0 0 \rangle - \langle \frac {R _ {A _ {i}} ^ {\theta_ {j} ^ {c x}} - R _ {A _ {i}} ^ {\beta_ {j} ^ {c x}}}{R _ {A _ {i}} ^ {\theta_ {j} ^ {c x}}} \times 1 0 0 \rangle = \frac {R _ {A _ {i}} ^ {\beta_ {j} ^ {c x}} - R _ {A _ {i}} ^ {\lambda_ {j} ^ {c x}}}{R _ {A _ {i}} ^ {\theta_ {j} ^ {c x}}} \times 1 0 0,\tag{35}
$$

$$
\Omega = n ^ {- 1} \sum n \langle \max _ {1 \leq i \leq m} \sum_ {j = 1} ^ {n} \Omega_ {\epsilon_ {j}} ^ {A _ {i} ^ {2}} \rangle - \sum_ {j = 1} ^ {n} \Omega_ {\epsilon_ {j}} ^ {A _ {i} ^ {2}}, 0 \leq \Omega \leq 1, i = \{1, \ldots , m \},\tag{36}
$$

Figure 12 depict the changes in each material’s rank caused by applying each criterion’s corresponding fair vital importance and fair feeble importance compared to the original ranking associated with the criteria’s rea importance. Compared to the changes in overall ranks afected by fair vital importance in overall rankings, almost no changes were detected in the rankings afected by the feeble fair criteria, which indicates that the SRP becomes more sensitive to weight changes by increasing the number of criteria. Figure 13, developed using Eq. (33), displays the dependency of the ranking generated by SRP on each criterion.

By applying Eq. (35), it has been found that the overall dependency of SRP method is 0.513, which indicates a value of Ω ≤ 0.50, slightly exceeding the limit established for an MCDM method’s reliability. Tis indicates that SRP method is reliable in analyzing problems with six criteria. Since SRP method employs the ranks of each alternative in each criterion, and the criteria weight plays a critical role in determining the generated rankings,

a

![](images/38348418eb1a2c52532fe8b9e6aa5744a990910c828f39419ec4989579955c56.jpg)

![](images/c328e56e7047f5891624e69c8c3d5f07372fb87754f248292a16a8be94471e19.jpg)

![](images/1a2dd33803de88199ffa9f9d647a545ea4e79d5980cfd7ac17c799079ffbd09a.jpg)

![](images/e01cd132d7bc871608f244230d6b158e56d8d44bae0a6b669d2c9432a26a3889.jpg)  
Figure 12. (a) Changes in ranking, afected by the vital and feeble fair importance values, associated with weight of $\cdot _ { c _ { 1 } . }$ (b) Changes in ranking, afected by the vital and feeble fair importance values, associated with weight of $c _ { 2 }$ criterion. (c) Changes in ranking, afected by the vital and feeble fair importance values, associated with weight $\mathrm { o f } c _ { 3 }$ criterion. (d) Changes in ranking, afected by the vital and feeble fair importance values, associated with weight of c4 criterion. (e) Changes in ranking, afected by the vital and feeble fair importance values, associated with weight o $: c _ { 5 }$ criterion. (f)Changes in ranking, afected by the vital and feeble fair importance values, associated with weight of $\dot { c } _ { 6 }$ criterion.

![](images/b85078178ca19bf33b4e568e972794b35f6ea4953d1cf39a68e227c0470775ed.jpg)

![](images/75d8442678acfd8ffbebc072fa50eabec47fd5bc93d44d897f5bb0f791d776fe.jpg)  
Figure 12. (continued)

![](images/a556148317a7c072b3e96ca6db61edf2fa7f979f11eec6ba3939c42cce9d57db.jpg)  
Figure 13. Dependency of each material on each criterion.

reliability of the method improves with increasing criteria, making it an efective tool for solving complex MCDM problems.

The comparative rankings analysis—Similarity measures. In this section, the obtained ranks from diferent MCDM methods have been evaluated through six similarity measures, including Manhattan distance and total similarity Eqs. (36) and (37), Canberra distance and total similarity Eqs. (38) and (39), Chi-square distance and total similarity Eqs. (40) and (41), and Squared Euclidean distance and total similarity Eqs. (42) and (43), in order to conclude the similarities between SRP and other MCDM methods Eq. (44). In the equations, $R _ { x } , R _ { y } , \mathbb { R } _ { i } ^ { x } .$ , and $\mathbb { R } _ { i } ^ { y }$ represent the output of xth MCDM method, yth MCDM method, ith alternative’s rank in xth MCDM method, and the same alternative’s rank in yth MCDM method, respectively. $\mathrm { T } d _ { ( R _ { x } , R _ { V } ) }$ denote the total similarity between xth MCDM method and yth MCDM method, in which ℵ signifes the total number of MCDM methods that have been used for similarity evaluation.

$$
d _ {1} \left(R _ {x}, R _ {y}\right) = \sum_ {i = 1} ^ {m} \left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right|, i = \{1,.., m \}, R _ {x} = \left\{\mathbb {R} _ {1} ^ {x},..., \mathbb {R} _ {m} ^ {x} \right\}, R _ {y} = \left\{\mathbb {R} _ {1} ^ {y},..., \mathbb {R} _ {m} ^ {y} \right\},\tag{37}
$$

$$
d _ {1} ^ {\prime} (R _ {x}, R _ {V}) = \langle \sum_ {i = 1} ^ {m} \left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right| \langle \sum_ {V = 1} ^ {g} \sum_ {i = 1} ^ {m} \left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right| \rangle^ {- 1} \rangle \times 1 0 0, y \in V, V = \bigl \{1, \ldots , g \bigr \},\tag{38}
$$

$$
d _ {2} \big (R _ {x}, R _ {y} \big) = \sum_ {i = 1} ^ {m} \frac {\left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right|}{\left| \mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y} \right|},\tag{39}
$$

$$
d _ {2} ^ {\prime} (R _ {x}, R _ {V}) = \langle \sum_ {i = 1} ^ {m} \frac {\left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right|}{\left| \mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y} \right|} \rangle \langle \sum_ {V = 1} ^ {g} \sum_ {i = 1} ^ {m} \frac {\left| \mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y} \right|}{\left| \mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y} \right|} \rangle^ {- 1} \rangle \times 1 0 0,\tag{40}
$$

$$
d _ {3} (R _ {x}, R _ {y}) = \sum_ {i = 1} ^ {m} \frac {(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}) ^ {2}}{\mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y}},\tag{41}
$$

$$
d _ {3} ^ {\prime} (R _ {x}, R _ {V}) = \langle \sum_ {i = 1} ^ {m} \frac {\left(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}\right) ^ {2}}{\mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y}} \langle \sum_ {V = 1} ^ {g} \sum_ {i = 1} ^ {m} \frac {\left(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}\right) ^ {2}}{\mathbb {R} _ {i} ^ {x} + \mathbb {R} _ {i} ^ {y}} \rangle^ {- 1} \rangle \times 1 0 0,\tag{42}
$$

$$
d _ {4} \big (R _ {x}, R _ {y} \big) = \sum_ {i = 1} ^ {m} \left(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}\right) ^ {2},\tag{43}
$$

$$
d _ {4} ^ {'} (R _ {x}, R _ {V}) = \langle \sum_ {i = 1} ^ {m} \left(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}\right) ^ {2} \langle \sum_ {V = 1} ^ {g} \sum_ {i = 1} ^ {m} \left(\mathbb {R} _ {i} ^ {x} - \mathbb {R} _ {i} ^ {y}\right) ^ {2} \rangle^ {- 1} \rangle \times 1 0 0,\tag{44}
$$

$$
\mathrm{T} d _ {(R _ {x}, R _ {V})} = \langle \frac {d _ {1} ^ {\prime} (R _ {x} , R _ {V})}{\sum d _ {1} ^ {\prime} (R _ {x} , R _ {V})} + \frac {d _ {2} ^ {\prime} (R _ {x} , R _ {V})}{\sum d _ {2} ^ {\prime} (R _ {x} , R _ {V})} + \frac {d _ {3} ^ {\prime} (R _ {x} , R _ {V})}{\sum d _ {3} ^ {\prime} (R _ {x} , R _ {V})} + \frac {d _ {4} ^ {\prime} (R _ {x} , R _ {V})}{\sum d _ {4} ^ {\prime} (R _ {x} , R _ {V})} \rangle \aleph^ {- 1},\tag{45}
$$

Manhattan distance. Using Manhattan distance to evaluate the similarities between SRP and VIKOR, WPM, TOPSIS, ARAS, COPRAS, and AHP showed that VIKOR has the most resemblance in evaluating materials with SRP. Te results of using Manhattan distance are illustrated in Fig. 14.

Canberra distance. Similar to the Manhattan distance, the Canberra distance puts VIKOR most resembling SRP. Applying the Canberra distance puts AHP higher than TOPSIS as the second most resemblance method to the SRP in solving the material selection problem. In contrast, the Manhattan distance considers TOPSIS the second most resemblance method to the SRP with a slightly higher score (see Table 29). The results of the Can. berra distance application are pictured in Fig. 15.

![](images/dcd5f627afb4bc679e5ed04c22368684287886804d232d4f2313ebd9d17e1f75.jpg)  
Figure 14. Comparative analysis of the similarity between SRP and other MCDM methods using Manhattan distance.

<table><tr><td>Distance</td><td>AHP</td><td>COPRAS</td><td>ARAS</td><td>TOPSIS</td><td>WPM</td><td>VIKOR</td></tr><tr><td>Manhattan distance</td><td>27.4509</td><td>13.7255</td><td>15.6860</td><td>27.4510</td><td>13.725</td><td>29.4117</td></tr><tr><td>Canberra distance</td><td>17.6120</td><td>15.5224</td><td>15.8209</td><td>17.6119</td><td>15.5223</td><td>17.9104</td></tr><tr><td>Chi-square distance</td><td>21.8610</td><td>11.2600</td><td>11.2470</td><td>21.2340</td><td>9.0500</td><td>25.3480</td></tr><tr><td>Hamming distance</td><td>22.3048</td><td>10.0371</td><td>10.7806</td><td>23.7918</td><td>7.8066</td><td>25.2788</td></tr></table>

Table 29. Results of each similarity measure method.

![](images/78bb5061c44ffb9778187b94a535c7a6cdbd435ee1c0275823e6e2b651c79d83.jpg)

Figure 15. Comparative analysis of the similarity between SRP and other MCDM methods using Canberra distance.  
![](images/3544dfb5628513e79f911a305173d558ca880a7bb49cac4e5a4c61eacb8c5811.jpg)  
Figure 16. Comparative analysis of the similarity between SRP and other MCDM methods using Chi-square distance.

Chi‑square distance. Te Chi-square distance analysis reveals that AHP is the second most similar MCDM method to SRP, while WPM is the least similar. In comparison to Manhattan and Canberra distances, where COPRAS and WPM have almost equal scores, Chi-square distance gives WPM the lowest similarity score and the farthest distance from the COPRAS method. Te results of this comparison are shown in Fig. 16.

Squared Euclidean distance. Except for VIKOR which has been placed by Squared Euclidean distance as the most similar method to SRP dominantly, TOPSIS is the second MCDM method that shows similarity to SRP in ranking the materials. Te results of Squared Euclidean distance application are portrayed in Fig. 17.

Total similarity. "Total similarity" as computed using Eq. (44), has generated almost identical rankings of similarity, where VIKOR, TOPSIS, and AHP, with a considerable distance, are the most similar methods to the SRP method, respectively. On the other hand, ARAS, COPRAS, and WPM showed the most dissimilarity compared to SRP. Te results are demonstrated in Table 29 and Fig. 18.

The rank reversal phenomenon: A comparison between SRP and other rank reversal free MCDM methods. Te rank reversal phenomenon refers to the occurrence of changes in the relative rankings of alternatives when additional alternatives are introduced or existing alternatives are removed from a set being evaluated in MCDM environment<sup>99</sup>. Tis phenomenon can lead to inconsistent decisions and can make it challenging to compare and evaluate alternatives across diferent decision problems. Several MCDM methods have been proven to be rank reversal-free, including Characteristic Objects Method (COMET) proposed by Piegat & Sałabun<sup>100</sup> and Sałabun<sup>101</sup>, Stable Preference Ordering Towards Ideal Solution (SPOTIS) developed by Dezert<sup>102</sup>, Ranking of Alternatives through Functional mapping of criterion sub-intervals into a Single Interval (RAFSI) proposed by Žižović et  al.<sup>103</sup>, and the Sequential Interactive Model of Urban Systems (SIMUS) developed by Munier<sup>104</sup>. Among these methods, COMET method is the frst MCDM method that is completely immune to the rank reversal paradox. COMET method considers the correlations between the criteria, and provides ranking by considering the characteristic objects and fuzzy rules<sup>101</sup>. COMET method has proven to be robust and efective in avoiding the rank reversal paradox in various applications, such as those described in Wątróbski et al.<sup>105,</sup> Shekhovtsov et al.<sup>106,</sup> Faizi et al.<sup>107,</sup> and Palczewski & Sałabun<sup>108</sup>. To test the rank reversal paradox of SRP, three examples are provided including a material selection case and two other numerical examples.

![](images/1a4b5999fd5c6fd87757027318b7fe2420a36fdc5cac2b43309c68a2d4ccc6d7.jpg)

Figure 17. Comparative analysis of the similarity between SRP and other MCDM methods using Squared Euclidean distance.  
![](images/f46d6fb57c74d1fb23accf1d5744c44d169f21afd2da6b361baf533c0edb1bef.jpg)  
Figure 18. Total similarity of each MCDM method to SRP.

The material selection case A new alternative is added to the original material selection decision matrix (Table  5), in which A<sup>∗</sup> stands for the new alternative and its performance is equal to A . Te new decision matrix and the corresponding ranks given by SRP are shown in Table 30. In order to demonstrate the correlation between the original ranking and the obtained ranking, Fig. 19 is presented, where a correlation of 1 is indicated, suggesting that SRP is a rank reversal free MCDM method.

The frst numerical example. A numerical example is presented in Table 31, comprising of eleven alternatives and ffeen criteria. All the criteria are benefcial, having equal weights. Te ranking of alternatives is shown in Table 32, where A6 is assigned the frst rank. In the case of adding a new alternative with the same performance as A6, no changes have been observed in the ranks, and the correlation between the two rankings is one, as shown in Table 33 and Fig. 20.

Second numerical example. An additional example is presented to represent a more complex MCDM problem with a larger number of alternatives and fewer criteria. Tis example includes twenty alternatives and four criteria, each with equal weights, as shown in Table 33. To illustrate the robustness of SRP, a new alternative with the same performance as the original top-ranked alternative (A15) is added, resulting in no changes in the ranking and a correlation coefcient of one, as shown in Fig. 21. Tis provides further evidence that SRP is a rank reversal-free MCDM method

<table><tr><td>PCM</td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td> $c_4$ </td><td> $c_5$ </td><td> $c_6$ </td><td> $SR_i$ </td><td> $\Re_i$ </td><td>Original rank</td><td>New rank</td></tr><tr><td>A1</td><td>169.98</td><td>1560</td><td>1.46</td><td>2.13</td><td>1.09</td><td>0.255</td><td>4.269</td><td>4.731</td><td>2</td><td>2</td></tr><tr><td>A2</td><td>186.5</td><td>903</td><td>2.83</td><td>2.38</td><td>0.18</td><td>0.745</td><td>5.012</td><td>3.988</td><td>7</td><td>7</td></tr><tr><td>A3</td><td>190</td><td>830</td><td>2.1</td><td>2.1</td><td>0.21</td><td>0.335</td><td>4.68</td><td>4.32</td><td>5</td><td>5</td></tr><tr><td>A4</td><td>214.4</td><td>850</td><td>0.9</td><td>0.9</td><td>0.2</td><td>0.255</td><td>4.084</td><td>4.916</td><td>1</td><td>1</td></tr><tr><td>A5</td><td>206</td><td>789</td><td>1.8</td><td>2.4</td><td>0.18</td><td>0.335</td><td>4.674</td><td>4.326</td><td>4</td><td>4</td></tr><tr><td>A6</td><td>194.6</td><td>785</td><td>1.93</td><td>2.38</td><td>0.22</td><td>0.335</td><td>4.321</td><td>4.679</td><td>3</td><td>3</td></tr><tr><td>A7</td><td>245</td><td>773.22</td><td>0.3767</td><td>2.267</td><td>0.14</td><td>0.335</td><td>5.545</td><td>3.455</td><td>9</td><td>9</td></tr><tr><td>A8</td><td>222</td><td>775.8</td><td>1.7189</td><td>1.921</td><td>0.142</td><td>0.665</td><td>5.339</td><td>3.661</td><td>8</td><td>8</td></tr><tr><td>A9</td><td>247</td><td>776.33</td><td>0.7467</td><td>2.377</td><td>0.138</td><td>0.336</td><td>4.981</td><td>4.019</td><td>6</td><td>6</td></tr><tr><td>A4*</td><td>214.4</td><td>850</td><td>0.9</td><td>0.9</td><td>0.2</td><td>0.255</td><td colspan="4"></td></tr></table>

Table 30. New ranking given by SRP afer adding the new alternative.

![](images/d83685a6a7840b1ec2ffe8e98ae7bf34792f43a4bac11bdd53153be1b6233307.jpg)  
Figure 19. Te correlation between two ranks to assess the rank reversal incident.

<table><tr><td>Weight</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td><td>0.067</td></tr><tr><td>Alternative</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>C8</td><td>C9</td><td>C10</td><td>C11</td><td>C12</td><td>C13</td><td>C14</td><td>C15</td></tr><tr><td>A1</td><td>0.087</td><td>0.046</td><td>3.252</td><td>0.737</td><td>0.092</td><td>1.318</td><td>2.912</td><td>0.074</td><td>0.054</td><td>0.067</td><td>1.505</td><td>1.599</td><td>1.219</td><td>0.056</td><td>0.031</td></tr><tr><td>A2</td><td>0.002</td><td>0.094</td><td>0.732</td><td>3.564</td><td>2.545</td><td>2.059</td><td>1.860</td><td>0.056</td><td>0.070</td><td>0.085</td><td>1.265</td><td>0.116</td><td>0.783</td><td>0.080</td><td>0.005</td></tr><tr><td>A3</td><td>0.047</td><td>0.052</td><td>2.485</td><td>1.599</td><td>3.900</td><td>0.267</td><td>1.477</td><td>0.089</td><td>0.067</td><td>0.096</td><td>0.898</td><td>1.037</td><td>0.821</td><td>0.028</td><td>0.088</td></tr><tr><td>A4</td><td>0.093</td><td>0.011</td><td>1.336</td><td>1.788</td><td>1.804</td><td>3.879</td><td>2.650</td><td>0.001</td><td>0.041</td><td>0.050</td><td>0.023</td><td>0.976</td><td>1.057</td><td>0.002</td><td>0.010</td></tr><tr><td>A5</td><td>0.058</td><td>0.084</td><td>2.777</td><td>3.025</td><td>0.814</td><td>1.256</td><td>1.136</td><td>0.034</td><td>0.054</td><td>0.078</td><td>0.606</td><td>1.650</td><td>0.805</td><td>0.013</td><td>0.032</td></tr><tr><td>A6</td><td>0.017</td><td>0.032</td><td>3.353</td><td>2.240</td><td>3.840</td><td>2.005</td><td>2.250</td><td>0.030</td><td>0.099</td><td>0.080</td><td>0.578</td><td>1.660</td><td>0.669</td><td>0.030</td><td>0.083</td></tr><tr><td>A7</td><td>0.075</td><td>0.050</td><td>0.467</td><td>0.681</td><td>0.960</td><td>1.986</td><td>1.998</td><td>0.002</td><td>0.096</td><td>0.084</td><td>0.660</td><td>0.800</td><td>1.673</td><td>0.089</td><td>0.002</td></tr><tr><td>A8</td><td>0.011</td><td>0.051</td><td>2.966</td><td>0.639</td><td>0.959</td><td>3.116</td><td>0.424</td><td>0.097</td><td>0.089</td><td>0.089</td><td>0.438</td><td>0.944</td><td>0.544</td><td>0.041</td><td>0.080</td></tr><tr><td>A9</td><td>0.080</td><td>0.096</td><td>3.819</td><td>3.948</td><td>2.994</td><td>3.610</td><td>1.725</td><td>0.001</td><td>0.017</td><td>0.030</td><td>0.221</td><td>1.516</td><td>0.755</td><td>0.064</td><td>0.017</td></tr><tr><td>A10</td><td>0.002</td><td>0.035</td><td>2.546</td><td>0.787</td><td>3.038</td><td>0.552</td><td>1.946</td><td>0.002</td><td>0.007</td><td>0.050</td><td>0.068</td><td>0.397</td><td>0.127</td><td>0.029</td><td>0.002</td></tr><tr><td>A11</td><td>0.048</td><td>0.011</td><td>1.675</td><td>3.243</td><td>0.306</td><td>1.696</td><td>1.732</td><td>0.081</td><td>0.068</td><td>0.059</td><td>0.334</td><td>0.342</td><td>0.348</td><td>0.038</td><td>0.031</td></tr></table>

Table 31. Decision matrix of the frst numerical example.

Te above examples revealed that the SRP method is utterly immune to the rank reversal paradox. As mentioned earlier, SPOTIS, COMET, and SIMUS are also rank reversal-free MCDM methods. Te complexity of any MCDM method can lead to less transparency and uncertainty in its outcomes, especially in complex systems with many interacting parts and variables. Increased complexity of an MCDM method also hinders the ability to track and identify errors in the algorithmic output. Complex systems, such as those with numerous pairwise comparisons or diferent normalization approaches, are more likely to produce uncertain outcomes due to the complex interplay between variables. One of the major benefts of SRP in this context is its simplicity which helps to avoid those issues and provides reliable results when the problem becomes more complex.

<table><tr><td>Alternative</td><td> $SR_i$ </td><td> $\Re_i$ </td><td> $SR_{i2}$ </td><td> $\Re_{i2}$ </td><td>Original rank</td><td>New rank</td></tr><tr><td>A1</td><td>5.0000</td><td>6.0000</td><td>5.5333</td><td>6.4667</td><td>2</td><td>2</td></tr><tr><td>A2</td><td>5.4000</td><td>5.6000</td><td>5.8667</td><td>6.1333</td><td>4</td><td>4</td></tr><tr><td>A3</td><td>5.1333</td><td>5.8666</td><td>5.6000</td><td>6.4000</td><td>3</td><td>3</td></tr><tr><td>A4</td><td>6.9333</td><td>4.0666</td><td>7.6667</td><td>4.3333</td><td>9</td><td>9</td></tr><tr><td>A5</td><td>6.0666</td><td>4.9333</td><td>6.6667</td><td>5.3333</td><td>8</td><td>8</td></tr><tr><td>A6</td><td>4.7333</td><td>6.2666</td><td>4.7333</td><td>7.2667</td><td>1</td><td>1</td></tr><tr><td>A7</td><td>5.7333</td><td>5.2666</td><td>6.3333</td><td>5.6667</td><td>6</td><td>6</td></tr><tr><td>A8</td><td>5.8666</td><td>5.1333</td><td>6.5333</td><td>5.4667</td><td>7</td><td>7</td></tr><tr><td>A9</td><td>5.4666</td><td>5.5333</td><td>6.0000</td><td>6.0000</td><td>5</td><td>5</td></tr><tr><td>A10</td><td>8.600</td><td>2.40000</td><td>9.5333</td><td>2.4667</td><td>11</td><td>11</td></tr><tr><td>A11</td><td>7.0666</td><td>3.9333</td><td>7.8000</td><td>4.2000</td><td>10</td><td>10</td></tr></table>

Table 32. Te diferent alternatives’ rankings to test the rank reversal paradox.

<table><tr><td>Weight</td><td>0.25</td><td>0.25</td><td>0.25</td><td>0.25</td><td colspan="6"></td></tr><tr><td>Alternative</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td> $SR_i$ </td><td> $\mathfrak{R}_i$ </td><td> $SR_{i2}$ </td><td> $\mathfrak{R}_{i2}$ </td><td>Original rank</td><td>New rank</td></tr><tr><td>A1</td><td>912.4845</td><td>0.3018</td><td>206.4309</td><td>0.1221</td><td>12.75</td><td>7.25</td><td>13.5</td><td>7.5</td><td>14</td><td>14</td></tr><tr><td>A2</td><td>517.0006</td><td>0.1986</td><td>616.1050</td><td>0.0945</td><td>13.5</td><td>6.5</td><td>14.5</td><td>6.5</td><td>16</td><td>16</td></tr><tr><td>A3</td><td>19.61708</td><td>0.6361</td><td>348.3409</td><td>0.1985</td><td>14.5</td><td>5.5</td><td>15.5</td><td>5.5</td><td>17</td><td>17</td></tr><tr><td>A4</td><td>1069.093</td><td>0.9259</td><td>918.6073</td><td>0.0005</td><td>8.25</td><td>11.75</td><td>9</td><td>12</td><td>5</td><td>5</td></tr><tr><td>A5</td><td>151.0204</td><td>0.0969</td><td>376.8284</td><td>0.2074</td><td>15.25</td><td>4.75</td><td>16.25</td><td>4.75</td><td>19</td><td>19</td></tr><tr><td>A6</td><td>1022.647</td><td>0.2007</td><td>430.3449</td><td>0.3781</td><td>9</td><td>11</td><td>9.75</td><td>11.25</td><td>6</td><td>6</td></tr><tr><td>A7</td><td>944.3263</td><td>1.2419</td><td>443.6463</td><td>0.2520</td><td>6.75</td><td>13.25</td><td>7.5</td><td>13.5</td><td>4</td><td>4</td></tr><tr><td>A8</td><td>974.168</td><td>0.2407</td><td>978.1523</td><td>0.0137</td><td>10.25</td><td>9.75</td><td>10.75</td><td>10.25</td><td>9</td><td>9</td></tr><tr><td>A9</td><td>504.9541</td><td>1.2165</td><td>176.6877</td><td>0.3398</td><td>10</td><td>10</td><td>11</td><td>10</td><td>8</td><td>8</td></tr><tr><td>A10</td><td>549.4893</td><td>0.2430</td><td>645.7940</td><td>0.2352</td><td>10.5</td><td>9.5</td><td>11.5</td><td>9.5</td><td>10</td><td>10</td></tr><tr><td>A11</td><td>319.5062</td><td>1.1863</td><td>57.60621</td><td>0.3537</td><td>11</td><td>9</td><td>12</td><td>9</td><td>12</td><td>12</td></tr><tr><td>A12</td><td>86.49311</td><td>0.6288</td><td>258.042</td><td>0.0811</td><td>15.5</td><td>4.5</td><td>16.5</td><td>4.5</td><td>20</td><td>20</td></tr><tr><td>A13</td><td>991.6532</td><td>0.6623</td><td>962.0012</td><td>0.3963</td><td>4</td><td>16</td><td>4.25</td><td>16.75</td><td>2</td><td>2</td></tr><tr><td>A14</td><td>279.4132</td><td>1.0169</td><td>688.305</td><td>0.0302</td><td>11.5</td><td>8.5</td><td>12.5</td><td>8.5</td><td>13</td><td>13</td></tr><tr><td>A15</td><td>787.9316</td><td>2.1867</td><td>926.4695</td><td>0.3922</td><td>3.75</td><td>16.25</td><td>3.75</td><td>17.25</td><td>1</td><td>1</td></tr><tr><td>A16</td><td>866.5065</td><td>1.0388</td><td>1044.6860</td><td>0.2068</td><td>6</td><td>14</td><td>6.5</td><td>14.5</td><td>3</td><td>3</td></tr><tr><td>A17</td><td>580.661</td><td>0.3445</td><td>430.0089</td><td>0.0343</td><td>13.25</td><td>6.75</td><td>14.25</td><td>6.75</td><td>15</td><td>15</td></tr><tr><td>A18</td><td>407.2574</td><td>0.5822</td><td>659.9484</td><td>0.3830</td><td>9</td><td>11</td><td>10</td><td>11</td><td>6</td><td>6</td></tr><tr><td>A19</td><td>460.7242</td><td>0.0873</td><td>491.7818</td><td>0.1171</td><td>14.5</td><td>5.5</td><td>15.5</td><td>5.5</td><td>17</td><td>17</td></tr><tr><td>A20</td><td>45.74425</td><td>0.7103</td><td>643.1528</td><td>0.2860</td><td>10.75</td><td>9.25</td><td>11.75</td><td>9.25</td><td>11</td><td>11</td></tr></table>

Table 33. Two obtained rankings from SRP application for the second numerical example.

## Conclusions and future research

Material selection problems are complex MCDM problems that comprise many options and criteria. To solve material selection problems, a new simple MCDM method called SRP is proposed in this paper. Te new method functions based on the diferent ranks of the material in each criterion to generate reliable outputs in solving MCDM problems. One of the sources of anomalies in comparison processes of the generated results of MCDM methods is the diferent normalization strategies employed by diferent MCDM methods. To enhance the reli ability of results in complex MCDM problems, SRP method avoids the normalization process of the decision matrix and operates solely with the ranks of alternatives, enabling a comparison of scores with the same unit. In a material selection problem that involved selecting a suitable phase change material to store solar energy, SRP method was employed. However, since SRP relies heavily on the criteria weights in generating rankings, it is essential to have a dependable method for determining these weights. In this study, VIMM method was utilized to extract the criteria weights through a decision-making process involving seven experts. By utilizing the newly proposed method to validate MCDM methods based on the analysis of their dependency on criteria weights, it was found that the SRP method is sensitive to changes in the criteria weights. Even slight changes in the weights can signifcantly afect the ranks of materials obtained by the SRP method. We also compared the results obtained from the application of other MCDM methods and found signifcant diferences between the generated results. In this paper, CDI has been introduced as a new statistical measure to validate the results. CDI is used to interpret the results of MCDM methods in four categories, namely pragmatic compromise, rational compromise, fair compromise, and rotten compromise. Te most reliable results were placed under the pragmatic compromise category. On the other hand, undependable results were interpreted according to the fair compromise and the rotten compromise situations, and their comparison needed to be executed in the real world to determine which method was better, while the mathematical proof was enough in the frst category. Te comparison results were put under the fair compromise category by the results of CDI. Te new measure will decrease the cost of wrong material selection. Te obtained ranking from SRP is also compared with other MCDM methods using Zakeri-Konstantas Performance Correlation Coefcient, which showed that the new method is more similar to the COPRAS than AHP and ARAS. Four diferent similarity measures are also applied to evaluate the similarity between other MCDM methods to SRP which has some salient advantages to make it an ideal MCDM method for solving complex problems. Overall, with the employed comparison processes, it is concluded that:

![](images/bd1c0b4e139a13ec387809f4032d945d9d806b6dc4f060792850ae8d96fe825e.jpg)  
Figure 20. Correlation between two obtained rankings for the frst numerical example.

![](images/55b72a5a198d5606545c9203af883a070a02c43857c084d40f4f6cfe888f8dcd.jpg)  
Figure 21. Te correlation between two obtained rankings from the second numerical example.

## 1. SRP produces more reliable products since it does not execute the normalization process.

2. SRP is a reliable MCDM method since the analytical processes showed that it is sensitive to changes in the criteria weights.

3. SRP is designed to generate ranking in a less complex analysis which correlates to less uncertainty in the fnal results.

4. Te algorithm of SRP is easy to reverse track by decision-makers to identify possible errors.

5. Te reliability of SRP increases by increasing the number of criteria, making it ideal for solving complex decision-making problems involving a large number of criteria and alternatives

6. According to the results obtained from evaluation of the similarities between other MCDM methods and SRP, it is observed that SRP behaves similar to distance-based methods, e.g. VIKOR and TOPSIS, and also shows a resemblance to AHP in some results.

Te results also revealed a limitation of SRP. Te obtained results are not potentially reliable for those MCDM problems where the number of criteria is less than six, which makes it an ideal method for solving complex MCDM problems involving higher number of criteria. Future research would be interesting in assessing the applicability and validation of the new method. Application and validation of the results of SRP for solving other material selection problems is the second suggestion for future research. Validation of the interpretation of CDI by simulation is a very interesting future study work. Other intriguing ideas for future research include compar ing the interpretation with other statistical techniques and CDI to validate the outcomes. Integrating criteria weights from diferent weighting methods, including both subjective and objective methods, with dependency analysis to evaluate and validate the result is another exciting suggestion for future research. Tis paper used VIMM: the frst scenario as a weighting method because of its reliability. It is also suggested to use AHP and BWM in conjunction with SRP to comparing the results as future research scope. Development of extensions of SRP for resolving diferent types of MCDM problems with multiple-layer criteria is the concluding suggestion for further research.

## Data availability

Te datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 2 December 2022; Accepted: 17 May 2023

Published online: 27 May 2023

## References

1. Bhaskar, A. S. & Khan, A. Comparative analysis of hybrid MCDM methods in material selection for dental applications. Exper Syst. Appl. https://doi.org/10.1016/j.eswa.2022.118268 (2022).

2. Farid, H. M. A. & Riaz, M. Single-valued neutrosophic Einstein interactive aggregation operators with applications for materia selection in engineering design: Case study of cryogenic storage tank. Complex Intell. Syst. https://doi.org/10.1007/s40747-021- 00626-0 (2022).

3. Takker, A., Jarvis, J., Buggy, M. & Sahed, A. A novel approach to materials selection strategy case study: Wave energy extraction impulse turbine blade. Mater. Des. 29(10), 1973–1980. https://doi.org/10.1016/j.matdes,2008.04.022 (2008).

4. Aksakal, B., Ulutaş, A., Balo, F. & Karabasevic, D. A new hybrid MCDM model for insulation material evaluation for healthier environment. Buildings 12(5), 655. https://doi.org/10.3390/buildings12050655 (2022)

5. Bhadra, D. & Dhar, N. R. Selection of the natural fber for sustainable applications in aerospace cabin interior using fuzzy MCDM model. Materialia 21, 101270. https://doi.org/10.1016/j.mtla.2021.101270 (2022).

6. Goswami, S. S. & Behera, D. K. Solving material handling equipment selection problems in an industry with the help of entropy integrated COPRAS and ARAS MCDM techniques. Process Integr. Optim. Sustain. 5(4), 947–973. https://doi.org/10.1007 s41660-021-00192-5 (2021).

7. Agrawal, R. Sustainable material selection for additive manufacturing technologies: A critical analysis of rank reversal approach. J. Clean. Prod. 296, 126500. https://doi.org/10.1016/j.jclepro.2021.126500 (2021).

8. Chatterjee, S. & Chakraborty, S. Material selection of a mechanical component based on criteria relationship evaluation and MCDM approach. Mater. Today 44, 1621–1626. https://doi.org/10.1016/j.matpr.2020.11.817 (2021).

9. Zakeri, S., Ecer, F., Konstantas, D. & Cheikhrouhou, N. Te vital-immaterial-mediocre multi-criteria decision-making method. Kvbernetes https://doi.org/10.1108/K-05-2021-0403 (2021)

10. Patnaik, P. K., Swain, P. T. R., Mishra, S. K., Purohit, A. & Biswas, S. Composite material selection for structural applications based on AHP-MOORA approach. Mater. Today 33, 5659–5663. https://doi.org/10.1016/j.matpr.2020.04.063 (2020).

11. Rahim, A. A., Musa, S. N., Ramesh, S. & Lim, M. K. Development of a fuzzy-TOPSIS multi-criteria decision-making model for material selection with the integration of safety, health and environment risk assessment. Proc. Inst. Mech. Eng. L https://doi org/10.1177/2F1464420721994269 (2021)

12. Figueiredo, K., Pierott, R., Hammad, A. W. & Haddad, A. Sustainable material choice for construction projects: A life cycle sustainability assessment framework based on BIM and Fuzzy-AHP. Build. Environ. https://doi.org/10.1016/j.buildenv.2021. 107805 (2021).

13. Zoghi, M., Rostami, G., Khoshand, A. & Motalleb, F. Material selection in design for deconstruction using Kano model, fuzzy AHP and TOPSIS methodology. Waste Manag. Res. https://doi.org/10.1177/2F0734242X211013904 (2021).

14. MacCrimmon, K. R. Decisionmaking among multiple-attribute alternatives: a survey and consolidated approach (No. RM 4823-ARPA). RAND CORP SANTA MONICA CA (1968)

15. Peng, C., Feng, D. & Guo, S. Material selection in green design: A method combining DEA and TOPSIS. Sustainability 13(10) 5497, https://doi.org/10.3390/su13105497 (2021)

16. Kiani, B., Liang, R. Y. & Gross, J. Material selection for repair of structural concrete using VIKOR method. Case Stud. Constr. Mater, 8, 489–497. https://doi,org/10.1016/i.cscm,2018.03.008 (2018).

17. Fontela, E. & Gabus, A. Te Dematel Observer (Battelle Geneva Research Center, 1976).

19. Jahan, A. & Zavadskas, E. K. ELECTRE-IDAT for design decision-making problems with interval data and target-based criteria. Soft Comput, 23(1), 129–143. https://doi.org/10.1007/s00500-018-3501-6 (2019).

20. Zakeri, S. Ranking based on optimal points multi-criteria decision-making method. Grey Syst. https://doi.org/10.1108/GS-09- 2018-0040 (2019)

21. Keršulienė, V. & Turskis, Z. Integrated fuzzy multiple criteria decision making model for architect selection. Technol. Econ. Dev. Econ. 17(4), 645–666. https://doi.org/10.3846/20294913.2011.635718 (2011).

22. Toloie-Eshlaghy, A., Homayonfar, M., Aghaziarati, M. & Arbabiun, P. A subjective weighting method based on group decision making for ranking and measuring criteria values. Aust. J. Basic Appl. Sci. 5(12), 2034–2040 (2011).

23. Xu, X. Te SIR method: A superiority and inferiority ranking method for multiple criteria decision making. Eur. J. Oper. Res. 131(3), 587-602, https://doi,org/10.1016/S0377-2217(00)00101-6 (2001).

24. Jessop, A. IMP: A decision aid for multiattribute evaluation using imprecise weight estimates. Omega 49, 18–29. https://doi.org/ 10.1016/j.omega.2014.05.001 (2014).

25. Rezaei, J. Best-worst multi-criteria decision-making method. Omega 53, 49–57. https://doi.org/10.1016/j.omega.2014.11.009 (2015).

26. Voogd, H. Multicriteria evaluation with mixed qualitative and quantitative data. Environ. Plann. B. Plann. Des. 9(2), 221–236 https://doi.org/10.1068/b090221 (1982).

27. Voogd, J. H. Multicriteria evaluation for urban and regional planning (1982). https://doi.org/10.6100/IR102252

28. Opricovic, S. & Tzeng, G. H. Extended VIKOR method in comparison with outranking methods. Eur. J. Oper. Res. 178(2), 514–529. https://doi.org/10.1016/j.ejor.2006.01.020 (2007).

29. Zamani-Sabzi, H., King, J. P., Gard, C. C. & Abudu, S. Statistical and analytical comparison of multi-criteria decision-making techniques under fuzzy environment. Oper. Res. Perspect. 3, 92–117. https://doi.org/10.1016/j.orp.2016.11.001 (2016)

30. Zanakis, S. H., Solomon, A., Wishart, N. & Dublish, S. Multi-attribute decision making: A simulation comparison of select methods. Eur. J. Oper. Res. 107(3), 507–529. https://doi.org/10.1016/S0377-2217(97)00147-1 (1998).

31. Zardari, N. H., Ahmed, K., Shirazi, S. M. & Yusop, Z. B. Weighting Methods and their Efects on Multi-criteria Decision Making Model Outcomes in Water Resources Management (Springer, 2015). https://doi.org/10.1007/978-3-319-12586-2.

32. Dehghan-Manshadi, B., Mahmudi, H., Abedian, A. & Mahmudi, R. A novel method for materials selection in mechanical design: combination of non-linear normalization and a modifed digital logic method. Mater. Des. 28(1), 8–15. https://doi.org/10.1016/j. matdes.2005.06.023 (2007).

33. Peng, D. H., Wang, T. D., Gao, C. Y. & Wang, H. Enhancing relative ratio method for MCDM via attitudinal distance measures of interval-valued hesitant fuzzy sets. Int. J. Mach. Learn. Cybern. 8(4), 1347–1368. https://doi.org/10.1007/s13042-016-0510-6 (2017).

34. Mustajoki, J., Hämäläinen, R. P. & Salo, A. Decision support by interval SMART/SWING-incorporating imprecision in the SMART and SWING methods. Decis. Sci. 36(2), 317–339. https://doi.org/10.1111/j.1540-5414.2005.00075.x (2005).

35. Siskos, E. & Tsotsolas, N. Elicitation of criteria importance weights through the Simos method: A robustness concern. Eur. J Oper. Res. 246(2), 543–553. https://doi.org/10.1016/j.ejor.2015.04.037 (2015).

36. Shannon, C. E. & Weaver, W. Te Mathematical Teory of Communication (University of Illinois Press, 1949).

37. Wang, D. & Zhao, J. Design optimization of mechanical properties of ceramic tool material during turning of ultra-high-strength steel 300M with AHP and CRITIC method. Int. J. Adv. Manufac. Technol. 84(9–12), 2381–2390. https://doi.org/10.1007/s00170- 015-7903-7 (2016).

38. Das, D., Bhattacharva, S. & Sarkar, B. Decision-based design-driven material selection: a normative-prescriptive approach for simultaneous selection of material and geometric variables in gear design. Mater. Des. 92, 787–793. https://doi.org/10.1016/j. matdes,2015.12.064 (2016).

39. Mahmoudkelaye, S., Azari, K. T., Pourvaziri, M. & Asadian, E. Sustainable material selection for building enclosure through ANP method. Case Stud. Constr. Mater. 9, e00200. https://doi.org/10.1016/j.cscm.2018.e00200 (2018).

40. Prasad, R. V., Rajesh, R. & Tirumalaikumarasamy, D. Selection of coating material for magnesium alloy using Fuzzy AHP-TOPSIS. Sādhanā 45(1), 1–20. https://doi.org/10.1007/s12046-019-1261-3 (2020).

41. Palanisamy, M., Pugalendhi, A. & Ranganathan, R. Selection of suitable additive manufacturing machine and materials through best–worst method (BWM). Int. J. Adv. Manufac. Technol. https://doi.org/10.1007/s00170-020-05110-6 (2020).

42. Maghsoodi, A. I., Soudian, S., Martínez, L., Herrera-Viedma, E. & Zavadskas, E. K. A phase change material selection using the interval-valued target-based BWM-CoCoMULTIMOORA approach: A case-study on interior building applications. Appl. Sof Comput. 95, 106508. https://doi.org/10.1016/j.asoc.2020.106508 (2020)

43. Yang, W.-C., Ri, J.-B., Yang, J.-Y. & Kim, J.-S. Materials selection criteria weighting method using analytic hierarchy process (AHP) with simplest questionnaire and modifying method of inconsistent pairwise comparison matrix. Proc. Inst. Mech. Eng. L 236(1), 69–85. https://doi.org/10.1177/14644207211039912 (2022).

44. Kumar, S., Bhaumik, S., Patnaik, L., Maity, S. R. & Paleu, V. Application of integrated BWM Fuzzy-MARCOS approach for coating material selection in tooling industries. Materials 15, 9002. https://doi.org/10.3390/ma15249002 (2022).

45. Grachev, D. I. et al. Dental material selection for the additive manufacturing of removable complete dentures (RCD). Int. J. Mol Sci, 24(13), 6432, https://doi,org/10.3390/iims24076432 (2023).

46. Bhowmik, C., Gangwar, S., Bhowmik, S. & Ray, A. Selection of energy-efcient material: An entropy–TOPSIS approach. In Sof Computing: Teories and Applications (eds Pant, M. et al.) 31–39 (Springer, 2018).

47. Oluah, C., Akinlabi, E. T. & Njoku, H. O. Selection of phase change material for improved performance of Trombe wall systems using the entropy weight and TOPSIS methodology. Energy Build. 217, 109967. https://doi.org/10.1016/j.enbuild.2020.109967 (2020).

48. Mahajan, A., Binaz, V., Singh, I. & Arora, N. Selection of natural fber for sustainable composites using hybrid multi criteria decision making techniques. Composites C 7, 100224. https://doi.org/10.1016/j.jcomc.2021.100224 (2022).

49. Akgün, H., Yapıcı, E., Özkan, A., Günkaya, Z. & Banar, M. A combined multi-criteria decision-making approach for the selection of carbon-based nanomaterials in phase change materials. J. Energy Storage 60, 106619. https://doi.org/10.1016/j.est.2023. 106619 (2023).

50. Haq, R. S. U., Saeed, M., Mateen, N., Siddiqui, F. & Ahmed, S. An interval-valued neutrosophic based MAIRCA method for sustainable material selection. Eng. Appl. Artif. Intell. 123, 106177. https://doi.org/10.1016/j.engappai.2023.106177 (2023).

51. Ulutaş, A., Balo, F. & Topal, A. Identifying the most efcient natural fbre for common commercial building insulation materials with an integrated PSI, MEREC LOPCOW and MCRAT model. Polvmers 15(6), 1500. https://doi,org/10.3390/polym15061500 (2023).

52. Gupta, S. M., & Ilgin, M. A. Multiple criteria decision making applications in environmentally conscious manufacturing and product recovery. CRC Press. https://www.routledge.com/Multiple-Criteria-Decision-Making-Applications-in-Environmen tally-Conscious/Gupta-Ilgin/p/book/9780367781798 (2017).

53. Wu, X. & Liao, H. A consensus-based probabilistic linguistic gained and lost dominance score method. Eur. J. Oper. Res. 272(3), 1017–1027, https://doi,org/10.1016/i,eior,2018.07.044 (2019).

54. Chen, Z. S. et al. Sustainable building material selection: A QFD-and ELECTRE III-embedded hybrid MCGDM approach with consensus building, Eng, Appl, Artif. Intell, 85, 783–807, https://doi,org/10.1016/i,engappai,2019.08.006 (2019)

55. Singh, T., Pattnaik, P., Pruncu, C. I., Tiwari, A. & Fekete, G. Selection of natural fbers based brake friction composites using hybrid ELECTRE-entropy optimization technique. Polymer Test. 89, 106614. https://doi.org/10.1016/j.polymertesting.2020. 106614 (2020)

71. Bhuiyan, M. M. A. & Hammad, A. A hybrid multi-criteria decision support system for selecting the most sustainable structura material for a multistory building construction. Sustainability 15(4), 3128. https://doi.org/10.3390/su15043128 (2023).

56. Gul, M., Celik, E., Gumus, A. T. & Guneri, A. F. A fuzzy logic based PROMETHEE method for material selection problems. Beni-Suef Univ, I. Basic Appl, Sci, 7(1), 68–79. https://doi,org/10.1016/i,bibas,2017.07.002 (2018)

57. Zindani, D. & Kumar, K. Material selection for turbine seal strips using PROMETHEE-GAIA method. Mater. Today 5(9), 17533–17539. https://doi.org/10.1016/j.matpr.2018.06.069 (2018).

58. Exconde, M. K. J. E., Co, J. A. A., Manapat, J. Z. & Magdaluyo, E. R. Materials selection of 3D printing flament and utilization of recycled polyethylene terephthalate (PET) in a redesigned breadboard. Procedia CIRP 84, 28–32. https://doi.org/10.1016/j. procir.2019.04.337 (2019)

59. Kirişci, M., Demir, I. & Şimşek, N. Fermatean fuzzy ELECTRE multi-criteria group decision-making and most suitable biomedical material selection. Artif. Intell. Med. 127, 102278. https://doi.org/10.1016/j.artmed.2022.102278 (2022).

60. Zhou, D. Choosing the optimal recycled plastic for making 3D printing flament by ELECTRE decision model. Proc. SPIE Int. Soc. Opt. Eng. https://doi.org/10.1117/12.2639070 (2022).

61. Jayakrishna, K. & Vinodh, S. Application of grey relational analysis for material and end of life strategy selection with multiple Int. J. Mater. Eng. Innov. 8

62. Zhang, H., Peng, Y., Tian, G., Wang, D. & Xie, P. Green material selection for sustainability: A hybrid MCDM approach. PLoS ONE 12(5), e0177578. https://doi.org/10.1371/journal.pone.0177578 (2017).

63. Sanghvi, N., Vora, D., Charaya, E., Patel, J. & Sharma, S. An approach for material selection for bone staple (an orthopaedic implant) using GRA and Fuzzy logic. Mater. Today https://doi.org/10.1016/j.matpr.2020.11.331 (2020).

64. Wang, D. & Li, S. Material selection decision-making method for multi-material lightweight automotive body driven by performance. Proc. Inst. Mech. Eng. L 236(4), 730–746. https://doi.org/10.1177/14644207211055661 (2021).

65. Dwivedi, P. & Sharma, D. K. Application of Shannon entropy and CoCoSo methods in selection of the most appropriate engineering sustainability components. Clean. Mater. 5, 100118. https://doi.org/10.1016/j.clema.2022.100118 (2022).

66. Maidin, N. A., Sapuan, S. M., Taha, M. M. & Mohd, Z. M. Y. Constructing a framework for selecting natural fbres as reinforce ments composites based on grey relational analysis. Phys. Sci. Rev. https://doi.org/10.1515/psr-2022-0081 (2022).

67. Maidin, N. A., Sapuan, S. M., Mastura, M. T. & Zuhri, M. Y. M. Materials selection of thermoplastic matrices of natural fbre composites for cyclist helmet using an integration of DMAIC approach in six sigma method together with grey relational analysis approach. J. Renew. Mater. 11(5), 2381–2397. https://doi.org/10.32604/jrm.2023.026549 (2023).

68. Ishak, N. M., Malingam, S. D. & Mansor, M. R. Selection of natural fbre reinforced composites using fuzzy VIKOR for car fronthood. Int. J. Mater. Prod. Technol. 53(3–4), 267–285. https://doi.org/10.1504/IJMPT.2016.079205 (2016).

69. Dev, S., Aherwar, A. & Patnaik, A. Material selection for automotive piston component using entropy-VIKOR method. SILICON 12(1), 155–169. https://doi.org/10.1007/s12633-019-00110-y (2020).

70. Gadhave, P. D., Prabhune, C. & Pathan, F. Selection of phase change material for domestic water heating using multi criteria decision approach. Aust. I. Mech. Eng, 21(1), 295–315. https://doi.org/10.1080/14484846.2020.1842297 (2020)

72. Xue, Y., You, J., Lai, X. & Liu, H. An interval-valued intuitionistic fuzzy MABAC approach for material selection with incomplete weight information. Appl. Sof Comput. 38, 703–713. https://doi.org/10.1016/j.asoc.2015.10.010 (2016).

73. Tian, G. et al. Green decoration materials selection under interior environment characteristics: A grey-correlation based hybrid MCDM method. Renew. Sustain. Energy Rev. 81, 682–692. https://doi.org/10.1016/j.rser.2017.08.050 (2018).

74. Ahmed, M., Qureshi, M. N., Mallick, J. & Ben Kahla, N. Selection of sustainable supplementary concrete materials using OSM-AHP-TOPSIS approach. Adv. Mater. Sci. Eng. https://doi.org/10.1155/2019/2850480 (2019).

75. Deshmukh, D. & Angira, M. Investigation on switching structure material selection for RF-MEMS shunt capacitive switches using Ashby, TOPSIS and VIKOR. Trans. Electr. Electron. Mater. 20(3), 181–188. https://doi.org/10.1007/s42341-018-00094-3 (2019).

76. Maghsoodi, A. I., Maghsoodi, A. I., Poursoltan, P., Antucheviciene, J. & Turskis, Z. Dam construction material selection by implementing the integrated SWARA–CODAS approach with target-based attributes. Arch. Civil Mech. Eng. 19(4), 1194–1210. https://doi.org/10.1016/j.acme.2019.06.010 (2019).

77. Roy, J., Das, S., Kar, S. & Pamučar, D. An extension of the CODAS approach using interval-valued intuitionistic fuzzy set for sustainable material selection in construction proiects with incomplete weight information. Symmetry 11(3), 393. https://doi. org/10.3390/sym11030393 (2019).

78. Yadav, S., Pathak, V. K. & Gangwar, S. A novel hybrid TOPSIS-PSI approach for material selection in marine applications. Sadhana-Acad. Proc. Eng. Sci. https://doi.org/10.1007/s12046-018-1020-x (2019).

79. Dhanalakshmi, C. S., Madhu, P., Karthick, A., Mathew, M. & Kumar, R. V. A comprehensive MCDM-based approach using TOPSIS and EDAS as an auxiliary tool for pyrolysis material selection and its application. Biomass Convers. Biorefinery https:// doi.org/10.1007/s13399-020-01009-0 (2020).

80. Kar, S. & Jha, K. N. Assessing criticality of construction materials for prioritizing their procurement using ANP-TOPSIS. Int. J. Constr, Manag, https://doi,org/10.1080/15623599.2020.1742637 (2020)

81. Patra, P. & Angira, M. Investigation on dielectric material selection for RF-MEMS shunt capacitive switches using ashby, TOPSIS and VIKOR. Trans. Electr. Electron. Mater. 21(2), 157–164. https://doi.org/10.1007/s42341-019-00162-2 (2020)

82. Yang, W.-C., Chon, S.-H., Choe, C.-M. & Yang, J.-Y. Materials selection method using TOPSIS with some popular normalization methods. Eng. Res. Express 3(1), 015020. https://doi.org/10.1088/2631-8695/abd5a7 (2021).

83. Kumar, P. G., Meikandan, M., Sakthivadivel, D. & Vigneswaran, V. S. Selection of optimum glazing material for solar thermal applications using TOPSIS methodology. Int. J. Ambient Energy 42(3), 274–278. https://doi.org/10.1080/01430750.2018.15426 26 (2021).

84. de Aires, R. F. & Ferreira, L. A new multi-criteria approach for sustainable material selection problem. Sustainability 14(18) 11191. https://doi.org/10.3390/su141811191 (2022).

85. Abishini, A. & Karthikeyan, K. Application of MCDM and Taguchi super ranking concept for materials selection problem. Mater. Today 72, 2480–2487. https://doi.org/10.1016/j.matpr.2022.09.526 (2022).

86. Kazemian, N. et al. Material selection of intraoral stents for head and neck cancer patients undergoing radiation therapy: A Multi-criteria multi-physics design approach. Mater. Des. 225, 111558. https://doi.org/10.1016/j.matdes.2022.111558 (2023).

87. Sharma, V, et al. Multi-criteria decision making methods for selection of lightweight material for railway vehicles, Materials 16(1), 368. https://doi.org/10.3390/ma16010368 (2022).

88. Remadi, F. D. & Frikha, H. M. Te triangular intuitionistic fuzzy numbers CODAS method for solving green material selection problem. Int. J. Oper. Res. 46(3), 398–415. https://doi.org/10.1504/ijor.2022.10049713 (2023).

89. Wankhede, S., Pesode, P., Gaikwad, S., Pawar, S. & Chipade, A. Implementing combinative distance base assessment (CODAS) for selection of natural fibre for long lasting composites. Mater. Sci. Forum 1081, 41–48. https://doi,org/10.4028/p-4pd120 (2023).

90. Zhang, K., Zhan, J. & Yao, Y. TOPSIS method based on a fuzzy covering approximation space: An application to biological nano-materials selection. Inf. Sci. 502, 297–329. https://doi.org/10.1016/j.ins.2019.06.043 (2019).

91. Hafezalkotob, A. & Hafezalkotob, A. Comprehensive MULTIMOORA method with target-based attributes and integrated signifcant coefcients for materials selection in biomedical applications. Mater. Des. 87, 949–959. https://doi.org/10.1016/j. matdes.2015.08.087 (2015).

92. Mousavi-Nasab, S. H. & Sotoudeh-Anvari, A. A comprehensive MCDM-based approach using TOPSIS, COPRAS and DEA as an auxiliary tool for material selection problems. Mater. Des. 121, 237–253. https://doi.org/10.1016/j.matdes.2009.08.013 (2017).

93. Zhang, H. et al. Materials selection of 3D-printed continuous carbon fber reinforced composites considering multiple criteria. Mater. Des. 196, 109140. https://doi.org/10.1016/j.matdes.2020.109140 (2020)

94. Zhang, O., Hu, J., Feng, J. & Liu, A. A novel multiple criteria decision making method for material selection based on GGPFWA operator. Mater. Des. 195, 109038. https://doi.org/10.1016/j.matdes.2020.109038 (2020).

95. Chatterjee, P., Athawale, V. M. & Chakraborty, S. Materials selection using complex proportional assessment and evaluation of mixed data methods. Mater. Des. 32(2), 851–860. https://doi.org/10.1016/j.matdes.2010.07.010 (2011).

96. Rathod, M. K. & Kanzaria, H. V. A methodological concept for phase change material selection based on multiple criteria decision analysis with and without fuzzy environment. Mater. Des. 32(6), 3578–3585. https://doi.org/10.1016/j.matdes.2011.02.040 (2011).

97. Wendt, F. Compromise, Peace and Public Justifcation: Political Morality Beyond Justice (Springer, 2016). https://doi.org/10.1007/ 978-3-319-28877-2\_5.

98. Zakeri, S. & Konstantas, D. Solving decision-making problems using a measure for information values connected to the equilibrium points (IVEP) MCDM method and Zakeri-Konstantas performance correlation coefcient. Information 13(11), 512. https://doi.org/10.3390/info13110512 (2022).

99. Bączkiewicz, A. et al. Comparative analysis of solar panels with determination of local signifcance levels of criteria using the mcdm methods resistant to the rank reversal phenomenon. Energies 14(18), 5727. https://doi.org/10.3390/en14185727 (2021).

100. Piegat, A. & Sałabun, W. Identifcation of a multicriteria decision-making model using the characteristic objects method. Appl. Comput. Intell. Sof Comput. 2014, 14–14. https://doi.org/10.1155/2014/536492 (2014).

101. Sałabun, W. Te characteristic objects method: a new distance-based approach to multicriteria decision-making problems. J. Multi-Crit, Decis, Anal, 22(1–2), 37–50, https://doi,org/10.1002/mcda,1525 (2015)

102. Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. Te SPOTIS rank reversal free method for multi-criteria decision-making support. In 2020 IEEE 23rd International Conference on Information Fusion (FUSION), pp 1–8 (IEEE, 2020). https://doi.org 10.23919/FUSION45008.2020.9190347

103. Žižović, M., Pamučar, D., Albijanić, M., Chatterjee, P. & Pribićević, I. Eliminating rank reversal problem using a new multiattribute model-the RAFSI method. Mathematics 8(6), 1015. https://doi.org/10.3390/math8061015 (2020).

104. Munier, N. A new approach to the rank reversal phenomenon in MCDM with the SIMUS method. Multiple criteria decision making, (11), 137–152. https://bibliotekanauki.pl/articles/578600.pdf (May 2023) (2016).

105. Wątróbski, J., Bączkiewicz, A., Król, R. & Sałabun, W. Green electricity generation assessment using the CODAS-COMET method. Ecol. Indic. 143, 109391. https://doi.org/10.1016/j.ecolind.2022.109391 (2022).

106. Shekhovtsov, A., Więckowski, J., Kizielewicz, B., & Sałabun, W. Efect of Criteria Range on the Similarity of Results in the COMET Method. In 2021 16th Conference on Computer Science and Intelligence Systems (FedCSIS), pp 453–457 (IEEE, 2021). https:// doi.org/10.15439/2021F44

107. Faizi, S., Sałabun, W., Ullah, S., Rashid, T. & Więckowski, J. A new method to support decision-making in an uncertain environment based on normalized interval-valued triangular fuzzy numbers and comet technique. Symmetry 12(4), 516. https://doi org/10.3390/sym12040516 (2020).

108. Palczewski, K. & Sałabun, W. Identifcation of the football teams assessment model using the COMET method. Procedia Comput. Sci. 159, 2491–2501. https://doi.org/10.1016/j.procs.2019.09.424 (2019).

109. Chatterjee, P. & Chakraborty, S. Material selection using preferential ranking methods. Mater. Des. 35, 384–393. https://doi.org/ 10.1016/j.matdes.2011.09.027 (2012)

110. Hatef, S. M., Asadi, H., Shams, G., Tamošaitienė, J. & Turskis, Z. Model for the sustainable material selection by applying integrated Dempster-Shafer evidence theory and additive ratio assessment (ARAS) method. Sustainability 13, 10438. https://doi. org/10.3390/su131810438 (2021).

111. Liu, H. C., You, J. X., Zhen, L. & Fan, X. J. A novel hybrid multiple criteria decision making model for material selection wit target-based criteria. Mater. Des. 60, 380–390. https://doi.org/10.1016/j.matdes.2014.03.071 (2014).

112. Toledo, H., Martínez-Gómez, J. & Nicolalde, J. F. Selection of rear axle tip alternative material of a car by multi-criteria means. Int. J. Math. Oper. Res. 21(1), 46–66. https://doi.org/10.1504/IJMOR.2022.120320 (2022).

## Author contributions

S.Z.: Conceptualization, Methodology, Validation, Formal analysis, Writing—Original Draf, Visualization. P.C.: Resources, Investigation, Data Curation, Writing—Review & Editing. D.K.: Supervision, Writing—Original Draf, Writing—Review & Editing. F.E.: Writing- Reviewing and Editing, Validation.

## Competing interests

Te authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to S.Z.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/64ee64686143d5d7a5863576c1bc5b1b1bf3021053566adf93f52048c3ea71ed.jpg)

Cc Open Access Tis article is licensed under a Creative Commons Attribution 4.0 International BY License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. Te images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© Te Author(s) 2023