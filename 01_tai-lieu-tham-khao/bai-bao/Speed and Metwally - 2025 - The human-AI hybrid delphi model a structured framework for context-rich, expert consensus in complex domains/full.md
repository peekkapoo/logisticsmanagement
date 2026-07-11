# The Human–AI Hybrid Delphi Model: A Structured Framework for Context-Rich, Expert Consensus in Complex Domains

Cathy Speed<sup>1†</sup> and Ahmed A. Metwally<sup>1‡</sup>

<sup>1</sup>Google Research, <sup>†</sup>Work done while at Google Research

Expert consensus plays a critical role in domains where evidence is complex, conflicting, or insuficient for direct prescription. Traditional methods, such as Delphi studies, consensus conferences, and systematic guideline synthesis, ofer structure but face limitations including high panel burden, interpretive oversimplification, and suppression of conditional nuance. These challenges are now exacerbated by information overload, fragmentation of the evidence base, and increasing reliance on publicly available sources that lack expert filtering. This study introduces and evaluates a Human–AI Hybrid Delphi (HAH-Delphi) framework designed to augment expert consensus development by integrating a generative AI model (Gemini 2.5 Pro), small panels of senior human experts, and structured facilitation. The HAH-Delphi was tested in three phases: retrospective replication, prospective comparison, and applied deployment in two applied domains (endurance training and resistance and mixed cardio/strength training). The AI replicated 95% of published expert consensus conclusions in Phase I and showed 95% directional agreement with senior human experts in Phase II, though it lacked experiential and pragmatic nuance. In Phase III, compact panels of six senior experts achieved >90% consensus coverage and reached thematic saturation before the final participant. The AI provided consistent, literature-grounded scafolding that supported divergence resolution and accelerated saturation. The HAH-Delphi framework ofers a flexible, scalable approach for generating high-quality, context-sensitive consensus. Its successful application across health, coaching, and performance science confirms its methodological robustness and supports its use as a foundation for generating conditional, personalised guidance and published consensus frameworks at scale.

## 1. Introduction

Achieving reliable and nuanced expert consensus is fundamental to advancing evidence-informed practice across the full spectrum of healthcare and applied sciences. From the development of clinical guidelines and rehabilitation protocols to public health recommendations and performance training principles, structured group judgment plays a pivotal role, particularly where empirical evidence is vast, complex, or equivocal, and requires interpretation to become actionable in real-world settings. In such cases, the ability to synthesise informed judgment across experienced professionals is not simply useful, however, it is essential for navigating uncertainty and enabling progress.

The Delphi technique has served as a widely accepted method for structured consensus building for over half a century (Boulkedid et al., 2011; Dalkey and Helmer, 1963; Fink-Hafner et al., 2019; Hall et al., 2018; Hasson et al., 2000; Linstone et al., 1975; Nasa et al., 2021,?; Niederberger and Spranger, 2020; Sinha et al., 2011). Originally designed for technological forecasting, it has since become central to health sciences research, underpinning processes from guideline formulation to the identification of research priorities and the definition of clinical competencies. Its defining features, anonymous input to reduce dominance bias, iterative rounds to enable refinement, structured feedback, and statistical aggregation, have ensured its adaptability across diverse contexts.

However, despite its widespread use and enduring value, the conventional Delphi method is increasingly challenged by a set of practical and methodological limitations that can impair feasibility, diminish insight quality, and reduce the interpretability or applicability of its outputs (Boulkedid et al., 2011; Dalkey and Helmer, 1963; Fink-Hafner et al., 2019; Hall et al., 2018; Hasson et al., 2000; Linstone et al., 1975; Nasa et al., 2021,?; Niederberger and Spranger, 2020; Shang, 2023; Sinha et al., 2011). A persistent barrier lies in the resource demands associated with assembling and managing large expert panels, which in some studies has exceeded 100 participants (Shang, 2023). Sustaining engagement through multiple rounds commonly proves dificult, with attrition rates reported to surpass 90% in some studies (Shang, 2023). These challenges not only compromise the stability and validity of the resulting consensus but also limit the method’s accessibility for time-constrained or highly specialised experts.

At a methodological level, Delphi processes can inadvertently constrain the very nuance they aim to capture. In pursuit of consensus, responses may converge toward statistical averages or generalised statements, obscuring the conditional logic, domain-specific caveats, and divergent interpretations that define expert-level judgment. Heterogeneous panels may further exacerbate this tendency, amplifying lowest-common-denominator agreement while sidelining minority insights that migh otherwise carry significant applied value. Moreover, when consensus is narrowly defined by numerical agreement, it can suppress dissent or misrepresent partial alignment, diminishing the ecological validity of the findings.

The burden placed on facilitators to synthesise qualitative input across large panels and multiple iterations introduces both interpretive load and potential bias. As facilitators necessarily act as intermediaries in shaping feedback summaries, their framing and judgment influence how perspectives are represented back to the panel. Finally, methodological inconsistencies across Delphi studies, particularly around definitions of consensus and treatment of qualitative data, reduce reproducibility and limit comparability between studies (Boulkedid et al., 2011; Dalkey and Helmer, 1963; Fink-Hafner et al., 2019; Hall et al., 2018; Hasson et al., 2000; Linstone et al., 1975; Nasa et al., 2021,?; Niederberger and Spranger, 2020; Shang, 2023; Sinha et al., 2011).

These limitations are not confined to Delphi. Many widely used consensus processes, including modified Delphi formats, structured single-round expert panels, and evidence-based guideline working groups, exhibit similar weaknesses: loss of conditional nuance, inconsistent definitions of consensus, and limited transparency in how expert reasoning is synthesised. Despite procedural diferences, these formats often rely on unstructured synthesis and binary agreement metrics, leaving them vulnerable to the same interpretive flattening and lack of reproducibility. A new model must therefore address not only the specific limitations of Delphi, but the broader structural challenges of expert consensus across designs.

Together, these limitations highlight a need for innovation. This study proposes that Generative Artificial Intelligence (GenAI), when used within rigorously defined boundaries and under expert facilitation, ofers a powerful means to address these longstanding constraints, not through automation of expert reasoning, but through its strategic augmentation. The HAH-Delphi model developed and evaluated herein introduces a reconfigured approach to consensus generation, one that reconsiders panel structure, redistributes cognitive labour, and systematises the analysis of qualitative insight.

This study introduces a Human–AI Hybrid Delphi (HAH-Delphi) model designed to meet that need. It reconfigures the consensus process to balance AI-supported synthesis with structured expert interpretation, enabling small senior panels to generate rich, conditional, and implementable guidance. The model introduces two core methodological innovations: a structured qualitative saturation framework to assess expert suficiency, and a four-tier consensus classification system (Strong, Conditional, Operational, Divergent) that moves beyond simplistic percentage thresholds. These components are integrated through structured facilitation, constrained AI synthesis, and justification-based analysis, supporting the generation of context-sensitive, transparent consensus across a range of expert formats.

Advanced GenAI models, such as Gemini 2.5 Pro (Comanici et al., 2025), are uniquely positioned to retrieve, synthesise, and contextualise extensive scientific evidence at a breadth and speed beyond human capability. Their integration into the early stages of the Delphi process relieves senior experts of lower-order retrieval and synthesis tasks, allowing them to concentrate on what AI cannot yet replicate: deep contextual interpretation, application of experiential wisdom, and the articulation of conditional, domain-specific reasoning. This rebalancing supports the use of smaller, more experienced panels without compromising the breadth or depth of the outputs.

A central methodological innovation in this HAH-Delphi model is the use of systematic qualitative analysis to evaluate thematic saturation in expert reasoning. This step, seldom incorporated in traditional Delphi studies, provides a direct mechanism to determine whether the insights generated by a small senior panel are suficiently comprehensive, ofering a grounded measure of expert suficiency and content completeness. The model further enables structured comparisons across difering levels of expertise, as demonstrated through sub-studies involving less experienced participants, to explore how reasoning depth and alignment vary across groups.

Crucially, the model adheres to the principle of augmentation rather than substitution. All AI-derived material is generated from a constrained corpus of trusted, predominantly public sources, set and validated by a domain-expert facilitator prior to being made available to the panel. This procedural rigour is designed to mitigate risks such as hallucinated content, overconfidence, or bias propagation, which are issues increasingly recognised in large language models. This study aimed to develop, implement, and evaluate this HAH-Delphi model, testing its capacity to enhance epistemic clarity, interpretive richness, and operational feasibility within the consensus-building process. In doing so, it explores the redefinition of what constitutes expert input, how panels are composed, and how best to extract meaningful insight from their contributions in an era of human–AI collaboration.

This study aimed to develop, implement, and evaluate the HAH-Delphi framework capable of addressing longstanding limitations in expert consensus generation, particularly those afecting interpretive clarity, conditional nuance, and methodological feasibility across real-world formats. Specifically, we sought to:

<sup>•</sup> Validate the synthesis capabilities of generative AI by assessing whether an AI model could replicate the item-level outcomes of six previously published expert consensus sources, including Delphi studies, modified Delphi formats, structured panels, and guideline-derived recommendations, when constrained to using only contemporaneous public evidence.

<sup>•</sup> Compare the reasoning depth of human experts and AI by analysing qualitative justifications across a shared set of consensus items within a single domain (chronic insomnia).

<sup>•</sup> Test the HAH-Delphi model in applied domains to determine whether small panels of senior experts, supported by AI, could achieve rich, context-sensitive consensus with thematic saturation.

<sup>•</sup> Explore the contribution of less experienced experts and assess how their input difered in structure, alignment, and reasoning depth from that of senior experts.

<sup>•</sup> The overarching goal was to evaluate whether a compact, structured, and generalisable Human–AI hybrid model could enhance the depth, transparency, and scalability of expert consensus development, across diverse domains and consensus formats.

## 2. Methods

## 2.1. Study Design and Phases

This study employed a three-phase design to develop, test, and evaluate the HAH-Delphi model. Each phase was designed to address a specific methodological aim, progressing from retrospective simulation, through prospective comparison, to applied implementation in complex, real-world domains. We developed and evaluated the HAH-Delphi framework using Gemini 2.5 Pro (Comanic et al., 2025). Throughout this paper, Gemini 2.5 Pro will be abbreviated to Gemini.

## 2.2. Phase I (Retrospective Validation)

Phase I tested whether a generative AI model (Gemini) could replicate item-level outcomes from six previously published expert consensus sources, using only contemporaneous public-domain evidence available at the time of each study (Figure 1). While formal Delphi studies were a key focus, the included sources also encompassed modified Delphi processes, structured single-round expert panels, and high-grade guideline-derived consensus statements. This methodological diversity was intentional, designed to reflect the varied formats through which expert-derived standards are developed in real world practice. The six selected studies spanned a range of clinical and applied domains, including insomnia, sedentary behaviour, concussion, low back pain, rotator cuf disorders, and hypertension, and allowed evaluation of the AI’s alignment with both Delphi-specific and broader expert consensus outputs. The corresponding consensus formats were: Delphi (insomnia, rotator cuf), modified Delphi (sedentary behaviour), structured panel (concussion), and guideline-derived consensus (low back pain, hypertension). Full study details, including topic, structure, and consensus type, are provided in Appendix A .

