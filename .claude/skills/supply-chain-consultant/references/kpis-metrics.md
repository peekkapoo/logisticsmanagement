# KPIs and Metrics Reference

A consultant is often asked "how do we measure X?" — and the right answer is usually "here are two or three metrics that together will tell you something useful, and here's how to calculate each one." This reference organizes the standard KPIs of supply chain, logistics, procurement, and trade operations by what they actually measure. Formulas are given with enough context to compute them correctly; benchmarks are offered as rough orienting ranges, not as targets.

## Customer-facing service metrics

**On-Time In-Full (OTIF)** is the share of orders delivered on time and complete. Definitions vary — "on time" can mean on the originally promised date, on the revised promised date, or within a delivery window, and "in full" can mean all line items or all requested units. Before reporting OTIF, pin down the definitions; comparisons across organizations that define it differently are meaningless. OTIF = (Orders on time AND in full) / Total orders. Large retailers (Walmart, Tesco, and their peers) impose OTIF penalties on suppliers, which has made the metric central to CPG supply chains.

**Perfect Order** extends OTIF with accuracy and documentation dimensions. A perfect order is on time, in full, damage-free, and with correct documentation. Perfect Order Rate = (Perfect orders) / (Total orders). In SCOR terms, this is the principal reliability metric.

**Fill Rate** measures the share of demand satisfied from on-hand stock. Unit fill rate = units shipped from stock / units ordered. Line fill rate = order lines shipped complete / order lines ordered. Unit fill rate weights large orders more heavily; line fill rate weights each SKU equally. Both matter — quote both when benchmarking.

**Order Cycle Time** is elapsed time from order receipt to customer receipt. Decompose into order processing, picking and packing, dispatch, transit, and customer receipt to identify where time is being spent. Compared against promised lead time to assess reliability.

**Back-Order Rate** is the share of orders that could not be filled from stock and were back-ordered. High and persistent back-order rates often indicate misaligned safety stock, inaccurate forecasting, or upstream supply issues.

## Inventory and working-capital metrics

**Inventory Turns** = COGS / Average Inventory (at cost). Alternatively, sales turns = Sales / Average Inventory, but COGS-based is the apples-to-apples number. Industry turns vary enormously: grocery retailers run 12–20+ turns, fashion retailers 4–6, heavy industrial 3–5, aerospace spares 1–2. Use industry peers as comparators.

**Days Inventory Outstanding (DIO)** or **Days On Hand (DOH)** = (Average Inventory / COGS) × 365. The reciprocal of inventory turns expressed in days. A C2C component and the most intuitive inventory metric for executive audiences.

**Cash-to-Cash Cycle Time (C2C)** = DIO + DSO − DPO. The working-capital heart-rate of the business. Amazon's famously negative C2C (collect fast, pay suppliers slowly, sell inventory before paying for it) finances much of its operation. A supply chain initiative that worsens C2C had better deliver clear service or cost gains to justify it.

**Obsolescence and Excess Inventory**. Obsolete inventory is stock with zero expected future demand; excess inventory is stock above planning-cycle coverage for demand that does exist. Obsolescence Rate = (Obsolete inventory value) / (Average inventory value). Excess inventory can be tracked as the value of SKUs with DOH > N months where N is set by category (e.g., 6 months for fashion, 24 months for industrial spares). Excess and obsolescence combined often represent 5–15% of inventory in poorly managed supply chains; aggressive S&OE processes can reduce this toward 2–3%.

**Inventory Accuracy** = (SKUs matching system record in a cycle count) / (SKUs counted). Any distribution operation below 97–98% inventory accuracy will have chronic picking errors, planning errors, and customer complaints — the metric is that sensitive.

## Forecast accuracy metrics

**MAPE (Mean Absolute Percentage Error)** = (1/n) · Σ|Actualᵢ − Forecastᵢ| / |Actualᵢ|. Intuitive percentage but breaks on near-zero actuals and is biased toward penalizing over-forecasts less than under-forecasts.

**Bias** = (1/n) · Σ(Forecastᵢ − Actualᵢ), expressed as % of mean demand. Positive sustained bias means chronic over-forecasting (inventory risk); negative means under-forecasting (service risk). Many forecasting disasters trace to uncorrected bias rather than high absolute error.

