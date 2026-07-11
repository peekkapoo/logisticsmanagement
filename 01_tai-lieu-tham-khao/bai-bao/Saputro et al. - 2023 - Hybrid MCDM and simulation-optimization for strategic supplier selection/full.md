# Hybrid MCDM and simulation-optimization for strategic supplier selection

Thomy Eko Saputro <sup>a,∗</sup>, Gonçalo Figueira <sup>b</sup>, Bernardo Almada-Lobo <sup>b</sup>

![](images/f5465a549b27af4f48d23409a228f43db529f3ad2e9048f21fba60f4009c8ff2.jpg)

<sup>a</sup> University of Muhammadiyah Malang, Jl. Raya Tlogomas 246, 65144 Malang, Indonesia

<sup>b</sup> INESC-TEC, Faculty of Engineering, University of Porto, s/n, R. Dr. Roberto Frias, 4200-465 Porto, Portugal

## A R T I C L E I N F O

Keywords: Supplier selection Inventory management Multi-criteria decision-making Simulation-optimization Supply disruptions

## A B S T R A C T

Supplier selection for strategic items requires a comprehensive framework dealing with qualitative and quantitative aspects of a company’s competitive priorities and supply risk, decision scope, and uncertainty. In order to address these aspects, this study aims to tackle supplier selection for strategic items with a multi-sourcing, taking into account multi-criteria, incorporating uncertainty of decision-makers judgment and supplier–buyer parameters, and integrating with inventory management which the past studies have not addressed well. We develop a novel two-phase solution approach based on integrated multi-criteria decisionmaking (MCDM) and multi-objective simulation-optimization (S-O). First, MCDM methods, including fuzzy AHP and interval TOPSIS, are applied to calculate suppliers’ scores, incorporating uncertain decision makers judgment. S-O then combines the (quantitative) cost-related criteria and considers supply disruptions and uncertain supplier–buyer parameters. By running this approach on data generated based on previous studies, we evaluate the impact of the decision maker’s and the objective’s weight, which are considered important in supplier selection.

## 1. Introduction

Managing the supply of strategic items can have a significant impact on a company’s profit and should therefore be sourced from the right suppliers, with the right price and quantity, and at the right time. Selecting the right supplier relies on several processes, such as iden tification of criteria (Aissaoui et al., 2007; de’Boer et al., 2001; Saputro et al., 2021), which are typically conflicting (Weber et al., 2000). A set of various criteria composed of qualitative and quantitative should be considered when evaluating suppliers (related to the main competi tive priorities i.e., price, quality, delivery, flexibility, relationship, and service) (Yadav & Sharma, 2016).

Furthermore, the complexity of supply and rapid change of the global market have compelled companies to focus on risk mitigation. Mitigating risk is crucial for strategic items since the impact can be tremendous to the entire supply chain’s operations. Some of the potential supply risks might come from suppliers due to delivery fail ures, quality problems, discontinuity of supply, or disruptions (Zsidisin, 2003). To create supply chain resilience, supplier selection processes have to be redesigned. For instance, the adoption of risk-related selec tion criteria (Awasthi et al., 2018; Igoulalene et al., 2015; Rajesh & Ravi, 2015) and multi-sourcing (Haleh & Hamidi, 2011), as well as the integration of inventory management (Firouz et al., 2017; Keskin et al., 2010; Saputro et al., 2020) can be important levers for risk mitigation in supplier selection.

The supplier selection framework has been formalized in the literature based on four dimensions: selection criteria, sourcing strategy, decision scope, and decision environment (Saputro et al., 2022). However, the problem concerning those four dimensions becomes more challenging when dealing with strategic items. In other words, supplier selection problems for strategic items involve considering comprehensive criteria, which generally include both qualitative and qualitative criteria as well as risk factors, ensuring supply continuity with multi sourcing, integrating a broader scope (i.e., order allocation and inventory management), and incorporating different sources of uncertainty.

Several studies have focused on supplier selection for strategic items under the integration of order allocation. Suppliers were eval uated by decision makers under multi-criteria. Using human judgment, evaluating suppliers can lead to vague judgment, particularly when the exact values of the evaluated alternatives are unavailable. In this uncertain decision environment, DMs’ opinions or judgments need to be perceived realistically to avoid potentially misleading decision making. It requires transforming linguistic variables into uncertain numerical values (i.e., fuzzy or interval) (Haeri & Rezaei, 2019). Singh (2014), Ayhan and Kilic (2015), Hamdan and Cheaitou (2017), Cheraghalipour and Farsad (2018), Gören (2018), and Kilic and Yalcin (2020) considered uncertain decision maker’s judgment in supplier selection. Still, these studies do not consider uncertainty in terms of supplier–buyer parameters (i.e., buyer’s demand, supplier’s capacity, quality, and delivery).

Hasan et al. (2020) and Kaur and Prakash Singh (2021) incorporated risk factors into supplier selection. Nevertheless, these studies do not simultaneously consider uncertainty and risk factors regard ing the delivery delay, imperfect quality, and disruptions. Moreover, these studies do not accurately consider risk factors and integration of disruptions risk mitigation strategies via inventory management.

The studies on supplier selection have been tackled by using multi criteria decision-making (MCDM) approaches, including analytical hi erarchy process (AHP), analytic network process (ANP), and Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) (Chai et al., 2013). However, although these methods can handle various criteria, a standalone MCDM method cannot properly evaluate the im plications of multi-sourcing. Therefore, several studies have employed a two-phase solution approach, particularly for strategic items, initialized by evaluating suppliers’ performance under multi-criteria and then op timizing order allocation of multiple suppliers (Gören, 2018; Hamdan & Cheaitou, 2017; Kilic & Yalcin, 2020). Nevertheless, this solution approach could not accurately represent the nature of disruptions and handle its impacts on parameters (i.e., supplier’s lead time or delivery) which change dynamically according to the disruptions characteristic.

To fill the literature gaps, our study has a twofold contribution focusing on supplier selection for strategic items. First, we propose a comprehensive model by considering criteria holistically, including risk factors (i.e., imperfect quality, disruptive lead time, disruptions) and integrating inventory management. The proposed model also addresses the different sources of uncertainty to accommodate more realistic DMs’ judgment and supplier–buyer parameters (e.g., buyer’s demand, supplier’s lead time, and imperfect quality rate). Second, we develop a novel two-phase solution approach using hybrid MCDM and simula tion optimization to solve the proposed model. Two MCDM methods, namely fuzzy AHP and interval TOPSIS are employed to incorporate DMs’ uncertainty in perceiving their opinion when determining the criteria weight and evaluating suppliers, respectively. In addition, the simulation–optimization tackles uncertain supplier-related parameters and disruptions simultaneously. For instance, the dynamic change of a parameter (e.g., supplier’s lead time) resulting from the disruptions is considered while optimizing supplier and inventory decisions.

The remainder of this paper is organized as follows. Section 2 briefly reviews relevant literature on strategic supplier selection studies and their solution approaches. The problem’s context and model formulation are defined in Section 3. Section 4 describes the proposed solution approach, including MCDM and simulation–optimization. Finally, Section 5 gives an example to illustrate the application of the proposed solution approach. In addition, we provide sensitivity analysis on objectives and DMs weights.

## 2. Literature review

## 2.1. Strategic supplier selection

Studies on supplier selection have grown rapidly in the supply chain management literature. It becomes a critical concern for companies when the selection is focused on purchases that have a strategic role and impact on profitability and operations, the so-called strategic items (Kraljic, 1983). Therefore, supplier selection is different in terms of selection criteria, sourcing strategy, decision scope, and decision environment, depending on the types of items. Saputro et al. (2022) defined the characteristics of supplier selection for different types of items according to the dimensions as mentioned earlier.

Supplier selection for strategic items is designed for a single-period basis in which the supply is managed under multi-sourcing. Under multi-sourcing, order allocation needs to be determined properly while selecting suppliers. For the items with a high impact on profit and operations, and high supply risk, such as this type of item, supplier selection criteria, including monetary and non-monetary based, are important to be taken into account (Saputro et al., 2022).

Our literature review focuses on supplier selection for strategic items from the studies published in reputable journals between 2014 and 2022. Recent literature has focused on strategic supplier selection integrating order allocation. Singh (2014) and Toffano et al. (2022) determined supplier selection and order allocation by considering qual ity, price, delivery, and consistency. Ayhan and Kilic (2015) evaluated suppliers according to quality, price, delivery, and after-sales performance. Hamdan and Cheaitou (2017), Kilic and Yalcin (2020), and Feng and Gong (2020) taken into account environmental aspects into supplier selection. Besides environmental, other aspects, including social and economic, have also been incorporated into supplier selection (Bektur, 2020; Cheraghalipour & Farsad, 2018; Ghadimi et al., 2018; Gören, 2018; Kellner & Utz, 2019; Moheb-Alizadeh & Handfield, 2019). Hasan et al. (2020), and Kaur and Prakash Singh (2021) attempted to mitigate disruptions risk in supplier selection by consid ering suppliers’ ability to adapt to the disruptions, such as rerouting, restorative capacity, agility, and cyber security risk management.

Among the existing types of items, supplier selection for strategic items is challenging due to its supply risks which can result in signif icant profit and operational loss, as well as its decision environment, which contains uncertainty in terms of buyer–supplier parameters and decision maker’s judgment (Saputro et al., 2022). However, most of the studies mentioned earlier do not incorporate disruptions risk and the different sources of uncertainty in supplier selection.

Table 1 summarizes the main features of the strategic supplier selection problems, including decision scope, sourcing strategy, selection criteria, and various sources of uncertainty. Some of those studies have addressed the aforementioned aspects but with some limitations.

## 2.2. Supplier selection approaches

The past studies have proposed a two-phase solution approach deal ing with multi-sourcing and incorporating qualitative and quantitative criteria, as well as DMs’ judgment uncertainty for a comprehensive decision-making process. Typically, supplier evaluation with respect to the qualitative criteria is performed in the first phase to calculate suppliers’ scores. Then, in the second phase, final decisions regarding supplier selection and order allocation are determined considering both qualitative and quantitative criteria.

The two-phase solution approach generally employs MCDM and optimization, subsequently. Singh (2014) tackled supplier selection problem using fuzzy TOPSIS and mixed-integer linear programming (MILP). Ayhan and Kilic (2015) proposed an integrated approach using fuzzy AHP to determine criteria weight and MILP to determine supplier selection and order allocation. Hamdan and Cheaitou (2017) applied integrated AHP, fuzzy TOPSIS, and mathematical programming to solve supplier selection and order allocation with a multi-objective model. In the first phase, AHP and fuzzy TOPSIS were used to determine criteria weight and supplier score, respectively. Cheraghalipour and Farsad (2018) focused on integrated supplier selection considering disruption risk. However, they did not consider the impact of disruptions and did not incorporate uncertainty l. The best–worst method was employed to determine the criteria weight and calculate the suppliers’ score. The final decisions were determined via revised multi-choice goal pro gramming. Gören (2018) introduced integrated fuzzy decision-making trial and evaluation laboratory (DEMATEL), Taguchi loss function, and mathematical programming. Criteria weight and supplier score were calculated using fuzzy DEMATEL and Taguchi loss functions. However, suppliers’ performance based on a percentage value can be difficult to be perceived and estimated by DMs for intangible criteria using Taguchi loss function. Kilic and Yalcin (2020) integrated intuitionistic fuzzy TOPSIS with fuzzy goal programming to tackle supplier selection in an uncertain environment. Feng and Gong (2020) proposed

Table 1  
Problem features of supplier selection.

<table><tr><td>Study</td><td>Sourcing strategy</td><td>Integration</td><td>Objective</td><td>Criteria</td><td>Risks</td><td>Uncertainty</td></tr><tr><td>Singh (2014)</td><td>M-S</td><td>OA</td><td>Single</td><td>Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Ayhan and Kilic (2015)</td><td>M-S</td><td>OA</td><td>Single</td><td>Ql, Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Hamdan and Cheaitou (2017)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Gören (2018)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Cheraghalipour and Farsad (2018)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>-</td></tr><tr><td>Moheb-Alizadeh and Handfield (2019)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>-</td></tr><tr><td>Kellner and Utz (2019)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>√</td><td>-</td></tr><tr><td>Kilic and Yalcin (2020)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Feng and Gong (2020)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>-</td></tr><tr><td>Bektur (2020)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Hasan et al. (2020)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Qn</td><td>-</td><td>DMs judgment</td></tr><tr><td>Kaur and Prakash Singh (2021)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Ql, Qn</td><td>√</td><td>DMs judgment</td></tr><tr><td>Toffano et al. (2022)</td><td>M-S</td><td>OA</td><td>Multi</td><td>Qn</td><td>-</td><td>-</td></tr><tr><td>This study</td><td>M-S</td><td>OA, I</td><td>Multi</td><td>Ql, Qn</td><td>√</td><td>DMs judgment &amp; Supplier-buyer parameters</td></tr></table>

Abbreviation:  
M-S: Multi Sourcing — OA: Order Allocation — Ql: Qualitative — Qn: Quantitative — I: Inventory Management — DMs: Decision Makers’.

Problem features of supplier selection.

