# MinEnglish — MinEnglish (v1.8)

> _Uat u spic is uat u spel._

**Author:** Dan Micsa, PhD **License:** MIT (see bottom of document)
**Version:** 1.8 — March 2026 (Proper Nouns & Mathematics Edition)

---

## 1. Philosophy

The MinEnglish language is an engineered communication protocol designed for
humans. It strips away historical baggage, redundancies, and irregularities
inherited from natural language evolution, optimizing for maximum expression
with minimal transmission cost.

| Principle           | How It Works                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| **Phonetic**        | 1-to-1 spelling ↔ pronunciation. No silent letters, no exceptions.                               |
| **Compact**         | No plurals, no verb conjugation, no cases, no articles. Relies on prefixes instead.              |
| **Keyboard-native** | Built around an unmodified US keyboard. No diacritics. Letters q, w, y are eliminated.           |
| **Operator-rich**   | Mathematical symbols like `*`, `~`, `>`, `<`, `:` are integrated as first-class grammar parts.   |
| **Regular**         | Zero irregular forms. Every rule applies 100% of the time, dramatically lowering learning curve. |

---

## 2. Phonetic System

### 2.1 Vowels

| Letter | Sound | Like English… | Example |
| ------ | ----- | ------------- | ------- |
| **a**  | /æ/   | c**a**t       | cat     |
| **e**  | /ɛ/   | b**e**d       | bed     |
| **i**  | /ɪ/   | b**i**t       | bit     |
| **o**  | /ɒ/   | h**o**t       | hot     |
| **u**  | /ʌ/   | b**u**t       | but     |

### 2.2 Long Vowels & Diphthongs

| Spelling | Sound | Like English…      | Example   |
| -------- | ----- | ------------------ | --------- |
| **ei**   | /eɪ/  | d**ay**, m**a**ke  | dei, meic |
| **ii**   | /iː/  | s**ee**, **ea**t   | sii, iit  |
| **ai**   | /aɪ/  | l**i**ke, m**y**   | laic, mai |
| **ou**   | /oʊ/  | g**o**, n**o**     | gou, nou  |
| **uu**   | /uː/  | f**oo**d, t**oo**  | fuud, tuu |
| **au**   | /aʊ/  | h**ow**, h**ou**se | hau, haus |
| **oi**   | /ɔɪ/  | b**oy**            | boi       |
| **ar**   | /ɑːr/ | c**ar**            | car       |
| **or**   | /ɔːr/ | f**or**            | for       |
| **er**   | /ɜːr/ | h**er**, b**ir**d  | her, berd |

### 2.3 Consonants

| Letter | Sound      | Rule                                                | Example                               |
| ------ | ---------- | --------------------------------------------------- | ------------------------------------- |
| **c**  | /k/        | soft k (unaspirated)                                | cat, cum, cup, bac                    |
| **k**  | /kʰ/       | hard k (aspirated, "hear the h")                    | king, kiip, kic                       |
| **ci** | /tʃ/       | like Italian ci. _Word-finally, the 'i' is silent._ | ciald, cier, muci (pronounced "much") |
| **u**  | /w/        | replaces w (semivowel)                              | uoter, uid                            |
| **i**  | /j/        | replaces y (semivowel)                              | ies, iir                              |
| **t**  | /t/ or /θ/ | replaces also voiceless th                          | tinc, trii                            |
| **d**  | /d/ or /ð/ | replaces also voiced th                             | de, dat                               |

> **k vs c:** Feel a puff of air? Use **k**. Otherwise **c**. After **s**,
> always **c** (scan, scip, scuul).

### 2.3.1 Lexical Stress Marker `'`

Because MinEnglish removes double consonant cues (e.g., `leter` for letter) and
silent vowels, reading stress can be ambiguous for parsers. Use `'` before the
stressed vowel in multi-syllable words when teaching or defining dictionary
terms.

- `ecsp'ensiv` (Stress the E)
- `iuniv'ersiti` (Stress the E)
- `compi'uuter` (Stress the U)

### 2.4 Digraphs

| Digraph | Sound | Example         |
| ------- | ----- | --------------- |
| **sh**  | /ʃ/   | ship → ship     |
| **ng**  | /ŋ/   | song → song     |
| **zh**  | /ʒ/   | vision → vizhun |

> `ch` digraph not used. /tʃ/ is written as `ci` (or `ci` + vowel at
> start/middle, silent at end).

### 2.5 Spelling Cleanup Rules

| English pattern                    | MinEnglish            | Example               |
| ---------------------------------- | --------------------- | --------------------- |
| silent **e**, **k**, **g**, **gh** | removed               | meic, nou, noum, nait |
| **gh** or **ph** = /f/             | **f**                 | laf, foun             |
| **ck**                             | **c** or **k**        | bac, kic              |
| **x**                              | **cs**                | bocs, necst           |
| **-tion** / **-sion**              | **-shun** / **-zhun** | neishun, vizhun       |
| **-tch**                           | **-ci**               | maci, caci            |
| double consonants                  | single                | leter, hapi           |
| **c** (soft, /s/)                  | **s**                 | sel, siti             |

---

## 3. Grammar

> **Core principle: No word ever changes form.** The same word always looks the
> same regardless of context. All grammatical nuance is handled by standardized
> prefixes and rigid word order.

