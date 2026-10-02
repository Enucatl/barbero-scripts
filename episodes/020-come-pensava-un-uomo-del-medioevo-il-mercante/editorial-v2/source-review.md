# Source review — user approved and Italian assembled

Configured reviewer: `gpt-6-astra`, reasoning `high` (parent confirmed launch). Read the entire Italian transcript, U-00001–U-00801, in five untruncated batches. Contextual review is complete. Inspected all 257 original uncertainty entries and their preserved provider confidence evidence, the processed utterances, original Deepgram structure and targeted raw utterance/word records, transcription manifest and empty correction diff. This is text and provider-metadata review, not performed audio listening. No audio interval is marked reviewed.

Queue: 257 original items retained; 38 new items; 295 total, all resolved under explicit user approval. 93 utterances have applied textual changes: {'auxiliary': 39, 'format': 17, 'lexical': 18, 'orthography': 9, 'ambiguous': 10}. U-00788 was explicitly accepted unchanged with the approved U-00786–U-00788 phrase. 201 remaining flagged utterances have no proposed word change after contextual review. Detection complete records the completed scan; source acceptance is separately documented by the explicit user decision below.

## User decision and application

On 2026-10-02 the user explicitly instructed: “they are all right, with one exception: TU-219 gli VIENE naturale ragionare così. Fix that, approve everything and move on with the workflow”.

Applied all 295 complete-utterance resolutions: 83 straightforward corrections, ten previously ambiguous corrections, 201 unchanged contextual flag confirmations, and the linked unchanged U-00788. TU-219 / U-00703 uses the user-supplied **gli viene naturale ragionare così**, with normal capitalization. The original proposed **gli è naturale** is superseded. The source reasons below remain as historical evidence of why choices were raised; their alternatives no longer represent pending decisions.

Reran `uv run barbero render episodes/020-come-pensava-un-uomo-del-medioevo-il-mercante/episode.yaml`, then `uv run barbero assemble-italian episodes/020-come-pensava-un-uomo-del-medioevo-il-mercante`. Both completed successfully. No raw Deepgram content was changed; processed utterances and transcript now contain the approved readings. No audio-listening claim is made.

## Previously ambiguous wording — approved

### TU-044 · U-00153 · original 09:56.130–10:04.450

Before: Cioè, un certo numero di giovani nobili erano stati addobbati cavalieri con il rituale che trasforma di un uomo qualunque in un cavaliere.

Approved: Cioè, un certo numero di giovani nobili erano stati addobbati cavalieri con il rituale che trasforma un uomo qualunque in un cavaliere.

Reason: Potrebbe essere una falsa partenza realmente pronunciata; proposta di eliminare di solo se confermata. Conservare il testo grezzo è alternativa valida.

### TU-057 · U-00198 · original 13:09.190–13:17.285

Before: Voi capite che se uno deve andare in piazza, si sta facendo politica, dobbiamo andare in piazza, e sono della nostra famiglia, siamo in 60 che vanno in piazza a cavallo con l'armatura,

Approved: Voi capite che se uno deve andare in piazza, si sta facendo politica, dobbiamo andare in piazza, e solo della nostra famiglia, siamo in 60 che vanno in piazza a cavallo con l'armatura,

Reason: Sono ha confidence 0.539; il ragionamento conta sessanta armati della sola famiglia. Solo è plausibile, ma l’ascolto deve distinguere una falsa partenza.

### TU-102 · U-00335 · original 22:51.570–22:52.930

Before: Dino dice hai la guerra,

Approved: Dino dice, ah, la guerra,

Reason: Hai ha confidence 0.542. Probabile interiezione prima della citazione; ah/eh o la sola la guerra restano alternative non risolvibili dal testo.

### TU-140 · U-00450 · original 31:02.555–31:06.075

Before: Ma comunque, per fortuna, ci protetti, è andata bene lo stesso. Ma ecco.

Approved: Ma comunque, per fortuna, ci ha protetti, è andata bene lo stesso. Ma ecco.

Reason: Riparazione minima; soggetto sottinteso non accertato. Potrebbe mancare un riferimento a Dio oppure esservi altra formulazione. Non introdurre Dio dalla citazione storica senza ascolto/decisione.

### TU-286 · U-00640 · original 44:51.415–44:55.490

Before: Però lui, uno di questi partiti non fa parte, lui è un uomo modesto, è un imprenditore,

Approved: Però lui, di uno di questi partiti non fa parte, lui è un uomo modesto, è un imprenditore,

Reason: La negazione finale richiede di, ma la frase può contenere un anacoluto orale. La tesi storica della non appartenenza va verificata separatamente, non corretta qui.

### TU-219 · U-00703 · original 48:44.240–48:55.375

Before: non han voglia di dire, sai che c'è? Tirian fuori le spade e vediamo chi è più uomo. E invece ai nobili vi è naturale ragionare così. I nobili piuttosto che accettare il compromesso, la pacificazione,

Approved: non han voglia di dire, sai che c'è? Tiriam fuori le spade e vediamo chi è più uomo. E invece ai nobili gli viene naturale ragionare così. I nobili piuttosto che accettare il compromesso, la pacificazione,