<table><tr><td>Study</td><td>Approach</td></tr><tr><td>Singh (2014)</td><td>MCDM, Optimization</td></tr><tr><td>Ayhan and Kilic (2015)</td><td>MCDM, Optimization</td></tr><tr><td>Hamdan and Cheaitou (2017)</td><td>MCDM, Optimization</td></tr><tr><td>Gören (2018)</td><td>MCDM, Optimization</td></tr><tr><td>Cheraghalipour and Farsad (2018)</td><td>MCDM, Optimization</td></tr><tr><td>Moheb-Alizadeh and Handfield (2019)</td><td>Optimization</td></tr><tr><td>Kellner and Utz (2019)</td><td>Optimization</td></tr><tr><td>Kilic and Yalcin (2020)</td><td>MCDM, Optimization</td></tr><tr><td>Feng and Gong (2020)</td><td>MCDM, Optimization</td></tr><tr><td>Bektur (2020)</td><td>MCDM, Optimization</td></tr><tr><td>Hasan et al. (2020)</td><td>Optimization</td></tr><tr><td>Kaur and Prakash Singh (2021)</td><td>MCDM, Optimization</td></tr><tr><td>Toffano et al. (2022)</td><td>Optimization</td></tr><tr><td>This study</td><td>MCDM, Simulation-Optimization</td></tr></table>

Abbreviation:  
MCDM: Multi-Criteria Decision Making.

Integrated linguistic entropy weight method and multi-objective pro gramming model for supplier selection and order allocation. Bektur (2020) evaluated suppliers under multi-criteria by using Fuzzy Analytic Hierarchy Process (F-AHP) and fuzzy Preference Ranking Organization Method for Enrichment Evaluation (F-PROMETHEE). Augmented ?? - constraint (AUG- MECON) method and LP-metrics are used to optimize supplier selection and order allocation. Hasan et al. (2020) optimized supplier selection by using the integration of Fuzzy TOPSIS and multi choice goal programming (MCGP). Kaur and Prakash Singh (2021) solved supplier selection and order allocation using F-AHP and TOPSIS integrated with mixed integer programming. The solution approach proposed by the studies depicts evaluation redundancy with respect to price or cost addressed in both phases (e.g., Cheraghalipour and Farsad 2018, Gören 2018, Hamdan and Cheaitou 2017). Table 2 shows the different supplier selection approaches from the past studies.

Simulation is indeed a flexible modeling paradigm, which, com bined with optimization (S-O), allows to approach a wide variety of complex systems in uncertain environments (Tordecilla et al., 2021; Wang & Shi, 2013), including production planning, transport planning, inventory management, production–distribution planning, and supply chain design (Bang & Kim, 2010). Metaheuristics are most commonly used to address these complex problems, as optimality is frequently unattainable. Combining metaheuristics with simulation can be done in different procedures depending on the simulation purpose and hi erarchical structures (Figueira & Almada-Lobo, 2014). For example, simulation can be used to evaluate the performance of various solu tions, refine or extend parameters so that a given analytical model can be enhanced, or generate solutions (Figueira & Almada-Lobo, 2014). Our case is the second, as the analytical model allows us to avoid an excessive number of simulations and hence save computational time.

Our study’s main contribution is to present a comprehensive multi objective model by incorporating uncertainty of DMs’ judgment and supplier–buyer parameters and integrating the decision scope with order allocation and inventory management. Besides, our study also contributes to a novel two-phase solution approach using MCDM and S-O. More specifically, we proposed fuzzy AHP and interval TOPSIS; which can be used to deal with qualitative criteria and supplier evaluation under uncertain DMs’ judgment (Liu et al., 2020). These methods are very useful for the selection of the best alternative and the ranking of different alternative (Dogan et al., 2020; Kiracı & Akan, 2020). For the final decision-making, S-O is used to optimize the decisions under multi-objectives. Also, it explicitly addresses uncertain supplier–buyer parameters or other quantitative criteria with discrete-event simulation and incorporates the disruptions information to improve the decisions. Therefore, this problem formulation is distinctive from the previous studies, as some criteria typically considered qualitative and more abstract are here quantified and simulated.

## 3. Model development

We study supplier selection integrated with inventory management for a single item and single-period based on a multi-sourcing strategy. We extend the model by incorporating imperfect quality, disruptions, and vehicle capacity. Suppliers are selected by considering multi-criteria classified into two objective functions, namely, maximizing a total value of purchasing (TVP) and minimizing total costs (TC).

We consider a network consisting of ?? suppliers $( j \in J = ( 1 , \ldots , m ) )$ and one buyer that has ?? manufacturing plants $( i \in I \ = \ ( 1 , \ldots , n ) )$ in different locations. The demand of each plant $i ,$ which follows a normal distribution, is met through the material supply from one or more suppliers ?? that are selected $( X _ { j } ~ = ~ 1 )$ , with certain amounts $( Y _ { i j } )$ . The full notation of parameters and decision variables is shown in Table 3.

In order to manage inventory, a (??, ??) policy is applied by placing an order with a fixed quantity (??), as soon as the inventory level drops to or below a reorder point (??). Order quantity $( Q _ { i j } )$ and reorder point $( R _ { i j } )$ have a specific amount since the order allocation of each plant is specific for each selected supplier $( Y _ { i j } )$ , the so-called inventory compartmentalization.

Table 3  
Input parameters and decision variables.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">Indices</td></tr><tr><td>i</td><td>: index for plant, i = 1, 2, ..., n</td></tr><tr><td>j</td><td>: index for supplier, j = 1, , ..., m</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td>E[Di]</td><td>: Expected annual demand of plant i</td></tr><tr><td>ai</td><td>: External failure costs per unit for imperfect items of plant i</td></tr><tr><td>oi</td><td>: Setup costs of plant i</td></tr><tr><td>hi</td><td>: Holding costs per unit for perfect items of plant i</td></tr><tr><td>h&#x27;i</td><td>: Holding costs per unit for imperfect items of plant i</td></tr><tr><td>si</td><td>: Shortage costs per unit and per time of plant i</td></tr><tr><td>SSj</td><td>: Score of supplier j, which refers to a closeness coefficient CCk</td></tr><tr><td>fj</td><td>: Fixed annual contractual costs of supplier j</td></tr><tr><td>cj</td><td>: Purchasing costs per unit of supplier j</td></tr><tr><td>kj</td><td>: Rate of imperfect quality for supplier j</td></tr><tr><td>bj</td><td>: Annual supply capacity of supplier j</td></tr><tr><td>uj</td><td>: Capacity of a TL vehicle for supplier j</td></tr><tr><td>θj</td><td>: Disruption frequency rate for supplier j</td></tr><tr><td>vj</td><td>: Disruption length for supplier j</td></tr><tr><td>E[LTDij]</td><td>: Expected lead time demand between plant i and supplier j</td></tr><tr><td>η[LTDij, Rij]</td><td>: Standardized loss function between plant i and supplier j</td></tr><tr><td>pij</td><td>: Fixed transportation costs per replenishment from supplier j to plant i</td></tr><tr><td>rij</td><td>: Transportation costs per mile and per replenishment from supplier j to plant i</td></tr><tr><td>dij</td><td>: Distance between plant i and supplier j</td></tr><tr><td>lij</td><td>: Lead time between plant i and supplier j</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td>Xj</td><td>: 1, if supplier j is selected; 0, otherwise</td></tr><tr><td>Yij</td><td>: Purchase amount allocated by plant i to supplier j</td></tr><tr><td>Qij</td><td>: Order quantity of plant i to supplier j</td></tr><tr><td>Rij</td><td>: Reorder point of plant i to supplier j</td></tr></table>

We also consider supply disruptions and their related risk to the entire supply network accurately through the integration of inventory management, such as delivery delays. When deliveries are delayed due to disruptions, the actual observed lead time and corresponding lead time demand will be higher than the stated lead time. It is critical to mitigate their impact by avoiding more stock outs through proper inventory management. Thus, we determine the reorder points $( R _ { i j } )$ by incorporating an adjusted lead time $( l _ { i j } ^ { \prime } )$ that takes those disruptions into consideration. This is done through refinements undertaken by the proposed solution approach detailed in Section 4.2.2.

## 3.1. Total value of purchasing

The total value of purchasing (TVP) is the consideration in supplier selection of the maximization of the firm’s long-term value. Rather than focusing on pure monetary-based values, TVP focuses on the advantage resulting from every unit purchase allocated to the selected suppliers. Since sourcing experiences from every unit purchase can affect a firm’s willingness to buy and perceptions toward suppliers, TVP relies on purchase quantity $( Y _ { i j } )$ . In this context, TVP is perceived based on the non-monetary criteria, which contribute to an intangible value of advantages. This includes service (C1), relationship (C2), and flexibility (C3).

In order to calculate TVP, we assess suppliers based on the aforementioned criteria. The supplier’s performance score $( S S _ { j } )$ is a function of those criteria $( S S _ { j } = C C _ { k } = f ( C 1 _ { k } , C 2 _ { k } , C 3 _ { k } )$ , where $k = j )$ which is derived through multi-criteria decision-making approaches. Finally, TVP is maximized by using the following expression.

$$
\text { Max   } Z 1 (\text { TVP }) = \sum_ {i} ^ {n} \sum_ {j} ^ {m} S S _ {j} Y _ {i j}\tag{1}
$$

## 3.2. Total costs

Total costs (TC) are considered monetary-based values, which consist of contractual and purchasing costs (2a), inventory costs ((2b-1), (2b-2)), transportation costs (2c), external failure, and imperfect holding costs (2d).

$$
\text { Min   } Z 2 (\mathrm{TC}) = \sum_ {j = 1} ^ {m} f _ {j} X _ {j} + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} c _ {j} Y _ {i j}\tag{2a}
$$

$$
+ \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \frac {o _ {i} Y _ {i j}}{Q _ {i j} (1 - E [ k _ {j} ])} + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} h _ {i} \left(\frac {Q _ {i j} (1 - E [ k _ {j} ])}{2} + R _ {i j} - E [ L T D _ {i j} ]\right)\tag{2b-1}
$$

$$
+ \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} s _ {i} \eta (L T D _ {i j}, R _ {i j}) \frac {Y _ {i j}}{Q _ {i j} (1 - E [ k _ {j} ])}\tag{2b-2}
$$

$$
\sum_ {i} ^ {n} \sum_ {j} ^ {m} (p _ {i j} + r _ {i j} d _ {i j}) \lceil \frac {Q _ {i j}}{u _ {j}} \rceil Y _ {i j}
$$

$$
+ \sum_ {i = 1} ^ {\infty} \sum_ {j = 1} ^ {\infty} \frac {(p _ {i j} + p _ {i j} u _ {i j}) | _ {u _ {j}} | _ {i j}}{Q _ {i j} (1 - E [ k _ {j} ])}\tag{2c}
$$

$$
+ \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} a _ {i} Y _ {i j} E [ k _ {j} ] + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} h _ {i} ^ {\prime} Q _ {i j} E [ k _ {j} ]\tag{2d}
$$

Fixed contractual costs $( f _ { j } )$ incur once a contract is awarded to the selected supplier. Moreover, each plant has to pay variable purchasing costs $( c _ { i } )$ for the order allocated to a supplier.

Some other costs also have to be paid throughout the supply, in cluding inventory and transportation. More specifically, transportation cost for each delivery is charged according to vehicle capacity $( u _ { j } ) _ { i }$ considering mileage $( r _ { i j } )$ and fixed costs $( { p } _ { i j } )$ . Total inventory costs are calculated according to setup costs $\left( o _ { i } \right)$ and inventory carrying costs $\left( h _ { i } \right)$ ). Additionally, shortage costs incur if stock outs occur at plant $( s _ { i } , i \in I )$ . Due to their different distance and location, a lead time for each pair of supply (supplier-plant) $( l _ { i j } )$ is specific. $\eta ( . , . )$ in (2b-2) represents the standard loss function.

The average annual transportation costs (2c) are calculated according to the vehicle capacity $u _ { j } .$ The costs per vehicle are measured based on the fixed vehicle charge $( p _ { i j } )$ and mileage costs $( r _ { i j } )$ . In $( \mathrm { 2 c } ) , d _ { j }$ represents the distance between suppliers and plants, which is measured according to Euclidean measure associated with suppliers coordinates $d _ { j }$ and plants’ coordinates $d _ { i } .$

We also consider a quality risk by incorporating suppliers’ quality variability and its associated costs. In this regard, the incoming material from a supplier includes a specific rate of imperfect quality $( k _ { j } ) _ { \ l }$ . As a result, plants have to spend a specific holding cost $( h _ { i } ^ { \prime } )$ for these imperfect items. Additionally, external failure costs $( a _ { i } )$ incurs due to liability or complaints by customers acquiring imperfect items. The expected imperfect rate $( E [ k _ { j } ] )$ is taken into account as a function of the inventory, transportation, and external failure costs. $E [ k _ { j } ]$ is computed according to a particular distribution; more specifically, it is perceived as uniformly distributed.

## 3.3. Constraints

The main constraints regard capacity and demand fulfillment.

Constraint (3) ensures that the order allocated to the selected sup pliers $Y _ { i j }$ must satisfy the demand in each plant $E [ D _ { i } ]$

$$
\sum_ {j = 1} ^ {m} Y _ {i j} = E [ D _ {i} ], \quad \forall i \in I\tag{3}
$$

Due to the suppliers’ capacity constraint, the order allocation $Y _ { i j }$ should not exceed their capacity $b _ { j }$ .

