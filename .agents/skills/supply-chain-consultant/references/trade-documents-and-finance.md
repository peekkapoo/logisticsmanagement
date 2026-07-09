# Trade Documents and Trade Finance Reference

International trade is executed through documents. The physical shipment and the commercial payment travel on parallel tracks, connected by a set of standardized documents that evidence shipment, ownership, origin, and value. Understanding how these documents interact is essential for advising on export-import operations, resolving payment disputes, and structuring trade finance.

## The core shipping documents

### Commercial Invoice

The commercial invoice is the seller's bill to the buyer and the single most important document for customs valuation. It states the parties, goods description, HS code (recommended), quantity, unit price, total value, Incoterm with named place, currency, payment terms, and country of origin. Customs authorities use it as the starting point for duty calculation and for screening against declared values. Discrepancies between the invoice and other documents (packing list, Bill of Lading, LC) are the most common cause of delay in LC transactions.

### Packing List

The packing list details how goods are packed — number of cartons, pallets, or packages; gross and net weights; dimensions; marks and numbers. It supports physical customs inspection and cargo claims. It does not state price.

### Bill of Lading (B/L) — for sea freight

A Bill of Lading performs three functions simultaneously: it is a **receipt** from the carrier acknowledging goods received, it is **evidence of the contract of carriage**, and — critically — it is a **document of title**. A negotiable ("order") B/L can be endorsed and transferred, meaning whoever holds the original endorsed B/L is entitled to claim the cargo at destination. This property is what makes the B/L the anchor of traditional trade finance: a bank holding the B/L effectively controls the cargo.

Three variants matter:

- **Straight B/L** names a specific consignee and is not negotiable — only the named consignee can collect the cargo. Common for intra-company shipments and open-account trade with trusted counterparties.
- **Order B/L** ("to order of [party]") is negotiable by endorsement. Required for most LC transactions.
- **Bearer B/L** (rare today) is transferable by simple delivery of the document.

An **on-board** B/L ("shipped on board") is issued once goods are actually loaded onto the named vessel and is the form most LCs require. A **received-for-shipment** B/L is issued earlier and is usually not acceptable under an LC unless expressly permitted.

The **Sea Waybill** is a non-negotiable cousin of the B/L. It works like an air waybill — the named consignee can collect cargo on identification, no original needs to travel. Sea waybills are increasingly used where title transfer via documents is not required (intra-group, open account).

### Air Waybill (AWB)

The AWB is the air-freight analogue of a sea waybill: a receipt and evidence of contract of carriage, but **not a document of title**. Cargo is released to the named consignee on identification. The AWB bears a unique 11-digit number (three-digit airline prefix + eight-digit serial) that allows tracking across IATA systems. Because the AWB is non-negotiable, LCs for air shipments typically require the bank to be named as consignee, with the underlying buyer notified on the "also notify" line, so the bank retains control until payment.

### Certificate of Origin (COO)

A COO certifies the country in which the goods were produced. Two classes matter:

- **Non-preferential COO** establishes origin for general customs purposes (quota, anti-dumping, marking). Usually issued by chambers of commerce.
- **Preferential COO** certifies that the goods meet the rules of origin of a specific free trade agreement and qualify for reduced or zero duty. Common preferential COO forms include **Form A** (historic GSP), **Form E** (China–ASEAN FTA), **Form D** (ATIGA intra-ASEAN), **Form EUR.1** (EU FTAs), **Form A.TR** (EU-Turkey customs union), and USMCA's self-certification. For FTAs such as EVFTA, traders above a certain threshold self-certify under a **Registered Exporter (REX)** system instead of using a paper certificate.

Getting the right COO is often what determines whether a shipment moves at preferential duty or standard MFN rate. Rules of origin (wholly obtained, substantial transformation by change in tariff heading, regional value content percentage, specific process rule) must be met for the COO to be valid.

### Insurance Certificate or Policy

Evidences cargo insurance coverage. Required under CIF and CIP Incoterms and typically required by banks in LC transactions. Key fields: assured party, voyage, cover clauses (ICC A/B/C), insured value (typically 110% of CIF value), currency, and claims-settlement location.

### Other commonly required documents