Reason: Tirian/Tiriam: proposta morfologica nella battuta collettiva, non verificata all’ascolto. Vi ha confidence 0.374; gli è naturale è plausibile italiano orale ridondante. Alternative: viene naturale o è naturale. Non scegliere per sola eleganza.

### TU-241 · U-00765 · original 53:14.995–53:20.595

Before: possono restare in città, ma basta con la politica, con la politica importante. Han chiuso quello. Dino chiuso,

Approved: possono restare in città, ma basta con la politica, con la politica importante. Han chiuso quelli. Dino ha chiuso,

Reason: Quello ha confidence 0.561; probabile quelli riferito ai piccoli imprenditori, insieme all’omissione di ha dopo Dino. L’esatta prima frase resta da confermare.

### TU-248 · U-00783 · original 54:20.835–54:29.380

Before: Perché ogni ogni città che tocca pacifica I partiti, fa rientrare gli esiliati, questa è la grande speranza. Quando Dino scrive, ancora aspettando che l'imperatore arrivi.

Approved: Perché ogni ogni città che tocca pacifica I partiti, fa rientrare gli esiliati, questa è la grande speranza. Quando Dino scrive, sta ancora aspettando che l'imperatore arrivi.

Reason: Manca un verbo reggente; sta è ricostruzione più naturale, non accertata dal provider. Non introdurre una data di composizione.

### TU-293 · U-00787 · original 54:47.025–54:48.705

Before: come dire, l'affermazione

Approved: come dire, la fazione

Reason: Nei segmenti 786–788 si parla del ritorno al potere dei capi di fazione. La fazione è plausibile, ma affermazione può essere una falsa partenza reale: ascoltare insieme il periodo.

### TU-252 · U-00794 · original 55:05.505–55:11.665

Before: Noi in politica abbiamo perso, ci siam buttati fuori dal potere, si son presi tutto loro, però Dio

Approved: Noi in politica abbiamo perso, ci han buttati fuori dal potere, si son presi tutto loro, però Dio

Reason: Il racconto implica espulsione da parte degli avversari; ci han è plausibile. Ci siam può essere un lapsus pronunciato: non trasformare il contenuto senza conferma.

Linked unchanged resolution: TU-295 · U-00788 · original 54:48.705–54:52.810

Before and approved unchanged: violenta più brutale al potere della città. E I grandi capipartito

Approved unchanged together with U-00786–U-00787. No additional phrase was inserted.

## Routine repeated missing ha forms

### TU-259 · U-00008 · original 00:23.665–00:25.745

Before: e che ci scritto un piccolo libro.

Approved: e che ci ha scritto un piccolo libro.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-004 · U-00009 · original 00:26.145–00:33.270

Before: Chi c'era ieri sera ricorda che Fra Salimbene scritto una cronaca di 900 pagine. Ecco, Dino Compagni scritto un piccolo libro

Approved: Chi c'era ieri sera ricorda che Fra Salimbene ha scritto una cronaca di 900 pagine. Ecco, Dino Compagni ha scritto un piccolo libro

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-006 · U-00011 · original 00:35.110–00:36.790

Before: in cui voluto raccontare

Approved: in cui ha voluto raccontare

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-260 · U-00020 · original 01:08.450–01:12.210

Before: è innanzitutto uno che fatto politica a Firenze

Approved: è innanzitutto uno che ha fatto politica a Firenze

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-261 · U-00028 · original 01:34.210–01:35.970

Before: che questo nome un po' curioso,

Approved: che ha questo nome un po' curioso,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-262 · U-00031 · original 01:43.250–01:45.410

Before: Dino una sua ditta importante,

Approved: Dino ha una sua ditta importante,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-015 · U-00039 · original 02:07.520–02:12.880

Before: e però dentro questa cosa che lo rode, lui per un po' di tempo è stato al potere.

Approved: e però ha dentro questa cosa che lo rode, lui per un po' di tempo è stato al potere.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-263 · U-00040 · original 02:13.280–02:18.585

Before: Cercato, dice lui, di evitare che le cose andassero così male come stanno andando.

Approved: Ha cercato, dice lui, di evitare che le cose andassero così male come stanno andando.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-264 · U-00056 · original 03:18.615–03:22.215

Before: E questa è una cosa che 2º me è significativa. A me colpito.

Approved: E questa è una cosa che secondo me è significativa. A me ha colpito.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-265 · U-00062 · original 03:32.510–03:35.230

Before: I suoi conflitti anche violentissimi,

Approved: ha I suoi conflitti anche violentissimi,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-266 · U-00071 · original 04:07.460–04:09.700

Before: che poi a un certo punto perso,

Approved: che poi a un certo punto ha perso,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-267 · U-00098 · original 06:01.375–06:03.615

Before: in realtà degli scontri durissimi.

Approved: in realtà ha degli scontri durissimi.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-041 · U-00149 · original 09:32.260–09:34.900

Before: dove combattuto anche Dante, che era un nobile,

Approved: dove ha combattuto anche Dante, che era un nobile,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-268 · U-00173 · original 11:20.115–11:25.155

Before: che sempre la spada al fianco in qualunque momento e che la tira fuori

