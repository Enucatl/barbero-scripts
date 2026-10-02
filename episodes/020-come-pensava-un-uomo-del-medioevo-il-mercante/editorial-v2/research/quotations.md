# Quotation provenance: merchant episode

Researcher: quotation investigation subagent. Accessed 2026-10-02 UTC. Read the complete supplied Italian transcript U-00001–U-00801 in successive batches; final batch reread where tool display clipped. Read v2 SKILL.md and references/evidence.md. Source corrections remain coordinator-owned. After research, read the final approved brief and rechecked the treatment-sensitive corrected utterances (including U-00335, U-00450, U-00532, U-00546, U-00626, U-00640, U-00703, U-00765, U-00783, U-00787–88 and U-00794). Approved source transcript SHA-256: b0eb338b676cf8a61d4c0c3bdd562df362835e6c033ff72107271e025876c44b. The corrected source does not resolve the historical discrepancies listed below. No script wording has been changed or authorized here. IDs below are proposed in first-appearance order. Repeated instances of the same quotation are included under their initial ID where appropriate. Historical passages loosely attributed to Dino are included as paraphrases; illustrative speech has an exclusion inventory at the end.

## Retrieved sources and actual scope

```yaml
- id: QSRC-001
  title: "Cronica delle cose occorrenti ne' tempi suoi"
  author: Dino Compagni
  date: "early fourteenth century; electronic edition 2007"
  url: https://www.intratext.com/IXT/ITA1139/
  edition: "IntraText, from Liber Liber electronic transcription; credits identify Gino Luzzatto introduction and notes, Einaudi, Turin, 1968"
  locator: "Proemio; I.1–27; II.1–36; III.1–42; individual chapter URLs in each Q record"
  accessed: "2026-10-02"
  evidence_type: "Primary medieval narrative in electronic Italian transcription"
  limitations: "Not an autograph or new critical collation. Electronic text has visible transcription defects and historical dates that must not be silently adopted. Modern chapter summaries are editorial, not Compagni's words. Print edition attribution comes from site's credits, not independent inspection of the 1968 volume."
- id: QSRC-002
  title: "Cronica delle cose occorrenti ne' tempi suoi"
  author: "Dino Compagni; introductory essay by Atto Vannucci"
  date: "1860 edition"
  url: https://it.wikisource.org/wiki/Indice:Compagni_-_Cronica,_1860.djvu
  edition: "Milano: M. Guigoni, 1860; Wikisource transcription of scan"
  locator: "Proemio and three books; print pp. 27, 28–70, 71–118, 119–182"
  accessed: "2026-10-02"
  evidence_type: "Primary medieval text in nineteenth-century edition"
  limitations: "Index and Proemio/three book pages opened; selected corresponding passages consulted, especially book I. Wikisource labels transcription complete but not proofread. Not full facsimile collation. Spelling/readings differ from QSRC-001, and its I.4 contains an evident 1283/1282 inconsistency."
- id: QSRC-003
  title: "COMPAGNI, Dino"
  author: Girolamo Arnaldi
  date: "1982"
  url: https://www.treccani.it/enciclopedia/dino-compagni_(Dizionario-Biografico)/
  edition: "Dizionario Biografico degli Italiani, volume 27"
  locator: "Biographical entry; opening family and education paragraphs; political career and discussion of II.13"
  accessed: "2026-10-02"
  evidence_type: "Scholarly biographical interpretation"
  limitations: "Used for contextual caution, not to replace primary wording; no modern translated passages used."
```

All 106 IntraText chapter pages were retrieved and saved as parsed text under `quotation-sources/`; `retrieval.txt` lists their exact URLs. The whole retrieved corpus was searched for quotation vocabulary and variants. This is a full-corpus search, **not** a claim that every chapter was close-read. Chapters close-read in full for this report: Proemio; I.1–12, I.15, I.20–21, I.23–24, I.27; II.1, II.5, II.8–10, II.12–14, II.19–20, II.34; III.7–8, III.24, III.36–38, III.40–42. Relevant surrounding passages occur in saved pages and can be checked without another download. All translations below are fresh direct translations of the recovered medieval Italian. Ellipses marked `[…]` are deliberate excerpt boundaries, never unmarked joining of text.

Book/section locators refer to the numbered IntraText text. QSRC-002 has the corresponding text in continuous books. Preserve the edition difference: for instance, the opening has **ho cessato** in IntraText and **ho restato** in the 1860 Wikisource transcription. I.8 assigns treaty authority to **Dino Compagni** in IntraText, but **Dino di Giovanni** in the 1860 text. Do not quietly settle this unrelated variant by printing either name as established fact.

## Findings that can alter treatment

- **Funeral and exiles:** I.20 says a funeral in the *piazza dei Frescobaldi*, not that the dead woman was a Frescobaldi or that Dino attended. I.3 compensates people **remaining at confino**, not returning exiles. Keep lecture framing distinct from recovered words.
- **Noble complaints are two episodes:** the “dogs of the people” speech is Berto Frescobaldi in I.15; the Campaldino boast is unnamed grandees assaulting guild consuls in I.21. They cannot become one continuous historic speech.
- **Government did not take office:** II.12 records agreement/election of a mixed slate followed by Noffo Guidi's demand and the meeting's dissolution. II.19 gives the succeeding actual all-Black priorate. The lecture's “it does not last” risks inventing a period in office.
- **Treasury and spinning:** I.21 says *sanza i consigli palesi*, not literally “without an open vote,” and does not say no vote was required below 2,000. III.38 says the **Parte** knighted Rosso's two sons **and a young kinsman**, with money taken from poor women spinning. It supplies no equivalence calculation, “factories,” or exact tax total. Render *filatoio* as spinning wheel/apparatus, not industrial mill.
- **Quotation vs gloss:** III.42 says what is done one day is **criticized** the next, not necessarily undone. II.8 grieves over **many** damned souls and conditionally accepts blame; it does not say every oath-taker was damned, or straightforwardly “I should not have done it.” III.38 says a dog tripped Rosso, his knee developed a fistula, and he died in agony under treatment; “gangrene” and “a month” are not in this source.
- ** chronology:** the Uberti visit is a protected delegation in June 1304 (III.7), not the 1280 general settlement (I.3); the chronicle itself does not give “fifty years.” Henry's angel passage describes his early descent (III.24), but the chronicle continues through his presence in Rome (III.36): “waiting for him to arrive” must not become waiting for him to enter Italy.

The following quotation records provide evidence and proposed treatment, **not editorial permission**. `eligible` means that exact source wording could support an explicit recovered-quotation proposal. Default treatment remains the lecture's contextual rendering, with factual departures placed in the coordinator's decision package.

## Proposed quotes.yaml records