$$
\sum_ {i = 1} ^ {n} Y _ {i j} \leq b _ {j} X _ {j}, \quad \forall j \in J\tag{4}
$$

Finally, constraint (5) represents non-negativity and binary decision variables.

$$
Y _ {i j} \geq 0, Q _ {i j} \geq 0, X _ {j} = 0 o r 1, \forall i \in I, \forall j \in J\tag{5}
$$

![](images/6470da858161d4736af68077dac8d4107bf11124f499744db75dec7330b7a269.jpg)  
Fig. 1. Two-phase solution approach: MCDM and simulation–optimization.

Table 4  
Linguistic variables for the importance of the criterion.

<table><tr><td>Linguistic variables</td><td>Saaty&#x27;s scale</td><td>TFN</td></tr><tr><td>Equally important</td><td>1</td><td>1, 1, 1</td></tr><tr><td>Weakly or slightly more important</td><td>2</td><td>1, 2, 3</td></tr><tr><td>Moderately more important</td><td>3</td><td>2, 3, 4</td></tr><tr><td>Moderately plus more important</td><td>4</td><td>3, 4, 5</td></tr><tr><td>Strongly more important</td><td>5</td><td>4, 5, 6</td></tr><tr><td>Strongly plus more important</td><td>6</td><td>5, 6, 7</td></tr><tr><td>Strongly very more important</td><td>7</td><td>6, 7, 8</td></tr><tr><td>Very, very strongly more important</td><td>8</td><td>7, 8, 9</td></tr><tr><td>Absolutely more important</td><td>9</td><td>8, 9, 9</td></tr></table>

## 4. Proposed approach

In order to solve the problem, a two-phase solution approach is developed integrating MCDM and simulation–optimization. In the first phase, we focus on suppliers’ evaluation based on the qualitative crite ria. We determine the criteria weight using fuzzy AHP and calculate the supplier score using interval TOPSIS. Then, supplier scores are included into the objective function depicted in Eq. (1), to be optimized at the second phase.

After multi-criteria evaluation, the second phase focuses on solving the multi-objective mathematical model defined in Section 3, inte grating supplier selection, order allocation, and inventory manage ment. Simulation–optimization is developed to solve this phase. The two-phase solution approach in this study is illustrated in Fig. 1.

## 4.1. Multi-criteria decision-making

First, criteria weights are determined using fuzzy AHP. Criteria are given different importance by DMs which is perceived using linguistic variables. The linguistic variables are then transformed into its respec tive triangular fuzzy numbers (TFN) for each Saaty’s scale shown in Table 4.

Second, alternatives are evaluated by DMs under each criterion using linguistic variables. Then, DMs judgment is transformed into an interval value shown in Table 5. To calculate the score of alternatives, interval TOPSIS is employed.

## 4.1.1. Fuzzy AHP

AHP has been widely used for a wide area of decision-making problems due to its advantages: (i) it can be used not only to assess relative criteria weights but also to assess the performance of alter natives through pairwise comparisons, (ii) it can handle both tangible and intangible attributes, (iii) it is suitable for a hierarchical structure of criteria (fundamental components and inter-dependencies) (Zardar et al., 2015).

Table 5  
Linguistic variables for the rating of the alternative

<table><tr><td>Linguistic variable</td><td>Interval number</td></tr><tr><td>Very Poor (VP)</td><td>0, 1</td></tr><tr><td>Poor (P)</td><td>1, 3</td></tr><tr><td>Medium Poor (MP)</td><td>3, 4</td></tr><tr><td>Fair (F)</td><td>4, 5</td></tr><tr><td>Medium Good (MG)</td><td>5, 6</td></tr><tr><td>Good (G)</td><td>6, 9</td></tr><tr><td>Very Good (VG)</td><td>9, 10</td></tr></table>

Table 6  
The algebraic operations of fuzzy numbers.

<table><tr><td>Fuzzy operation</td><td>Fuzzy formula</td><td>Calculation operation</td></tr><tr><td>Addition</td><td> $\tilde{a}_{1} \oplus \tilde{a}_{1}$ </td><td> $(l_{1} + 1_{2}, m_{1} + m_{2}, u_{1} + u_{2})$ </td></tr><tr><td>Subtraction</td><td> $\tilde{a}_{1} \ominus \tilde{a}_{1}$ </td><td> $(l_{1} + u_{2}, m_{1} + m_{2}, u_{1} + l_{2})$ </td></tr><tr><td>Multiplication</td><td> $\tilde{a}_{1} \otimes \tilde{a}_{1}$ </td><td> $(l_{1}.1_{2}, m_{1}.m_{2}, u_{1}.u_{2})$ </td></tr><tr><td>Division</td><td> $\frac{1}{\tilde{a}_{1}}$ </td><td> $(\frac{1}{u_{1}}, \frac{1}{m_{1}}, \frac{1}{l_{1}})$ </td></tr></table>

To deal with qualitative, imprecise information or even incomplete structures decision problems, fuzzy set theory is employed as a modeling tool for complex systems that can be controlled by humans but are not easy to define exactly. It provides a sensible way to represent vague, ambiguous, and imprecise input of knowledge. Decision makers are usually more confident to perceive interval judgments rather fixed value (crisp) judgments when their opinions can be explicit due to fuzzy nature of evaluation process.

According to fuzzy set theory, crisp values are transformed into fuzzy numbers. A triangular fuzzy number (TFN) is widely used as fuzzy numbers. It involves lower, middle, and upper values.

Definition 1. A fuzzy number ?? on $R \in ( - \infty , + \infty )$ is defined to be a fuzzy triangular number if its membership function $\mu _ { m } : R \to [ 0 , 1 ]$ is equal to:

$$
\mu_ {m} (x) = \left\{ \begin{array}{l l} \frac {x}{m - l} - \frac {l}{m - l}, & \text { if } x \in [ l, m ] \\ \frac {x}{m - u} - \frac {l}{m - l}, & \text { if } x \in [ m, u ] \\ 0, & \text { otherwise } \end{array} \right.\tag{6}
$$

In Eq. (6)?? and ?? stand for the lower and upper value of fuzzy number ??, respectively, and ?? represents the middle value, where $l \leq m \leq u .$ A TFN, expressed in Eq. (6), is denoted as (??, ??, ??). The basic operations of TFNs are defined in Table 6.

The deficiency of AHP to deal with the imprecision and subjectiveness in the pairwise comparison process has been improved in fuzzy

AHP (Demirel et al., 2008). In this study, fuzzy AHP proposed by Chang (1996) is adopted to determine criteria weight.

Let $C = \{ C _ { 1 } , C _ { 2 } , \dots , C _ { n } \} ( j = 1 , 2 , \dots , n )$ represent the element of sup plier selection criteria. Thus, criteria weight is determined according to the following steps:

Step 1. Construct pairwise comparison matrix for each pair of criteria according to the linguistic variables shown in Table 4.

Step 2. Transform the matrix into triangular fuzzy numbers (TFN) (c.f. Table 4) denoted by ${ M _ { g } } _ { i } ^ { j } , j \in N$

Step 3. Calculate the value of fuzzy synthetic with respect to the ??th criterion using

$$
S _ {i} = \sum_ {j = 1} ^ {n} M _ {g i} ^ {j} \otimes \left[ \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} M _ {g i} ^ {j} \right] ^ {- 1}\tag{7}
$$

where

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} M _ {g i} ^ {j} = \left(\sum_ {i = 1} ^ {m} l _ {i}, \sum_ {i = 1} ^ {m} m _ {i}, \sum_ {i = 1} ^ {m} u _ {i}\right) \\ \left[ \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} M _ {g i} ^ {j} \right] ^ {- 1} = \left(\frac {1}{\sum_ {i = 1} ^ {m} u _ {i} , \sum_ {i = 1} ^ {m} m _ {i} , \sum_ {i = 1} ^ {m} l _ {i}}\right) \end{array}
$$

Step 4. Determine the degree of possibility of $M _ { 2 ( l , m , u ) } \geq M _ { 1 ( l , m , u ) }$ using

$$
V (M _ {2} \geq M _ {1}) = \sup _ {y \geq x} \lfloor m i n (\mu_ {M _ {1}} (x), \mu_ {M _ {2}} (y)) \rfloor\tag{8}
$$

$$
\begin{array}{l} V (M _ {2} \geq M _ {1}) = h g t (\mu_ {M _ {1}} \cap \mu_ {M _ {2}}) \\ = \mu_ {M _ {2}} (d) = \left\{ \begin{array}{l l} 1, & \text { if } m _ {2} \geq m _ {1} \\ 0, & \text { if } l _ {1} \geq u _ {2} \\ \frac {l _ {1} - u _ {2}}{(m _ {2} - u _ {2}) - (m _ {1} - l _ {1})}, & \text { otherwise } \end{array} \right. \end{array}
$$

Step 5. Define a convex fuzzy number as

$$
V (F \geq F _ {1}, F _ {2}, \dots , F _ {k}) = \min V (F \geq F _ {i}), i = 1, 2, \dots , k\tag{9}
$$

$$
\begin{array}{l} V (F _ {i}) = \min V (F _ {i} \geq F _ {k}) = W _ {i} ^ {\prime}, k = 1, 2, \dots , n \text { and } k \neq i \\ \text { Step   6. Determine the criteria weight vector using } \end{array}
$$

$$
W ^ {\prime} = (W _ {1} ^ {\prime}, W _ {2} ^ {\prime}, \dots , W _ {n} ^ {\prime}) ^ {T}\tag{10}
$$

Step 7. After normalization, obtain the priority weights as

$$
W = (W _ {1}, W _ {w}, \ldots , W _ {n}) ^ {T}\tag{11}
$$

where ?? is a crisp number

## 4.1.2. Interval TOPSIS

TOPSIS is a method based on the concept that the ranking of alternatives is based on the shortest distance from the positive-ideal solution (PIS) and the farthest distance from the negative-ideal solution (NIS) (Hwang & Yoon, 1981). The wide application of TOPSIS in decision-making problems comes from its advantages, including: (i) a sound logic that represents the rationale of DM’s choice; (ii) a scalar value that accounts for both the best and worst alternatives simultaneously; (iii) it is not restrained by the human capacity for information processing since DM’s evaluation is based on cardinal absolute measurement instead of pairwise comparison; iv) a sensible computation process that can be programmed easily into a spreadsheet (Shih et al., 2007). By using pairwise comparison, consistent judgment becomes very difficult to make when evaluating typically more than seven alternatives since the number of pairwise comparisons increases rapidly with the number of criteria or alternatives $( n ( n - 1 ) / 2 )$ (Shih et al., 2007). Therefore, we can use TOPSIS to evaluate a number of suppliers.

Decision-makers would be more comfortable to perceive their opin ion into interval measurement when confronting with uncertainty or lack of certain information. According to Jahanshahloo et al. (2009), we adapt interval TOPSIS in this study. Each step of the procedure is explained in the following.

Let $A \ = \ \{ A _ { 1 } , A _ { 2 } , \ldots , A _ { m } \} ( i \ = \ 1 , 2 , \ldots , m )$ be a discrete set of m feasible alternatives, $C = \{ C _ { 1 } , C _ { 2 } , \dots , C _ { n } \} ( j = 1 , 2 , \dots , n )$ be a finite set of attributes, and ${ \cal D } M = \{ { \cal D } M _ { 1 } , { \cal D } M _ { 2 } , \ldots , { \cal D } M _ { l } \} ( k = 1 , 2 , \ldots , l )$ be a group of DMs.

Step 1. For each DM, evaluate each alternative with respect to ?? attributes using linguistic variables, as shown in Table 5, whose value is an interval $( x _ { i j } \in [ x _ { i j } ^ { ( l ) } , \ x _ { i j } ^ { ( u ) } ] )$ ).

Step 2. For each DM, construct decision matrix which denotes by

$$
X _ {k} = ([ x _ {i j} ^ {(l)}, x _ {i j} ^ {(u)} ]) _ {m \mathbf {x} n}\tag{12}
$$

$$
= \begin{array}{c} A _ {1} \\ = A _ {2} \\ \vdots \\ A _ {m} \end{array} \left( \begin{array}{c c c c} [ x _ {1 1} ^ {k (l)}, x _ {1 1} ^ {k (u)} ] & [ x _ {1 2} ^ {k (l)}, x _ {1 2} ^ {k (u)} ] & ... & [ x _ {1 n} ^ {k (l)}, x _ {1 n} ^ {k (u)} ] \\ [ x _ {2 1} ^ {k (l)}, x _ {2 1} ^ {k (u)} ] & [ x _ {2 2} ^ {k (l)}, x _ {2 2} ^ {k (u)} ] & ... & [ x _ {2 n} ^ {k (l)}, x _ {2 n} ^ {k (u)} ] \\ \vdots & \vdots & \vdots & \vdots \\ [ x _ {m 1} ^ {k (l)}, x _ {m 1} ^ {k (u)} ] & [ x _ {m 2} ^ {k (l)}, x _ {m 2} ^ {k (u)} ] & ... & [ x _ {m n} ^ {k (l)}, x _ {m n} ^ {k (u)} ] \end{array} \right)
$$

Step 3. The weight of ??th DMs $( k \in L )$ is denoted by vector $\lambda =$ $( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { l } ) ^ { T }$ , such that $\lambda _ { k } \ \ge \ 0 , \ \sum _ { k = 1 } ^ { l } \ = \ 1$ . Given the DMs weight, aggregate the decision matrices into a collective matrix ??.

