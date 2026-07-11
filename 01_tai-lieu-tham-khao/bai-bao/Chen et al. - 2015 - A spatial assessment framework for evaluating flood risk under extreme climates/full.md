# A spatial assessment framework for evaluating flood risk under extreme climates

Yun Chen <sup>a,</sup>⁎, Rui Liu <sup>a,b</sup>, Damian Barrett <sup>c</sup>, Lei Gao <sup>d</sup>, Mingwei Zhou <sup>e</sup>, Luigi Renzullo <sup>a</sup>, Irina Emelyanova <sup>f</sup>

<sup>a</sup> CSIRO Land and Water, Canberra, Australia

<sup>b</sup> Key Laboratory of Geographic Information Science (Ministry of Education), East China Normal University, China

<sup>c</sup> CSIRO Energy, Canberra, ACT, Australia

<sup>d</sup> CSIRO Land and Water, Glen Osmond, SA, Australia

<sup>e</sup> CSIRO Land and Water, Highett, VIC, Australia

<sup>f</sup> CSIRO Energy, Floreat, WA, Australia

## H I G H L I G H T S

• A spatial risk evaluation framework incorporating multidisciplinary indices.

• An integrated modeling approach coupling GIS, RS and multicriteria decision making.

• A risk assessment to demonstrate transparency, efficiency and analytic rigour.

• A methodology widely applicable to water resource and environmental studies.

## G R A P H I C A L A B S T R A C T

![](images/27b7f106466875ee47c966f8ae72ee3aa266ed5b820623d23858ad587be6e310.jpg)

## a r t i c l e i n f o

Article history: Received 6 March 2015 Received in revised form 1 August 2015 Accepted 16 August 2015 Available online 28 August 2015

## Editor: Simon Pollard

Keywords: Multi-criteria decision making AHP GIS MODIS Inundation

## a b s t r a c t

Australian coal mines have been facing a major challenge of increasing risk of flooding caused by intensive rainfall events in recent years. In light of growing climate change concerns and the predicted escalation of flooding, estimating flood inundation risk becomes essential for understanding sustainable mine water management in the Australian mining sector. This research develops a spatial multi-criteria decision making prototype for the evaluation of flooding risk at a regional scale using the Bowen Basin and its surroundings in Queensland as a case study. Spatial gridded data, including climate, hydrology, topography, vegetation and soils, were collected and processed in ArcGIS. Several indices were derived based on time series of observations and spatial modeling taking account of extreme rainfall, evapotranspiration, stream flow, potential soil water retention, elevation and slope generated from a digital elevation model (DEM), as well as drainage density and proximity extracted from a river network. These spatial indices were weighted using the analytical hierarchy process (AHP) and integrated in an AHP-based suitability assessment (AHP-SA) model under the spatial risk evaluation framework. A regiona flooding risk map was delineated to represent likely impacts of criterion indices at different risk levels, which was verified using the maximum inundation extent detectable by a time series of remote sensing imagery. The result provides baseline information to help Bowen Basin coal mines identify and assess flooding risk when making adaptation strategies and implementing mitigation measures in future. The framework and methodology developed in this research offers the Australian mining industry, and social and environmental studies around the world, an effective way to produce reliable assessment on flood risk for managing uncertainty in water availability under climate change

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

The mining sector in Australia and globally has always been vulnerable to catastrophic damage that can be hard hit communities and businesses by floods and inundation due to extreme phenomena, such as high rainfalls, spilling dams and flooding rivers. In 2011, cyclone Yasi and the ensuing flood shut down 85% of Queensland's coal mines, costing AUD 2.5 billion (Smith, 2013). Since climate change is forecast to increase the exposure of the mining sector to flooding risk, identifying and understanding the potential risks of flooding is critical to inform strategies and actions for the mining industry to avoid or manage dangerous levels of changes and minimize possible harm (Gao et al., 2013; Foulds et al., 2014).

Flood risk is the probability of flood occurrence and its potential consequences. Risk is thus a function of the hazard (i.e. frequency of the flood) and the vulnerability (susceptibility) of the receptor exposed to the hazard (Koks et al., 2015; Foudi et al., 2015). Mapping has become the keystone for flood risk management and communication in representing the spatial relationship between hazard and vulnerability, as well as resulting risk which is a combination of the two at a particular location.

In general, assessing flood risk falls into two categories: qualitative and quantitative. Qualitative methods are used to gain an understanding of underlying reasons, opinions, and motivations. They provide insights into the problem or help to develop ideas or hypotheses for potential quantitative study. Qualitative data collection methods vary using unstructured or semi-structured techniques. Some common methods include focus groups (group discussions) and individual interviews. Quantitative methods are used to quantify the problem by way of generating numerical data or data that can be transformed into useable statistics. They are based on measurable data to formulate facts and uncover patterns in research. Quantitative data collection methods are much more structured than qualitative data collection methods, mainly include systematic observations and various forms of surveys. In comparison with qualitative flood risk assessment which mainly depends on expert opinions, quantitative evaluation are usually based on numerical modeling, such as hydraulic, hydrological and hydrodynamic models. The most commonly used analytical hierarchy process (AHP; Saaty, 1980) in multi-criteria decision making (MCDM) is a semiquantitative method that has a partly subjective nature. It integrates the ideas of ranking and weighting with the knowledge of experts. Criterion weights are calculated using a preference matrix where all identified relevant criteria are compared against each other in pairs. The weights can then be aggregated with the criteria in different weighted combination methods for the derivation of evaluation results.

The AHP-based MCDM approaches have been widely used because of their simplicity in implementing and interpreting, capability in handling sparse or poor quality data, and efficiency in regional studies (Dewan et al., 2007; Chen et al., 2010, 2013b; Wang et al., 2011). GIS is an appropriate tool for processing spatial data with attributes for deriving regional indicators on flood risk (Jiqun et al., 2002; Chau et al., 2013), which is an important step in effective risk estimation. Building analytic units based on grids or administrative areas, GIS is capable of integrated modeling on natural conditions including climate, topography, hydrology, and other social and economic features. It also has intra/inter spatial data operations through the powerful spatial analysis and geo-statistical functions for the spatial and temporal analysis of flood disasters and risk assessment. GIS-based spatial MCDM (SMCDM) is a suitable method to incorporate all relevant types of consequences (Chen et al., 2009, 2010; Chen and Paydar, 2012). There are abundant literatures about SMCDM.

For an extensive review, see Malczewski (2004) and Chen et al. (2010). SMCDM has been widely applied to landuse and environmental planning (e.g. Davidson et al., 1994; Jiang and Eastman, 2000; Joerin et al., 2001; Store and Kangas, 2001; Setiawan et al., 2004; Svoray et al., 2005; Nekhay et al., 2008; Kienberger, et al., 2009; Kubal, et al., 2009; Udoh and Ekanem, 2011; Rahman et al., 2012; Zarekar et al., 2013; Feizizadeh et al., 2014), as well as water and agricultural management (e.g. Tiwari et al., 1999; Ahamed et al., 2000; Ceballos-Silva and López-Blanco, 2003; Sicat et al., 2005; Chen et al., 2007, 2009, 2010; Grayson et al., 2008; Chandrasekar, et al., 2009). However, the application of SMCDM in flood risk assessment is relatively rare based on relatively limited coverage in literature (Tkach and Simonovic, 1997; Simonovic and Nirupama, 2005; Thinh and Vogel, 2006; Jonkman et al., 2008; Meyer et al., 2009; Wang et al., 2011; Yang et al., 2011; Huang et al., 2014a; Siddayao et al., 2014; Kannan et al., 2014; Papaioannou et al., 2015). With an increasing demand on SMCDM to support collaborative decisions over the last decade, relevant systems, tools and related methodologies (Kollias and Kalivas, 1998; Karnatak et al., 2007; Chen et al., 2009; Reshmidevi et al., 2009; Rahman et al., 2012) have been developed extensively. Among these published studies, the AHP-SA framework (Chen et al., 2010, 2013b) has a great potential to be efficiently applied to many application domains. The concept and tool has been used in assist decision makers with making justifiable decisions for solving complex issues in natural resources management and environmental studies. They have provided informed, systematic and transparent analysis of diverse environmental, social and economic data along with value judgments and policy and management goals.