In this phase, Gemini was constrained to a predefined corpus of publicly available sources, as specified in Appendix A. For panel-based studies, the corpus was restricted to before the first item distribution or expert convening; where this was unknown, a cutof of at least 9 months prior to publication was applied. For systematic reviews, the cutof was set to the publication date. It was explicitly prohibited from accessing non-public material, including full-text articles behind paywalls, post-publication summaries, or any content with access restrictions. All AI inputs were structured to mirror the original study formats (e.g. Likert ratings, binary decisions, prioritisation tasks). The expert facilitator ensured corpus fidelity, extracted and reformatted all items, prompted the AI, and analysed outputs for comparison.

## 2.3. Phase II (Prospective Study)

Phase II re-administered the questions from one of the Phase I benchmark studies, on chronic insomnia in primary care, to a new panel of six human experts (Figure 2). These clinicians were independently contracted as subject matter experts through a third-party medical expert service. Participants rated 20 items using a 5-point Likert scale and provided open-text justifications. Gemini was given the same items and prompted using updated evidence from within its allowed corpus (current to February 2025). All responses were blinded. This phase enabled direct item-level comparison of AI and human responses, including alignment of both conclusions and reasoning structures.

## 2.4. Phase III: Applied Delphi in Endurance and Mixed Cardio/Strength Training

In Phase III, the HAH-Delphi model was implemented in two complex, high-variability training domains: (A) recreational endurance running and (B) resistance and mixed cardio/strength training.

![](images/328ce2b36a93d853e18af8c4d89c0d7152aa071890d9bcb7dc5d077b04257727.jpg)  
Figure 1 | Phase I: Retrospective Evaluation.

![](images/a989c4c51a7ed1c4852be35a3aaacd7c7948b571971fa1545ac51ecce5d11bdb.jpg)  
Figure 2 | Phase II: Prospective Evaluation.

Both domains were selected for their relevance to large non-elite populations and their demand for nuanced, context-sensitive application of foundational principles. The primary aim of this phase was to explore how experienced practitioners apply foundational training principles in real-world scenarios, particularly when managing individual variability, life disruptions, and areas of incomplete or ambiguous scientific guidance. A secondary aim of this phase was to explore the methodological implications of incorporating an AI language model as an independent respondent within this HAH-Delphi model. This involved assessing its response patterns against human expert consensus and divergence, and understanding its potential utility in complex knowledge synthesis and consensusbuilding endeavors. A third aim of this phase was to evaluate the contribution of a panel of less experienced practitioners, whose qualifications would typically meet standard Delphi study inclusion criteria, but who lacked the same depth of applied expertise as the senior panel. Each study was conducted as a structured, single-round Delphi using a common methodological framework and was facilitated by the same expert lead.

## Definition of Experts

Senior experts held relevant qualifications and were selected for substantial applied experience, including direct responsibility for program design across varied populations. Selection prioritised real-world decision-making, contextual exposure, and the ability to contribute structured, practiceinformed input. Experts were sourced and compensated through a third-party service specializing in providing independent medical expert consultation. Less Experienced Participants are less experienced participants also held relevant qualifications but lacked the applied depth required for senior panel inclusion. They had limited responsibility for independent program design and narrower exposure to diverse coaching or training contexts.

## 2.4.1. Phase III.A: Endurance Training Study

A 143-item questionnaire was developed across 13 thematic domains, covering weekly structure, long run design, intensity zone distribution, tapering, fatigue monitoring, strength integration, rest days, and recovery management. The panel comprised six senior experts (four experienced coaches and two academic practitioners with applied credentials) and eight less experienced participants. All participants rated each item on a 5-point Likert scale and provided detailed justifications. Consensus was assessed using the predefined categories of Strong, Conditional, Operational, and Divergent. Thematic saturation was reached before the sixth expert, and all seven justification types were identified. The structured guidance document containing all consensus principles is included in Appendix D.

## 2.4.2. Phase III.B: Resistance and Mixed Cardio/Strength Training Study

This study addressed 159 items across 10 core domains, including progression logic, fatigue management, autoregulation, concurrent training, special populations, volume/intensity regulation, and adaptation over time. The panel again consisted of six senior experts (four coaches, two academic practitioners) and eight less experienced participants. The same consensus classification and justification framework were used. All seven reasoning categories were present across responses, and thematic saturation was reached before expert six. Gemini diverged on four items, each involving contextual judgment that exceeded evidence-based summaries. Consensus outputs from this study are in Appendix E.

## 2.5. Consensus Categorisation Framework

Consensus was assessed using a novel integrated framework combining Likert ratings and qualitative reasoning analysis. This allowed classification of agreement not only by score, but by the convergence or divergence of underlying logic. Conventional Delphi studies typically define consensus using arbitrary percentage thresholds (e.g. ≥70–80% agreement), with limited attention to the reasoning behind those ratings. This approach risks overstating alignment, suppressing valuable dissent, and obscuring conditional or context-specific logic, especially in domains requiring nuanced judgment (Hasson et al., 2000; Rahimi et al., 2024). Justifications, if collected, are often analysed narratively and post hoc, rather than used to structure consensus classification itself. The framework developed in this study addresses these limitations by integrating quantitative agreement with structured qualitative analysis. It introduces four categories, Strong, Conditional, Operational, and Divergent consensus, defined not only by rating convergence but by the coherence and compatibility of expert justifications (Table 1). This allows for clearer diferentiation between general agreement and conditional validity, improving interpretability, transparency, and practical relevance. Where clarification revealed that divergent views were in fact conditionally reconcilable, reclassification to ’Conditional Consensus’ was permitted. The facilitator adjudicated all such cases.

Table 1 | Consensus Categories.

<table><tr><td>Category</td><td>Definition</td></tr><tr><td>Strong Consensus</td><td>≥75% agreement (Likert 4–5 or 1–2), with clearly shared justifications indicating general applicability.</td></tr><tr><td>Conditional Consensus</td><td>Varied Likert ratings reconciled by common justifications specifying valid conditions or context-specific boundaries.</td></tr><tr><td>Operational Consensus</td><td>67–74% directional agreement, with the remaining justifications expressing only minor reservations or weak divergence.</td></tr><tr><td>No Consensus / Divergent</td><td>No coherent agreement on score or logic. Justifications were irreconcilable or conceptually incompatible.</td></tr></table>

## 2.6. Thematic Reasoning Framework

To assess reasoning structure and depth across respondent types, all free-text justifications from Phases II and III were manually coded by the facilitator using a predefined seven-category thematic framework (Table 2). This framework was developed specifically for the study to capture the layered, conditional, and source-specific nature of expert reasoning in applied domains. It distinguishes between forms of conditionality, general, population-specific, and phased, as well as sources of logic, including evidence-based, experiential, pragmatic, and principle-driven justifications. The framework supports multi-label coding and was applied consistently to both AI and human responses, enabling structured comparison of reasoning breadth, interpretive richness, and justification architecture. Each justification could be assigned more than one category, and in many cases was. Where multiple reasoning types coexisted, a multi-label classification was applied. This approach preserved the depth and structure of expert cognition and allowed the facilitator to identify layered or context-integrated reasoning. The same framework was used to analyse AI and human justifications.

Table 2 | Thematic Reasoning and Justification Framework

<table><tr><td>Reasoning Type</td><td>Definition</td></tr><tr><td>Conditional (General)</td><td>Application limited to broadly defined, non-universal conditions.</td></tr><tr><td>Conditional (Population-Based)</td><td>Reasoning tied to specific user groups, characteristics, or demographics.</td></tr><tr><td>Conditional (Temporal/Phased)</td><td>Reasoning tied to time, adaptation stage, or phase-based progression.</td></tr><tr><td>Evidence-Based</td><td>Justifications citing scientific literature, guidelines, or research synthesis.</td></tr><tr><td>Experiential</td><td>Based on applied knowledge, observation, or real-world practitioner experience.</td></tr><tr><td>Pragmatic</td><td>Centred on feasibility, logistical reality, or implementation constraints.</td></tr><tr><td>Principle-Based</td><td>Founded on theoretical constructs, physiological laws, or foundational training models.</td></tr></table>

## 2.7. Thematic Saturation Assessment

While thematic saturation is well established in qualitative research (Fusch Ph D and Ness, 2015; Guest et al., 2006), its use in Delphi studies is limited and inconsistently defined (Hasson et al., 2000; Jünger et al., 2017). Where referenced, it typically reflects item-level redundancy or convergence in scoring, rather than interpretive suficiency.

This study introduces a more robust and domain-specific application of saturation, grounded in the coverage and convergence of predefined reasoning categories across thematic domains. Unlike generic definitions, this approach captures not only the breadth but also the closure of expert insight, providing a reproducible threshold for panel suficiency based on reasoning depth rather than response volume.

Thematic saturation was assessed in Phase III to determine whether the compact senior expert panels were suficient to capture the full spectrum of relevant reasoning across both domains. Crucially, saturation was not defined by the mere absence of new reasoning types, nor by superficial item-level repetition. Instead, it required redundancy across interpretive categories and conditional structures. This represents a more stringent and functionally grounded definition than is typically employed, and is consistent with the model’s emphasis on reasoning depth over numeric suficiency.

In this study, we defined thematic saturation as the point at which:

<sup>•</sup> All seven predefined reasoning categories (see Table 2) had been represented across the expert justifications;

<sup>•</sup> No new interpretations, qualifiers, or conditional refinements were introduced within those categories that would alter the formulation or applicability of a principle; and

<sup>•</sup> Expert order became immaterial, as reasoning content showed clear convergence and repetition, indicating diminishing returns from additional input.

This definition captures not only thematic breadth, but also the stability and closure of expert insight, and was applied consistently to determine panel suficiency.

The facilitator tracked the presence and distribution of reasoning types across expert responses, mapping them to item counts and distinct thematic domains (e.g., intensity zones, recovery models, progression logic). Saturation required full coverage of reasoning categories across these domains, not simply overall emergence. This approach prevented false positives arising from superficial or isolated mentions.

New experts were considered to contribute meaningfully only if they introduced distinct conceptual approaches, interpretive refinements, or novel contextual reasoning not previously observed. In both applied studies, saturation was achieved before the final expert. The sixth participant added elaborative detail and verbal variation but did not extend the reasoning landscape or shift the interpretive architecture.

Gemini’s responses were similarly reviewed for thematic coverage using this framework, though saturation assessment focused primarily on the human panels. Less-experienced participants were coded using the same system but analysed separately. Their inputs did not expand the reasoning landscape or thematic coverage and were not required to meet saturation thresholds.

## 2.8. AI–Human Alignment Classification