```yaml
- id: Q-001
  transcript: [U-00040, U-00574–U-00577, U-00643–U-00648]
  attribution: "Dino Compagni's account of his own political aims, paraphrased by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Ritrovandomi in detto consiglio io Dino Compagni, disideroso di unità e pace fra' cittadini"
  translation: "Finding myself, Dino Compagni, in that council, desiring unity and peace among the citizens"
  locator: "I.24 opening; https://www.intratext.com/IXT/ITA1139/_PP.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase of his self-presentation, as Barbero already cautions. The source supports desire for concord; claims that he had no party or no personal stakes are separate interpretive assertions, not established by this line."
- id: Q-002
  transcript: [U-00045–U-00047, U-00052–U-00055, U-00067–U-00068]
  attribution: "Dino Compagni, Proemio"
  quotation_kind: composite
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "Le ricordanze dell'antiche istorie lungamente ànno stimolata la mente mia di scrivere i pericolosi advenimenti non prosperevoli […] E io, scusandomi a me medesimo siccome insufficiente, credendo che altri scrivesse, ho cessato di scrivere molti anni"
  translation: "Memories of ancient histories have long prompted my mind to write of the dangerous and unhappy events […] And I, excusing myself to myself as unequal to the task, believing that others would write, refrained from writing for many years"
  locator: "Proemio first paragraph; https://www.intratext.com/IXT/ITA1139/_P1.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: preserve paraphrase around exact short fragment 'believing that others would write.' The narrator's Latin-literacy explanation is not in the Proemio. The source's insufficiency is a statement of authorial modesty, not proof of inability to read Latin. QSRC-002 reads 'ho restato'; do not conflate variants."
- id: Q-003
  transcript: [U-00107–U-00117]
  attribution: "Dino Compagni narrating a funeral"
  quotation_kind: paraphrase
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "Essendo molti cittadini un giorno, per seppellire una donna morta, alla piazza de' Frescobaldi, e essendo l'uso della terra a simili raunate i cittadini sedere basso in su stuoie di giunchi, e i cavalieri e dottori su alto sulle panche"
  translation: "One day many citizens were in the Frescobaldi square to bury a woman who had died, and since it was the city's custom at such gatherings for citizens to sit low down on rush mats and knights and doctors higher up on benches"
  locator: "I.20, funeral paragraph; https://www.intratext.com/IXT/ITA1139/_PL.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual rendering, or an exact seating excerpt if approved. Funeral attendance in first person and the woman's Frescobaldi kinship are lecture additions. 'Doctors' means learned degree holders here, not specifically modern medical doctors; Barbero's university aside remains his commentary. Source then narrates a Cerchi–Donati scare, not merely ceremonial seating."
- id: Q-004
  transcript: [U-00119–U-00122]
  attribution: "Dino Compagni on allowances to political confinees"
  quotation_kind: paraphrase
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "a quelli che sostenessono lo incarico de' confini, fusse dato dal Comune, per ristoro del suo esilio, alcuni danari il dì ma meno al non cavaliere che al cavaliere"
  translation: "those who bore the burden of confinement away from home were to receive from the commune, as compensation for their exile, some money each day, but less for a man who was not a knight than for a knight"
  locator: "I.3 final paragraph, 1280 settlement; https://www.intratext.com/IXT/ITA1139/_P4.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual rendering pending decision on framing. Differential payment is confirmed, but the lecture says recalled exiles received retrospective redress after an acknowledged mistake. Source instead says Uberti and others remained confined and received a daily allowance. A recovered substitution must not preserve that false setting."
- id: Q-005
  transcript: [U-00145–U-00157]
  attribution: "Dino Compagni on Campaldino, interspersed with Barbero's explanation of knighting"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "La battaglia fu molto aspra e dura: cavalieri novelli vi s'erano fatti dall'una parte e dall'altra. […] Molti quel dì, che erano stimati di grande prodeza, furono vili; e molti, di cui non si parlava, furono stimati."
  translation: "The battle was very fierce and hard: new knights had been made there on both sides. […] Many that day who had been considered very brave proved cowardly; and many of whom no one spoke won esteem."
  locator: "I.10 battle narrative; https://www.intratext.com/IXT/ITA1139/_PB.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase with source fragments. 'That morning', a shoulder-tap ceremony, afternoon combat, and the recruit's hypothetical determination to die rather than lose face are Barbero's explanatory additions. The source does not name Dante here; his service requires separate claim evidence."
- id: Q-006
  transcript: [U-00181–U-00186, U-00209]
  attribution: "Dino Compagni describing the bishop of Arezzo"
  quotation_kind: direct
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "sapea meglio gli ufici della guerra che della Chiesa"
  translation: "he knew the duties of war better than those of the Church"
  locator: "I.6; https://www.intratext.com/IXT/ITA1139/_P7.HTM; death separately I.10"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: short contextual quotation. Source calls him 'de' Pazi'; lecture names Guglielmino degli Ubertini. This genealogical discrepancy must not be silently imported into the quote. Source confirms the bishop's death in battle in I.10."
- id: Q-007
  transcript: [U-00188–U-00197]
  attribution: "Dino Compagni's descriptions of families and the Cavalcanti"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Ma i Cavalcanti, che era potente famiglia, e circa LX uomini erano da portare arme"
  translation: "But the Cavalcanti, who were a powerful family, with about sixty men capable of bearing arms"
  locator: "III.40 opening paragraph; https://www.intratext.com/IXT/ITA1139/_P2W.HTM; generic family usage also I.20"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: paraphrase. Preserve 'about' for source-accurate number; lecture rounds to sixty. Context is Cavalcanti hatred of faction chiefs and Pazzino's death, not an enumerated company of sixty armored horsemen marching together. Mafia analogy and invented patronymics at U-00194 belong to Barbero."
- id: Q-008
  transcript: [U-00208–U-00221]
  attribution: "Dino Compagni on the bishop's negotiations and Arezzo's response"
  quotation_kind: paraphrase
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "Il Vescovo d'Arezo in questo mezo pensò, che se consentisse al trattato, sarebbe traditore […] Gli Aretini, sdegnati per le parole sue, perché ogni loro disegno si rompeva, ordinavano di farlo uccidere"
  translation: "Meanwhile the bishop of Arezzo considered that, if he agreed to the treaty, he would be a traitor […] The Aretines, angered by his words because all their plans were being undone, were arranging to have him killed"
  locator: "I.8 final paragraph; https://www.intratext.com/IXT/ITA1139/_P9.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: contextual paraphrase, no invented council quotation treated as documentary words. Dino narrates a negotiation, then the bishop's scruple and appeal to his faction; lecture compresses this into an accomplished betrayal. The murder plan is thwarted, and he later dies at Campaldino."
- id: Q-009
  transcript: [U-00222–U-00231]
  attribution: "Guglielmo de' Pazzi, reported indirectly by Dino Compagni"
  quotation_kind: direct
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "messer Guglielmo de' Pazi, suo consorto, che era nel consiglio, disse che sarebbe stato molto contento l'avessono fatto, non l'avendo saputo; ma essendo richiesto, non lo consentirebbe, ché non volea esser micidiale del sangue suo"
  translation: "Messer Guglielmo de' Pazzi, his kinsman, who was on the council, said he would have been very pleased if they had done it without his knowing; but, since he was being asked, he would not consent, because he did not wish to be the murderer of his own blood"
  locator: "I.8 final paragraph; https://www.intratext.com/IXT/ITA1139/_P9.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: indirect speech matching Dino; preserve Barbero's modern first-person gloss U-00230–31 as explanation. Source is a chronicler's reported speech, not verbatim council minutes. 'Consorto' is a member of the kin group, not a spouse."
- id: Q-010
  transcript: [U-00253–U-00260]
  attribution: "Dino Compagni on Guelf and Ghibelline factions"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "le maladette parti de' Guelfi e Ghibellini"
  translation: "the accursed factions of Guelfs and Ghibellines"
  locator: "I.2 final sentence; https://www.intratext.com/IXT/ITA1139/_P3.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: exact short phrase embedded in commentary. 'Parti' means factions, not modern political parties. The claim that Dino cared nothing about factional allegiance is Barbero's interpretation, not the meaning of this adjective."
- id: Q-011
  transcript: [U-00270–U-00282]
  attribution: "Dino Compagni on the return of White/ Ghibelline representatives"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Quando quelli di Parte bianca vennono in Firenze, furon molto onorati dalla gente minuta. Molti antichi Ghibellini, uomini e femmine, baciavano l'arme degli Uberti"
  translation: "When those of the White faction came to Florence, they were greatly honored by the ordinary people. Many old Ghibellines, men and women, kissed the arms of the Uberti"
  locator: "III.7, delegation and reception paragraphs; https://www.intratext.com/IXT/ITA1139/_P1Z.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual paraphrase; 'arms' here is the heraldic device. Fourteen representatives came under safe conduct and left 8 June 1304; no general return or months-long residence is stated. Lapo degli Uberti is named. Fifty years of exile, horses and shields are not in this recovered sentence. Must not merge with cardinal Latino's 1280 peace in Q-004."
- id: Q-012
  transcript: [U-00323–U-00326]
  attribution: "Dino Compagni's account of public-interest government, generalized by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Le loro leggi in effetto furono, che avessono a guardare l'avere del Comune […] e che i piccoli e impotenti non fussono oppressati da' grandi e potenti. […] ma tosto si mutò"
  translation: "Their laws in substance required them to guard the commune's property […] and to ensure that the small and powerless were not oppressed by the great and powerful. […] But it soon changed"
  locator: "I.5; https://www.intratext.com/IXT/ITA1139/_P6.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: signalled paraphrase of an ideal. Dino explicitly blames officeholding wealthy popolani too; do not turn the source into a claim that all merchants were virtuous and only nobles corrupted government."
- id: Q-013
  transcript: [U-00328–U-00334]
  attribution: "Dino Compagni on the 1289 war and negotiations"
  quotation_kind: composite
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "I Guelfi fiorentini e potenti aveano gran voglia andare a oste ad Arezo: ma a molti altri, popolani, non parea […] né non voleano la guerra, considerando il male che di quella segue"
  translation: "The powerful Florentine Guelfs were very eager to campaign against Arezzo, but many others, popolani, disagreed […] nor did they want war, considering the harm that follows from it"
  locator: "I.7 opening https://www.intratext.com/IXT/ITA1139/_P8.HTM; I.8 first paragraph https://www.intratext.com/IXT/ITA1139/_P9.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: contextual composite paraphrase. I.8 names Dino as a prior but does not record his individual antiwar vote. Noble salaries are supported by I.7's 'gran soldo e provisione'; the fully developed economic motive and inner dialogue are the lecturer's interpretation."
- id: Q-014
  transcript: [U-00335–U-00337]
  attribution: "Dino Compagni's authorial apostrophe"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "più si consuma in un dì nella guerra, che molti anni non si guadagna in pace"
  translation: "more is consumed in one day of war than is earned in many years of peace"
  locator: "II.1 final sentence; https://www.intratext.com/IXT/ITA1139/_PT.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: short contextual quotation. It is an apostrophe to destructive citizens at the start of book II, not recorded speech during the Arezzo council. Translate 'consuma' broadly as consumed/destroyed/spent; the passage is not limited to a quantified public-budget calculation. U-00335 is now approved as 'Dino dice, ah, la guerra'; this is the lecturer's framing interjection, not part of the recovered source maxim."
- id: Q-015
  transcript: [U-00343–U-00348]
  attribution: "Dino Compagni's assumption about civilian priors and military command, interpreted by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Molto furono biasimati quelli due di tale andata, cioè de' Priori, perché non era loro uficio, ma di gentili uomini usi alla guerra."
  translation: "Those two priors were much criticized for going, because it was not their office, but that of gentlemen accustomed to war."
  locator: "I.10 final paragraph; https://www.intratext.com/IXT/ITA1139/_PB.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: interpretive paraphrase. This criticizes two priors' participation as officials; it does not mean no merchants ever fought. Same chapter explicitly mentions mounted popolani and Vieri de' Cerchi's prowess."
- id: Q-016
  transcript: [U-00350–U-00358]
  attribution: "Dino Compagni on laws and judges"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "I maladetti giudici cominciorono a interpretare quelle leggi […] lo distendevano in danno dello adversario; e impaurivano i rettori"
  translation: "The accursed judges began interpreting those laws […] they extended it to the harm of their opponent, and intimidated the magistrates"
  locator: "I.12 opening; https://www.intratext.com/IXT/ITA1139/_PD.HTM; general good-law ideal I.5"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: quote only 'the accursed judges', then contextual paraphrase. 'Those laws' are specifically the Ordinances of Justice, not an undifferentiated law code. Compagni also says many crimes were punished, complicating an absolute claim of total legal failure."
- id: Q-017
  transcript: [U-00365–U-00376]
  attribution: "Dino Compagni on Arezzo's popular regime"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "feciono uno della città di Lucca che si chiamava Priore, il quale condusse il popolo molto prosperevolmente, e i nobili constrignea a ubidire le leggi. I quali s'accordorono insieme, e ruppono il popolo; e lui presono e misono in una citerna, e quivi si morì."
  translation: "they appointed a man from Lucca called Priore, who led the people very successfully and forced the nobles to obey the laws. The nobles agreed among themselves and broke the people's regime; they seized him and put him in a cistern, and there he died."
  locator: "I.6 opening; https://www.intratext.com/IXT/ITA1139/_P7.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: paraphrase. Source supplies death in cistern but not the explicit mechanism starvation. 'Ruppono il popolo' means defeated/broke the organized popular regime. U-00372 self-correction Firenze→Arezzo is not a historical alternate setting."
- id: Q-018
  transcript: [U-00379–U-00392]
  attribution: "Ordinances of Justice as summarized by Dino and then Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "E fecesi leggi, che si chiamorono Ordini della Giustizia, contro a' potenti che facessono oltraggio a' popolani: e che l'uno consorto fusse tenuto per l'altro […] e che non potessono esser de' Signori, né Gonfaloniere di Giustizia, né de' loro collegi"
  translation: "Laws were made, called the Ordinances of Justice, against powerful men who committed outrages against popolani, with one kinsman held liable for another […] and they could not be among the Signori, or be Gonfalonier of Justice, or members of their associated councils"
  locator: "I.11; https://www.intratext.com/IXT/ITA1139/_PC.HTM; enforcement I.12"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: explanatory paraphrase, not a verbatim statute. This is a chronicler's account of law, not the original legislation. Source specifies offices and councils; 'no governmental role in any commission' is broader. Thousand armed foot soldiers and a standard are described immediately before excerpt; 'police' is the lecturer's functional analogy."
- id: Q-019
  transcript: [U-00393–U-00394]
  attribution: "Dino Compagni on the priors' protection, implicitly used by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "stettono rinchiusi nella torre della Castagna appresso alla Badia, acciò non temessono le minaccie de' potenti […] e furono loro dati sei famigli e sei berrovieri"
  translation: "they stayed shut inside the Torre della Castagna near the Badia, so that they need not fear the threats of the powerful […] and were given six attendants and six armed officers"
  locator: "I.4 final lines; https://www.intratext.com/IXT/ITA1139/_P5.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: contextual paraphrase with proposed factual correction if authorized. Placement belongs to creation of priorate in 1282, not a new consequence of 1293 Ordinances. Source says tower near Badia, not palace of the Badia."
- id: Q-020
  transcript: [U-00397–U-00405]
  attribution: "Dino Compagni's summary of classification as Grandi"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "diliberorono che qualunque famiglia avesse avuti cavalieri tra loro, tutti s'intendessono esser Grandi"
  translation: "they decreed that any family that had had knights among its members should all be considered Grandi"
  locator: "I.11; https://www.intratext.com/IXT/ITA1139/_PC.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: paraphrase of Dino's account, not an independently sufficient legal definition. 'If you've had a knight, you're not one of us' is Barbero's illustrative speech. The source has a gap where number of listed families would stand."
- id: Q-021
  transcript: [U-00408–U-00411]
  attribution: "Messer Berto Frescobaldi, reported by Dino Compagni"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "come i cani del popolo aveano tolti loro gli onori e gli ufici"
  translation: "how the dogs of the people had taken away their honors and offices"
  locator: "I.15 council in San Iacopo Oltrarno; https://www.intratext.com/IXT/ITA1139/_PG.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual rendering or clearly bounded source excerpt. Dino gives Berto's speech with an indirect opening; Barbero turns it into first person. Keep separate from next Campaldino boast, made by other nobles at another event."
- id: Q-022
  transcript: [U-00412]
  attribution: "Unnamed grandi attacking the guild consuls, as narrated by Dino Compagni"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Noi siamo quelli che demo la sconfitta in Campaldino; e voi ci avete rimossi degli ufici e onori della nostra città"
  translation: "We are the men who won the victory at Campaldino, and you have removed us from the offices and honors of our city"
  locator: "I.21, vigil of San Giovanni procession; https://www.intratext.com/IXT/ITA1139/_PM.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: source quotation kept distinct from Q-021. 'Dare la sconfitta' means inflict the defeat on the enemy, not suffer defeat. It is addressed to guild consuls during an assault, not said privately at the I.15 meeting."
- id: Q-023
  transcript: [U-00434–U-00450]
  attribution: "Dino Compagni on the route debate before Campaldino"
  quotation_kind: composite
  source_ids: [QSRC-001, QSRC-002]
  original_language: Italian
  original_text: "Dicitori vi furono assai; le pallottole segrete si dierono: vinsesi d'andare per Casentino. Ma con tutto fusse più dubbiosa e pericolosa via, il meglio ne seguì. […] ove, se avessono trovati i nimici, arebbono ricevuto assai danno: ma non volle Dio."
  translation: "There were many speakers; the secret ballots were cast: the decision was to go through the Casentino. But although it was a more uncertain and dangerous route, the best outcome followed. […] Had they encountered the enemy there, they would have suffered great harm; but God did not will it."
  locator: "I.9 first paragraph https://www.intratext.com/IXT/ITA1139/_PA.HTM; I.10 opening https://www.intratext.com/IXT/ITA1139/_PB.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: maintain discussion/paraphrase/quotation alternation. Source specifies captains and war governors, not all citizens; secret ball ballots, not explicitly white and black beans; and no all-day duration. Divine protection is present in the chronicle's I.10, but approved U-00450 reads only 'ci ha protetti'; do not add an explicit divine subject to the approved lecture source. No audio was checked here. Do not silently combine I.9 and I.10 into one exact source sentence."
- id: Q-024
  transcript: [U-00456–U-00460]
  attribution: "Dino Compagni on Charles of Valois, paraphrased by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Messer Carlo di Valos, signore di grande e disordinata spesa, convenne palesasse la sua rea intenzione"
  translation: "Messer Charles of Valois, a lord of great and uncontrolled expenditure, was obliged to reveal his evil intention"
  locator: "II.20; https://www.intratext.com/IXT/ITA1139/_P1C.HTM; arrival II.9"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: narrative paraphrase of distrust and subsequent conduct. 'We had to obey' and the council's invented question are lecture dramatisation. Do not quote them as Dino's actual words. Q-025 gives the specific meeting anecdote."
- id: Q-025
  transcript: [U-00461–U-00471]
  attribution: "Dino Compagni on Bandino Falconieri"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Bandino Falconieri, uomo vile […] Tenea la ringhiera impacciata mezo il dì; e eravamo ne' più bassi tempi dell'anno."
  translation: "Bandino Falconieri, a cowardly man […] kept the speaking platform occupied for half the day; and we were in the shortest days of the year."
  locator: "II.10 second body paragraph; https://www.intratext.com/IXT/ITA1139/_P12.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: preserve exact phrases around commentary. Ringhiera means the platform for public speaking, not a railing or balcony. Source attributes actual words to Bandino; 'nothing to say' is Barbero's gloss. November context is justified by surrounding events; the entire argument about evening shutdown and 5 p.m. is an inference, not this quotation."
- id: Q-026
  transcript: [U-00490–U-00500]
  attribution: "Dino Compagni on cardinal Matteo d'Acquasparta"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "si levò uno di non molto senno, il quale con uno balestro saettò uno quadrello alla finestra del vescovado (dove era il Cardinale), il quale si ficcò nell'asse"
  translation: "a man of little sense came forward and shot a crossbow bolt at the window of the bishop's residence, where the cardinal was staying; it lodged in the board"
  locator: "I.21 penultimate body paragraph; https://www.intratext.com/IXT/ITA1139/_PM.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual paraphrase with small quoted 'little sense'. Source says a board, not linen window covering, and immediate move across the Arno for safety. The narrative identifies the cardinal's peace as intended to weaken Cerchi and strengthen Donati; Barbero's general peacemaker frame omits this partisan assessment. Interdict is not stated in this retrieved paragraph."
- id: Q-027
  transcript: [U-00501–U-00510]
  attribution: "Dino Compagni describing and delivering the 2,000 florins"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "gli presentorono fiorini MM nuovi. E io gliel portai in una coppa d'ariento, e dissi: «Messere, non li disdegnate perché siano pochi, perché sanza i consigli palesi non si può dare più moneta»."
  translation: "they offered him two thousand new florins. I carried them to him in a silver cup and said, 'My lord, do not disdain them because they are few, since without the public councils we cannot give more money.'"
  locator: "I.21 final paragraph; https://www.intratext.com/IXT/ITA1139/_PM.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual rendering, or exact source speech with 'public councils'. 'Consigli palesi' should not be confidently translated as roll-call/open ballot; source does not spell out the lecturer's secret-vote mechanism. The fresh/new coins, amount, Dino's personal delivery and silver cup are confirmed."
- id: Q-028
  transcript: [U-00511–U-00513]
  attribution: "Cardinal Matteo d'Acquasparta's response, indirectly reported by Dino"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Rispose gli avea cari; e molto li guardò, e non li volle."
  translation: "He replied that he appreciated them; he looked at them at length, and would not take them."
  locator: "I.21 last sentence; https://www.intratext.com/IXT/ITA1139/_PM.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: source-style indirect response with pause before refusal. It does not establish why he refused or that he was generally incorruptible."
- id: Q-029
  transcript: [U-00516–U-00528]
  attribution: "Dino Compagni's diagnosis of private interest and competition for office"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "per gara d'ufici […] Se l'amico o il parente loro cadea nelle pene, procuravano con le signorie e con li uficiali a nascondere le loro colpe, acciò che rimanessono impuniti."
  translation: "through rivalry for offices […] If their friend or relative incurred a penalty, they worked with the authorities and officials to conceal their offenses, so they would remain unpunished."
  locator: "I.2 https://www.intratext.com/IXT/ITA1139/_P3.HTM; I.5 https://www.intratext.com/IXT/ITA1139/_P6.HTM; 'gara d'ufici' also I.20, II.8 and II.12"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: 'rivalry for office' as short recurring phrase, remainder paraphrase. Source supports patronage and corruption; precise priority order self/kin/party, frantic two-month profiteering and 'everything, including contracts, is bought and sold' are lecture synthesis, not this continuous historic quotation."
- id: Q-030
  transcript: [U-00529–U-00530]
  attribution: "Dino Compagni on daily criticism, paraphrased as reversal by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "E ciò che si fa l'uno dì, si biasima l'altro."
  translation: "And what is done one day is criticized the next."
  locator: "III.42 opening; https://www.intratext.com/IXT/ITA1139/_P2Y.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual lecture rendering pending proposed correction. 'Undone' is stronger than 'criticized'; no source support here for automatic cancellation of decisions. For an authoritative source quotation, only the recovered translation is eligible."
- id: Q-031
  transcript: [U-00531–U-00533]
  attribution: "Dino Compagni, conclusion of Cronica"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "il male per legge non si punisce; ma come il malfattore à degli amici, e può moneta spendere, così è liberato dal malificio fatto"
  translation: "wrongdoing goes unpunished by law; as soon as the wrongdoer has friends and money to spend, he is absolved of the offense he has committed"
  locator: "III.42 first paragraph; https://www.intratext.com/IXT/ITA1139/_P2Y.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: bounded quotation. 'Liberato' can be rendered 'gets off' for speech; it is freedom from liability for a crime, not a claim that crime itself becomes lawful. Approved U-00532 now has 'ha degli amici'; this ordinary recognition repair matches the source."
- id: Q-032
  transcript: [U-00540–U-00546]
  attribution: "Dino Compagni on theft from the communal treasury"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Né l'avere del Comune non guardavano, anzi trovavano modo come meglio il potessono rubare; e così della camera del Comune molta pecunia traevano, sotto protesto di meritare uomini l'avesson servito."
  translation: "They did not safeguard the commune's property; instead, they found ways to steal it more effectively, drawing large sums from the communal treasury under the pretext of rewarding men who had served it."
  locator: "I.5; https://www.intratext.com/IXT/ITA1139/_P6.HTM; the 2,000-florin reference is separately I.21"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: exact short theft phrase plus paraphrase. U-00546's 'no need to vote' is not in I.5 and is stronger than I.21's limit without public councils; do not join it to the source quotation. 'Meritare' here means reward."
- id: Q-033
  transcript: [U-00548–U-00564]
  attribution: "Dino Compagni on Rosso della Tosa's heirs; public nickname reported by Dino"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Lasciò due figliuoli, Simone e Gottifredi; che dalla Parte furono fatti cavalieri, e con loro un giovane loro parente, chiamato Pinuccio, e molti danari furono donati loro. E chiamavansi i cavalieri del filatoio; però che i danari, che si dierono loro, si toglievan alle povere femminelle che filavano a filatoio."
  translation: "He left two sons, Simone and Gottifredi, who were made knights by the Party, together with a young kinsman called Pinuccio, and they were given a great deal of money. They were called the knights of the spinning wheel, because the money given to them was taken from the poor women who spun at the wheel."
  locator: "III.38 third paragraph; https://www.intratext.com/IXT/ITA1139/_P2U.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: nickname as quotation, story as contextual paraphrase pending decisions. Party (Guelf Party) not simply commune; two sons plus Pinuccio; no comparative tax calculation. Source does not locate the women in factories or give hunger details. Recommended translation 'knights of the spinning wheel', avoiding 'mill knights'. Pinuccio may be omitted from an excerpt only without claiming exactly two men were knighted."
- id: Q-034
  transcript: [U-00566–U-00573]
  attribution: "Corso Donati's calls for accountability, as reported and interpreted by Dino Compagni"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "I poveri uomini sono tribolati e spogliati di loro sustanzie con le imposte e con le libbre, e alcuni se ne empiono le borse. Veggasi dove sì gran somma di moneta è ita, però che non se ne può esser tanta consumata nella guerra."
  translation: "Poor people are tormented and stripped of their property by taxes and assessments, while some people fill their purses. Let us see where such a great sum of money has gone, because so much cannot have been consumed in the war."
  locator: "II.34; https://www.intratext.com/IXT/ITA1139/_P1Q.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase of a named example. Dino explicitly says Corso sought to weaken rival Black leaders, and calls the appeal a pretext of justice/pity. Source's 1303 dispute is not identified as accounting for the 1289 Arezzo war; Barbero's U-00571 supplies Arezzo. Do not quote that identification as recovered."
- id: Q-035
  transcript: [U-00579–U-00601]
  attribution: "Dino Compagni on pressure to replace the priorate before its term expired"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "I signori erano molto stimolati da' maggiori cittadini, che facessono nuovi signori. Benché contro alla Legge della Giustizia fusse, perché non era il tempo da eleggerli, accordamoci di chiamarli, più per piatà della città che per altra cagione. […] eleggemo sei cittadini comuni, tre de' Neri e tre de' Bianchi."
  translation: "The leading citizens pressed the Signori hard to appoint new Signori. Although it was against the Law of Justice, because the time to elect them had not arrived, we agreed to appoint them, more out of compassion for the city than for any other reason. […] We elected six citizens acceptable to both sides, three Blacks and three Whites."
  locator: "II.12 opening; https://www.intratext.com/IXT/ITA1139/_P14.HTM; legal objection first II.10"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: paraphrase of proposed early replacement. 'Comuni' means a shared/balanced slate, not six politically unaffiliated men. Actual resignation and successor priorate occur later in II.19. No new mixed administration took office in this scene."
- id: Q-036
  transcript: [U-00602–U-00610]
  attribution: "Dino Compagni on the seventh officer in the proposed slate"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Il settimo, che dividere non si potea, eleggemo di sì poco valore, che niuno ne dubitava."
  translation: "For the seventh, who could not be divided, we chose a man of so little ability that no one feared him."
  locator: "II.12; https://www.intratext.com/IXT/ITA1139/_P14.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: short source quotation preserving the joke. 'Ne dubitava' here means feared/mistrusted him, not had no doubt he was incompetent. Gonfalonier's explanation is lecturer context supported by I.11."
- id: Q-037
  transcript: [U-00612–U-00622]
  attribution: "Noffo Guidi's request, indirectly reported by Dino"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "E Noffo Guidi parlò […] mi domandò, che mi piacesse far loro parte, nell'ufficio, maggiore che l'altra"
  translation: "And Noffo Guidi spoke […] he asked me to give their side a larger share of the offices than the other"
  locator: "II.12; https://www.intratext.com/IXT/ITA1139/_P14.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase; name recoverable even though lecturer withholds it. Source gives public speech at the meeting; being taken aside and addressed 'listen, Dino' are illustrative dramatisation, not recorded source dialogue."
- id: Q-038
  transcript: [U-00623–U-00626]
  attribution: "Dino Compagni's interpretation and response to Noffo Guidi"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "che tanto fu a dire, quanto «disfa' l'altra parte», e me porre nel luogo di Giuda. E io li risposi che innanzi io facessi tanto tradimento, dare' i miei figliuoli a mangiare a' cani."
  translation: "which was as much as to say, 'destroy the other side,' and put me in Judas's place. And I answered him that before I committed such a betrayal, I would give my children to the dogs to eat."
  locator: "II.12 last lines; https://www.intratext.com/IXT/ITA1139/_P14.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: keep Judas as Dino's interpretive gloss, then his reported reply. A natural exact proposal is 'Before I committed such a betrayal, I would feed my own children to the dogs.' That is a fresh direct translation. Approved U-00626 now reads 'a mangiare ai cani', matching this meaning. Earlier assertion that Dino never mentions relatives must allow this explicit reference to his children."
- id: Q-039
  transcript: [U-00627–U-00634]
  attribution: "Dino Compagni's narrative outcome, expanded by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "E così da collegio ci partimo."
  translation: "And so we left the meeting."
  locator: "II.12 final sentence https://www.intratext.com/IXT/ITA1139/_P14.HTM; actual replacement II.19 https://www.intratext.com/IXT/ITA1139/_P1B.HTM"
  verdict: unresolved
  source_replacement: unavailable
  status: deferred
  research_note: "Intended treatment: contextual rendering pending explicit narrative intervention. No passage confirms that this mixed government assumed office and rapidly fell; election/agreement failed in this meeting, and the actual succeeding priorate in II.19 was Black. Remaining problem is lecture-to-source mismatch, not missing retrieval. Do not mark 'briefly governed' confirmed or silently fix it in adaptation."
- id: Q-040
  transcript: [U-00649–U-00652]
  attribution: "Dino Compagni reporting his appeal in the Santa Trinita council"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Signori, perché volete voi confondere e disfare una così buona città? Contro a chi volete pugnare? contro a' vostri fratelli?"
  translation: "Gentlemen, why do you want to throw so fine a city into confusion and destroy it? Against whom do you want to fight? Against your own brothers?"
  locator: "I.24 opening; https://www.intratext.com/IXT/ITA1139/_PP.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: bounded speech excerpt. This is a different council from San Giovanni oath in II.8, which follows in the lecture. Do not merge the two addresses into one source speech."
- id: Q-041
  transcript: [U-00656–U-00670, U-00673–U-00675, U-00728–U-00729]
  attribution: "Dino Compagni reporting his San Giovanni address and oath"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Cari e valenti cittadini, i quali comunemente tutti prendesti il sacro baptesmo di questo fonte, la ragione vi sforza e strigne ad amarvi come cari frategli […] E sopra questo sacrato fonte, onde traesti il santo battesimo, giurate tra voi buona e perfetta pace, acciò che il signore che viene truovi i cittadini tutti uniti."
  translation: "Dear and worthy citizens, who all received holy baptism from this font, reason presses and binds you to love one another as dear brothers […] And over this sacred font, where you received holy baptism, swear among yourselves to a good and perfect peace, so that the lord who is coming may find all the citizens united."
  locator: "II.8 address; https://www.intratext.com/IXT/ITA1139/_P10.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual rendering with exact short baptism/reason excerpts if proposed. Narrator then says all agreed, touched the book and swore. 'Reason says we should agree' later U-00673–75 paraphrases this address and II.5, not a separate recovered maxim. Baptistery is not cathedral; U-00663's 'in cattedrale' is lecturer/transcript issue."
- id: Q-042
  transcript: [U-00666, U-00669–U-00672]
  attribution: "Dino Compagni on ostentatious tears and subsequent destruction"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "I malvagi cittadini, che di tenereza mostravano lagrime, e baciavano il libro, e che mostrarono più acceso animo, furono i principali alla distruzion della città."
  translation: "The wicked citizens who displayed tears of tenderness, kissed the book, and showed the greatest fervor became the chief agents in the city's destruction."
  locator: "II.8 after the oath; https://www.intratext.com/IXT/ITA1139/_P10.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: paraphrase; 'as soon as they left' is lecturer compression, not specified timing. 'Displayed tears' preserves Dino's judgment of performance. This is narrated commentary, not words spoken to the assembly."
- id: Q-043
  transcript: [U-00687–U-00691]
  attribution: "Dino Compagni on the Cerchi and Donati, interpreted by Barbero"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "i Cerchi (uomini di basso stato, ma buoni mercatanti e gran ricchi […]); […] i Donati, i quali erano più antichi di sangue, ma non sì ricchi"
  translation: "the Cerchi, men of low origin but good merchants and very rich […] the Donati, who were of older lineage but not so rich"
  locator: "I.20 opening; https://www.intratext.com/IXT/ITA1139/_PL.HTM; Corso 'Barone' II.20"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: paraphrase. 'Barone' is Corso's nickname in II.20, not proof that the entire Donati family held a baronial title. 'Like me/Dino' is lecturer analogy."
- id: Q-044
  transcript: [U-00692–U-00700]
  attribution: "Unnamed 'wise men', quoted by Dino Compagni"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Ma i savi uomini diceano: «E' sono mercatanti, e naturalmente sono vili; e i lor nimici sono maestri di guerra e crudeli uomini»."
  translation: "But the wise men said, 'They are merchants, and by nature they are timid; their enemies are masters of war and cruel men.'"
  locator: "I.27 middle paragraph; https://www.intratext.com/IXT/ITA1139/_PS.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: preserve nested attribution ('people who understood these things, Dino says'). 'Vili' may be 'cowardly' where force is desired; 'timid' conveys military irresolution. Do not present the generalization as an independently established fact about all merchants. Source also criticizes a knightly White commander who disliked war, complicating the lecturer's class contrast."
- id: Q-045
  transcript: [U-00704–U-00712]
  attribution: "Dino Compagni's retrospective criticism of his fellow priors and himself"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "E così perdemo il primo tempo, che non ardimo a chiudere le porti, né a cessare l'udienza a' cittadini […] Demo loro intendimento di trattare pace, quando convenìa arrotare i ferri."
  translation: "And so we lost the first opportunity, because we did not dare close the gates or stop receiving the citizens […] We led them to expect peace negotiations when we should have been sharpening our weapons."
  locator: "II.5; https://www.intratext.com/IXT/ITA1139/_PX.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: paraphrase around the exact weapons image. 'Ferri' means weapons; 'swords' is a reasonable contextual narrowing but not the only possible literal instrument. 'We failed because we were merchants' is lecture synthesis. Preserve distinction from identical weapons phrase attributed to mockers in II.13/Q-048."
- id: Q-046
  transcript: [U-00730–U-00735]
  attribution: "Dino Compagni reflecting on the broken oath"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Se nelle parole ebbe alcuna fraude, io ne debbo patire le pene; benché di buona intenzione ingiurioso merito non si debba ricevere. Di quel saramento molte lagrime ò sparte, pensando quante anime ne sono dannate per la loro malizia."
  translation: "If there was any deceit in those words, I must suffer the penalty for it, although good intentions should not earn an unjust reward. I have shed many tears over that oath, thinking how many souls are damned through their own wickedness."
  locator: "II.8 final paragraph; https://www.intratext.com/IXT/ITA1139/_P10.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual paraphrase with treatment-changing limits. Source does not say every signer was damned, none kept oath, or unequivocally 'I should never have made them swear.' He makes blame conditional and partly defends his good intentions. If exact replacement proposed, include that nuance rather than back-translating the lecturer's regret."
- id: Q-047
  transcript: [U-00736–U-00741]
  attribution: "Frate Benedetto's advice, reported by Dino Compagni"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Signori, voi venite in gran tribulazione, e la vostra città. Mandate a dire al vescovo facci fare processione, e imponeteli che la non vada oltrarno: e del pericolo cesserà gran parte."
  translation: "Gentlemen, you and your city face great tribulation. Send word to the bishop to hold a procession, and instruct him not to let it cross the Arno; much of the danger will then cease."
  locator: "II.13; https://www.intratext.com/IXT/ITA1139/_P15.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase, preserving unnamed holy friar if following lecture. Source names Benedetto, says he approached secretly and requested anonymity, and includes a strategic route restriction. The stated purpose of civic unity/invoking protection is contextual expansion, not his exact advice."
- id: Q-048
  transcript: [U-00744–U-00747]
  attribution: "Dino Compagni reporting other citizens' mockery"
  quotation_kind: direct
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "Seguitammo il suo consiglio; e molti ci schernirono, dicendo che meglio era arrotare i ferri."
  translation: "We followed his advice, and many mocked us, saying it would have been better to sharpen our weapons."
  locator: "II.13; https://www.intratext.com/IXT/ITA1139/_P15.HTM"
  verdict: confirmed
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: bounded quotation with attribution to mockers nested in Dino's narration. It does not establish that almost no one in Florence believed any longer. Source immediately continues with hard laws, execution apparatus, and enhanced military command, so government also attempted coercive action."
- id: Q-049
  transcript: [U-00767–U-00771, U-00785–U-00796, U-00798]
  attribution: "Dino Compagni's interpretation of divine justice, voiced by Barbero"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "molta pace dà a coloro nell'animo, che le ingiurie da' potenti ricevono, quando veggiono che Iddio se ne ricorda. […] quando egli à molto indugiato e sofferto! ma quando lo indugia, è per maggior punizione […] e de' loro errori furono puniti."
  translation: "It gives great peace of mind to those who suffer wrongs from the powerful when they see that God remembers them. […] after he has long delayed and endured! But when he delays, it is for greater punishment […] and they were punished for their wrongdoing."
  locator: "III.37 https://www.intratext.com/IXT/ITA1139/_P2T.HTM; III.41 https://www.intratext.com/IXT/ITA1139/_P2X.HTM"
  verdict: confirmed in substance
  source_replacement: not-applicable
  status: resolved
  research_note: "Intended treatment: clearly signalled paraphrase of his providential interpretation. 'God is there and sees' and retrospective 'we lost politically' are Barbero's illustrative inner monologue, not recovered sentences. Geri Spini is still alive in III.41; do not convert rhetorical 'one after another' into every enemy already dead."
- id: Q-050
  transcript: [U-00772–U-00783]
  attribution: "Dino Compagni on Henry VII's descent into Italy"
  quotation_kind: composite
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "venne giù, discendendo di terra in terra, mettendo pace come fusse uno agnolo di Dio, ricevendo la fedeltà fino presso a Milano"
  translation: "he came down from town to town, bringing peace as though he were an angel of God, receiving oaths of allegiance as far as the vicinity of Milan"
  locator: "III.24 final paragraph; https://www.intratext.com/IXT/ITA1139/_P2G.HTM; later career through III.36"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: exact angel fragment within contextual narrative. Preserve 'as though', not identification as an actual angel. Book III proceeds to Henry in Pisa/Rome; waiting for arrival cannot mean the entire Cronica was written before he entered Italy. The lecturer's surrender-of-self-government argument is interpretation, not source speech."
- id: Q-051
  transcript: [U-00797]
  attribution: "Dino Compagni on Rosso della Tosa's death"
  quotation_kind: paraphrase
  source_ids: [QSRC-001]
  original_language: Italian
  original_text: "uno dì andando, uno cane li si attraversò tra' piè e fecelo cadere, per modo si ruppe il ginocchio: il quale infistellì; e martoriandolo i medici, di spasimo si morì"
  translation: "one day as he walked, a dog crossed between his feet and made him fall, breaking his knee; a fistula developed, and as the doctors tormented him with treatment, he died in agony"
  locator: "III.38 second paragraph; https://www.intratext.com/IXT/ITA1139/_P2U.HTM"
  verdict: confirmed in substance
  source_replacement: eligible
  status: resolved
  research_note: "Intended treatment: contextual paraphrase or proposed exact replacement. Named man is Rosso, already discussed in Q-033. Source says fistula/festering injury, not diagnosed gangrene; medici, not specifically surgeons; no month-long duration. The dog is an optional source detail omitted in lecture, not license for unapproved addition."
```

