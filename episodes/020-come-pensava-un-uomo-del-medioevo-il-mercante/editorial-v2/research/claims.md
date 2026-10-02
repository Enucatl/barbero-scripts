# Claim investigation — merchant episode

Research date: 2026-10-02. Research context assigned by coordinator: GPT-6 Astra / high; no separate runtime model-introspection facility used. Read the complete source, U-00001–U-00801, in four untruncated batches (lines 1–800, 801–1600, 1601–2400, 2401–3207), and the v2 skill plus evidence reference. The brief did not yet exist when research began; the coordinator subsequently supplied the twelve provisional chapter ranges. No audio was heard. No source, shared ledger, draft, or decision file was edited.

This report supplies provisional C IDs in first-appearance order. `resolved` means the evidence question has been investigated, not that every part of Barbero's formulation is confirmed or that correction is authorized. A source's account of an event establishes what that source says; it is not independent corroboration. Preserve Barbero's argument and source wording until consequential alternatives receive approval. Quotation recovery belongs to the separate quotation investigator.

Actual retrieval: opened Arnaldi's DBI biography, Vallone's Enciclopedia Dantesca biography, the three books of an 1860 Cronica transcription, a second complete chapter-numbered Cronica transcription, the Reti Medievali university anthology (including primary Ordinances and Villani extracts), Gualtieri's institutional-history article in French, D'Addario's Uberti entry, Fabbri's baptism study, and Boespflug's DBI Luca Fieschi biography. Inspected the relevant passages using full source pages and targeted open/find calls. Searches that only produced snippets were not promoted to evidence. The ideal Cappi critical edition was not retrieved. The 1860 transcription contains obvious OCR intrusions; use its relevant wording only where corroborated by the second transcription or the quotation investigator's edition. The final addendum records further opened sources for five audience-context references requested during research.

## Source records for coordinator deduplication

```yaml
- id: CSRC-001
  title: "COMPAGNI, Dino"
  author: "Girolamo Arnaldi"
  date: "1982"
  url: "https://www.treccani.it/enciclopedia/dino-compagni_(Dizionario-Biografico)/"
  edition: "Dizionario Biografico degli Italiani, volume 27"
  locator: "Opening biography paragraphs; paragraphs on withdrawal and immunity; discussion of Cronica composition and political viewpoint"
  accessed: "2026-10-02"
  evidence_type: "scholarly biography with documentary and bibliographic references"
  limitations: "Secondary synthesis; cited archival records not independently inspected. Birth dating differs across reference works. Do not reproduce the entry's apparent five-children/six-names inconsistency."
- id: CSRC-002
  title: "Cronaca fiorentina: Libro I"
  author: "Dino Compagni"
  date: "1310–1312, approximately"
  url: "https://it.wikisource.org/wiki/Cronica_delle_cose_occorrenti_ne%27_tempi_suoi/Cronaca_di_Dino_Compagni/Libro_I"
  edition: "M. Guigoni, Milan/Turin, 1860, with prefatory discourse by Atto Vannucci; Wikisource transcription"
  locator: "Book I; passages identified by chapter numbers in CSRC-005"
  accessed: "2026-10-02"
  evidence_type: "primary narrative, retrospective and partisan"
  limitations: "Public-domain original. Transcription marked complete but not proofread; OCR errors, no modern chapter division, not the Cappi critical edition."
- id: CSRC-003
  title: "Cronaca fiorentina: Libro II"
  author: "Dino Compagni"
  date: "1310–1312, approximately"
  url: "https://it.wikisource.org/wiki/Cronica_delle_cose_occorrenti_ne%27_tempi_suoi/Cronaca_di_Dino_Compagni/Libro_II"
  edition: "M. Guigoni, Milan/Turin, 1860; Wikisource transcription"
  locator: "Book II; chapter correspondence in CSRC-005"
  accessed: "2026-10-02"
  evidence_type: "primary narrative, retrospective and partisan"
  limitations: "Same edition/transcription cautions as CSRC-002; source testimony is not independent corroboration."
- id: CSRC-004
  title: "Cronaca fiorentina: Libro III"
  author: "Dino Compagni"
  date: "1310–1312, approximately"
  url: "https://it.wikisource.org/wiki/Cronica_delle_cose_occorrenti_ne%27_tempi_suoi/Cronaca_di_Dino_Compagni/Libro_III"
  edition: "M. Guigoni, Milan/Turin, 1860; Wikisource transcription"
  locator: "Book III; chapter correspondence in CSRC-005"
  accessed: "2026-10-02"
  evidence_type: "primary narrative, retrospective and partisan"
  limitations: "Same edition/transcription cautions; explicit OCR contamination near the Cavalcanti passage."
- id: CSRC-005
  title: "Cronica delle cose occorrenti ne' tempi suoi"
  author: "Dino Compagni"
  date: "1310–1312, approximately"
  url: "https://www.andreaconti.it/libri/Compagni-Cronica%20delle%20cose.html"
  edition: "Complete online transcription with Del Lungo chapter divisions/headings; underlying printed edition not established on opened page"
  locator: "Book.chapter notation used throughout this report"
  accessed: "2026-10-02"
  evidence_type: "primary text in a modern web transcription"
  limitations: "Private host, encoding blemishes, edition metadata uncertain. Chapter headings are editorial, not Compagni's own words. Relevant passages cross-checked with CSRC-002–004."
- id: CSRC-006
  title: "Antologia delle fonti bassomedievali, XV.5: Il caso di Firenze/3, Magnati e Popolani"
  author: "Stefano Gasparri, Andrea Di Salvo, Fiorella Simoni, editors; primary texts by Giovanni Villani, Dino Compagni, Comune di Firenze"
  date: "2002"
  url: "https://www.rm.unina.it/didattica/fonti/anto_bme/cap_XV/XV_5_stampa.htm"
  edition: "Reti Medievali teaching anthology"
  locator: "A: Villani VIII.79; B–D: Compagni I.4–5, I.10–11; E: Ordinamenti di Giustizia 1,5–6,8–9,12,22; F: Compagni I.20"
  accessed: "2026-10-02"
  evidence_type: "university-hosted primary-source anthology with scholarly introduction"
  limitations: "Selected extracts, some normalized/translated wording; not a complete statute edition. Distinguish primary extracts from the modern introductory synthesis."
- id: CSRC-007
  title: "Les pratiques institutionnelles de la République Florentine: Du regime del Popolo de 1282 à la réforme électorale de 1328"
  author: "Piero Gualtieri; French translation Yves Sintomer"
  date: "2014"
  url: "https://shs.cairn.info/revue-francaise-de-science-politique-2014-6-page-1109?lang=fr"
  edition: "Revue française de science politique 64/6, pp. 1109–1121; DOI 10.3917/rfsp.646.1109"
  locator: "Opening on 1328; sections on priorate and changing selection; notes 3,7,20,27"
  accessed: "2026-10-02"
  evidence_type: "peer-reviewed institutional-history research"
  limitations: "French HTML opened successfully; English HTML/PDF returned 403 on open. English search extraction was read but French opened article is the cited retrieval. Earlier positive sortition examples in note 27 concern replacements in 1324, not all councils in 1290."
- id: CSRC-008
  title: "Compagni, Dino"
  author: "Aldo Vallone"
  date: "1970"
  url: "https://www.treccani.it/enciclopedia/dino-compagni_(Enciclopedia-Dantesca)/"
  edition: "Enciclopedia Dantesca"
  locator: "Opening biography; priorates 1289 and 1301; gonfalonierate 1293; composition paragraph"
  accessed: "2026-10-02"
  evidence_type: "scholarly reference entry"
  limitations: "Older than Arnaldi; conflicting birth and early guild-membership dating. Use office chronology and explicit White affiliation, not its birth estimate as settled."
- id: CSRC-009
  title: "Uberti"
  author: "Arnaldo D'Addario"
  date: "1970"
  url: "https://www.treccani.it/enciclopedia/uberti_(Enciclopedia-Dantesca)/"
  edition: "Enciclopedia Dantesca"
  locator: "1266–1268 crisis and diaspora paragraphs; Lapo di Azzolino safe-conduct paragraph"
  accessed: "2026-10-02"
  evidence_type: "scholarly family history"
  limitations: "Dates the safe-conduct visit 1303, whereas Cronica III.4 places departure June 8, 1304. Some family remained in Florence; a single exile date for every Uberti is misleading."
- id: CSRC-010
  title: "Una città, un fonte: il Battistero di Firenze e i suoi registri"
  author: "Lorenzo Fabbri"
  date: "2014"
  url: "https://battesimi.duomo.firenze.it/api/assets/Registri%20battesimi.pdf"
  edition: "Mucchi, September 2014; excerpt hosted by Opera di Santa Maria del Fiore"
  locator: "Printed pp. 17–18, PDF pages 2–3; especially p.18 opening on the single urban/suburban font"
  accessed: "2026-10-02"
  evidence_type: "archival scholarship hosted by the custodian institution"
  limitations: "The single-font norm is not proof that literally every resident, including migrants and emergency baptisms, was baptized there."
- id: CSRC-011
  title: "FIESCHI, Luca"
  author: "Thérèse Boespflug"
  date: "1997"
  url: "https://www.treccani.it/enciclopedia/luca-fieschi_(Dizionario-Biografico)/"
  edition: "Dizionario Biografico degli Italiani, volume 47"
  locator: "Henry VII itinerary paragraphs: March 1312 voyage, Rome coronation, forty-day Florence siege, death August 24, 1313"
  accessed: "2026-10-02"
  evidence_type: "scholarly biography with documentary references"
  limitations: "Supports Henry's actions and failure to take Florence; not evidence for Compagni's personal response."
```