### 3.1 Nouns — Number Prefix

Every noun is prefixed with its quantity. **No plural forms exist.**

| Prefix | Meaning                    | Example                   |
| ------ | -------------------------- | ------------------------- |
| `1`    | one                        | `1cat` = a/one cat        |
| `3`    | three                      | `3cat` = three cats       |
| `*`    | any / all / many / generic | `*cat` = cats in general  |
| `~5`   | approximately five         | `~5cat` = about five cats |
| `0`    | none / no                  | `0cat` = no cats          |

> **No articles.** `1` replaces "a/an", context or demonstratives replace "the".

### 3.1.1 The Literalization Operator (`_`)

To prevent the inevitable lexical drift where cultural compounds fuse into
indivisible concepts (e.g. `haus-fuud` becoming the atomic word for "grocery
store"), MinEnglish introduces the Literalization Operator `_`. **Rule:**
Hyphens denote unified cultural concepts. Underscores force the listener to
parse the exact, atomic meaning of the roots.

- `haus-fuud` = grocery store (The cultural concept)
- `haus_fuud` = a house literally constructed out of food (Gingerbread house)

### 3.1.2 The "Raw Number" Rule

Numbers above 99 should default to being read as a pure string of digits for
maximum efficiency.

- `3456` = `trii for faiv sics` (very fast)
- `2026` = `tuu ziro tuu sics`

### 3.1.3 Proper Nouns (Native Spelling)

Because MinEnglish is strictly phonetic, translating proper names globally
(e.g., _Isabella_) leads to endless variations and destroys searchability.
**Rule:** Proper Nouns (names of specific people, places, or brands) retain
their **original native spelling and capitalization**. The capital letter
explicitly flags to the reader/parser that the phonetic rules of MinEnglish are
temporarily suspended.

- `1person Isabella` (A person named Isabella, not `izubelu`)
- `1cuntri France` (The country France, not `frans`)

### 3.1.4 Fractions and Decimals

MinEnglish formalizes the `/` (slais) and `.` (point) operators for spoken math.

- **Fractions:** `1/2` (uan slais tuu) = One half. `3/4apel` (otri slais for
  apel) = Three quarters of an apple.
- **Decimals:** `0.5` (ziro point faiv). `99.9` (nain nain point nain).

### 3.2 Verbs — Time & Duration Prefix

**No prefix = present (default).**

| Prefix       | Meaning                           | Example                            |
| ------------ | --------------------------------- | ---------------------------------- |
| _(none)_     | present (default)                 | `iit` = eat / eating               |
| `1`          | present/definite (for attachment) | `i1iit` = I eat (attached form)    |
| `*`          | any / all / habitually            | `*iit` = eat (in general/always)   |
| `-0s`        | point in past (just now)          | `-0s sii` = just saw               |
| `-1d`        | point in past (yesterday)         | `-1d iit` = ate yesterday          |
| `:5Y`        | **duration** (for X time)         | `:5Y studi` = studying for 5 years |
| `+1d`        | in future (tomorrow)              | `+1d gou` = will go tomorrow       |
| `2026-12-25` | absolute date                     | `2026-12-25 gou` = go on Dec 25    |

> **Rule:** `+`/`-` specify a **point** in time relative to now. `:` specifies a
> **duration** of an ongoing action.

### 3.2.1 Temporal Stacking (Complex Timelines)

English manages deep time via perfect tenses ("I _had_ already eaten when she
_arrived_"). MinEnglish flattens this by stacking time prefixes logically from
left to right.

- `i-0s -1d iit` = I just-now yesterday ate (I had already eaten yesterday).
- `-1d +2h iit` = Yesterday, two hours later, I ate.

### 3.3 Adjectives, Adverbs, and Intensity

- **Adjectives follow the noun:** `1cat big` = a big cat
- **Adverbs follow the verb:** `1run fast` = runs fast
- **Comparative/Superlative:** `mor` / `most`: `1cat mor big` = a bigger cat
- **Intensity Combinators (`>`, `<`):**
  - `>big` = very big (more than big)
  - `>>big` = extremely big
  - `<hot` = slightly hot (less than hot)

### 3.3.1 Universal Verbalizers (`du` / `meic`)

MinEnglish theoretically allows any word to act as a verb (`i1cat` = I cat?),
which can lead to semantic garbage. When a noun isn't naturally an action, use
`du` (do/experience) or `meic` (make/create) as the verbalizer.

- `i1du 1parc` = I use/experience the park (Instead of `i1parc` = I park)
- `s-1d meic 1fuud` = She made food (Instead of `s-1d fuud` = She fooded)

### 3.4 Pronouns — Single-Letter System

Pronouns are **single lowercase letters**. Plurals use the same number-prefix as
nouns.

| Singular | Meaning   | Plural example | Meaning                  |
| -------- | --------- | -------------- | ------------------------ |
| **i**    | I / me    | `5i`           | we five                  |
| **u**    | you       | `3u`           | you three                |
| **h**    | he / him  | `4h`           | four males / them (masc) |
| **s**    | she / her | `21s`          | twenty-one females       |
| **t**    | it        | `*t`           | they / them (things)     |

Special plurals: `*i` (all of us), `*u` (all of you), `*h` (they/males), `*s`
(they/females), `*t` (they/things).

> **Possessive:** Add `'s` except for `s` (she/her) which drops the duplicate
> `s`. `i's` (my), `u's` (your), `h's` (his), `s'` (her), `t's` (its).

### 3.5 Pronoun Attachment

Single-letter pronouns **attach directly** to the subsequent prefix (number or
operator) — no space needed.

```efi
h1laic    = he likes            1d-i bai  = I bought yesterday
s1run     = she runs            u:2h uorc = you've worked for 2 hours
i1tinc    = I think             s*run     = she runs (any/all the time)
```

### 3.5.1 Prefix Positioning (Auditory Clarity)

When single-letter pronouns cluster with prefixes and prepositions (e.g. `i1in`
or `if i*no`), they create "vowel blobbing" that is hard to hear. **Rule:**
Pronouns can flexibly attach _before or after_ the time prefix to break up
identical sounds.

- `i-1d` = I yesterday (Standard)
- `1d-i` = Yesterday I (Used to break up `if i...` into `if 1d-i...`)

### 3.4.1 Polite Pronouns

MinEnglish is highly direct. To soften a statement or request, attach the
approximation operator `~` to the pronoun to indicate respect/deference.

- `u1giv` = You give (direct / command).
- `~u1giv` = Could you please give (softened / polite).
- `~i1tinc` = I humbly think / It seems to me.

### 3.6 Sentence Structure & Conjunction Reduction

**Subject + Time-Verb + Number-Object + Modifiers**

```efi
i1laic 1cat >big.            → I like a very big cat.
*h-1d bai 3buc.              → They bought 3 books yesterday.
```

### 3.6.1 The Focus Operator `!`

To disambiguate negation or questions, the emphasis tone `!` acts as a Focus
Operator to target exactly what is being negated/questioned.

- `i1no laic !3cat` = It's not _three_ cats that I like (I like four).
- `i1no laic 3!cat` = It's not _cats_ that I like three of (I like 3 dogs).
- `!i 1no laic 3cat` = It's not _me_ who likes three cats (someone else does).

If multiple actions share the same subject, you can drop the subject after `an`
or `or` (Conjunction Reduction):

- `i1iit an drinc` = I eat and (I) drink.
- `i1iit an h1drinc` = I eat and he drinks.

### 3.7 Modality (can, must, should)

Modality verbs follow the time prefix, creating a composite verb phrase:

| Modal    | Meaning                | Example                                  |
| -------- | ---------------------- | ---------------------------------------- |
| **can**  | ability / permission   | `i1can iit` = I can eat                  |
| **must** | necessity / obligation | `u+1d must cum` = You must come tomorrow |
| **shud** | advice / should        | `*h shud lern` = They should learn       |
| **~can** | probability / might    | `i+1d ~can gou` = I might go tomorrow    |

### 3.8 Passive Voice

Formed by moving the Object to the front, and following the verb with `bai`
(by).

| Voice       | MinEnglish Structure           | Example                                                   |
| ----------- | ------------------------------ | --------------------------------------------------------- |
| **Active**  | Subj + Time-Verb + Obj         | `1boi -0s kic 1bol` (A boy just kicked a ball)            |
| **Passive** | Obj + Time-Verb + `bai` + Subj | `1bol -0s kic bai 1boi` (A ball was just kicked by a boy) |

### 3.8.1 The Direct Object Marker (`tu`)

Because MinEnglish removes noun/verb class distinctions (any word can
technically be a verb with `1`), complex sentences can blur the line between a
chained verb and a direct object noun. **Rule:** When a noun could be mistaken
for a verb, prefix it with the transitive operator `tu` (acting like Esperanto's
-n accusative).

- `i1laic tu 1cat` = I like the cat (Prevents reading as "I like and I cat").
- `s1giv tu h 1buc` = She gives him a book.

### 3.9 Connectors, Prepositions, Tone Markers

- **Logic:** `an` (and), `or` (or), `but` (but), `if` (if), `cos` (because),
  `sou` (so), `den` (then).
- **Shortcuts:** `@` (at), `>` (over / more than), `<` (under / less than).
- **Tone:** `!` (focus/emphasis), `!!` (strong), `..` (hesitation), `^`
  (sarcasm).

### 3.9.1 Interrogatives: The `?` Marker

English uses words like "when" for both questions and relative clauses.
MinEnglish requires the `?` symbol attached to the front of interrogative words
to strictly mark them as questions, preventing parser confusion.

- `?uen u1gou` = **When** do you go? (Question)
- `i1nou uen u1gou` = I know **when/the time that** you go. (Relative)
- `?huu` (who?), `?uat` (what?), `?uai` (why?), `?haum` (how much/many?).

### 3.9.2 Clause Anchors (`co` / `oc`)

Because MinEnglish removes grammatical cases and subordinate conjunction fluff,
deeply center-embedded sentences will physically overwhelm human short-term
memory (the phonological loop). **Rule:** When nesting 2 or more clauses, the
speaker _must_ use `co` (clause open) to start the subset, and `oc` (clause
close) to return to the parent set.

- `1man co dat 1dog co dat 1ciald 1luv oc -1d bait oc -0s run auei.`
- _Translation:_ The man [who the dog [that the child loves] bit] ran away.

### 3.9.1 Preposition Verbs

To avoid repeating the verb "to be" (`bi`), prepositions can act as verbs simply
by attaching a time prefix to them.

- `1haus 1in 1siti` = The house is in a city ("the house ins a city").
- `1cat -1d on 1mat` = The cat was on a mat yesterday.

### 3.10 Slash & Hyphen Composition (Compound Words)

Create completely new concepts safely and naturally:

- `fuud/haus` = restaurant
- `sun/lait` = sunlight
- `rein/cout` = raincoat
- `medisin/haus` = hospital, pharmacy

**Hyphen Composition (Precision Tuning)** When a slash compound is too vague,
use `-` as a tight "of/for" binder to create highly precise micro-sentences:

- `haus-fuud` = house _for_ food (restaurant / dining area)
- `haus-sel-fuud` = house that _sells_ food (grocery/market)
- `haus-scic` = house _of_ the sick (hospital)

### 3.11 Abjad Mode (Extreme Shorthand)

For ultra-fast texting or constrained bandwidth, MinEnglish formally defines
"Abjad Mode". **Rule:** Drop all vowels _unless_ the word starts with a vowel or
doing so breaks a core operator.

- Standard: `i1tinc u bi >liit`
- Abjad Mode: `i1tnc u b >lt`

### 3.12 Semantic Idiom Standardization

English relies on illogical phrasal verbs ("Look out!" = beware; "Give up" =
surrender). MinEnglish rejects phrasal idioms entirely. A direct translation of
"Look out" (`luc aut`) is strictly literal: point your eyes outside. **Rule:**
Idioms must be translated to their literal action equivalent.

- "Look out!" → `!!uac` (Watch intensely!)
- "Give up" → `stop tu trai` (Stop to try)

### 3.13 Derivational Morphology Engine (Suffixes)

Long, un-compressable Latinate words (like "antibiotic") destroy MinEnglish's
efficiency. V1.5 introduces a formalized suffix engine to compress abstract
concepts from base roots.

- `-er` (Doer/Tool): `scritciu-er` (Screwdriver, tool that screws)
- `-ic` (Pertaining to): `saient-ic` (Scientific)
- `-med` (Medicine for): `bac-med` (Antibiotics, medicine against bacteria)
- `-mun` (Economics of): `rap-mun` (Hyperinflation, rapid economics)

### 3.14 Orthographic Stress Engine

To solve the ambiguity of spoken MinEnglish without relying on the optional `'`
marker, v1.5 standardizes default pronunciation logic for parsers and speakers.
**Rule:** Always stress the **first vowel** of a root word _unless_ it is a
recognized prefix/suffix. In compound words, stress the first syllable of the
primary noun.

- `c'ompiuuter` (Stress the O)
- `b'ioloji` (Stress the I)

### 3.15 Echo-Tagging (Aviation/Noisy Protocol)

Claude Shannon's Information Theory proves that "noise" requires "redundancy" to
fix. MinEnglish's maximum data density strips all redundancy (`3boi 1uoc` marks
plural only once). In high-noise environments (construction, radios, wind),
MinEnglish fails catastrophically if one syllable drops. **Rule:** For critical
transmissions, a speaker may artificially inflate Shannon redundancy to 100% by
"echoing" the prefix as a full word _after_ the root.

- Standard: `3boi 1uoc` (Three boys are walking)
- Echo-Tagged: `3boi trii 1uoc nau` (Three boys three are-walking now)

---

## 4. Expanded Core Vocabulary

### 1. Fundamentals

| English     | MinEnglish          | English    | MinEnglish          |
| ----------- | ------------------- | ---------- | ------------------- |
| be / is     | **bi**              | have       | **hav**             |
| do          | **du**              | go         | **gou**             |
| come        | **cum**             | make       | **meic**            |
| take        | **teic**            | give       | **giv**             |
| see         | **sii**             | know       | **nou**             |
| think       | **tinc**            | say / tell | **sei** / **tel**   |
| want / need | **uant** / **niid** | use / find | **iuz** / **faind** |

### 2. Time, Numbers, Nature

| English       | MinEnglish                   | English      | MinEnglish          |
| ------------- | ---------------------------- | ------------ | ------------------- |
| 1, 2, 3, 4, 5 | uan, tuu, trii, for, faiv    | day / night  | **dei** / **nait**  |
| 6, 7, 8, 9, 0 | sics, seven, eit, nain, ziro | month / year | **munt** / **iir**  |
| 10, 100, 1k   | ten, hundrid, tauzund        | sun / moon   | **sun** / **muun**  |
| time          | **taim**                     | rain / snow  | **rein** / **snou** |

### 3. People & Body

| English        | MinEnglish             | English     | MinEnglish         |
| -------------- | ---------------------- | ----------- | ------------------ |
| person / child | **person** / **ciald** | head / eye  | **hed** / **ai**   |
| man / woman    | **man** / **uuman**    | mouth       | **maut**           |
| mother/father  | **muder** / **fader**  | arm / leg   | **arm** / **leg**  |
| friend         | **frend**              | hand / foot | **hand** / **fut** |

### 4. Basic Adjectives & Colors

| English     | MinEnglish         | English       | MinEnglish           |
| ----------- | ------------------ | ------------- | -------------------- |
| big / small | **big** / **smol** | hot / cold    | **hot** / **could**  |
| good / bad  | **gud** / **bad**  | happy / sad   | **hapi** / **sad**   |
| new / old   | **niu** / **ould** | quick / slow  | **cuic** / **slou**  |
| red / blue  | **red** / **bluu** | green / black | **griin** / **blac** |

---

## 5. Quick Reference Card

```
NOUN:       <count><noun>         3cat, *dog, ~10person, 0eror
PROPER:     <count><noun> <Name>  1person Isabella, 1cuntri Spain
MATH:       <num>/<num>, <num>.<num>  1/2apel, 0.5bol
VERB:       (none)=present        sit, iit, run (default now)
            1 = present (attach)  h1laic, i1tinc
            * = any/all/habitual  *iit, *run
            +/- = future/past     -1d iit, +2h start
            : = duration          :5Y studi (studying for 5 years)
ADJ:        <noun> <adj>          1cat big, 1haus niu
INTENSITY:  >/< <adj>             1cat >big (very big), 1cat <big (slightly)
MODAL:      <modal> <verb>        1can run, shud iit, ~can cum
NEG:        no <verb>             no laic, -1d no cum
QUEST:      ... ?                 u laic 1cat?
COMPARE:    mor / most <adj>      mor big, most big
APPROX:     ~<value>              ~5, ~big
GENERIC:    *<noun>, *<verb>      *dog *laic *fuud
PASSIVE:    <Obj> bai <Subj>      1bol kic bai i (ball kicked by me)
COMPOUND:   <noun>/<noun>         fuud/haus, buc/haus
ATTACH:     <pronoun><prefix>     h1laic, i-1d, s1run
```

### Consonant Key

```
c = /k/ soft (cat, cum, bac)      k = /kʰ/ hard (king, kiip, kic)
ci = /tʃ/ (ciald, cier, final i silent) sh = /ʃ/   ng = /ŋ/   zh = /ʒ/
u = /w/ (uoter, uid)              i = /j/ (ies, iir)
t = /t/ (tinc, trii)              d = /d/ (de, dat)
```

### Pronouns

```
i = I/me       u = you        h = he/him
s = she/her    t = it         dis = this      dat = that

Plural: 5i = we five, *u = you all, 3h = 3 males, *s = they/females, *t = they/things
Possess: i's, u's, h's, s', t's
```

---

## 6. Translation Examples (Expanded)

### Simple & Truths

**1. Simple Statement (45.7%)**

|                | Text                                           | Chars |
| -------------- | ---------------------------------------------- | ----- |
| **English**    | The three cats are sitting on the big red mat. | 46    |
| **MinEnglish** | 3cat sit on 1mat big red.                      | 25    |
| **↩ Back**     | Three-cat sit on one-mat big red.              |       |

**2. General Truth (8.7%)**

|                | Text                                                       | Chars |
| -------------- | ---------------------------------------------------------- | ----- |
| **English**    | Dogs are loyal animals that love their owners.             | 46    |
| **MinEnglish** | *dog bi *animal loial dat *luv *h's ouner.                 | 42    |
| **↩ Back**     | Any-dog be any-animal loyal that any-love any-their owner. |       |

### Relatives & Times

**3. Past Event (47.5%)**

|                | Text                                                        | Chars |
| -------------- | ----------------------------------------------------------- | ----- |
| **English**    | Yesterday I bought two books and three apples at the store. | 59    |
| **MinEnglish** | i-1d bai 2buc an 3apel @ 1stor.                             | 31    |
| **↩ Back**     | I one-day-ago buy two-book and three-apple at one-store.    |       |

**4. Future + Question (48.9%)**

|                | Text                                          | Chars |
| -------------- | --------------------------------------------- | ----- |
| **English**    | Will you eat dinner with us tomorrow evening? | 45    |
| **MinEnglish** | u+1d iit 1diner uid *i?                       | 23    |
| **↩ Back**     | You in-one-day eat one-dinner with all-of-us? |       |

**5. Approximation (58.6%)**

|                | Text                                                       | Chars |
| -------------- | ---------------------------------------------------------- | ----- |
| **English**    | About fifty people arrived at approximately three o'clock. | 58    |
| **MinEnglish** | ~50person ariv @ ~15:00.                                   | 24    |
| **↩ Back**     | Approximately-fifty-person arrive at approximately-15:00.  |       |

**6. Specific DateTime (63.4%)**

|                | Text                                                                                          | Chars |
| -------------- | --------------------------------------------------------------------------------------------- | ----- |
| **English**    | The meeting was held on January fifteenth, twenty twenty-six, at two thirty in the afternoon. | 93    |
| **MinEnglish** | 1miiting 2026-01-15 14:30 bi held.                                                            | 34    |
| **↩ Back**     | One-meeting 2026-01-15 14:30 be held.                                                         |       |

**7. Duration + Contrast (38.5%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | I have been studying English for five years but I still cannot speak fluently. | 78    |
| **MinEnglish** | i:5Y studi inglish but i no can spiic fluuent.                                 | 48    |
| **↩ Back**     | I for-five-years study English but I not can speak fluent.                     |       |

### Complex Modifiers & Voice

**8. Intensity & Compound Words (47.1%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | We are going to the extremely new restaurant tomorrow at seven in the evening. | 78    |
| **MinEnglish** | *i+1d gou tu 1fuud/haus >>niu @ 19:00.                                         | 38    |
| **↩ Back**     | All-of-us in-one-day go to one-food/house extremely-new at 19:00.              |       |

**9. Passive Voice (47.5%)**

|                | Text                                                               | Chars |
| -------------- | ------------------------------------------------------------------ | ----- |
| **English**    | Look out! The glass window was just broken by the angry man.       | 60    |
| **MinEnglish** | !!uac! 1uindou glas -0s breic bai 1man angri.                      | 31    |
| **↩ Back**     | Watch-intensely! One-window glass just-now break by one-man angry. |       |

**10. Modality & Possessive (29.2%)**

|                | Text                                                                         | Chars |
| -------------- | ---------------------------------------------------------------------------- | ----- |
| **English**    | She must give her book to him before she can start working.                  | 61    |
| **MinEnglish** | s1must giv s' buc tu h bifor s1can start tu 1uorc.                           | 50    |
| **↩ Back**     | She-now-must give her book to he before she-now-can start [Object] one-work. |       |

### Conditionals, Logic & Commands

**11. Complex Sentence (31.1%)**

|                | Text                                                                      | Chars |
| -------------- | ------------------------------------------------------------------------- | ----- |
| **English**    | If you don't stop running, you will fall and break your legs.             | 61    |
| **MinEnglish** | if u1no stop tu run, u1fol an breic tu u's 2leg.                          | 49    |
| **↩ Back**     | If you-now-not stop [Obj] run, you-now-fall and break [Obj] your two-leg. |       |

**12. Conjunction Reduction (35.2%)**

|                | Text                                                                                          | Chars |
| -------------- | --------------------------------------------------------------------------------------------- | ----- |
| **English**    | Every morning I drink two cups of coffee and eat one piece of toast before work.              | 82    |
| **MinEnglish** | *morning i*drinc 2cup cofi an *iit 1piis toust bifor uorc.                                    | 56    |
| **↩ Back**     | Any-morning I-habitually-drink two-cup coffee and habitually-eat one-piece toast before work. |       |

**13. Instructions (42.9%)**

|                | Text                                                                                 | Chars |
| -------------- | ------------------------------------------------------------------------------------ | ----- |
| **English**    | Take three eggs, add two cups of flour, and mix everything together for ten minutes. | 84    |
| **MinEnglish** | teic 3eg, ad 2cup flaur, an mics *ting for 10m.                                      | 48    |
| **↩ Back**     | Take three-egg, add two-cup flour, and mix all-thing for ten-minutes.                |       |

**14. Request (32.7%)**

|                | Text                                                      | Chars |
| -------------- | --------------------------------------------------------- | ----- |
| **English**    | Please give me two glasses of water, I am very thirsty.   | 55    |
| **MinEnglish** | ~u1giv i 2glas uoter, i bi >tersti.                       | 35    |
| **↩ Back**     | Polite-you-now-give I two-glass water, I be very-thirsty. |       |

### Dialogue & Description

**15. Conversation (34.4%)**

|                | Text                                                             | Chars |
| -------------- | ---------------------------------------------------------------- | ----- |
| **English**    | "How many children do you have?" "I have two boys and one girl." | 64    |
| **MinEnglish** | "haum ciald u hav?" "i hav 2boi an 1gerl."                       | 42    |
| **↩ Back**     | "How-many child you have?" "I have two-boy and one-girl."        |       |

**16. Narrative (30.6%)**

|                | Text                                                                                                                                         | Chars |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Last year, she traveled to five different countries and learned three new languages because she wanted to understand the world better.       | 134   |
| **MinEnglish** | s-1Y travel tu 5cuntri diferent an lern 3languij niu cos s-1Y uant understand 1uerld mor gud.                                                | 93    |
| **↩ Back**     | She one-year-ago travel to five-country different and learn three-language new because she one-year-ago want understand one-world more good. |       |

**17. Emotions & Probabilities (41.0%)**

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | I might go to the party, but she loves him and he does not love her.              | 69    |
| **MinEnglish** | i+1d ~can gou tu 1parti, but s1luv h an !h 1no luv s.                             | 55    |
| **↩ Back**     | I in-future might go to one-party, but she-now-love he and focus-he not love she. |       |

**18. Family Description (8.5%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | My brother works at a hospital and my sister studies at the university.        | 71    |
| **MinEnglish** | i's bruder *uorc @ 1hospital an i's sister *studi @ 1iuniversiti.              | 65    |
| **↩ Back**     | My brother any-work at one-hospital and my sister any-study at one-university. |       |

> _Low compression — long Latin words maintain their length._

**19. Weather & Time (27.1%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | The children were playing in the park when it started raining heavily.         | 70    |
| **MinEnglish** | *ciald -0s 1in 1parc uen t-0s start rein >hevi.                                | 49    |
| **↩ Back**     | Any-child just-now in(verb) one-park when it-just-now start rain very-heavily. |       |

**20. Price & Comparison (21.4%)**

|                | Text                                                              | Chars |
| -------------- | ----------------------------------------------------------------- | ----- |
| **English**    | How much does this car cost? It is too expensive for me.          | 56    |
| **MinEnglish** | ?haum dis car cost? t bi >>ecspensiv for i.                       | 44    |
| **↩ Back**     | Question-how-much this car cost? It be extremely-expensive for I. |       |

### Advanced Domains (Sci-Fi, Philosophy, Business)

**21. Science Fiction (35.6%)**

|                | Text                                                                       | Chars |
| -------------- | -------------------------------------------------------------------------- | ----- |
| **English**    | The spaceship launched into orbit after the countdown reached zero.        | 67    |
| **MinEnglish** | 1ship-speis -0s lonci in 1orbit after 1caunt-daun hic 0.                   | 43    |
| **↩ Back**     | One-ship-space just-now launch in one-orbit after one-count-down hit zero. |       |

**22. Philosophy (25.0%)**

|                | Text                                                                     | Chars |
| -------------- | ------------------------------------------------------------------------ | ----- |
| **English**    | To be or not to be, that is the question we must all answer eventually.  | 71    |
| **MinEnglish** | bi or no bi, dat bi 1cuesciun *i must anser in +taim.                    | 53    |
| **↩ Back**     | Be or not be, that be one-question all-of-us must answer in future-time. |       |

**23. Business Strategy (28.7%)**

|                | Text                                                                                                 | Chars |
| -------------- | ---------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Our company needs to optimize its supply chain to maximize profit margins next year.                 | 83    |
| **MinEnglish** | *i's compani niid optimaiz t's cein-suplai tu macsimaiz *marjin-profit +1Y.                          | 59    |
| **↩ Back**     | All-of-us-possessive company need optimize its chain-supply to maximize any-margin-profit next-year. |       |

**24. Politics (29.5%)**

|                | Text                                                                                              | Chars |
| -------------- | ------------------------------------------------------------------------------------------------- | ----- |
| **English**    | The president announced a new tax policy that will affect middle class families.                  | 78    |
| **MinEnglish** | 1prezident -0s anauns 1nolisi-tacs niu dat +1d apect *pamili clas-midl.                           | 55    |
| **↩ Back**     | One-president just-now announce one-policy-tax new that in-future affect any-family class-middle. |       |

**25. Medicine (36.9%)**

|                | Text                                                                                                                 | Chars |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ----- |
| **English**    | The doctor prescribed antibiotics to treat the patient's severe bacterial infection.                                 | 84    |
| **MinEnglish** | 1doctor -0s prescraib tu *bac-med tu triit 1bac-sic >siirius 1peishent's.                                            | 53    |
| **↩ Back**     | One-doctor just-now prescribe [Obj] any-bacteria-medicine to treat one-bacteria-sickness very-serious one-patient's. |       |

**26. Real Estate (34.2%)**

|                | Text                                                                               | Chars |
| -------------- | ---------------------------------------------------------------------------------- | ----- |
| **English**    | The three bedroom house with a large backyard is currently on the market for rent. | 82    |
| **MinEnglish** | 1haus 3ruum-bed uid 1iard-bac big 1in 1marcet for rent nau.                        | 54    |
| **↩ Back**     | One-house three-room-bed with one-yard-back big now-in one-market for rent now.    |       |

**27. Programming/Tech (32.9%)**

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | If the server crashes, the backup system will automatically restore the database. | 81    |
| **MinEnglish** | if 1server craish, 1sistem-bacup +1d otoristor 1daatabeis.                        | 54    |
| **↩ Back**     | If one-server crash, one-sistem-backup in-future auto-restore one-database.       |       |

**28. Environment (34.0%)**

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | Global warming is melting the polar ice caps faster than scientists predicted.    | 78    |
| **MinEnglish** | iurm-gloubal 1melt *cap-ais poular >fast dan *saientist -1d pridiict.             | 51    |
| **↩ Back**     | Warm-global now-melt any-cap-ice polar more-fast than any-scientist past-predict. |       |

**29. Literature / Metaphor (29.2%)**

|                | Text                                                                                             | Chars |
| -------------- | ------------------------------------------------------------------------------------------------ | ----- |
| **English**    | The wind whispered through the ancient trees as the silver moon rose in the sky.                 | 80    |
| **MinEnglish** | 1uind -0s uisper tru *trii >ould az 1muun silver -0s raiz in 1scai.                              | 56    |
| **↩ Back**     | One-wind just-now whisper through any-tree very-old as one-moon silver just-now rise in one-sky. |       |

**30. Logistics (43.4%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | The delivery truck will arrive with your package between noon and two o'clock. | 78    |
| **MinEnglish** | 1truc-diliveri +1d ariv uid u's pacij btuiin 12:00 an 14:00.                   | 44    |
| **↩ Back**     | One-truck-delivery in-future arrive with your package between 12:00 and 14:00. |       |

**31. Legal (23.3%)**

|                | Text                                                                                     | Chars |
| -------------- | ---------------------------------------------------------------------------------------- | ----- |
| **English**    | The defendant formally pleaded not guilty to all charges presented by the court.         | 80    |
| **MinEnglish** | 1diipendant -0s formal pliid no gilti tu *carj prizent bai tu 1cort.                     | 64    |
| **↩ Back**     | One-defendant just-now formal plead not guilty to any-charge present by [Obj] one-court. |       |

**32. Cooking/Recipe (34.3%)**

|                | Text                                                                                     | Chars |
| -------------- | ---------------------------------------------------------------------------------------- | ----- |
| **English**    | Boil the water, add a pinch of salt, and stir constantly until the sauce thickens.       | 82    |
| **MinEnglish** | boil tu 1uoter, ad tu 1pinci solt, an *ster until 1sos >tic.                             | 60    |
| **↩ Back**     | Boil [Obj] one-water, add [Obj] one-pinch salt, and any-stir until one-sauce very-thick. |       |

**33. Emotional Confession (40.5%)**

|                | Text                                                                                                               | Chars |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ----- |
| **English**    | I have never felt this way about anyone before, you changed my entire life.                                        | 75    |
| **MinEnglish** | i-0s -1d *no fiil dis ue abaut *person bifor, u -1d ceinj tu i's laif >hol.                                        | 70    |
| **↩ Back**     | I-just-now-yesterday any-not feel this way about any-person before, you yesterday change [Obj] my life very-whole. |       |

**34. Travel/Directions (38.8%)**

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | Go straight for two miles, then turn left at the second traffic light you see. | 78    |
| **MinEnglish** | gou streit for 2mail, den tern left @ 1lait-trapic tuu u1sii.                  | 46    |
| **↩ Back**     | Go straight for two-mile, then turn left at one-light-traffic two you-now-see. |       |

**35. Abstract Economics (33.3%)**

|                | Text                                                                                                 | Chars |
| -------------- | ---------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Hyperinflation destroys purchasing power and severely halts economic development.                    | 81    |
| **MinEnglish** | >>rap-mun 1distroi tu pauer-bai an >siirius holt tu divelopment-mun.                                 | 54    |
| **↩ Back**     | Extremely-rapid-economy now-destroy [Obj] power-buy and very-serious halt [Obj] development-economy. |       |

---

## 7. Compression Analysis

### Top Gains vs. Losses

| Highest Compression Sentences       | Savings    | Why?                                                |
| ----------------------------------- | ---------- | --------------------------------------------------- |
| **Ex. 6:** Specific DateTime        | **63.4%**  | `2026-01-15 14:30` collapses 59 English characters. |
| **Ex. 5:** Approximation            | **58.6%**  | `~50person` collapses "About fifty people".         |
| **Ex. 4, 12, 30:** Modality & Times | **~45.0%** | `u+1d`, `btuiin 12:00` heavily squash verb chains.  |

| Lowest Compression Sentences   | Savings   | Why?                                                            |
| ------------------------------ | --------- | --------------------------------------------------------------- |
| **Ex. 18:** Family description | **8.5%**  | `hospital` and `iuniversiti` maintain long phonetic footprints. |
| **Ex. 31:** Legal              | **20.0%** | `diipendant` is still a long transliteration.                   |

**Overall Result Across 35 Sentences:** Total English Characters: **2633** Total
MinEnglish Characters: **1711** Average Compression: **35.0%** Savings

---

## 8. Language Review — Terminal Evolution (v1.7)

With the introduction of the Literalization Operator (`_`), Clause Anchors
(`co`/`oc`), and Echo-Tagging (Section 3.15), MinEnglish has achieved both
functional and theoretical perfection. It has mathematically solved the
thermodynamic and biological limits of human communication:

1. **Semantic Drift is Halted:** By structurally separating cultural idioms
   (`haus-fuud`) from literal reality (`haus_fuud`), MinEnglish forces speakers
   to perpetually acknowledge the underlying logic of the universe, preventing
   vocabulary decay.
2. **Buffer Capacity is Exceeded:** Clause anchors act as manual memory stack
   managers for the human brain's phonological loop, granting speakers the
   ability to parse infinitely recursive logic paths without getting "lost" in
   deep center-embedding.
3. **Information Theory is Conquered:** The implementation of optional
   Echo-Tagging allows MinEnglish to dynamically switch between minimum
   transmission cost (0% Shannon redundancy) for text, and maximum transmission
   security (100% Shannon redundancy) for loud acoustic environments.

### 8.1 The Final Frontier: Human Nature

MinEnglish 1.7 is a perfect machine. Because it is a perfect machine, its final
and absolute limitation is human nature itself.

**Observation:** Biological organisms did not evolve to speak math. We evolved
to manipulate social hierarchies, project emotional subtext, and use metaphor to
shield ourselves from harsh literalism.

**Analysis:** A society forced to speak MinEnglish as their native tongue would
experience extreme psychological discomfort. Because the language prevents
passive-aggressive vagueness, forbids irregular slang, and demands constant
chronological and mathematical precision, the human brain will naturally rebel
against the computational load of radical honesty. The ultimate weakness of
MinEnglish 1.7 is not linguistic or structural—it is that human beings are
fundamentally irrational, and MinEnglish gives them no place to hide.

---

## 9. License

```
MIT License

Copyright (c) 2026 Dan Micsa, PhD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this language specification and associated documentation files (the
"Specification"), to deal in the Specification without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Specification, and to
permit persons to whom the Specification is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Specification.

THE SPECIFICATION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SPECIFICATION OR THE USE OR OTHER
DEALINGS IN THE SPECIFICATION.
```