Alignment between Gemini and human expert responses was evaluated independently from saturation. For each item rated by both, the AI’s conclusion and accompanying justification were compared to the consensus and reasoning structure of the expert panel (Table 3). This classification was applied in Phases II and III. The facilitator independently reviewed and adjudicated all alignment calls to ensure rigour.

Table 3 | AI-Human Panel Alignment Categories

<table><tr><td>Alignment Category</td><td>Definition</td></tr><tr><td>Fully Aligned</td><td>AI reached the same conclusion and provided a justification closely re-sembling expert reasoning.</td></tr><tr><td>Partially Aligned</td><td>AI endorsed a broadly similar stance but used different or less nuanced logic.</td></tr><tr><td>Divergent</td><td>AI provided a substantively different conclusion or justification inconsistent with expert consensus.</td></tr></table>

## 2.9. Questionnaire Design and Delphi Execution (Phase III)

The Delphi questionnaires for the endurance and strength/mixed-modality training studies were developed through structured evidence synthesis by the expert facilitator, supported by Gemini. Items were designed to examine both foundational principles and nuanced areas of disagreement or conditionality, particularly where implementation challenges or contextual variability were anticipated.

In the Endurance Training study, the questionnaire comprised 18 core questions, each accompanied by multiple follow-up questions. These were organised across 13 thematic sections, yielding a total of 179 Likert-scale items. Of these, 143 were fixed statements developed a priori, and 36 were ’Other items that allowed participants to propose and rate additional alternatives.

In the Strength/Mixed-Modality Training study, the questionnaire was structured into 10 thematic sections and included 159 Likert-scale items, also combining fixed statements and expert-specified alternatives.

All participants, including both senior and less-experienced contributors, completed the full questionnaire and were required to provide written justifications for each rating. The study employed a single-round Delphi format to prioritise depth and quality of reasoning without seeking forced convergence. The expert facilitator reviewed all responses and solicited clarifications where necessary.

## 3. Results

## 3.1. Phase I: AI Replication of Historical Consensus

Gemini replicated human expert consensus with high fidelity across six published expert consensus sources, spanning Delphi studies, modified Delphi formats, structured expert panels, and guidelinederived recommendations (Bames et al., 2012; Corp et al., 2021; Morin et al., 2024; Patricios et al., 2023; Requejo-Salinas et al., 2022; Williams et al., 2018) (see Appendix C). Of 40 core propositions reconstructed from these studies, Gemini reached full alignment with published consensus in 95% (38/40) and partial alignment in the remainder. Where there was partial alignment this reflected areas where the literature was actively evolving at the time of the original studies (e.g., shifting pharmacological guidance or emerging diagnostic thresholds). These findings support the feasibility of using a generative AI model to simulate expert consensus retrospectively, based purely on a defined historical evidence base.

This validated the first premise of the HAH-Delphi model: that AI can serve as a transparent, reproducible, and literature-grounded benchmark for consensus development, particularly in domains where synthesising broad evidence is time- or labour-intensive.

Performance was consistent across all study types, including formal Delphi studies, modified Delphi processes, structured expert panels, and high-consensus guideline syntheses, indicating that Gemini was capable of aligning with expert-derived standards regardless of the underlying consensus method. Where divergence occurred, it typically reflected areas of evolving clinical uncertainty or interpretive nuance, rather than limitations specific to any one consensus format.

## 3.2. Phase II: Prospective AI–Human Comparison

A convened panel of six contracted senior sleep experts completed the 20-item insomnia consensus questionnaire. Gemini was prompted concurrently, using access to publicly available evidence up to December 2023. Likert ratings were analysed for directional concordance, and free-text justifications were evaluated thematically.

## 3.2.1. Directional Concordance on Consensus Items

Gemini demonstrated strong directional concordance with the senior expert panel on the 20-item insomnia questionnaire. Likert-scale ratings were compared at the level of agreement bands (i.e., agree/strongly agree, neutral, disagree/strongly disagree). In 19 out of 20 items (95%), Gemini’s rating fell within the same consensus category as the human panel’s majority stance. This indicated that the AI was able to interpret and apply evidence in a way that closely mirrored the overall direction of expert opinion.

The single item where alignment was not achieved concerned the use of Dual Orexin Receptor Antagonists (DORAs). While human experts provided mixed ratings and contextualised their responses with caution about long-term data and prescribing limitations, Gemini ofered an unqualified positive endorsement based on short-term eficacy. This diference in interpretive emphasis led to a classification of divergence, despite some overlapping evidence references.

## 3.2.2. Thematic Breadth and Justification Coverage

All seven predefined reasoning categories were identified in the senior expert justifications. Experts frequently layered multiple reasoning types within single responses, such as combining phased conditionality with experiential reasoning, or embedding pragmatic concerns within evidence-based logic (Table 4). This diversity reflected the contextual complexity of applied decision-making and directly contributed to the richness of the consensus outputs. In contrast, Gemini consistently applied evidence-based and general conditional reasoning, and occasionally used principle-based logic (Table 4). However, it did not produce experiential or pragmatic justifications, and showed no use of temporal or phased reasoning. These omissions were most evident in items involving implementation trade-ofs, behavioural staging, or longitudinal adaptation, contexts that typically require real-world experience or temporally embedded logic

Table 4 | Justification/Reasoning Themes: Senior Experts Vs. Gemini.

<table><tr><td>Reasoning Theme</td><td>Senior Experts</td><td>Gemini</td></tr><tr><td>Conditional (General)</td><td>Y</td><td>Y</td></tr><tr><td>Conditional (Population-Based)</td><td>Y</td><td>Y</td></tr><tr><td>Conditional (Temporal/Phased)</td><td>Y</td><td>N</td></tr><tr><td>Evidence-Based</td><td>Y</td><td>Y</td></tr><tr><td>Experiential</td><td>Y</td><td>N</td></tr><tr><td>Pragmatic</td><td>Y</td><td>N</td></tr><tr><td>Principle-Based</td><td>Y</td><td>Y</td></tr></table>

## 3.2.3. Thematic Saturation and Panel Suficiency

Thematic saturation was assessed to determine whether the six-person senior expert panel was suficient to capture the full range of relevant reasoning types across the questionnaire. Saturation was defined not simply as the appearance of all seven reasoning categories, but as the point at which additional experts failed to introduce novel interpretive logic, alternative framings, or reasoning structures that would alter the meaning or application of the consensus principles. For saturation to be confirmed, full category coverage had to occur across the questionnaire’s thematic domains, and later experts had to ofer either elaboration or stylistic variation, but not new conceptual insight. This threshold was reached by the fifth expert. All seven reasoning types had appeared by expert four, and expert five added unique conditional refinements. Expert six provided additional phrasing and detail but introduced no new reasoning categories or distinct contextual logic. Furthermore, saturation was confirmed as robust to response order: whichever way expert input was sequenced, the cumulative reasoning landscape stabilised prior to the sixth participant. These findings confirmed that the small, senior panel was suficient to produce context-rich, interpretively complete guidance under the HAH-Delphi model.

## 3.3. Phase III: Applied Evaluation of the HAH-Delphi Model

## 3.3.1. Consensus Achievement and Coverage

In the Endurance Training study, the panel of six senior experts achieved a high degree of consensus, with 92.3% (132 out of 143) of the categorised items reaching Strong, Conditional, or Operational Consensus. No Consensus/Divergence occurred on only 7.7% (11/143) of items. These items primarily related to: (i) how to handle missed sessions, specifically whether they should be skipped, rescheduled, or adapted; (ii) the optimal design of long runs, including whether to specify fixed durations or allow flexible ranges; (iii) the necessity and placement of fixed rest days; and (iv) the use of fatigue monitoring tools and metrics in recreational populations. In each case, the divergence reflected principled diferences in emphasis, such as prioritising structure versus flexibility, or simplicity versus precision, rather than fundamental conceptual disagreement.

In the Strength/Mixed-Modality Training study, the panel of six senior experts also achieved a high level of consensus. A substantial majority of the 159 specific topics resulted in Strong Consensus (60 items, 37.7%), Conditional Consensus (94 items, 59.1%), or Operational Consensus (5 items, 3.1%). Items that did not reach consensus were limited in number and typically involved boundary conditions for application, such as the use of training to failure in specific lifts or population-dependent recovery strategies under fatigue. The full consensus principles for resistance and mixed-modality training are likewise published separately as a dedicated guidance document [see Supplementary Resource B].

## 3.3.2. Reasoning Structure and Thematic Diversity

In both studies, all seven predefined reasoning categories, Conditional (General), Conditional (Population-Based), Conditional (Temporal/Phased), Evidence-Based, Experiential, Pragmatic, and Principle-Based, were used by the senior expert panels. These reasoning types were distributed across all thematic sections of each questionnaire. Experts provided detailed, context-aware justifications that incorporated specific variables such as training age, fatigue status, and programme goals. Phrasing frequently included qualifiers such as “when appropriate,” “if fatigue permits,” or “depending on the individual’s context.” Across both panels, experts drew on practical experience, theoretical principles, and scientific evidence to produce justifications that were both context-sensitive and well-grounded. Most responses integrated multiple reasoning types, reflecting the interpretive complexity of applied programme design. This diversity was central to principle development and was systematically captured by the HAH-Delphi model’s justification analysis.

## 3.3.3. Panel Suficiency and Thematic Saturation

Thematic saturation was achieved before the sixth expert in both studies. In the Endurance study, all seven predefined reasoning categories had emerged by the fourth expert. The fifth expert added meaningfully distinct variants of conditional logic and application nuance. The sixth expert contributed only redundant or elaborative content. In the Strength/Mixed-Modality study, all reasoning types were covered by expert five, with expert six adding expression and emphasis but no new categories or decision pathways.

Response order had no efect on the emergence of reasoning types. Regardless of the sequence in which experts were analysed, the point at which additional conceptual framings ceased to emerge was consistently reached before the sixth participant. These results confirm that a small, carefully selected panel of senior experts was suficient to achieve saturation under the criteria specified in Methods Section IV.

## 3.3.4. Role of Gemini in Evidence Benchmarking

Gemini served as a valuable evidence baseline. Although it lacked the full contextual nuances of senior experts in applied settings, its structured output was useful where human experts diverged. In both studies, Gemini demonstrated a strong capacity to reflect evidence-informed core principles and systematically apply conditional logic, often mirroring the conclusions of academic experts and providing a robust baseline of established knowledge. It contributed to the rapid saturation of foundational knowledge and common conditionalities. Its justifications were typically well-structured and drew from the scientific literature.

However, in the Endurance study, Gemini utilised ’Neutral/Unsure’ scores significantly less than typical human expert averages, resulting in more definitive scaled judgments which sometimes diverged from nuanced human consensus summaries, despite its textual justifications often articulating conditional factors. Divergences occurred on topics like the definitive role of wearable technology or specific numerical limits for long runs, where the AI’s stance was more assertive than the more cautious or variable human consensus.