The mining sector in Australia and around the world is facing increasing challenges in water-resource management under extreme climates which are extreme weather events with destructive potential, such as droughts, cyclones and storms. Flooding of mining pits (underground or open cut), which can be caused by flash flooding from short-periods of intensive rainfall and inundation from surrounding water courses due to prolonged extensive rainfall, has the potential to be the largest and most critical impact on a mine. Owing to Queensland's high natural climatic variability and associated ecological vulnerability of the mining industry to climatic changes, a number of extreme weather events have been witnessed in the past decade (Sharma et al., 2013). From June 2002 to late 2010, severe drought conditions across several parts of Central Queensland. While these regions have experienced intermittent flooding since 2000, major flood events occurred between the summer periods of 2007–08 and 2011–12. In addition to floods, Central Queensland is also highly vulnerable to cyclonic events. During the period of 2000 to 2011, four cyclones were recorded that resulted in significant impacts on coal mining operations in the Bowen Basin. Through this extended period of extreme wet conditions, Queensland experienced the highest rainfall on record. The consequential inundation caused major disruption to operations resulting in loss of revenue for the mining sector. The flooding also led to excessive water on mine sites. Given the history of highly variable climate conditions in the area, these have underscored an urgent need for appraising flood risk on coal mines at regional-scale. The evaluation will support the development of improved water management strategies for efficiently and effectively sustain the productivity and profitability of coal mines under extreme climate conditions. This research, therefore, aims to adapt the AHP-SA model to develop a spatial framework which integrates several evaluation indices for assessing regional-scale flood risk to coal mines. It takes the Bowen Basin and its surrounding environment in Queensland as an example.

## 2. Methdology

## 2.1. Study area

The study area (Fig. 1) is located at central Queensland in Australia, covering an area of more than 60,000 km<sup>2</sup>. It is one of Australia's primary coal mining areas. It plays a key role in the economic prosperity of Queensland by producing and exporting mainly high quality coal. The average annual precipitation in the area is approximately 830 mm. The mean annual discharge (1963–2013) from the gauge station in the catchment (130401A) is approximately 1930 GL (gigaliter). Prolonged heavy rainfall during the 2010–2011 wet-season caused a significantly high flow discharge with a maximum observed daily flow of 416 GL, which severely affected industry operations. There was no explicit warning of the exceptionally wet conditions in the seasonal forecast from the Australian Bureau of Meteorology, which simply suggested at least a 50% probability of above mean rainfall for the Bowen Basin (Abbot and Marohasy, 2015). The region has been regarded as home to one of the most highly variable climates in the world and consequently managing mine water resources is a major challenge (Gao et al., 2014).

There are 16 coal mines spreading over the study area. They are representative of central Queensland which contains the largest coal reserves in Australia with an ongoing plan to be transited to the Coal Hub for the state (Zhang et al., 2014). Hence, it is very important to evaluate flood risk and to develop risk maps for future water resources management in the region (Zhou et al., 2013).

## 2.2. Conceptual framework

After a review of similar research in the literature, a SMCDM framework for risk assessment was conceptualized and outlined in Fig. 2. It integrates a wide range of spatio-temporal data and indices which can then be linearly ranked and weighted for risk mapping. The first step of the framework is spatial data acquisition, followed by selection of evaluation criteria. The choice of criteria depends on data availability and the consideration of control and impact factors. When combined, the selected indices form comprehensive indicators of flood risk. They were derived through data processing and analysis in a GIS environment. The AHP module in the AHP-SA model was employed to weight each criterion index. The weighted criteria indices were then standardized into different risk levels and aggregated to a classified risk map as the output of the framework. The evaluation results were finally verified using hydrological data and remotely sensed images.

![](images/f3a3b0fd9723f5c4114f287fab1b703b32fd5cb79c09d25329eb8a6c68d80e46.jpg)  
Fig. 1. Study area viewing from a color composite (R2G4B7) Landsat ETM+ image.

## 2.3. Selection of criteria and risk factors

Flood risk arises from the combination of hazards and vulnerabilities at a particular location. Flood risk assessment requires systematic collection and analysis of data, and should consider the dynamic nature of hazards and vulnerabilities that result from processes such as landuse and climate change and environmental degradation. The focus of this study was precipitation (hazard) and landscape (vulnerability).

In this study, hazard is defined as floods caused by extreme (severe and prolonged) precipitation which is the driving factor for flood disaster; whereas vulnerability is hazard inducing environment determined by formative factors which refers mainly to other climate variables and underlying surfaces, including evapotranspiration (ET), topography, river network, vegetation and soils, which play a vital role in the redistribution of floods.

Based on data availability, factors identified that need to be considered when deriving risk assessment criteria were climate (rainfall and ET), hydrology (river network), topography (elevation and slope), soils and land cover (retention). These factors interactively influence and control the dynamic processes of flooding. The intensive and/or extensive rainfall was derived as hazard, other measures such as ET, elevation, slope, drainage density, distance to nearest creeks/rivers, and potential soil water retention were estimated to represent the vulnerabilities. Six indices were considered as most critical criteria for risk assessment.

Major data collected from different sources can be classified into three categories: (1) time series observations, including daily stream flow from 1963 to 2013; (2) rasters, including DEM at a 25 m resolution, daily rainfall from 2000 to 2013 at a 5 km resolution, daily ET from 2000 to 2011 at a 250-m resolution, MODIS imagery from 2000 to 2012 at a 500 m resolution, land cover at a 50 m resolution, and soils at a 1-km resolution; (3) vectors, including the study area boundary and the river network. Data was processed using ArcGIS version 10.1. The vector datasets were rasterized. All datasets were then projected, resampled to a 50 m grid cell, clipped to the study area and registered, so all input grids accurately overlaid with the same projection, cell size and extent.

## 2.4. Criteria/indices derivation

## 2.4.1. Rainfall