## Boundary audit: passages not to manufacture into source quotations

- U-00125–26 “Send a cobbler to the pope?” is Barbero's rhetorical example; no historic envoy says it here.
- U-00153–57 knighting mechanics and a young knight's hypothetical thoughts explain the narrative; Q-005 covers only Compagni's supplied battle statements.
- U-00194 invented patronymics, U-00198–200 the imagined sixty-man armed appearance, U-00218–19 the council's “bishop is a nuisance” speech: illustrative scenarios. Q-007/008 supply their underlying referents without pretending to recover that dialogue.
- U-00230–31 is the lecturer's explicit modern restatement of Guglielmo's indirect speech; Q-009 preserves the distinction.
- U-00240–42 “Dino has no relatives; self-made man” is an interpretive factual claim, not a source quotation. It is not literally true biographically (QSRC-003 opening), and Q-038 actually mentions his children. Treat “does not talk about relatives” as a claim about emphasis, not proven absence from the full work.
- U-00252 forgotten ancestral feud; U-00264–66 imagined Uberti tenants; U-00288–90 “without nobles we could work”; U-00331 “we nobles won”; U-00402–05 “you're not one of us”: Barbero voices generalized mentalities. They need no invented medieval source wording.
- U-00299–U-00322 government mechanics are historical claims, with background in I.4/11; no claim that the lecturer recites legislation verbatim. U-00421–24 random drawing is likewise a general institutional claim requiring separate chronological checking, not recovered Compagni speech.
- U-00436–38 alternative routes are paraphrase of an actual debate (Q-023); U-00460 imagined urgent question before Charles's arrival is a dramatized council question. Neither is a recoverable transcript of an actual meeting.
- U-00472–76 November darkness and politics ending at five are inference/explanation. Q-025 confirms only occupied platform and short days.
- U-00501–07 imagined discussion of the cardinal gift is lecturer staging. Q-027 is the actual speech Dino reports at delivery. U-00510 parenthesis that 2,000 is colossal is commentary.
- U-00526 profiteering within two months and U-00546 payment without a vote are lecture commentary, not extensions of a source quotation.
- U-00562 the hypothetical computation of tax equivalence is not retrieved source testimony. Q-033 recovers the nickname and the actual stated link to poor spinners.
- U-00589–90 demand for a “truly neutral government” paraphrases partisan demands recorded in II.10/12. U-00616–17 “listen, Dino” and taking him aside dramatize Noffo; the original does not supply either detail.
- U-00623 Judas and U-00624–26 children/dogs have different modes: explanatory authorial judgment then reported answer. Keep quotation boundaries visible.
- U-00703 “draw our swords and see who's a man” is hypothetical merchant/noble speech. U-00712 class-based self-reproach is Barbero's interpretive ending to the real II.5 retrospective.
- U-00731–35 oath remorse overstates quantifiers and removes the source's conditional self-defense; do not fabricate original text to match it.
- U-00779 outsiders must command us is the lecturer's interpretation. U-00793–96 divine inner monologue is a contextual rendering of III.37/41, not recovered speech. U-00784 future imperial failure is narrator hindsight, outside the quoted chronicle.

