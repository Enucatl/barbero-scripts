# Source review — La paura dell’Anno Mille

Status: full contextual scan complete; source resolutions pending. This is a text and provider-evidence review, not an audio review. No audio has been listened to, no spoken text has been changed, and no Italian script has been assembled. The source metadata and transcript remain authoritative.

All 907 retained utterances (U-00001–U-00907) were read in order. The complete transcript’s ordered IDs and spoken text match `utterances.json` exactly. Provider word confidence and tokenization were inspected for the semantic problems below and all 262 original generated queue entries were inspected. A recognizer confidence score is not listening evidence or a guarantee of correct wording.

## Inputs and checks

| Input | SHA-256 |
|---|---|
| `/opt/docker/barbero-scripts/episodes/013-la-paura-dell-anno-mille/episode.yaml` | `5135c3e3260e8b327deb09961776ac39cfb878201738d687345b68ab51ef4c06` |
| `/opt/docker/barbero-scripts/episodes/013-la-paura-dell-anno-mille/transcript.it.md` | `6088b19e1b5f07591128aa565434bf425d2a2a8196ae926d2e8561e3a6d3a52e` |
| `/opt/docker/barbero-scripts/episodes/013-la-paura-dell-anno-mille/chapters.yaml` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| `/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/utterances.json` | `063049d06f1f04eda8707868915993ab79a44cf456a480d3f1ed954d5972cd73` |
| `/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/transcription-manifest.json` | `4cadb4be0dd7f4d0fd8a5bf8b9deee86f1717176e022844ea7acecb367814e8b` |
| `/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/deepgram.json` | `0fd7fcc34d10fb75d2f87a9586a9906a07fabbeee16f25c63edcf3ae1facfcad` |
| `/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/edit-map.json` | `6a322578a514fbb6f80e585572a8879ebae6b6c95028310f1463a1efd5e194d2` |
| `transcript-uncertainties.yaml` before this review | `86ab88afd7c4824fd15f58bfe65c871a95bcfd7a26c02d323c7a0f2c61cd914a` |
| `transcript-uncertainties.yaml` after this review | `6408574529e06ef5d04f34a536a4996c09db1c3e0da2fc660e38662b2aa6a512` |

Actual manifest fingerprint: `47b5df524e16c240bb004068ce6a1283a76a465d9233cf2482f17a310c8708cc`. The queue matches it and `validate_transcript_uncertainties` returned no errors. All original IDs, timestamps, current text, acoustic/semantic reasons and pending resolutions were preserved. New IDs begin at TU-263. `detection_status: complete` records completion of the whole contextual scan, not human acceptance or audio verification.

There is no `script.it.md`, earlier source decision file, or assembled chapter map in this episode; `chapters.yaml` currently contains `[]`. No accepted/rejected source decisions exist to inherit. Existing episodes’ editorial decisions do not authorize cuts here.

## Consolidated source decisions

**Package A:** accept the exact complete-utterance proposals below for contextual recognition/spelling, numeral tokenization, and missing auxiliaries. These remain proposals until accepted. Numerals representing dates or genuine ordinals are otherwise preserved. No historical date, argument, joke, hesitation, repetition, or digression has been replaced. Capitalization, broad punctuation polishing, and natural spoken grammar have not been normalized throughout.

**Package B:** five tentative reconstructions need a focused decision. They are plausible alternatives, not conclusions. Accept each exact proposal, retain its complete current utterance, or supply a complete corrected utterance. Original timestamps and adjacent context are included for listening. Historical research must not silently settle what was spoken.

Total: **109 changed-text proposals** (104 in A; 5 in B); **195 unchanged flagged utterances**; **304 pending queue items** after adding 42 semantic items. No item is resolved.

The unchanged flags are provider confidence/date/name triggers with coherent contextual readings, not additional identified material source ambiguities. They can be accepted together as their existing complete `current_text` / `proposed_text`; they must not be marked audio-reviewed. A future source finding may reopen an affected item. Existing [REVIEW:…] markers have not been removed.

Unchanged queue IDs: TU-001 (U-00002), TU-002 (U-00004), TU-003 (U-00010), TU-004 (U-00011), TU-005 (U-00012), TU-006 (U-00015), TU-007 (U-00017), TU-008 (U-00020), TU-009 (U-00022), TU-010 (U-00023), TU-011 (U-00024), TU-012 (U-00025), TU-013 (U-00031), TU-014 (U-00032), TU-015 (U-00040), TU-016 (U-00042), TU-017 (U-00044), TU-023 (U-00052), TU-024 (U-00058), TU-025 (U-00061), TU-026 (U-00064), TU-027 (U-00070), TU-028 (U-00075), TU-029 (U-00078), TU-030 (U-00083), TU-031 (U-00085), TU-032 (U-00087), TU-033 (U-00090), TU-034 (U-00093), TU-035 (U-00095), TU-036 (U-00107), TU-037 (U-00108), TU-039 (U-00111), TU-040 (U-00115), TU-042 (U-00127), TU-043 (U-00132), TU-044 (U-00135), TU-045 (U-00142), TU-046 (U-00143), TU-047 (U-00158), TU-051 (U-00170), TU-052 (U-00171), TU-054 (U-00176), TU-055 (U-00177), TU-056 (U-00189), TU-057 (U-00190), TU-061 (U-00211), TU-062 (U-00213), TU-063 (U-00214), TU-064 (U-00221), TU-065 (U-00223), TU-067 (U-00226), TU-068 (U-00227), TU-070 (U-00232), TU-071 (U-00234), TU-072 (U-00237), TU-073 (U-00248), TU-074 (U-00250), TU-075 (U-00252), TU-076 (U-00254), TU-078 (U-00258), TU-079 (U-00261), TU-080 (U-00268), TU-081 (U-00269), TU-082 (U-00273), TU-083 (U-00275), TU-084 (U-00278), TU-085 (U-00279), TU-086 (U-00281), TU-087 (U-00283), TU-088 (U-00291), TU-089 (U-00295), TU-090 (U-00302), TU-091 (U-00303), TU-092 (U-00306), TU-093 (U-00307), TU-094 (U-00309), TU-095 (U-00311), TU-096 (U-00312), TU-098 (U-00321), TU-099 (U-00325), TU-100 (U-00327), TU-101 (U-00333), TU-102 (U-00334), TU-103 (U-00335), TU-105 (U-00338), TU-107 (U-00343), TU-110 (U-00352), TU-112 (U-00365), TU-113 (U-00368), TU-115 (U-00383), TU-116 (U-00387), TU-117 (U-00391), TU-118 (U-00396), TU-121 (U-00403), TU-123 (U-00409), TU-124 (U-00416), TU-126 (U-00428), TU-128 (U-00433), TU-130 (U-00438), TU-131 (U-00443), TU-132 (U-00446), TU-133 (U-00456), TU-134 (U-00459), TU-136 (U-00471), TU-137 (U-00472), TU-138 (U-00473), TU-139 (U-00477), TU-141 (U-00479), TU-142 (U-00490), TU-144 (U-00497), TU-146 (U-00505), TU-147 (U-00506), TU-149 (U-00514), TU-151 (U-00518), TU-153 (U-00526), TU-154 (U-00530), TU-155 (U-00532), TU-156 (U-00543), TU-160 (U-00550), TU-161 (U-00552), TU-162 (U-00558), TU-163 (U-00559), TU-164 (U-00560), TU-167 (U-00567), TU-169 (U-00569), TU-172 (U-00577), TU-173 (U-00582), TU-175 (U-00586), TU-176 (U-00594), TU-177 (U-00595), TU-179 (U-00598), TU-181 (U-00616), TU-182 (U-00620), TU-183 (U-00623), TU-184 (U-00624), TU-186 (U-00638), TU-188 (U-00640), TU-189 (U-00642), TU-190 (U-00651), TU-191 (U-00653), TU-192 (U-00654), TU-193 (U-00656), TU-194 (U-00657), TU-195 (U-00669), TU-196 (U-00670), TU-197 (U-00674), TU-198 (U-00676), TU-199 (U-00679), TU-200 (U-00681), TU-201 (U-00689), TU-202 (U-00704), TU-203 (U-00708), TU-204 (U-00709), TU-205 (U-00719), TU-207 (U-00724), TU-208 (U-00730), TU-209 (U-00731), TU-210 (U-00734), TU-211 (U-00735), TU-212 (U-00738), TU-213 (U-00739), TU-214 (U-00746), TU-216 (U-00751), TU-217 (U-00755), TU-218 (U-00757), TU-219 (U-00760), TU-220 (U-00765), TU-221 (U-00773), TU-222 (U-00777), TU-223 (U-00779), TU-224 (U-00785), TU-225 (U-00787), TU-226 (U-00788), TU-228 (U-00792), TU-229 (U-00793), TU-230 (U-00805), TU-231 (U-00814), TU-232 (U-00817), TU-233 (U-00818), TU-234 (U-00822), TU-236 (U-00824), TU-238 (U-00826), TU-240 (U-00831), TU-242 (U-00836), TU-244 (U-00855), TU-246 (U-00857), TU-247 (U-00858), TU-252 (U-00867), TU-256 (U-00881), TU-258 (U-00892), TU-259 (U-00895), TU-260 (U-00896), TU-261 (U-00901), TU-262 (U-00905).