In the Strength/Mixed-Modality study, Gemini diverged from senior expert consensus on 4 out of 159 topics. These included: (1) whether failure-based training should be used for compound lifts in novice populations; (2) the importance of integrating autoregulatory strategies during deload weeks; (3) whether to set fixed repetition ranges for hypertrophy work across diverse populations; and (4) how to prioritise fat loss versus recovery capacity when adjusting training under fatigue. In each case, Gemini’s recommendations were well-structured and grounded in published literature but lacked the applied contextual reasoning provided by senior experts. While not inaccurate in isolation, these recommendations did not reflect the layered decision-making or safety-oriented judgment required for implementation in variable real-world settings.

## 3.3.5. Contributions of Less-Experienced Participants

To assess the potential value and limitations of including lesser-experienced participants in consensus development, their responses were compared to those of the senior expert panels. This analysis focused on both scoring patterns and reasoning quality. In the Strength/Mixed-Modality Training study, the larger sample size enabled a structured comparison between the eight lesser-experienced respondents and the senior panel. The lesser-experienced group in this study demonstrated marked diferences in both rating behaviour and justification quality. While 82% of senior expert ratings fell within the 4–5 range and were accompanied by structured, conditional justifications, the less experienced group showed significantly more variability: 38% of their responses landed at Likert 3, and several respondents selected 1 or 2 on items that were strongly endorsed (Likert 4–5) by the senior panel. Although 65% of their responses were directionally aligned with the seniors in terms of rating category, only 38% of their justifications reflected reasoning logic consistent with the expert panel’s conditional framework.

Thematic analysis further confirmed the limits of these contributions. Over half of the less experienced practitioners’ responses contained vague or generic statements, such as “depends on the person” or “progress over time,” without the operational specificity that characterised the senior panel. In areas demanding conditional nuance, such as training to failure, progression strategies, or autoregulation, their justifications were frequently absent, circular, or conceptually inconsistent. Some respondents endorsed a statement with a high Likert score while ofering a justification that directly contradicted the intended interpretation or omitted justification entirely.

Several examples highlighted these diferences. On progression models, senior experts uniformly referenced autoregulation based on training age; none of the lesser experts mentioned this concept. In concurrent training, all senior experts considered modality type and sequencing to mitigate interference efects, whereas only a quarter of lesser respondents acknowledged modality at all, and none discussed structural programme design. Regarding training to failure, senior experts gave conditional support linked to exercise type, recovery capacity, and training phase, while less experienced respondents often responded with categorical positions lacking context.

In the Endurance Training study, three less-experienced individuals were also included for exploratory comparison. Although no formal statistical analysis was performed due to the smaller sample, the qualitative trends were consistent with those observed in the strength study. Their responses tended to be less precise, less conditional, and notably less detailed than those of the senior panel. No novel reasoning structures were introduced by these participants, and their contributions did not expand the thematic coverage achieved by the senior panel alone. In several cases, their ratings diverged from senior consensus in ways that appeared unanchored to meaningful justification, and their explanatory comments, where present, lacked the interpretive structure required to inform nuanced principle development.

Taken together, these findings demonstrate that divergence between senior and less experienced respondents was evident not only in justification quality but also in scoring reliability. The lack of consistent contextual logic and conditional specificity among lesser participants confirmed that their inclusion risked distorting the clarity and depth of the final outputs. This reinforces a central tenet of the HAH-Delphi model: that the generation of reliable, actionable, and context-sensitive guidance relies on expert panels composed of individuals with the experience and interpretive fluency required to navigate complexity and ambiguity.

## 4. Discussion

This study introduced, implemented, and evaluated the HAH-Delphi model designed to overcome the current limitations in expert consensus generation, which include feasibility challenges in recruiting and retaining large panels, the interpretive shallowness of forced agreement models, and the underutilisation of qualitative reasoning in complex domains (Boulkedid et al., 2011; Dalkey and Helmer, 1963; Fink-Hafner et al., 2019; Hall et al., 2018; Hasson et al., 2000; Linstone et al., 1975; Nasa et al., 2021,?; Niederberger and Spranger, 2020; Shang, 2023; Sinha et al., 2011). Across three phases, retrospective replication, prospective comparison, and applied deployment, the HAH-Delphi model demonstrated high methodological transparency, and the capacity to generate rich, context-sensitive consensus outputs from compact panels of senior experts.

Phase I established that a generative AI model (Gemini), constrained solely to pre-publication evidence, could replicate the directional consensus of six historical expert consensus studies, including formal Delphi, modified Delphi, structured consensus, and guideline-derived benchmarks, with 84% alignment across 32 items. While Delphi studies informed the conceptual design of the HAH-Delphi model, the Phase I benchmarks were intentionally drawn from a broader range of expert consensus approaches. These included not only formal and modified Delphi methods, but also structured single-round expert panels and high-grade guideline-derived recommendations. This diversity reflects the actual landscape of expert knowledge production, particularly in applied health and performance domains, where consensus often emerges through hybrid or pragmatic processes rather than strict methodological templates. That Gemini showed high alignment across this range reinforces the generalisability of the HAH-Delphi framework beyond Delphi-specific replication and supports its application in settings where consensus may take multiple forms. This confirmed the framework’s utility as an evidence synthesiser, capable of inferring the prevailing conclusions of expert panels across multiple consensus formats when appropriately constrained. Importantly, divergence tended to occur in areas where the literature was actively evolving at the time of the original expert consensus, supporting the validity of Gemini’s outputs as reflective of their temporal evidence context.

While Delphi studies formed the methodological foundation of the HAH-Delphi model, Phase I deliberately included a broader range of consensus types. This included structured single-round processes and high-level guideline syntheses where no recent Delphi studies existed. This diversity reflects real-world practice and allows evaluation of AI alignment across difering expert consensus formats. The model thus supports both methodological generalisability and robustness in heterogeneous evidence environments.

Phase II extended this validation to a live setting, comparing Gemini’s responses to those of a newly convened panel of senior sleep experts using a re-administered Delphi questionnaire on insomnia. Gemini aligned with the expert panel’s directional ratings on 95% of items. However, qualitative analysis revealed key diferences: Gemini drew on evidence and structured logic, but it did not replicate the full interpretive richness, experiential insight, or pragmatic reasoning shown by the human experts. Thematic saturation analysis Jünger et al. (2017); Malterud et al. (2016); Rahimi et al. (2024), not typically performed in Delphi studies, further demonstrated that all reasoning categories emerged by the fifth expert, reinforcing the suficiency of a small senior panel. These results highlighted the complementary roles of AI and human experts—AI as a consistent, evidence-aligned foundation, and humans as the source of contextual interpretation and applied judgment.

Phase III applied the full HAH-Delphi model in two demanding domains: endurance training and resistance/mixed-modality training. These were deliberately selected for their complexity, conditionality, and variability. Across both studies, the six-person senior expert panels achieved high consensus (92.3% in endurance; 159 items categorised in strength/mixed), and thematic saturation was again reached before the sixth expert. Divergence did occur, but it reflected prioritisation trade-ofs, e.g., structure vs. adaptability, safety vs. stimulus, not inconsistency or error. These findings directly challenge the assumption that large heterogeneous panels are necessary for credible consensus and demonstrate that compact panels, when carefully selected and facilitated, can generate complete, sophisticated, and implementable guidance.

Notably, the complexity and nuance captured in these studies is not atypical of specialised domains, it is characteristic of them. Most health, rehabilitation, and performance settings require conditiona decisions, population-specific logic, and phased application. The failure of many traditional Delphi processes lies not in the efort to find consensus, but in their design’s inability to accommodate nuance without erasing it. By contrast, the HAH-Delphi model elevates nuance as a primary product, not a side-efect, and structures the process accordingly. The successful capture of layered reasoning structures (e.g., temporal logic, general and population-based conditionality, experiential framing) is one of this model’s core strengths.

A second methodological innovation of this study lies in the development and application of a structured, four-tier consensus classification framework, comprising Strong, Conditional, Operational, and Divergent consensus. Unlike conventional Delphi approaches, which rely primarily on percentage agreement thresholds, this framework integrates quantitative convergence with qualitative justification analysis. This dual-anchored model allows for fine-grained distinctions between general agreement, conditional validity, operational suficiency, and irreconcilable disagreement. It avoids false consensus, preserves conditional nuance, and provides a clear basis for facilitator adjudication. Crucially, it enables structured, implementable principles to emerge even in areas of partial alignment, ofering a more transparent and practice-ready alternative to binary consensus/no-consensus models.

Thematic saturation was assessed using a predefined framework covering seven reasoning types. The model required not just category coverage but interpretive redundancy across thematic domains. By the fifth expert, no new reasoning types emerged that would alter principle construction or shift their application boundaries. The sixth expert’s input added elaboration but no new conceptual logic. This consistency, verified both in Phase II and III, supports a principled, rather than numerical, definition of panel suficiency.

The key findings of this work is that Gemini consistently aligned with human experts on core content and exhibited stable, coherent reasoning grounded in the literature. That it did not ofer experiential or pragmatic justifications is neither surprising nor problematic at this stage of model development. These reasoning types require situational pattern recognition, value trade-ofs, ethical caution, and accumulated applied wisdom, capacities not encoded in literature alone. However, with increased access to structured, high-quality, expert-derived outputs such as those generated in this study, future AI models will likely become more adept at approximating this style of conditional logic. In this way, the HAH-Delphi model not only uses AI, it contributes to its training and evolution.

Importantly, even where Gemini diverged from human experts, its responses remained internally coherent, logically sound, and free of conceptual or safety-critical flaws. Divergence most often reflected simplification, lack of contextual sensitivity, or overconfidence, factors that make it a valuable benchmark but not a replacement for human oversight. The AI’s role in areas of human disagreement was often stabilising: by ofering a neutral, evidence-based scafold, it helped crystallise key distinctions and prompted clearer articulation of expert reasoning.

The role of the expert human facilitator was central throughout. This individual was not a neutral intermediary but a highly skilled interpreter responsible for ensuring internal coherence, resolving ambiguities, aligning Likert ratings with nuanced justifications, and conducting thematic synthesis. Facilitator-led clarification was especially important where text justifications were conditionally framed or misaligned with scalar ratings. The rigour and clarity of the final principles were directly dependent on this role, which should be considered a requirement for successful implementation of the HAH-Delphi model.

The inclusion of less-experienced respondents provided important contrast. Their responses, though generally aligned, lacked the structured conditionality, applied nuance, and interpretive depth seen in the senior panels. They did not introduce new reasoning categories and, if weighted equally, would have diluted the thematic precision of the final outputs. This does not suggest that less experienced perspectives are without value, but rather that when the objective is to generate deeply contextualised and conditional guidance, epistemic quality must take precedence over numerical inclusiveness.

The one-round structure of Phases II and III placed high initial demands on experts, but it avoided the attrition and procedural fatigue associated with multi-round designs. Structured facilitation, expert familiarity with the domain, and the inclusion of Gemini as an evidence scafold allowed the full range of reasoning to be elicited in a single round. This format proved not only feasible but eficient, and particularly suitable for settings in which expert availability is limited or where rapid guidance development is necessary.