To examine whether rainfall extremes have changed over time a variety of extreme rainfall indices can be defined (Karl et al., 1999). Gridded daily rainfall data (2000–2012, at 5 km resolution) provided by the Australian Government Bureau of Meteorology (BOM) from the Australian Water Availability Project (AWAP; Jones et al., 2009) were collected and analyzed. Two indices were derived from the AWAP data: the maximum annual peak 1-day precipitation $( R _ { m a x } )$ , and the mean annual count of heavy precipitation days $( R _ { d a y } )$ with daily precipitation ≥ 10 mm which is defined as a threshold for heavy precipitation by Australian Government Bureau of Meteorology (http://www. bom.gov.au/climate/change/about/extremes.shtml). The former was extracted by taking the highest values of maximum annual daily rainfall during the time period from 2000 to 2012 (Fig. 3a); and the latter was calculated by averaging the annual number of heavy rainfall days among these 13 years (Fig. 3b).

![](images/665e1657627c36170ba6b135f26d278a3ae226dc64e8442f8b3ed6cbf226cb51.jpg)  
Fig. 2. Conceptual framework of SMCDM. R is rainfall; ET is evapotransparition; $R _ { m a x }$ is the maximum annual peak 1-day precipitation $( 2 0 0 0 - 2 0 1 2 ) ; E T _ { m a x }$ is ET associated with $R _ { m a x } ; R _ { d a y } \mathrm { i } s$ the mean annual count of heavy precipitation days with daily precipitation ≥ 10 mm (2000– $- 2 0 1 2 ) ; E T _ { d a y }$ covers the same period of $R _ { d a y } ; R _ { m e a n }$ is the mean daily rainfall (mm) o $\mathrm { \dot { R } } _ { d a y } ;$ ET<sub>mean</sub> is the mean daily ET (mm) of $E T _ { d a y } ;$ NWI denotes net-water index; DEM means digital elevation model; SWR is defined as soil water retention. ARI refers to annual recurrence interval; MODIS stands for Moderate Resolution Imaging Spectroradiometer: and OWL, represent the Open Water Likelihood algorithm

## 2.4.2. ET

ET is the sum of evaporation from water, soil and plants. While precipitation is the key driver for flooding, it is the effective rainfall, after allowing for evaporation, which actually contributes to runoff, or floods.

![](images/a31194d32c8ba429e359ce2bf7203af6c87360232025b661fb1f1bafa41a1ace.jpg)

This is obviously a more critical aspect during summer, when potential evapotranspiration rates are at their highest, but even during the autumn and winter the evaporative regime contributes to the antecedent conditions, which is critical in determining how a landscape responds to a rainfall event. Gridded 8-days mean Actual ET datasets (2000–2012, at a 250-m resolution) derived from interpolated climate surfaces and MODIS 8-day reflectance data (Guerschman et al., 2009) were investigated. Two indices corresponding to the above rainfall indices were derived. One is ET associated with maximum annual peak 1-day precipitation $( E T _ { m a x }$ in Fig. 4a); and the other is a net-water index (NWI in Fig. 4c) which is expressed as:

![](images/a86f5af8c1177089bdb0098978da1f2eb8c4223c9a840d4cde040eae461a2364.jpg)

![](images/8a4b6658e09af62d3c0823fae1fabd42c4f815b9bd3db07c7b2808fbe9ca001f.jpg)  
Fig. 3. Spatial distribution of rainfall characteristics between 2000 and 2012. (a) maximum annual peak 1-day precipitation, (b) mean annual count of heavy precipitation days with daily precipitation ≥ 10 mm and (c) mean daily rainfall of heavy precipitation days with daily precipitation ≥ 10 mm.

$$
N W I = \frac {R _ {\text { mean }}}{E T _ {\text { mean }}}
$$

where $R _ { m e a n }$ (Fig. 3c) is the mean daily rainfall (mm) of the heavy precipitation days (with daily precipitation ≥ 10 mm) during 2000 and 2012; and $E T _ { m e a n }$ (Fig. 4b) is the mean daily ET (mm) corresponding to the heavy precipitation days over the same period.

## 2.4.3. Soil water retention (SWR)

Flooding is impacted by how much water is stored in the soil from previous flooding and local rainfall, described as ‘antecedent conditions’. Prolonged, severe drought depletes stores of water in soil, which means that larger flows are then required for inundation to occur. Soil water is influenced by vegetation type and soil properties. Different vegetation and soil types have different water infiltration capacities. The potential maximum soil water retention was calculated cell by cell using a spatial hydrological modeling approach, which is driven by the Soil Conservation Service Curve Number (SCS CN) method (McCuen, 1982). The CN values are determined by the soil hydrologic characteristics and ground cover conditions. They can be referenced from the list published by SCS (1986). Land cover data (Fig. 5a) were acquired from Catchment Scale Land Use Mapping for Australia — CLUM (Lesslie et al., 2006). Soil texture data (Fig. 5b) were obtained from the Digital Atlas of Australian Soils at a scale of 1:2,000,000, and classified into hydrologic soil group (HSG). HSG reflects soil infiltration rates. Group A (sand, loamy sand or sandy loam) has the highest rate, and Group D (clay loam, silty clay loam, sandy clay, silty clay or clay) has the lowest rate. Group B (silt loam or loam) and Group C (sandy clay loam) have moderate to slow rates. The land cover and HSG datasets (Fig. 5a and b) were intersected to estimate the spatial distribution of CNs (Fig. 5c) under the possible combination of HSG and cover type (Table 1; Chen et al., 2014).

On the basis of the CN method, the potential maximum SWR (Fig. 5d) at cell i (SWR<sub>i</sub>) is parameterized as a function of a CN (CN<sub>i</sub>) value for the cell. This is given by

$$
S W R _ {i} = S W R _ {0} (1 0 0 / C N _ {i} - 1)
$$

where $C N _ { i }$ is an integer, $0 < C N _ { i } < 1 0 0$ and $S W R _ { 0 }$ is a scale factor depending upon the unit used (e.g. $S W R _ { 0 } = 1 0$ for units of inches, and $S W R _ { 0 } = 2 5 4$ for units of millimeters).

## 2.4.4. Topographic characteristics

Topography has an important influence on flood formation and redistribution. A surface with a lower elevation has a higher risk because it is easier to be inundated by flood. A surface with a steeper slope has lower possibility of being inundated because the flood can be easily drained towards down-slope. Both elevation (Fig. 6a) and slope (Fig. 6b) were generated from the DEM at a 25 m resolution.

## 2.4.5. Drainage features

![](images/a0122051a1d058309be571b956c375b260dbb7f994612fd7d52d7e14886df806.jpg)

The occurrence of flood disaster is related to the distribution of the drainage system. Drainage indices – drainage proximity and drainage density – were designed to account for inundation from individual creek and multiple creeks, respectively. Drainage proximity indicates the distance to the closest river and drainage density refers to the length of rivers per unit area. Both indices were derived from named rivers of Geofabric surface network (BOM, 2011). The proximity (Fig. 7a) was obtained using the Multiple Buffer operator, and the density (Fig. 7b) was calculated from the Line Density function using a 1-km radius.

## 2.5. Risk assessment model

## 2.5.1. Criteria standardization and weighting

The criterion indices were converted to relative ratings from 1 to 4 to represent high to low risk according to specific threshold values. These standardized input were displayed in the AHP-SA tool interface (Fig. 8a). The weighting of the input criteria was achieved with the AHP module (Saaty, 1980) equipped to compare spatial criteria in the AHP-SA model. AHP is commonly used and widely accepted in decision making. A pair-wise comparison matrix (PCM) is the basic measurement mode of AHP, which provides a mathematically robust way to derive criteria weights. One of the emphases of applying AHP is to

![](images/509fd7aca348b8ca56d5d35bcdfc6093b33ab875f2533ee017c9e237911f2fcc.jpg)

![](images/0ef3d996560515cbff9bcb8b24565d7eb462dce7f0bcec4ec67d4fe47e8bb771.jpg)  
Fig. 4. Spatial distribution of ET characteristics between 2000 and 2012. (a) ET associated with $R _ { m a x } .$ in Fig. 3a, (b) ET corresponding to $R _ { m e a n } \mathrm { i }$ in Fig. 3c and (c) mean net-water index NWI averaged over the same period.

Table 1  
![](images/e92f6ffa081e43a7e48cbd7c0877a9b9163960043cba523b8a3a690648bd8fb8.jpg)

![](images/bf45c41044b27d87f3fba1eb50b054ace748ae90f4dcbe646ed28c009e589d97.jpg)

![](images/15a7b4cb6d3f19764e6752d5054d004676b218815ab0c675933b4ea963e67a1d.jpg)

![](images/f3560ef65df8d6357ea4b912372ef3889d6b33b6f48d7a54578857ebaf998040.jpg)  
Fig. 5. Spatial data ((a) Land cover, (b) soil texture and (c) curve number) used for derivation of soil water retention index ((d) potential maximum soil water retention)

avoid the ad hoc nature of even weighting. The approach requires experts' best judgments to the relative importance of one criterion index against another in the PCM. Experts' advice was obtained during the selection and weighting of criteria. A group of experts, including groundwater and surface-water hydrologists, ecologist, soil scientist, environmental scientist and GIS specialist, were brought together not just scientifically, but physically – in the same room – to discuss requirements, to agree terminology, and to promote mutual understanding of criterion indices and their impacts on flood risk evaluation. In this way they could move forward together in the process of weighting criterion indices. All indices were compared against each other in the AHP window which has the capability to list criteria and to establish the PCM (Fig. 8a). Each element in the PCM was assigned a value by these experts to express the relative importance among the criteria. The rating employs an underlying semantic scale which has values representing the member of the set: {9, 8, 7, 6, 5, 4, 3, 2, 1, 1/2, 1/3, 1/ 4, 1/5, 1/6, 1/7, 1/8, 1/9}, with 9 representing absolute importance and 1/9 the absolute triviality (Saaty and Vargas, 1991). The AHP module in the AHP-SA tool allows the values in the PCM to be modified by the experts through an iterative agreement procedure to elaborate the consensus PCM in Fig. 8a in keeping with expert opinions and statements. In this study, the PCM built by the integration of experts' experience, comprehensive literature review and professional expertise is given in Table 2. $R _ { m a x }$ was regarded slightly more important than $E T _ { m a x , }$ and significantly more important than SWR, hence a value of 2 and 3 was assigned to the corresponding matrix position (first row in Table 2), respectively. The transpose position automatically gets a value of the reciprocal value, in this case 1/2 (0.50) or 1/3 (0.33). The weights of all criteria were then automatically derived based on the constructed PCM (Fig. 8a).

Simplified curve number lookup table for study area. (adapted from SCS, 1986)

<table><tr><td>Cover</td><td>HSG_A</td><td>HSG_B</td><td>HSG_C</td><td>HSG_D</td></tr><tr><td>Nature conservation</td><td>30</td><td>55</td><td>70</td><td>77</td></tr><tr><td>Other protected areas including indigenous uses</td><td>36</td><td>60</td><td>73</td><td>79</td></tr><tr><td>Minimal use</td><td>81</td><td>88</td><td>91</td><td>93</td></tr><tr><td>Grazing natural vegetation</td><td>39</td><td>61</td><td>74</td><td>80</td></tr><tr><td>Production Forestry</td><td>30</td><td>55</td><td>70</td><td>77</td></tr><tr><td>Plantation Forestry</td><td>32</td><td>58</td><td>72</td><td>79</td></tr><tr><td>Grazing modified pastures</td><td>49</td><td>69</td><td>79</td><td>84</td></tr><tr><td>Dryland cropping</td><td>69</td><td>79</td><td>86</td><td>90</td></tr><tr><td>Dryland horticulture</td><td>53</td><td>70</td><td>85</td><td>89</td></tr><tr><td>Irrigated pastures and cropping</td><td>64</td><td>75</td><td>83</td><td>87</td></tr><tr><td>Irrigated horticulture</td><td>43</td><td>65</td><td>76</td><td>82</td></tr><tr><td>Intensive animal and plant production</td><td>89</td><td>92</td><td>94</td><td>95</td></tr><tr><td>Rural residential</td><td>48</td><td>66</td><td>78</td><td>83</td></tr><tr><td>Urban intensive uses</td><td>77</td><td>85</td><td>90</td><td>92</td></tr><tr><td>Mining and waste</td><td>77</td><td>75</td><td>80</td><td>85</td></tr><tr><td>Water</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

## 2.5.2. Risk evaluation

In this study, flood risk is defined as a weighted sum, which is a compensatory aggregation function in the AHP-SA tool. Based on the criterion indices, the ood risk assessment model was established as follows:

$$
\begin{array}{l} R i s k _ {i} = \sum_ {i = 1} ^ {n} w _ {i} I _ {i} (x, y) \\ \quad = w _ {1} I _ {1} (x, y) + w _ {2} I _ {2} (x, y) + w _ {3} I _ {3} (x, y) + w _ {4} I _ {4} (x, y) + w _ {5} I _ {5} (x, y) \\ \quad + w _ {6} I _ {6} (x, y) + w _ {7} I _ {7} (x, y) + w _ {8} I _ {8} (x, y) + w _ {9} I _ {9} (x, y) \end{array}
$$

where $\mathsf { W } _ { \mathrm { i } }$ is the weight of the ith criterion index; $I _ { i } ( x , y )$ is the contribution function of that normalized criterion index; x, y are the geographical coordinates of the cell/pixel; and n is the number of indices used $( \mathtt { n } = 9$ in this study). The I (x, y) follows the order of (1) $R _ { m a x } ,$ (2) $R _ { d a y , } \left( 3 \right) E T _ { m a x , } \left( 4 \right)$ NWI, (5) SWR, (6) elevation, (7) slope, (8) proximity and (9) density.

The weighted criterion maps (Fig. 9a–i) were then aggregated, according to the derived base criteria weights, to produce a final suitability map (Figs. 8b; 9j).

## 3. Result and discussions

A flood risk map (Figs. 8b; 9j) was delineated as an output from the spatial risk evaluation framework. According to the risk assessment indices (Fig. 9a–i) input into the AHP-SA model in the framework, flood risk is divided to four levels: high (red), medium (orange), low (yellow) and no-risk (green).

## 3.1. Result verification

Observed daily flow data (Fig. 10) were obtained from the downstream gauging station 130401A. Over 60 years of long-term daily stream flow from 1963 to 2013 was examined to derive annual recurrence intervals (ARIs) using the partial duration flood frequency analysis in River Analysis Package (Stewardson and Marsh, 2004). The estimated 1-in-1, 1-in-2, 1-in-5, 1-in-10, 1-in-20 and 1-in-50 ARI flows for the study area are 40, 180, 390, 600, 1000 and 1800 GL/day, respectively.

Extent of flood inundation can be detected from remotely sensed data (Chen et al., 2011, 2013a, 2014; Huang et al., 2015; Wang et al., 2015). In this study, MODIS imagery was used to verify the resultant flood risk evaluation. Flow peaks, or floods, which were defined as daily mean discharges greater than the 1-in-1 ARI flow, that is 130 GL/day, were extracted from the flow time series between 2000 and 2012, which covers the entire period of available MODIS imagery. The

a

![](images/4a4eb9b2be4d5ee12b2a1d6a6ec54b61de4c84d1291e4c2919ab38a2bbaa15f6.jpg)

![](images/4ca59e53dcd16144c2cb2d7ec6f9fef73a8ade3881a3c15fc028da481bb45fe3.jpg)  
b  
Fig. 6. Spatial distribution of topographic indices ((a) elevation and (b) slope) derived from DEM.

flooding dates were then used to acquire corresponding MODIS images. The largest flood event in the area was observed as less than 800 GL/day, which is smaller than the magnitude/size of the 1-in-20 ARI flood. The inundation extent was detected from these images by applying the Open Water Likelihood (OWL) algorithm/index (Ticehurst et al., 2014; Huang et al., 2014b; Li et al., 2015a,b). The OWL represents the probability of the presence of standing water within a MODIS 500 m pixel (Chen et al., 2011, 2012). The pixel values of the OWL images range from 0 to 100, which can be interpreted spatially as indicating no inundation within the pixel area (OWL = 0) to inundation occurring over the entire pixel area (OWL = 100). All OWL images were aggregated to a maximum flood inundation extent map by taking the maximum OWL values among the overlaid pixels. This map was used as a surrogate for ground truthing for the verification of the final flood risk map.

![](images/75f09bec4fdfe98437d3f02fc28679b36078d52ba3efdaeeff510b3b6bd10288.jpg)

The flood risk map (Fig. 11a) was compared to the maximum flood inundation extent map (Fig. 11b). This comparison provides a partial verification of our modeling approach because inputs to the risk assessment model are independent of the inundation detected from the MODIS images. The modeling results conform basically and reasonably to the actual disaster data with more than 93% actual inundation overlaying the modeled risk areas (Fig. 11c). Within the area delineated

![](images/655f045c30cd542c660b1020ca474d873fd03dc5d367999d00cdc041aa6b6ec3.jpg)  
Fig. 7. Spatial distribution of drainage features ((a) proximity and (b) density) derived from river network.

a  
![](images/f45fe82e8744a438338ec64b3b7a9530455f8fd206b8e8bea07e72f02227756c.jpg)

![](images/8c05c8678b95b3a9e085b13bbf6bcd30e73a8a187efbf59f5e181e232b085657.jpg)  
b  
Fig. 8. Example snapshots of AHP-SA tool interface: (a) AHP window mainly consists of PCM and derived weights; and (b) main interface displays output risk map.

Table 2  
Pair-wise comparison matrix and calculated criteria weights.

<table><tr><td></td><td> $R_{max}$ </td><td> $R_{day}$ </td><td> $ET_{max}$ </td><td>NWI</td><td>SWR</td><td>Elevation</td><td>Slop</td><td>Proximity</td><td>Density</td><td>Weight</td></tr><tr><td> $R_{max}$ </td><td>1.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>3.00</td><td>3.00</td><td>2.00</td><td>3.00</td><td>3.00</td><td>0.2087</td></tr><tr><td> $R_{day}$ </td><td>1.00</td><td>1.00</td><td>2.00</td><td>1.00</td><td>1.00</td><td>2.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>0.1397</td></tr><tr><td> $ET_{max}$ </td><td>0.50</td><td>0.50</td><td>1.00</td><td>0.50</td><td>1.00</td><td>2.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>0.1024</td></tr><tr><td>NWI</td><td>0.50</td><td>1.00</td><td>2.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>0.1382</td></tr><tr><td>SWR</td><td>0.33</td><td>1.00</td><td>1.00</td><td>0.50</td><td>1.00</td><td>1.00</td><td>0.50</td><td>2.00</td><td>2.00</td><td>0.0909</td></tr><tr><td>Elevation</td><td>0.33</td><td>0.50</td><td>0.50</td><td>0.50</td><td>1.00</td><td>1.00</td><td>0.50</td><td>2.00</td><td>2.00</td><td>0.0779</td></tr><tr><td>Slope</td><td>0.50</td><td>1.00</td><td>1.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>1.00</td><td>2.00</td><td>2.00</td><td>0.1272</td></tr><tr><td>Proximity</td><td>0.33</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>1.00</td><td>2.00</td><td>0.0621</td></tr><tr><td>Density</td><td>0.33</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.50</td><td>1.00</td><td>0.0529</td></tr></table>

![](images/ba79836533be05cf0ebce037abbb8f84f69508e0389e187b30fbdbdd15f2d7b2.jpg)  
a

![](images/079325171582cb4d1f001580e915ca2c015ed634a746221f8e0a8fc1be267cd5.jpg)  
b

![](images/b85f9e8d875dda097f0b1497f3b06c9fa763965af061813fa5253aa5ec53513e.jpg)

![](images/08b973a0b171a7fb14872aa52fd78558253a6cadf95f7214d53965f257b3e50e.jpg)

![](images/3afa359b782caff96a07a12e1422a61eec7609d41ac3d612e3cf93285a4d078b.jpg)

![](images/997c3518665b63a1dd3a4916d130faec86ee265155af9f1bf8504a90dc3b8f49.jpg)  
f

C  
e  
![](images/40be6021394c733bee2c66792e91fbc515bf580ba00f6d84de38fa8ada8e7bae.jpg)  
g

![](images/a2d7b1167909e3ddd917f105dd4c1bb4d20ec352b0f3e047dad16e7f71af55a3.jpg)  
h

d  
![](images/639f93cfc7c4774df68e274dc28ed93c2e1bddc14df457768ae6f7ba627d9e16.jpg)

![](images/426170d9efdf0d77b98038d529865b491d8608c8f489fcb9d7cdfd77e55cbfa2.jpg)  
Fig. 9. Risk assessment indices input into the model in the study area were (from top-left to bottom-right) (a) $R _ { m a x }$ and $( \mathsf { b } ) R _ { d a y }$ derived from daily rainfall grids, $\left( \mathrm { c } \right) E T _ { m a x }$ derived from daily ET grids, (d) NWI derived from daily rainfall and ET surfaces, (e) SWR derived from soil and land cover, (f) elevation and (g) slope both derived from a DEM, (h) proximity and (i) density derived from river network. Also shown is (j) the resultant risk map.

## 3.2. Risk distribution pattern

as maximum inundation extent, about 23% is classified as high risk, 36% has medium risk and 34% has low risk. 7% mismatched pixels were found to have low OWL values, which are mainly spread in the northwest part of the study area. More than 80% of them have an OWL value smaller than 10, plus another 10% with a value between 10 and 20. This indicates the probability for these areas to be inundated is very low. The remaining errors could be explained by the uncertainties introduced in the process of MODIS inundation detection (Ticehurst et al., 2014; Chen et al., 2013a). It should be noted that the modeled inundation extent is, in fact, much larger than the actual inundation extent. This could be due to (1) MODIS images are only available from 2000 afterwards, (2) quality images are hard to find during severe rainfall or large flood events, (3) MODIS 8-days composite images used in this study could have missed out flash rainfall events and (4) the actual extent only represents the maximum flood extent (b1-in-20 flood) observed in the study area during the same period. A severe rainfall event can cause an inundation much larger than that from a 1-in-20 flood. Therefore, while MODIS 8-days composite data provides the most realistic way to achieve the goal of verifying modeling results, they are often limited by cloud cover during flooding events, their spatial resolution (500 m pixel) is not always suited to small study areas, and the loss of temporal detail through the compositing process makes them inadequate for fast moving floods.

The resultant risk map (Fig. 11a) reveals the extent and distribution of the flood risk in the study area. For each risk class, the percentage of the study area was calculated from the risk map (Fig. 11a). About 16% of the total study area is classified as high risk. 32% is medium risk. 36% is low risk and 16% is no risk. Locations of the highest risk coincide well with the areas where $R _ { m a x }$ greater than 150 mm (Fig. 11a) since this criterion index received the highest weight. Drainage proximity and density were assigned the smallest weight, partly due to their almost uniform values across the region. Neither of them had a significant impact on the evaluation result. However, the effect of both is especially critical to overbank inundation. Slope and elevation are not only essential factors, but also reliable criteria derived from the high-resolution DEM. They can finely discriminate land units to delineate areas of different risk levels for a detailed assessment. These two indices accordingly received higher weights. They produced relatively significant impacts on the resultant risk map, which can be obviously observed, particularly in the north-west area. It is also interesting to notice that three criteria, $R _ { d a y } , E T _ { m a x }$ and NWI (Fig. 10b,c and d), all received fairly high weights, however, their influence are not as visible as the others, such as elevation which has a lower weight. $R _ { d a y }$ displays a relatively similar trend to $R _ { m a x } ,$ whereas NWI and $E T _ { m a x }$ follow the same pattern with ET $( E T _ { m e a n }$ in Fig. 4b) exceeding precipitation $( R _ { m e a n }$ in Fig. 3c) across the region. They contribute most to the central part across west to east. Retention, together with slope, is one of major drivers in the central south of the study area. It is critical to know that the model identifies the combined risk due to unfavorable $E T _ { m a x } ,$ NWI, slope and elevation properties of the central part of the study area. It has highlighted the usefulness of the proposed model, in that it was able to identify a medium risk area in that region that would have been missed in a model based solely on the dominant risk indicator $\left( R _ { m a x } \right)$ . The risk map (Fig. 11a) clearly shows about half of the study area is classified as medium–high risk. Six mines in the central and south of the study area are exposed to medium–high flood risk. Ten mines, mainly located in the northwest of the area, lie in the relatively safe region with seven of these falling in the low risk zone and three in the safe zone. These results, therefore, provide a baseline information which need to be considered before offering management options for mine water management under ooding conditions.

![](images/bc459e75c692ea595213ba390335d0210425ee30f1dba0085fc54f38ca9a7f69.jpg)  
Fig. 10. Daily flow time series (from gauge 130401A) which were used to link MODIS images in this study (due to the availability of MODIS data)

![](images/22c5605144e92a5b6483553ae483a66d34b1da02d31895e8bd07f23d2181b5a6.jpg)  
a

![](images/014e44bf24fa17ae6495c6ab002a94ed57f97b6e18c0d5375a5d62516ebab4d6.jpg)  
b

![](images/26244f7858f23404759d79adc5b9d7957a235e509edff98343e213bc540e9d22.jpg)  
C  
Fig. 11. Result verification: (a) risk map based on modeled inundation extent (black dots are mines; blue dot is gauge 130401A), (b) actual inundation extent from MODIS imagery and (c) overlay comparison of modeled and actual inundation extent.

## 3.3. Uncertainty identification

The whole risk evaluation process did not involve optimisation of any sort, which means the absence of a modeled optimum avoids over-determining the modeling process where input data are of variable quality and mixed type. The operations and outcomes are very much dependent upon the experts and users. There exist some common concerns on the uncertainties involved in the proposed approaches to integrate the knowledge of experts in certain procedures:

(1) Specific classification values (Figs. 3 to 7) and thresholds (Fig. 9) of the model input and output have a crucial impact on evaluation results. Their determinations were significantly influenced by the views expressed by experts.

(2) To ensure meaningful criteria weights, expert knowledge has to be taken into account. The experts were involved in the pairwise comparison process to fill in the PCM in the AHP module of the framework. The relative rankings of input criteria depend heavily upon the opinions of experts.

However, with the aid of the visualization module in AHP-SA (Fig. 8), the participatory procedures support subsequent input data classification, threshold determination, criterion weight derivation and output results interpretation. Map layers can be displayed in the framework to show a range of indices and evaluations based on different classification and thresholds (Chen et al., 2010, 2013b). The AHP-SA model interface facilities for incorporation of multiple expert opinions, and multiple stakeholder views were added through pair-wise comparison. This enables the decision tension between particular viewpoints to be examined and visualized. A process of comparison of scenarios from different perspectives using the AHP-SA tool could also reveal redundancies, correlations and interrelationships between spatial data, but no attempt at quantification was made in this study.

## 4. Concluding remarks

A spatial framework for the assessment of regional flood risk under extreme climates was developed. It was demonstrated using an Australian case study in Central Queensland where annual and seasonal average rainfall is strongly influenced by natural variability, and extreme weather events, such as cyclones, have a significant impact on flooding hazard. The SMCDM approach used in this study couples AHP-based MCDM techniques with GIS. Incorporating GIS enhances the visualization capability and increases the assessment efficiency. Criteria considered in such an analysis are diverse and complex. The GIS approach integrates spatial variability of climate, hydrology, terrain, vegetation, soil and other relevant parameters. This allows delineation of areas of various risk ratings for a detailed assessment. SMCDM was found to provide transparency and accountability to decision procedures which may otherwise have unclear motives and rationale. Transparency in SMCDM is mainly achieved by explicitly classifying input spatial data and weighting decision criteria. The reasons for choice are made explicit and past decisions can easily be audited. With adjustments and improvement to evaluation criteria and their weights (according to the circumstances and available data), this spatial framework would be applicable to other extreme climates.

The derivation of criteria indices and the determination of the weights for each criterion or index are vital because they would directly affect the evaluation result. AHP can be one of the fit-for-purpose options. One of the benefits of AHP is the use of a standardized process by which to compare criteria presented with both quantitative and qualitative data, although some suggest that the scale used for comparisons should be non-linear. The AHP-SA model incorporated into the risk evaluation framework in this study proved to be highly suitable for determining indicator weights due to its advantage of integrating expert knowledge in a simple way. The satisfactory match between MODIS detected and modeled results have showed that the proposed linear model in the risk assessment framework describes the complicated nonlinear processes well, and the evaluation result is meaningful. The results show that this method is effective to evaluate flood risk. It provides intuitive space information for decision makers. The framework and associated tool can be used in a range of analytical tasks within the area of scientific advice and analysis for the policy-making process. The resultant risk map is helpful in prioritizing flood warning systems and guiding preparations for disaster prevention and responses.

The application of SMCDM in risk assessment is widespread and growing. Risk evaluation is typically a multi-objective problem which makes SMCDM a well suited decision support tool. The outcomes are often intangible and are measured in a variety of units. SMCDM has been found to assist with conflict resolutions, stakeholder participation and community engagement. It has also been shown to improve the auditability, transparency and analytic rigor of risk management decisions. The integration of spatial data and application of the SMCDM procedures can provide a comprehensive database and a guide map for decision makers in order to achieve sustainable water resource management in mining.

Finally, we have restricted our analysis to the regional assessment of environmental vulnerability. The selection of criteria was largely limited due to data availability. Several issues need to be further investigated to ensure an adequate and detailed flood risk assessment. These include the use of coarse resolution precipitation data which has directly influenced the assessment results and the model validation which was limited by using 1-in-20 ARI inundation extent, instead of the possible maximum extent, due to image availability. A more comprehensive data collection and an improved assessment are recommended to extend this approach to the whole central QLD. Overall, this study exemplifies the need for multi-disciplinary and cross-sphere approaches, which are essential to producing reliable assessments on flood risk on mine water resources, which can later be translated into policy issues and implemented by water resource managers at a regional scale. The framework will provide an important technical basis for determining measures to prevent flood disaster and enhance the safety of coal mines.

## Acknowledgments

This project is funded by the Australian Coal Association Research Program (ACARP C21037), and supported by CSIRO Land and Water.

## References

Abbot, J., Marohasy, J., 2015. Using artificial intelligence to forecast monthly rainfall under present and future climates for the Bowen Basin, Queensland, Australia. Int. J. Sustain. Dev. Plan. 10 (1), 66–75.

Ahamed, T.R.N., Rao, K.G., Murthy, J.S.R., 2000. GIS-based fuzzy membership model for crop-land suitability analysis. Agric. Syst. 63, 75–95.

BOM, 2011. Australia Hydrological Geospatial Fabric (Geofabric) Product Guide Version 2.0. Bureau of Meteorology, Australia.

Ceballos-Silva, A., López-Blanco, J., 2003. Evaluating biophysical variables to identify suitable areas for oat in Central Mexico: a multi-criteria and GIS approach. Agric. Ecosyst, Environ.95. 371-377

Chandrasekar, K., Sai, M.S., Roy, P.S., Jayaraman, V., Krishnamurthy, R.R., 2009. Identification of agricultural drought vulnerable areas of Tamil Nadu, India: using GIS based multi criteria analysis, Asian I. Environ, Disaster Manag, 1 (1). 43–64.

Chau, V.N., Holland, J., Cassells, S., Tuohy, M., 2013. Using GIS to map impacts upon agriculture from extreme floods in Vietnam. Appl. Geogr. 41, 65–74.

Chen, Y., Paydar, Z., 2012. Evaluation of potential irrigation expansion using a spatial fuzzy multi-criteria decision framework. Environ, Model Softw, 38, 147–157.

Chen Y. Khan S. Paydar Z. 20o7. Irrigation intensification or extensification assessment using spatial modelling in GIS. In: Oxley I. Kulasiri D. (Eds.) MODSIM 2007 International Congress on Modelling and Simulation. Modelling and Simulation Society of Australia and New Zealand pp. 1321–1327 (December 2007)

Chen, Y., Khan, S., Paydar, Z., 2009. To retire or expand? A fuzzy GIS-based spatial multicriteria evaluation framework for irrigated agriculture. Irrig. Drain. 59 (2), 174–188.

Chen, Y., Yu, J., Khan, S., 2010. Spatial sensitivity analysis of multi-criteria weights in GISbased land suitability evaluation. Environ, Model Softw. 25. 1582–1591.

Chen, Y., Cuddy, S., Wang, B., Merrin, L., 2011. Linking inundation timing and extent to ecological response models using the Murray–Darling Basin Floodplain Inundation Model (MDB-FIM). In: Chan, F., Marinova, D., Anderssen, R.S. (Eds.), MODSIM2011,

19th International Congress on Modelling and Simulation. Modelling and Simulation Society of Australia and New Zealand, pp. 4092–4098 (December 2011).

Chen, Y., Huang, C., Ticehurst, C., Merrin, L., Thew, P., 2013a. An evaluation of MODIS daily and 8-day composite products for floodplain and wetland inundation mapping. Wetlands 33 (5), 823–835.

Chen, Y., Yu, J., Khan, S., 2013b. The spatial framework for weight sensitivity analysis in AHP-based multi-criteria decision making. Environ. Model Softw. 48, 129–140.

Chen, Y., Wang, W., Cuddy, S., Pollino, C., Merrin, L., 2012. Spatial modelling of potential water retention under floodplain inundation using remote sensing and GIS. In iEMSs 2012 International Environmental Modelling and Software Society (iEMSs) 6th International Congress on Environmental Modelling and Software ModellingLeipzig, Germany.

Chen, Y., Wang, B., Pollino, C.A., Cuddy, S.M., Merrin, L.E., Huang, C., 2014. Estimate of flood inundation and retention on wetlands using remote sensing and GIS. Ecohydrology 7 (5), 1412–1420.

Davidson, D.A., Theocharopoulos, S.P., Bloksma, R.J., 1994. A land evaluation project in Greece using GIS and based on Boolean and fuzzy set methodologies. Int. J. Geogr. Inf. Syst. 8, 369–384.

Dewan, A.M., Islam, M.M., Kumamoto, T., Nishigaki, M., 2007. Evaluating flood hazard for land-use planning in Greater Dhaka of Bangladesh using remote sensing and GIS techniques. Water Resour. Manag. 21, 1601–1612.

Feizizadeh, B., Roodposhti, M.S., Jankowski, P., Blaschke, T., 2014. A GIS-based extended fuzzy multi-criteria evaluation for landslide susceptibility mapping. Comput. Geosci. 73.208-221.

Foudi, S., Oses-Eraso, N., Tamayo, I., 2015. Integrated spatial flood risk assessment: the case of Zaragoza. Land Use Policy 42, 278–292.

Foulds, S.A., Brewer, P.A., Macklin, M.G., Haresign, W., Betson, R.E., Rassner, S.M.E., 2014. Flood-related contamination in catchments affected by historical metal mining: an unexpected and emerging hazard of climate change. Sci. Total Environ. 476–477, 165–180.

Gao, L., Connor, J.D., Barrett, D., Chen, Y., Zhang, X., 2013. Strategic water management for reliable mine water supply under dynamical climates. MODSIM2013, 20th International Congress on Modelling and Simulation, Adelaide, Australia.

Gao, L., Barrett, D., Chen, Y., Zhou, M., Cuddy, S., Paydar, Z., Renzullo, L., 2014. A systems model combining process-based simulation and multi-objective optimisation for strategic management of mine water. Environ. Model Softw. 60, 250–264.

Grayson, R., Kay, P., Foulger, M., 2008. The use of GIS and multi-criteria evaluation (MCE) to identify agricultural land management practices which cause surface water pollution in drinking water supply catchments. Water Sci. Technol. 58 (9), 1797–1802.

Guerschman, J.P., Van Dijk, A.I.J.M., Mattersdorf, G., Beringer, J., Hutley, L.B., Leuning, R., Pipunic, R.C., Sherman, B.S., 2009. Scaling of potential evapotranspiration with MODIS data reproduces flux observations and catchment water balance observations across Australia. J. Hydrol. 369, 107–119.

Huang, C., Chen, Y., Wu, J., 2014a. Mapping spatio-temporal flood inundation dynamics at large river basin scale using time-series flow data and MODIS imagery. Int. J. Appl. Earth Obs, Geoinf, 26, 350–362

Huang, C., Chen, Y., Wu, J., 2014b. DEM-based modification of pixel-swapping algorithm for enhancing floodplain inundation mapping. Int. J. Remote Sens. 35 (1), 365–381.

Huang C. Chen Y. Wu L. Li L. Liu R. 2015, An evaluation of Suomi NPP-VIIRS data fon surface water detection, Remote Sens. Lett, 6 (2). 155–164

Jiang, H., Eastman, J.R., 2000. Application of fuzzy measures in multi-criteria evaluation in GIS. Int. I. Geogr, Inf, Sci, 14. 173–184

Jiqun, Z., Chenghu, Z., Kaiqin, X., Masataka, W., 2002. Flood disaster monitoring and evaluation in China. Environ. Hazards 4, 33–43.

Joerin, F., Theriault, M., Musy, A., 2001. Using GIS and outranking multicriteria analysis for land-use suitability assessment. Int. J. Geogr. Inf. Sci. 15 (2), 153–174.

Jones, D.A., Wang, W., Fawcett, R., 2009. High-quality spatial climate data-sets for Australia. Aust. Meteorol. Oceanogr. J. 58, 233–248.

Jonkman, S.N., Kok, M., Vrijling, J.K., 2008. Flood risk assessment in the Netherlands: a case study for dike ring South Holland. Risk Anal. 28 (5), 1357–1374.

Kannan, M., Saranathan, E., Anbalagan, R., 2014. Comparative analysis in GIS-based landslide hazard zonation — a case study in Bodi-Bodimettu Ghat section, Theni District Tamil Nadu India Arab L Geosci 8 (2). 691-699

Karl, T.R., Nicholls, N., Ghazi, A., 1999. CLIVAR/GCOS/WMO workshop on indices and indicators for climate extremes: workshop summary. Clim. Chang. 42, 3–7

Karnatak, H.C., Saran, S., Bhatia, K., Roy, P.S., 2007. Multicriteria spatial decision analysis in web GIS environment. Geoinformatica 11, 407–429.

Kienberger, S., Lang, S., Zeil, P., 2009. Spatial vulnerability units expert-based spatial modelling of socio-economic vulnerability in the Salzach catchment, Austria. Nat. Hazards Earth Syst. Sci. 9, 767–778.

Koks, E.E., Jongman, B., Husby, T.G., Botzen, W.J.W., 2015. Combining hazard, exposure and social vulnerability to provide lessons for flood risk management. Environ. Sci. Pol. 47, 42–52.

Kollias, V.J., Kalivas, D.P., 1998. The enhancement of a commercial geographical information system (ARC/INFO) with fuzzy processing capabilities for the evaluation of land resources. Comput, Electron, Agric, 20 79–95.

Kubal, C., Haase, D., Meyer, V., Scheuer, S., 2009. Integrated urban flood risk assessment — adapting a multicriteria approach to a city, Nat Hazards Earth Syst Sci, 9 1881–1895

Lesslie, R., Barson, M., Smith, J., 2006. Land use information for integrated natural resource management — a coordinated national mapping program for Australia. J. Land Use Sci. 1 (1), 45–62.

Li, L., Chen, Y., Yu, X., Liu, R., 2015a. Sub-pixel flood inundation mapping from multispectral remotely sensed images based on discrete particle swarm optimization. ISPRS J. Photogramm. Remote Sens. 101, 10–21.

Li, L., Chen, Y., Xu, T., Liu, R., Shi, K., Huang, C., 2015b. Super-resolution mapping of wetland inundation from remote sensing imagery based on integration of backpropagation neural network and genetic algorithm. Remote Sens. Environ. 164, 142–154.

Malczewski, J., 2004. GIS-based land-use suitability analysis: a critical overview. Prog. Plan. 62 (1), 3–65.

McCuen, R.H., 1982. A Guide to Hydrologic Analysis Using SCS Methods. Prentice-Hall, Inc., Englewood Cliffs, New Jersey, p. 145 (No. 35174).

Meyer, V., Scheuer, S., Haase, D., 2009. A multi-criteria approach for flood risk mapping exemplified at the Mulde river, Germany. Nat. Hazards 48, 17–39.

Nekhay, O., Arriaza, M., Guzmán-Álvarez, J.R., 2008. Spatial analysis of the suitability of olive plantations for wildlife habitat restoration. Comput. Electron. Agric. 65, 49–64.

Papaioannou, G., Vasiliades, L., Loukas, A., 2015. Multi-criteria analysis framework for potential flood prone areas mapping. Water Resour. Manag. 29 (2), 399–418.

Rahman, M.A., Rusteberg, B., Gogu, R.C., Lobo Ferreira, J.P., Sauter, M., 2012. A new spatial multi-criteria decision support tool for site selection for implementation of managed aquifer recharge. J. Environ. Manag. 99, 61–75.

Reshmidevi, T.V., Eldho, T.I., Jana, R., 2009. A GIS-integrated fuzzy rule-based inference system for land suitability evaluation in agricultural watersheds. Agric. Syst. 101, 101–109.

Saaty, T.L., 1980. The Analytic Hierarchy Process. McGraw-Hill, New York.

Saaty, T.L., Vargas, L.G., 1991. Prediction, Projection and Forecasting. Kluwer Academic Publisher, Dordrecht, p. 251.

SCS (Soil Conservation Service), 1986. Urban hydrology for small watersheds. Technical Release 55 (TR-55).

Setiawan, I., Mahmud, A.R., Mansor, S., Mohamed Shariff, A.R., Nuruddin, A.A., 2004. GIS grid-based and multi-criteria analysis for identifying and mapping peat swamp forest fire hazard in Pahang, Malaysia. Disaster Prev. Manag. Int. J. 13 (5), 379–386.

Sharma, V., van de Graaff, S., Loechel, B., Franks, D.M., 2013. Extractive Resource Development in a Changing Climate: Learning the Lessons from Extreme Weather Events in Queensland, Australia. National Climate Change Adaptation Research Facility, Gold Coast (110 pp.).

Sicat, S.R., Carranza, E.J.M., Nidumolu, U.B., 2005. Fuzzy modeling of farmers' knowledge for land suitability classification. Agric. Syst. 83, 49–75.

Siddayao, G.P., Valdez, S.E., Fernandez, P.L., 2014. Analytic hierarchy process (AHP) in spatial modeling for floodplain risk assessment. Int. J. Mach. Learn. Comput. 4 (5), 450.

Simonovic, S.P., Nirupama, N., 2005. A spatial multi-objective decision-making under uncertainty for water resources management. J. Hydrol. 7 (2), 117–133.

Smith, M.H., 2013. Assessing climate change risks and opportunities for investors — mining and minerals processing sector. IGCC (Investor Group on Climate Change) Reports. Australian National University.

Stewardson, M., Marsh, N., 2004. River Analysis Program (RAP). www.toolkit.net.au/rap Store, R., Kangas, J., 2001. Integrating spatial multi-criteria evaluation and expert knowledge for GIS-based habitat suitability modelling. Landsc. Urban Plan. 55 (2), 79–93.

Svoray, T., Bar, P., Bannet, T., 2005. Urban land-use allocation in a Mediterranean ecotone: habitat heterogeneity model incorporated in a GIS using a multicriteria mechanism. Landsc. Urban Plan. 72 (4), 337–351.

Thinh, N.X., Vogel, R., 2006. GIS-based multiple criteria analysis for land-use suitability assessment in the content of flood risk management. InterCarto-InterGIS 12. Berlin

Ticehurst, K., Guerschman, J.P., Chen, Y., 2014. The strengths and limitations in using daily MODIS data for identifying flood events. Remote Sens. 6, 11791–11809.

Tiwari, D.N., Loof, R., Paudyal, G.N., 1999. Environmental-economic decision-making in lowland irrigated agriculture using multi-criteria analysis techniques. Agric. Syst. 60, 99–112.

Tkach, R.J., Simonovic, S.P., 1997. A new approach to multi-criteria decision making in water resources. Int. J. Geogr. Inf. Sci. 1 (1), 25–43.

Udoh, J.C., Ekanem, E.M., 2011. GIS based risk assessment of oil spill in the coastal areas of Akwa Ibom State Nigeria, Afr. L. Environ, Sci, Technol, 5 (3) 205–211

Wang, Y., Li, Z., Tang, Z., 2011. A GIS-based spatial multi-criteria approach for flood risk assessment in the Dongting Lake Region, Hunan, Central China. Water Resour. Manag. 25, 3465–3484.

Wang, B., Chen, Y., Lu, C., 2015. Evaluating the impact of flood inundation on FPAR of wetland vegetation using remote sensing and GIS technologies. Environ. Earth Sci. http://dx.doi.org/10.1007/s12665-015-4511-7.

Yang, M., Qian, X., Zhang, Y.C., Sheng, J.B., Shen, D.L., Ge, Y., 2011. Spatial multicriteria decision analysis of flood risks in aging-dam management in China: a framework and case study. Int. J. Environ. Res. Public Health 8 (5), 1368–1387.

Zarekar, A., Zamani, B.K., Ghorbani, S., Moalla, M.A., Jafari, H., 2013. Mapping spatial distribution of forest fire using MCDM and GIS (case study: three forest zones in Guilan Province). Iran. J. For. Poplar Res. 21 (2), 218–230.

Zhang, X., Gao, L., Barrett, D., Chen, Y., 2014. Evaluating water management practice for sustainable mining. Water 6 (2), 414–433.

Zhou, M., Barrett, D., Chen, Y., Gao, L., Cuddy, S., Paydar, Z., Renzullo, L., 2013. A scenario model for mine water management under extreme climate variability. MODSIM2013, 20th International Congress on Modelling and Simulation, Adelaide, Australia