## Provisional claim records

```yaml
- id: C-001
  transcript: ["U-00004–U-00022"]
  claim: "Dino Compagni was a Florentine merchant and political participant, contemporary with Dante, whose short chronicle recounts his city's conflicts."
  centrality: central
  supporting_sources: [CSRC-001, CSRC-008, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "Confirmed in substance; office chronology in CSRC-008, self-identification in Cronica I.8. Do not introduce a precise birth year: reference works disagree."
- id: C-002
  transcript: ["U-00024–U-00032", "U-00254", "U-00766"]
  claim: "Compagni belonged to Por Santa Maria, ran a wealthy import-export cloth business, and imported cloth from France."
  centrality: supporting
  supporting_sources: [CSRC-001]
  conflicting_sources: []
  status: deferred
  research_note: "Membership and exporting documented; specific French imports and scale not independently established. Preserve lecture pending any proposal; avoid embellishing him into a major international magnate."
- id: C-003
  transcript: ["U-00033–U-00046", "U-00753–U-00766"]
  claim: "Political defeat ended Dino's public career, but he remained in Florence and continued business."
  centrality: central
  supporting_sources: [CSRC-001, CSRC-008]
  conflicting_sources: []
  status: resolved
  research_note: "Business after 1301 and withdrawal supported. The later explanation of why he escaped exile requires C-040/C-049."
- id: C-004
  transcript: ["U-00048–U-00051"]
  claim: "Dino knew little or no Latin and wrote in the Tuscan vernacular."
  centrality: supporting
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-001]
  status: deferred
  research_note: "Vernacular text confirmed. Latin proficiency unknown; Arnaldi infers substantial rhetorical education. His merchant status does not establish ignorance. Keep the source's own 'or little' hedge; do not strengthen to categorical illiteracy."
- id: C-005
  transcript: ["U-00070–U-00075", "U-00574–U-00577", "U-00638–U-00639"]
  claim: "Dino's chronicle presents a defeated participant's viewpoint, requiring caution about his moral judgments."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "Supported by proem, I.1–2, II.1, II.5, III.42. Preserve Barbero's explicit caveats: they prevent self-presentation being mistaken for neutral history."
- id: C-006
  transcript: ["U-00081–U-00105", "U-00136–U-00144", "U-00160–U-00168"]
  claim: "Noble knights long dominated communal life and retained prestige among merchants, despite political conflict."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "I.20 funeral precedence and I.11 anti-magnate legislation support status conflict. I.5 and I.20 show wealthy merchants intermarrying with nobles and merchant families becoming knights. Treat as an analytical contrast, not sealed hereditary classes or a claim that no merchant had governed before Dino."
- id: C-007
  transcript: ["U-00108–U-00117"]
  claim: "At a funeral Dino attended for a Frescobaldi woman, common citizens sat on mats while knights and legal doctors sat on benches."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: [CSRC-002, CSRC-005]
  status: resolved
  research_note: "I.20 confirms seating convention and a funeral in the Frescobaldi piazza. It does not identify the dead woman's kin or put Dino personally there. Few household furnishings is Barbero's contextual explanation, not demonstrated by this passage."
- id: C-008
  transcript: ["U-00119–U-00123"]
  claim: "Returning political exiles received compensation, knights more than others."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: [CSRC-002, CSRC-005]
  status: resolved
  research_note: "I.3 gives allowances to people still assigned to confino, including Uberti, after the cardinal's peace. Knight/commoner differential is confirmed; regret, recall, and retrospective wrongful-exile damages are not what the passage says."
- id: C-009
  transcript: ["U-00124–U-00135", "U-00235–U-00240", "U-00342–U-00348"]
  claim: "Knights were indispensable in diplomacy and warfare; merchants lacked military skills, remained home, and did not determine battles."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "I.10 supports distinction between professional military leadership and priors, but explicitly records mounted popolani and active infantry; II.7 names citizen-popolo envoys. I.27's merchant-cowardice judgment is attributed speech. Preserve the ethos argument; absolute military/diplomatic exclusion is overbroad."
- id: C-010
  transcript: ["U-00141", "U-00418–U-00432", "U-00451"]
  claim: "Communal Florence was democratic and all citizens could participate or hold office."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: [CSRC-007]
  status: resolved
  research_note: "The lecture itself excludes employees at U-00309. Councils and guild consultation existed, but citizenship, sex, guild, magnate and factional qualifications constrained participation. 'All' is rhetorical, not universal suffrage; democratic is an interpretive analogy."
- id: C-011
  transcript: ["U-00145–U-00157"]
  claim: "Florence defeated Arezzo at Campaldino in 1289; Dante fought mounted; new knights were made before the battle."
  centrality: supporting
  supporting_sources: [CSRC-005, CSRC-001]
  conflicting_sources: []
  status: resolved
  research_note: "Cronica I.10 confirms battle and new knights; Arnaldi locates Dante at Campaldino, June 11, 1289. The chronicle does not begin at this battle: I.2–4 precede it. Sword-on-shoulder ceremony and exact morning/afternoon schedule not verified here."
- id: C-012
  transcript: ["U-00178–U-00186"]
  claim: "Bishops were all nobles; Guglielmino degli Ubertini was a warrior bishop who died at Campaldino."
  centrality: sampled-incidental
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: deferred
  research_note: "I.6 and I.10 support the individual warrior-bishop and death. They call him of the Pazzi, a kinship issue handled by quotation research. No episcopate-wide evidence retrieved for 'all'; do not promote that generalization into a proven universal."
- id: C-013
  transcript: ["U-00187–U-00195"]
  claim: "Noble power ran through extended families with surnames, whereas most Florentines used patronymics."
  centrality: supporting
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: deferred
  research_note: "Consorterie and naming patterns visible throughout I.20–22. No population-level naming study retrieved; 'most' lacks a denominator. The mafia analogy is Barbero's illustration, not a historical identity."
- id: C-014
  transcript: ["U-00197–U-00205"]
  claim: "The Cavalcanti alone could mobilize about sixty armed family members."
  centrality: sampled-incidental
  supporting_sources: [CSRC-004, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "III.40 says about sixty men capable of bearing arms. It does not say all sixty were mounted armored knights; preserve the approximate number and distinguish illustrative staging."
- id: C-015
  transcript: ["U-00208–U-00231"]
  claim: "Arezzo's councillors contemplated killing their negotiating bishop; his kinsman Guglielmo de' Pazzi would welcome the result but would not consent in advance."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "I.8 supports the story and blood-kinship explanation. It is Compagni's narrative, not surviving council minutes or a verified verbatim transcript."
- id: C-016
  transcript: ["U-00240–U-00242"]
  claim: "Dino had no consequential family network and was a self-made political figure."
  centrality: central
  supporting_sources: [CSRC-001]
  conflicting_sources: [CSRC-001, CSRC-005]
  status: resolved
  research_note: "Limited family political weight supports individual ascent, not literal absence of relatives. Relatives were business partners; II.12 mentions his children. The lecture's 'never a relative' is rhetorical."
- id: C-017
  transcript: ["U-00244–U-00266"]
  claim: "Guelph and Ghibelline loyalties combined papal/imperial alignments with family enmities, patronage and economic dependence; Dino deplored faction."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-007]
  conflicting_sources: []
  status: resolved
  research_note: "I.2 supplies feud origin tradition and I.22 specific kinship, debt, friendship, and rivalry motives; Gualtieri note 5 gives wider alignments. No evidence establishes that Dino was wholly uninterested in faction or that ideology was always a pretext."
- id: C-018
  transcript: ["U-00267–U-00282"]
  claim: "The exiled Uberti returned briefly in a peace settlement after fifty years and supporters kissed their arms."
  centrality: supporting
  supporting_sources: [CSRC-004, CSRC-005, CSRC-009]
  conflicting_sources: [CSRC-005, CSRC-009]
  status: resolved
  research_note: "III.4 describes a White/Ghibelline delegation including Lapo di Azzolino; it leaves June 8, 1304. This is distinct from I.3's 1280 peace, which kept Uberti confined. Family diaspora developed in 1266–1268; fifty continuous years is unsupported. CSRC-009 itself calls visit 1303: record discrepancy, favor primary 1304 context, and propose 'decades' rather than false precision."
- id: C-019
  transcript: ["U-00287–U-00309"]
  claim: "The popolo organized to restrain noble violence; its government primarily represented guild employers and excluded their wage workers."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: []
  status: resolved
  research_note: "I.4–5 and Ordinances preamble support corporate political identity and stratification. Confindustria is an explicit modern analogy; avoid treating all guilds as only big-business associations, since artisanal and professional organizations mattered."
- id: C-020
  transcript: ["U-00299–U-00304"]
  claim: "Six guild-associated priors governed Florence."
  centrality: supporting
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: []
  status: resolved
  research_note: "I.4 and Villani VIII.79: three initially in June 1282, six by August, one per sesto. Six is correct for the period emphasized. Selection arrangements changed; do not imply every guild directly supplied one prior."
- id: C-021
  transcript: ["U-00311–U-00322", "U-00580–U-00588"]
  claim: "Numerous communal bodies rotated rapidly, with priors normally serving two months to check concentrated power."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006, CSRC-007]
  conflicting_sources: []
  status: resolved
  research_note: "I.4 and Villani VIII.79 confirm bimonthly terms. Treat the one-year maximum across every commission as generalization, not audited universal; terms and emergency arrangements varied."
- id: C-022
  transcript: ["U-00328–U-00333", "U-00341"]
  claim: "Dino opposed war with Arezzo while noble interests favored it, but war happened despite his vote."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "I.7 records opposition among popolani and I.8 a divided priorate, then unanimous acceptance of a negotiated castle transfer entrusted to Dino. No individual recorded antiwar vote is given. Pay and prestige are interpretive motives consistent with I.7, not an exhaustive causal account."
- id: C-023
  transcript: ["U-00334–U-00340"]
  claim: "Dino's warning that a day of war consumes years of peaceful earnings expresses his opposition to the Arezzo campaign."
  centrality: supporting
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "The words occur at II.1 in an apostrophe against destructive factional warfare, not the I.7–8 Arezzo deliberation. General economic-moral point valid, specific original context differs. Quote investigator owns wording."
- id: C-024
  transcript: ["U-00349–U-00361"]
  claim: "Factional judges and powerful lawbreakers undermined Florence's good laws."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "I.5, I.14, I.16 and III.37 provide Compagni's criticism. Narrate as his diagnosis; 'good laws alone would ensure prosperity' remains his political ideal, not demonstrated causation."
- id: C-025
  transcript: ["U-00365–U-00376"]
  claim: "Arezzo's nobles overthrew a popular government and starved its Lucchese leader in a cistern."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: []
  status: deferred
  research_note: "I.6 confirms confinement and death there. Starvation is not explicit; leader is called Priore, no modern identity or independent death evidence retrieved. Preserve as Dino's story and flag cause-of-death detail for any correction proposal."
- id: C-026
  transcript: ["U-00377–U-00392", "U-00603–U-00604"]
  claim: "The Ordinances of Justice excluded magnates from governing offices, imposed kin liability, and supplied armed enforcement and property destruction."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: []
  status: resolved
  research_note: "I.11–12 and Ordinances rubrics 5–6 support the core. Penalties depended on offense and procedure; mere accusation did not make every penalty automatic. 'All offices' exceeds the specifically named priorate, gonfalonierate and associated bodies in I.11. Keep magnate as a legal/political classification rather than simply every noble-born person."
- id: C-027
  transcript: ["U-00393–U-00394"]
  claim: "After the Ordinances, priors were shut in the Badia and given guards because of noble threats."
  centrality: supporting
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: [CSRC-005, CSRC-006]
  status: resolved
  research_note: "Chronology displaced: I.4 and Villani VIII.79 place guarded collective residence at priorate creation, 1282. Compagni says Torre della Castagna by the Badia, Villani the Badia's house. The detail supports fear and seclusion but not a new 1293 measure."
- id: C-028
  transcript: ["U-00397–U-00412"]
  claim: "A family containing a knight could be classified as magnate; nobles resented exclusion after Campaldino."
  centrality: supporting
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: []
  status: resolved
  research_note: "I.11 gives the criterion and I.13–14 grievances. It is Compagni's simplified account of a changing legal classification, not proof that every family in every later period was treated identically."
- id: C-029
  transcript: ["U-00417", "U-00421–U-00426"]
  claim: "Dino frequently became prior; councils were sometimes filled by drawing all citizens' names from a sack in late-thirteenth-century Florence."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-007, CSRC-008]
  status: resolved
  research_note: "Two documented priorates (1289,1301), plus 1293 gonfalonierate and other service. Gualtieri dates regular purse-and-scrutiny reform 1328; earlier positive lottery evidence concerns substitute priors in 1324. Cannot rule out every prior council's occasional lot, but no basis for all-citizen eligibility or this 1290s system."
- id: C-030
  transcript: ["U-00434–U-00450"]
  claim: "A deliberative assembly at San Giovanni chose the Casentino route to Arezzo by secret ballot despite its hazards."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "I.9 confirms commanders and governors debating and voting with secret balls; I.10 supplies successful result. It does not specify a whole day or beans rather than balls. Frame as council deliberation, not an open vote of every Florentine."
- id: C-031
  transcript: ["U-00442–U-00443", "U-00663"]
  claim: "San Giovanni was the assembly venue because Palazzo Vecchio did not yet exist; it is described as the cathedral."
  centrality: sampled-incidental
  supporting_sources: [CSRC-005, CSRC-010]
  conflicting_sources: [CSRC-010]
  status: resolved
  research_note: "I.9 identifies church of San Giovanni. Distinguish Baptistery from cathedral in English, consistent with U-00441 and U-00658; do not make the lecture's loose duomo wording relocate the meeting. Official palace search corroborated 1299 construction but page open failed, so not independent opened support here."
- id: C-032
  transcript: ["U-00457–U-00460"]
  claim: "Charles of Valois arrived as a papal peacemaker but assisted one faction."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: []
  status: resolved
  research_note: "II.2–9 and II.19–25 support commission and Black triumph. Papal peaceful intent is not neutral fact: II.2 alleges deliberate pro-Black purpose. Preserve lecture's early uncertainty and later revelation without adding unproved benevolent papal motivation."
- id: C-033
  transcript: ["U-00461–U-00476"]
  claim: "Bandino Falconieri wasted the short November day speaking; darkness ended public politics."
  centrality: supporting
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: [CSRC-003, CSRC-005]
  status: resolved
  research_note: "II.10 confirms half-day speech and short season. Universal nighttime shutdown contradicted by secret night council at II.25 and armed night activity. Public daylight constraints remain plausible; exact 5 p.m. cutoff is rhetorical, not a retrieved regulation."
- id: C-034
  transcript: ["U-00477–U-00489"]
  claim: "Rich citizens financed the commune and obtained influence or private advantages through their loans."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "II.24 gives a concrete 100-florin loan whose lender demands soldiers guard his home; II.6 and II.7 show money accelerating Charles's intervention. Supports mechanisms and incentives, not that every lender always lent willingly."
- id: C-035
  transcript: ["U-00490–U-00514", "U-00546"]
  claim: "After a crossbow attack Matteo d'Acquasparta refused 2,000 new florins Dino brought in silver; that was the spending limit without open voting."
  centrality: supporting
  supporting_sources: [CSRC-002, CSRC-005]
  conflicting_sources: [CSRC-002, CSRC-005]
  status: resolved
  research_note: "I.21 confirms amount, delivery and refusal; projectile lodged in a board, not explicitly a fabric window. Text says without public councils, not without any vote. U-00546's no-vote formula contradicts earlier secret-vote explanation. Coordinate translation and institutional threshold with quote investigator."
- id: C-036
  transcript: ["U-00515–U-00545", "U-00566–U-00578"]
  claim: "Officeholders profited from corruption, patronage and public money; opposition calls for accountability could be factional tactics."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "I.5, I.19 and III.2 support the indictment; III.2 specifically frames Corso's demand for accounts as a bid for power. This is Dino's diagnosis, not quantitative proof that nobody served public interests or every transaction was bought."
- id: C-037
  transcript: ["U-00547–U-00565"]
  claim: "Public funding knighted Rosso della Tosa's two sons, drawing taxes equivalent to poor spinning women's payments and provoking the name knights of the spinning wheel."
  centrality: supporting
  supporting_sources: [CSRC-004, CSRC-005]
  conflicting_sources: [CSRC-004, CSRC-005]
  status: resolved
  research_note: "III.38 identifies two sons PLUS Pinuccio, their relative; says the Party knighted them and money was taken from poor women spinning. No calculated equivalence or tax total is supplied. Avoid modern factory/industrial spinning-mill imagery for filatoio. Civic/party treasury distinction unresolved here."
- id: C-038
  transcript: ["U-00583–U-00595"]
  claim: "Pressure forced Dino and colleagues to consider replacing their government before the legal term ended."
  centrality: supporting
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "II.10–12 confirms premature replacement breached normal law and concession under pressure. Do not infer that the negotiated replacement actually assumed office; C-039."
- id: C-039
  transcript: ["U-00596–U-00634"]
  claim: "Dino formed a three-White/three-Black government plus a harmless seventh member; it briefly ruled and fell."
  centrality: central
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "II.12 confirms proposed names, weak seventh and Noffo Guidi's demand. It does not narrate their installation. Del Lungo heading says Black arrogance prevented execution. II.19 recounts the eventual imposed government. 'Fell immediately' can describe collapse of the compromise, not a verified term in office."
- id: C-040
  transcript: ["U-00638–U-00641", "U-00755–U-00760"]
  claim: "Dino belonged to neither faction and escaped exile because he was politically insignificant."
  centrality: central
  supporting_sources: []
  conflicting_sources: [CSRC-001, CSRC-008]
  status: resolved
  research_note: "White affiliation is explicit in both biographies. Arnaldi identifies former-prior immunity as protection, possibly aided by moderation. Desire for concord is not factional non-membership. Material factual departure needed if corrected."
- id: C-041
  transcript: ["U-00643–U-00672"]
  claim: "Dino appealed to common baptism and civic brotherhood at San Giovanni; emotional oaths failed."
  centrality: central
  supporting_sources: [CSRC-003, CSRC-005, CSRC-010]
  conflicting_sources: []
  status: resolved
  research_note: "II.8 confirms speech, oath and tears. Fabbri p.18 confirms single urban/suburban font tradition. 'Every Florentine' is a civic idealization; do not expand to every migrant or exception."
- id: C-042
  transcript: ["U-00673–U-00681"]
  claim: "Reason was an important medieval ideal, understood as God-given, despite irrational factional behavior."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: []
  status: deferred
  research_note: "II.8 explicitly links reason and common baptism; supports Dino's thought. No broad intellectual-history investigation performed across medieval people. Preserve as Barbero's interpretive generalization without adding a universal consensus."
- id: C-043
  transcript: ["U-00685–U-00703"]
  claim: "White leadership by newly wealthy Cerchi merchants contrasted with the old noble Donati leading the Blacks; merchant reluctance to fight favored Black victory."
  centrality: central
  supporting_sources: [CSRC-005, CSRC-006]
  conflicting_sources: [CSRC-005]
  status: resolved
  research_note: "I.20 and I.27 support social origins and attributed cowardice judgment. I.10 praises Vieri Cerchi's fighting; both factions contained nobles and merchants, I.22. Class ethos is Dino/Barbero's explanation, not exclusive faction membership or sufficient cause apart from papal/Charles intervention."
- id: C-044
  transcript: ["U-00704–U-00712"]
  claim: "Dino retrospectively blamed his government for pursuing peace when it should have armed."
  centrality: central
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "II.5 directly supports the missed-moment reflection. Preserve its reversal of the peace ideal and its retrospective voice."
- id: C-045
  transcript: ["U-00715–U-00727", "U-00736", "U-00743", "U-00748–U-00752"]
  claim: "Religion meant nothing in communal politics and survived chiefly as private faith or defeated politicians' consolation."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-005, CSRC-006]
  status: resolved
  research_note: "The oath-breaking and mocked procession support a moral claim about faith failing to restrain ambition. Literal secularization is disputed by the same narrative's papal commissions, oaths, sanctions and procession, plus the Ordinances' sacred preamble. Preserve Barbero's interpretation; narrowing its scope is a proposed intervention, not automatic correction."
- id: C-046
  transcript: ["U-00728–U-00735"]
  claim: "Dino feared responsibility for the damned souls who broke the peace oath he administered."
  centrality: central
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "II.8 supplies tears and conditional self-accountability, while blaming their malice. 'Not one kept it' exceeds the explicit number but expresses the lecture's force. Preserve religious remorse without suggesting source certainty about every soul."
- id: C-047
  transcript: ["U-00737–U-00747"]
  claim: "A holy friar urged a procession to avert disaster, but many said sharpening weapons would help more."
  centrality: supporting
  supporting_sources: [CSRC-003, CSRC-005]
  conflicting_sources: []
  status: resolved
  research_note: "II.14 names friar Benedetto and the ridicule. 'Many mocked' is not evidence that almost nobody believed in religion; distinguish loss of confidence in the remedy from unbelief."
- id: C-048
  transcript: ["U-00753–U-00765"]
  claim: "Black victory ended the ordinary merchants' political experiment and restored noble power allied with the richest merchants."
  centrality: central
  supporting_sources: [CSRC-005]
  conflicting_sources: [CSRC-005, CSRC-007]
  status: resolved
  research_note: "III.2 and III.37 support capture by faction chiefs and popolo grasso allies. Priors and guild constitutional framework persisted; not a legal abolition of merchant participation. This is a claim about effective power and Dino's defeat."
- id: C-049
  transcript: ["U-00756–U-00757"]
  claim: "White defeat led to mass banishment, including Dante."
  centrality: supporting
  supporting_sources: [CSRC-003, CSRC-005, CSRC-008]
  conflicting_sources: []
  status: resolved
  research_note: "II.25 lists Dante among the condemned. Distinguish November 1301 takeover from 1302 judgments. No need to add dates absent from spoken source."
- id: C-050
  transcript: ["U-00767–U-00784"]
  claim: "Dino hoped Henry VII would pacify Florence as God's agent; when he wrote he still awaited the intervention, which ultimately accomplished nothing."
  centrality: central
  supporting_sources: [CSRC-004, CSRC-005, CSRC-008, CSRC-011]
  conflicting_sources: [CSRC-011]
  status: resolved
  research_note: "III.23–36 and III.42 confirm imperial hopes. 'Nothing' is sound only as failure to deliver the hoped-for Florentine settlement: Henry reached Italy, was crowned and besieged Florence unsuccessfully before dying in 1313. The chronicle already narrates events through 1312; do not imply he had not yet entered Italy."
- id: C-051
  transcript: ["U-00785–U-00800"]
  claim: "Dino construed enemies' deaths as divine justice; one broke his knee, suffered medical treatment, and died."
  centrality: central
  supporting_sources: [CSRC-004, CSRC-005]
  conflicting_sources: []
  status: deferred
  research_note: "III.38 identifies Rosso, a dog causing the fall, an infistellito knee and painful death; III.39–40 continue providential deaths. Gangrene and a month of treatment not independently established. Preserve as reported moral narrative, not diagnosis or externally confirmed divine causation."
```