Approved: che ha sempre la spada al fianco in qualunque momento e che la tira fuori

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-053 · U-00194 · original 12:39.220–12:48.095

Before: Dino Compagni un cognome perché è già un borghese ricco, ma la maggior parte dei fiorentini non neanche un cognome. Si chiamano Dino di Giovanni, di Andrea, di Bartolomeo.

Approved: Dino Compagni ha un cognome perché è già un borghese ricco, ma la maggior parte dei fiorentini non ha neanche un cognome. Si chiamano Dino di Giovanni, di Andrea, di Bartolomeo.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-059 · U-00210 · original 13:54.720–14:02.160

Before: il quale dice Dino, cioè a un certo punto c'è stato un problema politico, il vescovo tradito la sua parte, tradito la sua famiglia,

Approved: il quale dice Dino, cioè a un certo punto c'è stato un problema politico, il vescovo ha tradito la sua parte, ha tradito la sua famiglia,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-269 · U-00211 · original 14:02.400–14:07.840

Before: cercato di accordarsi coi fiorentini mentre I suoi amici e parenti volevano fare la guerra contro Firenze.

Approved: ha cercato di accordarsi coi fiorentini mentre I suoi amici e parenti volevano fare la guerra contro Firenze.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-068 · U-00231 · original 15:11.545–15:20.505

Before: seccato, ecco. Però è un mio parente, quindi non potete chiedermi che io voti per farlo ammazzare in consiglio comunale. Mi dispiace, ma io non posso votare per farlo ammazzare.

Approved: ha seccato, ecco. Però è un mio parente, quindi non potete chiedermi che io voti per farlo ammazzare in consiglio comunale. Mi dispiace, ma io non posso votare per farlo ammazzare.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-270 · U-00236 · original 15:34.175–15:35.855

Before: non la spada al fianco.

Approved: non ha la spada al fianco.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-271 · U-00241 · original 15:54.255–16:02.255

Before: tutto gira intorno alla parentela. Dino non ne di parenti, è un uomo che si è fatto da solo, ecco, è un self-made man veramente,

Approved: tutto gira intorno alla parentela. Dino non ne ha di parenti, è un uomo che si è fatto da solo, ecco, è un self-made man veramente,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-099 · U-00331 · original 22:23.360–22:39.825

Before: I nobili la vogliono fare la guerra. Perché a loro conviene, loro la sanno fare. Se si fa la guerra, sono stipendi d'oro per I nobili. E bottino, e vuol dire che loro conteranno. E se la guerra si vince, chi l' vinta? Noi, I nobili. Quindi I mercanti stessero un po' al loro posto. Quindi ai nobili conviene.

Approved: I nobili la vogliono fare la guerra. Perché a loro conviene, loro la sanno fare. Se si fa la guerra, sono stipendi d'oro per I nobili. E bottino, e vuol dire che loro conteranno. E se la guerra si vince, chi l'ha vinta? Noi, I nobili. Quindi I mercanti stessero un po' al loro posto. Quindi ai nobili conviene.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-274 · U-00368 · original 25:08.495–25:11.935

Before: hanno chiamato uno da fuori che comandato ad Arezzo

Approved: hanno chiamato uno da fuori che ha comandato ad Arezzo

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-275 · U-00369 · original 25:11.935–25:16.015

Before: e messo I nobili al loro posto, dice Dino, li costringeva

Approved: e ha messo I nobili al loro posto, dice Dino, li costringeva

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-276 · U-00400 · original 27:31.250–27:34.850

Before: Ogni famiglia che avuto un cavaliere fra I suoi

Approved: Ogni famiglia che ha avuto un cavaliere fra I suoi

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-138 · U-00447 · original 30:47.760–30:56.475

Before: Votano con le fave bianche e nere, come si vota in tutti I consigli. Ognuno la sua fava bianca, la sua fava nera, poi le depositano nell'urna e si vede.

Approved: Votano con le fave bianche e nere, come si vota in tutti I consigli. Ognuno ha la sua fava bianca, la sua fava nera, poi le depositano nell'urna e si vede.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-279 · U-00468 · original 32:24.215–32:29.095

Before: non aveva niente da dire, però è venuto lì, tenuto la ringhiera impacciata mezza giornata

Approved: non aveva niente da dire, però è venuto lì, ha tenuto la ringhiera impacciata mezza giornata

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-280 · U-00480 · original 33:20.285–33:21.885

Before: Quando il comune bisogno di soldi,

Approved: Quando il comune ha bisogno di soldi,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-281 · U-00532 · original 37:22.095–37:26.015

Before: Come il malfattore degli amici e può moneta spendere,

Approved: Come il malfattore ha degli amici e può moneta spendere,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-283 · U-00552 · original 38:48.300–38:52.620

Before: Il comune deciso di ricompensare la sua famiglia per I grandi servigi

Approved: Il comune ha deciso di ricompensare la sua famiglia per I grandi servigi

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-179 · U-00554 · original 38:55.500–39:05.105

Before: Armato cavalieri a spese del comune I figli di Messerrosso della Tosa. Ora voi dovete sapere che armare uno cavaliere è una cosa costosissima,