In summary, the HAH-Delphi model ofers a viable, flexible, and rigorous approach to expert consensus development in complex domains. It does not seek to automate expert judgment but to structure, preserve, and elevate it, integrating the strengths of generative AI, senior expert reasoning, and skilled human facilitation. The findings from all three phases support its application across a range of domains where nuanced, conditional, and practically applicable guidance is required. As AI systems continue to evolve and consensus-building becomes more central to health and performance decision-making, the importance of such a structured hybrid model is likely to grow.

## 4.1. Limitations

While this study provides strong support for the HAH-Delphi model, limitations and operational considerations should be acknowledged.

First, although the AI model (Gemini) performed reliably as an evidence synthesiser and benchmark across all phases, its outputs remain constrained by current model architecture and its dependence on textual sources. It did not produce experiential, pragmatic, or ethically grounded justifications, reasoning types that are central to expert decision-making. This limitation is expected, given the nature of generative models, and it does not undermine the AI’s role as a structured, transparent scafold. However, it reinforces the model’s dependence on human interpretive input and facilitator

oversight.

Second, the model’s success depends heavily on expert selection. While this was operationalised through strict inclusion criteria, the ability to identify and recruit truly reflective senior experts remains a key dependency. Additionally, the human experts participating in Phases Two and Three were compensated for their time and expertise which introduces a potential source of bias. This is not a limitation of the model per se but an implementation requirement: if high-quality, contextualised outputs are the goal, panel selection must prioritise epistemic depth over surface-level representativeness. Broader stakeholder engagement may be appropriate in other consensus contexts, but not when generating nuanced guidance. Moreover, the number of expert raters in this study was relatively small, so the model’s generalization and reliability with a larger panel require validation in future studies.

Third, the role of the facilitator is crucial and requires significant depth and breadth of expertise. Thematic synthesis and clarification processes demand consistency, interpretive judgment, and methodological discipline. While the use of a single senior facilitator may be seen as a limitation, it reflects standard practice in consensus research, especially Delphi format, where one lead is typically responsible for guiding item development, coordinating panel interaction, and adjudicating responses. The model adopted here was consistent with published guidance and methodological norms. In real-world settings, the feasibility of deploying multiple facilitators with equivalent expertise is low, particularly in specialist domains requiring subject-matter fluency, methodological rigour, and continuity of interpretation. Importantly, this study mitigated bias risks by using pre-specified reasoning categories, transparent adjudication processes, and explicit documentation of facilitator decisions across all phases. Nonetheless, future studies should test the model with several diferent facilitators to validate its facilitator-independent reliability.

Finally, the one-round structure, though efective in this study, may not be suitable in all cases. It relies on robust item construction, responsive clarification procedures, and cognitively prepared panels. In domains where item clarity is low or expert familiarity is limited, a second refinement round may improve outcome quality. Future work should explore when and how to best deploy single- versus multi-round formats under the HAH-Delphi model.

## 4.2. Future Directions

The successful development and application of the HAH-Delphi model opens several avenues for future research, methodological refinement, and domain-specific implementation.

First, further application across diverse domains is essential. While this study focused on applied health and performance contexts, where conditionality and pragmatic nuance are core features, the model is equally relevant to clinical guideline development, rehabilitation planning, public health policy, digital therapeutics, and regulatory consensus. Future research should explore how the model performs in ethically charged, interdisciplinary, or contested domains where evidence alone is insuficient to guide practice, and where reasoning quality becomes the decisive factor in shaping consensus.

Second, additional investigation is warranted into the optimal configuration of AI constraints and interaction design. Although this study used a conservative, facilitator-vetted constraint corpus and static AI benchmarking, future iterations might explore dynamic AI-human interaction loops, version comparisons, or prompt variations to test how generative models can adaptively support, not just benchmark, expert deliberation. This includes examining how future AI models, trained on structured human justifications like those generated here, might evolve to ofer more conditional and contextually embedded reasoning.

Third, longer-term follow-up of consensus outputs generated using the HAH-Delphi model could ofer insights into their practical impact. Are they more actionable? Do they reduce implementation ambiguity? Are they better received by clinicians, practitioners, or decision-makers than traditional consensus statements? Structured evaluations of downstream uptake and efect would help establish the model not just as a methodological innovation but as a meaningful contributor to practice change.

Fourth, future work should continue to refine definitions of thematic saturation and panel suficiency in hybrid models. As new AI capabilities emerge, and as expert–AI collaboration becomes more routine, it will be important to revisit and adapt these thresholds to maintain standards of clarity, richness, and suficiency in expert consensus development.

Finally, a particularly promising direction lies in the deliberate use of structured, high-quality outputs from senior experts to inform the future of AI training. As generative models evolve, their capacity to emulate context-sensitive reasoning will depend heavily on exposure to well-articulated, experientially grounded, and conditionally nuanced expert logic, precisely the type of content produced through the HAH-Delphi process. Future research could explore how curated datasets from hybrid Delphi studies might contribute to the development of more trustworthy, responsible, and domain-specific AI systems capable of supporting complex reasoning under uncertainty. In this respect, senior human experts are not just irreplaceable within the consensus process, they are essential architects of the next generation of AI reasoning.

## 5. Conclusion

This study introduced and evaluated the HAH-Delphi model capable of generating nuanced, actionable, and context-sensitive expert consensus. Across three distinct phases, retrospective validation, prospective comparison, and applied deployment, the HAH-Delphi model consistently demonstrated high alignment between constrained generative AI outputs and human expert reasoning, while preserving the interpretive richness and conditional depth typically absent from traditional Delphi methods.

Small panels of carefully selected senior experts, supported by an evidence-synthesising AI and guided by a domain-competent facilitator, proved suficient to achieve thematic saturation and principled consensus across complex domains. The model’s structured integration of AI and human input allowed it to overcome common Delphi limitations: high panel burden, attrition risk, methodological opacity, and loss of nuance. At the same time, it preserved and amplified the contributions that only human experts can provide, experiential reasoning, ethical caution, and applied judgment.

While the AI model could not independently replicate the full reasoning spectrum of human experts, it provided a stable, transparent scafold and helped accelerate knowledge synthesis. Its structured divergence, when present, was informative rather than erroneous, reinforcing the model’s capacity to guide, not replace, expert deliberation. The role of the human facilitator proved central to ensuring interpretive fidelity, methodological consistency, and thematic clarity.

The HAH-Delphi model ofers a transparent, flexible, and rigorous pathway to expert consensus formation in domains where guidance must reflect complexity, context, and conditionality. It stands not as a replacement for expert thinking, but as a framework to preserve and amplify it, with clarity, depth, and integrity. Crucially, by systematically capturing the reasoning of senior human experts in structured form, the model creates a valuable corpus for future AI development. As AI systems advance, they will require not just data, but principled, context-rich reasoning to emulate. In this regard, expert panels operating within models such as HAH-Delphi are not only consensus-builders, but teachers—imparting the interpretive scafolds from which future decision-support systems can learn. As both the challenges and capabilities of human–AI collaboration evolve, models like this wil be essential to ensuring that future tools remain both evidence-informed and experience-grounded.

## 6. Acknowledgement

We are deeply grateful to the members of the Consumer Health Research Team at Google for their valuable feedback and technical support throughout this study, in particular Daniel Roggen, Jacqueline Shreibati, Conor Heneghan, Yun Liu, Nova Hammerquist, Brent Winslow, Heiko Maiwand, Mark Malhotra, Shwetak Patel, Mark Brooke, Yojan Patel, Robert Harle, and Florence Thng.

## 7. Competing Interests

This study was funded by Google LLC. C.S., A.A.M. are employees of Alphabet and may own stock as part of the standard compensation package.

## References

J. Bames, T. K. Behrens, M. E. Benden, S. Biddle, D. Bond, P. Brassard, H. Brown, L. Carr, V. Carson, J. Chaput, et al. Standardized use of the terms" sedentary" and" sedentary behaviours". Applied Physiology Nutrition and Metabolism-Physiologie Appliquee Nutrition Et Metabolisme, 37:540–542, 2012.

R. Boulkedid, H. Abdoul, M. Loustau, O. Sibony, and C. Alberti. Using and reporting the delphi method for selecting healthcare quality indicators: a systematic review. PloS one, 6(6):e20476, 2011.

G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.

N. Corp, G. Mansell, S. Stynes, G. Wynne-Jones, L. Morsø, J. C. Hill, and D. A. van der Windt. Evidence-based treatment recommendations for neck and low back pain across europe: a systematic review of guidelines. European Journal of Pain, 25(2):275–295, 2021.

N. Dalkey and O. Helmer. An experimental application of the delphi method to the use of experts. Management science, 9(3):458–467, 1963.

D. Fink-Hafner, T. Dagen, M. Doušak, M. Novak, and M. Hafner-Fink. Delphi method: strengths and weaknesses. Advances in Methodology and Statistics, 16(2):1–19, 2019.

P. I. Fusch Ph D and L. R. Ness. Are we there yet? data saturation in qualitative research. 2015.

G. Guest, A. Bunce, and L. Johnson. How many interviews are enough? an experiment with data saturation and variability. Field methods, 18(1):59–82, 2006.

D. A. Hall, H. Smith, E. Hefernan, K. Fackrell, and C. O. M. in Tinnitus International Delphi (COMiT’ID) Research Steering Group. Recruiting and retaining participants in e-delphi surveys for core outcome set development: evaluating the comit’id study. PloS one, 13(7):e0201378, 2018.

F. Hasson, S. Keeney, and H. McKenna. Research guidelines for the delphi survey technique. Journal of advanced nursing, 32(4):1008–1015, 2000.

S. Jünger, S. A. Payne, J. Brine, L. Radbruch, and S. G. Brearley. Guidance on conducting and reporting delphi studies (credes) in palliative care: Recommendations based on a methodological systematic review. Palliative medicine, 31(8):684–706, 2017.

S. Lessard, W. K. Chow, S. E. Cook, G. Lessard, and A. Khullar. Insomnia management in primary care: Outcomes from a canadian national survey reveal challenges and opportunities to improve clinical practice. Canadian Journal of Medicine, 6(2):88–104, 2024. doi: 10.33844/cjm.2024.6041.

H. A. Linstone, M. Turof, et al. The delphi method, volume 1975. Addison-Wesley Reading, MA, 1975.

K. Malterud, V. D. Siersma, and A. D. Guassora. Sample size in qualitative interview studies: guided by information power. Qualitative health research, 26(13):1753–1760, 2016.

C. M. Morin, A. Khullar, R. Robillard, A. Desautels, M. S. Mak, T. T. Dang-Vu, W. Chow, J. Habert, S. Lessard, L. Alima, et al. Delphi consensus recommendations for the management of chronic insomnia in canada. Sleep Medicine, 124:598–605, 2024.

P. Nasa, R. Jain, and D. Juneja. Delphi methodology in healthcare research: how to decide its appropriateness. World journal of methodology, 11(4):116, 2021.