## A1 — Names and terms

51 complete utterance proposals.

### TU-263 · U-00013 · original 01:43.395–01:46.435

**Current:** ho visto che quando gli dicevo guarda che lo ius prime noctis

**Proposed:** ho visto che quando gli dicevo guarda che lo ius primae noctis

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-038 · U-00110 · original 07:11.790–07:14.030

**Current:** il La Vallet, allievo di Michelée,

**Proposed:** il Lavallée, allievo di Michelet,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-041 · U-00123 · original 07:49.845–07:52.725

**Current:** con gioia del professor Oddifreddi che vedo qui davanti a me.

**Proposed:** con gioia del professor Odifreddi che vedo qui davanti a me.

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-048 · U-00161 · original 10:05.585–10:08.865

**Current:** si chiamava Gerberto di Oriac 1º di diventare papa,

**Proposed:** si chiamava Gerberto di Aurillac prima di diventare papa,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-049 · U-00168 · original 10:35.190–10:37.030

**Current:** uno è un prete, Ad Alberto,

**Proposed:** uno è un prete, Adalberto,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-058 · U-00191 · original 11:52.325–11:56.805

**Current:** L'albero degli zoccoli di Hermanno Olmi tanto per citare un film che magari molti hanno visto.

**Proposed:** L'albero degli zoccoli di Ermanno Olmi tanto per citare un film che magari molti hanno visto.

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-069 · U-00230 · original 14:56.145–15:03.985

**Current:** potrà dare in beneficio a qualcuno il monastero di di Parfa ma rimanga sempre di proprietà dello stato

**Proposed:** potrà dare in beneficio a qualcuno il monastero di di Farfa ma rimanga sempre di proprietà dello stato

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-268 · U-00231 · original 15:04.305–15:05.345

**Current:** res pubblica.

**Proposed:** res publica.

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-104 · U-00337 · original 21:36.620–21:37.980

**Current:** Si chiama Abone,

**Proposed:** Si chiama Abbone,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-106 · U-00339 · original 21:40.300–21:45.660

**Current:** Abone di Fleury, grande studioso, grande scrittore, grande intellettuale, uno che letto molto e capisce molto,

**Proposed:** Abbone di Fleury, grande studioso, grande scrittore, grande intellettuale, uno che ha letto molto e capisce molto,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-108 · U-00344 · original 21:55.260–21:57.980

**Current:** Abone di Fleury dice al re di Francia,

**Proposed:** Abbone di Fleury dice al re di Francia,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-111 · U-00357 · original 22:41.295–22:48.890

**Current:** il calendario liturgico fan cominciare l'avvento un giorno 1º e anche questo non va bene dice Abone, il re deve provvedere.

**Proposed:** il calendario liturgico fan cominciare l'avvento un giorno prima e anche questo non va bene dice Abbone, il re deve provvedere.

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed. Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-274 · U-00358 · original 22:49.690–22:51.290

**Current:** E poi dice Abone,

**Proposed:** E poi dice Abbone,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-275 · U-00362 · original 23:05.695–23:07.695

**Current:** Abone dice io mi ricordo

**Proposed:** Abbone dice io mi ricordo

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-276 · U-00369 · original 23:27.835–23:29.595

**Current:** E io, dice Abone,

**Proposed:** E io, dice Abbone,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-114 · U-00373 · original 23:44.660–23:46.420

**Current:** poi dice Abone

**Proposed:** poi dice Abbone

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-277 · U-00401 · original 25:25.940–25:30.740

**Current:** ma la cosa interessante è che Abone, che ci sta raccontando questa cosa, dice,

**Proposed:** ma la cosa interessante è che Abbone, che ci sta raccontando questa cosa, dice,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-120 · U-00402 · original 25:31.140–25:35.380

**Current:** quando è arrivata questa notizia, il buon abate Riccardo mi detto, Abone,

**Proposed:** quando è arrivata questa notizia, il buon abate Riccardo mi ha detto, Abbone,

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-122 · U-00404 · original 25:43.045–25:50.325

**Current:** ma è chiaro che questo è il senso del discorso e io dice Abone ho scritto spiegando quanto fosse folle questo ragionamento.

**Proposed:** ma è chiaro che questo è il senso del discorso e io dice Abbone ho scritto spiegando quanto fosse folle questo ragionamento.

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-278 · U-00417 · original 26:28.280–26:34.120

