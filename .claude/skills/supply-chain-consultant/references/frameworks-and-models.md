# Frameworks and Models Reference

A consultant's value often lies in picking the right framework for the problem. Below are the working frameworks for supply chain, logistics, procurement, and operations analysis — with enough mathematical and conceptual detail to apply them correctly, not just name-drop them.

## SCOR — Supply Chain Operations Reference Model

SCOR, maintained by ASCM (Association for Supply Chain Management, formerly APICS), is the dominant process reference model for supply chain. It organizes supply chain activity into six top-level processes: **Plan, Source, Make, Deliver, Return, Enable**. Each decomposes into level-2 process categories (e.g., Plan → Plan Supply Chain, Plan Source, Plan Make, Plan Deliver, Plan Return) and further into level-3 process elements with defined inputs, outputs, and metrics.

SCOR is useful as a common vocabulary across a fragmented supply chain organization, as a diagnostic checklist ("which of these processes is weak?"), and as a benchmarking framework (SCOR's performance attributes — reliability, responsiveness, agility, cost, asset management efficiency — map to defined metrics like perfect order fulfillment, order cycle time, upside supply chain flexibility, total cost to serve, and cash-to-cash cycle time). When advising on a broad supply chain assessment, SCOR is the natural structure. When advising on a specific problem, SCOR is usually too heavy — pick a more focused tool.

## Kraljic Matrix — Procurement Portfolio Analysis

Peter Kraljic's 1983 HBR framework segments purchased items along two axes: **profit impact** (how much the item affects the buyer's profitability — typically proxied by annual spend) and **supply risk** (how hard the item is to source — scarcity, number of suppliers, switching cost, technical complexity). This yields four quadrants with distinct sourcing strategies:

- **Strategic items** (high impact, high risk) — form strategic partnerships, develop joint roadmaps, consider vertical integration, invest heavily in supplier relationship management. Don't tender these on price; they are too important to treat transactionally.
- **Leverage items** (high impact, low risk) — exploit buying power through competitive tendering, reverse auctions, and volume consolidation. Many substitutes exist, so price discipline is the lever.
- **Bottleneck items** (low impact, high risk) — secure supply through long-term contracts, dual sourcing, safety stock, or redesign to eliminate the dependency. Cost is secondary to availability.
- **Routine items** (low impact, low risk) — minimize transaction cost with catalogues, p-cards, e-procurement, consignment stock. Stop wasting management time on them.

Kraljic is the first tool to reach for when someone asks "how should we manage our suppliers?" or "we have 8,000 suppliers, where do we focus?" The segmentation itself is the diagnostic.

## ABC and XYZ Analysis — Inventory Segmentation

**ABC analysis** applies Pareto logic to inventory value: roughly 20% of SKUs typically account for 70–80% of value (A items), the next 30% for ~15–20% (B items), and the bottom 50% for the last 5–10% (C items). Different control policies are justified for each tier: tight count accuracy, cycle counts, and optimized safety stock for A items; lighter controls for C items.

**XYZ analysis** segments by demand variability, typically measured as coefficient of variation (CV = σ/μ) of demand: X items have stable, predictable demand (low CV); Y items have moderate variability or clear seasonality; Z items are lumpy, sporadic, or intermittent (high CV). The combination — a 3×3 ABC/XYZ matrix — dictates forecasting and stocking approaches. AX items deserve sophisticated forecasting and tight stock control; CZ items should probably be made to order or not carried at all.

## EOQ — Economic Order Quantity

The classic Wilson formula finds the order quantity that minimizes the sum of ordering cost and inventory holding cost under constant demand:

```
Q* = sqrt( (2 · D · S) / H )
```

Where D is annual demand (units), S is the fixed cost per order, and H is the annual holding cost per unit. The total relevant cost at Q* is sqrt(2·D·S·H). The formula is insensitive to small errors — being 20% off on Q* raises cost by only about 2%, which is why EOQ remains useful despite its restrictive assumptions (constant demand, instant replenishment, no stockout cost, no discounts).

