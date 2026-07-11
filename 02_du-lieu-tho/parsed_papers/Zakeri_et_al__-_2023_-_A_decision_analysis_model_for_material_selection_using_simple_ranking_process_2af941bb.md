## OPEN


# A decision analysis model for material selection using simple ranking process

#### Shervin Zakeri [1][*], Prasenjit Chatterjee [2], Dimitri Konstantas [1] & Fatih Ecer [3]

**A large number of materials and various criteria fashion material selection problems as complex multi-**
**criteria decision-making (MCDM) problems. This paper proposes a new decision-making method called**
**the simple ranking process (SRP) to solve complex material selection problems. The accuracy of the**
**criteria weights has a direct impact on the outcomes of the new method. In contrast to current MCDM**
**methods, the normalization step has been eliminated from the SRP method as a potential source**
**of producing incorrect results. The application of the method is appropriate for situations with high**
**levels of complexity in material selection because it only considers the ranks of alternatives in each**
**criterion. The first scenario of vital-immaterial mediocre method (VIMM) is used as a tool to derive**
**criteria weights based on expert assessment. The result of SRP is compared with a number of MCDM**
**methods. In order to evaluate the findings of analytical comparison, a novel statistical measure known**
**as compromise decision index (CDI) is proposed in this paper. CDI revealed that the MCDM methods’**
**outputs for solving the material selection could not be theoretically proven and requires to be**
**evaluated through practice. As a result, the dependency analysis-an additional innovative statistical**
**measure is introduced to demonstrate the reliability of MCDM methods by assessing its dependency**
**on criteria weights. The findings demonstrated that SRP is extremely reliant on criteria weights and**
**its reliability rises with the number of criteria, making it a perfect tool for solving challenging MCDM**
**problems.**

Material selection problems and multi-criteria decision-making (MCDM) methods have strong relationships.
Selecting suitable materials is the most challenging task in designing and developing new ­products[1]. Engineering
design revolves around the objectives of achieving high performance, minimizing costs, and being environmentally conscious, which are often constrained by materials. Therefore, one of the key goals of optimal product
design is the selection of materials that fulfill the design criteria while delivering the highest level of performance
at the most economical ­cost[2][,][3]. Material selection is a complex decision-making process that involves the selection
of the most suitable materials from a range of available alternatives based on multiple criteria. Multi-Criteria
Decision Making (MCDM) refers to a class of mathematical methods used to solve such complex decisionmaking problems. These problems often arise in real-world situations where decision-makers has to select from
a set of alternatives that differ across several criteria or dimensions. The goal of MCDM is to identify the best
possible alternative or set of alternatives based on the decision-makers’ preferences and priorities. MCDM problems are typically represented in a matrix format, where each row represents an alternative and each column
represents a criterion. The elements of the matrix correspond to the performance of each alternative on each
criterion. The decision-makers are then asked to provide weights or priorities for each criterion, indicating the
relative importance of each criterion in the decision-making process. Material selection problems also involve
the evaluation and selection of the most suitable material from a set of alternatives based on multiple criteria.
This type of problem requires a decision-maker to weigh the importance of each criterion and to evaluate the
alternatives accordingly. Material selection decisions typically involve multiple conflicting criteria, such as cost,
performance, durability, physical and engineering properties, environmental factors, cost, and manufacturability, among others. These criteria may have different units of measurement, making it challenging to compare
and evaluate alternatives using a single metric. Since the material selection could be converted into an MCDM
problem-form problem, MCDM methods are suitable solutions to find the best material to meet the needs of
the design and development of products. Many researchers have drawn attention to the connection between

1Geneva School of Economics and Management, University of Geneva, 1211 Geneva, Switzerland. 2Faculty of
Civil Engineering, Institute of Sustainable Construction, Laboratory of Operational Research, Vilnius Gediminas
Technical University, Vilnius, Lithuania. [3]Sub‑Department of Operations Research, Faculty of Economics and
Ad i i t ti S i Af K t U i it Af k hi T k - il Sh i k i@ t i h


-----

MCDM methods and material selection problems. According ­to[4], among various methods and techniques that are
employed to select the most suitable material for different projects, MCDM methodologies are among the most
popular approaches. ­Reference[5] call material selection problems MCDM dilemmas, ­and[6] believe that MCDM
methods are the only solution for the material selection problems that incorporate a large number of competing
performance characteristics and are involved with many decision-makers. Similar to the latter ­authors[7], argues
that MCDM methods are efficient tools for effectively managing material selection problems incorporating
various material properties and varied criteria. ­Reference[8] also mentioned that MCDM methods aid in achieving the desired results from a product since the methods evaluate the materials’ performance under conflicting
criteria. The use of MCDM methods in material selection problems has several advantages. First, it provides a
systematic and objective approach to evaluate and rank materials based on multiple criteria. Second, it helps
decision-makers to identify the critical criteria that have the most significant impact (having highest weight
value) on the decision. Third, it enables decision-makers to evaluate and compare the performance of different
materials under different scenarios. Finally, it provides a transparent and structured approach to the decisionmaking process, which can help to build consensus and improve communication among stakeholders. MCDM
methods are widely used in material selection problems for computing the criteria weights and determining the
rank of materials. Different scholars have proposed various categories for these two tasks. MCDM weighting
methods can generally be classified into two categories: subjective weighting methods and objective weighting
methods. The subjective weighting methods rely solely on human opinions, expectations, and judgments to
assign weights to the criteria, whereas the objective weighting methods extract the criteria weights from the
matrix of the decision-making problem. The ranking methods are divided into four subcategories, including the
outranking methods, compromise ranking methods, distance-based methods, and the methods that use pairwise
comparison. The complexity of an MCDM problem is associated with:

1. The complexity of input, involving objective and subjective values,
2. Different numbers of goals involved in the evaluation process of the alternatives,
3. Confliction between the nature of the criteria in the MCDM problems with multiple layers of criteria,
4. The number of non-beneficial criteria,
5. The number of criteria.

In this case, material selection problems always involve many alternatives and criteria, where with increasing
the number of criteria, the reliability of the MCDM methods used for ranking the material decreases. To solve
this problem, this paper proposes new MCDM method, called simple ranking process (SRP) which is based on
ranking the alternatives against each criterion. The precision of criteria weight estimation directly affects the
effectiveness of SRP algorithm. The new method is designed to deal with complex decision-making problems
using simple processes compared to the existing MCDM methods. In this paper, the new method is applied to
solve a material selection problem. Criteria weights of the problem are reassessed by the seven experts through
a group decision-making process, followed by the application of vital-immaterial mediocre method (VIMM) to
provide accurate weights. VIMM, which was proposed ­by[9], is a subjective weighting method that was developed
to bridge the structural and processual gaps in AHP and BWM. The paper presents several contributions centered
around a new MCDM method that can effectively address complex decision-making problems. Reliability of the
method is also shown to increase as the complexity of the problem increases. Additionally, the paper introduces
two new statistical measures for validating results of MCDM methods. The paper is structured as follows: the
second section presents the literature review, while the third section describes the proposed method and VIMM.
The fourth section applies the methods to a real-world material selection problem. The fifth section discusses
the results and introduces a new statistical measure to validate complex MCDM solutions. The paper concludes
in the sixth section with a summary of the findings and suggestions for future research.

### Literature review
Dissimilar mathematical treatments are employed by different MCDM methods based on the categories they
are members of to derive the best material, consequently offering different materials as the most suitable option
for the same problem. With an extensive literature review, this section aims to provide a scientific perspective
for the readers regarding the MCDM methods application in material selection problems and the gaps in the
current course of MCDM methods and material selection engagement. Specifically, this section seeks to demonstrate the following:

1. The investigation of the relationship between MCDM methods in the different categories with the different
complex material selection problems,
2. The prevalent problem of dissimilarities between the outputs of the MCDM methods in solving material
selection problems that are revealed by different studies, which emerges as the results validation issues,
3. Solutions the studies employed to overcome the dissimilarities.

These gaps will be later addressed in the paper. To visualize the literature review section’s composition, its
structure has been illustrated in Fig. 1.

#### MCDM methods for material selection problems. Appropriate material selection results in improved
quality and enhanced product life cycle, while inaccurate selection leads to increased design cost, lack of productivity, poor end product performance, critical component damage, and eventually untimed product ­failure[10].


-----

**Figure 1. The literature review structure.**