**Current:** quando scrive Abone sono ricordi di giovinezza.

**Proposed:** quando scrive Abbone sono ricordi di giovinezza.

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-125 · U-00419 · original 26:36.680–26:43.345

**Current:** l'abate Riccardo dice ad Abone queste son tutte frottole scrivi tu? Perché son così convinti gli uomini di chiesa

**Proposed:** l'abate Riccardo dice ad Abbone queste son tutte frottole scrivi tu? Perché son così convinti gli uomini di chiesa

**Reason:** Consistent Italian spelling Abbone di Fleury, the same named monk throughout; audio not reviewed.

### TU-127 · U-00432 · original 27:20.655–27:26.175

**Current:** lo sa. San Paolo, 1º lettera ai Testalonicesi,

**Proposed:** lo sa. San Paolo, prima lettera ai Tessalonicesi,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Write the feminine ordinal prima for lettera/storia; preserve the ordinal meaning.

### TU-283 · U-00488 · original 30:07.775–30:09.215

**Current:** si chiama fiota.

**Proposed:** si chiama Thiota.

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-152 · U-00521 · original 32:35.895–32:41.335

**Current:** vedo sempre il professore di freddi che ride sotto I baffi, ma anche voi matematici 2º me certe volte, comunque

**Proposed:** vedo sempre il professor Odifreddi che ride sotto I baffi, ma anche voi matematici secondo me certe volte, comunque

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Here secondo means according to/in my view, not an ordinal number.

### TU-157 · U-00545 · original 33:58.055–34:02.455

**Current:** e un bravo cronista si chiama Sigeberto Sigeberto di Jean Blu scrive

**Proposed:** è un bravo cronista si chiama Sigeberto Sigeberto di Gembloux scrive

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Resolve e/è recognition ambiguity from the complete sentence context, preserving the intended assertion.

### TU-165 · U-00563 · original 35:09.821–35:17.340

**Current:** Non dice, va detto a onore di Sigeberto di Jean-Blou, non dice e tutti hanno avuto paura della fine del mondo. Lui si limita a accumulare

**Proposed:** Non dice, va detto a onore di Sigeberto di Gembloux, non dice e tutti hanno avuto paura della fine del mondo. Lui si limita a accumulare

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-171 · U-00576 · original 35:53.386–35:54.585

**Current:** Guillon Godel scrive,

**Proposed:** Guillaume Godel scrive,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-174 · U-00583 · original 36:09.915–36:14.875

**Current:** ma ghioen godel non è mica uno sciocco lo sa cosa pensa la gente quando vede l'eclisse

**Proposed:** ma Guillaume Godel non è mica uno sciocco lo sa cosa pensa la gente quando vede l'eclisse

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-178 · U-00597 · original 37:05.655–37:09.735

**Current:** che nella sua cronaca anche lui letto sigeberto di jam blu

**Proposed:** che nella sua cronaca anche lui ha letto Sigeberto di Gembloux

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-180 · U-00601 · original 37:22.480–37:28.080

**Current:** questo non l' letto Insigeberto di Jean-Blue ma voi capite come funziona è un umanista

**Proposed:** questo non l’ha letto in Sigeberto di Gembloux ma voi capite come funziona è un umanista

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-290 · U-00648 · original 39:46.175–39:50.310

**Current:** quella francese in lingua dohil, poi quella italiana, I trovatori, tutto.

**Proposed:** quella francese in lingua d’oïl, poi quella italiana, I trovatori, tutto.

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-227 · U-00791 · original 47:37.091–47:38.050

**Current:** Domplen,

**Proposed:** Dom Plaine,

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-237 · U-00825 · original 49:47.115–49:49.195

**Current:** che si chiama Silvan Guggenheim

**Proposed:** che si chiama Sylvain Gouguenheim

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-241 · U-00834 · original 50:15.200–50:21.200

**Current:** perché se andiamo a vedere la storiografia del 900 la grande storiografia francese du be quegli

**Proposed:** perché se andiamo a vedere la storiografia del 900 la grande storiografia francese Duby quegli

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-296 · U-00837 · original 50:25.920–50:27.120

**Current:** dice guggenheim

**Proposed:** dice Gouguenheim

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-297 · U-00844 · original 50:41.305–50:42.745

**Current:** in sostanza guggenheim

**Proposed:** in sostanza Gouguenheim

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-243 · U-00846 · original 50:43.970–50:58.050

**Current:** alcuni mostri sacri della storiografia del 900 come appunto jeuge du bies, gugenheim dice questi in realtà grandi maestri per carità però hanno creato di nuovo un'impressione falsa son tornati a dare questa impressione dell'anno 1000 come epoca

**Proposed:** alcuni mostri sacri della storiografia del 900 come appunto Georges Duby, Gouguenheim dice questi in realtà grandi maestri per carità però hanno creato di nuovo un'impressione falsa son tornati a dare questa impressione dell'anno 1000 come epoca

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed. The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-298 · U-00849 · original 51:02.605–51:07.486

**Current:** mentre dice guggenheim non è vero niente

**Proposed:** mentre dice Gouguenheim non è vero niente

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-299 · U-00850 · original 51:07.565–51:10.845

**Current:** perchè è interessante scoprire questo perchè guggenheim

**Proposed:** perchè è interessante scoprire questo perchè Gouguenheim

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-245 · U-00856 · original 51:22.650–51:26.650

**Current:** Guggenheim è diventato famoso in Francia per un libro che è uscito 5 anni fa

**Proposed:** Gouguenheim è diventato famoso in Francia per un libro che è uscito 5 anni fa

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-300 · U-00859 · original 51:29.736–51:31.496

**Current:** al mont Saint-Michelle.

**Proposed:** al mont Saint-Michel.

**Reason:** Consistent spelling of Mont Saint-Michel; no factual substitution.

### TU-248 · U-00860 · original 51:32.375–51:39.736

**Current:** Il mont Saint-Michelle avete presente, è la famosa abbazia in Normandia, quella che sta in mezzo al mare quando c'è la marea rimane isolata dalla terraferma.

**Proposed:** Il mont Saint-Michel avete presente, è la famosa abbazia in Normandia, quella che sta in mezzo al mare quando c'è la marea rimane isolata dalla terraferma.

**Reason:** Consistent spelling of Mont Saint-Michel; no factual substitution.

### TU-249 · U-00861 · original 51:40.710–51:41.590

**Current:** Guggenheimin

**Proposed:** Gouguenheim in

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-250 · U-00862 · original 51:41.590–51:43.670

**Current:** aristotele al mont Saint-Michelle

**Proposed:** aristotele al mont Saint-Michel

**Reason:** Consistent spelling of Mont Saint-Michel; no factual substitution.