**Weighted MAPE (WMAPE)** = Σ|Actualᵢ − Forecastᵢ| / Σ|Actualᵢ|. Weights each observation by its own magnitude — more meaningful when comparing performance across SKUs of very different volumes, and far less noisy than straight MAPE on low-volume series.

**MASE (Mean Absolute Scaled Error)** = MAE / MAE_naive, where MAE_naive is the error of a simple naive forecast (last period = next period, or seasonal naive). MASE < 1 means the forecast beats naive; MASE > 1 means it does not. Scale-free, interpretable, and recommended for cross-series comparison.

**Forecast Value Added (FVA)** compares the accuracy of a more complex forecast to a simpler one at each stage of the forecasting process (naive → statistical → statistical + adjustments → final consensus). Each stage that does not improve accuracy is subtracting value rather than adding it — a useful way to show that "management override" or "consensus review" processes can actively make forecasts worse.

## Logistics cost and productivity metrics

**Transportation Cost as % of Revenue** and **as % of COGS** are the two standard framings. Typical ranges: 3–6% of revenue for manufacturers, 5–10% for distributors, higher for heavy or low-value-density goods. A sharp rise not explained by fuel or freight market conditions points to mode mix problems, routing inefficiency, or carrier rate erosion.

**Cost per Unit Shipped** or **Cost per Pallet** or **Cost per Container** normalizes cost by an appropriate volume unit. Which denominator to use depends on what drives cost — weight, volume, or units.

**Freight Cost per Lane** tracks rates by origin-destination-mode, typically benchmarked against market indices (SONAR, Xeneta for ocean, DAT for US truckload, Freightos for ocean spot). Persistent deviation from market indicates contract structure problems.

**Truck or Container Utilization** = (Cubic volume or weight actually shipped) / (Usable capacity). Low utilization is money left on the table every shipment. 80–90% is realistic for well-run operations; below 70% warrants investigation into routing, packaging, or consolidation opportunities.

**On-Time Delivery (carrier)** is the carrier-reported metric: share of shipments delivered by the promised transit time. Compare to OTIF, which is customer-facing — a shipment can be on-time-carrier but not on-time-customer if the promise to the customer was based on an unrealistic lead time.

**Pick Productivity** = Lines picked per labor hour, with benchmarks varying by operation type (pallet pick, case pick, piece pick). Combined with pick accuracy (correct picks / total picks; typically tracked at 99.5%+ for mature operations).

**Dock-to-Stock Time** is time from receipt at the inbound dock to available for picking. Short dock-to-stock (a few hours) indicates a well-run operation; long dock-to-stock (days) creates phantom stockouts — the inventory is in the building but unavailable.

## Procurement metrics

**Spend Under Management** = (Spend routed through formal procurement process) / (Total addressable spend). Mature procurement organizations run at 75–90%; low figures indicate rogue spending, maverick buying, and lost leverage.

**Savings Realization** = (Realized savings) / (Forecast savings). Procurement savings notoriously disappear between signed contract and actual P&L impact because buyers keep buying at the old price or volumes do not materialize. Rigorous organizations track both "negotiated savings" and a separately validated P&L impact.

**Supplier Lead Time** and its **variability** are first-order drivers of safety stock. Shaving lead time is often the highest-leverage supply chain intervention — every day of lead time you remove reduces safety stock requirements by a fraction of σ_LT × D_avg.

**Supplier OTIF (inbound)** mirrors customer-facing OTIF applied to supplier performance. Chronic poor supplier OTIF drives inbound-side safety stock and production disruption.

**Price Variance** = (Actual price − Standard/contracted price) × Quantity. Segments into market-driven variance (raw material indices, currency) and behavior-driven variance (off-contract buying, small-quantity emergency purchases).

**PPV — Purchase Price Variance** in accounting usage is similar. Be aware that PPV vs. standard is not the same as savings vs. last year's price — both are useful, measuring different things.

## Trade and customs metrics

**Duty as % of Landed Cost** tracks the weight of customs duty in total landed cost. Categories where this is high (e.g., apparel into the US, automotive parts under certain tariff schemes) are prime candidates for FTA utilization, duty drawback, or tariff engineering.