$$
G = \sum_ {k = 1} ^ {l} \lambda_ {k} G _ {k} = ([ g _ {i j} ^ {(l)}, g _ {i j} ^ {(u)} ]) _ {m \mathbf {x} n}\tag{13}
$$

Step 4. Calculate the normalized decision matrix ??

$$
R _ {k} = ([ r _ {i j} ^ {(l)}, r _ {i j} ^ {(u)} ]) _ {m \times n}\tag{14}
$$

$$
= \begin{array}{c} C _ {1} \\ A _ {1} \\ = A _ {2} \\ \vdots \\ A _ {m} \end{array} \left( \begin{array}{c c c c} [ r _ {1 1} ^ {(l)}, r _ {1 1} ^ {(u)} ] & [ r _ {1 2} ^ {(l)}, r _ {1 2} ^ {(u)} ] & ... & [ r _ {1 n} ^ {(l)}, r _ {1 n} ^ {(u)} ] \\ [ r _ {2 1} ^ {(l)}, r _ {2 1} ^ {(u)} ] & [ r _ {2 2} ^ {(l)}, r _ {2 2} ^ {(u)} ] & ... & [ r _ {2 n} ^ {(l)}, r _ {2 n} ^ {(u)} ] \\ \vdots & \vdots & \vdots & \vdots \\ [ r _ {m 1} ^ {(l)}, r _ {m 1} ^ {(u)} ] & [ r _ {m 2} ^ {(l)}, r _ {m 2} ^ {(u)} ] & ... & [ r _ {m n} ^ {(l)}, r _ {m n} ^ {(u)} ] \end{array} \right)
$$

We can further transform the aggregated decision matrix $( [ g _ { i j } ^ { ( l ) } , ~ g _ { i j } ^ { ( u ) } ] ) _ { m \mathbf { x } n }$ into normalized decision matrix $( [ r _ { i j } ^ { ( l ) } , ~ r _ { i j } ^ { ( u ) } ] ) _ { m \times n }$ using the following formula

$$
r _ {i j} ^ {(l)} = \frac {g _ {i j} ^ {(l)}}{\sqrt {\sum_ {i = 1} ^ {m} (g _ {i j} ^ {(l)}) ^ {2} + (g _ {i j} ^ {(u)}) ^ {2}}}, \forall i \in M, j \in N\tag{15}
$$

$$
r _ {i j} ^ {(u)} = \frac {g _ {i j} ^ {(u)}}{\sqrt {\sum_ {i = 1} ^ {m} (g _ {i j} ^ {(l)}) ^ {2} + (g _ {i j} ^ {(u)}) ^ {2}}},   \forall i \in M,   j \in N\tag{16}
$$

Step 5. Calculate weighted normalized decision matrix ?? considering the different importance of each attribute as decision matrix ?? .

$$
V = ([ v _ {i j} ^ {(l)}, v _ {i j} ^ {(u)} ]) _ {m \mathbf {x} n} = ([ w _ {j} r _ {i j} ^ {(l)}, w _ {j} r _ {i j} ^ {(u)} ]) _ {m \mathbf {x} n}\tag{17}
$$

$$
= \begin{array}{c} C _ {1} \\ A _ {1} \\ = A _ {2} \\ \vdots \\ A _ {m} \end{array} \left( \begin{array}{c c c c} [ v _ {1 1} ^ {(l)}, v _ {1 1} ^ {(u)} ] & [ v _ {1 2} ^ {(l)}, v _ {1 2} ^ {(u)} ] & ... & [ v _ {1 n} ^ {(l)}, v _ {1 n} ^ {(u)} ] \\ [ v _ {2 1} ^ {(l)}, v _ {2 1} ^ {(u)} ] & [ v _ {2 2} ^ {(l)}, v _ {2 2} ^ {(u)} ] & ... & [ v _ {2 n} ^ {(l)}, v _ {2 n} ^ {(u)} ] \\ \vdots & \vdots & \vdots & \vdots \\ [ v _ {m 1} ^ {(l)}, v _ {m 1} ^ {(u)} ] & [ v _ {m 2} ^ {(l)}, v _ {m 2} ^ {(u)} ] & ... & [ v _ {m n} ^ {(l)}, v _ {m n} ^ {(u)} ] \end{array} \right)
$$

where $w _ { j }$ is the weight of the ??th attribute, such that $0 ~ \leq ~ w _ { j } ~ \leq$ 1, and $\sum _ { j = 1 } ^ { n } w _ { j } = 1 ,$

Step 6. Find the positive ideal solution (PIS) and negative idea solution (NIS).

Step 6.1 Determine PIS

Determine the best value of alternative $A _ { k }$ based on the criteria, such as maximum for benefit criteria and minimum for cost criteria.

Accordingly, ${ A } _ { k } ^ { + ( u ) }$ can be defined as follows:

$$
A _ {k} ^ {+ (u)} = \{(v _ {1} ^ {+ (u)}, v _ {2} ^ {+ (u)}, \ldots , v _ {n} ^ {+ (u)}) \} = \{(m a x v _ {i j} ^ {(u)} | i \in O), (m i n v _ {i j} ^ {(l)} | i \in I) \}\tag{18}
$$

where ?? is associated with benefit criteria and ?? with cost criteria.

Determine the worst value for alternative $A _ { k }$ based on the criteria, such as minimum for benefit criteria and maximum for cost criteria. ${ A } _ { k } ^ { + ( l ) }$ can be found using the following form:

$$
\begin{array}{r l} A _ {k} ^ {+ (l)} = \{(v _ {1} ^ {+ (l)}, v _ {2} ^ {+ (l)}, \dots , v _ {n} ^ {+ (l)}) \} \\ = \{(m a x _ {j \neq i} \{v _ {i j} ^ {(u)}, v _ {i j} ^ {(l)} \} | i \in O), (m i n _ {j \neq i} \{v _ {i j} ^ {(u)}, v _ {i j} ^ {(l)} \} | i \in I) \} \end{array}\tag{19}
$$

Step 6.2 Determine NIS

$$
\begin{array}{r l} A _ {k} ^ {- (u)} = \{(v _ {1} ^ {- (u)}, v _ {2} ^ {- (u)}, \ldots , v _ {n} ^ {- (u)}) \} \\ = \{(m i n _ {j \neq i} \{v _ {i j} ^ {(u)}, v _ {i j} ^ {(l)} \} | i \in O), (m a x _ {j \neq i} \{v _ {i j} ^ {(u)}, v _ {i j} ^ {(l)} \} | i \in I) \} \end{array}\tag{20}
$$

$$
A _ {k} ^ {- (l)} = \{(v _ {1} ^ {- (l)}, v _ {2} ^ {- (l)}, \dots , v _ {n} ^ {- (l)}) \} = \{(m i n v _ {i j} ^ {(l)} \mid i \in O), (m a x v _ {i j} ^ {(u)} \mid i \in I) \}\tag{21}
$$

Step 7. Calculate the distance of each individual decision $A _ { k }$ from the PIS $( d _ { k } ^ { + ( l ) } , ~ d _ { k } ^ { + ( u ) } )$ and NIS $( d _ { k } ^ { - ( l ) } , ~ d _ { k } ^ { - ( u ) } )$ using the ??-dimensional Euclidean distance.

$$
d _ {k} ^ {+ (u)} = \sqrt {\sum_ {i \in I} (v _ {i} ^ {+ (u)} - d _ {i k} ^ {(u)}) ^ {2} + \sum_ {i \in O} (v _ {i} ^ {+ (u)} - d _ {i k} ^ {(l)}) ^ {2}}\tag{22}
$$

$$
\begin{array}{l} d _ {k} ^ {+ (l)} = \sqrt {\sum_ {i \in I} (v _ {i} ^ {+ (l)} - d _ {i k} ^ {(l)}) ^ {2} + \sum_ {i \in O} (v _ {i} ^ {+ (l)} - d _ {i k} ^ {(u)}) ^ {2}} \\ d _ {k} ^ {- (u)} = \sqrt {\sum_ {i \in I} (v _ {i} ^ {- (l)} - d _ {i k} ^ {(l)}) ^ {2} + \sum_ {i \in O} (v _ {i} ^ {- (l)} - d _ {i k} ^ {(u)}) ^ {2}} \\ d _ {k} ^ {- (l)} = \sqrt {\sum_ {i \in I} (v _ {i} ^ {- (u)} - d _ {i k} ^ {(l)}) ^ {2} + \sum_ {i \in O} (v _ {i} ^ {- (u)} - d _ {i k} ^ {(u)}) ^ {2}} \end{array}
$$

Step 8. Calculate closeness coefficients $( C C _ { k } ^ { ( l ) } , \ C C _ { k } ^ { ( u ) } ) ;$

$$
C C _ {k} ^ {(l)} = \frac {d _ {k} ^ {- (l)}}{d _ {k} ^ {- (u)} + d _ {k} ^ {+ (u)}}\tag{23}
$$

$$
C C _ {k} ^ {(u)} = \frac {d _ {k} ^ {- (u)}}{d _ {k} ^ {- (u)} + d _ {k} ^ {+ (u)}}
$$

Step 9. Rank the best alternative. We adopt Sengupta’s approach in the following.

Calculate the mid-point ?? $( C C _ { k } )$ and half width of the interval closeness coefficient $w ( C C _ { k } )$ using

$$
m (C C _ {k}) = \frac {1}{2} (C C _ {k} ^ {(l)} + C C _ {k} ^ {(u)})\tag{24}
$$

$$
w (C C _ {k}) = \frac {1}{2} (C C _ {k} ^ {(u)} - C C _ {k} ^ {(l)})\tag{25}
$$

According to the acceptability function, compare two alternatives a and b as follows:

$$
\mathcal {A} _ {(<  )} = \frac {m (b) - m (a)}{w (b) + w (a)}\tag{26}
$$

$\scriptstyle A _ { ( < ) }$ can be interpreted as the first interval to be inferior to the second interval. The term ‘‘inferior $\mathrm { t o } ^ { \prime \prime }$ (‘‘superior to’’) can be defined as ‘‘less than’’ (‘‘greater than’’). Decision-makers can select an alternative between two according to the value of $\mathbf { \mathcal { A } } _ { ( < ) } .$ According to this procedure, the best choice of alternative can stand for the one with a smaller uncertain interval (the half width) if two interval numbers have the same mid-point.

![](images/0366582d0f544f70f74713bc4acc3bd3ccd93674e0f8e116e126400184eb3779.jpg)  
Fig. 2. Simulation–optimization: Analytic model enhancement.

## 4.2. Simulation-optimization

## 4.2.1. Multi-objective approach

First, we divide the multi-objective model defined in Section 3 into two single-objective sub-problems. The first sub-problem is defined according to the objective function in Eqs. (1) and constraints in Eqs. (3), (4), and (5). The second sub-problem comprises an objective function in Eqs. $( 2 \mathrm { a } ) \mathrm { - } ( 2 \mathrm { d } )$ , subject to the same constraints. We solve these two sub-problems separately using an S-O approach to obtain their best solutions, $Z 1 _ { m a x }$ and $Z 2 _ { m i n } .$ , respectively.

Second, the distance method is used to calculate the deviation of the objective function (??) representing the distance from the ideal solution $( Z ^ { * }$ , where $Z ^ { * } = Z _ { m a x }$ for maximization, $Z ^ { * } = Z _ { m i n }$ for minimization).

$$
f 1 = \frac {Z 1 _ {m a x} - Z 1}{Z 1 _ {m a x}}\tag{27}
$$

$$
f 2 = \frac {Z 2 - Z 2 _ {m i n}}{Z 2 _ {m i n}}\tag{28}
$$

Finally, we transform both objective functions into a single objective for minimizing total deviation (??) using the weighted comprehensive criterion method (WCCM) (Abdallah et al., 2021). The importance weights $( \alpha _ { 1 } , \alpha _ { 2 } )$ is also assigned to each objective function. A single objective function is expressed as follows.

$$
\mathrm{Min} e = \alpha_ {1}. f 1 + \alpha_ {2}. f 2\tag{29}
$$

??.??.

$$
\mathrm{Eq.} (3), (4), (5)\tag{30}
$$

where $\alpha _ { 1 } + \alpha _ { 2 } = 1 .$

## 4.2.2. Simulation enhancing the analytical model

We develop simulation–optimization using a genetic algorithm (GA) to search within the solution space. A simulation model provides a thor ough evaluation for stochastic input parameters, considering stochastic demand, uncertain imperfect rate, and disruptions. In our proposed approach, the GA optimizes decision variables of ?? (supplier selection) based on the performance measure (??) formulated in Eq. (29).

Given the value of X. which is randomly selected, we determine order allocation (?? ) according to the transportation cost given by (2c), constraints (3) and (4). More specifically, we derived the solution using a transportation method. Then, the optimal order quantity from a plant to a supplier $( Q _ { i j } )$ is obtained according to inventory costs given by (2b 1), (2b-2), (2c), and imperfect items’ holding costs (2d). To incorporate vehicle capacity, order quantity is determined by using a heuristic (see Saputro et al., 2020).