### TU-251 · U-00866 · original 51:51.990–52:01.066

**Current:** e altri illustri studiosi che hanno detto che invece è molto interessante. Quindi io non l'ho ancora letto vi riferisco soltanto quel che so in sintesi gugenheim in questo libro

**Proposed:** e altri illustri studiosi che hanno detto che invece è molto interessante. Quindi io non l'ho ancora letto vi riferisco soltanto quel che so in sintesi Gouguenheim in questo libro

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-302 · U-00872 · original 52:17.360–52:18.160

**Current:** etolomeo

**Proposed:** e Tolomeo

**Reason:** Context identifies the name or expression; correct its written recognition/spelling without changing the historical claim. Audio not reviewed.

### TU-303 · U-00874 · original 52:21.360–52:26.800

**Current:** io credo che voi capiate già le implicazioni di questo ma guggenheim per non farsi mancar niente

**Proposed:** io credo che voi capiate già le implicazioni di questo ma Gouguenheim per non farsi mancar niente

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-253 · U-00875 · original 52:27.075–52:33.315

**Current:** le esplicita nel suo libro. Queste pagine le ho viste, sono andato a vederle. Guggenheim dice, e quindi

**Proposed:** le esplicita nel suo libro. Queste pagine le ho viste, sono andato a vederle. Gouguenheim dice, e quindi

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-254 · U-00879 · original 52:43.770–52:52.730

**Current:** La filosofia e la scienza greca dice Guggenheim noi cristiani ce le siamo tradotte direttamente dal greco e non avevamo nessun bisogno degli arabi.

**Proposed:** La filosofia e la scienza greca dice Gouguenheim noi cristiani ce le siamo tradotte direttamente dal greco e non avevamo nessun bisogno degli arabi.

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-255 · U-00880 · original 52:53.610–53:09.906

**Current:** E tanto per essere ancora più chiaro nelle ultime pagine del libro Guggenheim dice e del resto si sa l'arabo è una lingua completamente inadatta per parlare di argomenti scientifici che gli arabi come mentalità non sono un popolo di scienziati e di conseguenza era ridicolo pensare che noi gli dovessimo qualche cosa.

**Proposed:** E tanto per essere ancora più chiaro nelle ultime pagine del libro Gouguenheim dice e del resto si sa l'arabo è una lingua completamente inadatta per parlare di argomenti scientifici che gli arabi come mentalità non sono un popolo di scienziati e di conseguenza era ridicolo pensare che noi gli dovessimo qualche cosa.

**Reason:** The scholar referred to throughout is Sylvain Gouguenheim. Preserve the distinct Peggy Guggenheim joke at U-00826 and the speculative ancestry remark at U-00827 for editorial review, not transcript correction.

### TU-257 · U-00889 · original 53:30.125–53:31.646

**Current:** al mont Saint-Michelle

**Proposed:** al mont Saint-Michel

**Reason:** Consistent spelling of Mont Saint-Michel; no factual substitution.

## A2 — Recognition and word boundaries

9 complete utterance proposals.

### TU-053 · U-00175 · original 10:57.685–11:03.205

**Current:** perché in molte parti d'Europa andavano più alla buona. Un contratto, uno spunto sul palmo, stretta di mano.

**Proposed:** perché in molte parti d'Europa andavano più alla buona. Un contratto, uno sputo sul palmo, stretta di mano.

**Reason:** Spitting into the palm before a handshake fits the narrated informal contract; spunto does not. Audio not reviewed.

### TU-059 · U-00199 · original 12:27.130–12:38.265

**Current:** dà in affitto queste terre del monastero a questi 2 fratelli per la durata di 29 anni. La condizione che dovranno abitarci, coltivarle,

**Proposed:** dà in affitto queste terre del monastero a questi 2 fratelli per la durata di 29 anni. Alla condizione che dovranno abitarci, coltivarle,

**Reason:** Lease conditions introduce the following obligations; missing initial a in the transcription. Audio not reviewed.

### TU-066 · U-00225 · original 14:30.475–14:41.720

**Current:** I monaci di farfa hanno il privilegio, non possono essere dati in questo modo a nessuno, I loro abate se lo eleggono loro. L'imperatore Ottone 3º dice benissimo, siamo d'accordo, ve lo concediamo.

**Proposed:** I monaci di farfa hanno il privilegio, non possono essere dati in questo modo a nessuno, il loro abate se lo eleggono loro. L'imperatore Ottone 3º dice benissimo, siamo d'accordo, ve lo concediamo.

**Reason:** The singular abbot is elected by the monks; article recognition error. Audio not reviewed.

### TU-109 · U-00348 · original 22:06.365–22:10.445

**Current:** del fatto che I conti anziché rendere giustizia in tasca le bustarelle,

**Proposed:** del fatto che I conti anziché rendere giustizia intascano le bustarelle,

**Reason:** The counts take bribes instead of administering justice; wrong token boundaries obscure the finite verb. Audio not reviewed.

### TU-282 · U-00482 · original 29:56.400–29:57.360

**Current:** un'analista

**Proposed:** un annalista

**Reason:** The source is a chronicler/annalist, not an analyst; confirmed by the immediately following narrative of 847. Audio not reviewed.

### TU-285 · U-00501 · original 30:59.745–31:07.905

**Current:** dicendole tu vai in giro a predicare che l'anno prossimo viene la figlia del mondo vedrai la gente quanti regali ci porta e infatti è proprio successo così

**Proposed:** dicendole tu vai in giro a predicare che l'anno prossimo viene la fine del mondo vedrai la gente quanti regali ci porta e infatti è proprio successo così

**Reason:** The prophecy concerns the end of the world throughout this anecdote. Audio not reviewed.

### TU-286 · U-00503 · original 31:19.120–31:30.205

**Current:** e così viene come dire spento il movimento millenneristico di magonza dell'anno 847

**Proposed:** e così viene come dire spento il movimento millenaristico di magonza dell'anno 847

**Reason:** Recognition/spelling of the term used throughout the lecture. Audio not reviewed.

### TU-158 · U-00547 · original 34:05.255–34:09.415

**Current:** letto gli analisti dell'anno 1000 I quali delle paure non parlavan per niente

**Proposed:** ha letto gli annalisti dell'anno 1000 I quali delle paure non parlavan per niente

**Reason:** The named sources are the annalists of the year 1000. Audio not reviewed. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-187 · U-00639 · original 39:18.470–39:24.390

**Current:** Tutti abbiamo studiato a scuola storia della letteratura italiana, no? Comincia tutto dopo l'anno 1001º

**Proposed:** Tutti abbiamo studiato a scuola storia della letteratura italiana, no? Comincia tutto dopo l'anno 1000, prima

**Reason:** Merged number and prima: next utterance is niente; contrast is everything after 1000, nothing before, not year 1001. Audio not reviewed.