Thus, it is critical to exert a method that optimizes material selection decisions and minimizes the risk of poor
selection. This paper proposes a new MCDM method to solve this problem. So far, several MCDM methods
for material selection problems have been developed and applied. The technique for order of preference by
similarity to ideal solution (TOPSIS) developed by Hwang and ­Yoon[11], analytic hierarchy process (AHP) by
­Saaty[12], analytical network process (ANP) proposed by ­Saaty[13][,] simple additive weighted (SAW) (MacCrimmon
& Rand.[14][,] data envelopment analysis (DEA) proposed by ­Charnes[15], Vise Kriterijumska Optimizacija I Kompromisno Resenje (VIKOR) developed by Opricovic and ­Tzeng[16], decision making trial and evaluation laboratory
(DEMATEL) developed by Fontela and ­Gabus[17], preference ranking organization method for enrichment evaluations (PROMETHEE)[18] and ELimination Et Choix Traduisant la REalité or ELimination and Choice expressing reality (ELECTRE) proposed and advocated by ­Roy[19] are some of the most popular MCDM methods for
material selection problems. Some of the recent developments in MCDM methods are ranking based on optimal
points multi-criteria decision-making method (RBOP) by Zakeri.[20][,] step-wise weight assessment ratio analysis
(SWARA) first developed by Keršulienė & ­Turskis[21], subjective weighting method using continuous interval
scale by Toloie-Eshlaghy et al.[22][,] superiority and inferiority ranking (SIR) method by ­Xu[23], multi-attribute evaluation using imprecise weight estimates (IMP) method proposed by ­Jessop[24], and best–worst method (BWM)
introduced by ­Rezaei[25].
In some problems, the outputs of MCDM methods are ­dissimilar[26][,][27]. The comparison of MCDM methods
and their outputs can be found in Refs.[28][,][29]. To evaluate alternative hydropower systems on the “Drina River,”
Opricovic & ­Tzeng[28] compared the extended VIKOR method with TOPSIS, PROMETHEE, and ELECTRE, where
the TOPSIS and VIKOR generated the same ranking for the two best alternatives while the ratio was different. By
utilizing Kendall’s tau-b test and Spearman’s rho test to determine the significance of rank correlation between
the compared methods, the sensitivity of final ranks to selected fuzziness intervals, and the sensitivity of similarities and dissimilarities of different decision ranking methods to the dimensions of the decision matrix, the
appropriate MCDM method was selected in the work of Zamani-Sabzi et al.[29]. They evaluated the performances
of ten popular MCDM methods including SAW, weighted product method (WPM), compromise programming
(CP), TOPSIS, AHP, VIKOR, and ELECTRE under a fuzzy environment. According to Ref.[30], the inconsistency
that occurred in generating dissimilar results by MCDM methods is due to four reasons:

1. The methods use weights differently in their calculations.
2. Algorithms differ in their approach to selecting the ‘best’ solution.
3. Many algorithms attempt to scale the objectives, which affects the weights already chosen.
4. Some algorithms introduce additional parameters that affect the selection of the solution.

The most important reasons that directly affect the final output of the MCDM methods are 1. Determining
criteria weights; and 2. Policies/philosophies for evaluating alternatives. The application of these two items to
material selection problems has been discussed in the following sections.

_MCDM methods for criteria weighting._ One of the main challenges in MCDM problems is to determine the
relative importance of each criterion. Criteria weighting methods are used to assign weights to the criteria,
reflecting their relative importance in the decision-making process. Criteria weighting methods in MCDM
environment are mostly divided into subjective and objective methods. There is also a third type of weighting method, popularly known as combinative weighting method, which utilizes hybridization or integration of
different subjective and objective methods using multiplication and additive ­synthesis[31]. Subjective weighting
methods depend on DMs’ judgments, levels of knowledge, perception, and intentions,and these methods do not
use a formal mathematical approach to determine the eights but rather rel on the e perience and e pertise


-----

of the decision-makers. Subjective weighting methods are often used when there is a lack of data or when the
criteria are difficult to quantify. On the other hand, objective weighting methods extract weights directly from
decision matrix using mathematical algorithms without considering human judgments to avoid inaccuracies
and imprecisions. In order to reduce errors and ambiguities in the decision-making process, hybrid weighting
methods (subjective and objective methods) have also been developed. Some of the most popular subjective
methods are Digital Logic and Modified Digital Logic ­methods[32], Pairwise Comparison (e.g. AHP), Best–worst
Method, Ratio ­method[33],[ Swing ­method][34][, Simple multi-attribute ranking technique (SMART) and SIMOS ]

­method[35]. Some of the most popular objective weighting methods are Shannon’s ­entropy[36] and CRITIC (The
CRiteria Importance Through Intercriteria Correlation) ­methods[37]. An overview of MCDM weighting methods
for material selection problems has been presented briefly in the following sections.

Subjective weighting methods in materials selection. Some examples of the subjective weighting methods in
the complex material selection problems to evaluate the importance of the selected criteria are shown in Table 1.
AHP and BWM methods are observed to be very popular methods for criteria weighting in material selection problems. AHP provides a systematic and structured approach to decision-making and helps to organize
complex decision problems in a hierarchical structure, making it easier for decision-makers to understand the
problem and the relationships between the criteria. On the other hand, BWM is a straightforward method that
requires decision-makers to select the best and worst criteria from a set of options, making it easy to understand
and apply.

Objective weighting methods in materials selection. Shannon’s entropy method is one of the most popular
objective methods for computing criteria weights for material selection applications. Compared to other objective weighting methods, most studies employed Shannon’s entropy to compute the criteria weights in this category. Apart from Entropy method, there are other recently developed objective weighting methods like method
based on the removal effects of criteria (MEREC) and logarithmic percentage change driven objective weighting
(LOPCOW). Table 2 shows instances of using objective weighting methods in material selection problems.

_MCDM methods for ranking alternatives._ MCDM methods are generally developed for ranking alternatives
based on four main concepts:

**Criteria** **Subjective weighting method**

1. The pressure angle, 2. Module, 3. Number of teeth to
Material selection case study of spur gear reduction unit AHP
avoid interference, 4. Gear width, and 5. Gear material

Economic, technical, environmental, and socio-cultural
To select sustainable materials for building enclosures ANP
and their corresponding sub-criteria

To select the best composite materials for wear-resistant 1. Physical properties, 2. Mechanical properties, 3. Slurry
AHP
abrasion, 4. Wear properties

1. Density, 2. Thermal conductivity, 3. Thermal expansion
coefficient hardness, 4. Young’s modulus elastic recovery,
5. Critical load, 6. Yield stress, 7. Melting temperature, 8.
H/E ratio H3/E2 ratio, 10. Wear resistance, 11. Coefficient
of friction, 12. Radiation sensitivity, 13. Workability, 14.
Appearance, 15. Oxidation resistance, 16. Oxidation rate
constant, 17. Impact resistance, 18. The possibility of

Coating material for magnesium alloy Fuzzy AHP

surface treatment material, 19. Manufacturing, 20. Availability, 13. Accessibility, 14. Toxicity, 15. Adhesion to the
substrate, 16. Bond strength, 17. Durability, 18. Brittleness,
19. Compatibility of the material, 20. Matrix, 21. Framed,
22. Mixed, 23. The aging tendency, 24. Porosity, 25. Geographical location, 26/political stability & foreign policy,
27. Exchange rate & economic position

1. Cost, 2. Visual and aesthetic modeling, 3. Tensile
strength, 4. Shore hardness, 5. Mixing number, 6. Number

Additive manufacturing machine and materials BWM

of digital materials, 7. Frequent order, and 8. Elongation
at break

1. Melting temperature, 2. Latent heat storage capacity, 3.

Phase change material selection for interior building

Thermal conductivity, 4. Specific heat capacity, 5. Energy BWM
density and 6. Cost

Phase change material selection for solar domestic hot 1. Latent heat, 2. Density, 3. Specific heat for solid, 4. SpeAHP
cific heat for liquid, 5. Thermal conductivity and 6. Cost

1. Indentation hardness, 2. Young’s modulus, 3. Wear
resistance, 4. Plastic Deformation, 5. Strain hardening

Coating material selection in tooling industries BWM

exponent, 6. Coefficient of thermal expansion, 7. Surface
roughness, 8. Coefficient of friction 9. Wear rate

1. Thermal conductivity, 2. Periodic thermal transmittance,
Thermal insulation material selection 3. Specific heat, 4. Density, 5. Decrement factor, 6. Surface Fuzzy BWM
mass, 7. Thermal transmittance, 8. Thermal wave shift

Dental material selection in manufacturing removable 1. Mechanical properties, 2. Biological properties, 3. TriboAHP
logical properties, 4. Technological properties and 5. Cost

**Table 1. Subjective weighting methods and their applications in materials selection.**

|Author(s)|Case application|Criteria|Subjective weighting method|
|---|---|---|---|
|Das et al.38|Material selection case study of spur gear reduction unit|1. Teh pressure angle, 2. Module, 3. Number of teeth to avoid interference, 4. Gear width, and 5. Gear material|AHP|
|Mahmoudkelaye et al.39|To select sustainable materials for building enclosures|Economic, technical, environmental, and socio-cultural and their corresponding sub-criteria|ANP|
|Patnaik et al.10|To select the best composite materials for wear-resistant applications|1. Physical properties, 2. Mechanical properties, 3. Slurry abrasion, 4. Wear properties|AHP|
|Prasad et al.40|Coating material for magnesium alloy|1. Density, 2. Tehrmal conductivity, 3. Tehrmal expansion coefficient hardness, 4. Young’s modulus elastic recovery, 5. Critical load, 6. Yield stress, 7. Melting temperature, 8. H/E ratio H3/E2 ratio, 10. Wear resistance, 11. Coefficient of friction, 12. Radiation sensitivity, 13. Workability, 14. Appearance, 15. Oxidation resistance, 16. Oxidation rate constant, 17. Impact resistance, 18. Teh possibility of surface treatment material, 19. Manufacturing, 20. Avail- ability, 13. Accessibility, 14. Toxicity, 15. Adhesion to the substrate, 16. Bond strength, 17. Durability, 18. Brittleness, 19. Compatibility of the material, 20. Matrix, 21. Framed, 22. Mixed, 23. Teh aging tendency, 24. Porosity, 25. Geo- graphical location, 26/political stability & foreign policy, 27. Exchange rate & economic position|Fuzzy AHP|
|Palanisamy et al.41|Additive manufacturing machine and materials|1. Cost, 2. Visual and aesthetic modeling, 3. Tensile strength, 4. Shore hardness, 5. Mixing number, 6. Number of digital materials, 7. Frequent order, and 8. Elongation at break|BWM|
|Maghsoodi et al.42|Phase change material selection for interior building surface application|1. Melting temperature, 2. Latent heat storage capacity, 3. Tehrmal conductivity, 4. Specific heat capacity, 5. Energy density and 6. Cost|BWM|
|Yang et al.43|Phase change material selection for solar domestic hot water system|1. Latent heat, 2. Density, 3. Specific heat for solid, 4. Spe- cific heat for liquid, 5. Tehrmal conductivity and 6. Cost|AHP|
|Kumar et al.44|Coating material selection in tooling industries|1. Indentation hardness, 2. Young’s modulus, 3. Wear resistance, 4. Plastic Deformation, 5. Strain hardening exponent, 6. Coefficient of thermal expansion, 7. Surface roughness, 8. Coefficient of friction 9. Wear rate|BWM|
|Aksakal et al.4|Tehrmal insulation material selection|1. Tehrmal conductivity, 2. Periodic thermal transmittance, 3. Specific heat, 4. Density, 5. Decrement factor, 6. Surface mass, 7. Tehrmal transmittance, 8. Tehrmal wave shift|Fuzzy BWM|
|Grachev et al.45|Dental material selection in manufacturing removable dentures|1. Mechanical properties, 2. Biological properties, 3. Tribo- logical properties, 4. Technological properties and 5. Cost|AHP|


-----

|Author(s)|Case application|Criteria|Objective weighting method|
|---|---|---|---|
|Bhowmik et al.46|Energy-efficient materials|1. Density, 2. Bulk Modulus, 3. Compressive Strength, 4. Tehr- mal Conductivity, 5. Tehrmal Expansion, 6. Resistivity, 7. Cost, 8. Energy Production, and 9. ­CO Emission 2|Entropy|
|Oluah et al.47|Latent heat storage materials for optimal performance of a Trombe wall|1. Heat of Fusion, 2. Tehrmal Conductivity, 3. Density, and 4. Cost|Entropy|
|Aksakal et al.4|Tehrmal insulation material|1. Tehrmal Conductivity, 2. Periodic Tehrmal Transmittance, 3. Specific Heat, 4. Density, 5. Decrement Factor, 6. Surface Mass, 7. Tehrmal Transmittance, and 8. Tehrmal Wave Shift|CRITIC|
|Mahajan et al.48|Natural Fiber for Sustainable Composite|1. Aspect Ratio, 2. Strain at break, 3. Specific strength, 4. Spe- cific modulus, 5. Moisture Absorption, and 6. Cost|Entropy and CRITIC|
|Akgün et al.49|Selection of most appropriate carbon-based nanomaterials|1. Melting Point Temperature Change, 2. Latent Heat Change, 3. Tehrmal Conductivity Enhancement, 4. Leakage, 5. Greenhouse Gas, 6. Cost, and 7. Agglomeration|Entropy|
|Haq et al.50|Material selection for wing-spar of human-powered aircraft|1. Price, 2. Tensile Strength, 3. Young’s Modulus, 4. Density, 5. Compressive Strength, 6. Creep Resistance, 7. Fatigue Resistance, 8. Machinability, 9. Recyclability and 10. Carbon Footprint During Manufacture|Entropy|
|Ulutaş et al.51|Building insulation material selection|1. vapour diffusion resistance factor, 2. sound absorption coefficient, 3. embodied carbon, 4. embodied energy, 5. cost, 6. reaction to fire, 7. specific heat capacity, 8. thermal conductiv- ity, and 9. density|MEREC and LOPCOW|


**Table 2. Objective weighting methods and their applications in materials selection.**

1. Outranking methods such as ELECTRE, PROMETHEE, and GLDS (Gain and Lost Dominance Score).
2. Compromise ranking policies such as VIKOR, GRA.
3. Distance-based methods such as TOPSIS, Evaluation based on Distance from Average Solution (EDAS),
Multi-Attributive Border Approximation Area Comparison (MABAC) and Combinative Distance-based
Assessment Method (CODAS).
4. Pairwise comparison such as AHP and ANP.

There are other categorizations suggested by scholars, e.g. the classification of the MCDM methods into five

­classes[52][,] including the quantitative methods, qualitative methods, mixed techniques, heuristics, and metaheuristics, and simulation,or categorizing them into the three main ­groups[53] including the utility value-based methods,
the outranking methods, preference ordering based methods. Except for the pairwise comparison methods,
which have been discussed earlier, in the following sections, the application of MCDM methods to material
selection problems has been briefly reviewed based on the three MCDM categories comprising outranking,
compromise ranking, and distance-based ranking methods.

Material selection using outranking methods. Different forms of ELECTRE method have been applied to
material selection problems. Using a hybrid method and the opinions of four experts in a group decision-making
­framework[54], employed ELECTRE III to solve the office flooring selection problem, in which the ease of cleaning
and maintenance, durability, quietness, style and comfort, sustainability, and cost-effectiveness have been used
as criteria. Singh et al.[55] employed a hybrid model of ELECTRE II and entropy to solve the friction composite
selection problem consisting of seven attributes and nine alternatives. ELECTRE and PROMETHEE methods
have also been used to solve material selection problems. Gul et al.[56] proposed a solution for an automotive
instrument panel material selection problem using fuzzy PROMETHEE method while considering Styrene
Maleic Anhydride, Polycarbonate, Polypropylene, and Acrylonitrile Butadiene Styrene as the potential material
alternatives, and maximum temperature limit, recyclability, elongation, weight, thermal conductivity, tensile
strength, cost, and toxicity level as the criteria. Using six criteria containing creep strength, resistance to oxidation, thermal expansion coefficient, yield strength, limit strain, and toughness against five alternatives, Zindani
& ­Kumar[57] designed a PROMETHEE-GAIA method to find the best material suitable for the labyrinth seal
strips. Exconde et al.[58] focused on the selection of materials for use in 3D printer filaments using ELECTRE
method. Singh et al.[55] employed a hybrid ELECTRE II-entropy model for selecting natural fibers for use in brake
friction composites. The results revealed that 10 wt% banana fiber emerged as the best alternative among all
fibers that were considered. Mahajan et al.[48] investigated the selection process of natural fibers for sustainable
composites. They proposed a hybrid MCDM model that utilized the Entropy and CRITIC methods to calculate the criteria weights, and the PROMETHEE II, TOPSIS, and VIKOR methods to rank the materials under
consideration. Bhaskar and ­Khan[1] evaluated seven materials based on ten material selection criteria to identify
the best polymer-based biomaterial for dental applications using ELECTRE, PROMTHEE, VIKOR, TOPSIS,
and MOORA methods. Ranjith and Vimalkumar (2022) developed a hybrid MCDM method that integrated
ELECTRE and MOORA methods for selecting the best electrode material from five available alternatives for
electrical discharge machining of magnesium composites. Kirişci et al.[59] extended the ELECTRE I model to
the Fermatean fuzzy ELECTRE I model for group decision-making using Fermatean fuzzy human assessments
for material selection of the femoral component of the hip joint prosthesis. ­Zhou[60] adopted ELECTRE method
to select an optimal recycled material for 3D printer filament from a waste plastic stream containing a mixture


-----

of polymers. The results indicated that recycled polyethylene terephthalate outperformed all other considered
plastic materials.

Material selection using compromise ranking methods. The literature suggests that GRA and VIKOR are the
most widely used compromise ranking methods for material selection applications. Jayakrishna and ­Vinodh[61]
proposed an integrated approach that employed GRA to rank materials based on cost, material properties, and
environmental impact. Zhang et al.[62] used GRA in combination with other methods, such as DEMATEL, ANP,
and TOPSIS, to select the optimal green material for sustainable rubbish bins based on multiple criteria. Sanghvi et al.[63] adopted a combined framework of GRA and fuzzy logic to leverage the benefits of both methods for
bone staples material selection problem. Similarly, Wang & ­Li[64] employed GRA in conjunction with a hybrid
weighting method that integrated AHP, Fuzzy AHP, and quality function deployment (QFD) methods to solve
the lightweight automotive body material selection problem. Dwivedi & ­Sharma[65] applied an integrated entropyCoCoSo method to identify the most suitable sustainable material for an engineering application. Maidin et al.[66]
developed a systematic evaluation framework using GRA to rank natural fiber materials as reinforcement composites for cyclist helmets, with pineapple identified as the most suitable candidate for optimal safety. In another
study, Maidin et al.[67] applied 6 Sigma and GRA methods to select the most suitable thermoplastic matrix for
natural fiber composites in cyclist helmets, integrating qualitative and quantitative approaches to identify thermoplastic polyethylene as the ideal matrix.
Ishak et al.[68] applied fuzzy VIKOR method to select the optimal natural fiber type for fiber-reinforced composites to be utilized in the manufacture of a fiber-metal laminate for car front hoods. The objective of this
analysis was to achieve a reduction in transportation weight, which is crucial for improving fuel efficiency
and reducing environmental impact. Dev et al.[69] utilized an Entropy-VIKOR model to determine the optimal
composite material for an automobile piston application case study. Entropy method was applied to compute
the relative weights of various evaluation criteria, while VIKOR method was employed to rank the composite
materials under consideration. The approach ensured a comprehensive and objective evaluation of the available
alternative materials, leading to a well-informed decision regarding the most suitable composite material for the
intended application. Gadhave et al.[70] conducted a study on the selection of phase change material using three
MCDM methods and utilized AHP—entropy methods to determine the criteria weights. VIKOR, TOPSIS and
EXPROM2 methods were used to rank the alternative materials. The ranking was based on the compromised
weight obtained through AHP and entropy methods. Bhaskar & ­Khan[1] showcased the effectiveness of five different hybrid MCDM methods in identifying the optimal polymer-based biomaterial for use in dentistry. They
evaluated seven materials based on ten criteria and utilized AHP to determine criteria weights. The materials were
ranked using AHP-VIKOR, AHP-TOPSIS, AHP-MOORA, AHP-ELECTRE, and AHP-PROMTHEE methods.
Grachev et al.[45] developed a formalized method for selecting dental materials in the production of removable
dentures. Their approach combined AHP-Extended VIKOR method and involved analyzing interval quantitative estimations. Bhuiyan & ­Hammad[71] developed a decision support system to assist with selecting the most
sustainable structural material using a hybrid MCDM method that combined AHP, TOPSIS, and VIKOR in a
fuzzy environment.

Material selection using distance‑based methods. Applications of distance-based MCDM methods are well
popular in solving material selection problems. Xue et al.[72] introduced a new method based on interval-valued intuitionistic fuzzy sets and MABAC to address the issue of incomplete weight information in automotive
instrument panel material selection problems. Tian et al.[73] proposed a hybrid MCDM approach that combined
AHP and grey correlation TOPSIS (GC-TOPSIS) methods to select the optimal green decoration materials
from a pool of 10 different types of solid woods. Ahmed et al.[74] proposed a decision support framework taking
into account technical, environmental, social, and economic criteria for ranking concrete materials. The framework comprised of an optimal scoring method (OSM) that shortlisted the materials, followed determination
of ranking orders using AHP-TOPSIS method. Deshmukh & Angira.[75], used VIKOR and TOPSIS to solve the
material selection problem for radio-frequency microelectromechanical system (RF-MEMS) shunt capacitive
switches considering Young’s Modulus, Electrical resistivity, Thermal conductivity, Fracture strength as the criteria. Maghsoodi et al.[76] addressed a material selection problem in the context of dam construction projects by
proposing a hybrid decision-making approach that combined SWARA and CODAS methods. The proposed
approach considered target-based attributes to facilitate the evaluation process. Roy et al.[77] developed an evaluation framework for solving sustainable material selection problems in construction projects with incomplete
weight information. The approach extended CODAS method by incorporating interval-valued intuitionistic
fuzzy numbers. Yadav et al.[78] proposed a novel MCDM approach based on TOPSIS-PSI for choosing the best
alternative material in marine conditions. Dhanalakshmi et al.[79] employed a comprehensive MCDM-based
approach, combining Fuzzy AHP, TOPSIS, and EDAS methods, for the selection of pyrolysis materials. The
criteria were defined based on the objective of achieving maximum bio-oil yield during pyrolysis. Kar & ­Jha[80]
proposed a novel approach that integrates material management with construction schedule to prioritize construction materials using ANP-TOPSIS method. The criteria weights were determined using ANP, while TOPSIS
was used to calculate material criticality of the alternative materials. The result of the study showed that structural steel was the best material. Another hybrid method of VIKOR and TOPSIS could be found in Ref.[81], where
it is used to select the best dielectric material for RF-MEMS switches with low power consumption. Yang et al.[82]
developed a method for selecting an appropriate normalization method in TOPSIS when choosing the optimal
tribological coating material. They also introduced entropy-based and variation coefficient-based performance
scores to evaluate the effectiveness of the normalization method. Kumar et al.[83] applied TOPSIS method to
optimize the selection of glazing materials for solar thermal applications with multiple response characteristics.


-----

The study considered seven alternative materials and six criteria for material selection in the optimal design. The
results showed that Polysulfone material was the best choice for solar thermal applications. Aires & ­Ferreira[84]
developed a decision-making framework for selecting the most suitable thermal insulation material for enhancing energy efficiency, by integrating Fuzzy BWM, CRITIC, and Mixed Aggregation by Comprehensive Normalization Technique (MACONT). Among the considered alternatives, Polyisocyanurate was identified as the
optimal material based on the defined criteria. Abishini & ­Karthikeyan[85] investigated the use of AHP, TOPSIS,
EDAS, VIKOR, and Taguchi-based super ranking concepts to select the optimal aluminum alloy material for the
sheet metal forming process. The study revealed that AA2024 aluminum was the best-ranked material among
the alternatives considered. Kazemian et al.[86] conducted a comprehensive evaluation of ten different materials
used for intraoral stents in head and neck cancer patients. The study aimed to identify the most suitable material
using the TOPSIS method, and the results showed that Ethylene Vinyl Acetate was the best material. Sharma
et al.[87] investigated the optimal material selection problem for railway wagons using VIKOR, TOPSIS, PROMETTHEE, and WASPAS methods and also compared the relative performances. The study revealed aluminum
alloy Al 6005-T6 as the most suitable material. Remadi & ­Frikha[88] proposed a model for ranking green materials
using CODAS method and utilized intuitionistic fuzzy sets within an uncertain group decision-making environment. Wankhede et al.[89] focused on selection of natural fiber for long lasting composites using CODAS method.
Basalt was found as the best natural for long lasting composites followed by flax and Kenaf respectively. Ranking performance of CODAS was also compared with MOORA method. Table 3 summarizes the distance-based
studies which used the aforementioned methods. Based on the literature review as presented above, a number of
MCDM methods have been employed to solve material selection problems. This leads us to the next part of the
literature review, which focuses on the differences between the results of different MCDM methods. This section
poses the question: "Which MCDM method is most suitable for solving complex material selection problems
with a large number of alternatives and criteria?".

#### Dissimilarities in ranking results for material selection problems. This section discusses the application of various MCDM methods to the same material selection problems, which reveal that decision-makers
may have different rankings using different methods. For instance, Singh et al.[55] used ELECTRE II to select the
best material and compared the rankings derived using COPRAS, TOPSIS, VIKOR, SAW, MOORA, and PSI to
validate the outputs. While all the methods identified a similar alternative as the best, the rankings were slightly
different. Similarly, Hafezalkotob & ­Hafezalkotob[91] compared the rankings produced by Target-based MULTIMOORA method with two different modes and their aggregate ranking of with other methods including Targetbased TOPSIS, Target-based VIKOR and Interval target-based VIKOR methods. Despite generating different
rankings, all methods, except for Target-based MULTIMOORA with an integrated significant coefficient (Mode
2), suggested the same material for the considered problem. However, the aggregate ranking methodology proposed two materials as the best. To analyze the similarity of MCDM outputs, Spearman rank correlation coefficient was also used which revealed differences in the obtained rankings. Mousavi-Nasab & Sotoudeh-Anvari[92]
presented five material selection examples and compared the rankings using DEA, VIKOR, TOPSIS, ELECTRE
II, and COPRAS methods. In the first example, a significant difference in material ranking between DEA and
other methods was observed, while in the second example, the results were more similar. Although the same
material was selected by most methods, the rankings of the remaining materials varied significantly. The authors
also concluded that for material selection problems, it is more reliable to use multiple MCDM methods instead

**Case application** **Distance-based MCDM method**

Automotive instrument panel Interval-valued intuitionistic fuzzy MABAC

Building decoration material selection (Solid wood) Grey correlation-TOPSIS

Ranking concrete supplementary material TOPSIS

Material selection problem for the bridge of RF-MEMS shunt capacitive switches TOPSIS

Dam construction material selection CODAS

Sustainable material selection in construction projects Interval-valued intuitionistic fuzzy CODAS

Material selection in marine applications TOPSIS-PSI

Bone transplant replacement material selection TOPSIS

Pyrolysis material selection TOPSIS and EDAS

Construction material selection TOPSIS

Tribological coating material selection TOPSIS

Glazing material for solar thermal application TOPSIS

Flywheel material selection R-TOPSIS

[85] Aluminum alloy material selection for sheet metal forming process EDAS

Material selection of intraoral stents TOPSIS

Lightweight material for railway vehicles TOPSIS

Green material selection Intuitionistic fuzzy CODAS

Selection of natural fiber for long lasting composites CODAS

**Table 3. Distance-based MCDM methods in materials selection.**

|Author|Case application|Distance-based MCDM method|
|---|---|---|
|Xue et al.72|Automotive instrument panel|Interval-valued intuitionistic fuzzy MABAC|
|Tian et al.73|Building decoration material selection (Solid wood)|Grey correlation-TOPSIS|
|Ahmed et al.74|Ranking concrete supplementary material|TOPSIS|
|Deshmukh & ­Angira75|Material selection problem for the bridge of RF-MEMS shunt capacitive switches|TOPSIS|
|Maghsoodi et al.76|Dam construction material selection|CODAS|
|Roy et al.77|Sustainable material selection in construction projects|Interval-valued intuitionistic fuzzy CODAS|
|Yadav et al.78|Material selection in marine applications|TOPSIS-PSI|
|Zhang et al.90|Bone transplant replacement material selection|TOPSIS|
|Dhanalakshmi et al.79|Pyrolysis material selection|TOPSIS and EDAS|
|Kar & ­Jha80|Construction material selection|TOPSIS|
|Yang et al.82|Tribological coating material selection|TOPSIS|
|Kumar et al.83|Glazing material for solar thermal application|TOPSIS|
|Aires & ­Ferreira84|Flywheel material selection|R-TOPSIS|
|Abishini & ­Karthikeyan85|Aluminum alloy material selection for sheet metal forming process|EDAS|
|Kazemian et al.86|Material selection of intraoral stents|TOPSIS|
|Sharma et al.87|Lightweight material for railway vehicles|TOPSIS|
|Remadi & ­Frikha88|Green material selection|Intuitionistic fuzzy CODAS|
|Wankhede et al.89|Selection of natural fbier for long lasting composites|CODAS|


-----

of relying on a single technique. In example 3, differences were observed in the generated rankings and the
selected materials. Similarly, the application of MCDM methods in the subsequent two examples demonstrated
different ranking results and slight differences in the selected materials. The authors concluded that TOPSIS and
COPRAS are more consistent, but using multiple MCDM methods to solve material selection problems is preferable. Another attempt to optimize decision-making in material selection problems can be found in the work of
Zhang et al.[93][,] where they proposed a new MCDM method. It was evident that changes in methods for computing a component of the decision-making process, such as criteria weights, could significantly impact the final
results. Fuzzy BWM and fuzzy G-VIKOR methods were employed by Zhang et al.[94] to solve a material selection
problem. To validate the results, a sensitivity analysis was conducted to explore the influence of criteria weights
on the final ranking. ­In[54] study, a sustainable building material selection problem was solved using ELECTRE
III. The results obtained from ELECTRE III were compared with SAW, TOPSIS, COPRAS, and MULTIMOORA.
Additionally, sensitivity analysis was performed to demonstrate the superior performance of ELECTRE III compared to other MCDM methods. Consequently, if other MCDM methods are utilized by DMs for any reason,
a poor material selection result might have been obtained. Another significant difference between the rankings of materials generated by different MCDM methods is highlighted in the work conducted by Chatterjee
et al.[95]. COPRAS and EVAMIX methods were employed for solving material selection problems, and the results
obtained from these methods were compared with TOPSIS, VIKOR, and AHP in terms of calculation time,
simplicity, transparency, possibility of graphical interpretation, and information type, instead of using sensitivity
analysis or Spearman’s rank correlation coefficient. Through two examples, it was concluded that COPRAS and
EVAMIX methods are applicable, capable, and accurate for solving material selection problems.

### Research methodology
The research methodology is constructed on three main procedures, 1. Computing the criteria weights; 2. Selecting the best material; and 3. Validating the obtained results. The methodological process and the tools used in
this paper are shown in Fig. 2.

**Computing the**
**Material selection** **Validation**
**criteria weights**

End

Group decision- Determining each Performance Measuring similarity
making alternative’s rank analysis with other MCDM

against each criterion methods

Zakeri
Compromise

Konstantas

decision Performance

Identifying the index Correlation
Vital, Immaterial Coefficient

Ranking the materials

and Mediocre
criteria

Dependency Manhattan
analysis distance

Selecting the best

Computing the Rank Canberra

material

criteria weights reversal distance
using VIMM paradox

Chi-square
distance

Squared
Euclidean
distance

Total
similarity

**Fi** **2** Th th d l i l kfl

|Material selection|Col2|Validation|
|---|---|---|


-----

#### Research tools. This section presents two main tools used to solve the material selection problem. It is
divided into two sub-sections that address the issues mentioned previously. The first sub-section presents the
new MCDM method called SRP. The second sub-section presents VIMM, which is a subjective weighting
method used in the first scenario algorithm.

_SRP._ SRP method is a novel approach developed to solve MCDM problems. It is based on the ranks of alternatives in each criterion, which allows it to provide accurate and reliable outputs while avoiding the complexities
of existing MCDM methods. Unlike other methods, SRP does not require a normalization process as it directly
works with criteria weights. SRP has the following simple steps:
_Step 1 Defining criteria for the evaluation of the alternatives where Ai signifies the alternatives, cj states the_
criteria, and i = {1, . . ., m} and j = {1, . . ., n}.
_Step 2 Establishing the decision matrix, where Xij denote the decision matrix and rij expresses the score of_

i th alternative against j th criterion.

Xij = rij. (1)

_Step 3 Determining the ranks of alternatives in each criterion where the ranking process is based on the higher_
value of rij in the beneficial criteria ( max
1≤i≤m[r][ij][ ) and lower value of ][r][ij][ in the non-beneficial criteria ( ]′ 1[min]≤i≤m[r][ij][ ). The ]
following equation Eq. (2) demonstrates the new ranking matrix where Xij[ is the ranking matrix and ][R]i[j][ is the ]

rank of i th alternative against j th criterion.

′
Xij [=][ R]i[j][,] (2)

_Step 4 The fourth step is the construction of the weighted ranking matrix according to Eq. (3), where Wj stands_
for the importance wrights of criteria and Xij["][ shows the weighted ranking matrix.]

Xij["] [=][ W][j][R]i[j][,] (3)

_Step 5 Computing the total ranking score of the alternatives as follows:_


n

SRi = � WjR[j]i[,] (4)

j=1

_Step 6 Finally, prioritizing alternatives based on the higher value of Ri, where m is the number of alternatives._

Ri = m − SRi. (5)

_VIMM: first scenario algorithm._ VIMM is a subjective weighting method that is developed to use less pairwise comparison and also distance-based computations to extract the most accurate weights from the decisionmakers’ opinions and judgments. VIMM is designed based on three main elements called vital, immaterial, and
mediocre criteria. The vital criterion plays the role of the most important criterion, which has the most impact in
achieving the decision-making’s goal(s). It receives the highest value through computation. On the other hand,
the immaterial criterion plays the opposite role and has the lowest impact on reaching the goal(s). The first vital
and immaterial criteria select by the decision-maker(s), while the algorithm determines the following vital and
immaterial criteria. There exists a third criterion, called the mediocre criterion. It refers to a criterion that affects
reaching the decision-making goal to a lesser extent than the vital criteria and higher than the immaterial criterion. VIMM generates high-accuracy results and is more reliable than the popular MCDM weighting methods
such as AHP.
The following phases are proposed by Zakeri et al.[9] for the classic VIMM: the first scenario to calculate the
weights of criteria in a one-goal decision-making problem.
_Step 1 The algorithm begins with determining the vital, immaterial, and mediocre criteria by the_
decision-makers.
_Step 2 After selecting the vital and immaterial criteria, the second step is to allocate five and one as the cor-_
responding values for the vital and immaterial criteria, respectively.
_Step 3 Comparing the remaining criteria against the vital and immaterial criteria following the numerical-_
linguistic scale. To conduct the comparison, VIMM uses a scale to convert decision-makers’ subjective opinions


2 5 9


Less Equal More

importance importance importance

**Figure 3. The linguistic/numeric variables scale.**


-----

into numbers within an interval of [2, 5, 9], in which decision-maker is able to select any rational number between
these three numbers. The scale is illustrated in Fig. 3.
_Step 4 Establishing the distance matrix by calculating the distances between each criterion and the vital and_
immaterial criteria according to the linguistic/numeric scale in (Fig. 2) is the fourth step of the VIMM algorithm.
This step includes two steps:
_Step 4.1 Normalizing the distance matrix by following Eqs. (6), (7), where dxy[+][ and ][d]xy[−][ stand for distances ]_
between the y th criterion in the x th comparison, and the immaterial and vital criteria respectively, x states the
number of comparison process, and y stands for the number of criteria.

′

dxy[+] = cy/max xy [,][ y][ ∈] [j][,] (6)

y∈j [d][+]


′

dxy[−] = miny∈j [d]xy[−] /dxy[−] [,][ y][ ∈] [j][,] (7)


_Step 4.2 Computing the first score Eq. (8), where Sxy denotes the score of the_ y th criterion in the x th
comparison.

′ ′

Sxy = dxy[+] + dxy[−] . (8)


_Phase 5 Re-executing steps 3 and 4 until the number of remaining criteria reaches 2 for an even number of_
criteria or 1 for an odd number of criteria.
_Phase 6 Computing the weights of criteria according to Eqs. (9), (10), where ( [�][n]j=1_ [W][j][ =][ 1][)]

x

Sj = � Sxy, (9)

y∈j


y

Wj = � Sjy ∈ j. (10)

j=1

### Material selection via SRP and VIMM: the first scenario methods
This section is divided into four sub-sections. In this first sub-section, the case study and the information on
the materials, their properties, and the weights of the criteria for the evaluation of the materials are represented.
In the second section, a group decision-making process conducted by seven experts is represented to select the
vital and material criteria as the input for the VIMM method. VIMM method is applied to the case to compute
the weights of criteria in the third section. The evaluation process of the material is represented in the fourth
sub-section, in which the SRP method is applied to select the best material.

#### Case study. A case ­study[96] has been adopted in this paper to select the best phase change material to be used
to store solar energy. Criteria taken in consideration are Latent Heat J/Kg (c1), Density Kg/m3 (c2), Specific Heat
kJ/kg K (c3), Specific Heat kJ/kg K (c4), Thermal Conductivity W/m K (c5) and Cost (c6) . Among all the criterion Latent Heat, Density, Specific Heat (solid), Specific Heat (liquid) and Thermal Conductivity are beneficial
criterion i.e. higher the value better the alternative. Cost is non-beneficial criterion i.e. lower the value better the
alternative. Nine alternatives are considered as the phase change material such as Calcium chloride hexa-hydrate
(A1), Stearic acid (A2), p116 (A3), RT 60 (A4), Paraffin wax RT 30 (A5), n-Docosane (A6), n-Octadecane (A7),
n-Nonadecane (A8) and n-Eicosane (A9). The information on the properties of the materials and the material

**Material selection criteria**

**Specific heat kJ/kg K** **Specific heat kJ/kg K** **Thermal conductivity W/m**

(c1) **Density Kg/m[3]** (c2) **(Cp(s))(c3)** **(Cp(l))(c4)** **K (c5)** **Cost (c6)**

1560.0 1.4600 2.1300 1.0900 Very low

903.00 2.8300 2.3800 0.1800 Very high

830.00 2.1000 2.1000 0.2100 Low

850.00 0.9000 0.9000 0.2000 Very low

789.00 1.8000 2.4000 0.1800 Low

785.00 1.9300 2.3800 0.2200 Low

773.22 0.3767 2.2670 0.1400 Low

775.80 1.7189 1.9210 0.1420 High

776.33 0.7467 2.3770 0.1380 Low

**Table 4. Properties of PCMs for solar energy devices.**

|Phase change material (PCM)|Material selection criteria|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||Latent heat J/Kg (c1)|Density Kg/m3 (c2)|Specific heat kJ/kg K (Cp(s))(c3)|Specific heat kJ/kg K (Cp(l))(c4)|Thermal conductivity W/m K (c5)|Cost (c6)|
|Calcium chloride hexahy- drate (A1)|169.98|1560.0|1.4600|2.1300|1.0900|Very low|
|Stearic acid (A2)|186.50|903.00|2.8300|2.3800|0.1800|Very high|
|p116 (A3)|190.00|830.00|2.1000|2.1000|0.2100|Low|
|RT 60 (A4)|214.40|850.00|0.9000|0.9000|0.2000|Very low|
|Paraffin wax RT 30 (A5)|206.00|789.00|1.8000|2.4000|0.1800|Low|
|n-Docosane (A6)|194.60|785.00|1.9300|2.3800|0.2200|Low|
|n-Octadecane (A7)|245.00|773.22|0.3767|2.2670|0.1400|Low|
|n-Nonadecane (A8)|222.00|775.80|1.7189|1.9210|0.1420|High|
|n-Eicosane (A9)|247.00|776.33|0.7467|2.3770|0.1380|Low|


-----

|PCM|Material selection criteria|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||c1|c2|c3|c4|c5|c6|
|A1|169.98|1560.0|1.4600|2.1300|1.0900|0.2550|
|A2|186.50|903.00|2.8300|2.3800|0.1800|0.7450|
|A3|190.00|830.00|2.1000|2.1000|0.2100|0.3350|
|A4|214.40|850.00|0.9000|0.9000|0.2000|0.2550|
|A5|206.00|789.00|1.8000|2.4000|0.1800|0.3350|
|A6|194.60|785.00|1.9300|2.3800|0.2200|0.3350|
|A7|245.00|773.22|0.3767|2.2670|0.1400|0.3350|
|A8|222.00|775.80|1.7189|1.9210|0.1420|0.6650|
|A9|247.00|776.33|0.7467|2.3770|0.1380|0.3350|


**Table 5. Material selection decision matrix.**

**Criteria** **c1** **c2** **c3** **c4** **c5** **c6**

Weight 0.4901 0.1674 0.0528 0.0528 0.2109 0.0261

**Table 6. Criteria weights for the considered material selection case study.**

selection’s decision matrix, including the materials and the criteria for the evaluation, is demonstrated in Tables 4
and 5 respectively. The weights of the criteria are also illustrated in Table 6.

#### The group decision‑making process. In this section, in order to determine the vital and immaterial criteria as the main elements of VIMM algorithm, seven experts are employed to re-evaluate the material selection
criteria weights. The original criteria weights are exhibited in Table 6.
The number of pairwise comparisons in VIMM for the even number of criteria is (n/2), where n is the number
of criteria. Therefore, in this case, there are two comparison processes. The seven experts are asked to select three
criteria as the vital and immaterial criterion for each comparison based on the criteria priority of being the best
choice to meet the properties of the vital or immaterial criteria. Table 7 demonstrates expert responses, where
Z[y]αx[ and ][Z][y]βx[ represent different choice of decision-makers in the selection of vital and immaterial criteria in each ]
comparison, y shows the priority of the selected criterion, x indicates the number of comparison process, N is
the set of natural numbers, and ψZ[y]αx[ and ][ψ][Z][y]βx[ are the cardinal numbers, representing the frequency of the criteria ]

that decision-makers selected as the vital and immaterial criteria respectively see Eqs. (11) and (12).

|Criteria|c1|c2|c3|c4|c5|c6|
|---|---|---|---|---|---|---|
|Weight|0.4901|0.1674|0.0528|0.0528|0.2109|0.0261|


ψZ1αx ≤ ψZ2αx ≤ ψZ3αx, 1 ≤ y ≤ 3, y ∈ N, x = n/2, (n − 1)/2, n ∈ j, (11)

ψZ1βx [≤] [ψ][Z]β[2]x [≤] [ψ][Z]β[3]x [, 1][ ≤] [y][ ≤] [3,][ y][ ∈] [N][,][ x][ =][ n][/][2,][ (][n][ −] [1][)/][2,][ n][ ∈] [j][.] (12)

Table 8 shows the response distribution, where Fcj denotes the frequency of the criterion in each choice for
the selection of the vital and immaterial criterion in the comparison processes. According to the distribution
of responses of DMs (Table 8), the vital and immaterial selected by DMs criteria are shown in Tables 9 and 10.

α1 β1 α2 β2

**Expert** Z[1]α1 Z[2]α1 Z[3]α1 Z[1]β1 Z[2]β1 Z[3]β1 Z[1]α2 Z[2]α2 Z[3]α2 Z[1]β2 Z[2]β2 Z[3]β2

1 c1 c1 c1 c6 c6 c6 c5 c2 c2 c4 c4 c3

2 c1 c1 c5 c6 c3 c4 c5 c5 c2 c3 c4 c6

3 c5 c5 c1 c4 c6 c6 c1 c2 c5 c6 c4 c4

4 c1 c1 c2 c3 c6 c4 c2 c5 c5 c6 c4 c3

5 c1 c5 c2 c6 c6 c6 c1 c5 c5 c3 c4 c4

6 c1 c1 c5 c6 c6 c3 c5 c5 c5 c3 c3 c6

7 c1 c1 c1 c4 c6 c6 c5 c5 c5 c4 c3 c6

**Table 7. Responses of decision-makers for selection of vital and immaterial criteria in the two comparison**
processes.

|Col1|α1|Col3|Col4|β1|Col6|Col7|α2|Col9|Col10|β2|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Expert|Z1 α1|Z2 α1|Z3 α1|Z1 β1|Z2 β1|Z3 β1|Z1 α2|Z2 α2|Z3 α2|Z1 β2|Z2 β2|Z3 β2|
|1|c1|c1|c1|c6|c6|c6|c5|c2|c2|c4|c4|c3|
|2|c1|c1|c5|c6|c3|c4|c5|c5|c2|c3|c4|c6|
|3|c5|c5|c1|c4|c6|c6|c1|c2|c5|c6|c4|c4|
|4|c1|c1|c2|c3|c6|c4|c2|c5|c5|c6|c4|c3|
|5|c1|c5|c2|c6|c6|c6|c1|c5|c5|c3|c4|c4|
|6|c1|c1|c5|c6|c6|c3|c5|c5|c5|c3|c3|c6|
|7|c1|c1|c1|c4|c6|c6|c5|c5|c5|c4|c3|c6|


-----

|Criteria|Fcj|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||ψ Z1 α1|ψ Z2 α1|ψ Z3 α1|ψ Z1 β1|ψ Z2 β1|ψ Z3 β1|ψ Z1 α2|ψ Z2 α2|ψ Z3 α2|ψ Z1 β2|ψ Z2 β2|ψ Z3 β2|
|c1|6|5|3|0|0|0|2|0|0|0|0|0|
|c2|0|0|2|0|0|0|1|2|2|0|0|0|
|c3|0|0|0|1|1|1|0|0|0|3|2|2|
|c4|0|0|0|2|0|2|0|0|0|2|5|2|
|c5|1|2|2|0|0|0|4|5|5|0|0|0|
|c6|0|0|0|4|6|4|0|0|0|2|0|3|


**Table 8. Distribution of decision-makers’ responses.**

**Criteria** ψZ1α1 ψZ2α1 ψZ3α1 ψZ1α2 ψZ2α2 ψZ3α2

c1 6 5 3 2 0 0

c2 0 0 2 1 2 2

c3 0 0 0 0 0 0

c4 0 0 0 0 0 0

c5 1 2 2 4 5 5

c6 0 0 4 0 0 0

**Table 9. Distribution of decision-makers’ responses regarding the vital criterion.**

**Criteria** ψZ1β1 ψZ2β1 ψZ3β1 ψZ1β2 ψZ2β2 ψZ3β2

c1 0 0 0 0 0 0

c2 0 0 0 0 0 0

c3 1 1 1 3 2 2

c4 2 0 2 2 5 2

c5 0 0 0 0 0 0

c6 4 6 4 2 0 3

**Table 10. Distribution of decision-makers’ responses regarding the immaterial criterion.**

_Determining the vital and immaterial criteria._ The collected data in the previous section are evaluated in this
section to determine the vital and immaterial criteria. The evaluation comprises two steps as follows:
_Step 1 The first step of the evaluation process of decision-makers’ opinions is to compute the value of fre-_
quency of vital and immaterial criteria. The step is conducted using Eqs. (13), (14), (15), (16) and (17).

VF[α]cj[x] [=] �y ± ξ �ψZ1αx + ��y − 1� ± µ�ψZ2αx + ��y − 2� ± ν�ψZ3αx ; (13)

|Criteria|ψ Z1 α1|ψ Z2 α1|ψ Z3 α1|ψ Z1 α2|ψ Z2 α2|ψ Z3 α2|
|---|---|---|---|---|---|---|
|c1|6|5|3|2|0|0|
|c2|0|0|2|1|2|2|
|c3|0|0|0|0|0|0|
|c4|0|0|0|0|0|0|
|c5|1|2|2|4|5|5|
|c6|0|0|4|0|0|0|

|Criteria|ψ Z1 β1|ψ Z2 β1|ψ Z3 β1|ψ Z1 β2|ψ Z2 β2|ψ Z3 β2|
|---|---|---|---|---|---|---|
|c1|0|0|0|0|0|0|
|c2|0|0|0|0|0|0|
|c3|1|1|1|3|2|2|
|c4|2|0|2|2|5|2|
|c5|0|0|0|0|0|0|
|c6|4|6|4|2|0|3|


VF[β]cj[x] [=] �y ± ξ �ψZ1β1 [+] ��y − 1� ± µ�ψZ2β1 [+] ��y − 2� ± ν�ψZ3β1 [;] (14)

� 0 ≤ ξ ≤ y, y + ξ

ξ = 0 < ξ, y − ξ ; (15)


� 0 ≤ µ ≤ y, �y − 1� − µ

µ = y > µ + 1, �y − 1� − µ [;] (16)


� 0 ≤ ν ≤ y, �y − 2� + ν

ν = y > ν + 2, �y − 2� − ν [;] (17)

where the values of ξ, µ, and ν are determined by decision-makers.
_Step 2 The second step is to determine the vital and immaterial criteria in each comparison which is computed_
with the selection of the maximum value of Eqs. (13), (14), where.1max≤j≤6[V]F[α]cj[x][ and ]1[max]≤j≤6[V]F[β]cj[x][ are the vital and imma-]

terial in x th comparison.


-----

**Table 11. The vital criteria selection for two comparison processes based on expert opinions.**

**Table 12. The immaterial criteria selection for two comparison processes based on the experts’ opinion.**

In this case, we consider ξ, µ, ν = 0 for the selection of the immaterial and vital criteria. According to Eqs.
(13) and (14), results of the evaluation of the decision-makers’ opinions are demonstrated in Tables 11 and 12
where c1 (Latent Heat) is determined as the vital in the first comparison, and c5 (Thermal Conductivity) is determined as the second vital criterion in the second comparison. Criterion c6 (Cost) plays the immaterial criterion
role and c4 (Specific Heat) is selected by the experts to affect the criteria weighting process as the second immaterial criterion in the second comparison, as shown in Table 12 of the first comparison.

#### Computing weights of criteria. The prerequisite of VIMM algorithm is the goal definition, where if there
is one goal for the decision-making problem, the first scenario ought to be employed; otherwise, VIMM: the
second scenario must be used. This paper’s case follows one goal: selecting the most proper phase change material to store solar energy.
Since the weights were computed ­in[96] work, in contrast to the classic VIMM and instead of using the algorithm
for the computation of the vital and immaterial criteria, we relied on the experts’ opinions and the vital and
immaterial criteria in the second comparison are selected by them. In our case, there are no mediocre criteria
selected by decision-makers.
The first step of computing weights of criteria is to allocate 5 and 1 to the first selected vital and immaterial
criteria which are c1, the Latent Heat, and c6, the Cost, then:

c1 = 5

c6 = 1

The seven experts are asked to give their expert opinions to run the comparison. The first two comparisons
of the remaining criteria and the selected vital and immaterial are shown in Tables 13 and 14, where the scale as

**Criteria** **c2** **c3** **c4** **c5**

c1 6.166 3.882 3.827 7.053

**Table 13. Comparison of latent heat (vital criterion) with other criteria.**

|Criteria|c2|c3|c4|c5|
|---|---|---|---|---|
|c1|6.166|3.882|3.827|7.053|


-----

|Criteria|c2|c3|c4|c5|
|---|---|---|---|---|
|c6|6.414|2.126|2.023|8.080|


**Table 14. Comparison of cost (immaterial criterion) against other criteria.**

**Criteria** **d[+′]** **d[−′]**

c2 5.414 3.834

c3 1.126 6.118

c4 1.023 6.173

c5 7.080 2.947

Max 7.080

Min 6.173

**Table 15. Distances between the criteria and first vital and immaterial criteria.**

illustrated in Fig. 2 is used to conduct the comparison. The next phase is to compute the distances between all
criteria, and the vital and immaterial criteria are shown in Table 15, where d[+] stands for the distance between
the criteria and the immaterial criterion, while d[−] displays the distance between the criteria and the vital criterion. To display the computation of d[+] and d[−], the following examples are provided. The normalized distance
matrix, as shown in Table 16, is derived using Eqs. 6, and 7, where d[+′] and d[−′] indicate the normalized distances.

dDensity[+] [=][ 6.414][ −] [1]

dDensity[−] [=][ 10][ −] [6.166]

The next step is to compute the first criteria’ scores and identify the second vital and immaterial using the
VIMM algorithm’s “step no 4.2” and Eq. (8).
Similar to what have been selected by decision-makers (shown in Tables 11 and 12), as displayed in Table 17,
Specific Heat and Thermal Conductivity are calculated as the immaterial and vital criteria, respectively. In the
next step, the remaining criteria are compared with the second vital and immaterial criteria, the Thermal Conductivity and the Specific Heat. The comparisons are conducted by decision-makers as presented in Tables 16

**Criteria** **d[+]** **d[−]**

c2 0.765 1.610

c3 0.159 1.009

c4 0.144 1.000

c5 1.000 2.095

**Table 16. Normalized distance matrix.**

**Table 17. The first scores, and the second vital and immaterial criteria.**

**Criteria** **c2** **c3**

c5 0.1674 0.0555

**Table 18. Comparison of the vital criterion c5(thermal conductivity) with the remaining criteria.**

|Criteria|d+′|d−′|
|---|---|---|
|c2|5.414|3.834|
|c3|1.126|6.118|
|c4|1.023|6.173|
|c5|7.080|2.947|
|Max|7.080||
|Min||6.173|

|Criteria|d+|d−|
|---|---|---|
|c2|0.765|1.610|
|c3|0.159|1.009|
|c4|0.144|1.000|
|c5|1.000|2.095|

|Criteria|c2|c3|
|---|---|---|
|c5|0.1674|0.0555|


-----

|Criteria|c2|c3|
|---|---|---|
|c4|0.1674|0.0555|


**Table 19. Comparison of the immaterial criterion, c4(specific heat, (Cp(l)), against the remaining criteria.**

Criteria + − +′ −′

2 2.170 2.063 1 1 2.000

3 0.051 7.368 0.024 0.280 0.303

**Max** 2.170

**Min** 2.063

**Table 20. Normalized distance matrix and second scores of criteria.**

|Criteria|+|−|+′|−′|Col6|
|---|---|---|---|---|---|
|2|2.170|2.063|1|1|2.000|
|3|0.051|7.368|0.024|0.280|0.303|
|Max|2.170|||||
|Min||2.063||||


The vital criterion
extracted from 2

|Criteria|1|2|3|Col5|Col6|Vital|Immaterial|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|1|5|5|5|||||The vi extrac||
|2|2.374|2.000|5|||||||
|||||||||||
|3|1.168|0.303|1|||||||
|4|1.144|1|0|||||||
|5|3.095|5|5|||||||
|6|1|0|0|||||||


**Table 21. Final comparison process. Significant values are in bold.**

**Table 22. Derived criteria weights.**

and 17, and the corresponding scores are given in Tables 18 and 19, and the normalized distance matrix is
illustrated in Table 20.
The final phase is the computation of the weights, which are extracted from the scores. To do that, first, the
scores need to be calculated. The final comparison is shown in (Table 21) in which Density is the final vital
criterion and the Specific Heat (Cp(s)) is the last immaterial criterion. The scoring continues until all criteria
received their final 5 and 1 values. The allocation of value to the vital criteria continues to the last comparison,
while the immaterial criteria receive merely one time their corresponding value. The criteria weights as derived
using Eqs. (9) and (10) are the displayed in Table 22.


-----

|Wj|0.348|0.218|0.057|0.050|0.304|0.023|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PCM|c1|c2|c3|c4|c5|c6|c1|c2|c3|c4|c5|c6|
|A1|9|1|6|5|1|1|3.132|0.218|0.342|0.25|0.304|0.023|
|A2|8|2|1|2|5|5|2.784|0.436|0.057|0.1|1.52|0.115|
|A3|7|4|2|6|3|2|2.436|0.872|0.114|0.3|0.912|0.046|
|A4|4|3|7|8|4|1|1.392|0.654|0.399|0.4|1.216|0.023|
|A5|5|5|4|1|5|2|1.74|1.09|0.228|0.05|1.52|0.046|
|A6|6|6|3|2|2|2|2.088|1.308|0.171|0.1|0.608|0.046|
|A7|2|9|9|4|7|2|0.696|1.962|0.513|0.2|2.128|0.046|
|A8|3|8|5|7|6|4|1.044|1.744|0.285|0.35|1.824|0.092|
|A9|1|7|8|3|8|3|0.348|1.526|0.456|0.15|2.432|0.069|


**Table 23. Weighted ranking matrix using group decision-making and VIMM: the first scenario.**

**PCM** **SRi** Ri **Rank by SRP**

A1 4.269 4.731 2

A2 5.012 3.988 7

A3 4.68 4.32 5

A4 4.084 4.916 1

A5 4.674 4.326 4

A6 4.321 4.679 3

A7 5.545 3.455 9

A8 5.339 3.661 8

A9 4.981 4.019 6

**Table 24. Total ranking scores of materials along with derived ranking.**

#### Ranking materials. The final step in evaluating the materials is to derive the ranking orders of the alternatives using SRP which is based on ranking each alternative in relation to each criterion. The weighted ranking
matrix, obtained from the material evaluation decision matrix of Table 5 using Eqs. (2) and (3), is shown in
Table 23. The ranking order, as presented in Table 24, is determined using the total ranking scores of the alternatives, calculated in the fifth stage of SRP method using Eq. (4). The ranks of the materials are finally shown in
the same table employing Eq. (6) which indicates RT 60 (A4) as the best material to choose for the considered
application.

### Discussion
This paper introduced SRP to solve material selection problems. In this new method, the importance weights
of criteria play the leading role in evaluating the decision-making problems’ alternatives. Since the new method
algorithm’s process is mainly grounded on the ranks of each alternative against each criterion, it heavily relies
on the weights of each criterion.
SRP is applied to a material selection problem to evaluate a set of materials used to store solar energy.
Although the criteria weights have already been determined by Rathod and ­Kanzaria[96], yet we asked seven
experts to re-evaluate the criteria. VIMM, a reliable MCDM subjective weighting method, is used for extracting
opinions of the decision-makers. The original criteria weights, as determined by Rathod and ­Kanzaria[96], are also
utilized to compare the differences between the produced results in order to show how sensitive the SRP is to
the criteria weights (see Table 25).
The difference between the two rankings is illustrated in Fig. 4. To better understand the sensitivity of SRP
to criteria weights, different weight sets computed by two most popular MCDM objective weighting methods
namely Shannon’s entropy and CRITIC are considered here. The set of weights computed by Entropy and CRITIC
methods are as follows:

Wj[entropy] = {0.012, 0.050, 0.194, 0.046, 0.571, 0.128},

Wj[CRITIC] = {0.227, 0.134, 0.176, 0.151, 0.131, 0.180}.

Figure 5 shows considerable differences between the ranks of the results affected by distinctive weights
derived by different MCDM weighting methods, including objective and subjective approaches. This figure also
demonstrates high sensitivity of SRP to criteria weighting. Reliability of SRP is directly related to the reliability

|PCM|SRi|R i|Rank by SRP|
|---|---|---|---|
|A1|4.269|4.731|2|
|A2|5.012|3.988|7|
|A3|4.68|4.32|5|
|A4|4.084|4.916|1|
|A5|4.674|4.326|4|
|A6|4.321|4.679|3|
|A7|5.545|3.455|9|
|A8|5.339|3.661|8|
|A9|4.981|4.019|6|


-----

|Wj|0.4901|0.1674|0.0528|0.0528|0.2109|0.0261|SRP calculations|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|PCM|c1|c2|c3|c4|c5|c6|SRi|R i|Ranking|
|A1|9|1|6|5|1|1|5.3961|3.6039|9|
|A2|8|2|1|2|5|5|5.599|3.401|8|
|A3|7|4|2|6|3|2|5.2076|3.7924|7|
|A4|4|3|7|8|4|1|4.1243|4.8757|2|
|A5|5|5|4|1|5|2|4.6582|4.3418|3|
|A6|6|6|3|2|2|2|4.683|4.317|4|
|A7|2|9|9|4|7|2|4.7017|4.2983|5|
|A8|3|8|5|7|6|4|4.8129|4.1871|6|
|A9|1|7|8|3|8|3|4.0082|4.9918|1|


**Table 25. New ranking orders obtained using the original weights, estimated by Rathod and ­Kanzaria[96].**

10

8
6
4
2
0

0 1 2 3 4 5 6 7 8 9 10

Ranking with VIMM weights Ranking with original weights

**Figure 4. Comparative analysis of rankings affected by the criteria weights computed by the VIMM method**
and the original criteria weights.

10

5

0

0 1 2 3 4 5 6 7 8 9 10

Ranking with the VIMM weights Ranking with the original weights

Ranking with the CRITIC weights Ranking with the Entropy weights

**Figure 5. Comparative analysis of rankings affected by different weights computed by VIMM, CRITIC,**
Entropy, and original methods.

of weighting method used to assess the criteria under investigation. In this paper, VIMM method is used as a
subjective weighting tool to derive criteria weights from decision-makers’ opinions. This goal-oriented MCDM
weighting method is more reliable than classic forms of BWM and AHP. According to Zakeri et al.[9], there are
three main advantages of VIMM over the mentioned weighting methods including fewer number pairwise comparison, where n(n − 1)/2 and 2n − 3 number of comparisons are required for AHP and BWM respectively, while
VIMM needs merely (n − 1)/2 and n/2 number of comparisons for even and odd numbers of criteria in the evaluation process. In contrast to AHP method, VIMM is not limited to the number of criteria since it re-evaluates the
criteria in every process. VIMM is designed to consider the decision-making goal(s) by proposing two scenarios,
where the first scenario is developed to evaluate the weights of criteria in a decision-making problem with one
goal, and the second scenario is developed to consider more than one goal in its process of the computation
of the criteria weights. Thus, it is a proper pair for SRP in ranking alternatives to a decision-making problem.
Four MCDM methods, including WPM, VIKOR, and TOPSIS have also been applied to compare the results
obtained from SRP. The difference between rankings is pictured in Fig. 6.
Figure 6 demonstrates that there is no compromise in ranking among the four methods. Thus, the comparison
of MCDM results in the previous section cannot be used to validate the findings, leading to the next section.

#### The compromise decision index (CDI). In complex MCDM problems with several alternatives and criteria, irregularity in the result of comparing the generated rankings is inevitable. As shown in the previous


-----

10


0 1 2 3 4 5 6 7 8 9 10

TOPSIS WPM VIKOR SRP

**Figure 6. Comparison between rankings generated by four MCDM methods.**

section, there is an irregularity in the rankings generated by the MCDM methods; therefore, for these types of
situations, we have proposed an index called CDI to interpret the comparison between the outputs of MCDM
methods in the processes that at least four MCDM methods are applied to solve an MCDM problem ( K ≥ 4 ),
where K denotes the number of MCDM methods, the number of alternatives equals m ≥ 2K, and the number
of criteria equals n ≥ (2k − 2), which is the limitation of AHP in the evaluation of criteria where it is restricted
to seven (+ ⁄– 2) ­criteria[9].
The following steps shows the computation process of CDI.
_Step 1 Computing the performance of each alternative in accordance with Eqs. (18) and (19) respectively,_
where δi is the performance of i th alternative, ζR denotes weight of each rank, R stands for each rank, and Ai
states the i th alternative.

δi = ζRi FA[R]i[i] [,][ i][ = {][1, 2,][ . . .][,][ m][}][,][ F]A[R]i[i] [≤] [K,] (18)


ζRi = �� ζRi �−1(m − Ri + 1), (19)

_Step 2 Ranking alternatives according to the higher value of δi._
_Step 3 Calculating the deviation of each ranking fashioned by each MCDM method to the performance of_
alternative, according to (Eq. (20)).


σi = �����z �Xi − Yi[K] �2, K = {1, .., z}, i = {1, . . ., m}, (20)

K=1


_Step 4 The final step is the computation of CDI values using Eq. (21)._

m

CDI = 1/100 � σi. (21)

i=1

_CDI puts the results of MCDM methods in four types of compromises: Pragmatic compromise, Rational com-_
promise, Fair compromise, and Rotten compromise. The results are interpreted concerning these compromises
according to the defined categories provided by ­Wendt[97].

_The pragmatic compromise._ When there is a pragmatic reason for compromise, the pragmatic compromise
makes. When CDI shows the ranks have pragmatic compromise, results of the MCDM method are considered
to be reliable.

_The rational compromise._ According to Wendt.[97], a compromise is rational when it is rational for all parties to
agree on the compromise. When CDI interprets the comparison of ranks as the rational compromise, ranking
produced by the MCDM method is reliable to some extent. However, it is better to add another MCDM method
to reach a pragmatic compromise.

_The fair compromise._ When a fair compromise is made in the comparison analysis, decision-makers could
decide whether to consider the compromise as a rational compromise or rely on the practical results.

_The rotten compromise._ According to Wendt.[97], the purpose of introducing the concept of a "rotten compromise" is to have a term that signifies compromises that are morally dubious or unethical. When CDI interprets
the results as a rotten compromise, it means that the results of MCDM methods cannot be validated theoretically, and practical results must be evaluated and validated.


-----

### 0 1

**Figure 7. Interpretation of the MCDM results comparison based on the CDI.**

Rank 2 Rank 3 Rank 4 Rank 5 Rank 6 Rank 7 Rank 8 Rank 9

**Figure 8. Distribution of each material rank according to the MCDM methods.**

To interpret the results in accordance with the categories, first the maximum deviation needs to be computed.
The minimum deviation equals to zero, where all the applied MCDM methods generated the same results. The
interpretation of the results is based on Fig. 7, where

CDI1 = max1≤i≤m[σ][i][/][4,] (22)

CDI2 = max1≤i≤m[σ][i][/][2,] (23)

CDI3 = max1≤i≤m[σ][i][.] (24)

To interpret the obtained results from the comparison between the MCDM results with CDI, the distribution
of the materials’ rankings generated by the four MCDM methods needs to be calculated (see Fig. 8). According
to Eqs. (18) and (19), performance of the materials is shown in Table 26. According to Eqs. (20), (21), CDI =
0.430705. According to Eqs. (22), (23), (24), the interpretation of CDI is the fair compromise (see Fig. 9), where

max
1≤i≤m[σ][i][ =][ 0.64][.]

CDI1 = 0.16

|Calcium chloride exahydrate|Col2|Col3|Calcium chloride xahydrate|Col5|p116|Col7|earic acid|Calcium chloride xahydrate|Col10|Col11|p116|earic acid|Col14|ctadecane|Col16|Col17|raffin wax RT 30|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|h||he n-Docosane Nonadecane n- n-Eicosane Rank 2|he|p116 n-Docosane n-Octadecane Rank 3||St acid Stearic wax 30 Paraffin RT wax 30 Paraffin RT Rank 4|St|p116 he||60 RT 60 RT n-Eicosane Rank 6||St||n-O||Pa n-Octadecane n-Octadecane n-Eicosane Rank 9|Pa|
|Calcium chloride hexahydrate|||n-Docosane||p116||Stearic acid|||||RT 60||n- Nonadecane|||n-Octadecane|
|Stearic acid|||n- Nonadecane||n-Docosane||Paraffin wax RT 30|Paraffin wax RT 30|||RT 60|n-Docosane||n- Nonadecane|||n-Octadecane|
|RT 60|||n-Eicosane||n-Octadecane||Paraffin wax RT 30|n-Docosane||||n-Eicosane||n- Nonadecane|||n-Eicosane|
|||||||||||||||||||


-----

|ζRi|R1|R2|R3|R4|R5|R6|R7|R8|R9|δi|Rank|
|---|---|---|---|---|---|---|---|---|---|---|---|
||0.200|0.178|0.156|0.133|0.111|0.089|0.067|0.044|0.022|||
|PCM|FR1 A1|FR2 A2|FR3 A3|FR4 A4|FR5 A5|FR6 A6|FR7 A7|FR8 A8|FR9 A9|||
|A1|2|1|0|0|1|0|0|0|0|0.689|1|
|A2|1|0|0|2|0|0|1|0|0|0.533|2|
|A3|0|0|2|0|1|1|0|0|0|0.511|3|
|A4|1|0|0|0|0|2|1|0|0|0.444|4|
|A5|0|0|0|2|1|0|0|0|1|0.400|5|
|A6|0|1|1|0|1|0|1|0|0|0.511|3|
|A7|0||1|0|0|0|0|1|2|0.244|8|
|A8|0|1|0|0|0|0|0|3|0|0.311|7|
|A9|0|1|0|0|0|1|1|0|1|0.356|6|


**Table 26. Performance of materials.**


_The Fair compromise_


### 0 1

|The Pragmatic compromise|The Rational compromise|Col3|Col4|The Rotten compromise|
|---|---|---|---|---|
|compromise|compromise|||compromise|
||||||


1 [= 0.16] 2 [= 0.32] 3 [= 0.64]

=


**Figure 9. The fair compromise of CDI for the material selection problem.**

n-Eicosane

n-Octadecane

Paraffin wax RT 30

p116

Calcium chloride hexahydrate

0 1 2 3 4 5 6 7 8 9 10

ARAS COPRAS AHP SRP with VIMM

**Figure 10. Ranking of alternative materials using different MCDM methods.**

CDI2 = 0.32

CDI3 = 0.64

#### The comparative rankings analysis ‑the performance analysis. Similar to SRP, AHP is also highly
sensitive to criteria weights. This section uses the Zakeri–Konstantas performance correlation coefficient and
the dependency analysis to evaluate the SRP performance. ARAS and COPRAS (see Goswami et al.[6] are also
added to the list for the similarity evaluation. The rankings generated by the mentioned methods are illustrated
in Fig. 10. The Zakeri-Konstantas performance correlation coefficient has been employed to execute the comparative performance analysis of the MCDM methods, and the dependency analysis is used to validate the new
MCDM method


-----

COPRAS

AHP

0.00 5.00 10.00 15.00 20.00 25.00 30.00 35.00 40.00

**Figure 11. Performance similarity evaluation of ARPAS, COPRAS, and AHP with SRP using Zakeri-**
Konstantas performance correlation coefficient.

_Zakeri‑Konstantas performance correlation coefficient._ Zakeri-Konstantas performance correlation coefficient
a new tool to evaluate the similarities of the outputs of the MCDM methods. Introduced ­by[98], Zakeri–Konstantas performance correlation coefficient is a new nonparametric measure of rank correlation that measures the
similarities between the rankings generated by different MCDM methods. In order to provide the similarity
degree of the two MCDM methods, the new coefficient computes each decision option’s performance based on
its corresponding rank in the data sets generated by the two MCDM methods. Equations (24) and (25) depict
the computation of similarity conducted by Zakeri-Konstantas performance correlation coefficient, where ZK
stands for the Zakeri-Konstantas performance correlation coefficient, N denotes the natural numbers, and Ri[l]
and Ri[h][ show the rank of ][i][ th alternative generated by ][l][ th MCDM algorithm and the rank of ][i][ th alternative gener-]
ated by h th MCDM algorithm respectively. Zakeri-Konstantas performance correlation coefficient is architected
on two main bases, 1. significance of each option using Eqs. (26),and (2). performance of each option in each
rank using Eq. (27), and the total performance using Eq. (28). The performance analysis results are exhibited
in Fig. 11, where COPRAS showed the most similar results to SRP, and ARAS has the slightest similarity in the
performance according to the results obtained from the Zakeri-Konstantas performance correlation coefficient.
The results also show that AHP and SRP are different in generating results.


m 1min≤i≤m� mR2+i[l] �m−mi=mR1 [i][ ;]il [ m]R[2][+]i[h] �[m][−]mi=[mR]1 [i] i[h] �

ZK(l:h) = [100]m � � m2+m−mRil i �, (25)

i=1 1max≤i≤m Ri[l] �mi=1 [i][ ;][ m]R[2][+]i[h] �[m][−]mi=[mR]1 [i] [h]


where


ZK(l:h) = � 0, [�]i[m]=1 [�]�Ri[l] [−] [R]i[h]2�0.52�0.5 = [m]2[2] [,][ m][ =][ 2][κ][,][ κ][ ∈] [N][,][ κ][ �=][ 0, 1], (26)

0, i=1 [�]�Ri[l] [−] [R]i[h]� � = [m][2]2[−][1], m = 2κ + 1, κ ∈ N, κ �= 0

[�][m]


−1

Ui[F] [=] �(m + 1) − Ri[F] ��[m] i, i = {1, . . ., m}, (27)

i=1


−1

Ŵi[F] [=][ R]i[F] [�]�(m + 1) − Ri[F] ��[m] i �, i = {1, . . ., m}, (28)

i=1

ZK[t](l:h) [=][ ZK][(][l][:][h][)][(][m][ −] [1][)][−][1][,][ i][ = {][1,][ . . .][,][ m][}][,] (29)


_The dependency analysis._ The comparison process was conducted in the previous section to determine how
dependent each method is on the weights of criteria. As a result, a new statistical measure called dependency
analysis was proposed instead of using sensitivity analysis. The dependency analysis measures the dependency
of a ranking on the information embedded in a criterion’s corresponding data set. Greater dependency leads to
an increased sensitivity of the method to changes in criteria weights, which in turn results in greater reliability.
The dependency analysis is grounded on three central concepts: fair vital importance, real importance, and fair
feeble importance. It measures changes in a ranking based on the impact of the mentioned concepts to estimate
the dependency of a ranking on each criterion. The following equations show its process, where θj[c][x][, ][�]j[c][x][, ][β]j[c][x][, and ]

wj[c][F][ stand for the real importance, the fair vital importance, fair feeble importance of ][x][ th criteria, and weights ]

of the rest criteria, respectively. The constant values of �[c]j [x][, ][β]j[c][x][, and ][w]j[c][F][ have been provided in Tables ][27][ and ][28][.]

In Eqs. (33) and (34), RAβj[cx]i [, ][R]A�[cx]ji [, and ][R]Aθj[cx]i [ denote the rank ][i][ th alternative ( ][A][i][ ), affected by the fair vital impor-]

tance, fair feeble importance, and the real importance. �cx also demonstrates the overall dependency of the rank
generated by an MCDM method to a criterion. � stands for the dependency of a ranking to the criteria, where

� ≤ 0.5 expresses the reliability of the generator, in our case an MCDM method. In fact, in a comparison process
of the generators, MCDM methods, the one that its corresponding � is closer to 1 shows the more reliability


-----

|Col1|n|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
|cx j|0.800|0.833|0.857|0.875|0.889|0.900|0.909|0.917|0.923|0.929|0.933|0.938|0.941|0.944|0.947|0.950|
|wcF j|0.050|0.033|0.024|0.018|0.014|0.011|0.009|0.008|0.006|0.005|0.005|0.004|0.004|0.003|0.003|0.003|
|ς|||0.01 ≤ς ≤0.05|||0.05 ≤ς ≤0.1||||||0.06 ≤ς ≤0.11|||||


**Table 27. Constant values of the fair vital importance based on the number of criteria, 20 criteria,** max
1≤j≤n[j][ =][ 20][.]

**8** **9** **10** **11** **12** **13** **14** **15** **16** **17** **18** **19** **20**

0.175 0.161 0.150 0.081 0.073 0.067 0.061 0.057 0.053 0.049 0.046 0.043 0.040

0.118 0.105 0.094 0.092 0.084 0.078 0.072 0.067 0.063 0.059 0.056 0.053 0.051

0 < ξ ≤ 0.025

**Table 28. Constant values of the fair feeble importance based on the number of criteria, 20 criteria,**

max
1≤j≤n[j][ =][ 20][.]

and the more dependency to the criteria. In contrast, � ≥ 0.5 portrays the unreliability of the generator, or the
MCDM method in the evaluation of the alternatives.

θj[c][x] = wx, j = {1, . . ., n}, x ∈ j, x ≤ n, (30)

|Col1|n|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
|βcx j|0.250|0.217|0.193|0.175|0.161|0.150|0.081|0.073|0.067|0.061|0.057|0.053|0.049|0.046|0.043|0.040|
|wcF j|0.188|0.157|0.135|0.118|0.105|0.094|0.092|0.084|0.078|0.072|0.067|0.063|0.059|0.056|0.053|0.051|
|ξ|0 < ξ ≤0.05||||||0 < ξ ≤0.025||||||||||


 n[−][1](n − 1) wj, j = {1, . . ., n}, x ∈ j, x ≤ n, n ≤ 6

�[c][x]  �n[−][1](n − 1[�]) wj�− ς, j = {1, . . ., n}, x ∈ j, x ≤ n, 7 ≤ n ≤ 9, 0.01 ≤ ς ≤ 0.05,
j [=] �n[−][1](n − 1) [�] wj�− ς, j = {1, . . ., n}, x ∈ j, x ≤ n, 10 ≤ n ≤ 15, 0.06 ≤ ς ≤ 0.09 (31)

 �n[−][1](n − 1) [�][�] wj�− ς, j = {1, . . ., n}, x ∈ j, x ≤ n, 15 ≤ n ≤ 20, 0.06 ≤ ς ≤ 0.11

βj[c][x] = � ��nn[−][−][1][1][ �][ �] wwjj�+�+ ξ ξ,, j j = { = {1,1, . . . . . .,, n n}},, x x ∈ ∈ jj, 0, 0 < ξ < ξ ≤ ≤ 0.025,0.05, x x ≤ ≤nn, 5, 11 ≤ ≤n ≤n ≤1020 [,] (32)


 1−�[cx]j

wj[c][F] =  1n−−β1j[cx] [,][ j][ = {][1,][ . . .][,][ n][}][,][ x][ ∈] [j][,][ x][ ≤] [n][,][ F][ =][ j][ −{][x][}], (33)

 n−1 [,][ j][ = {][1,][ . . .][,][ n][}][,][ x][ ∈] [j][,][ x][ ≤] [n][,][ F][ =][ j][ −{][x][}]

βj[cx] �[cx]j

Ai [−] [R]Ai

�[A]cj[i] [=][ R] RAθj[cx]i × 100, i = {1, . . ., m}, j = {1, . . ., n}, x ∈ n, F = j −{x}, (34)


Proof:


θj[cx] �[cx]j θj[cx] βj[cx] βj[cx] �[cx]j

Ai [−] [R]Ai Ai [−] [R]Ai Ai [−] [R]Ai

�[A]cj[i] [= �] [R] RAθj[cx]i × 100�−� [R] RAθj[cx]i × 100�= [R] RAθj[cx]i × 100, (35)


n 0.5 n 0.5

� = n[−][1][ �] n�1max≤i≤m� �[A]cj[i] 2 �− � �[A]cj[i] 2, 0 ≤ � ≤ 1, i = {1, . . ., m}, (36)

j=1 j=1

Figure 12 depict the changes in each material’s rank caused by applying each criterion’s corresponding fair
vital importance and fair feeble importance compared to the original ranking associated with the criteria’s real
importance. Compared to the changes in overall ranks affected by fair vital importance in overall rankings,
almost no changes were detected in the rankings affected by the feeble fair criteria, which indicates that the
SRP becomes more sensitive to weight changes by increasing the number of criteria. Figure 13, developed using
Eq. (33), displays the dependency of the ranking generated by SRP on each criterion.
By applying Eq. (35), it has been found that the overall dependency of SRP method is 0.513, which indicates
a value of Ω ≤ 0.50, slightly exceeding the limit established for an MCDM method’s reliability. This indicates that
SRP method is reliable in analyzing problems with six criteria. Since SRP method employs the ranks of each
alternative in each criterion, and the criteria weight plays a critical role in determining the generated rankings,


-----

**a** 10

9

8

7

6

5

4

3

2

1

0

1 2 3 4 5 6 7 8 9

Vital fair importance Feeble fair importance SRP

**b** 10

9
8
7
6
5
4
3
2
1
0

1 2 3 4 5 6 7 8 9

Vital fair importance Feeble fair importance SRP

**c** 10

9
8
7
6
5
4
3
2
1
0

1 2 3 4 5 6 7 8 9

Vital fair importance Feeble fair importance SRP

**d** 10

9

8

7

6

5

4

3

2

1

0

1 2 3 4 5 6 7 8 9

Vital fair importance Feeble fair importance SRP

**Figure 12. (a) Changes in ranking, affected by the vital and feeble fair importance values, associated with**
weight of c1 . (b) Changes in ranking, affected by the vital and feeble fair importance values, associated with
weight of c2 criterion. (c) Changes in ranking, affected by the vital and feeble fair importance values, associated
with weight of c3 criterion. (d) Changes in ranking, affected by the vital and feeble fair importance values,
associated with weight of c4 criterion. (e) Changes in ranking, affected by the vital and feeble fair importance
values, associated with weight of c5 criterion. (f)Changes in ranking, affected by the vital and feeble fair
importance values, associated with weight of c6 criterion.


-----

**Figure 12. (continued)**


600

400

200


0


-200

-400

-600

-800

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|loride hexahydrate|Stearic acid|p116|RT 60|araffin wax RT 30|n-Docosane|n-Octadecane|n-Nonadecane|n-Eicosane|


Latent Heat Density Specific Heat (Cp(s))

Specific Heat (Cp(l)) Thermal Conductivity Cost


**Figure 13. Dependency of each material on each criterion.**

reliability of the method improves with increasing criteria, making it an effective tool for solving complex
MCDM problems.


#### The comparative rankings analysis—Similarity measures. In this section, the obtained ranks from
different MCDM methods have been evaluated through six similarity measures, including Manhattan distance
and total similarity Eqs. (36) and (37), Canberra distance and total similarity Eqs. (38) and (39), Chi-square distance and total similarity Eqs. (40) and (41), and Squared Euclidean distance and total similarity Eqs. (42) and
(43), in order to conclude the similarities between SRP and other MCDM methods Eq. (44). In the equations,
Rx, Ry, R[x]i [, and ][R]i[y][ represent the output of ][x][ th MCDM method, ] [y][ th MCDM method, ][i][ th alternative’s rank in ]

x th MCDM method, and the same alternative’s rank in y th MCDM method, respectively. Td(Rx,RV ) denote the
total similarity between x th MCDM method and yth MCDM method, in which ℵ signifies the total number of
MCDM methods that have been used for similarity evaluation.


-----

m

d1�Rx, Ry� = � ��Rxi [−] [R]i[y]��, i = {1, .., m}, Rx = �R[x]1[, ...,][ R]m[x] �, Ry = �R[y]1[, ...,][ R]m[y] �, (37)

i=1


m g m −1

d1′ [(][R][x][,][ R][V] [)][ = �]� ��Rxi [−] [R]i[y]���� � ��Rxi [−] [R]i[y]��� �× 100, y ∈ V, V = �1, . . ., g�, (38)

i=1 V =1 i=1


m Rx

d2�Rx, Ry� = � ��Rxi [−] [R]i[y]��, (39)

i=1 �� i [+][ R]i[y]��


d2′ [(][R][x][,][ R][V] [)][ = �]�m ��RRxxi [−] [R]i[y]�� ��g �m ��RRxix [−] [R]i[y]�� �−1�× 100, (40)

i=1 �� i [+][ R]i[y]�� V =1 i=1 �� i [+][ R]i[y]��


d3�Rx, Ry� = �m �RR[x]i[x][−] [R]i[y]�2, (41)

i=1 i [+][ R]i[y]


d3′ [(][R][x][,][ R][V] [)][ = �]�m �R[x]i [−] [R]i[y]�2 ��g �m �R[x]i [−] [R]i[y]�2 �−1�× 100, (42)

R[x] R[x]

i=1 i [+][ R]i[y] V =1 i=1 i [+][ R]i[y]


m

d4�Rx, Ry� = � �R[x]i [−] [R]i[y]�2, (43)

i=1


m g m −1

d4′ [(][R][x][,][ R][V] [)][ = �]� �R[x]i [−] [R]i[y]�2�� � �R[x]i [−] [R]i[y]�2� �× 100, (44)

i=1 V =1 i=1


′ ′ ′ ′
1[(][R][x][,][ R][V] [)] d2[(][R][x][,][ R][V] [)] d3[(][R][x][,][ R][V] [)] d4[(][R][x][,][ R][V] [)]

Td(Rx,RV ) = � [d] ′ + ′ + ′ + ′ �ℵ[−][1], (45)

� d1[(][R][x][,][ R][V] [)] � d2[(][R][x][,][ R][V] [)] � d3[(][R][x][,][ R][V] [)] � d4[(][R][x][,][ R][V] [)]

_Manhattan distance._ Using Manhattan distance to evaluate the similarities between SRP and VIKOR, WPM,
TOPSIS, ARAS, COPRAS, and AHP showed that VIKOR has the most resemblance in evaluating materials with
SRP. The results of using Manhattan distance are illustrated in Fig. 14.

_Canberra distance._ Similar to the Manhattan distance, the Canberra distance puts VIKOR most resembling
SRP. Applying the Canberra distance puts AHP higher than TOPSIS as the second most resemblance method
to the SRP in solving the material selection problem. In contrast, the Manhattan distance considers TOPSIS the
second most resemblance method to the SRP with a slightly higher score (see Table 29). The results of the Canberra distance application are pictured in Fig. 15.

5 10 15 20 25 30 35

VIKOR WPM TOPSIS ARAS COPRAS AHP

**Figure 14. Comparative analysis of the similarity between SRP and other MCDM methods using Manhattan**
di t


-----

|Distance|AHP|COPRAS|ARAS|TOPSIS|WPM|VIKOR|
|---|---|---|---|---|---|---|
|Manhattan distance|27.4509|13.7255|15.6860|27.4510|13.725|29.4117|
|Canberra distance|17.6120|15.5224|15.8209|17.6119|15.5223|17.9104|
|Chi-square distance|21.8610|11.2600|11.2470|21.2340|9.0500|25.3480|
|Hamming distance|22.3048|10.0371|10.7806|23.7918|7.8066|25.2788|


**Table 29. Results of each similarity measure method.**

14.5 15 15.5 16 16.5 17 17.5 18 18.5

VIKOR WPM TOPSIS ARAS COPRAS AHP

**Figure 15. Comparative analysis of the similarity between SRP and other MCDM methods using Canberra**
distance.

5 10 15 20 25 30

VIKOR WPM TOPSIS ARAS COPRAS AHP

**Figure 16. Comparative analysis of the similarity between SRP and other MCDM methods using Chi-square**
distance.

_Chi‑square distance._ The Chi-square distance analysis reveals that AHP is the second most similar MCDM
method to SRP, while WPM is the least similar. In comparison to Manhattan and Canberra distances, where
COPRAS and WPM have almost equal scores, Chi-square distance gives WPM the lowest similarity score and
the farthest distance from the COPRAS method. The results of this comparison are shown in Fig. 16.

_Squared Euclidean distance._ Except for VIKOR which has been placed by Squared Euclidean distance as the
most similar method to SRP dominantly, TOPSIS is the second MCDM method that shows similarity to SRP in
ranking the materials. The results of Squared Euclidean distance application are portrayed in Fig. 17.

_Total similarity._ "Total similarity" as computed using Eq. (44), has generated almost identical rankings of similarity, where VIKOR, TOPSIS, and AHP, with a considerable distance, are the most similar methods to the SRP
method, respectively. On the other hand, ARAS, COPRAS, and WPM showed the most dissimilarity compared
to SRP. The results are demonstrated in Table 29 and Fig. 18.

#### The rank reversal phenomenon: A comparison between SRP and other rank reversal free MCDM methods. The rank reversal phenomenon refers to the occurrence of changes in the relative rankings of alternatives when additional alternatives are introduced or existing alternatives are removed from a set
being evaluated in MCDM environment[99] This phenomenon can lead to inconsistent decisions and can make


-----

SRP

0 5 10 15 20 25 30

VIKOR WPM TOPSIS ARAS COPRAS AHP

**Figure 17. Comparative analysis of the similarity between SRP and other MCDM methods using Squared**
Euclidean distance.

Total similarity

0 5 10 15 20 25

VIKOR WPM TOPSIS ARAS COPRAS AHP

**Figure 18. Total similarity of each MCDM method to SRP.**

it challenging to compare and evaluate alternatives across different decision problems. Several MCDM methods
have been proven to be rank reversal-free, including Characteristic Objects Method (COMET) proposed by
Piegat & Sałabun[100] and Sałabun[101], Stable Preference Ordering Towards Ideal Solution (SPOTIS) developed by
­Dezert[102], Ranking of Alternatives through Functional mapping of criterion sub-intervals into a Single Interval (RAFSI) proposed by Žižović et al.[103], and the Sequential Interactive Model of Urban Systems (SIMUS)
developed by ­Munier[104]. Among these methods, COMET method is the first MCDM method that is completely
immune to the rank reversal paradox. COMET method considers the correlations between the criteria, and
provides ranking by considering the characteristic objects and fuzzy ­rules[101]. COMET method has proven to
be robust and effective in avoiding the rank reversal paradox in various applications, such as those described in
Wątróbski et al.[105][,] Shekhovtsov et al.[106][,] Faizi et al.[107][,] and Palczewski & Sałabun[108]. To test the rank reversal paradox of SRP, three examples are provided including a material selection case and two other numerical examples.

_The material selection case._ A new alternative is added to the original material selection decision matrix
(Table 5), in which A[∗]4[ stands for the new alternative and its performance is equal to ] [A][4][ . The new decision ]
matrix and the corresponding ranks given by SRP are shown in Table 30. In order to demonstrate the correlation
between the original ranking and the obtained ranking, Fig. 19 is presented, where a correlation of 1 is indicated,
suggesting that SRP is a rank reversal free MCDM method.

#### The first numerical example. A numerical example is presented in Table 31, comprising of eleven alternatives and fifteen criteria. All the criteria are beneficial, having equal weights. The ranking of alternatives is
shown in Table 32, where A6 is assigned the first rank. In the case of adding a new alternative with the same
performance as A6, no changes have been observed in the ranks, and the correlation between the two rankings
is one, as shown in Table 33 and Fig. 20.

#### Second numerical example. An additional example is presented to represent a more complex MCDM
problem with a larger number of alternatives and fewer criteria. This example includes twenty alternatives and
four criteria, each with equal weights, as shown in Table 33. To illustrate the robustness of SRP, a new alternative
with the same performance as the original top-ranked alternative (A15) is added, resulting in no changes in the


-----

|PCM|c1|c2|c3|c4|c5|c6|SRi|R i|Original rank|New rank|
|---|---|---|---|---|---|---|---|---|---|---|
|A1|169.98|1560|1.46|2.13|1.09|0.255|4.269|4.731|2|2|
|A2|186.5|903|2.83|2.38|0.18|0.745|5.012|3.988|7|7|
|A3|190|830|2.1|2.1|0.21|0.335|4.68|4.32|5|5|
|A4|214.4|850|0.9|0.9|0.2|0.255|4.084|4.916|1|1|
|A5|206|789|1.8|2.4|0.18|0.335|4.674|4.326|4|4|
|A6|194.6|785|1.93|2.38|0.22|0.335|4.321|4.679|3|3|
|A7|245|773.22|0.3767|2.267|0.14|0.335|5.545|3.455|9|9|
|A8|222|775.8|1.7189|1.921|0.142|0.665|5.339|3.661|8|8|
|A9|247|776.33|0.7467|2.377|0.138|0.336|4.981|4.019|6|6|
|A4*|214.4|850|0.9|0.9|0.2|0.255|||||


**Table 30. New ranking given by SRP after adding the new alternative.**

**Figure 19. The correlation between two ranks to assess the rank reversal incident.**

**0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067** **0.067**

**C3** **C4** **C5** **C6** **C7** **C8** **C9** **C10** **C11** **C12** **C13** **C14** **C15**

3.252 0.737 0.092 1.318 2.912 0.074 0.054 0.067 1.505 1.599 1.219 0.056 0.031

0.732 3.564 2.545 2.059 1.860 0.056 0.070 0.085 1.265 0.116 0.783 0.080 0.005

2.485 1.599 3.900 0.267 1.477 0.089 0.067 0.096 0.898 1.037 0.821 0.028 0.088

1.336 1.788 1.804 3.879 2.650 0.001 0.041 0.050 0.023 0.976 1.057 0.002 0.010

2.777 3.025 0.814 1.256 1.136 0.034 0.054 0.078 0.606 1.650 0.805 0.013 0.032

3.353 2.240 3.840 2.005 2.250 0.030 0.099 0.080 0.578 1.660 0.669 0.030 0.083

0.467 0.681 0.960 1.986 1.998 0.002 0.096 0.084 0.660 0.800 1.673 0.089 0.002

2.966 0.639 0.959 3.116 0.424 0.097 0.089 0.089 0.438 0.944 0.544 0.041 0.080

3.819 3.948 2.994 3.610 1.725 0.001 0.017 0.030 0.221 1.516 0.755 0.064 0.017

2.546 0.787 3.038 0.552 1.946 0.002 0.007 0.050 0.068 0.397 0.127 0.029 0.002

1.675 3.243 0.306 1.696 1.732 0.081 0.068 0.059 0.334 0.342 0.348 0.038 0.031

**Table 31. Decision matrix of the first numerical example.**

ranking and a correlation coefficient of one, as shown in Fig. 21. This provides further evidence that SRP is a
rank reversal-free MCDM method.
The above examples revealed that the SRP method is utterly immune to the rank reversal paradox. As mentioned earlier, SPOTIS, COMET, and SIMUS are also rank reversal-free MCDM methods. The complexity of any
MCDM method can lead to less transparency and uncertainty in its outcomes, especially in complex systems
with many interacting parts and variables. Increased complexity of an MCDM method also hinders the ability

|Weight|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|0.067|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Alternative|C1|C2|C3|C4|C5|C6|C7|C8|C9|C10|C11|C12|C13|C14|C15|
|A1|0.087|0.046|3.252|0.737|0.092|1.318|2.912|0.074|0.054|0.067|1.505|1.599|1.219|0.056|0.031|
|A2|0.002|0.094|0.732|3.564|2.545|2.059|1.860|0.056|0.070|0.085|1.265|0.116|0.783|0.080|0.005|
|A3|0.047|0.052|2.485|1.599|3.900|0.267|1.477|0.089|0.067|0.096|0.898|1.037|0.821|0.028|0.088|
|A4|0.093|0.011|1.336|1.788|1.804|3.879|2.650|0.001|0.041|0.050|0.023|0.976|1.057|0.002|0.010|
|A5|0.058|0.084|2.777|3.025|0.814|1.256|1.136|0.034|0.054|0.078|0.606|1.650|0.805|0.013|0.032|
|A6|0.017|0.032|3.353|2.240|3.840|2.005|2.250|0.030|0.099|0.080|0.578|1.660|0.669|0.030|0.083|
|A7|0.075|0.050|0.467|0.681|0.960|1.986|1.998|0.002|0.096|0.084|0.660|0.800|1.673|0.089|0.002|
|A8|0.011|0.051|2.966|0.639|0.959|3.116|0.424|0.097|0.089|0.089|0.438|0.944|0.544|0.041|0.080|
|A9|0.080|0.096|3.819|3.948|2.994|3.610|1.725|0.001|0.017|0.030|0.221|1.516|0.755|0.064|0.017|
|A10|0.002|0.035|2.546|0.787|3.038|0.552|1.946|0.002|0.007|0.050|0.068|0.397|0.127|0.029|0.002|
|A11|0.048|0.011|1.675|3.243|0.306|1.696|1.732|0.081|0.068|0.059|0.334|0.342|0.348|0.038|0.031|


-----

|Alternative|SRi|R i|SRi2|R i2|Original rank|New rank|
|---|---|---|---|---|---|---|
|A1|5.0000|6.0000|5.5333|6.4667|2|2|
|A2|5.4000|5.6000|5.8667|6.1333|4|4|
|A3|5.1333|5.8666|5.6000|6.4000|3|3|
|A4|6.9333|4.0666|7.6667|4.3333|9|9|
|A5|6.0666|4.9333|6.6667|5.3333|8|8|
|A6|4.7333|6.2666|4.7333|7.2667|1|1|
|A7|5.7333|5.2666|6.3333|5.6667|6|6|
|A8|5.8666|5.1333|6.5333|5.4667|7|7|
|A9|5.4666|5.5333|6.0000|6.0000|5|5|
|A10|8.600|2.40000|9.5333|2.4667|11|11|
|A11|7.0666|3.9333|7.8000|4.2000|10|10|


**Table 32. The different alternatives’ rankings to test the rank reversal paradox.**

**Weight** **0.25** **0.25** **0.25** **0.25**

**Alternative** **C1** **C2** **C3** **C4** **SRi** Ri **SRi** **2** Ri **2** **Original rank** **New rank**

A1 912.4845 0.3018 206.4309 0.1221 12.75 7.25 13.5 7.5 14 14

A2 517.0006 0.1986 616.1050 0.0945 13.5 6.5 14.5 6.5 16 16

A3 19.61708 0.6361 348.3409 0.1985 14.5 5.5 15.5 5.5 17 17

A4 1069.093 0.9259 918.6073 0.0005 8.25 11.75 9 12 5 5

A5 151.0204 0.0969 376.8284 0.2074 15.25 4.75 16.25 4.75 19 19

A6 1022.647 0.2007 430.3449 0.3781 9 11 9.75 11.25 6 6

A7 944.3263 1.2419 443.6463 0.2520 6.75 13.25 7.5 13.5 4 4

A8 974.168 0.2407 978.1523 0.0137 10.25 9.75 10.75 10.25 9 9

A9 504.9541 1.2165 176.6877 0.3398 10 10 11 10 8 8

A10 549.4893 0.2430 645.7940 0.2352 10.5 9.5 11.5 9.5 10 10

A11 319.5062 1.1863 57.60621 0.3537 11 9 12 9 12 12

A12 86.49311 0.6288 258.042 0.0811 15.5 4.5 16.5 4.5 20 20

A13 991.6532 0.6623 962.0012 0.3963 4 16 4.25 16.75 2 2

A14 279.4132 1.0169 688.305 0.0302 11.5 8.5 12.5 8.5 13 13

A15 787.9316 2.1867 926.4695 0.3922 3.75 16.25 3.75 17.25 1 1

A16 866.5065 1.0388 1044.6860 0.2068 6 14 6.5 14.5 3 3

A17 580.661 0.3445 430.0089 0.0343 13.25 6.75 14.25 6.75 15 15

A18 407.2574 0.5822 659.9484 0.3830 9 11 10 11 6 6

A19 460.7242 0.0873 491.7818 0.1171 14.5 5.5 15.5 5.5 17 17

A20 45.74425 0.7103 643.1528 0.2860 10.75 9.25 11.75 9.25 11 11

**Table 33. Two obtained rankings from SRP application for the second numerical example.**

to track and identify errors in the algorithmic output. Complex systems, such as those with numerous pairwise
comparisons or different normalization approaches, are more likely to produce uncertain outcomes due to the
complex interplay between variables. One of the major benefits of SRP in this context is its simplicity which helps
to avoid those issues and provides reliable results when the problem becomes more complex.

### Conclusions and future research
Material selection problems are complex MCDM problems that comprise many options and criteria. To solve
material selection problems, a new simple MCDM method called SRP is proposed in this paper. The new method
functions based on the different ranks of the material in each criterion to generate reliable outputs in solving
MCDM problems. One of the sources of anomalies in comparison processes of the generated results of MCDM
methods is the different normalization strategies employed by different MCDM methods. To enhance the reliability of results in complex MCDM problems, SRP method avoids the normalization process of the decision
matrix and operates solely with the ranks of alternatives, enabling a comparison of scores with the same unit. In
a material selection problem that involved selecting a suitable phase change material to store solar energy, SRP
method was employed. However, since SRP relies heavily on the criteria weights in generating rankings, it is
essential to have a dependable method for determining these weights. In this study, VIMM method was utilized
to extract the criteria weights through a decision-making process involving seven experts. By utilizing the newly

|Weight|0.25|0.25|0.25|0.25|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Alternative|C1|C2|C3|C4|SRi|R i|SRi2|R i2|Original rank|New rank|
|A1|912.4845|0.3018|206.4309|0.1221|12.75|7.25|13.5|7.5|14|14|
|A2|517.0006|0.1986|616.1050|0.0945|13.5|6.5|14.5|6.5|16|16|
|A3|19.61708|0.6361|348.3409|0.1985|14.5|5.5|15.5|5.5|17|17|
|A4|1069.093|0.9259|918.6073|0.0005|8.25|11.75|9|12|5|5|
|A5|151.0204|0.0969|376.8284|0.2074|15.25|4.75|16.25|4.75|19|19|
|A6|1022.647|0.2007|430.3449|0.3781|9|11|9.75|11.25|6|6|
|A7|944.3263|1.2419|443.6463|0.2520|6.75|13.25|7.5|13.5|4|4|
|A8|974.168|0.2407|978.1523|0.0137|10.25|9.75|10.75|10.25|9|9|
|A9|504.9541|1.2165|176.6877|0.3398|10|10|11|10|8|8|
|A10|549.4893|0.2430|645.7940|0.2352|10.5|9.5|11.5|9.5|10|10|
|A11|319.5062|1.1863|57.60621|0.3537|11|9|12|9|12|12|
|A12|86.49311|0.6288|258.042|0.0811|15.5|4.5|16.5|4.5|20|20|
|A13|991.6532|0.6623|962.0012|0.3963|4|16|4.25|16.75|2|2|
|A14|279.4132|1.0169|688.305|0.0302|11.5|8.5|12.5|8.5|13|13|
|A15|787.9316|2.1867|926.4695|0.3922|3.75|16.25|3.75|17.25|1|1|
|A16|866.5065|1.0388|1044.6860|0.2068|6|14|6.5|14.5|3|3|
|A17|580.661|0.3445|430.0089|0.0343|13.25|6.75|14.25|6.75|15|15|
|A18|407.2574|0.5822|659.9484|0.3830|9|11|10|11|6|6|
|A19|460.7242|0.0873|491.7818|0.1171|14.5|5.5|15.5|5.5|17|17|
|A20|45.74425|0.7103|643.1528|0.2860|10.75|9.25|11.75|9.25|11|11|


-----

**Figure 20. Correlation between two obtained rankings for the first numerical example.**

25


**Figure 21. The correlation between two obtained rankings from the second numerical example.**

proposed method to validate MCDM methods based on the analysis of their dependency on criteria weights, it
was found that the SRP method is sensitive to changes in the criteria weights. Even slight changes in the weights
can significantly affect the ranks of materials obtained by the SRP method. We also compared the results obtained
from the application of other MCDM methods and found significant differences between the generated results. In
this paper, CDI has been introduced as a new statistical measure to validate the results. CDI is used to interpret
the results of MCDM methods in four categories, namely pragmatic compromise, rational compromise, fair
compromise, and rotten compromise. The most reliable results were placed under the pragmatic compromise
category. On the other hand, undependable results were interpreted according to the fair compromise and
the rotten compromise situations, and their comparison needed to be executed in the real world to determine
which method was better, while the mathematical proof was enough in the first category. The comparison results
were put under the fair compromise category by the results of CDI. The new measure will decrease the cost of
wrong material selection. The obtained ranking from SRP is also compared with other MCDM methods using
Zakeri-Konstantas Performance Correlation Coefficient, which showed that the new method is more similar to
the COPRAS than AHP and ARAS. Four different similarity measures are also applied to evaluate the similarity
between other MCDM methods to SRP which has some salient advantages to make it an ideal MCDM method
for solving complex problems. Overall, with the employed comparison processes, it is concluded that:


1. SRP produces more reliable products since it does not execute the normalization process.


-----

2. SRP is a reliable MCDM method since the analytical processes showed that it is sensitive to changes in the
criteria weights.
3. SRP is designed to generate ranking in a less complex analysis which correlates to less uncertainty in the
final results.
4. The algorithm of SRP is easy to reverse track by decision-makers to identify possible errors.
5. The reliability of SRP increases by increasing the number of criteria, making it ideal for solving complex
decision-making problems involving a large number of criteria and alternatives.
6. According to the results obtained from evaluation of the similarities between other MCDM methods and
SRP, it is observed that SRP behaves similar to distance-based methods, e.g. VIKOR and TOPSIS, and also
shows a resemblance to AHP in some results.

The results also revealed a limitation of SRP. The obtained results are not potentially reliable for those MCDM
problems where the number of criteria is less than six, which makes it an ideal method for solving complex
MCDM problems involving higher number of criteria. Future research would be interesting in assessing the
applicability and validation of the new method. Application and validation of the results of SRP for solving other
material selection problems is the second suggestion for future research. Validation of the interpretation of CDI
by simulation is a very interesting future study work. Other intriguing ideas for future research include comparing the interpretation with other statistical techniques and CDI to validate the outcomes. Integrating criteria
weights from different weighting methods, including both subjective and objective methods, with dependency
analysis to evaluate and validate the result is another exciting suggestion for future research. This paper used
VIMM: the first scenario as a weighting method because of its reliability. It is also suggested to use AHP and
BWM in conjunction with SRP to comparing the results as future research scope. Development of extensions of
SRP for resolving different types of MCDM problems with multiple-layer criteria is the concluding suggestion
for further research.

### Data availability
The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 2 December 2022; Accepted: 17 May 2023

### References
1. Bhaskar, A. S. & Khan, A. Comparative analysis of hybrid MCDM methods in material selection for dental applications. Expert
_Syst. Appl._ [https://​doi.​org/​10.​1016/j.​eswa.​2022.​118268 (2022).](https://doi.org/10.1016/j.eswa.2022.118268)

2. Farid, H. M. A. & Riaz, M. Single-valued neutrosophic Einstein interactive aggregation operators with applications for material
selection in engineering design: Case study of cryogenic storage tank. Complex Intell. Syst. [https://​doi.​org/​10.​1007/​s40747-​021-​](https://doi.org/10.1007/s40747-021-00626-0)
[00626-0 (2022).](https://doi.org/10.1007/s40747-021-00626-0)

3. Thakker, A., Jarvis, J., Buggy, M. & Sahed, A. A novel approach to materials selection strategy case study: Wave energy extraction
impulse turbine blade. Mater. Des. **[29(10), 1973–1980. https://​doi.​org/​10.​1016/j.​matdes.​2008.​04.​022 (2008).](https://doi.org/10.1016/j.matdes.2008.04.022)**

4. Aksakal, B., Ulutaş, A., Balo, F. & Karabasevic, D. A new hybrid MCDM model for insulation material evaluation for healthier
environment. Buildings **[12(5), 655. https://​doi.​org/​10.​3390/​build​ings1​20506​55 (2022).](https://doi.org/10.3390/buildings12050655)**

5. Bhadra, D. & Dhar, N. R. Selection of the natural fiber for sustainable applications in aerospace cabin interior using fuzzy MCDM
model. Materialia **[21, 101270. https://​doi.​org/​10.​1016/j.​mtla.​2021.​101270 (2022).](https://doi.org/10.1016/j.mtla.2021.101270)**

6. Goswami, S. S. & Behera, D. K. Solving material handling equipment selection problems in an industry with the help of entropy
integrated COPRAS and ARAS MCDM techniques. Process Integr. Optim. Sustain. **[5(4), 947–973. https://​doi.​org/​10.​1007/​](https://doi.org/10.1007/s41660-021-00192-5)**
[s41660-​021-​00192-5 (2021).](https://doi.org/10.1007/s41660-021-00192-5)

7. Agrawal, R. Sustainable material selection for additive manufacturing technologies: A critical analysis of rank reversal approach.
_J. Clean. Prod._ **[296, 126500. https://​doi.​org/​10.​1016/j.​jclep​ro.​2021.​126500 (2021).](https://doi.org/10.1016/j.jclepro.2021.126500)**

8. Chatterjee, S. & Chakraborty, S. Material selection of a mechanical component based on criteria relationship evaluation and
MCDM approach. Mater. Today **[44, 1621–1626. https://​doi.​org/​10.​1016/j.​matpr.​2020.​11.​817 (2021).](https://doi.org/10.1016/j.matpr.2020.11.817)**

9. Zakeri, S., Ecer, F., Konstantas, D. & Cheikhrouhou, N. The vital-immaterial-mediocre multi-criteria decision-making method.
_Kybernetes_ [https://​doi.​org/​10.​1108/K-​05-​2021-​0403 (2021).](https://doi.org/10.1108/K-05-2021-0403)

10. Patnaik, P. K., Swain, P. T. R., Mishra, S. K., Purohit, A. & Biswas, S. Composite material selection for structural applications
based on AHP-MOORA approach. Mater. Today **[33, 5659–5663. https://​doi.​org/​10.​1016/j.​matpr.​2020.​04.​063 (2020).](https://doi.org/10.1016/j.matpr.2020.04.063)**

11. Rahim, A. A., Musa, S. N., Ramesh, S. & Lim, M. K. Development of a fuzzy-TOPSIS multi-criteria decision-making model for
material selection with the integration of safety, health and environment risk assessment. Proc. Inst. Mech. Eng. L [https://​doi.​](https://doi.org/10.1177/2F1464420721994269)
[org/​10.​1177/​2F146​44207​21994​269 (2021).](https://doi.org/10.1177/2F1464420721994269)

12. Figueiredo, K., Pierott, R., Hammad, A. W. & Haddad, A. Sustainable material choice for construction projects: A life cycle
sustainability assessment framework based on BIM and Fuzzy-AHP. Build. Environ. [https://​doi.​org/​10.​1016/j.​build​env.​2021.​](https://doi.org/10.1016/j.buildenv.2021.107805)
[107805 (2021).](https://doi.org/10.1016/j.buildenv.2021.107805)

13. Zoghi, M., Rostami, G., Khoshand, A. & Motalleb, F. Material selection in design for deconstruction using Kano model, fuzzyAHP and TOPSIS methodology. Waste Manag. Res. [https://​doi.​org/​10.​1177/​2F073​4242X​21101​3904 (2021).](https://doi.org/10.1177/2F0734242X211013904)

14. MacCrimmon, K. R. Decisionmaking among multiple-attribute alternatives: a survey and consolidated approach (No. RM4823-ARPA). RAND CORP SANTA MONICA CA (1968).

15. Peng, C., Feng, D. & Guo, S. Material selection in green design: A method combining DEA and TOPSIS. Sustainability **13(10),**
[5497. https://​doi.​org/​10.​3390/​su131​05497 (2021).](https://doi.org/10.3390/su13105497)

16. Kiani, B., Liang, R. Y. & Gross, J. Material selection for repair of structural concrete using VIKOR method. Case Stud. Constr.
_Mater._ **[8, 489–497. https://​doi.​org/​10.​1016/j.​cscm.​2018.​03.​008 (2018).](https://doi.org/10.1016/j.cscm.2018.03.008)**

17. Fontela, E. & Gabus, A. The Dematel Observer (Battelle Geneva Research Center, 1976).
18. Meng, F. & Dong, B. Linguistic intuitionistic fuzzy PROMETHEE method based on similarity measure for the selection of
sustainable building materials. J. Ambient Intell. Hum. Comput. [https://​doi.​org/​10.​1007/​s12652-​021-​03338-y (2021).](https://doi.org/10.1007/s12652-021-03338-y)

19. Jahan, A. & Zavadskas, E. K. ELECTRE-IDAT for design decision-making problems with interval data and target-based criteria.
_Soft Comput._ **[23(1), 129–143. https://​doi.​org/​10.​1007/​s00500-​018-​3501-6 (2019).](https://doi.org/10.1007/s00500-018-3501-6)**


-----

20. Zakeri, S. Ranking based on optimal points multi-criteria decision-making method. Grey Syst. [https://​doi.​org/​10.​1108/​GS-​09-​](https://doi.org/10.1108/GS-09-2018-0040)

[2018-​0040 (2019).](https://doi.org/10.1108/GS-09-2018-0040)

21. Keršulienė, V. & Turskis, Z. Integrated fuzzy multiple criteria decision making model for architect selection. Technol. Econ. Dev.
_Econ._ **[17(4), 645–666. https://​doi.​org/​10.​3846/​20294​913.​2011.​635718 (2011).](https://doi.org/10.3846/20294913.2011.635718)**

22. Toloie-Eshlaghy, A., Homayonfar, M., Aghaziarati, M. & Arbabiun, P. A subjective weighting method based on group decision
making for ranking and measuring criteria values. Aust. J. Basic Appl. Sci. **5(12), 2034–2040 (2011).**

23. Xu, X. The SIR method: A superiority and inferiority ranking method for multiple criteria decision making. Eur. J. Oper. Res.
**[131(3), 587–602. https://​doi.​org/​10.​1016/​S0377-​2217(00)​00101-6 (2001).](https://doi.org/10.1016/S0377-2217(00)00101-6)**

24. Jessop, A. IMP: A decision aid for multiattribute evaluation using imprecise weight estimates. Omega **[49, 18–29. https://​doi.​org/​](https://doi.org/10.1016/j.omega.2014.05.001)**

[10.​1016/j.​omega.​2014.​05.​001 (2014).](https://doi.org/10.1016/j.omega.2014.05.001)

25. Rezaei, J. Best-worst multi-criteria decision-making method. Omega **[53, 49–57. https://​doi.​org/​10.​1016/j.​omega.​2014.​11.​009](https://doi.org/10.1016/j.omega.2014.11.009)**
(2015).

26. Voogd, H. Multicriteria evaluation with mixed qualitative and quantitative data. Environ. Plann. B. Plann. Des. **9(2), 221–236.**

[https://​doi.​org/​10.​1068/​b0902​21 (1982).](https://doi.org/10.1068/b090221)

[27. Voogd, J. H. Multicriteria evaluation for urban and regional planning (1982). https://​doi.​org/​10.​6100/​IR102​252](https://doi.org/10.6100/IR102252)
28. Opricovic, S. & Tzeng, G. H. Extended VIKOR method in comparison with outranking methods. Eur. J. Oper. Res. **178(2),**
[514–529. https://​doi.​org/​10.​1016/j.​ejor.​2006.​01.​020 (2007).](https://doi.org/10.1016/j.ejor.2006.01.020)

29. Zamani-Sabzi, H., King, J. P., Gard, C. C. & Abudu, S. Statistical and analytical comparison of multi-criteria decision-making
techniques under fuzzy environment. Oper. Res. Perspect. **[3, 92–117. https://​doi.​org/​10.​1016/j.​orp.​2016.​11.​001 (2016).](https://doi.org/10.1016/j.orp.2016.11.001)**

30. Zanakis, S. H., Solomon, A., Wishart, N. & Dublish, S. Multi-attribute decision making: A simulation comparison of select
methods. Eur. J. Oper. Res. **[107(3), 507–529. https://​doi.​org/​10.​1016/​S0377-​2217(97)​00147-1 (1998).](https://doi.org/10.1016/S0377-2217(97)00147-1)**

31. Zardari, N. H., Ahmed, K., Shirazi, S. M. & Yusop, Z. B. Weighting Methods and their Effects on Multi-criteria Decision Making
_[Model Outcomes in Water Resources Management (Springer, 2015). https://​doi.​org/​10.​1007/​978-3-​319-​12586-2.](https://doi.org/10.1007/978-3-319-12586-2)_

32. Dehghan-Manshadi, B., Mahmudi, H., Abedian, A. & Mahmudi, R. A novel method for materials selection in mechanical design:
combination of non-linear normalization and a modified digital logic method. Mater. Des. **[28(1), 8–15. https://​doi.​org/​10.​1016/j.​](https://doi.org/10.1016/j.matdes.2005.06.023)**
[matdes.​2005.​06.​023 (2007).](https://doi.org/10.1016/j.matdes.2005.06.023)

33. Peng, D. H., Wang, T. D., Gao, C. Y. & Wang, H. Enhancing relative ratio method for MCDM via attitudinal distance measures
of interval-valued hesitant fuzzy sets. Int. J. Mach. Learn. Cybern. **[8(4), 1347–1368. https://​doi.​org/​10.​1007/​s13042-​016-​0510-6](https://doi.org/10.1007/s13042-016-0510-6)**
(2017).

34. Mustajoki, J., Hämäläinen, R. P. & Salo, A. Decision support by interval SMART/SWING-incorporating imprecision in the
SMART and SWING methods. Decis. Sci. **[36(2), 317–339. https://​doi.​org/​10.​1111/j.​1540-​5414.​2005.​00075.x (2005).](https://doi.org/10.1111/j.1540-5414.2005.00075.x)**

35. Siskos, E. & Tsotsolas, N. Elicitation of criteria importance weights through the Simos method: A robustness concern. Eur. J.
_Oper. Res._ **[246(2), 543–553. https://​doi.​org/​10.​1016/j.​ejor.​2015.​04.​037 (2015).](https://doi.org/10.1016/j.ejor.2015.04.037)**

36. Shannon, C. E. & Weaver, W. The Mathematical Theory of Communication (University of Illinois Press, 1949).
37. Wang, D. & Zhao, J. Design optimization of mechanical properties of ceramic tool material during turning of ultra-high-strength
steel 300M with AHP and CRITIC method. Int. J. Adv. Manufac. Technol. **[84(9–12), 2381–2390. https://​doi.​org/​10.​1007/​s00170-​](https://doi.org/10.1007/s00170-015-7903-7)**
[015-​7903-7 (2016).](https://doi.org/10.1007/s00170-015-7903-7)

38. Das, D., Bhattacharya, S. & Sarkar, B. Decision-based design-driven material selection: a normative-prescriptive approach for
simultaneous selection of material and geometric variables in gear design. Mater. Des. **[92, 787–793. https://​doi.​org/​10.​1016/j.​](https://doi.org/10.1016/j.matdes.2015.12.064)**
[matdes.​2015.​12.​064 (2016).](https://doi.org/10.1016/j.matdes.2015.12.064)

39. Mahmoudkelaye, S., Azari, K. T., Pourvaziri, M. & Asadian, E. Sustainable material selection for building enclosure through
ANP method. Case Stud. Constr. Mater. **[9, e00200. https://​doi.​org/​10.​1016/j.​cscm.​2018.​e00200 (2018).](https://doi.org/10.1016/j.cscm.2018.e00200)**

40. Prasad, R. V., Rajesh, R. & Thirumalaikumarasamy, D. Selection of coating material for magnesium alloy using Fuzzy AHPTOPSIS. Sādhanā **[45(1), 1–20. https://​doi.​org/​10.​1007/​s12046-​019-​1261-3 (2020).](https://doi.org/10.1007/s12046-019-1261-3)**

41. Palanisamy, M., Pugalendhi, A. & Ranganathan, R. Selection of suitable additive manufacturing machine and materials through
best–worst method (BWM). Int. J. Adv. Manufac. Technol. [https://​doi.​org/​10.​1007/​s00170-​020-​05110-6 (2020).](https://doi.org/10.1007/s00170-020-05110-6)

42. Maghsoodi, A. I., Soudian, S., Martínez, L., Herrera-Viedma, E. & Zavadskas, E. K. A phase change material selection using the
interval-valued target-based BWM-CoCoMULTIMOORA approach: A case-study on interior building applications. Appl. Soft
_Comput._ **[95, 106508. https://​doi.​org/​10.​1016/j.​asoc.​2020.​106508 (2020).](https://doi.org/10.1016/j.asoc.2020.106508)**

43. Yang, W.-C., Ri, J.-B., Yang, J.-Y. & Kim, J.-S. Materials selection criteria weighting method using analytic hierarchy process
(AHP) with simplest questionnaire and modifying method of inconsistent pairwise comparison matrix. Proc. Inst. Mech. Eng.
_L_ **[236(1), 69–85. https://​doi.​org/​10.​1177/​14644​20721​10399​12 (2022).](https://doi.org/10.1177/14644207211039912)**

44. Kumar, S., Bhaumik, S., Patnaik, L., Maity, S. R. & Paleu, V. Application of integrated BWM Fuzzy-MARCOS approach for
coating material selection in tooling industries. Materials **[15, 9002. https://​doi.​org/​10.​3390/​ma152​49002 (2022).](https://doi.org/10.3390/ma15249002)**

45. Grachev, D. I. et al. Dental material selection for the additive manufacturing of removable complete dentures (RCD). Int. J. Mol.
_Sci._ **[24(13), 6432. https://​doi.​org/​10.​3390/​ijms2​40764​32 (2023).](https://doi.org/10.3390/ijms24076432)**

46. Bhowmik, C., Gangwar, S., Bhowmik, S. & Ray, A. Selection of energy-efficient material: An entropy–TOPSIS approach. In Soft
_Computing: Theories and Applications (eds Pant, M. et al.) 31–39 (Springer, 2018)._

47. Oluah, C., Akinlabi, E. T. & Njoku, H. O. Selection of phase change material for improved performance of Trombe wall systems
using the entropy weight and TOPSIS methodology. Energy Build. **[217, 109967. https://​doi.​org/​10.​1016/j.​enbui​ld.​2020.​109967](https://doi.org/10.1016/j.enbuild.2020.109967)**
(2020).

48. Mahajan, A., Binaz, V., Singh, I. & Arora, N. Selection of natural fiber for sustainable composites using hybrid multi criteria
decision making techniques. Composites C **[7, 100224. https://​doi.​org/​10.​1016/j.​jcomc.​2021.​100224 (2022).](https://doi.org/10.1016/j.jcomc.2021.100224)**

49. Akgün, H., Yapıcı, E., Özkan, A., Günkaya, Z. & Banar, M. A combined multi-criteria decision-making approach for the selection of carbon-based nanomaterials in phase change materials. J. Energy Storage **[60, 106619. https://​doi.​org/​10.​1016/j.​est.​2023.​](https://doi.org/10.1016/j.est.2023.106619)**
[106619 (2023).](https://doi.org/10.1016/j.est.2023.106619)

50. Haq, R. S. U., Saeed, M., Mateen, N., Siddiqui, F. & Ahmed, S. An interval-valued neutrosophic based MAIRCA method for
sustainable material selection. Eng. Appl. Artif. Intell. **[123, 106177. https://​doi.​org/​10.​1016/j.​engap​pai.​2023.​106177 (2023).](https://doi.org/10.1016/j.engappai.2023.106177)**

51. Ulutaş, A., Balo, F. & Topal, A. Identifying the most efficient natural fibre for common commercial building insulation materials
with an integrated PSI, MEREC LOPCOW and MCRAT model. Polymers **[15(6), 1500. https://​doi.​org/​10.​3390/​polym​15061​500](https://doi.org/10.3390/polym15061500)**
(2023).

52. Gupta, S. M., & Ilgin, M. A. Multiple criteria decision making applications in environmentally conscious manufacturing and
[product recovery. CRC Press. https://​www.​routl​edge.​com/​Multi​ple-​Crite​ria-​Decis​ion-​Making-​Appli​catio​ns-​in-​Envir​onmen​](https://www.routledge.com/Multiple-Criteria-Decision-Making-Applications-in-Environmentally-Conscious/Gupta-Ilgin/p/book/9780367781798)
[tally-​Consc​ious/​Gupta-​Ilgin/p/​book/​97803​67781​798 (2017).](https://www.routledge.com/Multiple-Criteria-Decision-Making-Applications-in-Environmentally-Conscious/Gupta-Ilgin/p/book/9780367781798)

53. Wu, X. & Liao, H. A consensus-based probabilistic linguistic gained and lost dominance score method. Eur. J. Oper. Res. **272(3),**
[1017–1027. https://​doi.​org/​10.​1016/j.​ejor.​2018.​07.​044 (2019).](https://doi.org/10.1016/j.ejor.2018.07.044)

54. Chen, Z. S. et al. Sustainable building material selection: A QFD-and ELECTRE III-embedded hybrid MCGDM approach with
consensus building. Eng. Appl. Artif. Intell. **[85, 783–807. https://​doi.​org/​10.​1016/j.​engap​pai.​2019.​08.​006 (2019).](https://doi.org/10.1016/j.engappai.2019.08.006)**

55. Singh, T., Pattnaik, P., Pruncu, C. I., Tiwari, A. & Fekete, G. Selection of natural fibers based brake friction composites using
hybrid ELECTRE-entropy optimization technique. Polymer Test. **[89, 106614. https://​doi.​org/​10.​1016/j.​polym​ertes​ting.​2020.​](https://doi.org/10.1016/j.polymertesting.2020.106614)**
[106614 (2020)](https://doi.org/10.1016/j.polymertesting.2020.106614)


-----

56. Gul, M., Celik, E., Gumus, A. T. & Guneri, A. F. A fuzzy logic based PROMETHEE method for material selection problems.
_Beni-Suef Univ. J. Basic Appl. Sci._ **[7(1), 68–79. https://​doi.​org/​10.​1016/j.​bjbas.​2017.​07.​002 (2018).](https://doi.org/10.1016/j.bjbas.2017.07.002)**

57. Zindani, D. & Kumar, K. Material selection for turbine seal strips using PROMETHEE-GAIA method. Mater. Today **5(9),**
[17533–17539. https://​doi.​org/​10.​1016/j.​matpr.​2018.​06.​069 (2018).](https://doi.org/10.1016/j.matpr.2018.06.069)

58. Exconde, M. K. J. E., Co, J. A. A., Manapat, J. Z. & Magdaluyo, E. R. Materials selection of 3D printing filament and utilization
of recycled polyethylene terephthalate (PET) in a redesigned breadboard. Procedia CIRP **[84, 28–32. https://​doi.​org/​10.​1016/j.​](https://doi.org/10.1016/j.procir.2019.04.337)**
[procir.​2019.​04.​337 (2019).](https://doi.org/10.1016/j.procir.2019.04.337)

59. Kirişci, M., Demir, I. & Şimşek, N. Fermatean fuzzy ELECTRE multi-criteria group decision-making and most suitable biomedical material selection. Artif. Intell. Med. **[127, 102278. https://​doi.​org/​10.​1016/j.​artmed.​2022.​102278 (2022).](https://doi.org/10.1016/j.artmed.2022.102278)**

60. Zhou, D. Choosing the optimal recycled plastic for making 3D printing filament by ELECTRE decision model. Proc. SPIE Int.
_Soc. Opt. Eng._ [https://​doi.​org/​10.​1117/​12.​26390​70 (2022).](https://doi.org/10.1117/12.2639070)

61. Jayakrishna, K. & Vinodh, S. Application of grey relational analysis for material and end of life strategy selection with multiple
criteria. Int. J. Mater. Eng. Innov. **[8(3/4), 250. https://​doi.​org/​10.​1504/​ijmat​ei.​2017.​090241 (2017).](https://doi.org/10.1504/ijmatei.2017.090241)**

62. Zhang, H., Peng, Y., Tian, G., Wang, D. & Xie, P. Green material selection for sustainability: A hybrid MCDM approach. PLoS
_ONE_ **[12(5), e0177578. https://​doi.​org/​10.​1371/​journ​al.​pone.​01775​78 (2017).](https://doi.org/10.1371/journal.pone.0177578)**

63. Sanghvi, N., Vora, D., Charaya, E., Patel, J. & Sharma, S. An approach for material selection for bone staple (an orthopaedic
implant) using GRA and Fuzzy logic. Mater. Today [https://​doi.​org/​10.​1016/j.​matpr.​2020.​11.​331 (2020).](https://doi.org/10.1016/j.matpr.2020.11.331)

64. Wang, D. & Li, S. Material selection decision-making method for multi-material lightweight automotive body driven by performance. Proc. Inst. Mech. Eng. L **[236(4), 730–746. https://​doi.​org/​10.​1177/​14644​20721​10556​61 (2021).](https://doi.org/10.1177/14644207211055661)**

65. Dwivedi, P. & Sharma, D. K. Application of Shannon entropy and CoCoSo methods in selection of the most appropriate engineering sustainability components. Clean. Mater. **[5, 100118. https://​doi.​org/​10.​1016/j.​clema.​2022.​100118 (2022).](https://doi.org/10.1016/j.clema.2022.100118)**

66. Maidin, N. A., Sapuan, S. M., Taha, M. M. & Mohd, Z. M. Y. Constructing a framework for selecting natural fibres as reinforcements composites based on grey relational analysis. Phys. Sci. Rev. [https://​doi.​org/​10.​1515/​psr-​2022-​0081 (2022).](https://doi.org/10.1515/psr-2022-0081)

67. Maidin, N. A., Sapuan, S. M., Mastura, M. T. & Zuhri, M. Y. M. Materials selection of thermoplastic matrices of natural fibre
composites for cyclist helmet using an integration of DMAIC approach in six sigma method together with grey relational analysis
approach. J. Renew. Mater. **[11(5), 2381–2397. https://​doi.​org/​10.​32604/​jrm.​2023.​026549 (2023).](https://doi.org/10.32604/jrm.2023.026549)**

68. Ishak, N. M., Malingam, S. D. & Mansor, M. R. Selection of natural fibre reinforced composites using fuzzy VIKOR for car
fronthood. Int. J. Mater. Prod. Technol. **[53(3–4), 267–285. https://​doi.​org/​10.​1504/​IJMPT.​2016.​079205 (2016).](https://doi.org/10.1504/IJMPT.2016.079205)**

69. Dev, S., Aherwar, A. & Patnaik, A. Material selection for automotive piston component using entropy-VIKOR method. SILICON
**[12(1), 155–169. https://​doi.​org/​10.​1007/​s12633-​019-​00110-y (2020).](https://doi.org/10.1007/s12633-019-00110-y)**

70. Gadhave, P. D., Prabhune, C. & Pathan, F. Selection of phase change material for domestic water heating using multi criteria
decision approach. Aust. J. Mech. Eng. **[21(1), 295–315. https://​doi.​org/​10.​1080/​14484​846.​2020.​18422​97 (2020).](https://doi.org/10.1080/14484846.2020.1842297)**

71. Bhuiyan, M. M. A. & Hammad, A. A hybrid multi-criteria decision support system for selecting the most sustainable structural
material for a multistory building construction. Sustainability **[15(4), 3128. https://​doi.​org/​10.​3390/​su150​43128 (2023).](https://doi.org/10.3390/su15043128)**

72. Xue, Y., You, J., Lai, X. & Liu, H. An interval-valued intuitionistic fuzzy MABAC approach for material selection with incomplete
weight information. Appl. Soft Comput. **[38, 703–713. https://​doi.​org/​10.​1016/j.​asoc.​2015.​10.​010 (2016).](https://doi.org/10.1016/j.asoc.2015.10.010)**

73. Tian, G. et al. Green decoration materials selection under interior environment characteristics: A grey-correlation based hybrid
MCDM method. Renew. Sustain. Energy Rev. **[81, 682–692. https://​doi.​org/​10.​1016/j.​rser.​2017.​08.​050 (2018).](https://doi.org/10.1016/j.rser.2017.08.050)**

74. Ahmed, M., Qureshi, M. N., Mallick, J. & Ben Kahla, N. Selection of sustainable supplementary concrete materials using OSMAHP-TOPSIS approach. Adv. Mater. Sci. Eng. [https://​doi.​org/​10.​1155/​2019/​28504​80 (2019).](https://doi.org/10.1155/2019/2850480)

75. Deshmukh, D. & Angira, M. Investigation on switching structure material selection for RF-MEMS shunt capacitive switches
using Ashby, TOPSIS and VIKOR. Trans. Electr. Electron. Mater. **[20(3), 181–188. https://​doi.​org/​10.​1007/​s42341-​018-​00094-3](https://doi.org/10.1007/s42341-018-00094-3)**
(2019).

76. Maghsoodi, A. I., Maghsoodi, A. I., Poursoltan, P., Antucheviciene, J. & Turskis, Z. Dam construction material selection by
implementing the integrated SWARA–CODAS approach with target-based attributes. Arch. Civil Mech. Eng. **19(4), 1194–1210.**
[https://​doi.​org/​10.​1016/j.​acme.​2019.​06.​010 (2019).](https://doi.org/10.1016/j.acme.2019.06.010)

77. Roy, J., Das, S., Kar, S. & Pamučar, D. An extension of the CODAS approach using interval-valued intuitionistic fuzzy set for
sustainable material selection in construction projects with incomplete weight information. Symmetry **[11(3), 393. https://​doi.​](https://doi.org/10.3390/sym11030393)**
[org/​10.​3390/​sym11​030393 (2019).](https://doi.org/10.3390/sym11030393)

78. Yadav, S., Pathak, V. K. & Gangwar, S. A novel hybrid TOPSIS-PSI approach for material selection in marine applications.
_Sadhana-Acad. Proc. Eng. Sci._ [https://​doi.​org/​10.​1007/​s12046-​018-​1020-x (2019).](https://doi.org/10.1007/s12046-018-1020-x)

79. Dhanalakshmi, C. S., Madhu, P., Karthick, A., Mathew, M. & Kumar, R. V. A comprehensive MCDM-based approach using
TOPSIS and EDAS as an auxiliary tool for pyrolysis material selection and its application. Biomass Convers. Biorefinery [https://​](https://doi.org/10.1007/s13399-020-01009-0)
[doi.​org/​10.​1007/​s13399-​020-​01009-0 (2020).](https://doi.org/10.1007/s13399-020-01009-0)

80. Kar, S. & Jha, K. N. Assessing criticality of construction materials for prioritizing their procurement using ANP-TOPSIS. Int. J.
_Constr. Manag._ [https://​doi.​org/​10.​1080/​15623​599.​2020.​17426​37 (2020).](https://doi.org/10.1080/15623599.2020.1742637)

81. Patra, P. & Angira, M. Investigation on dielectric material selection for RF-MEMS shunt capacitive switches using ashby, TOPSIS
and VIKOR. Trans. Electr. Electron. Mater. **[21(2), 157–164. https://​doi.​org/​10.​1007/​s42341-​019-​00162-2 (2020).](https://doi.org/10.1007/s42341-019-00162-2)**

82. Yang, W.-C., Chon, S.-H., Choe, C.-M. & Yang, J.-Y. Materials selection method using TOPSIS with some popular normalization
methods. Eng. Res. Express **[3(1), 015020. https://​doi.​org/​10.​1088/​2631-​8695/​abd5a7 (2021).](https://doi.org/10.1088/2631-8695/abd5a7)**

83. Kumar, P. G., Meikandan, M., Sakthivadivel, D. & Vigneswaran, V. S. Selection of optimum glazing material for solar thermal
applications using TOPSIS methodology. Int. J. Ambient Energy **[42(3), 274–278. https://​doi.​org/​10.​1080/​01430​750.​2018.​15426​](https://doi.org/10.1080/01430750.2018.1542626)**
[26 (2021).](https://doi.org/10.1080/01430750.2018.1542626)

84. de Aires, R. F. & Ferreira, L. A new multi-criteria approach for sustainable material selection problem. Sustainability **14(18),**
[11191. https://​doi.​org/​10.​3390/​su141​811191 (2022).](https://doi.org/10.3390/su141811191)

85. Abishini, A. & Karthikeyan, K. Application of MCDM and Taguchi super ranking concept for materials selection problem.
_Mater. Today_ **[72, 2480–2487. https://​doi.​org/​10.​1016/j.​matpr.​2022.​09.​526 (2022).](https://doi.org/10.1016/j.matpr.2022.09.526)**

86. Kazemian, N. et al. Material selection of intraoral stents for head and neck cancer patients undergoing radiation therapy: A
Multi-criteria multi-physics design approach. Mater. Des. **[225, 111558. https://​doi.​org/​10.​1016/j.​matdes.​2022.​111558 (2023).](https://doi.org/10.1016/j.matdes.2022.111558)**

87. Sharma, V. et al. Multi-criteria decision making methods for selection of lightweight material for railway vehicles. Materials
**[16(1), 368. https://​doi.​org/​10.​3390/​ma160​10368 (2022).](https://doi.org/10.3390/ma16010368)**

88. Remadi, F. D. & Frikha, H. M. The triangular intuitionistic fuzzy numbers CODAS method for solving green material selection
problem. Int. J. Oper. Res. **[46(3), 398–415. https://​doi.​org/​10.​1504/​ijor.​2022.​10049​713 (2023).](https://doi.org/10.1504/ijor.2022.10049713)**

89. Wankhede, S., Pesode, P., Gaikwad, S., Pawar, S. & Chipade, A. Implementing combinative distance base assessment (CODAS)
for selection of natural fibre for long lasting composites. Mater. Sci. Forum **[1081, 41–48. https://​doi.​org/​10.​4028/p-​4pd120 (2023).](https://doi.org/10.4028/p-4pd120)**

90. Zhang, K., Zhan, J. & Yao, Y. TOPSIS method based on a fuzzy covering approximation space: An application to biological
nano-materials selection. Inf. Sci. **[502, 297–329. https://​doi.​org/​10.​1016/j.​ins.​2019.​06.​043 (2019).](https://doi.org/10.1016/j.ins.2019.06.043)**

91. Hafezalkotob, A. & Hafezalkotob, A. Comprehensive MULTIMOORA method with target-based attributes and integrated
significant coefficients for materials selection in biomedical applications. Mater. Des. **[87, 949–959. https://​doi.​org/​10.​1016/j.​](https://doi.org/10.1016/j.matdes.2015.08.087)**
[matdes.​2015.​08.​087 (2015).](https://doi.org/10.1016/j.matdes.2015.08.087)


-----

92. Mousavi-Nasab, S. H. & Sotoudeh-Anvari, A. A comprehensive MCDM-based approach using TOPSIS, COPRAS and DEA as
an auxiliary tool for material selection problems. Mater. Des. **[121, 237–253. https://​doi.​org/​10.​1016/j.​matdes.​2009.​08.​013 (2017).](https://doi.org/10.1016/j.matdes.2009.08.013)**

93. Zhang, H. et al. Materials selection of 3D-printed continuous carbon fiber reinforced composites considering multiple criteria.
_Mater. Des._ **[196, 109140. https://​doi.​org/​10.​1016/j.​matdes.​2020.​109140 (2020).](https://doi.org/10.1016/j.matdes.2020.109140)**

94. Zhang, Q., Hu, J., Feng, J. & Liu, A. A novel multiple criteria decision making method for material selection based on GGPFWA
operator. Mater. Des. **[195, 109038. https://​doi.​org/​10.​1016/j.​matdes.​2020.​109038 (2020).](https://doi.org/10.1016/j.matdes.2020.109038)**

95. Chatterjee, P., Athawale, V. M. & Chakraborty, S. Materials selection using complex proportional assessment and evaluation of
mixed data methods. Mater. Des. **[32(2), 851–860. https://​doi.​org/​10.​1016/j.​matdes.​2010.​07.​010 (2011).](https://doi.org/10.1016/j.matdes.2010.07.010)**

96. Rathod, M. K. & Kanzaria, H. V. A methodological concept for phase change material selection based on multiple criteria decision analysis with and without fuzzy environment. Mater. Des. **[32(6), 3578–3585. https://​doi.​org/​10.​1016/j.​matdes.​2011.​02.​040](https://doi.org/10.1016/j.matdes.2011.02.040)**
(2011).

[97. Wendt, F. Compromise, Peace and Public Justification: Political Morality Beyond Justice (Springer, 2016). https://​doi.​org/​10.​1007/​](https://doi.org/10.1007/978-3-319-28877-2_5)

[978-3-​319-​28877-2_5.](https://doi.org/10.1007/978-3-319-28877-2_5)

98. Zakeri, S. & Konstantas, D. Solving decision-making problems using a measure for information values connected to the equilibrium points (IVEP) MCDM method and Zakeri-Konstantas performance correlation coefficient. Information **13(11), 512.**
[https://​doi.​org/​10.​3390/​info1​31105​12 (2022).](https://doi.org/10.3390/info13110512)

99. Bączkiewicz, A. et al. Comparative analysis of solar panels with determination of local significance levels of criteria using the
mcdm methods resistant to the rank reversal phenomenon. Energies **[14(18), 5727. https://​doi.​org/​10.​3390/​en141​85727 (2021).](https://doi.org/10.3390/en14185727)**

100. Piegat, A. & Sałabun, W. Identification of a multicriteria decision-making model using the characteristic objects method. Appl.
_Comput. Intell. Soft Comput._ **[2014, 14–14. https://​doi.​org/​10.​1155/​2014/​536492 (2014).](https://doi.org/10.1155/2014/536492)**

101. Sałabun, W. The characteristic objects method: a new distance-based approach to multicriteria decision-making problems. J.
_Multi-Crit. Decis. Anal._ **[22(1–2), 37–50. https://​doi.​org/​10.​1002/​mcda.​1525 (2015).](https://doi.org/10.1002/mcda.1525)**

102. Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. The SPOTIS rank reversal free method for multi-criteria decision-making
[support. In 2020 IEEE 23rd International Conference on Information Fusion (FUSION), pp 1–8 (IEEE, 2020). https://​doi.​org/​](https://doi.org/10.23919/FUSION45008.2020.9190347)
[10.​23919/​FUSIO​N45008.​2020.​91903​47](https://doi.org/10.23919/FUSION45008.2020.9190347)

103. Žižović, M., Pamučar, D., Albijanić, M., Chatterjee, P. & Pribićević, I. Eliminating rank reversal problem using a new multiattribute model-the RAFSI method. Mathematics **[8(6), 1015. https://​doi.​org/​10.​3390/​math8​061015 (2020).](https://doi.org/10.3390/math8061015)**

104. Munier, N. A new approach to the rank reversal phenomenon in MCDM with the SIMUS method. Multiple criteria decision
[making, (11), 137–152. https://​bibli​oteka​nauki.​pl/​artic​les/​578600.​pdf (May 2023) (2016).](https://bibliotekanauki.pl/articles/578600.pdf)

105. Wątróbski, J., Bączkiewicz, A., Król, R. & Sałabun, W. Green electricity generation assessment using the CODAS-COMET
method. Ecol. Indic. **[143, 109391. https://​doi.​org/​10.​1016/j.​ecoli​nd.​2022.​109391 (2022).](https://doi.org/10.1016/j.ecolind.2022.109391)**

106. Shekhovtsov, A., Więckowski, J., Kizielewicz, B., & Sałabun, W. Effect of Criteria Range on the Similarity of Results in the COMET
[Method. In 2021 16th Conference on Computer Science and Intelligence Systems (FedCSIS), pp 453–457 (IEEE, 2021). https://​](https://doi.org/10.15439/2021F44)
[doi.​org/​10.​15439/​2021F​44](https://doi.org/10.15439/2021F44)

107. Faizi, S., Sałabun, W., Ullah, S., Rashid, T. & Więckowski, J. A new method to support decision-making in an uncertain environment based on normalized interval-valued triangular fuzzy numbers and comet technique. Symmetry **[12(4), 516. https://​doi.​](https://doi.org/10.3390/sym12040516)**
[org/​10.​3390/​sym12​040516 (2020).](https://doi.org/10.3390/sym12040516)

108. Palczewski, K. & Sałabun, W. Identification of the football teams assessment model using the COMET method. Procedia Comput.
_Sci._ **[159, 2491–2501. https://​doi.​org/​10.​1016/j.​procs.​2019.​09.​424 (2019).](https://doi.org/10.1016/j.procs.2019.09.424)**

109. Chatterjee, P. & Chakraborty, S. Material selection using preferential ranking methods. Mater. Des. **[35, 384–393. https://​doi.​org/​](https://doi.org/10.1016/j.matdes.2011.09.027)**

[10.​1016/j.​matdes.​2011.​09.​027 (2012).](https://doi.org/10.1016/j.matdes.2011.09.027)

110. Hatefi, S. M., Asadi, H., Shams, G., Tamošaitienė, J. & Turskis, Z. Model for the sustainable material selection by applying integrated Dempster-Shafer evidence theory and additive ratio assessment (ARAS) method. Sustainability **[13, 10438. https://​doi.​](https://doi.org/10.3390/su131810438)**
[org/​10.​3390/​su131​810438 (2021).](https://doi.org/10.3390/su131810438)

111. Liu, H. C., You, J. X., Zhen, L. & Fan, X. J. A novel hybrid multiple criteria decision making model for material selection with
target-based criteria. Mater. Des. **[60, 380–390. https://​doi.​org/​10.​1016/j.​matdes.​2014.​03.​071 (2014).](https://doi.org/10.1016/j.matdes.2014.03.071)**

112. Toledo, H., Martínez-Gómez, J. & Nicolalde, J. F. Selection of rear axle tip alternative material of a car by multi-criteria means.
_Int. J. Math. Oper. Res._ **[21(1), 46–66. https://​doi.​org/​10.​1504/​IJMOR.​2022.​120320 (2022).](https://doi.org/10.1504/IJMOR.2022.120320)**

### Author contributions
S.Z.: Conceptualization, Methodology, Validation, Formal analysis, Writing—Original Draft, Visualization. P.C.:
Resources, Investigation, Data Curation, Writing—Review & Editing. D.K.: Supervision, Writing—Original Draft,
Writing—Review & Editing. F.E.: Writing- Reviewing and Editing, Validation.

### Competing interests
The authors declare no competing interests.

### Additional information
**Correspondence and requests for materials should be addressed to S.Z.**

**Reprints and permissions information is available at www.nature.com/reprints.**

**Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and**
institutional affiliations.

**Open Access This article is licensed under a Creative Commons Attribution 4.0 International**
License, which permits use, sharing, adaptation, distribution and reproduction in any medium or
format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the
Creative Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from
[the copyright holder. To view a copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.](http://creativecommons.org/licenses/by/4.0/)

© The Author(s) 2023


-----