Approved: Ha armato cavalieri a spese del comune I figli di Messer Rosso della Tosa. Ora voi dovete sapere che armare uno cavaliere è una cosa costosissima,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-181 · U-00562 · original 39:29.745–39:43.585

Before: E la gente mormora, ma non può farci niente, si accontenta di prenderli in giro. La gente dice, qualcuno fatto il conto che tutti I soldi spesi per armare cavalieri questi 2 figli di papà, più o meno equivalevano alle tasse pagate

Approved: E la gente mormora, ma non può farci niente, si accontenta di prenderli in giro. La gente dice, qualcuno ha fatto il conto che tutti I soldi spesi per armare cavalieri questi 2 figli di papà, più o meno equivalevano alle tasse pagate

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-196 · U-00611 · original 42:59.680–43:05.840

Before: Come vedete, il manuale Cencelli non l' inventato nessuno. Loro hanno esattamente questa stessa preoccupazione di ripartizione.

Approved: Come vedete, il manuale Cencelli non l'ha inventato nessuno. Loro hanno esattamente questa stessa preoccupazione di ripartizione.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-285 · U-00616 · original 43:21.665–43:25.345

Before: mi preso da parte e mi detto, ma senti Dino,

Approved: mi ha preso da parte e mi ha detto, ma senti Dino,

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-200 · U-00621 · original 43:42.520–43:48.455

Before: perché quello è, lo sbocco poi delle rivalità. Dino questa idea che lui sta facendo finalmente un governo

Approved: perché quello è, lo sbocco poi delle rivalità. Dino ha questa idea che lui sta facendo finalmente un governo

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-287 · U-00679 · original 47:02.670–47:04.990

Before: perché la ragione l' data Dio 2º loro naturalmente.

Approved: perché la ragione l'ha data Dio secondo loro naturalmente.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-290 · U-00694 · original 48:13.775–48:16.335

Before: cominciato a un certo punto a dire, qui

Approved: ha cominciato a un certo punto a dire, qui

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-226 · U-00728 · original 50:27.985–50:34.785

Before: Dino. Dino a un certo punto li fatti giurare. Fatto giurare tutti I cittadini più importanti, tutti I capi partito in San Giovanni

Approved: Dino. Dino a un certo punto li ha fatti giurare. Ha fatto giurare tutti I cittadini più importanti, tutti I capi partito in San Giovanni

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto. Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-230 · U-00739 · original 51:20.595–51:23.075

Before: Ci detto, perché non fate una processione?

Approved: Ci ha detto, perché non fate una processione?

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

### TU-239 · U-00757 · original 52:34.610–52:39.730

Before: è il momento in cui anche Dante Alighieri viene esiliato da Firenze, perché stava col partito che perso.

Approved: è il momento in cui anche Dante Alighieri viene esiliato da Firenze, perché stava col partito che ha perso.

Reason: Omissione contestuale di ha: il soggetto e la costruzione verbale sono ricostruibili nelle frasi contigue; proposta testuale, non ascolto.

## Numerical formatting artifacts

### TU-258 · U-00006 · original 00:18.625–00:20.865

Before: vissuto fra 200.300,

Approved: vissuto fra Duecento e Trecento,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-043 · U-00151 · original 09:40.015–09:52.175

Before: C'è della gente che si è fatta ammazzare piuttosto che arretrare. C'è anche chi è scappato mentre si pensava che dovesse fare chissà cosa e poi invece è scappato. Ma molti si son battuti molto bene e dice Dino, quel mattino 1º della battaglia

Approved: C'è della gente che si è fatta ammazzare piuttosto che arretrare. C'è anche chi è scappato mentre si pensava che dovesse fare chissà cosa e poi invece è scappato. Ma molti si son battuti molto bene e dice Dino, quel mattino prima della battaglia

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-058 · U-00209 · original 13:47.675–13:54.075

Before: C'era appunto quel tal vescovo che vi dicevo 1º, il vescovo di Arezzo che si intendeva più di guerra che di chiesa,

Approved: C'era appunto quel tal vescovo che vi dicevo prima, il vescovo di Arezzo che si intendeva più di guerra che di chiesa,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-076 · U-00264 · original 17:36.860–17:40.780

Before: possiede botteghe, le dà in affitto, se tu 6 1 affittuario degli Uberti,

Approved: possiede botteghe, le dà in affitto, se tu sei un affittuario degli Uberti,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-077 · U-00266 · original 17:42.380–17:47.900

Before: Se 6 1, 1 come dire, un imprenditore che lavora per gli Uberti, stai con loro comunque.

Approved: Se sei un, un come dire, un imprenditore che lavora per gli Uberti, stai con loro comunque.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-082 · U-00276 · original 18:24.875–18:33.035

Before: e per la 1º volta son tornati gli uberti a Firenze e si son visti gli uberti entrare a Firenze a cavallo coi loro scudi, col loro stemma,

Approved: e per la prima volta son tornati gli Uberti a Firenze e si son visti gli Uberti entrare a Firenze a cavallo coi loro scudi, col loro stemma,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica. Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-087 · U-00295 · original 19:49.560–19:53.480

Before: A Firenze fanno a un certo 0.1 governo di popolo che sarebbe,