## A3 — Numerals used as words

19 complete utterance proposals.

### TU-020 · U-00048 · original 03:41.530–03:43.530

**Current:** 2º questo racconto

**Proposed:** secondo questo racconto

**Reason:** Here secondo means according to/in my view, not an ordinal number.

### TU-022 · U-00050 · original 03:47.050–03:49.850

**Current:** e negli ultimi anni 1º dell'anno 1000

**Proposed:** e negli ultimi anni prima dell'anno 1000

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-264 · U-00057 · original 04:10.380–04:16.940

**Current:** 2º questa storia che troviamo raccontata da tanti studiosi, da tanti dotti della nostra epoca dell'Ottocento,

**Proposed:** secondo questa storia che troviamo raccontata da tanti studiosi, da tanti dotti della nostra epoca dell'Ottocento,

**Reason:** Here secondo means according to/in my view, not an ordinal number.

### TU-265 · U-00088 · original 06:00.380–06:02.380

**Current:** aveva 2º la tradizione

**Proposed:** aveva secondo la tradizione

**Reason:** Here secondo means according to/in my view, not an ordinal number.

### TU-269 · U-00238 · original 15:36.270–15:37.310

**Current:** 1º o poi.

**Proposed:** prima o poi.

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-097 · U-00318 · original 20:29.305–20:34.905

**Current:** Ecco, questi movimenti, queste 7 noi come li chiamiamo? Li chiamiamo movimenti millenaristi,

**Proposed:** Ecco, questi movimenti, queste sette noi come li chiamiamo? Li chiamiamo movimenti millenaristi,

**Reason:** Here sette means religious sects, not the number seven.

### TU-271 · U-00319 · original 20:35.460–20:37.940

**Current:** parliamo di 7 millenariste,

**Proposed:** parliamo di sette millenariste,

**Reason:** Here sette means religious sects, not the number seven.

### TU-119 · U-00400 · original 25:20.075–25:24.980

**Current:** guarda lì si vede che l'anno 1º qualcuno fatto quel calcolo,

**Proposed:** guarda lì si vede che l'anno prima qualcuno ha fatto quel calcolo,

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words. Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-129 · U-00435 · original 27:32.580–27:34.260

**Current:** Cioè non è che si annuncia 1º,

**Proposed:** Cioè non è che si annuncia prima,

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-135 · U-00465 · original 28:57.465–29:06.280

**Current:** Sta scritto che 1º che venga l'anticristo e poi la fine del mondo il Vangelo dovrà essere predicato a tutti I popoli della terra.

**Proposed:** Sta scritto che prima che venga l'anticristo e poi la fine del mondo il Vangelo dovrà essere predicato a tutti I popoli della terra.

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-140 · U-00478 · original 29:46.880–29:49.360

**Current:** parecchio 1º dell'anno 1000 torniamo indietro

**Proposed:** parecchio prima dell'anno 1000 torniamo indietro

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-148 · U-00509 · original 31:54.165–32:00.980

**Current:** che negli ultimi mesi e giorni 1º dell'anno 1000 c'era il terrore collettivo e le chiese piene, è inutile che ve lo dica, no?

**Proposed:** che negli ultimi mesi e giorni prima dell'anno 1000 c'era il terrore collettivo e le chiese piene, è inutile che ve lo dica, no?

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-185 · U-00637 · original 39:13.445–39:15.365

**Current:** ma 1º o dopo l'anno 1000?

**Proposed:** ma prima o dopo l'anno 1000?

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-291 · U-00665 · original 40:36.925–40:41.725

**Current:** pubblica una 1º grande storia della letteratura e della cultura italiana.

**Proposed:** pubblica una prima grande storia della letteratura e della cultura italiana.

**Reason:** Write the feminine ordinal prima for lettera/storia; preserve the ordinal meaning.

### TU-292 · U-00684 · original 41:26.985–41:29.545

**Current:** che erano 1º state neglette

**Proposed:** che erano prima state neglette

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-293 · U-00710 · original 42:41.800–42:43.240

**Current:** un secolo 1º

**Proposed:** un secolo prima

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-294 · U-00712 · original 42:48.120–42:50.120

**Current:** Io l'ho detto 1º ma voi non ve lo ricordate

**Proposed:** Io l'ho detto prima ma voi non ve lo ricordate

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-206 · U-00721 · original 43:08.240–43:10.480

**Current:** 1º del 1000 non trova niente

**Proposed:** prima del 1000 non trova niente

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

### TU-295 · U-00795 · original 48:01.156–48:04.275

**Current:** perché io devo dire, ho già detto un po' 1º e lo dico di nuovo,

**Proposed:** perché io devo dire, ho già detto un po' prima e lo dico di nuovo,

**Reason:** Here prima means before/earlier, not an ordinal number. Preserve the original date and surrounding words.

## A4 — Missing auxiliaries

25 complete utterance proposals.

### TU-018 · U-00045 · original 03:29.715–03:32.835

**Current:** E quindi, quando l'anno 1000 cominciato a avvicinarsi,

**Proposed:** E quindi, quando l'anno 1000 ha cominciato a avvicinarsi,

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-019 · U-00047 · original 03:38.490–03:41.530

**Current:** ma quando l'anno 1000 cominciato a avvicinarsi

**Proposed:** ma quando l'anno 1000 ha cominciato a avvicinarsi

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-021 · U-00049 · original 03:43.930–03:46.570

**Current:** la gente cominciato a aver paura sul serio

**Proposed:** la gente ha cominciato a aver paura sul serio

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-266 · U-00129 · original 08:14.885–08:17.765

**Current:** che bloccato la società europea.

**Proposed:** che ha bloccato la società europea.

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-077 · U-00257 · original 17:03.410–17:09.010

**Current:** Torniamo un po' indietro. Noi l'abbiam detto, il Carducci dice 1000, non più 1000, citato l'apocalisse.

**Proposed:** Torniamo un po' indietro. Noi l'abbiam detto, il Carducci dice 1000, non più 1000, ha citato l'apocalisse.

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-272 · U-00330 · original 21:10.635–21:13.915

**Current:** c'è stato qualcuno che fatto questi ragionamenti

**Proposed:** c'è stato qualcuno che ha fatto questi ragionamenti

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-273 · U-00332 · original 21:15.755–21:17.835

**Current:** e che cominciato a dire in giro

**Proposed:** e che ha cominciato a dire in giro

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-279 · U-00424 · original 26:55.850–26:58.250

**Current:** e che gli uomini di chiesa del medioevo

**Proposed:** è che gli uomini di chiesa del medioevo

**Reason:** Resolve e/è recognition ambiguity from the complete sentence context, preserving the intended assertion.

### TU-280 · U-00442 · original 27:46.795–27:48.715

**Current:** il signore lo detto chiaramente