## Treatment-changing findings and exact alternatives

These are research proposals only. The default remains faithful contextual narration. Do not add fact-check interruptions merely because the dossier records an issue. Quotation substitutions, factual departures and substantive cuts require the coordinator's decision package under the v2 skill. All times below are cleaned-source times; original times are available alongside each utterance in the transcript.

1. **Factional identity and exemption (C-040, highest priority).** U-00640, 43:56: “uno di questi partiti non fa parte”; U-00755–758, 51:26–51:39: “Non è coinvolto nelle parti, lo lasciano stare … Dino no, è uno che non conta.” Evidence: CSRC-008 opening explicitly White; CSRC-001 paragraph on former-prior immunity. Options: preserve lecture literally; or replace the first assertion with **“He presents himself as a man trying to stand above the factions.”** Replace the exemption explanation with **“Dino supported the Whites too, but he escaped exile. A rule protecting former priors helped keep him safe. He remained in Florence, shut out of political life.”** This alters cause and identity and must not be silent.

2. **Lottery chronology and eligibility (C-029).** U-00421–426, 28:32–28:51: councils may choose anyone; every citizen's name goes in a sack; late 1200s. CSRC-007 opening and note 27 distinguish 1328 regular system from 1324 substitute selection. Options: retain as broad lecture shorthand; or **“There were councils and committees everywhere, drawing eligible citizens into public life. Political participation was remarkably broad for its time—though it certainly did not include everyone.”** This removes the unsupported sack mechanism for this period; do not replace it with “lotteries did not exist,” which exceeds evidence.