**FTA Utilization Rate** = (Value of imports claiming preferential FTA treatment) / (Value of imports from FTA partner countries eligible for preference). Many organizations leave tens of basis points on the table by failing to document origin for eligible shipments. A utilization rate below 70% where preferences could apply is usually fixable with better COO processes.

**Customs Clearance Cycle Time** = time from vessel/aircraft arrival to customs release. Benchmark against the country's trade facilitation norms (ASEAN Single Window targets, WCO Time Release Study data). Extended clearance time inflates inventory by the transit days it adds.

**Denied Party / Restricted Party Screening Coverage** = share of transactions screened against sanctions lists (OFAC SDN, EU consolidated list, UN sanctions, national lists) prior to shipment. Below 100% in a regulated supply chain is a material compliance risk.

## Supply chain finance metrics

**Days Sales Outstanding (DSO)** = (Accounts Receivable / Revenue) × 365. Rising DSO with stable payment terms usually means deteriorating collection performance or customer credit quality. A DSO that drops suddenly without a payment term change may reflect supply chain finance program effects on the supplier side.

**Days Payable Outstanding (DPO)** = (Accounts Payable / COGS) × 365. Extending DPO beyond contractual terms is real working-capital benefit to the buyer but real working-capital cost to the supplier — the more sophisticated approach is supply chain finance where both sides benefit.

**Letter of Credit Discrepancy Rate** = (Presentations with discrepancies on first presentation) / (Total presentations). Benchmarks cluster around 60–70% industry-wide, which is quite bad — a well-run trade operations team can drive this below 20% and save material discount fees and payment delays.

## Resilience and risk metrics

**Time to Recover (TTR)** = estimated time for a node (supplier, plant, port, lane) to return to normal capacity after a disruption. Used in scenario analysis — the financial impact of losing a node depends on both TTR and the revenue at risk during that time.

**Time to Survive (TTS)** = time the downstream operation can continue operating at normal output despite the node disruption, given current inventory and alternatives. If TTR > TTS for a node, the supply chain has insufficient resilience to that disruption. Simchi-Levi and colleagues have made this TTR-vs-TTS framing standard.

**Supplier Concentration** = share of category spend with top N suppliers. High concentration is efficient in normal times and fragile in disruption; low concentration is resilient but loses scale economies.

**Geographic / Node Concentration** = share of volume flowing through top N nodes (ports, DCs, lanes). The same trade-off at network level.

## Sustainability and carbon metrics

**Scope 3 Category 4 (Upstream Transportation and Distribution) and Category 9 (Downstream Transportation and Distribution)** emissions under the GHG Protocol are where supply chain typically owns the number. Activity-based calculation uses tonne-kilometers × emission factor by mode (GLEC Framework, or ISO 14083). Spend-based calculation is easier but much less accurate; increasingly unacceptable under evolving disclosure regimes (CSRD in the EU, SEC climate rules, Japan's TCFD adoption).

**Carbon Intensity of Freight** in kg CO₂e per tonne-km varies by mode: rail and ocean are the lowest (ocean containerized roughly 8–15 g/tkm, rail 20–30 g/tkm), road freight moderate (60–120 g/tkm depending on truck type and load), and air freight by far the highest (500–1500+ g/tkm). A 10% mode shift from road to rail on suitable lanes can be the single largest available scope-3 reduction.

## Choosing which KPIs to use

Picking KPIs is itself a consulting question. Three rules worth applying:

First, measure the few things that drive the decisions you actually make. Tracking 80 KPIs on a dashboard nobody reads is pure waste. A distribution operation might live on five: perfect order, inventory turns (or DOH), transportation cost % of revenue, pick productivity, and employee safety (TRIR).

Second, pair opposing metrics so single-metric optimization does not destroy balance. Service level alone gets gamed by over-stocking; cost alone gets gamed by under-serving. Service × cost, or OTIF × working capital, keeps the trade-off honest.

Third, watch for definitional drift. Metrics that quietly redefine themselves over time, or whose components get modified for convenience, destroy trust in measurement. The CFO-friendly version of this rule is "have an owner, have a definition document, have a review cadence, and lock it."