**Proposed:** il signore l’ha detto chiaramente

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-281 · U-00457 · original 28:36.020–28:37.620

**Current:** detto che nessuno

**Proposed:** ha detto che nessuno

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-143 · U-00491 · original 30:16.940–30:22.540

**Current:** lei conosce questa cosa dice il monaco che nessuno può sapere come se fosse dio che gliel' rivelata

**Proposed:** lei conosce questa cosa dice il monaco che nessuno può sapere come se fosse dio che gliel’ha rivelata

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-284 · U-00500 · original 30:53.665–30:59.265

**Current:** e viene fuori almeno la donna dice che questa cosa gliel' suggerita un prete suo amico

**Proposed:** e viene fuori almeno la donna dice che questa cosa gliel’ha suggerita un prete suo amico

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-150 · U-00517 · original 32:23.610–32:26.250

**Current:** chi è che l' inventata questa storia?

**Proposed:** chi è che l’ha inventata questa storia?

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-287 · U-00546 · original 34:02.455–34:04.375

**Current:** una cronaca letto tanti libri

**Proposed:** una cronaca, ha letto tanti libri

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-159 · U-00549 · original 34:11.370–34:15.930

**Current:** che nell'anno 1000 qualche cronista menzionato un terremoto

**Proposed:** che nell'anno 1000 qualche cronista ha menzionato un terremoto

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-166 · U-00565 · original 35:19.180–35:30.490

**Current:** E lui stesso un millenarista. L'anno 1000 è passato però l'impressione di quella cifra tonda continua a funzionare. Passano altri settant'anni, 1170

**Proposed:** È lui stesso un millenarista. L'anno 1000 è passato però l'impressione di quella cifra tonda continua a funzionare. Passano altri settant'anni, 1170

**Reason:** Resolve e/è recognition ambiguity from the complete sentence context, preserving the intended assertion.

### TU-168 · U-00568 · original 35:35.850–35:38.730

**Current:** che letto anche lui I cronisti

**Proposed:** che ha letto anche lui I cronisti

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-170 · U-00570 · original 35:41.786–35:44.265

**Current:** scoperto che nell'anno 1010

**Proposed:** ha scoperto che nell'anno 1010

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-288 · U-00580 · original 36:00.680–36:03.160

**Current:** avuto paura che il mondo finisse.

**Proposed:** ha avuto paura che il mondo finisse.

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-289 · U-00643 · original 39:37.775–39:40.335

**Current:** è un'epoca che lasciato poche testimonianze,

**Proposed:** è un'epoca che ha lasciato poche testimonianze,

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-215 · U-00750 · original 45:15.190–45:22.150

**Current:** perché la chiesa di allora è spaventata dal progresso, son cose che si posson dire tranquillamente perché la chiesa di oggi lo riconosciuto ampiamente.

**Proposed:** perché la chiesa di allora è spaventata dal progresso, son cose che si posson dire tranquillamente perché la chiesa di oggi l’ha riconosciuto ampiamente.

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-235 · U-00823 · original 49:41.275–49:42.796

**Current:** e di uno studioso

**Proposed:** è di uno studioso

**Reason:** Resolve e/è recognition ambiguity from the complete sentence context, preserving the intended assertion.

### TU-239 · U-00829 · original 49:57.530–50:02.090

**Current:** che scritto questo libro molto militante, I falsi terrori dell'anno 1000,

**Proposed:** che ha scritto questo libro molto militante, I falsi terrori dell'anno 1000,

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-301 · U-00864 · original 51:45.670–51:49.030

**Current:** e dico sostiene perché il suo libro provocato polemiche furibonde

**Proposed:** e dico sostiene perché il suo libro ha provocato polemiche furibonde

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

### TU-304 · U-00899 · original 54:06.630–54:09.271

**Current:** uno che aggiunto una righina in una cronaca

**Proposed:** uno che ha aggiunto una righina in una cronaca

**Reason:** Syntactic repair of a missing auxiliary in the recognizer text; preserves tense and the stated claim. Audio not reviewed.

## B — Tentative source reconstructions

5 complete utterance proposals.

### TU-267 · U-00160 · original 10:00.945–10:05.265

[Original audio excerpt with adjacent utterances](/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/source-clips/U-00160.mp3). Clip prepared by coordinator; not listened to in this review.

**Current:** tanto dotto che qualcuno addirittura lo sospettava anche di un po' di intrallarsi con la magia,

**Proposed:** tanto dotto che qualcuno addirittura lo sospettava anche di un po' di intrallazzi con la magia,

**Reason:** Likely noun intrallazzi (dealings), but current intrallarsi might represent an unusual spoken form; no listening evidence. Alternative: retain the current phrase and translate the evident suggestion of dabbling in magic.

**Before (U-00159):** Era un grande erudito, un grande dotto,

**After (U-00161):** si chiamava Gerberto di Oriac 1º di diventare papa,

**Provider tokens:** tanto (1.000), dotto (0.993), che (0.999), qualcuno (1.000), addirittura (0.999), lo (0.997), sospettava (0.999), anche (1.000), di (0.997), un (1.000), po' (0.994), di (0.982), intrallarsi (0.978), con (0.991), la (0.999), magia, (0.859).

### TU-050 · U-00169 · original 10:37.190–10:39.190

[Original audio excerpt with adjacent utterances](/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/source-clips/U-00169.mp3). Clip prepared by coordinator; not listened to in this review.

**Current:** l'altro è un laico, e Renzone

**Proposed:** l'altro è un laico, Erenzone

**Reason:** Tentative name boundary: e (confidence 0.487) plus Renzone (0.782) may be the single personal name Erenzone. Ermenzone/another spelling cannot be ruled out from these tokens. Need user wording or listening; no historical identification assumed.

**Before (U-00168):** uno è un prete, Ad Alberto,

**After (U-00170):** sono 2 piccoli imprenditori,

**Provider tokens:** l'altro (1.000), è (0.975), un (1.000), laico, (0.853), e (0.487), Renzone (0.782).

### TU-060 · U-00205 · original 12:56.815–13:02.015

[Original audio excerpt with adjacent utterances](/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/source-clips/U-00205.mp3). Clip prepared by coordinator; not listened to in this review.

**Current:** Dunque, la garanzia sta a contratto. Viviamo queste terre per 29 anni.

**Proposed:** Dunque, la garanzia sta a contratto. Vi diamo queste terre per 29 anni.

**Reason:** Strong contextual hypothesis: the abbot says Vi diamo queste terre per 29 anni. Provider Viviamo scores 0.918 but is incoherent with a grant/lease. Keep sta a contratto as spoken; do not polish it without evidence.

**Before (U-00204):** fa comodo al padrone averli lì per 29 anni ma anche a loro fa comodo è una bella garanzia per il contadino

