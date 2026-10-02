# Source review — 019 Il frate

## Confirmed source decisions — 2026-10-02

The user confirmed the spoken birth range **1220–1230** (TU-053/054), that the lecture ends after **Grazie** (TU-317), and the wording **non credere “istis pissintunicis, id est qui in tunicis mingunt”** (TU-349/350). These five complete-utterance resolutions are now saved in the queue. The date range and Latin quotation span their existing utterance boundaries. No printed-source Latin substitution was authorized.

The other 374 resolutions remain pending: the user supplied Latin wording in answer 3 and did not explicitly approve the remaining repair batch. The initial scan and hashes below describe the pre-decision review snapshot; no unheard audio is claimed reviewed. Rendering remains deferred because the existing renderer applies source resolutions only once the entire queue is resolved.

Updated queue SHA-256: `81ab163a936d19d08885b15aaa487df1ca466e2c2084c034d6a4f9bc80f1bd97`.

Full contextual scan completed on 2026-10-02: all 825 utterances (U-00001–U-00825), 9,462 provider words, read in narrative order. This was a text and provider-artifact review. No audio was listened to and no utterance is claimed reviewed against audio.

The queue retains every original TU-001–TU-317 identifier, original reason (including every acoustic word confidence), timestamp, current_text and pending resolution. It now contains 379 items. New IDs follow TU-317 in source order. detection_status is complete for contextual detection only; source resolution is still pending. No spoken transcript, Italian script, final chapters or English adaptation was changed or created.

SPEAKER_01 is already selected, matching the explicit longest-duration preference. The edit map records SPEAKER_01 = 3138.028493 seconds and SPEAKER_00 = 63.7603002 seconds of diarized speech. Retained audio is 3505.134759 seconds including the saved segment padding/gaps. These data establish the chosen speaker, not perfect speaker separation.

## Checks actually completed

- Reconstructed all utterances and word timestamps from deepgram.json using utterances_from_deepgram and the saved edit map; all 825 IDs and complete texts match transcript.it.md exactly.
- Recomputed the transcription fingerprint from the actual cleaned.flac SHA-256 plus manifest options using the existing object_hash convention; it equals both manifest and uncertainty queue.
- validate_transcript_uncertainties returns no errors. Stable IDs, exact old reasons, resolutions, current_text and timestamps were compared with the pre-review queue and preserved.
- All proposed_text values are complete utterances. Every resolution remains pending, with resolved_text null. Proposals have not been applied.

## Decision groups

1. **Routine recognition repairs:** recurring Salimbene variants, obvious word segmentation (questua, sporta, villania, luccio, pie), and omitted auxiliaries. Consider these as one source repair batch rather than separate material editorial decisions. Exact individual utterances appear below and in YAML. These repairs are contextual proposals, not claimed auditory confirmation.
2. **Individual source choices:** Diotisalvi, Eco, the father’s Latin insult, French place names, and the closing fragment. Approve exact wording only with the distinctions in each note.
3. **Retained wording requiring attention:** the 1220 / 30 birth-date phrase and caboli cannot be safely reconstructed from historical knowledge alone. The intelligible Latin insult caccarelli et merdazzoli and opening false start remain as transcribed pending any further evidence.

The generated queue also flags ordinary capitalized words (including I, E, Però and sentence openings), known names correctly recognized, low-confidence fillers, and “1000 persone” as a date. A flag alone is not a demonstrated wording defect. After reading those passages in context, this scan proposes no change to the remaining original items listed below. Their acoustic flags and pending states are preserved; a user may accept the complete current_text unchanged as one batch. Do not record that acceptance until supplied.

Unchanged generated items with no specific textual correction proposed: TU-001, TU-002, TU-003, TU-004, TU-006, TU-007, TU-008, TU-009, TU-010, TU-011, TU-012, TU-013, TU-014, TU-015, TU-017, TU-020, TU-021, TU-022, TU-023, TU-024, TU-025, TU-027, TU-028, TU-029, TU-031, TU-032, TU-033, TU-034, TU-035, TU-036, TU-037, TU-038, TU-039, TU-041, TU-043, TU-044, TU-046, TU-047, TU-048, TU-049, TU-051, TU-055, TU-056, TU-057, TU-058, TU-059, TU-060, TU-061, TU-062, TU-063, TU-064, TU-065, TU-066, TU-068, TU-069, TU-071, TU-072, TU-074, TU-077, TU-078, TU-080, TU-081, TU-082, TU-083, TU-085, TU-087, TU-088, TU-089, TU-090, TU-092, TU-093, TU-094, TU-095, TU-097, TU-098, TU-099, TU-100, TU-102, TU-103, TU-104, TU-105, TU-106, TU-107, TU-108, TU-109, TU-112, TU-113, TU-115, TU-116, TU-117, TU-120, TU-121, TU-122, TU-124, TU-126, TU-127, TU-128, TU-129, TU-130, TU-131, TU-133, TU-134, TU-138, TU-140, TU-141, TU-142, TU-143, TU-144, TU-145, TU-146, TU-147, TU-148, TU-149, TU-150, TU-152, TU-154, TU-155, TU-156, TU-157, TU-158, TU-159, TU-160, TU-161, TU-162, TU-163, TU-164, TU-165, TU-166, TU-168, TU-169, TU-170, TU-171, TU-172, TU-173, TU-177, TU-178, TU-179, TU-183, TU-184, TU-185, TU-186, TU-188, TU-189, TU-190, TU-191, TU-192, TU-194, TU-195, TU-196, TU-197, TU-198, TU-199, TU-200, TU-202, TU-204, TU-208, TU-210, TU-211, TU-212, TU-214, TU-216, TU-217, TU-219, TU-220, TU-221, TU-223, TU-226, TU-227, TU-228, TU-230, TU-232, TU-234, TU-235, TU-236, TU-237, TU-238, TU-239, TU-242, TU-243, TU-244, TU-246, TU-247, TU-248, TU-251, TU-252, TU-253, TU-254, TU-255, TU-256, TU-259, TU-268, TU-271, TU-272, TU-273, TU-275, TU-276, TU-277, TU-280, TU-281, TU-282, TU-284, TU-285, TU-286, TU-287, TU-288, TU-290, TU-291, TU-293, TU-294, TU-295, TU-296, TU-297, TU-298, TU-299, TU-300, TU-301, TU-302, TU-303, TU-304, TU-305, TU-307, TU-308, TU-311, TU-312, TU-313, TU-314, TU-315.