M. Niederberger and J. Spranger. Delphi technique in health sciences: a map. Frontiers in public health, 8:457, 2020.

J. S. Patricios, K. J. Schneider, J. Dvorak, O. H. Ahmed, C. Blauwet, R. C. Cantu, G. A. Davis, R. J. Echemendia, M. Makdissi, M. McNamee, et al. Consensus statement on concussion in sport: the 6th international conference on concussion in sport–amsterdam, october 2022. British journal of sports medicine, 57(11):695–711, 2023.

S. Rahimi et al. Saturation in qualitative research: An evolutionary concept analysis. International Journal of Nursing Studies Advances, 6:100174, 2024.

N. Requejo-Salinas, J. Lewis, L. A. Michener, R. La Touche, R. Fernández-Matías, J. Tercero-Lucas, P. R. Camargo, M. Bateman, F. Struyf, J.-S. Roy, et al. International physical therapists consensus on clinical descriptors for diagnosing rotator cuf related shoulder pain: a delphi study. Brazilian journal of physical therapy, 26(2):100395, 2022.

Z. Shang. Use of delphi in health sciences research: a narrative review. Medicine, 102(7):e32829, 2023.

I. P. Sinha, R. L. Smyth, and P. R. Williamson. Using the delphi technique to determine which outcomes to measure in clinical trials: recommendations for the future based on a systematic review of existing studies. PLoS medicine, 8(1):e1000393, 2011.

M. S. Tremblay, S. Aubert, J. D. Barnes, T. J. Saunders, V. Carson, A. E. Latimer-Cheung, S. F. Chastin, T. M. Altenburg, and M. J. Chinapaw. Sedentary behavior research network (sbrn)–terminology consensus project process and outcome. International journal of behavioral nutrition and physical activity, 14(1):75, 2017.

B. Williams, G. Mancia, W. Spiering, E. Agabiti Rosei, M. Azizi, M. Burnier, D. L. Clement, A. Coca, G. De Simone, A. Dominiczak, et al. 2018 esc/esh guidelines for the management of arterial hypertension: The task force for the management of arterial hypertension of the european society of cardiology (esc) and the european society of hypertension (esh). European heart journal, 39(33): 3021–3104, 2018.

## APPENDICES

## A. Benchmark Study Description

<table><tr><td>Consensus Type</td><td>Topic</td><td>Study Name</td><td>Experts</td><td>Rounds</td><td>Notes</td></tr><tr><td rowspan="2">Delphi</td><td>*Insomnia</td><td>(Lessard et al., 2024; Morin et al., 2024)</td><td>16 multidisciplinary sleep medicine experts. National survey items extracted from Delphi</td><td>2</td><td>Consensus on 37 recommendations using ≥75% agreement threshold.</td></tr><tr><td>Rotator cuff</td><td>(Requejo-Salinas et al., 2022)</td><td>15</td><td>3</td><td>Formal Delphi process.</td></tr><tr><td>Modified Delphi</td><td>Sedentarism</td><td>(Tremblay et al., 2017)</td><td>53 Delphi participants</td><td>2</td><td>Terminology defined using structured feedback rounds.</td></tr><tr><td>Structured Single-Round Consensus</td><td>Concussion</td><td>(Patricios et al., 2023)</td><td>29 expert authors; 600+ conference attendees reviewed and voted</td><td>1 (conference vote)</td><td>Final statements based on ≥80% agreement at 6th Concussion in Sport Conference.</td></tr><tr><td rowspan="2">Guideline-Derived Consensus</td><td>Low Back Pain (Primary Care)</td><td>Corp et al. (2021)</td><td>Guideline working group authorship (not applicable)</td><td>N/A</td><td>Synthesises expert consensus across European guidelines; no fixed panel or Delphi process.</td></tr><tr><td>Hypertension</td><td>(Williams et al., 2018)</td><td>Multidisciplinary panels across documents (not reported)</td><td>N/A</td><td>Structured expert panels using GRADE; no Delphi methodology used.</td></tr></table>

\*One of the benchmark domains—chronic insomnia—used question items adapted from (Lessard et al., 2024), a national survey developed to assess real-world alignment with expert recommendations from a four-round Delphi consensus (Morin et al., 2024). Both studies were conducted by the same research group, with the (Lessard et al., 2024) survey directly reflecting the questions posed and consensus statements generated in the (Morin et al., 2024) Delphi. The national findings broadly supported the expert consensus, confirming key priorities while highlighting gaps in adoption. Using these items enabled benchmarking against Delphi-derived content in a format consistent with clinical interpretation and practice-facing decision-making.

## B. Source Corpus & Boundaries Framework Template for Gemini 2.5 Pro Information Synthesis and Benchmarking.

<table><tr><td>Framework Section</td><td>Description / Components (Emphasis on Publicly Available &amp; Open Access)</td></tr><tr><td>1. Study Topic &amp; Scope</td><td>Defines the specific focus: Topic area, Target Population, Key Questions/-Domains covered, and the relevant Knowledge Cutoff Date (for historical simulations or defining currency for live studies).</td></tr><tr><td>2. Source Categories &amp; Inclusion Criteria</td><td>Specifies allowed information sources, prioritizing publicly available and openly accessible content:Open Access Peer-Reviewed Literature: Articles from open access journals or repositories (e.g., PubMed Central, arXiv), noting pre-print status where applicable.Publicly Available Clinical Practice Guidelines (CPGs): CPGs from major societies (e.g., WHO, NICE, ACSM) available without subscription.Governmental &amp; Public Health Agency Reports: Publicly available reports from bodies like the CDC, NHS, etc.Facilitator-vetted Reputable Websites: Information from pre-approved, evidence-based sites (e.g., professional organizations, academic institutions).Explicit Exclusions: Paywalled articles, commercial textbooks, social media, forums, and personal blogs.</td></tr><tr><td>3. Trustworthiness Hierarchy &amp; Weighting</td><td>Establishes levels of evidence among publicly available sources:Level 1: Major public guidelines, high-quality open access Systematic Reviews/Meta-Analyses.Level 2: Open access RCTs, public consensus statements.Level 3: Open access observational studies, vetted professional websites.Level 4: Other vetted grey literature.AI Instruction: Prioritize higher levels and note evidence strength.</td></tr><tr><td>4. Search Strategy Guidance</td><td>Provides examples of keywords, synonyms, MeSH terms, and database filters (e.g., &quot;open access,&quot; publication type, dates) to guide AI retrieval from the public corpus.</td></tr><tr><td>5. Quality Assessment Protocol (Public/Grey Lit Vetting)</td><td>Outlines facilitator criteria for vetting grey literature: Authority, Transparency, Objectivity, Referencing, and Currency.</td></tr><tr><td>6. Synthesis Rules &amp; Instructions for AI</td><td>Defines AI directives: Adhere to scope; Synthesize objectively from public sources only; Report conflicts; Do not extrapolate; Apply safety filters; Justify conclusions; Paraphrase and attribute to respect IP.</td></tr><tr><td>7. Facilitator Validation Criteria</td><td>Lists criteria for checking the AI&#x27;s output: Relevance, Accuracy, Completeness, Nuance, Source Adherence, IP Compliance, and Safety/Bias check. Iteration occurs if checks fail.</td></tr></table>

## C. Summary of Phase I Benchmark Studies and Consensus Methods.

<table><tr><td>Reference</td><td>Topic</td><td>Classification in Paper</td></tr><tr><td>(Bames et al., 2012)</td><td>Sedentary behaviour guidelines</td><td>Modified Delphi</td></tr><tr><td>(Requejo-Salinas et al., 2022)</td><td>Rotator Cuff signs</td><td>Delphi study</td></tr><tr><td>(Patricios et al., 2023)</td><td>Concussion return-to-play protocol</td><td>Structured panel</td></tr><tr><td>(Corp et al., 2021)</td><td>Low back pain recommendations</td><td>Guideline-derived consensus</td></tr><tr><td>(Williams et al., 2018)</td><td>Hypertension management</td><td>Guideline-derived / hybrid consensus</td></tr><tr><td>(Lessard et al., 2024; Morin et al., 2024)</td><td>Insomnia management</td><td>Delphi study</td></tr></table>

C.1. Chronic Insomnia in Primary Care – Published responses vs. Gemini (Morin et al., 2024)

<table><tr><td>Num.</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Take structured sleep history</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Use validated questionnaires (e.g. ISI)</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>Screen high-risk patients</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Aligned</td></tr><tr><td>4</td><td>Use sleep diaries</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>5</td><td>Consider insomnia in comorbid presentations</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>6</td><td>PCPs can deliver brief CBT-I</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Aligned</td></tr><tr><td>7</td><td>Refer for full CBT-I if possible</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>8</td><td>Avoid pharma-cotherapy as first-line</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Partially Aligned</td></tr><tr><td>9</td><td>CBT-I should be first-line</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>10</td><td>DORAs appropriate in select cases</td><td>3 – Neutral</td><td>Mixed Consensus</td><td>&lt;75% 4–5</td><td>Aligned</td></tr><tr><td>11</td><td>Sleep hygiene alone is insufficient</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>12</td><td>Use shared decision-making</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>13</td><td>Follow-up is necessary</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>14</td><td>Educate on sleep-wake regulation</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>15</td><td>Advise on caffeine, alcohol, screens</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>16</td><td>Deliver brief advice in routine visits</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Aligned</td></tr><tr><td>17</td><td>Use sleep restriction with caution</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Aligned</td></tr><tr><td>18</td><td>Refer complex cases to specialist</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>19</td><td>Use digital CBT-I apps</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Aligned</td></tr><tr><td>20</td><td>Insomnia should not be dismissed</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr></table>

C.2. Low Back Pain Management (Primary Care) Source: (Corp et al., 2021)

<table><tr><td>Num</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Reassure patients; LBP is common and not serious</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Imaging is rarely required</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>Use NSAIDs first-line; not paracetamol</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Partially Aligned*</td></tr><tr><td>4</td><td>Recommend physical activity and self-management</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>5</td><td>Avoid bed rest</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>6</td><td>Avoid routine opioids</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr></table>

Note on Item 3: Gemini, synthesizing pre-2021 evidence, reflected evolving guideline recommendations that increasingly questioned paracetamol’s efectiveness. The Delphi panel showed moderate agreement—likely due to real-world variability and slower de-implementation in practice. Thus, the direction was aligned, but confidence levels difered.

C.3. Concussion in Sport – Human Experts vs. Gemini Source: (Patricios et al., 2023) – Pre-Oct 2022 corpus cutof applied for Gemini synthesis.

<table><tr><td>Num.</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Remove athlete from play immediately upon suspicion</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Use a multidimensional assessment approach</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>Encourage gradual return-to-learn and return-to-sport</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>4</td><td>Initiate symptom-limited activity early in recovery</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>5</td><td>Use SCAT-type tools to assist with sideline/-clinic assessment</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Partially Aligned</td></tr></table>