3. **Exile allowances (C-008).** U-00120–122, 07:18–07:27: government repents, recalls exiles and pays compensation. Cronica I.3 pays people still confined. Proposed minimal contextual replacement: **“Under one peace settlement, some citizens still had to remain in exile. The city paid them an allowance—but more to knights, less to everybody else.”** Retains the status punchline; changes circumstances.

4. **Uberti return (C-018).** U-00270–282, 17:51–18:34: general recall followed by expulsion after months, fifty years' exile. Cronica III.4 describes negotiators' short visit and withdrawal, not restored residence for all. Proposed replacement: **“During one attempt at peace, a delegation of exiles came back into Florence. Among them was an Uberti. Old Ghibellines, men and women, rushed to kiss the family's coat of arms. After decades in exile, that name still meant something. The peace talks failed, and the delegates left again.”** Avoid exact exile arithmetic or silently blending 1280 with 1304.

5. **Protective residence chronology (C-027).** U-00393, 26:26: “A partire da quel momento” attaches seclusion to Ordinances. Cronica I.4/Villani VIII.79 puts it in 1282. Minimal replacement: **“The priors already lived under guard near the Badia, protected from the threats of powerful families.”** Retains danger, avoids creating new 1293 institution. Choice of Badia versus Torre della Castagna should follow quotation-source reconciliation.