Provider formatting remains: numeric “200” denotes the Duecento/thirteenth century in context; “1º”, “2º”, “6” often stand for prima/primo, secondo or sei. These intelligible normalization artifacts are not proposed historical edits. Uppercase I, rough punctuation, repetitions, truncated clauses, false starts and oral agreement are retained unless an exact correction is listed.

Historical claims retained for later evidence work include Fano “in Romagna”, Aigues-Mortes “in Provenza”, the 1220 / 30 birth-date wording, Louis IX’s journey on foot, the royal and patriarchal menus, the infant experiment, and the interpretation of ravioli without a crust. No historical finding has been silently substituted into the source.

## Supporting textual evidence and listening targets

- [Cantarelli’s 1882 translation](https://www.gutenberg.org/cache/epub/61304/pg61304-images.html) identifies Diotisalvi da Fiorenza (vol. I pp.54–55), Sens (pp.126–130), and the dialect expression Ke bulì? (around p.251). These support identification only; they do not establish Barbero’s precise utterance.
- [Bernini’s Latin text, Pars I](https://la.wikisource.org/wiki/Cronica_(Salimbene_de_Adam)/Pars_I) places Salimbene’s birth in 1221. This is evidence about history, not permission to replace 1220 / 30 in the recording transcript.
- [Bernini’s Latin, vol. I p.54](https://la.wikisource.org/wiki/Pagina:Salimbene_de_Adam_–_Cronica,_Vol._I,_1942_–_BEIC_1910163.djvu/60) attests the father’s insult and explanatory gloss. The evidence worker supplied this primary-text finding after the initial scan; it does not settle the recording’s credere/credas wording.
- Unheard review clips prepared by the coordinator: /scratch/audio_clip/barbero-019/birth-date.mp3 (original 694–714s); latin-insult.mp3 (2080–2105s); closing.mp3 (3646–3678s).
- The tail “Vagdaver Custis,” occupies provider word times 3672.092241–3673.495 in the final retained segment. A candidate deletion is listed, but the text could represent speaker leakage, a genuine final aside, or unrecognized audio; timing alone cannot decide.

## Candidate narrative map

These are planning boundaries only, covering the entire current source once in order. Do not treat them as finalized chapters until source choices are settled.

| Candidate | Inclusive utterances | Original seconds | Narrative work |
|---|---|---|---|
| 1 | U-00001–U-00048 | 45.745–251.075 | Opening: recover a person from his writing; introduce Salimbene and the enormous chronicle. |
| 2 | U-00049–U-00136 | 252.040–622.080 | An ordered world, scripture as its manual, trained memory, public disputes and scarce books. |
| 3 | U-00137–U-00263 | 622.800–1159.085 | Prediction and disappointment: Joachim, Frederick as Antichrist, the weaver prophet and erased books; individual censorship. |
| 4 | U-00264–U-00352 | 1161.565–1551.125 | Latin as elite identity; the devil’s grammar; pride, Giovanni da Vicenza and Diotisalvi’s latrine prank. |
| 5 | U-00353–U-00412 | 1551.365–1777.295 | Franciscan solidarity, rivalry with Apostolics, Segalelli’s garbled slogan and the Eco aside. |
| 6 | U-00413–U-00529 | 1777.775–2271.185 | The cost of choosing the friars: noble lineage, the father’s intervention, confrontation, curse, consoling dream and possible bishopric. |
| 7 | U-00530–U-00571 | 2271.905–2442.990 | Begging at Pisa, shame before a compatriot, dream of the begging Virgin and child, and the cabbage punchline. |
| 8 | U-00572–U-00621 | 2444.405–2670.600 | Noble values survive the vocation: courtesy versus boorishness, the unbelieving bishop, generous archbishop and rude Brother Elias. |
| 9 | U-00622–U-00669 | 2670.680–2900.005 | Food and wine as measures of generosity: English king, selfish bishops, Burgundy and French drinking. |
| 10 | U-00670–U-00739 | 2901.540–3214.145 | Louis IX on pilgrimage, the pike gift and royal meal, contrasted with Aquileia’s Lenten menu. |
| 11 | U-00740–U-00769 | 3214.145–3362.795 | Regional prejudice and language: southern insults and pronouns; Lombards’ indiscriminate voi. |
| 12 | U-00770–U-00803 | 3364.250–3537.960 | Curiosity about ravioli, climates, days and French women; observation through inherited social values. |
| 13 | U-00804–U-00825 | 3538.440–3673.495 | Frederick’s infant experiment; Salimbene’s humane understanding; closing return to the whole person. |

Preserve the arc from initially alien confidence and arrogance through costly vocation and class prejudice to curiosity and the humane final contrast. Preserve the funny and bodily examples, self-interruptions and unresolved ravioli interpretation. Do not equate digressions with expendable material.

## Exact proposed utterances

The following texts are proposals only. Original timestamps use the saved edit map; they are interval endpoints and may span removed gaps. ID stability follows YAML. An unchanged proposal means retain current wording while its noted question remains open.

### Individual source choices

**TU-111 · U-00321 · original 1398.135–1407.680s**

> Frate Diotisalvi da Firenze. E Salimbene dice, questo è molto interessante, si sa che ai fiorentini piace sfottere, piace beffare, che sono dei gran burloni.

Context and Cantarelli identify Diotisalvi da Fiorenza. The extra provider words “da sfida a” remain acoustically unverified; proposed complete sentence is provisional.

**TU-114 · U-00325 · original 1418.785–1423.425s**

> dice Salimbene con grande divertimento e approvazione, il nostro frate Diotisalvi

Same friar as U-00321; normalize the recognized name, pending source approval.

**TU-119 · U-00332 · original 1458.245–1461.285s**

> mangiano. Dopo avere ben mangiato, frate Diotisalvi,

Same friar as U-00321; normalize the recognized name, pending source approval.

**TU-123 · U-00341 · original 1491.890–1496.530s**

> Il frate Diotisalvi va alla latrina e naturalmente poi si pulisce con

Same friar as U-00321; normalize the recognized name, pending source approval.

**TU-153 · U-00411 · original 1768.415–1775.135s**

> Ecco, Eco ha attinto a piene mani a Salimbene per il nome della rosa. E dunque...

U-00408 names Umberto Eco; the second “ecco” is probably Eco, the subject of attinto. Contextual reconstruction, not listened audio.

**TU-349 · U-00489 · original 2093.005–2095.805s**

> Non credere istis pissintunicis,

Bernini 1942, vol. I p.54, attests “non credas istis pissintunicis” and the gloss “id est qui in tunicis mingunt”. Proposed_text repairs only the word boundary in pissintunicis and retains provider “Non credere”. Changing this to “Non credas istis pissintunicis,” is a separate exact alternative requiring listening or explicit approval of source-based Latin restoration; a printed edition does not establish Barbero’s wording.

**TU-350 · U-00490 · original 2096.205–2099.005s**

> Id est qui in tunicis mingunt,

Latin explanatory formula id est, followed by qui in tunicis mingunt; clear word-boundary recognition defect.

**TU-180 · U-00491 · original 2099.085–2102.800s**

> cioè che orinano spiega.

Immediately glosses mingunt; orinano is the contextual proposal. Urinano remains a plausible alternative requiring audio/user wording.

**TU-263 · U-00677 · original 2932.720–2945.365s**

> profonda per chi riesce a essere santo. Ecco il Re Luigi era uno così. Il Re Luigi è andato in crociata, è partito dalla Francia del Nord per andarsi a imbarcare a Aigues-Mortes in Provenza, ha attraversato tutto il regno

Proposed spelling of the embarkation port; retain Barbero’s “in Provenza” pending separate historical research, rather than changing the geography here.

**TU-265 · U-00685 · original 2974.950–2980.070s**

> Una volta stavano uscendo dalla città di Sens, incontro al re, il re arriva,

Same Louis IX reception as U-00686 and U-00795; Sens attested in Cantarelli, volume I pp.126–130. This supports the place spelling, not proof of the uttered sounds.

**TU-367 · U-00686 · original 2980.470–2983.750s**

> e il vescovo di Sens gli manda un regalo.

Same Louis IX reception as U-00685; bishop/archbishop wording remains as spoken in transcript.

**TU-306 · U-00795 · original 3480.320–3498.285s**

> Si trova in Francia, sempre durante il suo grande viaggio quando era giovane, ad accogliere il re fuori dalla città di Sens, e dice dalla città di Sens è uscita la processione delle dame della città ad accogliere il re. Io le ho guardate, m'han detto, guarda le dame della città, le ho guardate e mi son detto, a me mi sembran più delle cameriere queste.

Repeated place name in the account of the women greeting Louis IX; contextual spelling proposal linked to U-00685–00686.

**TU-317 · U-00825 · original 3648.062–3673.495s**

> E io spero insomma un pochino di avere trasmesso qualche cosa di questo stasera. Grazie.

Candidate removes only the unrecognized closing fragment. Source content/speaker status unknown; the retained edit segment at original 3671.895–3673.495 follows a gap after 3652.025. Timing is no proof of another speaker or an outro. Requires user decision or listening; no removal applied.


### Unsettled or deliberately retained wording

**TU-005 · U-00014 · original 120.220–123.100s**

> Ovviamente questo è l'obiezione viene fuori subito.

Possible false start “questo è…” rather than a recognition error. Retain exactly; no semantic consequence demanding a rewrite.

**TU-053 · U-00158 · original 698.135–703.910s**

> ci ho creduto a lungo. Salimbene è nato intorno al 1220

Birth-date phrase continues in U-00159 as “30.” Keep 1220 and 30 pending listening/user confirmation; historical 1221 is not evidence of what Barbero said. Proposed_text changes only the already established name.

**TU-054 · U-00159 · original 703.910–704.550s**

> 30.

Continuation of birth date: provider has “30.” Could be an approximate 1220–30 range or a spoken correction; no evidence yet. Complete-utterance candidate remains “30.”; do not infer 1221.

**TU-370 · U-00751 · original 3279.360–3284.325s**

> caccarelli et merdazzoli.

Latin/dialect insult in preceding “Sunt homines”: current “caccarelli et merdazzoli” is intelligible. Critical spellings may differ; retain the lecture form until quotation evidence and source decision establish a change.

**TU-371 · U-00755 · original 3293.205–3294.485s**

> Dicono caboli.

Provider “caboli” is a cited southern dialect expression, not ordinary Italian cavoli. Cantarelli prints “Ke bulì?”; that text does not prove Barbero’s sounds. Keep current complete utterance pending listening or explicit dialect spelling decision.


### Routine recognition repairs

**TU-318 · U-00002 · original 68.220–71.340s**

> dal punto di vista climatico, un po' meno gradevoli del solito.

**TU-319 · U-00016 · original 126.115–130.835s**

> Un cavaliere che ha scritto un libro, non era proprio uguale a tutti gli altri cavalieri.

**TU-320 · U-00017 · original 131.075–133.955s**

> Un mercante che ha scritto un libro, peggio che mai.

**TU-321 · U-00024 · original 167.860–172.100s**

> perché dei 3, il frate è quello che ha scritto il libro più grosso.

**TU-322 · U-00027 · original 183.375–184.815s**

> ha scritto una cronaca

**TU-323 · U-00033 · original 196.710–200.230s**

> Scegliere nel mare di cose che quest'uomo ci ha raccontato,

**TU-016 · U-00043 · original 231.480–235.400s**

> e sotto molti aspetti la sua mentalità, il suo modo di ragionare,

**TU-018 · U-00056 · original 280.060–284.140s**

> Ma di per sé il mondo è ordinato perché Dio l'ha costruito così.

**TU-324 · U-00057 · original 284.460–288.460s**

> C'è questa profonda fiducia nel fatto che il mondo ha una sua logica,

**TU-019 · U-00058 · original 288.860–290.380s**

> l'ha costruito Dio,

**TU-325 · U-00059 · original 291.100–292.940s**

> e Dio ha dato anche all'uomo

**TU-026 · U-00080 · original 365.990–373.830s**

> rispetto a noi. La Bibbia la sa a memoria e del resto dovevano saperla a memoria perché Salimbene non è un frate qualunque, è un predicatore.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-030 · U-00085 · original 396.260–399.060s**

> doveva convincere la gente che la Chiesa ha ragione,

**TU-326 · U-00106 · original 462.795–466.075s**

> Salimbene, a un certo punto cita una canzonetta satirica,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-040 · U-00127 · original 556.540–559.420s**

> Salimbene a un certo punto dice, sì, quando io ero giovane

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-327 · U-00132 · original 578.555–587.000s**

> Ecco, in queste condizioni, l'unico magazzino che uno ha a disposizione è la testa. E nella testa fa entrare tutto quello che può entrarci.

**TU-042 · U-00133 · original 587.000–596.615s**

> Quindi, uno come Salimbene, la Bibbia la sa a memoria. Sapere a memoria la Bibbia vuol dire sapersi orientare nel mondo, avere tutte le risposte pronte.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-045 · U-00138 · original 625.760–628.640s**

> E questa è una cosa che a Salimbene interessa tantissimo.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-328 · U-00143 · original 644.895–647.615s**

> è un manuale per prevedere anche il futuro.

**TU-050 · U-00150 · original 671.655–674.375s**

> La Chiesa ufficialmente non ha mai detto sì, è vero,

**TU-329 · U-00151 · original 675.180–678.300s**

> non ha neanche mai detto, sono tutte stupidaggini.

**TU-052 · U-00154 · original 683.740–688.220s**

> come si diceva, cioè quelli che credevano a questo sistema. E Salimbene che scrive da vecchio,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-330 · U-00171 · original 749.010–751.250s**

> Salimbene da giovane ci ha creduto.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-331 · U-00183 · original 792.765–797.485s**

> sta già commettendo dei delitti, peggiorerà ancora. Salimbene ci ha creduto.

**TU-332 · U-00192 · original 827.360–832.400s**

> ha predicato alla gente, io ero lì sul balcone accanto a lui, lo toccavo.

**TU-067 · U-00193 · original 833.680–839.600s**

> E il Papa ha annunciato pubblicamente che l'imperatore Federico 2º era morto, dice 1250.

**TU-070 · U-00196 · original 851.445–858.220s**

> E tanti ci credono a questa cosa che si possa prevedere il futuro. Salimbene non è più gioachimita, non crede più al sistema di Gioacchino,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-073 · U-00202 · original 878.535–881.255s**

> A Salimbene a un certo punto vengono a raccontare

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-333 · U-00204 · original 891.230–893.710s**

> Questo a un certo punto ha cominciato a profetizzare

**TU-075 · U-00205 · original 894.030–896.510s**

> e le cose che diceva funzionavano

**TU-076 · U-00206 · original 896.510–902.190s**

> insomma. A un certo punto si è ritirato in un monastero, un monastero dei cistercensi, Fontevivo, fuori Parma.

**TU-079 · U-00210 · original 917.735–928.535s**

> e profetizza il futuro. Salimbene che sente raccontare queste cose e poi viene il momento che insomma non sta più nella pelle, vuole andarlo a conoscere questo.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-084 · U-00218 · original 959.000–964.520s**

> Salimbene 1º ha raccontato, quest'uomo scrive, scrive e dice testualmente Salimbene,

**TU-334 · U-00224 · original 988.540–992.780s**

> Poi invece c'è chi scrive e ha piacere che le sue cose sian conosciute.

**TU-086 · U-00227 · original 999.900–1006.305s**

> Questo profeta pubblicava volentieri le sue opere, quindi Salimbene arriva al monastero e dice, ma saran rimasti I suoi libri?

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-335 · U-00236 · original 1034.215–1040.935s**

> e che ha una sua arte particolare, è un tecnico di una cosa specifica. È un tecnico della rasa... Della cancellatura

**TU-336 · U-00246 · original 1083.530–1090.330s**

> c'era questo vecchio monaco che conosceva quell'arte e dice, io 1º o poi morirò, vorrei trasmetterla a qualcuno questa tecnica.

**TU-091 · U-00257 · original 1126.005–1135.205s**

> e la chiesa a pubblicare l'indice dei libri proibiti. Però la cosa interessante è che all'epoca di Salimbene non è ancora il potere della chiesa che impone questo.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-337 · U-00261 · original 1148.080–1150.320s**

> ognuno c'ha la responsabilità individuale

**TU-096 · U-00270 · original 1184.605–1190.525s**

> pensa anche nel suo dialetto, Salimbene, pensa nel suo dialetto di Parma, si vede benissimo dal latino che scrive, però

**TU-101 · U-00292 · original 1271.105–1287.060s**

> È solo che con la bocca di questo contadino come si fa? Ha una lingua talmente rozza che non ci riesco a parlar bene con la sua bocca. Ovviamente questo ideale, diciamo, di un'élite dotta, di un'élite culturale,

**TU-338 · U-00312 · original 1368.665–1370.505s**

> Già che c'era, ne ha approfittato

**TU-110 · U-00316 · original 1383.560–1389.240s**

> I francescani dopo un po' di questo fra Giovanni de Vicenza non ne possono più. E Salimbene racconta con grandissimo

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-118 · U-00331 · original 1453.445–1457.685s**

> Dopodiché racconta Salimbene, ripeto, con grande divertimento ed entusiasmo,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-125 · U-00345 · original 1507.065–1518.345s**

> Venite a aiutarmi a tirarla fuori. E arrivano tutti I domenicani di corsa a cercar di tirarla fuori, e lui rimesta nella latrina con un bastone per tirarla fuori, finché dopo un po' I domenicani mangiano la foglia,

**TU-339 · U-00364 · original 1582.035–1583.635s**

> Ha voluto bene ai francescani.

**TU-132 · U-00365 · original 1584.100–1606.060s**

> Quelli che hanno voluto bene ai francescani li han trattati bene e gli si perdona tutto. Perché I francescani sono comunque il meglio che ci sia. E quindi la concorrenza invece è... La concorrenza ovviamente dà fastidio. I domenicani ancora ancora, adesso ho scherzato sui domenicani, ma sono un grande ordine fratello, sono I mendicanti anche loro. Ma ce n'è ben altra di concorrenza,

**TU-135 · U-00371 · original 1625.940–1630.260s**

> E l'altra cosa che c'è ben ferma nella testa di Salimbene è che attenzione,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-136 · U-00372 · original 1630.420–1641.395s**

> perché noi francescani abbiamo un esempio preciso, San Francesco ci ha insegnato come si fa questa cosa, ma non è che il 1º venuto adesso si mette un paio di sandali e pretende di fare come noi. Questa è una vergogna,

**TU-137 · U-00374 · original 1644.355–1647.795s**

> Quando Salimbene pensa a queste cose, perde il lume dell'intelletto

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-139 · U-00380 · original 1662.040–1665.400s**

> L'ha fondato uno che si chiama frate Gerardino Segalelli.

**TU-340 · U-00387 · original 1685.400–1686.760s**

> Lui ha visto quello,

**TU-341 · U-00388 · original 1686.920–1688.920s**

> ha creduto di dover fare la stessa cosa.

**TU-342 · U-00390 · original 1690.680–1692.440s**

> ha creato questo movimento

**TU-151 · U-00408 · original 1754.980–1759.060s**

> Ecco qualcuno si ricorderà che Umberto Eco ha ripreso testualmente

**TU-343 · U-00415 · original 1800.445–1801.965s**

> ha fatto delle rinunce

**TU-344 · U-00433 · original 1883.860–1887.860s**

> quando ha saputo che suo figlio si era fatto francescano, ha dato di matto.

**TU-345 · U-00443 · original 1921.715–1922.755s**

> E Salimbene,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-346 · U-00445 · original 1925.075–1930.035s**

> ha deciso a 17 anni di mollare tutto e andare coi frati.

**TU-347 · U-00447 · original 1936.850–1940.530s**

> E infatti è stata pesante perché la famiglia ha cercato di impedirglielo.

**TU-167 · U-00459 · original 1978.245–1981.365s**

> Questo è il livello a cui si muove la famiglia di Salimbene.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-348 · U-00473 · original 2025.780–2030.020s**

> E Salimbene che racconta questa storia cinquant'anni dopo, quando ormai è vecchio.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-174 · U-00474 · original 2030.855–2033.255s**

> Salimbene racconta orgoglioso

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-175 · U-00475 · original 2033.255–2035.655s**

> di aver tenuto duro. Al Padre ha detto,

**TU-176 · U-00479 · original 2048.060–2059.020s**

> Voi immaginate, è un diciassettenne, è l'età in cui col padre si litiga furiosamente anche adesso, e si litigava furiosamente anche allora, come in ogni epoca, quell'età lì. Salimbene al padre, dice le cose peggiori, dice, no, non voglio venire.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-181 · U-00492 · original 2103.065–2116.025s**

> T'hanno incantato, t'han messo in testa queste cose, torna a casa, salimbene tiene duro. E dice, I frati dall'altra parte erano lì che tremavano come giunchi temendo che io cedessi perché se cedevo io, chissà chi altri avrebbe accettato di venire in convento. Invece io ho tenuto duro.

**TU-182 · U-00494 · original 2119.551–2125.391s**

> maledice lui e l'altro figlio, gli raccomanda il diavolo. Non lo vedrà mai più il padre. Salimbene,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-187 · U-00500 · original 2140.355–2144.790s**

> Ho avuto un sogno che mi ha fatto capire che avevo fatto bene. Evidentemente,

**TU-351 · U-00504 · original 2156.535–2157.896s**

> racconta Salimbene,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-193 · U-00512 · original 2185.076–2196.195s**

> ci sarebbe da tirarne fuori di commenti, e Salimbene, non conosceva il dottor Freud, però come dire, per lui e quindi era era davvero la vergine col bambino che gli era apparsa, perché aveva visto tutto

**TU-201 · U-00529 · original 2261.970–2271.185s**

> è importante ricordare che quest'uomo di potere va scalzo e va in giro a mendicare per vivere, E che questa cosa lui l'ha vissuta come un trauma, pesantissimo.

**TU-203 · U-00534 · original 2283.030–2288.310s**

> Era nel convento di Pisa, faceva la questua e lui racconta, mi trovavo in quella certa strada,

**TU-205 · U-00538 · original 2302.055–2304.135s**

> Dunque, faceva la questua a Pisa,

**TU-206 · U-00539 · original 2304.455–2311.790s**

> e a un certo punto ha la sfortuna che incontra davvero uno di Parma lo stesso. Dice, mi viene incontro uno che era di Parma, che io non conoscevo,

**TU-207 · U-00540 · original 2311.871–2315.391s**

> ma lui mi conosceva, perché Salimbene è di una famiglia importante,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-209 · U-00546 · original 2333.756–2337.036s**

> E poi continua e dice, Salimbene riferisce parola per parola,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-352 · U-00551 · original 2353.095–2355.255s**

> e a dar mance ai giullari.

**TU-213 · U-00554 · original 2362.215–2367.175s**

> E Salimbene quella volta, lo respinge, lo caccia via in malo modo, gli cita un po' di passi biblici.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-215 · U-00560 · original 2385.635–2396.915s**

> Sogna che è a Pisa a mendicare e a un certo punto, lì un po' più in là, nella stessa strada, c'è Gesù bambino che va anche lui con la sporta a mendicare e la vergine che va anche lei con la sporta a mendicare.

**TU-218 · U-00568 · original 2428.590–2430.030s**

> E dice Salimbene,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-353 · U-00573 · original 2447.845–2452.725s**

> figlio di una grande famiglia nobile, ha fatto una scelta che l'ha portato molto lontano dalla sua famiglia.

**TU-222 · U-00575 · original 2455.765–2467.080s**

> ha conservato alcune caratteristiche, proprio di modo di pensare di sistema di valori. E io direi che la cosa che colpisce di più leggendo Salimbene è che lui è rimasto un nobile cavaliere da un punto di vista.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-354 · U-00578 · original 2471.720–2472.760s**

> o la villania.

**TU-355 · U-00586 · original 2495.110–2501.395s**

> non il fatto che sian dei peccatori o no, perché tutti son dei peccatori, figuriamoci. Salimbene ne ha viste di tutti I colori,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-356 · U-00589 · original 2508.435–2513.475s**

> Salimbene davvero non si fa nessuna illusione, lui ha visto in vita sua di tutto, ha visto perfino un vescovo ateo,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-357 · U-00590 · original 2514.570–2516.330s**

> ha visto il vescovo di Parma

**TU-358 · U-00592 · original 2520.330–2527.530s**

> ha detto, ma no, io non li voglio, tanto non ci credo. E quando gli hanno chiesto, ma allora perché hai fatto il vescovo?

**TU-359 · U-00593 · original 2528.335–2531.135s**

> Ha risposto, beh, per le ricchezze e per gli onori.

**TU-224 · U-00594 · original 2532.495–2537.135s**

> Quindi Salimbene ha visto tutto, ha sentito raccontare di tutto su papi, arcivescovi,

**TU-225 · U-00595 · original 2537.135–2550.385s**

> podestà, imperatori, principi, re. Lui ha un intercalare preferito. Quando racconta qualcosa di veramente enorme, che gli è stato riferito di qualche personaggio importante, lui dice, ipse viderit, se la vedrà lui.

**TU-360 · U-00603 · original 2586.995–2592.195s**

> Se uno gli faceva dei regali, poi dall'arcivescovo otteneva tutto quello che voleva, appalti, concessioni,

**TU-229 · U-00604 · original 2593.555–2602.275s**

> e tuttavia... Aveva anche una figlia che ha messo in convento. Ma tuttavia l'arcivescovo di Ravenna era un gran signore, ospitale, generoso, trattava bene la gente, Salimbene l'ha conosciuto.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-361 · U-00605 · original 2602.950–2609.270s**

> Lui l'ha sempre trattato bene, lo invitava a pranzo, dava dai grandi pranzi, dava da mangiare a tutti, beveva del buon vino, ne dava a tutti.

**TU-362 · U-00607 · original 2615.575–2620.215s**

> e ogni angolo della stanza aveva una caraffina di vino in fresco

**TU-231 · U-00613 · original 2634.800–2640.160s**

> che un giorno, quando un gran signore è andato a trovarlo, frate Elia, l'ha ricevuto seduto a tavola

**TU-233 · U-00617 · original 2654.325–2655.845s**

> Questa dice Salimbene, ecco.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-240 · U-00631 · original 2708.925–2712.125s**

> Qual è un comportamento che Salimbene giudica fantastico?

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-241 · U-00632 · original 2713.290–2726.090s**

> Gli hanno raccontato che il re d'Inghilterra un giorno era a fare un picnic. Picnic lo diciamo noi, ma insomma era in campagna, si era messo a mangiare su un prato con I suoi cavalieri, portano il vino, sono vicino a una fontana. Di vino c'è soltanto un fiasco.

**TU-245 · U-00643 · original 2768.170–2778.945s**

> Quando dice Salimbene berrebbero tutti volentieri perché tutte le gole sono sorelle. Sul vino potremmo continuare perché il vino è un tema importante appunto.

**TU-249 · U-00648 · original 2792.800–2794.800s**

> Poi ha fatto un lungo viaggio in Francia,

**TU-250 · U-00649 · original 2795.335–2799.015s**

> che racconteremo adesso, finiremo con quello, ha fatto un lungo viaggio in Francia,

**TU-363 · U-00651 · original 2801.815–2802.695s**

> e ha visto.

**TU-257 · U-00659 · original 2835.315–2838.995s**

> Certo poi dice Salimbene, I francesi esagerano perché I francesi son degli sbevazzoni,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-258 · U-00665 · original 2856.765–2887.765s**

> in cui lui ha fatto le abluzioni rituali, che gliela metta negli occhi per piacere, perché pensano che con quell'acqua consacrata gli guariscono gli occhi rossi per il troppo bere. E io, dice salimbene, una volta quando ero in Francia, ho conosciuto un frate che quando uno è venuto a chiedergli l'acqua da mettere negli occhi, gli ha detto, ma va via, mettete l'acqua nel vino, non negli occhi. Dopodiché, sapete come sono organizzati I francescani in Francia? Salimbene lo sa e ce lo dice. Dice, la provincia di Francia dell'ordine francescano è divisa in 8 custodie,

**TU-364 · U-00670 · original 2901.540–2904.340s**

> Ora, il cibo ha una funzione simbolica, è evidente.

**TU-260 · U-00672 · original 2908.340–2911.300s**

> Salimbene ha fatto questo viaggio in Francia di cui vi parlavo,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-261 · U-00673 · original 2911.540–2921.035s**

> e durante questo viaggio in Francia ha avuto tante avventure, ha conosciuto tanta gente, ha incontrato più volte il re Luigi, Luigi 9º il santo che proprio allora andava in crociata.

**TU-262 · U-00674 · original 2921.275–2928.795s**

> Questa è stata un'esperienza grossa perché Salimbene anche se è uno disilluso non si aspetta niente dalla gente, sa che succede il peggio, però sa riconoscere

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-365 · U-00676 · original 2931.600–2932.720s**

> e ha un'ammirazione

**TU-264 · U-00683 · original 2957.270–2963.675s**

> Quindi il re di Francia ha passato mesi e mesi a attraversare a piedi il suo regno in abito da pellegrino

**TU-366 · U-00684 · original 2963.675–2973.435s**

> fermandosi nelle città, fermandosi nei conventi dei frati a mangiare con loro, a discutere con loro, a parlare con loro. Salimbene l'ha incontrato diverse volte durante questo suo viaggio.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-266 · U-00694 · original 3002.360–3007.080s**

> E questo è un regalo degno di un re. Salimbene dice ai francesi il luccio piace.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-267 · U-00695 · original 3007.160–3016.280s**

> A lui evidentemente, lui non è un mantovano, è di Parma, a lui il luccio non piace, ma dice ai francesi il luccio piace. Stava dentro quella roba che si usa per lavare I neonati

**TU-269 · U-00697 · original 3021.375–3039.710s**

> perché interessa molto anche la lingua, Salimbene. Ha sempre delle notazioni sugli usi delle parole, ecco. Al re si regala un luccio ed è un regalo degno di un re. Dopodiché, il re entra nel convento dei francescani e parla con loro e gli dice che lui non è venuto a chiedere soldi, la crociata la paga lui, è venuto a chiedere soltanto le loro preghiere.

**TU-368 · U-00698 · original 3039.710–3042.590s**

> E dice Salimbene, tutti I frati francesi piangevano.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-270 · U-00704 · original 3061.240–3064.440s**

> Salimbene se lo ricorda ancora, a molti decenni di distanza,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-274 · U-00727 · original 3146.200–3155.640s**

> l'umiltà di quest'uomo che è un santo e sta andando a piedi a imbarcarsi. Perché Salimbene ne conosce ben altre di storie di pranzi e di menù che non sono altrettanto dignitose.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-369 · U-00731 · original 3163.835–3168.475s**

> Salimbene lo racconta, dice, patriarchi di aquileia farebbero meglio a cambiar sistema veramente.

**TU-278 · U-00739 · original 3205.030–3214.145s**

> Dice Salimbene, veramente Cristo ha digiunato 40 giorni e 40 notti nel deserto e I patriarchi di Aquileia farebbero meglio ricordarselo.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-279 · U-00741 · original 3219.425–3227.750s**

> Ci son tante cose ancora di Salimbene che andrebbero dette. Qualcuna l'ho messa addirittura nel programma del del del nostro festival e non l'ho ancora detta.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-283 · U-00745 · original 3248.145–3255.640s**

> Però ormai l'ho messo nel programma del convegno... Del convegno del festival, quindi lo diciamo lo stesso. Salimbene, a un certo punto, se la prende con quelli dell'Italia meridionale.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-289 · U-00757 · original 3303.405–3311.085s**

> Io mi fermerei piuttosto sulla notazione linguistica. Come vi dicevo, Salimbene è molto sensibile alla lingua, ci sta attento. Nella cronaca spesso cita frasi in francese

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-372 · U-00758 · original 3311.500–3313.260s**

> che ha sentito, orecchiato,

**TU-292 · U-00763 · original 3329.615–3338.471s**

> E Salimbene dice, però in realtà in Italia non si fa mica così, ogni zona d'Italia fa a modo suo. Quelli del sud e di Roma danno del tu a tutti. Dà del tu anche al Papa.

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

**TU-373 · U-00777 · original 3392.880–3394.400s**

> non ha proprio limiti.

**TU-374 · U-00781 · original 3407.505–3410.625s**

> Cosa voglia dire questo, a me ha lasciato molto perplesso.

**TU-375 · U-00784 · original 3426.850–3428.370s**

> Il pie inglese

**TU-309 · U-00805 · original 3542.600–3548.280s**

> Imperatore Federico 2º che lui appunto ha conosciuto, a cui ha voluto anche bene, poi pensava che fosse lui l'anticristo,

**TU-310 · U-00806 · original 3548.515–3555.876s**

> poi ha saputo che era morto, ci è rimasto malissimo. Ecco, l'imperatore Federico 2º era un uomo fuori dal normale. Aveva anche lui delle curiosità,

**TU-376 · U-00807 · original 3556.115–3558.195s**

> ma eran delle curiosità malsane,

**TU-377 · U-00811 · original 3571.860–3574.261s**

> Perciò ha preso dei bambini neonati

**TU-378 · U-00812 · original 3574.580–3576.980s**

> e ha dato ordine alle nutrici di allevarli,

**TU-379 · U-00818 · original 3594.860–3597.820s**

> ha sprecato il suo tempo perché quei bambini morivano tutti.

**TU-316 · U-00823 · original 3613.075–3641.875s**

> E questa cosa, l'imperatore Federico 2º, che era un genio, beh lui non era abbastanza umano per capirla evidentemente. Invece Salimbene, con tutti I suoi difetti, è abbastanza umano da capirla e da saperla. Dunque appunto quello che io spero di essere riuscito a trasmettere è che quest'uomo, che sotto tanti aspetti era tanto diverso da noi e che era pieno di difetti però insomma, ecco, ci ha lasciato un'opera dentro in cui... Da cui viene fuori un uomo insomma, ecco. Un uomo tutto a 360 gradi. Io ve ne ho potuti dare soltanto degli assaggi, dei pezzetti,

Recurring transcription variant of Salimbene, whose name is established within the lecture. Contextual spelling proposal; no audio listening.

## Input hashes

| Input | SHA-256 |
|---|---|
| episodes/019-il-frate/episode.yaml | b51c5170e9979c7fe3b8358e5ee58ca12ef4a2e15498b3464981b8e5635e17dd |
| episodes/019-il-frate/transcript.it.md | 9f86a30a8e24e08caeef2fd9e02b8824a45301b4e6ba17f658c958b24ef0660e |
| episodes/019-il-frate/transcript-uncertainties.yaml | 1ca8f5e8f94e1dc8d05ccd4273ee65517ec3f467ef1088a2fd798aae773d9db1 |
| /home/user/data/barbero/editorial/019-il-frate/deepgram.json | 1292359c02e52ecec74f6ac4ed062b088d160b3f9f7323614cc6a24d50ceb19d |
| /home/user/data/barbero/editorial/019-il-frate/edit-map.json | b6d575204bf338cb88f9033cc5a54f465d96a3586c8f451dfc740b1bdc92fe0a |
| /home/user/data/barbero/editorial/019-il-frate/transcription-manifest.json | 03c0f4eb530e8973c4d9650480328f859ca573a939694c9eb29dbe118799095b |

Transcription fingerprint: `2b323d5438ba59cf879394cf8502320cdfbae703d66feac9c07e2b4745ae4555`. No chapter or assembled-Italian fidelity check is claimed: final chapter assembly is deferred until source resolution.

## Follow-up — source settled and assembled, 2026-10-02

This follow-up supersedes the pending-resolution status above; the earlier scan and hashes remain historical provenance. The user explicitly confirmed the approximate birth range 1220–1230, the ending after Grazie, and the lecture wording “non credere istis pissintunicis, id est qui in tunicis mingunt”; then approved all other repairs and continuation. The coordinator resolved all 379 queue items and rerendered the source. The source-preparation agent read all 825 updated utterances in full. No agent audio listening is claimed.

Created chapters.yaml and ran `uv run barbero assemble-italian episodes/019-il-frate`. The final 13-chapter map adjusts two candidate boundaries: CH-002 ends U-00143 / CH-003 begins U-00144, avoiding a sentence broken at U-00136; CH-005 ends U-00411 / CH-006 begins U-00412, preserving the transition “E dunque Salimbene” with the discussion of his sacrifices.

Deterministic checks passed: all 825 transcript IDs/texts equal Deepgram utterances after resolve_utterances; all 379 resolutions resolved; no REVIEW flags; actual cleaned.flac plus manifest-options fingerprint matches; validate_transcript_uncertainties returns no errors; chapter IDs unique/sequential CH-001–CH-013; expanded endpoints cover every source utterance exactly once in order; all 13 assembled chapter bodies equal the corresponding transcript words and punctuation after whitespace normalization. The approved date remains split between U-00158 `1220–` and U-00159 `1230.`; assembly inserts its normal separating space. The user-confirmed Non credere is preserved despite different original Latin. Script ends at Grazie.

The authoritative current source hashes and complete inherited decisions are in brief.md. Research findings remain separate from approved transcript recognition repairs. No historical correction, source-quotation replacement, substantive cut or English adaptation was authorized merely by accepting transcript repairs.

## English review reconciliation checkpoint

Six exact routine repairs are recorded in decision-package.md. Both independent reviews were read in full. All historical/quotation/addition/cut decisions remain pending; original12-item queue preserved in history. C-007 and Q-003/Q-004 now correctly distinguish predictive claims from the Trinitarian condemnation. The source transcript and assembled Italian were not changed. Repaired draft SHA-256: `f5ebf4ba73ec46e2c148e74d67767b12835ec4bbfc39583cc1fe3757b5d5a1fe`; decision queue SHA-256: `4378a26c080284d3a22c71d9c000941d2fff9522c2b7714365f031056055c9dd`.