## Intended treatment and verification handoff

For each `eligible` item, the exact Italian and new translation above supply a bounded candidate, but do not themselves select a replacement. The safest initial draft maintains Barbero's alternation among small quoted phrases, narratorial paraphrase, and modern explanation. Authoritative recovered wording would require a concrete decision proposal with exact target and replacement spans, especially Q-004, Q-021/022, Q-027, Q-030, Q-033, Q-035/039, Q-046, Q-050/051. Do not turn this dossier into a continuous reading of the chronicle.

The one deferred record Q-039 is an explicit incompatibility, not an inaccessible source. Responsible narration can continue by retaining the lecture's claim as contextual rendering pending an editorial decision, or by an approved revision saying the mixed slate never took office. The evidence synthesizer must consider whether faithful repetition with this known contradiction meets its intended draft status.

No audio was listened to in this investigation. Primary-text matches can guide contextual transcript corrections (including 'ai cani', 'ha degli amici', 'arrotare i ferri') but cannot certify exact audible words. The source agent has completed contextual corrections with user approval; this report records the resulting transcript hash above. Research findings remain separate from that approval. Utterance IDs, rather than line numbers, are intentionally retained. Final validation parsed both embedded YAML lists: 3 source records and 51 quotation records; all required fields, sequential Q IDs, accepted enum values, utterance-ID bounds and downloaded chapter URL targets passed. Of the 51 records, 50 have resolved provenance and one is explicitly deferred (Q-039). 'Resolved' does not imply every lecture detail is historically confirmed: each material mismatch is retained in its research_note.