6. **Compromise government (C-039).** U-00629–634, 43:19–43:31 describes an installed balanced government falling immediately. II.12 supplies selection and failed negotiation; editor says implementation blocked. Minimal alternative: **“And this carefully balanced compromise? It collapsed almost immediately. The struggle began all over again.”** Retains joke and sequence without inventing tenure. Do not claim editor's heading is a quotation from Dino.

7. **Religion's causal scope (C-045).** U-00722–725, 49:12–49:19 and U-00748–752, 50:56–51:10: religion counts for nothing / is already outside politics. Same primary text contains ecclesiastical arbitration and binding sacred institutions. This is an interpretation, not a single mistaken fact. Preserve argument unless approved; a targeted alternative is **“Christian faith mattered deeply to them. But in this struggle for power, it did very little to restrain what people were willing to do.”** Later: **“And for Dino, after political defeat, faith became the hope that some justice still lay ahead.”** Does not impose a modern secularization lecture.

8. **Latin (C-004).** U-00048, 02:46 is categorical; U-00051, 03:04 adds “o lo sa poco.” At minimum carry the hedge into English rather than sharpening the claim. More consequential option: **“Dino writes in the language of his city, in Tuscan, rather than in Latin.”** This removes the unverified personal proficiency assertion while keeping vernacular contrast; requires approval as a cut.