Approved: A Firenze fanno a un certo punto un governo di popolo che sarebbe,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-091 · U-00306 · original 20:29.175–20:31.255

Before: Quando Firenze a fine 200

Approved: Quando Firenze a fine Duecento

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-277 · U-00426 · original 29:22.710–29:23.910

Before: siamo a fine 200.

Approved: siamo a fine Duecento.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-130 · U-00429 · original 29:33.005–29:38.845

Before: ci si sarebbe trovato benissimo nella Firenze di fine 200, perché a ogni occasione cosa si fa? Si convoca un'assemblea.

Approved: ci si sarebbe trovato benissimo nella Firenze di fine Duecento, perché a ogni occasione cosa si fa? Si convoca un'assemblea.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-282 · U-00535 · original 37:38.080–37:45.040

Before: e vuol dire che 6 tu che metti le mani nelle tasche dei cittadini, per usare ancora un linguaggio insomma attualizzante,

Approved: e vuol dire che sei tu che metti le mani nelle tasche dei cittadini, per usare ancora un linguaggio insomma attualizzante,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-174 · U-00537 · original 37:50.720–38:01.020

Before: non voglio, come dire, non voglio strappare degli applausi fin troppo facili, Io sto parlando della Firenze di fine del 200. A Firenze, fine del 200,

Approved: non voglio, come dire, non voglio strappare degli applausi fin troppo facili, Io sto parlando della Firenze di fine del Duecento. A Firenze, fine del Duecento,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-176 · U-00546 · original 38:28.230–38:32.950

Before: Fino al 2000. Fiorini, si capisce, non c'è bisogno di votare, si dà. E I soldi vanno fuori.

Approved: Fino a 2000 fiorini, si capisce, non c'è bisogno di votare, si dà. E I soldi vanno fuori.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-284 · U-00604 · original 42:29.235–42:41.110

Before: che è quello che comanda la polizia e quando 2º gli ordinamenti di giustizia, un nobile commette un delitto, deve farlo arrestare, andare a far spianare le sue case e così via. Ecco, il 7º, il gonfaloniere di giustizia,

Approved: che è quello che comanda la polizia e quando secondo gli ordinamenti di giustizia, un nobile commette un delitto, deve farlo arrestare, andare a far spianare le sue case e così via. Ecco, il 7º, il gonfaloniere di giustizia,

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-207 · U-00637 · original 44:38.420–44:44.935

Before: e che 2º lui non hanno nessuna idea di cos'è l'interesse pubblico, vogliono solo occuparlo il potere.

Approved: e che secondo lui non hanno nessuna idea di cos'è l'interesse pubblico, vogliono solo occuparlo il potere.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-242 · U-00770 · original 53:31.170–53:37.330

Before: che hanno fatto... Hanno portato la città alla rovina, 2º lui. Aspetta, perché la giustizia di Dio è lenta.

Approved: che hanno fatto... Hanno portato la città alla rovina, secondo lui. Aspetta, perché la giustizia di Dio è lenta.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

### TU-294 · U-00790 · original 54:53.690–54:56.970

Before: Dino è fortunato, vive a lungo. 1º o poi muoiono.

Approved: Dino è fortunato, vive a lungo. prima o poi muoiono.

Reason: Artefatto di formattazione numerica: scioglimento imposto dalla sintassi o dal periodo medievale esplicitato nel contesto; nessuna nuova data storica.

## Names, word segmentation and clear lexical repairs

### TU-012 · U-00021 · original 01:12.450–01:18.875

Before: e che ci racconta cosa voleva dire fare politica nella Firenze dei comuni, nella Firenze dei guelfi e degli bellini,

Approved: e che ci racconta cosa voleva dire fare politica nella Firenze dei comuni, nella Firenze dei guelfi e dei ghibellini,

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-013 · U-00024 · original 01:26.635–01:28.635

Before: Lino naturalmente è un mercante,

Approved: Dino naturalmente è un mercante,

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-037 · U-00131 · original 08:08.200–08:23.665

Before: chiama tutti a combattere e quindi tutti I cittadini, gli artigiani, I mercanti, tutti organizzati in compagnie di quartiere, tutti a piedi con le loro lanci, I loro scudi, sì, però I nobili che sanno stare a cavallo, che hanno le armature, che passan la vita a combattere nei tornei,

Approved: chiama tutti a combattere e quindi tutti I cittadini, gli artigiani, I mercanti, tutti organizzati in compagnie di quartiere, tutti a piedi con le loro lance, I loro scudi, sì, però I nobili che sanno stare a cavallo, che hanno le armature, che passan la vita a combattere nei tornei,

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-074 · U-00254 · original 16:55.835–17:00.635

Before: Lui è un uomo d'affari che pensa a fare I soldi a importare I pani dalla dalla Francia,

Approved: Lui è un uomo d'affari che pensa a fare I soldi a importare I panni dalla dalla Francia,

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-092 · U-00310 · original 20:40.380–20:50.700

Before: Lui però che è un imprenditore che di fronte ai nobili buon del Monti si toglie il cappello, invece si trova fra quelli che vanno al governo e spesso si trova in un organismo di potere.