Inspection certificates (SGS, Bureau Veritas, Intertek) for quality or pre-shipment verification; phytosanitary certificates for plant products; health certificates for food and animal products; fumigation certificates for wood packaging (ISPM 15 heat treatment stamp on pallets is effectively mandatory worldwide); dangerous goods declarations (IATA DGR for air, IMDG for sea); Certificate of Free Sale for regulated consumer products; weight certificates; and various import permits depending on the commodity and destination.

## Trade finance instruments

Trade finance exists to manage the fundamental risk asymmetry in cross-border trade: the seller wants payment before losing control of the goods; the buyer wants the goods before parting with money. The instruments below sit on a risk spectrum.

### Open account

The seller ships goods and invoices the buyer, with payment due by the agreed date (net 30, net 60, etc.). This is the simplest and cheapest structure, and now accounts for the majority of global trade by value. It works when the buyer is creditworthy and the relationship is established. Risk sits entirely with the seller, who may mitigate with **trade credit insurance** (e.g., Euler Hermes, Atradius, Coface, national ECAs).

### Cash in advance

The buyer pays before shipment. Risk sits entirely with the buyer. Used for small transactions, new relationships, custom manufacturing with high setup cost, or when the buyer's country has payment restrictions. Wire transfer (SWIFT MT103) is the typical mechanism.

### Documentary collection

The seller ships the goods and then hands the documents to its bank (the **remitting bank**), which forwards them to the buyer's bank (the **collecting bank**) with instructions. The collecting bank releases documents to the buyer only against payment or acceptance. Two variants:

- **Documents against Payment (D/P, sometimes "Cash against Documents")** — documents released when the buyer pays. The buyer cannot collect the cargo without first paying.
- **Documents against Acceptance (D/A)** — documents released when the buyer accepts a time draft (a bill of exchange promising payment at a future date). The buyer gets the goods on credit; the seller holds an accepted draft, which can be discounted.

Documentary collection is governed by **URC 522** (Uniform Rules for Collections, ICC). It is cheaper than an LC but the banks do not guarantee payment — they only handle documents per instructions. If the buyer refuses the documents, the seller is left with goods at a foreign port and must decide between reselling, reshipping, or abandoning.

### Letter of Credit (Documentary Credit)