9. **War participation and motive (C-009/C-022/C-023).** U-00333, 22:22 claims a recorded personal vote; I.8 gives divided views and a final unanimous negotiated decision. U-00336–337, 22:33–22:37 quote comes from II.1. Suggested bridge: **“Dino was among the priors trying to negotiate a settlement. Elsewhere in the chronicle, he puts the cost of war bluntly.”** Then quote as established by researcher. Keep noble prestige/profit argument attributed to lecture; do not amplify to all merchants being unarmed noncombatants.

10. **Knights of the spinning wheel (C-037).** U-00554–563, 38:04–38:52: two sons, calculated public tax equivalence, factory-like workers. III.38 also includes Pinuccio, says Party made them knights, and money came from poor women spinning. Proposed treatment: **“The party had Rosso's two sons knighted, along with a young relative, and showered them with money. Dino says that money came from poor women earning their living at the spinning wheel. So people called them ‘the knights of the spinning wheel.’”** This preserves the moral/economic sting and corrects the headcount/mechanism without modern factory imagery.

11. **Nighttime limit (C-033).** U-00473–475, 32:09–32:20 says all politics stops at dark. II.25 records a night council. Optional narrower rendering: **“And these were the shortest days of the year. While he talked, they were losing the daylight they needed to act.”** Keep time-pressure argument; avoid universal curfew or precise modern clock cutoff.