Approved: Lui però che è un imprenditore che di fronte ai nobili Buondelmonti si toglie il cappello, invece si trova fra quelli che vanno al governo e spesso si trova in un organismo di potere.

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-119 · U-00397 · original 27:16.750–27:25.875

Before: a far passare queste leggi, I nobili esclusi dagli uffici. A un certo punto Dina dice, sì, ma chi sono I nobili esattamente? Perché è facile dirlo, ma

Approved: a far passare queste leggi, I nobili esclusi dagli uffici. A un certo punto Dino dice, sì, ma chi sono I nobili esattamente? Perché è facile dirlo, ma

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-137 · U-00444 · original 30:33.295–30:41.520

Before: tutti lì e tutti discutono. Discuterno tutto il giorno in pubblico per decidere se per attaccare Arezzo si passa dal Casentino o si passa da Valdarno.

Approved: tutti lì e tutti discutono. Discutono tutto il giorno in pubblico per decidere se per attaccare Arezzo si passa dal Casentino o si passa da Valdarno.

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-144 · U-00457 · original 31:28.685–31:34.045

Before: C'è stato un momento di grave crisi a Firenze. È arrivato a Firenze Carlo di Valua, un principe francese,

Approved: C'è stato un momento di grave crisi a Firenze. È arrivato a Firenze Carlo di Valois, un principe francese,

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-155 · U-00490 · original 33:52.380–33:56.380

Before: È raro trovare qualcuno come il cardinale Matteo d'Aquasparta

Approved: È raro trovare qualcuno come il cardinale Matteo d'Acquasparta

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-159 · U-00494 · original 34:12.315–34:26.840

Before: divisa da guerre civili, da scontri. Il Papa vorrebbe mettere pace e loro hanno una gran paura che arrivi qualcuno dal Papa con degli ordini, perché gli secca che vengano I cardinali a dargli degli ordini, però a un certo punto arriva il cardinale Matteo d'Aqua Sparta

Approved: divisa da guerre civili, da scontri. Il Papa vorrebbe mettere pace e loro hanno una gran paura che arrivi qualcuno dal Papa con degli ordini, perché gli secca che vengano I cardinali a dargli degli ordini, però a un certo punto arriva il cardinale Matteo d'Acquasparta

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-161 · U-00507 · original 35:14.335–35:18.170

Before: va bene, al cardinale d'Aqua Sparta mandiamo 2000 fiorini.

Approved: va bene, al cardinale d'Acquasparta mandiamo 2000 fiorini.

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-173 · U-00536 · original 37:45.120–37:47.920

Before: perché il governo tassa, è tassa per... Ma però,

Approved: perché il governo tassa, e tassa per... Ma però,

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-178 · U-00550 · original 38:43.245–38:45.005

Before: Messerrosso della Tosa,

Approved: Messer Rosso della Tosa,

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-202 · U-00623 · original 43:56.855–43:59.095

Before: Lui dice, io da parte del Giuda non la voglio fare.

Approved: Lui dice, io la parte del Giuda non la voglio fare.

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-203 · U-00626 · original 44:05.390–44:08.670

Before: darei I miei figliuoli a mangiare I cani.

Approved: darei I miei figliuoli a mangiare ai cani.

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-220 · U-00704 · original 48:55.455–49:04.415

Before: tiran fuori le spade. Ed Ilo lo ammette, noi stessi, io e gli altri mercanti che eravamo al governo in quel momento, lui scrive anni dopo quando ormai è andata a finire malissimo,

Approved: tiran fuori le spade. E Dino lo ammette, noi stessi, io e gli altri mercanti che eravamo al governo in quel momento, lui scrive anni dopo quando ormai è andata a finire malissimo,

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

### TU-292 · U-00749 · original 52:03.490–52:06.530

Before: prendere a raffare a tutti I costi, in tutti I modi

Approved: prendere, arraffare a tutti I costi, in tutti I modi

Reason: Errore lessicale o di segmentazione riconoscibile nella sintassi e nel tema del passo; mantenuti contenuto, ripetizioni e registro orale.

### TU-257 · U-00801 · original 55:40.315–55:45.755

Before: Ma noi non siamo qui per fare dei paralleli con Loggi. Ero qui per raccontarvi come vedeva il mondo un mercante fiorentino. Grazie.

Approved: Ma noi non siamo qui per fare dei paralleli con l'oggi. Ero qui per raccontarvi come vedeva il mondo un mercante fiorentino. Grazie.

Reason: Nome o parola mal segmentata: proposta coerente con il referente e con il contesto dell’intera lezione; non una correzione storica.

## Proper-name capitalization

### TU-054 · U-00195 · original 12:48.495–12:53.135

Before: Invece I nobili sono I cavalcanti, I Brunelleschi, I Tosinghi e così via.

Approved: Invece I nobili sono I Cavalcanti, I Brunelleschi, I Tosinghi e così via.

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-056 · U-00197 · original 12:56.415–13:08.790

Before: E ogni famiglia è numerosa, dice a un certo punto, I cavalcanti. C'è stato un litigio tra diverse famiglie contro I cavalcanti e I cavalcanti eran forti. Solo loro erano 60 uomini capaci di portare le armi.