λ1, λ2 (0.5, 0.5)λ1, λ2 (0.55, 0.45)λ1, λ2 (0.6. 0.4)λ1, λ2 (1. 0) λ1, λ2 (0.45, 0.55)→λ1, λ2 (0.4. 0.6)λ1, λ2 (0.1)  
![](images/9fcd0d83cea319e07143ca72e9c9e01f166d4b29355a7895b39de72a9ad8abbb.jpg)

![](images/2473c4b30fbbda538c987d85709c3bee5b10071a82ffb56286e840ebad9cae46.jpg)  
λ1, λ2 (0.5, 0.5)λ1, λ2 (0.55, 0.45)→λ1, λ2 (0.6, 0.4)λ1, λ2 (1, 0) λ1, λ2 (0.45, 0.55)→λ1, λ2 (0.4, 0.6)λ1, λ2 (0, 1)

(a) Fast movers  
![](images/76dd8c9b164a49a92c1845d05d7cb3cb7d9701703038f1aa5bc44ba8e159834f.jpg)

![](images/c0e8b8f5feed839705089ceb900d191b7ddf6e1c0869dfd69eddff548d39f41c.jpg)  
(b) Slow movers  
Fig. 3. Impact of DMs weight $( \lambda _ { k } )$ on the suppliers score (???? ) and ranking.

The solutions containing supplier selection (??) and inventory decisions (??, ??) are then passed to the simulation incorporating demand uncertainty and disruptions for objective function evaluation (??). The optimization process is powered by simulation’s feedback, which is used to refine the lead-time (??). It is used to address possible delays that result from disruptions. The analytical expression (??, ??) is then enhanced while the lead-time is refined. This simulation–optimization approach is known as an analytic model enhancement (AME). The refinement procedure begins such that, for every randomly selected $X ,$ and each replication, the lead time derived from simulation based on the mean value is sent for optimization. According to the refined lead time, the reorder point is recalculated. The performance measure (??) is returned to the optimization according to the decision variables sent to the simulation. The GA then uses this performance measure to optimize the solutions. By refining lead time, inventory decisions can be updated for optimizing supplier selection as to mitigate the disruptions risk. The illustration of AME is shown in Fig. 2.

## 5. Computational experiments

In this study, we consider a firm that operates eight manufacturing plants located in different regions. The material supply of each man ufacturing plant is sourced from two or more suppliers. There are ten candidate suppliers to be evaluated under qualitative and quantitative criteria. We use qualitative criteria and their evaluation based on the decision-makers’ judgment from Yadav and Sharma (2016)’s study. Quantitative criteria and other parameters indicated in Eqs. (2a)–(2d), (3), and (4) are adopted from Saputro et al. (2020). These quantita tive criteria will be assessed objectively in a monetary based-value. The respective quantitative and qualitative criteria are summarized in Table 7. In addition, the values of input parameters, representing fast moving items, are indicated in Table 8. Fast-moving items represent a low purchasing price but a high turn over.

![](images/dc5edc465ca0ec07c7301771f0a6376789e7ee3aa4f23ac460b64bd9f7681a2b.jpg)

(a) Fast movers  
![](images/5fdbad5d24c760724865858c2ee6287cb4144b56e4c293656ed940e1782671b3.jpg)  
(b) Slow movers  
Fig. 4. Impact of objective weight $( \alpha _ { k } )$ on the deviation (??).

Table 7  
Quantitative and qualitative supplier selection criteria.

<table><tr><td>Category</td><td>Criteria</td><td>Sub-criteria</td><td>Category</td><td>Criteria</td><td>Sub-criteria</td></tr><tr><td rowspan="12">Quantitative</td><td rowspan="3">Cost</td><td>Purchasing cost (c)</td><td rowspan="12">Qualitative</td><td rowspan="4">Service</td><td>Technical support</td></tr><tr><td>Contractual cost (f)</td><td>Information sharing</td></tr><tr><td>Transportation cost (p,r)</td><td>Warranty &amp; claim policy</td></tr><tr><td>Quality</td><td>Rate of perfect quality (1-k)</td><td>Capabilities</td></tr><tr><td rowspan="4">Delivery</td><td>Lead time (l)</td><td rowspan="4">Relationship</td><td>Honesty</td></tr><tr><td>On-time delivery (simulation)</td><td>Reputation</td></tr><tr><td>Vehicle capacity (u)</td><td>Trust &amp; partnership</td></tr><tr><td>Distance (d)</td><td>Ease of communication</td></tr><tr><td>Technology</td><td>Supply capacity (b)</td><td rowspan="4">Flexibility</td><td>Product mix flexibility</td></tr><tr><td rowspan="3">Risk</td><td>Disruptions (θ,v)</td><td>Volume flexibility</td></tr><tr><td>Disruptive lead time (simulation)</td><td>Process flexibility</td></tr><tr><td>Rate of imperfect quality (k)</td><td>Service flexibility</td></tr></table>

Table 8  
Input parameters for fast movers

<table><tr><td colspan="2">Parameters</td><td>Values</td><td>Units</td></tr><tr><td colspan="4">Plant, i ∈ I</td></tr><tr><td>Demand</td><td>μi, σi</td><td>: U(1000, 3000), U(150, 300)</td><td>unit/year</td></tr><tr><td>Setup costs</td><td>oi</td><td>: U(500, 1000)</td><td>$/order</td></tr><tr><td>Holding costs</td><td>hi</td><td>: U(0.5, 3.0)</td><td>$/unit/year</td></tr><tr><td>Shortage costs</td><td>si</td><td>: U(5.0, 10.0)</td><td>$/unit/year</td></tr><tr><td>Imperfect items&#x27; holding costs</td><td>h&#x27;i</td><td>: U(0.25, 1.5)</td><td>$/unit/year</td></tr><tr><td>External failure costs</td><td>ai</td><td>: U(0.2, 1)</td><td>$/unit</td></tr><tr><td>Location</td><td></td><td>: [U(0, 500), U(0, 500)]</td><td></td></tr><tr><td colspan="4">Supplier, j ∈ J</td></tr><tr><td>Supply capacity</td><td>bj</td><td>: U(7500, 10000)</td><td>unit</td></tr><tr><td>Imperfect rate</td><td>kj</td><td>: U(0.15, 0.35)</td><td></td></tr><tr><td>Vehicle capacity</td><td>uj</td><td>: U(150, 300)</td><td>unit/vehicle</td></tr><tr><td>Disruption frequency</td><td>θj</td><td>: U(1, 7)</td><td>days</td></tr><tr><td>Disruption length</td><td>vj</td><td>: U(0.5, 2)</td><td>days</td></tr><tr><td>Contractual costs</td><td>fj</td><td>: U(50000, 100000)</td><td>$</td></tr><tr><td>Unit purchasing costs</td><td>cj</td><td>: U(0.4, 2.0)</td><td>$/unit</td></tr><tr><td>Location</td><td></td><td>: [U(0, 500), U(0, 500)]</td><td></td></tr><tr><td colspan="4">Plant-Supplier, i ∈ I, j ∈ J</td></tr><tr><td>Fixed transportation costs</td><td>pij</td><td>: U(250, 500)</td><td>$/order/vehicle</td></tr><tr><td>Variable transportation costs</td><td>rij</td><td>: U(0.75, 3)</td><td>$/mile/vehicle</td></tr><tr><td>Lead time</td><td>lij</td><td>: (U(1.2)/60)dij</td><td>hours</td></tr></table>

Fuzzy pairwise comparison matrix among qualitative criteria.  
Table 9

<table><tr><td>Citeria</td><td>Service (C1)</td><td>Relationship (C2)</td><td>Flexibility (C3)</td></tr><tr><td>Service (C1)</td><td>1, 1, 1</td><td>2, 3, 4</td><td>1, 2, 3</td></tr><tr><td>Relationship (C2)</td><td>1/4, 1/3, 1/2</td><td>1, 1, 1</td><td>1/3, 1/2, 1</td></tr><tr><td>Flexibility (C3)</td><td>1/3, 1/2, 1</td><td>1, 2, 3</td><td>1, 1, 1</td></tr></table>

## 5.1. Suppliers assessment based on qualitative criteria

## 5.1.1. Determining criteria weight

There are 3 criteria and 12 sub-criteria associated with qualitative measures. A decision-maker assessed the criteria and sub-criteria using fuzzy pairwise comparison matrices shown in Tables 9 and 10, respec tively. Finally, the weights are calculated using Fuzzy AHP and the result is shown in Table 11.

Criteria with a high importance weight become a critical aspect of evaluation. According to Table 11, the DM considers warranty and claim policy as the most critical one for supplier evaluation, followed by technical support, service flexibility, and volume flexibility, respectively.

## 5.1.2. Determining suppliers score

In this stage, suppliers performance are evaluated under sub-criteria using linguistic variables expressed in Table 5. The decision maker judgment regarding suppliers performance is summarized in Table 12. According to this information, the DM’ judgments are transformed into their respective interval numbers shown in Table C.16. Supplier score is then determined using interval TOPSIS, and sub-criteria global weights (?? ), indicated in Table 11, are used for this calculation (see Eq. (17) in Section 4.1.2). Finally, supplier score (???? ) is derived based on the mid-point of the closeness coefficient $( S S _ { j } = C C _ { k } ,$ , where $k = j )$ , shown in Table 13.

According to the closeness coefficient, supplier 4 has the best qual itative evaluation since it has the highest score. This implies that its overall performance is far from the worst existing evaluation. The second and third best alternatives refer to suppliers 8 and 2, respectively. Supplier 10 represents the worst-performing alternative although its performance on six out of ten criteria is better than supplier 8. This happened mainly due to the criteria weight assigned by the DM. In this study, sub-criteria, including technical support (SC1), warranty & claim policy (SC3), volume flexibility (SC10), and service flexibility (SC12), are given a high priority. At least under one of these sub criteria (i.e., technical support, warranty & claim policy, and volume flexibility), the performance of supplier 10 underperforms supplier 8.

Table 10  
Fuzzy pairwise comparison matrix among qualitative sub-criteria

<table><tr><td>Service (C1)</td><td>Technical support (SC1)</td><td>Information sharing (SC2)</td><td>Warranty and claim policy (SC3)</td><td>Capabilities (SC4)</td></tr><tr><td>Technical support (SC1)</td><td>1, 1, 1</td><td>2, 3, 4</td><td>1/4, 1/3, 1/2</td><td>1, 2, 3</td></tr><tr><td>Information sharing (SC2)</td><td>1/4, 1/3, 1/2</td><td>1, 1, 1</td><td>1/5, 1/4, 1/3</td><td>1/4, 1/3, 1/2</td></tr><tr><td>Warranty and claim policy (SC3)</td><td>2, 3, 4</td><td>1, 1, 1</td><td>1, 1, 1</td><td>2, 3, 4</td></tr><tr><td>Capabilities (SC4)</td><td>1/3, 1/2, 1</td><td>2, 3, 4</td><td>1/4, 1/3, 1/2</td><td>1, 1, 1</td></tr><tr><td>Relationship (C2)</td><td>Honesty (SC5)</td><td>Reputation (SC6)</td><td>Trust &amp; partnership (SC7)</td><td>Ease of communication (SC8)</td></tr><tr><td>Honesty (SC5)</td><td>1, 1, 1</td><td>2, 3, 4</td><td>4, 5, 6</td><td>4, 5, 6</td></tr><tr><td>Reputation (SC6)</td><td>1/4, 1/3, 1/2</td><td>1, 1, 1</td><td>2, 3, 4</td><td>2, 3, 4</td></tr><tr><td>Trust &amp; partnership (SC7)</td><td>1/6, 1/5, 1/4</td><td>1/4, 1/3, 1/2</td><td>1, 1, 1</td><td>1, 2, 3</td></tr><tr><td>Ease of communication (SC8)</td><td>1/6, 1/5, 1/4</td><td>1/4, 1/3, 1/2</td><td>1/3, 1/2, 1</td><td>1, 1, 1</td></tr><tr><td>Flexibility (C3)</td><td>Product mix flexibility (SC9)</td><td>Volume flexibility (SC10)</td><td>Process flexibility (SC11)</td><td>Service flexibility (SC12)</td></tr><tr><td>Product mix flexibility (SC9)</td><td>1, 1, 1</td><td>1/4, 1/3, 1/2</td><td>1, 2, 3</td><td>1/4, 1/3, 1/2</td></tr><tr><td>Volume flexibility (SC10)</td><td>2, 3, 4</td><td>1, 1, 1</td><td>3, 4, 5</td><td>1/3, 1/2, 1</td></tr><tr><td>Process flexibility (SC11)</td><td>1/3, 1/2, 1</td><td>1/5, 1/4, 1/3</td><td>1, 1, 1</td><td>1/4, 1/3, 1/2</td></tr><tr><td>Service flexibility (SC12)</td><td>2, 3, 4</td><td>1, 2, 3</td><td>2, 3, 4</td><td>1, 1, 1</td></tr></table>

Table 11  
Weight of criteria and sub-criteria.