12. **Imperial disappointment (C-050).** U-00780–784, 53:11–53:30: emperor still coming; will do nothing. Proposed **“Dino is still waiting for Henry to bring that peace to Florence. It will never happen.”** This preserves disappointed hope while acknowledging no new factual outcome beyond failure. A siege-and-death excursus is unnecessary.

13. **Funeral frame (C-007).** U-00108–109, 06:18–06:20: “Once I was at a funeral … a woman of the Frescobaldi.” I.20 says a woman was buried in their piazza. Proposed **“Dino describes a funeral in the Frescobaldi piazza.”** Then keep seating hierarchy. Quotation researcher must control authoritative wording.

14. **Other sampled embellishments.** C-025 starvation (U-00375, 25:12), C-051 gangrene/month (U-00797, 54:16), C-035 fabric pane/no vote (U-00499, 34:02; U-00546, 37:36), and C-011 battle as chronicle's starting point (U-00145, 09:15) need no explanatory digressions. Options are to retain attributed lecture wording with limitations recorded or approve narrower event description. No independent medical, fiscal, or episcopal-universality finding was manufactured to resolve them.

## Scope and remaining limits

All major narrative and interpretive claims were considered across the complete source. Selected incidental checks include funeral seating, unequal exile allowances, Campaldino and Dante, the sixty Cavalcanti, the cistern, ballot medium, Baptistery, 2,000 florins, spinning-wheel knights, and Rosso's death. Not every rhetorical generalization was independently quantified. The main deferred areas are precise business trade/wealth, Latin proficiency, population-wide surnames, all bishops' birth status, starvation, broad medieval rationalism, and precise medical detail. These do not justify filling gaps with confident prose or removing the source's examples.

