# Q-001: *La catedral del mar*

## Research question

At U-00053–U-00058, Barbero recounts a scene from Ildefonso Falcones's *La catedral del mar*.
Llorenç de Bellera invokes a right belonging to him as lord, takes Bernat Estanyol's wife on her
wedding night, and afterward tells Bernat that it is now his turn. The research question was
whether this sequence and dialogue occur in the novel or are Barbero's dramatization.

## Evidence supplied

The full-text search was conducted against the following user-supplied witness:

- Title: *La catedral del mar*
- Author: Ildefonso Falcones
- Original publication: 2006
- Digital witness: Titivillus ePub base r1.2, dated 19 February 2018
- Pagination: the e-text exposes neither printed page numbers nor stable PDF pagination

The scene is in *Primera parte: Siervos de la tierra*, chapter 1, headed “Año 1320, Masía de
Bernat Estanyol, Navarcles, Principado de Cataluña.” It occurs in the middle-to-late portion of the
chapter.

The reported scene boundaries are:

- Start: “Tres jinetes habían aparecido entre los árboles. Seguían sus pasos varios hombres a pie,
  uniformados.”
- End: “Llorenç de Bellera había oído los desesperados alaridos que procedían de la ventana del
  segundo piso y, cuando su espía le confirmó que el matrimonio había sido consumado, pidió los
  caballos y abandonó el lugar con su siniestra comitiva.”

## Recovered passages

Before invoking the claimed right, Llorenç orders Francesca to serve him:

> —Eso está mejor —comentó Llorenç, examinándola de arriba abajo sin recato alguno—, mucho mejor.
> Tú nos servirás el vino a partir de ahora.

The supplied direct English rendering was:

> “That’s better,” Llorenç commented, examining her unashamedly from top to bottom, “much better.
> You will serve us the wine from now on.”

Llorenç then explicitly invokes a right belonging to him as Bernat's lord:

> —Estanyol —gritó Llorenç de Bellera poniéndose en pie con Francesca agarrada de la muñeca—. En
> uso del derecho que como señor tuyo me corresponde, he decidido yacer con tu mujer en su primera
> noche.

Direct English rendering:

> “Estanyol,” shouted Llorenç de Bellera, standing up with Francesca held by the wrist. “In exercise
> of the right that belongs to me as your lord, I have decided to lie with your wife on her first
> night.”

After returning downstairs, he addresses Bernat again:

> —Estanyol —gritó con su atronadora voz mientras pasaba al lado de Bernat y se dirigía hacia la
> mesa—, ahora te toca a ti. […] ¡Cumple como un buen esposo cristiano!

Direct English rendering:

> “Estanyol,” he shouted in his thunderous voice as he passed beside Bernat and headed toward the
> table, “now it is your turn. […] Do your duty as a good Christian husband!”

## Comparison with Barbero

| Barbero element | Evidence in the novel | Assessment |
| --- | --- | --- |
| The lord arrives at a wedding banquet near Navarcles | Llorenç de Bellera, lord of Navarcles, arrives on horseback at Bernat Estanyol's wedding feast at the *masía*. | Exact or near-exact |
| The lord drinks at the banquet | The lord and his companions sit at the main table, demand wine, and drink heavily. | Exact or near-exact |
| The lord notices and touches the bride | He orders Francesca to serve wine, grabs her wrist, and pulls her close. | Exact or near-exact |
| The lord explicitly invokes a seigneurial right | He says, “En uso del derecho que como señor tuyo me corresponde…” | Near-exact translation |
| The lord takes her away | He grabs Francesca by the waist, places her over his shoulder, and carries her upstairs. | Exact or near-exact |
| He afterward tells the husband that it is his turn | He says, “ahora te toca a ti” and orders him to fulfill his duty as a Christian husband. | Near-exact translation |

The important result is not merely that an assault occurs. The novel explicitly represents it as
a right claimed by the lord, and the two principal lines rendered by Barbero are present in the
Spanish text. Barbero compresses the intervening narration but does not invent the essential
dialogue or sequence.

## Ledger decision

The initial automated recommendation described the passage as `paraphrase_summary`. That value is
not part of the repository schema. The ledger uses `near-direct` because Barbero closely translates
two recoverable lines while summarizing the action between them.

The resulting Q-001 treatment is:

```yaml
quotation_kind: near-direct
original_language: es
original_text: >-
  En uso del derecho que como señor tuyo me corresponde, he decidido yacer con tu mujer en su
  primera noche. […] Ahora te toca a ti. […] ¡Cumple como un buen esposo cristiano!
translation: >-
  In exercise of the right that belongs to me as your lord, I have decided to lie with your wife
  on her first night. […] Now it is your turn. […] Do your duty as a good Christian husband!
confidence: high
status: resolved
verdict: confirmed
source_replacement: eligible
human_reviewed: false
```

The bracketed ellipses disclose that the ledger joins two discontinuous dialogue excerpts. The
replacement remains unapproved until a human checks the transcription and translation against the
supplied e-text.

## Limitation

This note records the full-text extraction supplied during the editorial session. The ePub itself
is not stored in the repository, and the extracted wording was not independently collated against
a second edition. The absence of stable pagination makes the chapter heading and scene description
the best available locator.