<table><tr><td>Criteria</td><td>Criteria weight</td><td>Sub-criteria</td><td>Sub-criteria weight</td><td>Sub-criteria global weight (w)</td><td>Priority</td></tr><tr><td rowspan="4">Service (C1)</td><td rowspan="4">0.567</td><td>Technical support (SC1)</td><td>0.273</td><td>0.155</td><td>2</td></tr><tr><td>Information sharing (SC2)</td><td>0.067</td><td>0.038</td><td>8</td></tr><tr><td>Warranty &amp; claim policy (SC3)</td><td>0.503</td><td>0.285</td><td>1</td></tr><tr><td>Capabilities (SC4)</td><td>0.156</td><td>0.089</td><td>5</td></tr><tr><td rowspan="4">Relationship (C2)</td><td rowspan="4">0.077</td><td>Honesty (SC5)</td><td>0.593</td><td>0.046</td><td>6</td></tr><tr><td>Reputation (SC6)</td><td>0.242</td><td>0.019</td><td>9</td></tr><tr><td>Trust &amp; partnership (SC7)</td><td>0.134</td><td>0.010</td><td>11</td></tr><tr><td>Ease of communication (SC8)</td><td>0.030</td><td>0.002</td><td>12</td></tr><tr><td rowspan="4">Flexibility (C3)</td><td rowspan="4">0.356</td><td>Product mix flexibility (SC9)</td><td>0.125</td><td>0.045</td><td>7</td></tr><tr><td>Volume flexibility (SC10)</td><td>0.407</td><td>0.145</td><td>4</td></tr><tr><td>Process flexibility (SC11)</td><td>0.041</td><td>0.015</td><td>10</td></tr><tr><td>Service flexibility (SC12)</td><td>0.427</td><td>0.152</td><td>3</td></tr></table>

Table 12  
Supplier performance under DM’s judgment.

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>F</td><td>MG</td><td>F</td><td>MG</td><td>MP</td><td>F</td><td>G</td><td>P</td><td>P</td><td>F</td><td>MP</td><td>MG</td></tr><tr><td>2</td><td>F</td><td>MP</td><td>G</td><td>F</td><td>MP</td><td>F</td><td>G</td><td>F</td><td>MP</td><td>MP</td><td>MP</td><td>MP</td></tr><tr><td>3</td><td>MP</td><td>MG</td><td>F</td><td>MP</td><td>MP</td><td>F</td><td>MP</td><td>F</td><td>MG</td><td>P</td><td>P</td><td>F</td></tr><tr><td>4</td><td>F</td><td>P</td><td>G</td><td>F</td><td>P</td><td>MG</td><td>F</td><td>MP</td><td>F</td><td>MG</td><td>P</td><td>F</td></tr><tr><td>5</td><td>MP</td><td>F</td><td>G</td><td>F</td><td>P</td><td>MG</td><td>F</td><td>F</td><td>P</td><td>MG</td><td>P</td><td>P</td></tr><tr><td>6</td><td>MP</td><td>MP</td><td>G</td><td>MG</td><td>MP</td><td>F</td><td>MP</td><td>P</td><td>P</td><td>F</td><td>P</td><td>P</td></tr><tr><td>7</td><td>MP</td><td>F</td><td>G</td><td>F</td><td>P</td><td>P</td><td>F</td><td>F</td><td>F</td><td>P</td><td>P</td><td>F</td></tr><tr><td>8</td><td>F</td><td>MP</td><td>G</td><td>G</td><td>MP</td><td>MG</td><td>MG</td><td>P</td><td>P</td><td>MP</td><td>P</td><td>MP</td></tr><tr><td>9</td><td>MP</td><td>P</td><td>MP</td><td>MG</td><td>P</td><td>P</td><td>MG</td><td>F</td><td>F</td><td>MP</td><td>MP</td><td>MG</td></tr><tr><td>10</td><td>F</td><td>MG</td><td>MP</td><td>G</td><td>P</td><td>MP</td><td>G</td><td>F</td><td>MP</td><td>P</td><td>MP</td><td>MG</td></tr></table>

Table 13  
Suppliers score based on the closeness coefficient.

<table><tr><td rowspan="2">Supplier</td><td colspan="3">Closeness coefficient ( $CC_{k}$ )</td><td rowspan="2">Ranking</td></tr><tr><td>Interval</td><td>Mid-point</td><td>Half-width</td></tr><tr><td>1</td><td>[0.377, 0.685]</td><td>0.531</td><td>0.154</td><td>7</td></tr><tr><td>2</td><td>[0.324, 0.814]</td><td>0.569</td><td>0.245</td><td>3</td></tr><tr><td>3</td><td>[0.299, 0.532]</td><td>0.416</td><td>0.117</td><td>9</td></tr><tr><td>4</td><td>[0.420, 0.842]</td><td>0.631</td><td>0.211</td><td>1</td></tr><tr><td>5</td><td>[0.367, 0.760]</td><td>0.564</td><td>0.197</td><td>4</td></tr><tr><td>6</td><td>[0.339, 0.769]</td><td>0.554</td><td>0.215</td><td>5</td></tr><tr><td>7</td><td>[0.335, 0.757]</td><td>0.546</td><td>0.211</td><td>6</td></tr><tr><td>8</td><td>[0.330, 0.836]</td><td>0.583</td><td>0.253</td><td>2</td></tr><tr><td>9</td><td>[0.330, 0.539]</td><td>0.435</td><td>0.104</td><td>8</td></tr><tr><td>10</td><td>[0.319, 0.544]</td><td>0.397</td><td>0.112</td><td>10</td></tr></table>

## 5.2. Final selection

The final decision-making for the integrated supplier selection is accomplished by solving the multi-objective model (described in Sec tion 3) using an S-O approach considering disruptions (c.f. Section 4.2).

We construct objective function ??1, incorporating supplier scores (???? ) obtained from interval TOPSIS, and objective function ??2.

The best values are 14893 and 64972, respectively for $Z 1 _ { m a x }$ and $Z 2 _ { m i n } .$ For $Z 1 _ { m a x } ,$ supplier 4 and 8 are selected. While for $Z 2 _ { m i n } ,$ selected suppliers include 4 and 6.

After deriving the best value of each objective, the final solution is derived by minimizing total deviation of both objectives using Eq. (29) and setting up $\alpha _ { 1 } = 0 . 5$ and $\alpha _ { 2 } = 0 . 5$ . The best solution was found with a deviation of 0.073 (see Fig. B.5). Selected suppliers include 4 and 6. This indicates that $Z 1 _ { m a x }$ is compromised to achieve the trade-off.

## 5.3. Sensitivity analysis

This analysis aims to investigate the impact of DM weight and objective weight. In order to arrive at more general conclusions, we created an additional scenario namely slow moving items by using different values of input parameters, as seen in Table D.23. Slow moving items imply an expensive item with a low turn over. The parameters value is adopted from Saputro et al. (2020). Additionally,

Table 14  
Variation of supplier score according to different scenarios of $( \lambda _ { k } ) .$

<table><tr><td rowspan="2">Problem</td><td colspan="5">Scenarios</td></tr><tr><td> $\lambda_1, \lambda_2 (0.6, 0.4)$ </td><td> $\lambda_1, \lambda_2 (0.55, 0.45)$ </td><td> $\lambda_1, \lambda_2 (0.5, 0.5)$ </td><td> $\lambda_1, \lambda_2 (0.45, 0.55)$ </td><td> $\lambda_1, \lambda_2 (0.4, 0.6)$ </td></tr><tr><td>Fast movers</td><td>0.2920</td><td>0.2658</td><td>0.2534</td><td>0.2230</td><td>0.2234</td></tr><tr><td>Slow movers</td><td>0.2128</td><td>0.1953</td><td>0.1894</td><td>0.1784</td><td>0.1728</td></tr></table>

Table A.15  
Qualitative criteria for supplier selection