Note on Item 5: Gemini agreed with using structured tools like SCAT but did not specifically name SCAT6, which was finalized shortly after the cutof. The alignment is considered valid, as SCAT was already an established tool; the specific version evolution (SCAT6) fell outside the AI’s reference window.

## C.4. Rotator Cuf Signs (Requejo-Salinas et al., 2022)

<table><tr><td>Num.</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Pain with over-head/abduction movements</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Pain localised to deltoid region</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>Age over 40 typical feature</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>4</td><td>Symptom onset after increased activity</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>5</td><td>Imaging only if trauma/malignancy</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>6</td><td>Imaging not sole basis for surgery decision</td><td>4 – Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>7</td><td>Assess active shoulder ROM</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>8</td><td>Assess shoulder strength</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>9</td><td>Pain on resisted abduction</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>10</td><td>Pain on resisted external rotation</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>11</td><td>Special tests unnecessary for diagnosis</td><td>2 – Disagree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Divergent</td></tr><tr><td>12</td><td>Reproducible loading pain sufficient for diagnosis</td><td>3 – Neutral</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Partial</td></tr></table>

C.5. Hypertension Diagnosis and Management Pathway – Human Experts vs. Gemini (Williams et al., 2018) – Pre 2018 corpus cutof applied for Gemini synthesis.

<table><tr><td>Num</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Use ABPM or HBPM to confirm hypertension diagnosis</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Recommend lifestyle changes to all patients</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>Follow stepwise medication algorithm</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>4</td><td>Consider lower BP targets in high-risk patients</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Partially Aligned</td></tr><tr><td>5</td><td>Repeat BP measurements and review response</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr></table>

Note on Item 4: Gemini rated lower targets as appropriate but with more caution than the panel. While the Delphi group leaned toward lower BP targets in high-risk individuals, this was a debated issue. Gemini appropriately reflected this ambiguity in the literature of that time.

## C.6. Sedentary Behaviour Terminology – Human Experts vs. Gemini Source: Tremblay et al. (2017) – Pre2017 corpus cutof applied for Gemini synthesis.

Table 5 | Alignment on Sedentary Behaviour Definitions

<table><tr><td>Num.</td><td>Question Summary</td><td>Gemini Likert Rating</td><td>Human Consensus Category</td><td>Human Agreement Range</td><td>Alignment</td></tr><tr><td>1</td><td>Sedentary behaviour should be defined by energy expenditure (≤1.5 METs)</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>2</td><td>Sedentary behaviour should include sitting/reclining posture</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>3</td><td>The term “physical inactivity” should be distinct from “sedentary behaviour”</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr><tr><td>4</td><td>Prolonged sitting should be considered a subcategory of sedentary behaviour</td><td>4 – Agree</td><td>Moderate Agreement</td><td>75–89% 4–5</td><td>Partially Aligned</td></tr><tr><td>5</td><td>Definitions should be consistent across research, surveillance, and policy</td><td>5 – Strongly Agree</td><td>Strong Agreement</td><td>≥90% 4–5</td><td>Aligned</td></tr></table>

Note on Item 4: Gemini agreed that prolonged sitting is part of sedentary behaviour, but did not emphasize its subcategorical role as explicitly as the Delphi panel. This reflects some ambiguity in pre-2017 literature where terminology was still evolving, consistent with the panel’s goal of achieving clearer operational definitions.

## D. Guiding principles for endurance running

## D.1. The Foundational Architecture of Endurance Adaptation

<sup>•</sup> Long-Term Consistency: Sustained, regular, and thoughtfully planned training over extended periods is the primary catalyst for profound endurance adaptations.

<sup>•</sup> Progressive Overload: To enhance physiological capacity, training stress must be incrementally increased (via volume, intensity, or frequency), with progression managed gradually and meticulously to ensure it remains a positive stimulus.

<sup>•</sup> Gradualism in Progression: Implement conservative increases in training load (e.g., 10-15% weekly for long run duration), often with interspersed consolidation or "down" weeks to facilitate adaptation and mitigate injury risk.

<sup>•</sup> Individualization: Efective training programs must be bespoke frameworks tailored to the individual’s unique genetic predispositions, training history, physiological characteristics, lifestyle factors, recovery patterns, and goals.

<sup>•</sup> Training Must Fit Life: The athlete’s personal context and capacity should dictate training structure, not the other way around.

<sup>•</sup> Recovery and Adaptation as Critical Processes: Physiological improvements occur during periods of rest and recovery following catabolic training stress; insuficient recovery negates training benefits and increases risks.

<sup>•</sup> Individualized Rest Day Prescription: Decisions regarding the frequency and nature of ’true rest’ (no running) days must be deeply individualized based on training load, life stress, recovery capacity, and subjective athlete feedback, as no single universal rule for rest day prescription achieved expert consensus.

<sup>•</sup> Primacy of Subjective Feedback in Recovery Monitoring: Attentive listening to the athlete’s subjective feedback on fatigue, mood, and sleep quality, augmented by objective performance markers, is a critical coaching competency for monitoring recovery.

<sup>•</sup> Specificity: Training adaptations are highly specific to the nature of the stimulus applied; training must incorporate elements that replicate the demands of the target event (e.g., duration, pace, fueling, environment, terrain).

<sup>•</sup> Reversibility (Detraining): Fitness gains are transient and require consistent engagement with training, even during transitional phases, to preserve adaptations.

## D.2. Architecting the Training Regimen: Weekly Rhythms and Cyclical Progressions

<sup>•</sup> Polarized/Pyramidal Intensity Distribution: Efective weekly structures typically involve a high volume of low-intensity training (approx. 80%) punctuated by a smaller proportion of targeted high-intensity sessions (approx. 20%).

<sup>•</sup> Adequate Recovery Between Hard Sessions: Schedule 48 to 72 hours of recovery between high-intensity sessions to allow for physiological repair and optimal performance in subsequent quality workouts.

<sup>•</sup> Adaptation of Session Density by Experience: Novice runners generally benefit from fewer high-intensity days per week compared to more experienced and resilient athletes.

<sup>•</sup> Cautious Use of Back-to-Back Hard Days: This strategy is generally reserved for highly advanced athletes or specific, short-term blocks and requires extreme caution due to elevated overtraining risk.

<sup>•</sup> The Quintessential Long Run: The long run is a crucial element for extending aerobic endurance, enhancing fatigue resistance, improving fuel utilization, building musculoskeletal resilience, and practicing race-day strategies.

<sup>•</sup> Gradual Long Run Progression: Increase long run duration or distance gradually, adhering to progressive overload, often with weekly increases of no more than 10-15% or by using build/consolidation week patterns.

<sup>•</sup> Individualized Long Run Caps: Maximum long run durations (e.g., 3 hours or 20-22 miles for marathons) should be individualized to prevent excessive recovery demands relative to the athlete’s overall training and goals.

<sup>•</sup> Specialized Long Runs for Ultras: Ultramarathon preparation may involve even longer single eforts or "back-to-back" long runs to simulate event demands.

<sup>•</sup> Conditional Inclusion of Intensity in Long Runs: Incorporating segments at goal race pace, "fast finishes," or structured pace variations can enhance race-specific fitness for experienced runners, guided by the principle of specificity.

<sup>•</sup> Individualized Long Run Scheduling: The specific day for the long run should be flexible, primarily determined by the individual athlete’s life context, preferences, and recovery needs, as no single set of systematic rules for altering scheduling by runner type or experience achieved expert consensus.

<sup>•</sup> Limited Utility of "Running Doubles" for Most Recreational Runners: Performing two running sessions in a single day is generally unnecessary and potentially counterproductive for most recreational runners; focus should be on quality single sessions.

<sup>•</sup> Strategic Use of "Running Doubles" for Advanced Athletes: Doubles can be a tool for elite or very high-volume sub-elite athletes to accumulate mileage or incorporate advanced protocols.

<sup>•</sup> Beneficial "Doubling" with Run + Strength/Cross-Training: Pairing a run with strength training or low-impact cross-training on the same day is a widely beneficial practice for all levels to consolidate stress and preserve recovery days.

<sup>•</sup> Flexible Periodization for Recreational Runners: While periodization should ensure logical progression from general fitness to race-specific preparedness, its application for recreational runners often requires a flexible, non-linear, or "undulating" approach to accommodate life commitments.

## D.3. Calibrating Efort: The Science and Art of Training Intensity

<sup>•</sup> Multifaceted Approach to Defining Intensity Zones: Employ a range of methodologies including RPE, pace-based zones, and heart rate zones to define and communicate training intensity.

<sup>•</sup> Primacy of RPE/Talk Test: Rate of Perceived Exertion (RPE) and the "talk test" are highly valued for cultivating an athlete’s internal sense of efort and are often the ultimate arbiters of appropriate intensity, especially for novices or when external factors afect other metrics.

<sup>•</sup> Utility of Pace-Based Zones: Pace zones ofer objective targets useful for goal-oriented runners and specific workout structures.

<sup>•</sup> Cautious & Complementary Use of Heart Rate Zones: Heart rate is a useful physiological guide but should be used as a complementary tool or governor, acknowledging its liability due to various internal and external factors.

<sup>•</sup> Selective Use of Advanced Intensity Monitoring: Lactate threshold testing and running power meters are generally employed by higher-level athletes or those with specialized resources.

<sup>•</sup> Adaptable Number of Training Zones: Typically use a 3-zone model (beneficial for novices or emphasizing polarized concepts) or a more granular 5-zone system (common and efective for many), with the choice depending on athlete experience, understanding, and the need for clarity over complexity.

<sup>•</sup> Flexible Adherence to Intensity Zones: Prescribed intensity zones serve as valuable guidelines, but rigid adherence can be counterproductive; RPE and somatic feedback should play a critical role, especially for low-intensity sessions.

<sup>•</sup> Precision for Key High-Intensity Workouts: Greater precision in hitting target eforts is generally expected for key high-intensity workouts, though minor adjustments based on daily feel are warranted.

<sup>•</sup> Athlete Empowerment for Intensity Adjustments: Efective coaching involves educating athletes on the purpose of diferent intensities and empowering them to make intelligent adjustments.

## D.4. The Runner’s Toolkit: Principles of Specific Run Types (Derived from their purpose, execution, benefits, and integration)

<sup>•</sup> Recovery Runs - Principle: Perform at very low intensity for short durations primarily to promote active recovery and freshness, not direct fitness gains; complete rest or light cross-training may be more appropriate for some.

<sup>•</sup> Easy & LSD Runs - Principle: Constitute the bulk of training volume at a comfortable, conversational pace to build a robust aerobic base, enhance endurance, and improve physiological eficiency (mitochondria, capillarization, fuel utilization).

<sup>•</sup> Tempo Runs - Principle: Sustain eforts at or near lactate threshold ("comfortably hard") to improve lactate clearance, enhance metabolic eficiency at race-relevant intensities, and build speed endurance.

<sup>•</sup> Lactate Threshold (LT) Intervals - Principle: Accumulate significant time at or slightly above LT intensity through repeated bouts with short recoveries to potently stimulate lactate clearance and improve sustained speed.