Approved: E ogni famiglia è numerosa, dice a un certo punto, I Cavalcanti. C'è stato un litigio tra diverse famiglie contro I Cavalcanti e I Cavalcanti eran forti. Solo loro erano 60 uomini capaci di portare le armi.

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-079 · U-00269 · original 17:58.065–18:02.065

Before: Tutti ricordano farinata degli Uberti nell'inferno di Dante.

Approved: Tutti ricordano Farinata degli Uberti nell'inferno di Dante.

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-272 · U-00280 · original 18:40.070–18:44.150

Before: che correvano a baciare lo stemma degli uberti.

Approved: che correvano a baciare lo stemma degli Uberti.

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-273 · U-00282 · original 18:45.910–18:48.630

Before: che gli uberti erano esiliati dalla città.

Approved: che gli Uberti erano esiliati dalla città.

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-278 · U-00467 · original 32:22.695–32:24.215

Before: Bandino falconieri,

Approved: Bandino Falconieri,

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-288 · U-00688 · original 47:43.475–47:47.555

Before: Perché alla testa dei guelfi bianchi ci sono I cerchi, grande famiglia,

Approved: Perché alla testa dei guelfi bianchi ci sono I Cerchi, grande famiglia,

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-289 · U-00690 · original 47:59.940–48:05.700

Before: E invece dall'altra parte, alla testa dei neri, ci son dei baroni, ci sono I donati, son dei grandi nobili antichi

Approved: E invece dall'altra parte, alla testa dei neri, ci son dei baroni, ci sono I Donati, son dei grandi nobili antichi

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

### TU-291 · U-00696 · original 48:18.175–48:22.970

Before: Qui da una parte abbiamo I cerchi e sono mercatanti

Approved: Qui da una parte abbiamo I Cerchi e sono mercatanti

Reason: Maiuscola del nome proprio già identificato dal contesto; nessun cambiamento di parola pronunciata.

## Same-word contextual confirmations approved

These flags have been investigated in the complete running context. No alternate wording is justified by the available text. Retain discourse hesitations, unfinished sentences and meaningful repetitions. Name flags often mark correct known referents; date flags at U-00382 and U-00505/U-00507/U-00509/U-00510 are counts or money, not dates. Acoustic confidence remains model evidence only; retaining a reading is a contextual recommendation.

TU-001 (U-00002), TU-002 (U-00003), TU-003 (U-00004), TU-005 (U-00010), TU-007 (U-00013), TU-008 (U-00016), TU-009 (U-00017), TU-010 (U-00018), TU-011 (U-00019), TU-014 (U-00027), TU-016 (U-00049), TU-017 (U-00052), TU-018 (U-00065), TU-019 (U-00074), TU-020 (U-00075), TU-021 (U-00077), TU-022 (U-00080), TU-023 (U-00081), TU-024 (U-00091), TU-025 (U-00096), TU-026 (U-00106), TU-027 (U-00107), TU-028 (U-00109), TU-029 (U-00110), TU-030 (U-00112), TU-031 (U-00117), TU-032 (U-00119), TU-033 (U-00122), TU-034 (U-00123), TU-035 (U-00125), TU-036 (U-00126), TU-038 (U-00138), TU-039 (U-00145), TU-040 (U-00146), TU-042 (U-00150), TU-045 (U-00160), TU-046 (U-00168), TU-047 (U-00181), TU-048 (U-00182), TU-049 (U-00183), TU-050 (U-00184), TU-051 (U-00186), TU-052 (U-00188), TU-055 (U-00196), TU-060 (U-00212), TU-061 (U-00218), TU-062 (U-00220), TU-063 (U-00222), TU-064 (U-00223), TU-065 (U-00224), TU-066 (U-00225), TU-067 (U-00230), TU-069 (U-00233), TU-070 (U-00240), TU-071 (U-00250), TU-072 (U-00252), TU-073 (U-00253), TU-075 (U-00258), TU-078 (U-00267), TU-080 (U-00270), TU-081 (U-00275), TU-083 (U-00285), TU-084 (U-00287), TU-085 (U-00288), TU-086 (U-00292), TU-088 (U-00299), TU-089 (U-00301), TU-090 (U-00305), TU-093 (U-00315), TU-094 (U-00317), TU-095 (U-00320), TU-096 (U-00323), TU-097 (U-00328), TU-098 (U-00329), TU-100 (U-00333), TU-101 (U-00334), TU-103 (U-00336), TU-104 (U-00343), TU-105 (U-00347), TU-106 (U-00348), TU-107 (U-00350), TU-108 (U-00351), TU-109 (U-00358), TU-110 (U-00359), TU-111 (U-00365), TU-112 (U-00372), TU-113 (U-00377), TU-114 (U-00379), TU-115 (U-00382), TU-116 (U-00391), TU-117 (U-00392), TU-118 (U-00393), TU-120 (U-00401), TU-121 (U-00404), TU-122 (U-00405), TU-123 (U-00407), TU-124 (U-00410), TU-125 (U-00412), TU-126 (U-00417), TU-127 (U-00418), TU-128 (U-00423), TU-129 (U-00424), TU-131 (U-00431), TU-132 (U-00434), TU-133 (U-00438), TU-134 (U-00441), TU-135 (U-00442), TU-136 (U-00443), TU-139 (U-00448), TU-141 (U-00451), TU-142 (U-00455), TU-143 (U-00456), TU-145 (U-00459), TU-146 (U-00460), TU-147 (U-00461), TU-148 (U-00463), TU-149 (U-00469), TU-150 (U-00474), TU-151 (U-00476), TU-152 (U-00485), TU-153 (U-00486), TU-154 (U-00487), TU-156 (U-00491), TU-157 (U-00492), TU-158 (U-00493), TU-160 (U-00505), TU-162 (U-00508), TU-163 (U-00509), TU-164 (U-00510), TU-165 (U-00513), TU-166 (U-00514), TU-167 (U-00516), TU-168 (U-00523), TU-169 (U-00524), TU-170 (U-00525), TU-171 (U-00529), TU-172 (U-00534), TU-175 (U-00538), TU-177 (U-00548), TU-180 (U-00559), TU-182 (U-00563), TU-183 (U-00567), TU-184 (U-00570), TU-185 (U-00571), TU-186 (U-00572), TU-187 (U-00574), TU-188 (U-00576), TU-189 (U-00592), TU-190 (U-00594), TU-191 (U-00596), TU-192 (U-00599), TU-193 (U-00607), TU-194 (U-00609), TU-195 (U-00610), TU-197 (U-00612), TU-198 (U-00615), TU-199 (U-00618), TU-201 (U-00622), TU-204 (U-00629), TU-205 (U-00631), TU-206 (U-00635), TU-208 (U-00639), TU-209 (U-00643), TU-210 (U-00652), TU-211 (U-00658), TU-212 (U-00664), TU-213 (U-00667), TU-214 (U-00678), TU-215 (U-00680), TU-216 (U-00682), TU-217 (U-00685), TU-218 (U-00689), TU-221 (U-00711), TU-222 (U-00712), TU-223 (U-00715), TU-224 (U-00717), TU-225 (U-00722), TU-227 (U-00730), TU-228 (U-00736), TU-229 (U-00738), TU-231 (U-00740), TU-232 (U-00741), TU-233 (U-00744), TU-234 (U-00748), TU-235 (U-00750), TU-236 (U-00753), TU-237 (U-00754), TU-238 (U-00756), TU-240 (U-00764), TU-243 (U-00772), TU-244 (U-00773), TU-245 (U-00775), TU-246 (U-00777), TU-247 (U-00779), TU-249 (U-00784), TU-250 (U-00789), TU-251 (U-00792), TU-253 (U-00796), TU-254 (U-00797), TU-255 (U-00798), TU-256 (U-00799)