<table><tr><td>Criteria</td><td>Description</td><td>Sub-criteria</td><td>Description</td></tr><tr><td rowspan="4">Service</td><td rowspan="4">The after-sales service which promotes customers satisfaction and influences customer purchasing intentions</td><td>Technical support</td><td>Commitment of a supplier to provide technical support services</td></tr><tr><td>Information sharing</td><td>The willingness of a supplier to share technical information</td></tr><tr><td>Warranty and claim policy</td><td>The intention of a supplier to provide warranties or agreements between the customer and the supplier for the faulty products</td></tr><tr><td>Capabilities</td><td>The capability of a supplier to resolve issues or conflict</td></tr><tr><td rowspan="4">Relationship</td><td rowspan="4">The buyer–supplier relationship that enhances mutual motivation and results in better development of the total economy</td><td>Honesty</td><td>The attitude and responsibility of managers in professional relationship</td></tr><tr><td>Reputation</td><td>The track record of Supplier indicating a cooperation experience with large enterprises</td></tr><tr><td>Trust &amp; partnership</td><td>The commitment s of a supplier to Establish mutually beneficial long-term supplier relationship</td></tr><tr><td>Ease of communication</td><td>The ability of supplier in providing an effective commutations system to customers</td></tr><tr><td rowspan="4">Flexibility</td><td rowspan="4">The ability of a supplier to adapt to external changes while maintaining satisfactory system performance</td><td>Product mix flexibility</td><td>The ability to change the variety of products produced (customers&#x27; orders)</td></tr><tr><td>Volume flexibility</td><td>The ability to respond to change in demand</td></tr><tr><td>Process flexibility</td><td>The ability to adapt the production technology and its process in order to respond to the new customer product characteristics</td></tr><tr><td>Service flexibility</td><td>The ability to handle the abnormal orders without compromising the existing product price</td></tr></table>

DMs’ judgments for suppliers are provided in Appendix C. The analysis is respectively presented in Sections 5.3.1 and 5.3.2, emphasizing some key aspects.

## 5.3.1. Impact of decision maker weight

We investigate the impact of DMs weight $( \lambda _ { k } )$ on the suppliers score $( S S _ { j } )$ and their associated ranking. Thus, we consider an additional DM, namely $D M _ { 1 }$ and $D M _ { 2 }$ . To perform this analysis, we just focus on the first phase of the solution approach for fast and slow movers. For each pair of $\lambda _ { 1 }$ and $\lambda _ { 2 } ,$ we set up the weight varying from 0.4 up to $0 . 6 ,$ and $\lambda _ { 1 } + \lambda _ { 2 } = 1$ . The results of the sensitivity analysis are shown in Fig. 3.

Fig. 3 indicates that the opinions of each DM toward suppliers performance can differ. Variation of both suppliers score and ranking is considerable for each DM $( \lambda _ { 1 } = 1 o r \lambda _ { 2 } = 1 ) .$ . For fast movers, DM1 and DM2 make contrast assessment for suppliers 1, 7, 8, and 9. While for slow movers, assessment of suppliers 1, 2, 5, 6, and 9 contrast between DM1 and DM2. Therefore, to accommodate the different opinions, weight needs to be assigned to each DM so that consensus can be achieved.

The result of the sensitivity shows that the impact of $\lambda _ { k }$ on supplier score and ranking is quite evident. It improves satisfaction degree of consensus for each DM. According to each scenario of DMs weight, small variation can be achieved when $\lambda _ { 1 } = 0 . 4 5$ and $\lambda _ { 2 } = 0 . 5 5$ for fast movers, and $\lambda _ { 1 } = 0 . 4$ and $\lambda _ { 2 } = 0 . 6$ for slow movers. Table 14 shows the mean variation of suppliers’ score according to different scenarios of $\lambda _ { 1 }$ and $\lambda _ { 2 }$ against a single $\lambda ( \lambda _ { 1 } = 1 \ o r \ \lambda _ { 2 } = 1 )$

## 5.3.2. Impact of objective weight

Analysis regarding the impact of objective weight $( \alpha _ { k } )$ is further performed for each problem. The objective weight varies between 0.2 and 0.8 for each pair of $\alpha _ { 1 }$ and $\alpha _ { 2 } .$ . The results of this sensitivity analysis are shown in Fig. 4.

Both scenarios indicate that the trade-off between objective functions ??1 and $Z 2$ decreases when weights are more unbalanced. In those cases, the total deviation of the objectives tends to decrease. By contrast, total deviation increases when the weight of both objectives is nearly the same. Thus, it is not easy to achieve a high yield without compromising another objective.

Furthermore, our analysis indicates that the best trade-off is achieved when ??2 is given a priority, resulting in lower deviation compared to other scenarios. The total deviation on average decreases by 22% and 16%, respectively for fast and slow movers, for $\alpha _ { 2 } > 0 . 5$ . In other words, minimizing total costs can be considered more important than maximizing the total value of purchasing when selecting suppliers. This is aligned with the insight pointed by the case study explored by Gören (2018).

## 5.4. Managerial implication

Our analysis draws important implications for decision-makers in supplier selection. Selection criteria should be well incorporated for both qualitative and quantitative. Evaluating suppliers under quantitative criteria should be objectively performed as it can be measured based on a monetary-based value. This monetary measure should be the focus for purchases comprising high-profit impact. The quantitative cri teria become a critical aspect since it refers to a firm’s core performance (e.g., quality, delivery, and cost). Also, it is associated with risk factors (i.e., disruptions, imperfect quality, delivery delay), which becomes a critical issue for the purchases whose supply complexity is high such as strategic items. It becomes relevant since it also affects inventory decisions (Saputro et al., 2020).

![](images/767ae96396707de93f2f59a2bbb791a5454aefc21d25251009129f7ba53babec.jpg)

(a)  
![](images/c92ede557028fe3aca37bc825208235e1d47def04c1a6d6d5242934e1b56c506.jpg)

(b)  
![](images/6967bc7aa3854f9a55ace843b49efdc38af960fd5ca17a3da0e33b9a2e6301b7.jpg)  
(c)  
Fig. B.5. The convergence under multi-objective settings: (a) Value of purchasing (??1), (b) Total costs (??2), (c) Total deviation (??).

Under uncertainty in which information regarding suppliers can be incomplete or non-obtainable, imprecise or vague judgment raises particularly for qualitative criteria. This can result in contradictory judgment among DMs. Therefore, a weight needs to be assigned to each DM to accommodate the degree of satisfaction. In practice, it is important to look at DMs’ knowledge, experience, and consistency when assigning their weights.

A pre-qualification or screening process might be established in supplier selection, particularly when the number of candidates restrains human’s evaluation capacity. The two-phase solution approach pro posed in this study discloses a comprehensive decision-making process, which does not need pre-qualification. This also enhances the final decision-making by optimizing the decisions jointly via S-O, considering multi-objectives.

## 6. Conclusion

Due to high-profit impact and supply complexity, this study ad dresses supplier selection for strategic items incorporating criteria holistically under uncertainty and disruptions risk mitigation. A novel twophase solution approach is proposed to solve the model with multi objective. Fuzzy AHP and interval TOPSIS are respectively used to perceive imprecise DMs’ judgment in determining weight and assessing suppliers under qualitative criteria. The final decision-making process is performed using S-O based on analytic model enhancement (AME). AME provides a better decision for supplier selection and inventory management since the lead time is refined according to the disruption information. In other words, this solution approach is useful to dea with disruption risk mitigation.

Sensitivity analysis has been performed to understand the impact of the degree of intervention between two decision-makers on the supplier’s score and ranking. In addition, an analysis of the impact of the objective’s weight on the supplier’s score has also been presented. The managerial implications derived from the analysis provide insight for decision-making under multi-criteria and multi-decision makers. The associated weight has an important impact on the reliability and accuracy of the decision results. In other words, the degree of intervention needs to be reasonably assigned among the decision makers to achieve a consensus that results in a more reliable decision. Since the correct trade-off among objectives is critical to the decision, the importance of criteria should be determined properly.

This study has limitations that might lead to interesting future research. Despite the fact that the study has addressed the risk factors (i.g., disruptions, imperfect quality, delivery delay), other risk factors in global sourcing might also exist due to political or social instability. The future study can be extended, considering this aspect to sustain resilient supplier selection in global sourcing. Furthermore, the increase of awareness on sustainability might compel firms to identify related criteria and incorporate them into supplier selection. Developing a framework for supplier evaluation under sustainability could also be an interesting future research direction.

## CRediT authorship contribution statement

Thomy Eko Saputro: Conceptualization, Methodology, Investigation, Writing – original draft. Gonçalo Figueira: Supervision, Writing – review & editing, Validation. Bernardo Almada-Lobo: Supervision, Writing – review & editing, Validation.

## Declaration of competing interest

The authors declare that they have no known competing finan cial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The data was presented in the manuscript.

Table C.16  
Interval values for supplier assessment.

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>[4, 5]</td><td>[5, 6]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>2</td><td>[4, 5]</td><td>[3, 4]</td><td>[6, 9]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td></tr><tr><td>3</td><td>[3, 4]</td><td>[5, 6]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>4</td><td>[4, 5]</td><td>[1, 3]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>5</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td></tr><tr><td>6</td><td>[3, 4]</td><td>[3, 4]</td><td>[6, 9]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td><td>[1, 3]</td><td>[1, 3]</td></tr><tr><td>7</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>8</td><td>[4, 5]</td><td>[3, 4]</td><td>[6, 9]</td><td>[6, 9]</td><td>[3, 4]</td><td>[5, 6]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td></tr><tr><td>9</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>10</td><td>[4, 5]</td><td>MG</td><td>[3, 4]</td><td>[6, 9]</td><td>[1, 3]</td><td>[3, 4]</td><td>[6, 9]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[5, 6]</td></tr></table>

Table C.17

DM2: Linguistic variables of supplier assessment for problem (1).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>F</td><td>MP</td><td>G</td><td>MG</td><td>MP</td><td>MG</td><td>F</td><td>F</td><td>F</td><td>MP</td><td>MP</td><td>F</td></tr><tr><td>2</td><td>MP</td><td>F</td><td>G</td><td>F</td><td>P</td><td>MG</td><td>F</td><td>F</td><td>F</td><td>P</td><td>P</td><td>MP</td></tr><tr><td>3</td><td>P</td><td>P</td><td>MP</td><td>F</td><td>P</td><td>MG</td><td>MP</td><td>MP</td><td>P</td><td>MP</td><td>P</td><td>MP</td></tr><tr><td>4</td><td>F</td><td>MP</td><td>MP</td><td>F</td><td>MP</td><td>MP</td><td>MG</td><td>P</td><td>MG</td><td>MG</td><td>P</td><td>F</td></tr><tr><td>5</td><td>F</td><td>P</td><td>P</td><td>G</td><td>P</td><td>F</td><td>G</td><td>F</td><td>P</td><td>F</td><td>MP</td><td>MG</td></tr><tr><td>6</td><td>P</td><td>MG</td><td>F</td><td>MG</td><td>MP</td><td>MG</td><td>MP</td><td>F</td><td>P</td><td>MP</td><td>P</td><td>MP</td></tr><tr><td>7</td><td>P</td><td>MG</td><td>G</td><td>MG</td><td>P</td><td>P</td><td>G</td><td>F</td><td>P</td><td>MP</td><td>P</td><td>MG</td></tr><tr><td>8</td><td>MP</td><td>MP</td><td>P</td><td>MG</td><td>P</td><td>MG</td><td>MP</td><td>P</td><td>MG</td><td>P</td><td>MP</td><td>MP</td></tr><tr><td>9</td><td>P</td><td>F</td><td>F</td><td>G</td><td>MP</td><td>F</td><td>F</td><td>P</td><td>MG</td><td>MG</td><td>MP</td><td>MG</td></tr><tr><td>10</td><td>MP</td><td>MP</td><td>MP</td><td>F</td><td>MP</td><td>F</td><td>MG</td><td>MP</td><td>MP</td><td>P</td><td>P</td><td>MP</td></tr></table>

Table C.18  
DM2: Interval values of supplier assessment for problem (1).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>[4, 5]</td><td>[3, 4]</td><td>[6, 9]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td></tr><tr><td>2</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[1, 3]</td><td>[3, 4]</td></tr><tr><td>3</td><td>[1, 3]</td><td>[1, 3]</td><td>[3, 4]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td></tr><tr><td>4</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td><td>[1, 3]</td><td>[5, 6]</td><td>[5, 6]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>5</td><td>[4, 5]</td><td>[1, 3]</td><td>[1, 3]</td><td>[6, 9]</td><td>[1, 3]</td><td>[4, 5]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[4, 5]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>6</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td></tr><tr><td>7</td><td>[1, 3]</td><td>[5, 6]</td><td>[6, 9]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td></tr><tr><td>8</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td><td>[1, 3]</td><td>[5, 6]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td></tr><tr><td>9</td><td>[1, 3]</td><td>[4, 5]</td><td>[4, 5]</td><td>[6, 9]</td><td>[3, 4]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>10</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td><td>[1, 3]</td><td>[3, 4]</td></tr></table>

Table C.19  
DM1: Linguistic variables of supplier assessment for problem (2).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>P</td><td>F</td><td>MG</td><td>G</td><td>P</td><td>P</td><td>G</td><td>F</td><td>P</td><td>MP</td><td>MP</td><td>P</td></tr><tr><td>2</td><td>MP</td><td>P</td><td>MP</td><td>MP</td><td>MP</td><td>P</td><td>MP</td><td>MP</td><td>MP</td><td>F</td><td>MP</td><td>F</td></tr><tr><td>3</td><td>MP</td><td>MP</td><td>F</td><td>MG</td><td>MP</td><td>MG</td><td>G</td><td>MP</td><td>MP</td><td>MP</td><td>P</td><td>P</td></tr><tr><td>4</td><td>F</td><td>MP</td><td>F</td><td>MP</td><td>MP</td><td>MG</td><td>F</td><td>MP</td><td>F</td><td>MP</td><td>MP</td><td>MG</td></tr><tr><td>5</td><td>MP</td><td>MP</td><td>MG</td><td>G</td><td>P</td><td>P</td><td>MG</td><td>F</td><td>F</td><td>F</td><td>MP</td><td>MG</td></tr><tr><td>6</td><td>MP</td><td>MG</td><td>MG</td><td>MP</td><td>MP</td><td>MP</td><td>MG</td><td>F</td><td>MG</td><td>P</td><td>MP</td><td>P</td></tr><tr><td>7</td><td>F</td><td>P</td><td>MG</td><td>F</td><td>MP</td><td>P</td><td>MG</td><td>P</td><td>MP</td><td>P</td><td>MP</td><td>P</td></tr><tr><td>8</td><td>F</td><td>P</td><td>MG</td><td>G</td><td>MP</td><td>MG</td><td>MP</td><td>F</td><td>P</td><td>MP</td><td>MP</td><td>P</td></tr><tr><td>9</td><td>F</td><td>MG</td><td>MG</td><td>MG</td><td>MP</td><td>P</td><td>F</td><td>F</td><td>F</td><td>P</td><td>MP</td><td>P</td></tr><tr><td>10</td><td>P</td><td>F</td><td>F</td><td>MG</td><td>MP</td><td>P</td><td>MG</td><td>P</td><td>P</td><td>MP</td><td>P</td><td>MP</td></tr></table>

## Appendix A. Qualitative criteria: Strategic items suppliers

Appendix C. Decision makers judgment

See Table A.15.

See Tables C.16–C.22.

Appendix B. Convergence of genetic algorithm

Appendix D. Input parameters

See Fig. B.5.

See Table D.23.

Table C.20  
DM1: Interval values of supplier assessment for problem (2).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>[1, 3]</td><td>[4, 5]</td><td>[5, 6]</td><td>[6, 9]</td><td>[1, 3]</td><td>[1, 3]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td></tr><tr><td>2</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td></tr><tr><td>3</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td><td>[6, 9]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td><td>[1, 3]</td></tr><tr><td>4</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>5</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td><td>[6, 9]</td><td>[1, 3]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>6</td><td>[3, 4]</td><td>[5, 6]</td><td>[5, 6]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[5, 6]</td><td>[4, 5]</td><td>[5, 6]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td></tr><tr><td>7</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td></tr><tr><td>8</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[6, 9]</td><td>[3, 4]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td><td>[1, 3]</td></tr><tr><td>9</td><td>[4, 5]</td><td>[5, 6]</td><td>[5, 6]</td><td>[5, 6]</td><td>[3, 4]</td><td>[1, 3]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td></tr><tr><td>10</td><td>[1, 3]</td><td>[4, 5]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td></tr></table>

Table C.21  
DM2: Linguistic variables of supplier assessment for problem (2).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>F</td><td>F</td><td>G</td><td>MP</td><td>MP</td><td>MP</td><td>G</td><td>F</td><td>P</td><td>MP</td><td>P</td><td>MG</td></tr><tr><td>2</td><td>MP</td><td>P</td><td>MP</td><td>G</td><td>MP</td><td>F</td><td>G</td><td>P</td><td>MP</td><td>MG</td><td>P</td><td>F</td></tr><tr><td>3</td><td>MP</td><td>MP</td><td>F</td><td>MG</td><td>P</td><td>MG</td><td>G</td><td>MP</td><td>MG</td><td>P</td><td>P</td><td>MG</td></tr><tr><td>4</td><td>MP</td><td>MG</td><td>F</td><td>MG</td><td>MP</td><td>MG</td><td>MP</td><td>F</td><td>MG</td><td>MG</td><td>P</td><td>F</td></tr><tr><td>5</td><td>F</td><td>F</td><td>P</td><td>MG</td><td>MP</td><td>P</td><td>MP</td><td>F</td><td>F</td><td>P</td><td>MP</td><td>MG</td></tr><tr><td>6</td><td>MP</td><td>P</td><td>G</td><td>G</td><td>P</td><td>MP</td><td>P</td><td>F</td><td>MG</td><td>P</td><td>P</td><td>F</td></tr><tr><td>7</td><td>F</td><td>MG</td><td>MG</td><td>MG</td><td>P</td><td>P</td><td>G</td><td>F</td><td>MP</td><td>P</td><td>MP</td><td>MP</td></tr><tr><td>8</td><td>F</td><td>F</td><td>F</td><td>MG</td><td>MP</td><td>MG</td><td>P</td><td>P</td><td>F</td><td>MG</td><td>MP</td><td>F</td></tr><tr><td>9</td><td>F</td><td>P</td><td>MP</td><td>G</td><td>MP</td><td>P</td><td>F</td><td>MP</td><td>F</td><td>MP</td><td>P</td><td>MG</td></tr><tr><td>10</td><td>F</td><td>MG</td><td>F</td><td>F</td><td>MP</td><td>P</td><td>F</td><td>F</td><td>F</td><td>F</td><td>MP</td><td>P</td></tr></table>

Table C.22

DM2: Interval values of supplier assessment for problem (2).

<table><tr><td rowspan="2">Supplier</td><td colspan="12">Sub-criteria</td></tr><tr><td>SC1</td><td>SC2</td><td>SC3</td><td>SC4</td><td>SC5</td><td>SC6</td><td>SC7</td><td>SC8</td><td>SC9</td><td>SC10</td><td>SC11</td><td>SC12</td></tr><tr><td>1</td><td>[4, 5]</td><td>[4, 5]</td><td>[6, 9]</td><td>[3, 4]</td><td>[3, 4]</td><td>[3, 4]</td><td>[6, 9]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td></tr><tr><td>2</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[6, 9]</td><td>[3, 4]</td><td>[4, 5]</td><td>[6, 9]</td><td>[1, 3]</td><td>[3, 4]</td><td>[5, 6]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>3</td><td>[3, 4]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[1, 3]</td><td>[5, 6]</td><td>[6, 9]</td><td>[3, 4]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[5, 6]</td></tr><tr><td>4</td><td>[3, 4]</td><td>[5, 6]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td><td>[5, 6]</td><td>[5, 6]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>5</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[5, 6]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[4, 5]</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[5, 6]</td></tr><tr><td>6</td><td>[3, 4]</td><td>[1, 3]</td><td>[6, 9]</td><td>[6, 9]</td><td>[1, 3]</td><td>[3, 4]</td><td>[1, 3]</td><td>[4, 5]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td></tr><tr><td>7</td><td>[4, 5]</td><td>[5, 6]</td><td>[5, 6]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[6, 9]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[3, 4]</td><td>[3, 4]</td></tr><tr><td>8</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[5, 6]</td><td>[1, 3]</td><td>[1, 3]</td><td>[4, 5]</td><td>[5, 6]</td><td>[3, 4]</td><td>[4, 5]</td></tr><tr><td>9</td><td>[4, 5]</td><td>[1, 3]</td><td>[3, 4]</td><td>[6, 9]</td><td>[3, 4]</td><td>[1, 3]</td><td>[4, 5]</td><td>[3, 4]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[5, 6]</td></tr><tr><td>10</td><td>[4, 5]</td><td>[5, 6]</td><td>[4, 5]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[4, 5]</td><td>[3, 4]</td><td>[1, 3]</td></tr></table>

Table D.23  
Input parameters for slow movers.

<table><tr><td colspan="2">Parameters</td><td>Values</td><td>Units</td></tr><tr><td colspan="4">Plant, i ∈ I</td></tr><tr><td>Demand</td><td> $λ_i$ </td><td>: U(40, 100)</td><td>unit/year</td></tr><tr><td>Setup costs</td><td> $o_i$ </td><td>: U(500, 1000)</td><td>$/order</td></tr><tr><td>Holding costs</td><td> $h_i$ </td><td>: U(10, 15)</td><td>$/unit/year</td></tr><tr><td>Shortage costs</td><td> $s_i$ </td><td>: U(30, 50)</td><td>$/unit/year</td></tr><tr><td>Imperfect items&#x27; holding costs</td><td> $h'_i$ </td><td>: U(30, 50)</td><td>$/unit/year</td></tr><tr><td>External failure costs</td><td> $a_i$ </td><td>: U(5, 7.5)</td><td>$/unit</td></tr><tr><td>Location</td><td></td><td>: [U(0, 500), U(0, 500)]</td><td></td></tr><tr><td colspan="4">Supplier, j ∈ J</td></tr><tr><td>Supply capacity</td><td> $b_j$ </td><td>: U(100, 300)</td><td>unit</td></tr><tr><td>Imperfect rate</td><td> $k_j$ </td><td>: U(0.10, 0.20)</td><td></td></tr><tr><td>Vehicle capacity</td><td> $u_j$ </td><td>: U(60, 90)</td><td>unit/vehicle</td></tr><tr><td>Disruption frequency</td><td> $θ_j$ </td><td>: U(1, 7)</td><td>days</td></tr><tr><td>Disruption length</td><td> $v_j$ </td><td>: U(0.5, 2)</td><td>days</td></tr><tr><td>Contractual costs</td><td> $f_j$ </td><td>: U(10000, 17000)</td><td>$</td></tr><tr><td>Unit purchasing costs</td><td> $c_j$ </td><td>: U(25, 60)</td><td>$/unit</td></tr><tr><td>Location</td><td></td><td>: [U(0, 500), U(0, 500)]</td><td></td></tr><tr><td colspan="4">Plant-Supplier, i ∈ I, j ∈ J</td></tr><tr><td>Fixed transportation costs</td><td> $p_{ij}$ </td><td>: U(250, 500)</td><td>$/order/vehicle</td></tr><tr><td>Variable transportation costs</td><td> $r_{ij}$ </td><td>: U(0.75, 3)</td><td>$/mile/vehicle</td></tr><tr><td>Lead time</td><td> $l_{ij}$ </td><td>:  $\left( \frac{U(1.2)}{60} \right) d_{ij}$ </td><td>hours</td></tr></table>

## References

Abdallah, M., Hamdan, S., & Shabib, A. (2021). A multi-objective optimization mode for strategic waste management master plans. Journal of Cleaner Production, 284, Article 124714.

Aissaoui, N., Haouari, M., & Hassini, E. (2007). Supplier selection and order lot sizing modeling: A review. Computers & Operations Research, 34(12), 3516–3540.

Awasthi, A., Govindan, K., & Gold, S. (2018). Multi-tier sustainable global supplier se lection using a fuzzy AHP-VIKOR based approach. International Journal of Production Economics, 195, 106–117.

Ayhan, M. B., & Kilic, H. S. (2015). A two stage approach for supplier selection problem in multi-item/multi-supplier environment with quantity discounts. Computers & Industrial Engineering, 85, 1–12.

Bang, J., & Kim, Y. (2010). Hierarchical production planning for semiconductor wafer fabrication based on linear programming and discrete-event simulation. IEEE Transactions on Automation Science and Engineering, 7(2), 326–336.

Bektur, G. (2020). An integrated methodology for the selection of sustainable suppliers and order allocation problem with quantity discounts, lost sales and varying supplier availabilities. Sustainable Production and Consumption, 23, 111–127.

Chai, J., Liu, J. N., & Ngai, E. W. (2013). Application of decision-making techniques in supplier selection: A systematic review of literature. Expert Systems with Applications, 40(10), 3872–3885.

Chang, D.-Y. (1996). Applications of the extent analysis method on fuzzy AHP. European Journal of Operational Research. 95(3). 649–655.

Cheraghalipour, A., & Farsad, S. (2018). A bi-objective sustainable supplier selection and order allocation considering quantity discounts under disruption risks: A case study in plastic industry. Computers & Industrial Engineering, 118, 237–250.

de’Boer, L., Labro, E., & Morlacchi, P. (2001). A review of methods supporting supplier selection. European Journal of Purchasing & Supply Management, 7(2), 75–89.

Demirel, T., Demirel, N. Ç., & Kahraman, C. (2008). Fuzzy analytic hierarchy proces and its application. In C. Kahraman (Ed.), Fuzzy multi-criteria decision making: theory and applications with recent developments (pp. 53–83). Boston, MA: Springer US.

Dogan, O., Deveci, M., Canıtez, F., & Kahraman, C. (2020). A corridor selection for locating autonomous vehicles using an interval-valued intuitionistic fuzzy AHP and TOPSIS method. Soft Computing, 24, 8937–8953.

Feng, J., & Gong, Z. (2020). Integrated linguistic entropy weight method and multiobjective programming model for supplier selection and order allocation in a circular economy: A case study. Journal of Cleaner Production. 277. Article 122597.

Figueira, G., & Almada-Lobo, B. (2014). Hybrid simulation–optimization methods: A taxonomy and discussion. Simulation Modelling Practice and Theory, 46, 118–134, Simulation-Optimization of Complex Systems: Methods and Applications.

Firouz, M., Keskin, B. B., & Melouk, S. H. (2017). An integrated supplier selection and inventory problem with multi-sourcing and lateral transshipments. Omega, 70, 77–93.

Ghadimi, P.. Ghassemi Toosi, F.. & Heavey, C. (2018). A multi-agent systems approach for sustainable supplier selection and order allocation in a partnership supply chain. European Journal of Operational Research, 269(1), 286–301.

Gören, H. G. (2018). A decision framework for sustainable supplier selection and orde allocation with lost sales. Journal of Cleaner Production, 183, 1156–1169.

Haeri, S. A. S., & Rezaei, J. (2019). A grey-based green supplier selection model for uncertain environments. Journal of Cleaner Production, 221, 768–784.

Haleh, H., & Hamidi, A. (2011). A fuzzy MCDM model for allocating orders to suppliers in a supply chain under uncertainty over a multi-period time horizon. Expert Systems with Applications. 38(8). 9076–9083

Hamdan, S., & Cheaitou, A. (2017). Supplier selection and order allocation with green criteria: An MCDM and multi-objective optimization approach. Computers & Operations Research, 81, 282–304

Hasan, M. M., Jiang, D., Ullah, A. S., & Noor-E-Alam, M. (2020). Resilient supplie selection in logistics 4.0 with heterogeneous information. Expert Systems with Applications. 139 Article 112799

Hwang, C. L., & Yoon, K. (1981). Multiple attribute decision making. Berlin, Germany: Springer-Verlag.

Igoulalene, I., Benyoucef, L., & Tiwari, M. K. (2015). Novel fuzzy hybrid multi-criteria group decision making approaches for the strategic supplier selection problem. Expert Systems with Applications, 42(7), 3342–3356.

Jahanshahloo, G., Hosseinzadeh Lotfi, F., & Davoodi, A. (2009). Extension of TOPSIS for decision-making problems with interval data: Interval efficiency. Mathematical and Computer Modelling. 49(5). 1137–1142.

Kaur, H., & Prakash Singh, S. (2021). Multi-stage hybrid model for supplier selection and order allocation considering disruption risks and disruptive technologies. International Journal of Production Economics, 231, Article 107830.

Kellner, F., & Utz, S. (2019). Sustainability in supplier selection and order allocation: Combining integer variables with Markowitz portfolio theory. Journal of Cleaner Production, 214, 462–474.

Keskin, B. B., Melouk, S. H., & Meyer, I. L. (2010). A simulation-optimization approach for integrated sourcing and inventory decisions. Computers & Operations Research, 37(9), 1648–1661.

Kilic, H. S., & Yalcin, A. S. (2020). Modified two-phase fuzzy goal programming integrated with IF-TOPSIS for green supplier selection. Applied Soft Computing, 93, Article 106371.

Kiracı, K., & Akan, E. (2020). Aircraft selection by applying AHP and TOPSIS in interval type-2 fuzzy sets. Journal of Air Transport Management, 89, Article 101924.

Kraljic, P. (1983). Purchasing must become supply management. (pp. 110–117).

Liu. Y.. Eckert. C. M., & Earl. C. (2020). A review of fuzzy AHP methods for decisionmaking with subjective judgements. Expert Systems with Applications, 161, Article 113738.

Moheb-Alizadeh, H., & Handfield, R. (2019). Sustainable supplier selection and order allocation: A novel multi-obiective programming model with a hybrid solutior approach. Computers & Industrial Engineering, 129, 192–209.

Rajesh, R., & Ravi, V. (2015). Supplier selection in resilient supply chains: a grey relational analysis approach. Journal of Clegner Production. 86. 343–359

Saputro, T. E., Figueira, G., & Almada-Lobo, B. (2020). Integrating supplier selection with inventory management under supply disruptions. Interngtional Journal of Production Research, 1–19

Saputro, T. E., Figueira, G., & Almada-Lobo, B. (2021). Integrating supplier selection with inventory management under supply disruptions. International Journal of Production, Research 59(11). 3304–3322

Saputro, T. E., Figueira, G., & Almada-Lobo, B. (2022). A comprehensive framework and literature review of supplier selection under different purchasing strategies. Computers & Industrial Engineering, 167, Article 108010.

Shih, H.-S., Shyur, H.-J., & Lee, E. S. (2007). An extension of TOPSIS for group decision making. Mathematical and Computer Modelling. 45(7). 801–813

Singh, A. (2014). Supplier evaluation and demand allocation among suppliers in a supply chain. Journal of Purchasing and Supply Management, 20(3), 167–176.

Toffano, F., Garraffa, M., Lin, Y., Prestwich. S., Simonis, H., & Wilson, N. (2022). A multi-objective supplier selection framework based on user-preferences. Annals of Operations Research, 308, 609–640.

Tordecilla, R. D., Juan, A. A., Montoya-Torres, J. R., Quintero-Araujo, C. L., & Panadero, J. (2021). Simulation-optimization methods for designing and assessing resilient supply chain networks under uncertainty scenarios: A review. Simulation Modelling Practice and Theory, 106, Article 102166.

Wang, L.-F., & Shi, L.-Y. (2013). Simulation optimization: A review on theory and applications. Acta Automatica Sinica, 39(11), 1957–1968.

Weber, C. A., Current, J., & Desai, A. (20o0). An optimization approach to determining the number of vendors to employ. Supply Chain Management: An International Journal, 5(2), 90–98.

Yadav, V., & Sharma, M. K. (2016). Multi-criteria supplier selection model using the analytic hierarchy process approach. Journal of Modelling in Management, 143(1), 326–354.

Zardari, N. H., Ahmed, K., Shirazi, S. M., & Yusop, Z. B. (2015). Weighting methods and their effects on multi-criteria decision making model outcomes in water resources management. Berlin, Germany: Springer.

Zsidisin, G. A. (2003). A grounded definition of supply risk. Journal of Purchasing and Supply Management, 9(5), 217–224.