**After (U-00206):** Se nell'arco di questi 29 anni qualche mio successore abate dovesse cercare di riprendersele,

**Provider tokens:** Dunque, (0.974), la (1.000), garanzia (1.000), sta (0.998), a (1.000), contratto. (0.957), Viviamo (0.918), queste (0.998), terre (1.000), per (1.000), 29 (0.999), anni. (0.977).

### TU-270 · U-00253 · original 16:37.370–16:49.115

[Original audio excerpt with adjacent utterances](/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/source-clips/U-00253.mp3). Clip prepared by coordinator; not listened to in this review.

**Current:** penité, niente. Dobbiamo pensare che nel medioevo erano gente così laica e disinvolta

**Proposed:** penitenziali, niente. Dobbiamo pensare che nel medioevo erano gente così laica e disinvolta

**Reason:** Likely completion of movimenti penitenziali from previous utterance. Could instead be a cut-off penite…; do not infer a fully spoken word from syntax alone.

**Before (U-00252):** c'era il terrore dell'anno 1000, c'eran le folle, c'eran dei movimenti,

**After (U-00254):** che della fine del mondo non gli importava niente? No, evidentemente, l'abbiamo appena visto, della fine del mondo gli importava.

**Provider tokens:** penité, (0.824), niente. (0.944), Dobbiamo (1.000), pensare (1.000), che (0.999), nel (1.000), medioevo (0.702), erano (0.999), gente (1.000), così (1.000), laica (1.000), e (0.999), disinvolta (0.998).

### TU-145 · U-00502 · original 31:08.560–31:18.800

[Original audio excerpt with adjacent utterances](/home/user/data/barbero/editorial/013-la-paura-dell-anno-mille/source-clips/U-00502.mp3). Clip prepared by coordinator; not listened to in this review.

**Current:** il vescovo si consulta con altri vescovi decidono a questa una bella bastonatura non gliela toglie nessuno la fanno frustare sulla pubblica piazza e poi fuori dai piedi e che non più farsi sentire

**Proposed:** il vescovo si consulta con altri vescovi decidono a questa una bella bastonatura non gliela toglie nessuno la fanno frustare sulla pubblica piazza e poi fuori dai piedi e che non osi più farsi sentire

**Reason:** Tentative missing verb osi in the ban on further preaching. Alternatives include deve / venga a; current token stream cannot choose. Preserve current text unless user accepts a full reconstruction or supplies heard wording.

**Before (U-00501):** dicendole tu vai in giro a predicare che l'anno prossimo viene la figlia del mondo vedrai la gente quanti regali ci porta e infatti è proprio successo così

**After (U-00503):** e così viene come dire spento il movimento millenneristico di magonza dell'anno 847

**Provider tokens:** il (0.454), vescovo (0.981), si (1.000), consulta (1.000), con (1.000), altri (1.000), vescovi (0.999), decidono (0.987), a (0.454), questa (0.990), una (0.882), bella (1.000), bastonatura (0.999), non (0.957), gliela (0.928), toglie (0.983), nessuno (0.995), la (0.992), fanno (1.000), frustare (0.998), sulla (0.991), pubblica (0.999), piazza (0.998), e (0.998), poi (0.997), fuori (1.000), dai (0.998), piedi (1.000), e (0.994), che (0.999), non (0.999), più (0.996), farsi (0.998), sentire (1.000).

## Provisional ordered chapter plan

This plan is preparatory, not an assembled or approved chapter map. Its ranges cover all 907 utterances once in source order, including every aside. No compression quota. Chapter boundaries can be refined after the source decisions.

| Chapter | Inclusive range | Original time span | Narrative work and material to preserve |
|---|---|---|---|
| CH-001: The familiar terror and the precise claim | U-00001–U-00069 | 00:35.400–04:53.075 | Introduce invented medieval images and contrast this episode with the other two series subjects. Retain surprise, friends’ reactions and qualifications: apocalyptic expectations existed; the disputed claim is Europe collectively stopping before 1000. |
| CH-002: Romantic witnesses: Carducci and Lavallée | U-00070–U-00129 | 04:54.115–08:17.765 | Read the sunrise drama, rhetorical questions and lamenting crowds; preserve Carducci’s literary skill, Lavallée’s translated catalogue and Odifreddi joke. Establish what nineteenth-century writers believed. |
| CH-003: What people actually planned in 999 | U-00130–U-00240 | 08:19.045–15:49.100 | Sylvester II and Fulda’s future privileges/rent, Gerbert’s magical reputation; Tortona’s brothers and 29-year lease; spit/handshake versus notarial Italy, sharecropping and Ermanno Olmi aside; Farfa’s imperial privilege, retired adviser/abbot joke, and eventual judgment without a next-year deadline. |
| CH-004: Chronicles, Revelation, and millenarian reasoning | U-00241–U-00334 | 15:49.580–21:22.300 | Contemporary annalists’ silence versus certainty about the eventual end; universal chronicler can leave blank pages before a known ending; vivid Revelation 20 reading and explanation; modern sects/Texas/property/suicide aside; distinguish the number 1000 from a securely predicted calendar year. |
| CH-005: Abbone’s memories of failed predictions | U-00335–U-00417 | 21:23.020–26:34.120 | King Robert, mistaken creed and Advent calculations; young Abbone rebuts a Paris preacher; Richard and Lorraine letters; Good Friday/Annunciation coincidence, perpetual-calendar digression, and mock technical term fregnacce; conclude that a memory of predictions is not collective paralysis in 999. |
| CH-006: Why churchmen rejected prediction | U-00418–U-00503 | 26:34.200–31:30.205 | Matthew, Paul, Augustine and unknowability; gospel to all peoples first; Thiota’s 847 prophecy, gifts and priest-accomplice dialogue, episcopal beating and expulsion. Preserve the social-class observation and coercive ending. |
| CH-007: A legend accumulates a line at a time | U-00504–U-00620 | 31:30.205–38:32.970 | Historian’s embarrassment and Odifreddi/mathematician callback; genealogy of additions: Sigebert’s prodigies, Guillaume Godel in 1010, Trithemius and Renaissance assumptions; authorial credibility aside and copying over centuries. |
| CH-008: A national culture needs its beginning | U-00621–U-00724 | 38:33.930–43:25.580 | Eighteenth-century documentary history; nations and vernacular literatures, troubadours, cathedrals; Bettinelli’s title and long quotation; release from fear as origin story, with Carducci callback and teasing the audience’s memory. |
| CH-009: Ideology can produce the wrong history | U-00725–U-00807 | 43:25.660–48:59.131 | Carducci’s anticlerical politics, nineteenth-century church and modernity in their context; Dom Plaine’s debunking as a partisan intervention; Barbero’s explicit personal judgment that his ideological allies produced bad history while their opponents got this question right. |
| CH-010: Modern polemics and the survival of myths | U-00808–U-00907 | 48:59.451–54:37.375 | Gouguenheim, Duby and distinctions within millenarian debate; Peggy/ancestry aside; Aristotle at Mont Saint-Michel and the role of Arabic learning, conflicting scholarly reactions and Barbero’s partial-reading disclaimer; attribution of provocative claims, return to why useful myths survive; adapt first-lecture/tomorrow references to this series finale without cutting conclusion. |