<sup>•</sup> VO2 Max Intervals - Principle: Utilize high-intensity intervals (2-5 minutes at 3k-5k pace) with comparable recovery periods to directly challenge and improve maximal oxygen uptake and aerobic power.

<sup>•</sup> Strides - Principle: Incorporate short, controlled accelerations (not all-out sprints) regularly to improve neuromuscular coordination, running mechanics at faster speeds, and maintain leg turnover with minimal metabolic stress.

## D.5. Strategic Cross-Training: Enhancing Fitness and Mitigating Risk

<sup>•</sup> Cross-Training as a Strategic Supplement: Engage in non-running exercise modalities to enhance overall fitness, reduce impact stress, aid injury prevention/management, facilitate recovery, and provide psychological variety.

<sup>•</sup> Prioritize Low/Non-Impact Modalities for Recovery/Injury Management: Utilize activities like cycling, swimming, aqua jogging, or elliptical training to maintain cardiovascular fitness while minimizing impact.

<sup>•</sup> Aqua Jogging for Run-Specific Fitness Maintenance: Deep water running efectively maintains run-specific fitness and neuromuscular patterns during periods of non-running.

<sup>•</sup> Balance Cross-Training with Running Specificity: While beneficial, cross-training should supplement, not entirely replace, running for a healthy athlete, especially as a key race approaches, to adhere to the principle of specificity.

## D.6. Synergistic Elements: Enhancing Performance and Resilience

<sup>•</sup> Integral Role of Strength Training: Implement 1-2 weekly sessions of functional, runner-specific strength training year-round to prevent injuries, improve running economy, and build musculoskeletal resilience.

<sup>•</sup> Periodize and Integrate Strength Training: Shift the focus of strength training (e.g., foundational strength in base phase, maintenance or power-endurance in race phase) and integrate it to complement running, often on harder running days or days allowing recovery.

<sup>•</sup> Intra-Run Fueling for Prolonged Eforts: For eforts exceeding 75-90 minutes, consume carbohydrates (e.g., 30-60g/hr, increasing to 60-90g/hr+ for longer events if tolerated) to maintain blood glucose and spare glycogen.

<sup>•</sup> Individualized "Gut Training" for Fueling: Emphasize individual experimentation with fuel types, amounts, and timing during training to adapt the digestive system and develop a personalized, efective race-day strategy. (This reflects the Conditional Consensus on varying fueling guidance).

<sup>•</sup> Strategic Tapering for Peak Performance: Implement a taper (1-3 weeks, varying by race distance) by significantly reducing training volume while largely maintaining intensity and frequency to shed fatigue and optimize race readiness.

## D.7. The Shadow of Excessive Load: Understanding Overtraining Syndrome

<sup>•</sup> Distinguish FOR, NFOR, and OTS: Understand the spectrum of training maladaptation from functional overreaching (planned, beneficial) to non-functional overreaching (prolonged fatigue) and Overtraining Syndrome (severe, long-lasting).

<sup>•</sup> Multifactorial Etiology of Overtraining: Recognize that NFOR/OTS stem from chronic excessive total stress (training errors, insuficient recovery, nutritional deficiencies like RED-S, life stress) relative to coping capacity.

<sup>•</sup> Prioritize Prevention of Overtraining: Focus on individualized and periodized training, gradual progressive overload, systematic monitoring, prioritizing recovery, optimizing nutrition (maintaining energy availability), managing life stress, and athlete/coach education.

<sup>•</sup> Systematic Monitoring - Subjective Feedback as Cornerstone: Prioritize subjective athlete feedback (mood, fatigue, sleep, RPE) and performance cues for monitoring training load and recovery.

<sup>•</sup> Systematic Monitoring - Caution and Individualization with Technology: Approach wearable technology metrics (HRV, readiness scores) with caution as supplementary tools, acknowledging varied expert views on their standalone reliability and the need for individualized interpretation alongside subjective feedback. No single technological monitoring strategy or systematic diferentiation by athlete type achieved universal expert consensus.

<sup>•</sup> Systematic Monitoring - Response to Early Fatigue: Recognize that expert approaches to managing sessions missed due to early fatigue vary (e.g., structure preservation vs. immediate individualization based on context); no single rule applies, requiring careful coaching judgment.

<sup>•</sup> Rest as Cornerstone of NFOR/OTS Management: Prolonged rest is the primary treatment for NFOR/OTS, with a very gradual, monitored return to training only after full recovery and addressing underlying contributors (e.g., LEA/RED-S).

## D.8. The Human Element: Coaching Philosophy and the Athlete-Coach Dyad

<sup>•</sup> Athlete-Centered Coaching Philosophy: Prioritize the athlete’s long-term health, safety, and wellbeing above immediate performance, fostering sustainable engagement, enjoyment, intrinsic motivation, and autonomy.

<sup>•</sup> Transparent and Honest Communication: Build coaching relationships on transparency, honesty, realistic expectations, and evidence-based practices adapted to individual contexts.

<sup>•</sup> Individualized and Multifaceted Communication: Tailor communication modes and frequency to the athlete’s personality and needs. However, recognize that expert philosophies diverge on whether communication strategies should be systematically and formally adjusted based on broad runner categories (novice, intermediate, sub-elite), with the unifying principle being efective, empathetic, and responsive communication with the specific individual.

<sup>•</sup> Critical and Supplementary Use of Digital Tools: Utilize training platforms for planning/feedback and wearable technology as supplementary aids, but always prioritize coaching judgment and athlete subjective experience over raw data. Acknowledge varied expert views on the reliability of some wearable data when integrating it.

<sup>•</sup> Dynamic and Responsive Plan Modification: Drive training plan adjustments primarily by athlete subjective feedback, performance markers, and life stressors, balancing planned structure with real-time responsiveness.

<sup>•</sup> Cultivate Athlete Self-Awareness: Foster athlete autonomy in understanding their bodies and making sensible minor training adjustments as experience grows.

<sup>•</sup> Uphold Strong Professional Values: Commit to athlete safety, promote positive body image and mental health, foster joyful sport engagement, and recognize limits of expertise by referring when necessary.

## E. Guiding principles for resistance and mixed cardio/strength training

The expert consensus process yielded a comprehensive framework of principles guiding the application of resistance and mixed-modality (concurrent) training. The key dimensions of this framework are summarized below:

<sup>•</sup> Training Variables and Goal Alignment: A foundational outcome was the articulation of how training volume (primarily defined as efective working sets, but acknowledging total repetitions and volume load), intensity (load, often guided by %1RM, RPE, or RIR), and efort (proximity to technical failure) must be synergistically managed and meticulously aligned with primary training goals (whether strength, hypertrophy, endurance, or a combination in mixed-modality approaches). Specific guidelines were established for optimizing these variables for hypertrophy, strength development (including strength without mass), muscular endurance, metabolic conditioning, and muscle preservation during fat-loss phases. The critical role of recoverable volume ceilings and planned “deloads” (both proactive and reactive) for sustainable progress was consistently emphasized.

<sup>•</sup> Progression Strategies: The consensus highlighted an evolution in progression strategies, from simple linear and double-progression models suitable for novices (prioritizing technical mastery and confidence with conservative initial loads) to more sophisticated periodization models (e.g., ‘block’, undulating – “DUP”/“WUP”) for intermediate and advanced individuals engaging in resistance or mixed-modality training. The development of autoregulation was identified as a core skill, enabling performance-driven adjustments to maintain an optimal training stimulus relative to daily readiness.

<sup>•</sup> Application of Training to Failure: A nuanced perspective on training to failure emerged, positioning it as a specific tool rather than a default method. Emphasis was placed on diferentiating technical failure (form breakdown, the preferred stopping point for most training) from muscular failure. While selective, cautious use of muscular failure was deemed potentially beneficial for advanced trainees in specific hypertrophy or peaking contexts (e.g., final sets of isolation exercises, supervised AMRAPs – As Many Reps As Possible), consistent training near, but not to, failure (e.g., 1-3 RIR) was recognized as yielding similar benefits with less fatigue and risk, particularly for compound lifts and special populations.

<sup>•</sup> Exercise Order and Session Structure: The principles afirmed that exercise order should prioritize skill, safety, and the primary adaptation goal. Typically, complex, high-load, multijoint movements precede simpler, lower-load, or isolation exercises. However, context-specific adjustments, such as pre-activation drills or interleaved exercises in metabolic circuits (common in mixed-modality training), are permissible when aligned with the session’s purpose and do not compromise safety or key performance outcomes.

<sup>•</sup> Concurrent Training Integration: For integrating strength and endurance (mixed cardio/strength training), the consensus stressed strategic scheduling to mitigate interference. This includes prioritizing the primary goal in session sequencing (e.g., resistance training before cardio if strength is key), selecting lower-impact cardio modalities (e.g., cycling, incline walking), managing cardio intensity (especially HIIT) around demanding resistance sessions, and ensuring adequate recovery between conflicting stimuli.

<sup>•</sup> Recovery as a Foundational Component: Recovery was framed not as passive rest alone, but as an active, planned, and individualized component of training architecture, crucial for both resistance and mixed-modality programs. This includes structured deloads, attention to sleep quality and quantity, nutritional support, stress management, and the utility of low-intensity active recovery methods like walking. The need to tailor recovery strategies to individual profiles (e.g., age, occupational stress, training status, total training load from combined cardio and

strength work) was a strong theme.

<sup>•</sup> Autoregulation as an Essential Skill: Autoregulation was identified as a crucial skill for long-term, sustainable training, enabling individuals to modulate training variables based on daily readiness in both resistance-focused and mixed-modality regimens. The principles support introducing basic autoregulatory concepts (like RIR) to novices and developing more refined RPE-based and performance-based adjustments in experienced trainees.

<sup>•</sup> Multi-faceted Feedback Interpretation: Efective program modification relies on synthesizing a composite of subjective feedback (e.g., mood, soreness, RPE, motivation) and objective indicators (e.g., performance data, wearable metrics where appropriate and validated). No single metric is definitive; rather, a dialogue between data streams, contextualized by individual trends, should guide adjustments for any training type.

<sup>•</sup> Adaptations for Special Populations: The framework strongly advocates for structurally adapted programming for special populations (e.g., older adults, post-rehab, perimenopausal individuals, those with specific health conditions or anxieties), emphasizing that adaptation should facilitate safe participation and progress towards ambitious goals in resistance and mixed cardio/strength training, rather than merely reducing expectations. This involves modified loading, exercise selection, tempo, and a focus on building confidence and self-eficacy.

<sup>•</sup> Dynamic and Evolving Programs: Finally, the consensus underscored that training programs must be dynamic systems that evolve with the individual, not static templates, whether for pure resistance training or mixed-modality approaches. Regular review and revision based on ongoing feedback, changing goals, and life circumstances are essential for sustained adherence and progress. In summary, the consensus process produced a rich, multi-layered set of principles that emphasize individualization, evidence-based practice, and a holistic, adaptive approach to resistance and mixed-modality training.