The minimum adequate evidence package is sufficient to draft a faithful contextual adaptation and a concrete decision set. The most consequential issues are Dino's White identity/exile exemption, election eligibility/chronology, and whether a balanced government actually took office. Religion, class structure and noble/merchant behavior require calibrated attribution and preservation of Barbero's explanatory argument. Sources disagree on some dates and modern headings; ledger notes deliberately retain those limits.

## Requested American-audience context addendum

These are first-use gloss proposals, not permission to cut the Italian references or substitute American analogies. Merge into existing C records as indicated; the coordinator can assign separate IDs in source order if desired.

| Source passage | Evidence and scope | Concise proposed first-use wording |
|---|---|---|
| U-00114–117, 06:47–06:52; C-007 | Cronica I.20 says dottori; CSRC-012 distinguishes the learned/academic and older legal senses from physician. Barbero himself specifies law graduates and judges. | “the knights and the doctors of law—the university-trained jurists” Then retain Barbero's university-professor prestige joke. Do not say physicians. |
| U-00269, 17:46; C-018 | CSRC-013, Inferno X summary, and CSRC-009 establish Farinata as the proud Ghibelline Uberti leader encountered among heretics. | “Farinata degli Uberti, the proud Ghibelline leader Dante meets in the Inferno.” A fuller flaming-tomb gloss is supported but unnecessary. |
| U-00297/301, 19:38/19:51; C-019 | CSRC-014 official organization description: business representation for manufacturing and services. | “Confindustria, Italy's industrial employers' association.” Preserve the name and analogy; don't translate it as a trade union or a state ministry. |
| U-00428–429, 28:58–29:02; C-010 | CSRC-015 documents 1968 direct-democracy aspirations and student movement; CSRC-016's archived 1977 assembly announcement and CSRC-017 establish another Italian student-protest wave. | “A veteran of Italy's student protests of 1968—or 1977—would have felt right at home.” Preserve both dates and assembly joke. They are distinct waves, not one organization persisting unchanged. |
| U-00611, 42:06; C-039 | CSRC-018 defines the Manuale Cencelli as allocation of posts among parties or factions according to political weight. | “The Cencelli manual—the Italian formula for dividing government jobs among rival factions—hadn't been invented yet. But the idea was already there.” This renders the joke; do not claim medieval officers used Cencelli's later document. |

```yaml
- id: CSRC-012
  title: "dottore"
  author: "Istituto della Enciclopedia Italiana"
  date: null
  url: "https://www.treccani.it/vocabolario/dottore/"
  edition: "Vocabolario online"
  locator: "Senses 1–3, especially older legal title and academic degree"
  accessed: "2026-10-02"
  evidence_type: "authoritative lexicography"
  limitations: "Lexical scope, not a prosopographical identification of funeral attendees."
- id: CSRC-013
  title: "Argomento del Canto X"
  author: "Società Dante Alighieri, digital Commedia editorial presentation"
  date: null
  url: "https://divinacommedia.dante.global/inferno/testo/r_inf10.htm"
  edition: "Digital Inferno, canto X summary"
  locator: "Opening account of Farinata rising from the tomb, exile dispute and prophecy"
  accessed: "2026-10-02"
  evidence_type: "specialist institutional presentation of a primary literary text"
  limitations: "Summary, not a historical biography or edition of contemporary political records."
- id: CSRC-014
  title: "Sistema Confindustria"
  author: "Confindustria"
  date: null
  url: "https://www.confindustria.it/sistema-confindustria"
  edition: "Official organization website"
  locator: "Opening description of manufacturing and services business representation"
  accessed: "2026-10-02"
  evidence_type: "primary institutional self-description"
  limitations: "Current organization; use stable functional gloss only, no current numerical membership claims."
- id: CSRC-015
  title: "Sessantotto"
  author: "Istituto della Enciclopedia Italiana"
  date: "2011"
  url: "https://www.treccani.it/enciclopedia/sessantotto_(Dizionario-di-Storia)/"
  edition: "Dizionario di Storia"
  locator: "Paragraphs on direct democracy and Italian student movement"
  accessed: "2026-10-02"
  evidence_type: "historical reference synthesis"
  limitations: "General overview, not evidence that every activist used identical assembly practices."
- id: CSRC-016
  title: "Il Cerchio di gesso: Il '77 nella biblioteca dell'Archiginnasio"
  author: "Biblioteca comunale dell'Archiginnasio, Bologna"
  date: null
  url: "https://www.archiginnasio.it/exhibition/cerchio-di-gesso/il-77-nella-biblioteca-dell-archiginnasio"
  edition: "Digital exhibition and archival catalogue"
  locator: "Assembly announcement of February 24, 1977 for March 1; BCABo Fondo speciale Volantini e manifesti movimenti politici e ambientalisti, b.1,1977"
  accessed: "2026-10-02"
  evidence_type: "custodian's catalogue of primary political ephemera"
  limitations: "Specific Bologna event supports assembly culture; does not define every strand of the 1977 movement."
- id: CSRC-017
  title: "Un giorno lungo un anno. 17 febbraio 1977"
  author: "Rai Cultura, Diario Civile"
  date: null
  url: "https://www.raicultura.it/storia/articoli/2019/01/Diario-Civile-69bd296d-9060-40da-aa98-3eafa37cc760.html"
  edition: "Public-broadcaster history programme webpage"
  locator: "Opening paragraphs on university occupations and student protests"
  accessed: "2026-10-02"
  evidence_type: "institutional historical exposition"
  limitations: "Read webpage only; embedded programme not watched. Used only for broad first-use context."
- id: CSRC-018
  title: "cencellismo"
  author: "Istituto della Enciclopedia Italiana"
  date: "2018"
  url: "https://www.treccani.it/enciclopedia/cencellismo_(altro)/"
  edition: "Neologismi"
  locator: "Opening definition"
  accessed: "2026-10-02"
  evidence_type: "authoritative political lexicography"
  limitations: "Functional gloss only; no original manual or numerical allocation formula inspected."
```