## Scope boundaries and research handoff

Do not repair historical claims by editing this transcript. Separate research should check, among other things, Compagni’s party position, the timing of the Uberti return, the identity/death/knighting anecdote attributed to Rosso della Tosa, public voting rules, assemblies and magistracies, Dante at Campaldino, and the later imperial hope. The repeated Battistero/duomo/cattedrale wording is retained as spoken-context evidence, with the architectural terminology reserved for research. Keep the party-affiliation tension between Dino’s claimed neutrality and the narration of the White faction as an attributed perspective.

Retained harmless oral features include repetitions (È è, ogni ogni, non fare fare), clipped infinitival constructions, the self-correction Firenze/Arezzo, open sentences, numeral spellings for real counts, colloquial syntax, and spoken analogies. No omissions or compression were authorized.

## Verification

Verified original IDs, current_text, timestamps and existing reasons remain unchanged. All 295 resolutions contain the complete approved utterance and exact user-decision note. Queue validation passes against raw provider utterances; the actual cleaned-audio/options fingerprint still matches. All 801 rendered transcript texts equal the corresponding raw text plus explicit approved resolutions, and processed utterances exactly match them. No REVIEW flags remain. Twelve sequential chapter ranges cover every ID once in order. Assembled script.it.md spoken text and punctuation match the transcript after structural removal and whitespace normalization, both globally and for every chapter. No italian-review.yaml or reviewed_audio artifact was created. Current hashes are in the brief.

## Listening excerpts for user review

Extracted from the original recording; these files were not listened to by the reviewer. Each includes the full target utterance plus roughly three seconds on either side; long utterances produce longer clips. The U-00787 clip includes U-00788.

- [U-00153 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00153.mp3): original seconds 593.130–607.450.
- [U-00198 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00198.mp3): original seconds 786.190–800.285.
- [U-00335 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00335.mp3): original seconds 1368.570–1375.930.
- [U-00450 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00450.mp3): original seconds 1859.555–1869.075.
- [U-00640 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00640.mp3): original seconds 2688.415–2698.490.
- [U-00703 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00703.mp3): original seconds 2921.240–2938.375.
- [U-00765 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00765.mp3): original seconds 3191.995–3203.595.
- [U-00783 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00783.mp3): original seconds 3257.835–3272.380.
- [U-00787 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00787.mp3): original seconds 3284.025–3295.810.
- [U-00794 original-audio excerpt](/home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/source-review-clips/U-00794.mp3): original seconds 3302.505–3314.665.