Useful extensions: **EOQ with quantity discounts** (check each price break's EOQ and total cost), **production order quantity** (EPQ, for finite production rate), **EOQ with planned shortages** (when backorder cost is bounded and known). EOQ is a first approximation, not a final answer — use it to challenge intuitive order sizes, not to override judgment about lead time variability or supplier minimum order quantities.

## Safety Stock and Reorder Point

Safety stock buffers against demand and supply uncertainty. The standard single-item formula assuming normally distributed demand during lead time:

```
SS = z · σ_DLT
```

Where z is the service factor from the standard normal table (z = 1.65 for 95% cycle service level, z = 2.33 for 99%), and σ_DLT is the standard deviation of demand during lead time. When only demand variability matters (stable lead time), σ_DLT = σ_D · sqrt(LT). When both demand and lead time vary independently:

```
σ_DLT = sqrt( LT · σ_D² + D_avg² · σ_LT² )
```

Reorder point is then:

```
ROP = D_avg_LT + SS
```

Cycle service level (probability of no stockout in a cycle) is the most common target, but fill rate (fraction of demand satisfied from stock) is often what the business actually cares about — the two are related but not identical, and fill rate requires a more careful formulation involving the standard loss function.

Two common mistakes worth naming when advising: applying z-factors to variance-of-cycle-stock rather than variance-of-demand-during-lead-time, and assuming normality when the demand distribution is clearly skewed or intermittent (in which case Poisson, negative binomial, or simulation-based approaches are more appropriate).

## Bullwhip Effect

The bullwhip effect is the progressive amplification of demand variability moving upstream from consumer to raw material: supermarket demand varies 5%, distributor orders vary 15%, manufacturer orders vary 40%, component supplier orders vary 100%+. Lee, Padmanabhan, and Whang identified four operational causes: **demand signal processing** (each stage forecasts from its own orders and over-reacts to noise), **order batching** (stages order in batches, compressing demand signal into lumpy orders), **price fluctuation** (forward buying on discounts), and **rationing and shortage gaming** (when supply is short, buyers order more than they need to get their fair share of allocation).

Diagnosing bullwhip is straightforward once you know what to look for: compare the coefficient of variation of demand at each stage. If CV climbs as you move upstream, you have it. Remedies target the causes — share point-of-sale data upstream, reduce batch sizes through lower ordering cost (EDI, automated replenishment), flatten promotional pricing, and allocate based on historical demand rather than current orders during shortages. Vendor Managed Inventory (VMI) and Collaborative Planning, Forecasting, and Replenishment (CPFR) are structured responses.

## Lean, Agile, Leagile

**Lean** pursues waste elimination (muda — overproduction, waiting, transport, over-processing, inventory, motion, defects, underutilized talent) in service of reliable, low-cost flow. Its natural habitat is predictable, stable demand where variety is moderate. Tools: 5S, value stream mapping, kanban, SMED, poka-yoke, kaizen, heijunka. The Toyota Production System is the canonical example.

**Agile** prioritizes responsiveness to variety and volatility over cost efficiency. Its natural habitat is short-lifecycle, high-variety, demand-volatile products. Tools: postponement, modular design, rapid reconfiguration, late customization, high responsiveness from suppliers even at higher unit cost.

**Leagile** combines both: lean up to a decoupling point (where the order penetrates the supply chain — the furthest downstream point at which the product is held in generic form), then agile downstream of it. The canonical example is a paint retailer: base paints are made-to-stock lean; tinting to a specific customer color happens in-store, agile. Choosing the decoupling point is the central design decision.

When advising, match the approach to the demand pattern. Forcing lean on a highly variable fashion business produces missed seasons and markdown losses; forcing agile on a commodity business produces unnecessary cost.

## Theory of Constraints (TOC)

Goldratt's framework: the throughput of any system is determined by its bottleneck — the single most constrained resource. Therefore, improvement efforts that do not target the bottleneck produce little or no system-level benefit. The five focusing steps: **identify** the constraint, **exploit** it (get the most out of it without new investment), **subordinate** everything else to the constraint, **elevate** the constraint (invest to relax it), and then **repeat** — because a relaxed constraint shifts the bottleneck elsewhere.

Operationally, TOC gives rise to **drum-buffer-rope** scheduling (the bottleneck is the drum that sets pace; a buffer protects the drum from upstream disruption; the rope releases work into the system at the rate the drum can absorb). In distribution, TOC inspires pulled replenishment from a central buffer rather than pushed forecasts to each branch. TOC is particularly useful when someone is doing lots of local optimization that isn't moving system-level KPIs.

## Postponement and Mass Customization

Postponement delays the point at which a product takes its final form, allowing generic inventory to serve multiple end-SKUs. Forms include **form postponement** (a base module customized late — Benetton knitted greige sweaters and dyed them after seeing demand by color), **time postponement** (shipping only after order), and **place postponement** (centralizing inventory and distributing on demand rather than pre-positioning at many DCs).

Postponement reduces SKU-level forecast error (central limit theorem — aggregate forecasts are more accurate than disaggregated ones), reduces obsolescence risk, and enables mass customization. Its cost is usually higher unit cost for the late-stage operation and the engineering investment to redesign products for late differentiation. Make the case quantitatively: obsolescence reserve savings + stockout cost reduction vs. incremental unit cost and redesign cost.

## Porter's Five Forces (contextual use in procurement)

When analyzing a supply market rather than a competitive market, read Porter's Five Forces with the buyer as the "firm":

- **Buyer power** — how much concentration exists among buyers of this input; does the buyer have other options.
- **Supplier power** — how concentrated is supply; how differentiated; how high switching costs.
- **Threat of substitutes** — can a different input do the job.
- **Threat of new entrants** — is the supply market likely to attract new capacity.
- **Rivalry** — how aggressively do current suppliers compete.

High supplier power + limited substitutes + concentrated supply + barriers to entry = a bottleneck category in Kraljic terms, and a strategic issue for the buying firm.

## DMAIC and Six Sigma

DMAIC — **Define, Measure, Analyze, Improve, Control** — is the structured problem-solving loop of Six Sigma. It's useful whenever the problem is "our process performs inconsistently, find out why and fix it" and less useful when the problem is a fundamental design or strategy question. Tools commonly invoked at each stage: SIPOC diagrams and project charters (Define); measurement system analysis and process capability Cp/Cpk (Measure); root cause analysis via fishbone, 5-whys, and hypothesis tests (Analyze); design of experiments and pilot implementation (Improve); statistical process control charts and control plans (Control).

## FMEA — Failure Mode and Effects Analysis

FMEA is a structured risk assessment. For each process step or product feature, enumerate possible failure modes; for each, rate **Severity** of impact, **Occurrence** probability, and **Detection** difficulty (usually on 1-10 scales). Compute **RPN = S × O × D**; prioritize high-RPN items for mitigation. FMEA is particularly useful for supply chain risk assessment at the supplier or node level — map your supply network, identify failure modes (supplier insolvency, natural disaster, geopolitical disruption, quality failure), and attack the highest RPN items with dual sourcing, safety stock, or redesign.

## Cash-to-Cash Cycle Time and the Working Capital Lens

```
C2C = DSO + DIO - DPO
```

Days Sales Outstanding (how long to collect from customers) plus Days Inventory Outstanding (how long inventory sits) minus Days Payable Outstanding (how long you take to pay suppliers). Negative C2C — common in retail and some tech — means suppliers effectively finance the business. A supply chain strategy that improves service but extends C2C by 20 days has consumed working capital; always check.

## Network Design: Center of Gravity and MILP

For simple facility location with a single new node, the **center of gravity** method picks the point that minimizes weighted distance to demand points:

```
X* = Σ(wᵢ · xᵢ) / Σ(wᵢ)
Y* = Σ(wᵢ · yᵢ) / Σ(wᵢ)
```

Where (xᵢ, yᵢ) are demand coordinates and wᵢ are demand volumes. This ignores real road networks, fixed costs, capacity, and service requirements, but is a useful starting point.

Real network design uses **mixed-integer linear programming (MILP)**: binary variables for "open facility at candidate location k" and continuous variables for "flow from facility k to customer zone j," minimizing total fixed plus variable cost subject to capacity and demand-satisfaction constraints. Commercial tools (CPLEX, Gurobi, or domain-specific packages like Llamasoft/Coupa Supply Chain Modeler, AIMMS, AnyLogic) solve these at realistic scale. When the user asks about "should we open a new DC in Singapore" or "how many plants do we need in Europe," the underlying analysis is MILP — done properly, it answers "how many, where, serving whom, at what cost, under what scenarios."

## Forecasting methods — brief taxonomy

Match the method to the demand pattern, not the other way round.

- **Stable demand, no trend, no seasonality** — simple moving average, simple exponential smoothing.
- **Trending demand** — Holt's linear trend (double exponential smoothing).
- **Trending and seasonal demand** — Holt-Winters (triple exponential smoothing), SARIMA.
- **Causal factors dominate** — multiple regression with appropriate lags.
- **Intermittent / lumpy demand** — Croston's method, SBA (Syntetos-Boylan approximation), or TSB.
- **Short-lifecycle or new-product demand** — analog forecasting, Bass diffusion model.
- **Hierarchical demand (SKU × location × week, rolling up to brand × region × month)** — reconciled forecasts (bottom-up, top-down, or optimal reconciliation via MinT).
- **Machine learning approaches** (XGBoost, LightGBM, DeepAR, Temporal Fusion Transformers) — increasingly competitive, especially with rich feature sets (promotions, weather, holidays, price, web traffic), but require enough data and careful backtesting.

Forecast accuracy is measured with MAPE (Mean Absolute Percentage Error — easy to explain, breaks on low-volume series with near-zero actuals), MAE (Mean Absolute Error — same units as data, no percent weirdness), MASE (Mean Absolute Scaled Error — scale-free, preferred for cross-series comparison), and tracked alongside forecast bias (persistent over- or under-forecasting). Forecast accuracy alone is not the goal — the goal is decisions that use the forecast well, so pair accuracy metrics with inventory and service outcomes.

## Choosing a framework: a simple guide

- Someone asks **"how should we manage our 5,000 suppliers?"** → Kraljic.
- Someone asks **"why is our inventory so high?"** → ABC/XYZ segmentation + EOQ/safety stock review + bullwhip check.
- Someone asks **"our orders upstream swing more than our sales"** → Bullwhip diagnosis.
- Someone asks **"where should we locate our new warehouse?"** → Center of gravity first pass, MILP for real answer.
- Someone asks **"should we be lean or agile?"** → Leagile framing with decoupling point analysis.
- Someone asks **"our throughput is stuck despite investment in lots of places"** → Theory of Constraints.
- Someone asks **"we have a quality problem that keeps recurring"** → DMAIC.
- Someone asks **"our supply chain keeps getting disrupted"** → FMEA on the supply network plus risk mitigation portfolio.
- Someone asks **"our working capital is worse than peers"** → C2C decomposition.
- Someone asks **"our forecasts are terrible"** → Demand pattern classification first, then method selection — don't jump to "we need AI."

The framework is a lens, not an answer. The answer comes from applying the lens to the user's actual data and situation.