The inclusive proposed ranges were checked against all ordered transcript IDs: every utterance appears exactly once, with unique sequential CH-001–CH-010 IDs and valid endpoints. This check verifies only this provisional plan. No claim is made about an absent assembled Italian script.

## Research targets and editorial carry-forward

The following targets retain lecture wording pending research and editorial decisions. This source pass did not browse historical evidence. Allocate stable Q/C identifiers in the later brief/ledgers; there are no pre-existing ones in this episode.

| Source range | Evidence needed |
|---|---|
| U-00070–00107 | Carducci’s first discourse on national literature: distinguish direct excerpts, Barbero’s connective paraphrase, “Mille e non più mille” attribution, and the quoted Revelation wording. Do not silently replace Barbero’s wording with a preferred edition. |
| U-00109–00126 | Lavallée title/edition/date 1844, relationship to Michelet, exact French source and Barbero’s expressly rough translation. Preserve Odifreddi aside unless an editorial decision says otherwise. |
| U-00135–00161 | Sylvester II/Fulda privilege dated 31 December 999, recurring twelve-denarius payment, later election confirmation; Gerbert of Aurillac’s reputation. |
| U-00163–00208 | Tortona/San Marziano 999 lease: brothers’ names, 29-year duration, rent fractions and twenty-soldi penalty. Distinguish transcription uncertainty about name/verb from evidence about the document. Research sharecropping/San Martino and Olmi context as needed for accessible English. |
| U-00209–00240 | Otto III’s Farfa diploma, 3 October 999, inalienability, res publica and final judgment language. Separate reported quotation from comic invented administrative dialogue. |
| U-00241–00334 | Limits of argument from chronicle silence; Revelation authorship/date and 20:1–7 selection; millenarian terminology and modern-sect aside without inventing a named event. |
| U-00335–00417 | Abbone’s work/date/addressee, Paris prediction and Lorraine letter, Richard, creed/Advent details, and actual calendar coincidences. A disputed historical year is not a transcript correction. |
| U-00418–00503 | Matthew 24:36, 1 Thessalonians 5, Augustine passage and gospel-to-all-peoples argument; annal account of Thiota, exact year, Mainz proceeding and punishment. |
| U-00504–00620 | Sigebert of Gembloux, earthquake/comet/serpent and dating; Guillaume Godel’s 1010 entry; Trithemius and dependence on earlier chronicles. Preserve the distinction between a chronicler’s reported prodigies and later inferred collective terror. |
| U-00621–00724 | Bettinelli title/edition/date 1773 and all quoted passages; source of the national-literature turning-point argument; direct versus inferred influence on Carducci. |
| U-00725–00807 | Carducci’s Hymn to Satan and anticlerical poetry, nineteenth-century church/modernism chronology, Dom Plaine’s article/date 1873 and the “first” claim. Keep Barbero’s opinion attributed and avoid flattening historical nuances. |
| U-00808–00907 | Gouguenheim’s two books and publication chronology, Duby and millenarian scholarship, precise support for the inflammatory attributed Arabic-language/science claims, and the difference between reading selected pages and reading the book. Peggy comparison and guessed ancestry require an explicit editorial decision if altered. |

Production context: episode 013 concludes **Unbelievable Middle Ages**, following 014 **The Right of the First Night** and 015 **Flat Earth**. Source opening U-00001–00016 and closing U-00905–00907 describe the first live lecture; adapt unambiguous lecture-relative sequencing later for the actual release order. The source title remains `La paura dell’Anno Mille: Medioevo da non credere`; an English audience title needs its own decision. Do not silently convert “very recently” (U-00819), “five years ago” (U-00856), or “next book” (U-00890) into verified chronology. Preserve the intended claims and route discrepancies through evidence/editorial decisions.

014’s approved accessible vocabulary and restored dialogue/uncertainty are useful style context; its accepted Du Cange cut does not authorize any analogous cut here. This episode must retain argument, uncertainty, dialogue, jokes, and digressions unless the user makes a new substantive editorial decision.

Coordinator research handoff (source assertions unchanged): investigators report questions about the Apologeticus date/addressees and creed example, Godel’s Cistercian identification, and the order of Gouguenheim’s books. These are historical evidence/editorial issues, not grounds to substitute different source words or resolve this transcription queue.

## Source decision update — 2026-10-02

The user explicitly accepted all five tentative repairs (U-00160, U-00169, U-00205, U-00253, U-00502). Their exact complete proposed utterances are now recorded as resolved text in the uncertainty queue. The other 104 changed-text proposals and 195 unchanged items remain pending; no broader acceptance is inferred. This update records text acceptance, not performed audio review. The transcript has not been rerendered while any items remain pending, because the renderer applies source resolutions only once the complete queue is settled.

Updated uncertainty queue SHA-256: `5aef11b59482c73af643fd03647b3b4057d6f6de31f97503dafa10241ec38a1c`. Original review hashes above remain the scan provenance.

## Settled source verification — 2026-10-02

The user also accepted the remaining source package through the explicit question reply. All 304 queue items are resolved with exact complete utterance text and decision provenance. Rerendered transcript contains all 907 ordered IDs, no pending review flags, and exactly the deterministically resolved provider text. Ten chapters cover each utterance once; assembled Italian wording and punctuation equal the settled transcript after whitespace normalization. No audio/performed listening was assessed. Source preparation parser repair: provider word objects are preserved during named-entity detection; ruff formatting/lint and 12 relevant pytest tests passed.

Deterministic verification was run via `uv run --no-sync python` using `validate_transcript_uncertainties`, `resolve_utterances`, ordered ID/range comparison, and per-chapter exact normalized spoken-text comparison.

- `episode.yaml`: `5135c3e3260e8b327deb09961776ac39cfb878201738d687345b68ab51ef4c06`
- `transcript.it.md`: `f17641ad0a1f0c7b400b6d34098bda2a6628dc6db079deb880a1d26271d73e73`
- `script.it.md`: `40d4433f29e3d0da07235e91730b9ba487954ec6d39fd53e0ff19f21ec209bb9`
- `chapters.yaml`: `e6b5821f83b5fafd7e2c1804ed0aeb3412c6271eb7437bb127add83e1648efdd`
- `transcript-uncertainties.yaml`: `c95fd0007c659a64cd01c80c2651f5e67cccb6c5ba392a4ae4aa99457c868f94`