An LC is an undertaking by a bank (the **issuing bank**, acting on the buyer/applicant's instructions) to pay the seller (the **beneficiary**) a stated amount against presentation of specified documents that comply strictly with the LC's terms, provided presentation is made within the stated period and at the stated place. LCs are governed by **UCP 600** (Uniform Customs and Practice for Documentary Credits, ICC), with **ISBP 821** as the document-examination companion standard.

Key roles in an LC transaction:

- **Applicant** (buyer) instructs the issuing bank.
- **Issuing bank** issues the LC and carries primary payment obligation.
- **Advising bank** in the seller's country authenticates the LC and passes it to the beneficiary; typically has no payment obligation.
- **Confirming bank** (if the LC is confirmed) adds its own undertaking to the issuing bank's — giving the beneficiary a payment obligor in its own country and jurisdiction. Confirmation is used when the issuing bank's or country's risk is a concern.
- **Nominated bank** is authorized to pay, accept, negotiate, or incur a deferred-payment undertaking.
- **Beneficiary** (seller) presents documents and receives payment if they comply.

LCs are categorized several ways. By payment timing: **sight LC** (payment on presentation of complying documents), **usance LC** (payment at a stated future date, e.g., 90 days after shipment date). By revocability: **irrevocable** (the default under UCP 600; cannot be amended or cancelled without all parties' consent) — revocable LCs effectively no longer exist in UCP 600. By availability: by payment, by acceptance, by deferred payment, or by negotiation. Specialized structures include **transferable LCs** (allowing an intermediary beneficiary to transfer the LC to actual suppliers), **back-to-back LCs** (a second LC opened against the security of an incoming LC), **standby LCs** (functionally similar to guarantees, governed by UCP 600 or by ISP98), and **revolving LCs** (automatically reinstated for repeat shipments).

The practical reality of LCs is **discrepancies**. Banks examine documents strictly; if the commercial invoice says "Model XJ-100" and the packing list says "Model XJ100," that is a discrepancy, and the issuing bank can refuse to pay. Industry data consistently shows the majority of first-presentation LC documents contain discrepancies. The remedies are to fix the documents and re-present within the LC validity, to request the applicant's waiver of the discrepancies (requires the applicant's cooperation), or to send the documents on an approval or collection basis.

Typical required LC documents: commercial invoice, packing list, full set of on-board negotiable Bills of Lading or a non-negotiable transport document as specified, Certificate of Origin, insurance policy (if CIP or CIF), inspection certificate, and beneficiary's signed declaration or draft as required.

### Bank Payment Obligation (BPO) and electronic instruments

BPO is a bank-to-bank payment obligation triggered by automated data matching rather than physical document examination, developed by SWIFT. Adoption has been slow. Broader **digital trade finance** initiatives — the MLETR (Model Law on Electronic Transferable Records), eBL platforms (essDOCS, Bolero, WaveBL, TradeLens until its closure), and various blockchain-based consortia — are gradually replacing paper but have not yet displaced it at scale.

### Supply chain finance / reverse factoring

A large buyer arranges with a finance provider (bank or fintech) to pay the buyer's suppliers early, at a discount pegged to the buyer's credit quality rather than the supplier's. The buyer then pays the finance provider on the original due date. This extends the buyer's days-payable-outstanding while giving the supplier faster, cheaper cash. Scrutiny has increased after failures such as Greensill; accounting treatment (trade payable vs. short-term debt) has become an audit-and-disclosure issue under IAS 1 amendments and SEC attention.

### Factoring and forfaiting

**Factoring** sells receivables (usually short-term, often open account) to a factor who advances cash against them and collects from the debtor. Can be with recourse (credit risk stays with seller) or without recourse (credit risk transfers). Governed commercially by the GRIF (General Rules for International Factoring) when cross-border.

**Forfaiting** purchases medium-to-long-term receivables (usually backed by promissory notes, bills of exchange, or deferred-payment LCs) at a discount, without recourse, from exporters of capital goods and large transactions. Allows the exporter to convert medium-term paper to cash.

## How the documents and finance interact: a concrete example

An exporter in Vietnam sells USD 500,000 of textiles to a buyer in Germany under CIF Hamburg, payment by irrevocable sight LC issued by the German buyer's bank and confirmed by a German bank the exporter's Vietnamese bank works with.

Sequence: the buyer applies for the LC, specifying required documents (commercial invoice in three originals, full set of 3/3 on-board ocean B/L issued to the order of the issuing bank blank endorsed and marked freight prepaid, packing list, EUR.1 or EVFTA origin statement since EVFTA applies, insurance policy for 110% CIF value under ICC (A), and beneficiary's certificate of fax notice to the buyer within two days of shipment). The LC is advised and confirmed to the exporter in Vietnam, who reviews it carefully against the sale contract and requests amendments if terms are wrong (e.g., if the LC demands a document the exporter cannot produce in the time allowed).

The exporter manufactures and ships, handing goods to the shipping line which issues an on-board B/L. The exporter collects all required documents, assembles the presentation, and delivers it to the confirming bank within the LC's presentation period (typically 21 days from shipment date, but check the LC). The confirming bank examines documents strictly per UCP 600 and ISBP 821 standards. If complying, the confirming bank pays the exporter immediately (sight basis) and sends documents to the issuing bank for reimbursement. The issuing bank examines, pays the confirming bank, and releases documents to the buyer on payment. The buyer uses the endorsed B/L to claim the cargo at Hamburg, and customs-clears using the invoice, packing list, B/L, and EVFTA origin statement (which, if valid, entitles the goods to the reduced EVFTA duty rate instead of the EU MFN rate).

This sequence illustrates why precise documentation matters and why every clause in the LC needs to be achievable: a mismatch between the shipping schedule and the LC's latest shipment date, or a typo in the consignee's name, can block a USD 500,000 payment.

## Common pitfalls to flag when advising

When a user asks about LC structuring, push them to check: the latest shipment date and the presentation period (are they achievable given production lead time?), the required documents (can the seller produce each one in the form specified?), the consignment terms (who is consignee on the B/L, who is notify?), whether partial shipments and transhipment are allowed, the currency and any currency controls in the applicant's country, and whether the issuing bank's standing justifies confirmation.

When a user reports a stuck shipment, trace the document flow: where does the chain break? A B/L not released usually means unpaid freight (freight-collect not paid) or a payment dispute; a shipment held at customs usually means a documentation or classification issue; a rejected LC presentation means discrepancies that can often be cured.

When advising on trade credit insurance or factoring, remember that these are commercial products with materially different terms between providers — specific advice on rates or buyers' credit limits should come from actual quotes, not from memory.
