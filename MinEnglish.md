# MinEnglish Language Specification (v1.0.0)

> _Uat u spic is uat u spel._

**Author:** Dan Micsa, PhD (<<dmicsa@gmail.com>>) | **Repository:**
[GitHub](https://github.com/dmicsa/MinEnglish) | **License:** MIT (see Appendix)
| **Version:** 1.0.0 — March 2026

> **Versioning:** MinEnglish follows [Semantic Versioning](https://semver.org).
> `MAJOR.MINOR.PATCH` — breaking rule changes increment MAJOR. `0.x.y` indicates
> active pre-stable development; `1.0.0` marks the first frozen specification.

> **AI Attribution:** This specification was developed with extensive assistance
> from large language models. **Claude Opus** (Anthropic), **Gemini 2.5 Pro**
> (Google DeepMind), and **Antigravity** (Google DeepMind) contributed to the
> drafting, formalization, revision, and example generation documented herein.
> The intellectual framework, design decisions, and authorship remain those of
> the human author.

---

## Abstract

MinEnglish is a formal simplification and clarification of Modern English. Its
aim is to **remove** the inconsistencies, redundancies, and irregularities that
burden English — not to replace it with something foreign. The result is a
leaner, fully regular version of English: same vocabulary, same phonemes, same
word order — but with predictable spelling, explicit quantities, and precise
time operators. This specification (v1.0.0) documents the phonological,
morphological, and syntactic rules targeting the v1.0.0 stable release,
demonstrates a 35.0% average character reduction over standard English across a
35-sentence corpus, and acknowledges the primary adoption challenge: human
habit.

---

\newpage
## 1. Design Principles

> **Mission:** MinEnglish simplifies, clarifies, and formalizes Modern English.
> It removes constraints — it does not add them. Every rule below exists to
> **eliminate** an inconsistency or ambiguity already present in English.

| Principle               | What it removes from English                                                                                                                    |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Phonetic Spelling**   | Removes the burden of memorizing irregular spelling. Every letter has one sound, every sound one letter. (`knight` → `nait`, `enough` → `inuf`) |
| **Explicit Quantities** | Removes ambiguous pluralization. `cats` vs `cat` is a noise-channel problem. `3cat` is unambiguous. Singular is the default — no suffix needed. |
| **Regular Time**        | Removes 12+ irregular tense forms. One temporal operator (`-1d`, `1d`, `:5Y`) does the work of went/gone/had gone/will go/would have gone.      |
| **Symbolic Operators**  | Replaces multi-word constructs with single tokens already familiar from math and logic (`&`, `\|`, `>`, `<`, `~`, `@`).                         |
| **Zero Exceptions**     | Removes the entire category of irregular verbs, irregular plurals, and silent letters. What works for one word works for all words.             |

---

\newpage
## 2. Phonology and Orthography

### 2.1 Vowels

To ensure acoustic discernibility across diverse linguistic backgrounds, the
vowel space is constrained to five cardinal points:

| Grapheme | Phoneme | English Equivalent | Example |
| :------- | :------ | :----------------- | :------ |
| **a**    | /æ/     | c**a**t            | cat     |
| **e**    | /ɛ/     | b**e**d            | bed     |
| **i**    | /ɪ/     | b**i**t            | bit     |
| **o**    | /ɒ/     | h**o**t            | hot     |
| **u**    | /ʌ/     | b**u**t            | but     |

### 2.2 Long Vowels and Diphthongs

Diphthongs and elongated vowels are encoded as contiguous grapheme pairs,
preserving the 1-to-1 spelling mapping without requiring macron diacritics.

| Grapheme | Phoneme | English Equivalent | Example   |
| :------- | :------ | :----------------- | :-------- |
| **ei**   | /eɪ/    | d**ay**, m**a**ke  | dei, meic |
| **ii**   | /iː/    | s**ee**, **ea**t   | sii, iit  |
| **ai**   | /aɪ/    | l**i**ke, m**y**   | laic, mai |
| **ou**   | /oʊ/    | g**o**, n**o**     | gou, nou  |
| **uu**   | /uː/    | f**oo**d, t**oo**  | fuud, tuu |
| **au**   | /aʊ/    | h**ow**, h**ou**se | hau, haus |
| **oi**   | /ɔɪ/    | b**oy**            | boi       |
| **ar**   | /ɑːr/   | c**ar**            | car       |
| **or**   | /ɔːr/   | f**or**            | for       |
| **er**   | /ɜːr/   | h**er**, b**ir**d  | her, berd |

### 2.3 Consonants

Consonantal mappings prioritize acoustic clarity while resolving historical
orthographic collisions (such as the hard-soft _c_ boundary).

| Grapheme | Phoneme    | Application Rule                                                                   | Example            |
| :------- | :--------- | :--------------------------------------------------------------------------------- | :----------------- |
| **c**    | /k/        | Soft, unaspirated velar plosive.                                                   | cat, cum, cup, bac |
| **k**    | /kʰ/       | Hard, aspirated velar plosive.                                                     | king, kiip, kic    |
| **ci**   | /tʃ/       | Voiceless palato-alveolar affricate. The _i_ is phonetically null when word-final. | ciald, cier, muci  |
| **u**    | /w/        | Semivowel substitution for _w_.                                                    | uoter, uid         |
| **i**    | /j/        | Semivowel substitution for _y_.                                                    | ies, iir           |
| **t**    | /t/ or /θ/ | Alveolar plosive; assumes the voiceless dental fricative locally.                  | tinc, trii         |
| **d**    | /d/ or /ð/ | Alveolar plosive; assumes the voiced dental fricative locally.                     | de, dat            |

> **Aspiration Differentiation (`k` vs `c`):** The aspirated /kʰ/ is strictly
> represented by `k`, whereas the unaspirated variant uses `c`. Following
> sibilants (e.g., /s/), where aspiration naturally diminishes, `c` is mandated
> (e.g., _scan_, _scip_).

### 2.3.1 Lexical Prosody Marker (`'`)

Because MinEnglish eliminates the redundant double consonants and silent
terminal vowels often used as prosodic cues in natural English, lexical stress
can become ambiguous for computational parsers. The apostrophe (`'`) is
instituted as an optional prosody marker, to be affixed immediately preceding
the stressed vowel in pedagogy or lexicography.

- `ecsp'ensiv` (Stress alignment on the initial _e_)
- `iuniv'ersiti` (Stress alignment on the medial _e_)
- `compi'uuter` (Stress alignment on the first _u_)

### 2.4 Digraphs

| Digraph | Phoneme | Example         |
| :------ | :------ | :-------------- |
| **sh**  | /ʃ/     | ship → ship     |
| **ng**  | /ŋ/     | song → song     |
| **zh**  | /ʒ/     | vision → vizhun |

> Note: The standard English _ch_ (/tʃ/) is not utilized. It is strictly encoded
> as `ci` to maintain morphemic consistency.

### 2.5 Orthographic Normalization Constraints

To enforce the phonetic isomorphism principle, historical orthographic artifacts
must be algorithmically stripped.

| Historical Pattern                 | MinEnglish Normalization                 | Example               |
| :--------------------------------- | :--------------------------------------- | :-------------------- |
| Silent **e**, **k**, **g**, **gh** | Nullified                                | meic, nou, noum, nait |
| **gh** or **ph** rendered as /f/   | Regressive substitution to **f**         | laf, foun             |
| **ck** cluster                     | Resolved to **c** or **k** by aspiration | bac, kic              |
| **x** cluster                      | Decomposed to **cs**                     | bocs, necst           |
| **-tion** / **-sion**              | Phoneticized to **-shun** / **-zhun**    | neishun, vizhun       |
| **-tch**                           | Phoneticized to **-ci**                  | maci, caci            |
| Double consonants                  | Replaced with unitary equivalents        | leter, hapi           |
| Soft **c** (/s/)                   | Regressive substitution to **s**         | sel, siti             |

---

\newpage
## 3. Morphology and Syntax

> **Core Constraint: Morphological Invariance.** Lexical items never undergo
> morphological derivation or inflection. Grammatical relationships are managed
> exclusively through standardized operators and rigid syntactic ordering.

### 3.1 Nouns and Quantitative Prefixes

To eliminate the biological error-amplifier of plural suffixes (where the loss
of a terminal sibilant in a noisy channel alters the mathematical quantity of a
sentence), MinEnglish mandates explicit numerical prefixing. **Morphological
plurals are abolished.**

| Prefix | Semantic Value          | Example                           |
| :----- | :---------------------- | :-------------------------------- |
| `1`    | Unitary / Singular      | `1cat` (a cat)                    |
| `3`    | Exact enumeration       | `3cat` (three cats)               |
| `*`    | Universal / Generic set | `*cat` (cats, across all domains) |
| `~5`   | Approximate enumeration | `~5cat` (approximately five cats) |
| `0`    | Null set                | `0cat` (zero cats)                |

> **Absence of Articles:** The quantitative operator `1` functionally replaces
> the indefinite article. Definiteness is established contextually or via
> demonstrative pronouns.

### 3.1.1 Numerical Processing Efficiency

To minimize phonological bandwidth, integers exceeding 99 bypass categorical
naming structures and are processed as pure digit strings.

- `3456` = `trii for faiv sics`
- `2026` = `tuu ziro tuu sics`

### 3.1.2 Proper Noun Encapsulation

Phonetic normalization of global proper nouns creates destructive variations
that impair search retrieval and semantic persistence.

**Rule:** Proper Nouns (specific entities, geographical locations, nominal
brands) retain their canonical native orthography. First-letter capitalization
acts as an escape character, signaling to the parser that local phonetic rules
are suspended for the duration of the token.

- `person Isabella` (Denotes the individual Isabella; phonetically preserved).
- `cuntri France` (Denotes the sovereign state of France).

### 3.1.3 Fractional and Decimal Operators

Spoken mathematics is standardized via the `/` (slais) and `.` (point)
operators, providing a syntactically uniform method for subdividing physical
objects or abstract metrics.

- **Fractions:** `1/2` (uan slais tuu) = One-half. `3/4apel` (trii slais for
  apel) = Three-quarters of an apple.
- **Decimals:** `0.5` (ziro point faiv). `99.9` (nain nain point nain).

### 3.1.4 Token Optionality Rules (v0.2.0)

Three categories of token may be omitted when their value is recoverable from
context. **Parsers must implement the following defaults when a token is
absent:**

#### Rule A — Implicit Singular (`1` optional)

When no quantitative prefix is present before a noun, the parser defaults to
singular (`1`). The explicit `1` is required only when disambiguation from a
preceding plural context is necessary.

| Explicit            | Implicit          | Meaning              |
| :------------------ | :---------------- | :------------------- |
| `1cat sit on 1mat`  | `cat sit on mat`  | A cat sits on a mat  |
| `1dog run in 1parc` | `dog run in parc` | A dog runs in a park |

> **Note:** If the previous noun was plural, explicit `1` is required to
> re-establish singular: `3cat run, den 1cat stop.`

#### Rule B — Implicit First Person (`i` optional)

When the subject is first-person singular and the sentence structure is
declarative, the pronoun `i` may be omitted. The parser defaults to `i` when no
subject precedes the verb block.

| Explicit           | Implicit          | Meaning             |
| :----------------- | :---------------- | :------------------ |
| `i1laic cat`       | `laic cat`        | I like a cat        |
| `i-1d gou tu stor` | `-1d gou tu stor` | I went to the store |

> **Disambiguation:** If a third-person pronoun or noun immediately precedes the
> verb, `i` is not assumed. The implicit-I rule only fires when the verb begins
> the sentence.

#### Rule C — Implicit Present Tense (temporal marker optional)

A verb with no temporal prefix is already defined as present continuous.
Additionally, the discrete present marker `1` (as in `h1laic`) is also optional
when the subject is explicit and no tense ambiguity exists. The `1` attachment
is required only for disambiguation or emphasis.

| Explicit      | Implicit     | Meaning        |
| :------------ | :----------- | :------------- |
| `h1laic 1cat` | `h laic cat` | He likes a cat |
| `i1run fast`  | `run fast`   | I run fast     |

### 3.2 Verbs — Temporal Mechanics

Irregular conjugations are functionally inefficient. MinEnglish regulates time
via temporal operators that target an absolute mathematical timeline. A verb
without a temporal operator defaults to present continuous.

| Operator     | Temporal Value                            | Example                                         |
| :----------- | :---------------------------------------- | :---------------------------------------------- |
| _(null)_     | Present continuous (default)              | `iit` (eating)                                  |
| `1`          | Present discrete (attachment operator)    | `i1iit` (I eat)                                 |
| `*`          | Habitual / Universal continuity           | `*iit` (eats perpetually)                       |
| `-0s`        | Immediate past vector (zero offset)       | `-0s sii` (just perceived)                      |
| `-1d`        | Past vector (one day offset)              | `-1d iit` (ate yesterday)                       |
| `:5Y`        | Duration scalar (five years)              | `:5Y studi` (has studied for five years)        |
| `1d`         | Future vector (`+` accepted but optional) | `1d gou` (will go tomorrow)                     |
| `2026-12-25` | Absolute timestamp                        | `2026-12-25 gou` (transit scheduled for Dec 25) |

> **Direction Convention:** The `-` prefix marks past vectors (required). Future
> offsets default to positive — a bare numeric offset (`1d`, `2h`, `1Y`) always
> points forward. The `:` operator spans a duration rather than pointing to a
> discrete moment.

### 3.2.1 Temporal Stacking (Complex Timelines)

Natural language manages chronological depth via "perfect" tenses, increasing
syntactic distance between subject and action. MinEnglish resolves deep time by
permitting left-to-right stacking of temporal operators, enabling precise
algebraic timeline construction.

- `-0s -1d iit` = I just-now yesterday ate (I had already eaten by yesterday's
  timeline).
- `-1d 2h iit` = Yesterday, offset by +2 hours, I ate.

### 3.3 Modifiers and Scalar Intensity

- **Adjectival Ordering:** Adjectives strictly post-modify nouns (`cat big`).
- **Adverbial Ordering:** Adverbs post-modify verbs (`run fast`).
- **Comparative Mechanics:** Driven by scalar progression `mor` and `most`
  (`cat mor big`).
- **Intensity Combinators (`>`, `<`):**
  - `>big` = Positive scalar intensity (very big)
  - `>>big` = Extreme positive scalar intensity
  - `<hot` = Negative scalar intensity (slightly hot)

### 3.3.1 Universal Predicators (`du` / `meic`)

Because MinEnglish permits any token to accept an operational prefix,
inappropriate syntactic mapping can yield semantic anomalies. The universal
predicators `du` (experiential interaction) and `meic` (generative action) serve
as formal verbalizers for noun-class tokens.

- `du parc` = I interact with the park (replaces the ambiguous `parc`).
- `s-1d meic fuud` = She generated food (replaces the anomalous `s-1d fuud`).

### 3.4 Pronominal Indexing

Pronouns operate as highly compressed, single-character spatial indices.
Plurality logic inherits the identical numerical prefixing system utilized by
canonical nouns.

| Singular | Referent               | Plural Array | Array Referent              |
| :------- | :--------------------- | :----------- | :-------------------------- |
| **i**    | First-person singular  | `5i`         | First-person group (n=5)    |
| **u**    | Second-person singular | `3u`         | Second-person group (n=3)   |
| **h**    | Third-person masculine | `4h`         | Masculine demographic (n=4) |
| **s**    | Third-person feminine  | `21s`        | Feminine demographic (n=21) |
| **t**    | Third-person inanimate | `*t`         | Inanimate collective        |

> **Genitive Case Marking:** Possession is indicated universally via the `'s`
> suffix with no exceptions. (e.g., `i's`, `u's`, `h's`, `s's`, `t's`).

### 3.4.1 Syntactic Agglutination (Attachment)

For maximum data throughput, the single-character pronominal index agglutinates
physically to the succeeding temporal operator, eliminating whitespace parsing
overhead.

```efi
h1laic    (he likes)
s1run     (she runs)
u:2h uorc (you worked spanning two hours)
s*run     (she runs generically)
```

### 3.4.2 Auditory Disambiguation (Prefix Positioning)

Agglutination can generate overlapping vowel harmonics (e.g., `in` or
`if i*no`), increasing transmission error rates. To preserve auditory clarity
boundaries, pronominal indices have flexible positioning relative to the
temporal operator.

- Canonical: `i-1d` (I yesterday)
- Permuted: `1d-i` (Yesterday I; mitigates harmonic overlap after preceding
  vowels)

### 3.4.3 Pronominal Deference

By default, the syntactic structure is declarative and absolute. To inject
social deference or epistemological uncertainty, the approximation operator `~`
is bound to the pronoun.

- `u giv` = Absolute directive (You give).
- `~u giv` = Deferred directive (Could you please give).
- `~tinc` = Epistemological deferment (It seems to me).

### 3.5 Negation

Negation is expressed by prepending `no` immediately before the verb. The `no`
token is invariant and does not conjugate.

- `no laic cat` = I do not like the cat.
- `u1d no cum` = You will not come tomorrow.
- `*h no can spiic` = None of them can speak.

### 3.6 Sentence Structure & Conjunction Reduction

**Subject + Time-Verb + Number-Object + Modifiers**

```efi
laic cat >big.            → I like a very big cat.
*h-1d bai 3buc.              → They bought 3 books yesterday.
```

### 3.6.1 Conjunction Reduction

If multiple actions share the same subject, you can drop the subject after `an`
or `or` (Conjunction Reduction):

- `iit an drinc` = I eat and (I) drink.
- `iit an h1drinc` = I eat and he drinks.

### 3.7 Modality (can, must, should)

Modality verbs follow the time prefix, creating a composite verb phrase:

| Modal    | Meaning                | Example                                 |
| -------- | ---------------------- | --------------------------------------- |
| **can**  | ability / permission   | `can iit` = I can eat                   |
| **must** | necessity / obligation | `u1d must cum` = You must come tomorrow |
| **shud** | advice / should        | `*h shud lern` = They should learn      |
| **~can** | probability / might    | `i1d ~can gou` = I might go tomorrow    |

### 3.8 Passive Voice

Formed by moving the Object to the front, and following the verb with `bai`
(by).

| Voice       | MinEnglish Structure           | Example                                             |
| ----------- | ------------------------------ | --------------------------------------------------- |
| **Active**  | Subj + Time-Verb + Obj         | `boi kic bol` (A boy just kicked a ball)            |
| **Passive** | Obj + Time-Verb + `bai` + Subj | `bol kic bai boi` (A ball was just kicked by a boy) |

### 3.8.1 The Direct Object Marker (`tu`)

Because MinEnglish removes noun-verb class distinctions (any word can
technically be a verb with `1`), complex sentences can blur the line between a
chained verb and a direct object noun. **Rule:** When a noun could be mistaken
for a verb, prefix it with the transitive operator `tu` (acting like Esperanto's
-n accusative).

- `laic tu cat` = I like the cat (Prevents reading as "I like and I cat").
- `s1giv tu h buc` = She gives him a book.

### 3.9 Connectors, Prepositions, Tone Markers

- **Logic:** `an` / `&` (and), `or` / `|` (or), `but` (but), `if` (if), `cos`
  (because), `sou` (so), `den` (then).
- **Shortcuts:** `@` (at), `>` (over / more than), `<` (under / less than).
- **Tone:** `!` (emphasis), `?` (question), `..` (hesitation), `^` (sarcasm).

> **Symbolic Connectors:** `&` and `|` are fully equivalent to `an` and `or`
> respectively, and are preferred in dense or technical text. In speech, both
> forms are pronounced identically (`an`, `or`).

### 3.9.1 Terminal Punctuation (`?`, `!`)

To maintain familiarity and avoid syntactic overcomplication, MinEnglish uses
the standard English terminal punctuation marks (`?` and `!`) located at the end
of the sentence clause.

- `uen u1gou?` = **When** do you go?
- `uac!` = Watch out!
- `huu`, `uat`, `uai`, `haum` (who, what, why, how much-many).

### 3.9.2 Clause Anchors (`co` / `oc`)

Because MinEnglish removes grammatical cases and subordinate conjunction fluff,
deeply center-embedded sentences will physically overwhelm human short-term
memory (the phonological loop). **Rule:** When nesting 2 or more clauses, the
speaker _must_ use `co` (clause open) to start the subset, and `oc` (clause
close) to return to the parent set.

- `man co dat dog co dat ciald luv oc -1d bait oc run auei.`
- _Translation:_ The man [who the dog [that the child loves] bit] ran away.

### 3.9.3 Arithmetic & Logical Operator Inventory

MinEnglish formally adopts five symbolic operators as first-class syntactic
tokens. `/` is reserved for fractions and math (see 3.1.4) and is **not** a
compound word operator.

| Operator | Name      | Primary Role                               | Example                     |
| :------- | :-------- | :----------------------------------------- | :-------------------------- |
| `+`      | Plus      | Future offset (optional; bare N = default) | `1d gou` = will go tomorrow |
| `-`      | Minus     | Past offset (required) / compound binder   | `-1d iit`; `haus-fuud`      |
| `*`      | Star      | Universal / generic quantifier             | `*cat` = all cats           |
| `&`      | Ampersand | Logical AND (≡ `an`)                       | `laic cat & dog`            |
| `\|`     | Pipe      | Logical OR (≡ `or`)                        | `laic cat \| dog`           |

> `*i` means "all of us" (universal quantifier on first-person pronoun) — not
> habitual verb. When `*` prefixes a pronoun it quantifies it; when it prefixes
> a verb it marks habitual action. Parsers distinguish by token class.

### 3.9.4 Preposition Verbs

To avoid repeating the verb "to be" (`bi`), prepositions can act as verbs simply
by attaching a time prefix to them.

- `haus in siti` = The house is in a city (`in` acts as the verb "to be in").
- `cat -1d on mat` = The cat was on a mat yesterday.

### 3.10 Abjad Mode (Extreme Shorthand)

For ultra-fast texting or constrained bandwidth, MinEnglish formally defines
"Abjad Mode". **Rule:** Drop all vowels _unless_ the word starts with a vowel or
doing so breaks a core operator.

- Standard: `tinc u bi >liit`
- Abjad Mode: `tnc u b >lt`

### 3.11 Semantic Idiom Standardization

English relies on illogical phrasal verbs ("Look out!" = beware; "Give up" =
surrender). MinEnglish rejects phrasal idioms entirely. A direct translation of
"Look out" (`luc aut`) is strictly literal: point your eyes outside. **Rule:**
Idioms must be translated to their literal action equivalent.

- "Look out!" → `!!uac` (Watch intensely!)
- "Give up" → `stop tu trai` (Stop to try)

### 3.12 Derivational Morphology Engine (Suffixes)

Long, un-compressable Latinate words (like "antibiotic") destroy MinEnglish's
efficiency. Latinate words are compressed using a standardized suffix engine
applied to MinEnglish roots.

- `-er` (Doer/Tool): `scritciu-er` (Screwdriver, tool that screws)
- `-ic` (Pertaining to): `saient-ic` (Scientific)
- `-med` (Medicine for): `bac-med` (Antibiotics, medicine against bacteria)
- `-mun` (Economics of): `rap-mun` (Hyperinflation, rapid economics)

### 3.13 Orthographic Stress Engine

To solve the ambiguity of spoken MinEnglish without relying on the optional `'`
marker, v0.9.0 standardizes default pronunciation logic for parsers and
speakers. **Rule:** Always stress the **first vowel** of a root word _unless_ it
is a recognized prefix-suffix. In compound words, stress the first syllable of
the primary noun.

- `c'ompiuuter` (Stress the O)
- `b'ioloji` (Stress the I)

### 3.14 Echo-Tagging (Aviation/Noisy Protocol)

Claude Shannon's Information Theory proves that "noise" requires "redundancy" to
fix. MinEnglish's maximum data density strips all redundancy (`3boi uoc` marks
plural only once). In high-noise environments (construction, radios, wind),
MinEnglish fails catastrophically if one syllable drops. **Rule:** For critical
transmissions, a speaker may artificially inflate Shannon redundancy to 100% by
"echoing" the prefix as a full word _after_ the root.

- Standard: `3boi uoc` (Three boys are walking)
- Echo-Tagged: `3boi trii uoc nau` (Three boys three are-walking now)

### 3.15 Formal Syntax (Backus-Naur Form)

The absolute regularity of MinEnglish allows it to be algorithmically validated.
Below is the strict parsing configuration for a standard declarative sentence.

```ebnf
<sentence>      ::= [<subject_block>] <verb_block> [<object_block>] [<modifier_block>]...
<subject_block> ::= <noun_phrase> | <pronoun_phrase>
<object_block>  ::= <noun_phrase> | <pronoun_phrase>

<noun_phrase>   ::= <quantity> <noun_root> [<adjective_phrase>]
<pronoun_phrase>::= [<quantity>] <pronoun_root>
<adjective_phrase> ::= [<intensity>] <adjective_root>

<verb_block>    ::= [<temporal_vector>] <verb_root> [<adverb_phrase>]
<temporal_vector> ::= <time_prefix> | <duration_prefix> | <unix_timestamp>

<clause>        ::= "co" <connective> <sentence> "oc"
```

---

\newpage
## 4. Base Lexicon

### 4.1 Fundamentals

| English     | MinEnglish          | English    | MinEnglish          |
| ----------- | ------------------- | ---------- | ------------------- |
| be / is     | **bi**              | have       | **hav**             |
| do          | **du**              | go         | **gou**             |
| come        | **cum**             | make       | **meic**            |
| take        | **teic**            | give       | **giv**             |
| see         | **sii**             | know       | **nou**             |
| think       | **tinc**            | say / tell | **sei** / **tel**   |
| want / need | **uant** / **niid** | use / find | **iuz** / **faind** |

### 4.2 Time, Numbers, Nature

| English       | MinEnglish                   | English      | MinEnglish          |
| ------------- | ---------------------------- | ------------ | ------------------- |
| 1, 2, 3, 4, 5 | uan, tuu, trii, for, faiv    | day / night  | **dei** / **nait**  |
| 6, 7, 8, 9, 0 | sics, seven, eit, nain, ziro | month / year | **munt** / **iir**  |
| 10, 100, 1k   | ten, hundrid, tauzund        | sun / moon   | **sun** / **muun**  |
| time          | **taim**                     | rain / snow  | **rein** / **snou** |

### 4.3 People & Body

| English        | MinEnglish             | English     | MinEnglish         |
| -------------- | ---------------------- | ----------- | ------------------ |
| person / child | **person** / **ciald** | head / eye  | **hed** / **ai**   |
| man / woman    | **man** / **uuman**    | mouth       | **maut**           |
| mother-father  | **muder** / **fader**  | arm / leg   | **arm** / **leg**  |
| friend         | **frend**              | hand / foot | **hand** / **fut** |

### 4.4 Basic Adjectives & Colors

| English     | MinEnglish         | English       | MinEnglish           |
| ----------- | ------------------ | ------------- | -------------------- |
| big / small | **big** / **smol** | hot / cold    | **hot** / **could**  |
| good / bad  | **gud** / **bad**  | happy / sad   | **hapi** / **sad**   |
| new / old   | **niu** / **ould** | quick / slow  | **cuic** / **slou**  |
| red / blue  | **red** / **bluu** | green / black | **griin** / **blac** |

---

\newpage
## 5. Syntactic Reference Guide

```
NOUN:       <count><noun>         3cat, *dog, ~10person, 0eror
PROPER:     <count><noun> <Name>  person Isabella, cuntri Spain
MATH:       <num>/<num>, <num>.<num>  1/2apel, 0.5bol
VERB:       (none)=present        sit, iit, run (default now)
            1 = present (attach)  h1laic, tinc
            * = any/all/habitual  *iit, *run
            Nd = future (+ optional)  1d gou, 2h start
            -Nd = past            -1d iit, -2h
            : = duration          :5Y studi (studying for 5 years)
ADJ:        <noun> <adj>          cat big, haus niu
INTENSITY:  >/< <adj>             cat >big (very big), cat <big (slightly)
MODAL:      <modal> <verb>        can run, shud iit, ~can cum
NEG:        no <verb>             no laic, -1d no cum
QUEST:      ... ?                 u laic cat?
COMPARE:    mor / most <adj>      mor big, most big
APPROX:     ~<value>              ~5, ~big
GENERIC:    *<noun>, *<verb>      *dog *laic *fuud
PASSIVE:    <Obj> bai <Subj>      bol kic bai i (ball kicked by me)
ATTACH:     <pronoun><prefix>     h1laic, -1d, s1run
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
i = I/me       u = you        h = he-him
s = she-her    t = it         dis = this      dat = that

Plural: 5i = we five, *u = you all, 3h = 3 males, *s = they-females, *t = they-things
Possess: i's, u's, h's, s', t's
```

---

\newpage
## 6. Comparative Corpus

### Simple & Truths

#### Ex. 1

```text
EN: The three cats are sitting on the big red mat. (46)
ME: 3cat sit on mat big red. (24)
BT: Three-cat sit on one-mat big red.
```

> **Compression:** 47.8% Δ
>
> **Observation:** High compression achieved via removal of definite articles,
> auxiliary verbs, and strict phonetic normalization.

#### Ex. 2

```text
EN: Dogs are loyal animals that love their owners. (46)
ME: *dog bi *animal loial dat *luv *h's ouner. (42)
BT: Any-dog be any-animal loyal that any-love any-their owner.
```
 8.7% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

### Relatives & Times

#### Ex. 3

```text
EN: Yesterday I bought two books and three apples at the store. (59)
ME: -1d bai 2buc an 3apel @ stor. (29)
BT: I one-day-ago buy two-book and three-apple at one-store.
```

---

> **Compression:** 50.8% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

\newpage
## 7. Comparative Information Density Analysis

The transmission efficiency (information density) of MinEnglish was modeled
against a 35-sentence standard English corpus. Efficiency is measured locally in
byte-length (character count reduction).

### Top Compression Vectors vs. Deficits

| Highest Reductions                  | Char Δ     | Variable Vector                                                                                 |
| :---------------------------------- | :--------- | :---------------------------------------------------------------------------------------------- |
| **Ex. 6:** Absolute Timestamp       | **63.4%**  | `2026-01-15 14:30` collapses 59 English alphabetical characters into absolute numeric notation. |
| **Ex. 5:** Approximation            | **58.6%**  | `~50person` collapses multi-word approximation phrases ("About fifty people").                  |
| **Ex. 4, 12, 30:** Modality & Tense | **~45.0%** | Prefixing operators (`1d`, `btuiin 12:00`) computationally squash auxiliary verb chains.        |

| Lowest Reductions               | Char Δ    | Variable Vector                                                                                        |
| :------------------------------ | :-------- | :----------------------------------------------------------------------------------------------------- |
| **Ex. 18:** Lexical Description | **8.5%**  | Base nouns of Latinate origin (`hospital`, `iuniversiti`) maintain protracted phonetic transcriptions. |
| **Ex. 31:** Legal Domain        | **20.0%** | Domain-specific transliterations (`diipendant`, `carj`) resist operator optimization.                  |

**Corpus Density Metric (n=35):**

- Total Standard English Bytes (Chars): **2633**
- Total MinEnglish Bytes (Chars): **1711**
- Average Information Density Gain (Length Reduction): **35.0%**

---

\newpage
## 8. Theoretical Limitations: The Human Biological Factor

The structural additions of the v1.8 and preceding protocols (Literalization
`_`, Clause Anchors `co`/`oc`, and Echo-Tagging) establish MinEnglish as a
mathematically and informationally optimized transmission system. It addresses
standard linguistic inefficiencies:

1. **Short-Term Memory Bounds:** Clause anchors act as explicit stack managers
   for human working memory, permitting indefinite center-embedding.
2. **Transmission Integrity:** Echo-Tagging permits dynamic redundancy scaling
   to guarantee fidelity in high-loss environments (Shannon's Theorem).

### 8.1 Psychological Friction

The primary identified limitation of MinEnglish exists externally to its
syntactic structure; the limitation is biological. Mammalian communicative
pathways evolved to facilitate social cohesion, hierarchical navigation, and
emotional subtext, often utilizing ambiguity to reduce friction.

MinEnglish's computational design enforces an objective, algebraic paradigm. The
absolute requirement for temporal precision, numerical exactness, and the
prohibition of metaphorical obfuscation inherently conflicts with natural human
cognitive behavior. Widespread neurological adoption of MinEnglish natively
would likely prompt measurable psychological resistance, as the protocol
disables the linguistic mechanisms humans rely on to process and mitigate
sociological complexity.

### 8.2 Global Formalization Standards

As MinEnglish is designed to be a mathematically and informationally optimized
transmission system, it inherently relies on existing, globally accepted
objective standards to eliminate ambiguity. We strongly recommend that all
implementations, translations, and corpus generations of MinEnglish strictly
adhere to the following universal formalisms:

1. **Chronometry:** All temporal references should default to Universal
   Coordinated Time (UTC) or Universal Standard Time (UST) representations
   (e.g., `14:30Z`).
2. **Measurement:** Only the International System of Units (SI / Metric System)
   should be utilized for weights, measures, distances, and volumes.
3. **Mathematics:** Equations, variable definitions, and complex mathematical
   relationships should be expressed natively in LaTeX syntax to avoid ad-hoc
   lexical transcriptions.
4. **Dates:** Adherence strictly to the ISO 8601 standard (`YYYY-MM-DD`).

---

\newpage
## 9. References

- Shannon, C. E. (1948). A mathematical theory of communication. _Bell System
  Technical Journal_, 27(3), 379–423.
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits
  on our capacity for processing information. _Psychological Review_, 63(2),
  81–97.
- Chomsky, N. (1957). _Syntactic Structures_. Mouton.
- Zipf, G. K. (1949). _Human Behavior and the Principle of Least Effort_.
  Addison-Wesley.
- Ogden, C. K. (1930). _Basic English: A General Introduction with Rules and Grammar_. Kegan Paul.
- Zamenhof, L. L. (1887). _Dr. Esperanto's International Language_.
- Pinker, S. (1994). _The Language Instinct: How the Mind Creates Language_. William Morrow.
- Sapir, E. (1921). _Language: An Introduction to the Study of Speech_. Harcourt, Brace.

---

\newpage
## Appendix A: Full Comparative Corpus

#### Ex. 4

```text
EN: Will you eat dinner with us tomorrow evening? (45)
ME: u1d iit diner uid \*i? (22)
BT: You in-one-day eat one-dinner with all-of-us?
```
 51.1% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 5

```text
EN: About fifty people arrived at approximately three o'clock. (58)
ME: ~50person ariv @ ~15:00. (24)
BT: Approximately-fifty-person arrive at approximately-15:00.
```

> **Compression:** 58.6% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 6

```text
EN: The meeting was held on January fifteenth, twenty twenty-six, at two thirty in the afternoon. (93)
ME: miiting 2026-01-15 14:30 bi held. (33)
BT: One-meeting 2026-01-15 14:30 be held.
```
 64.5% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 7

```text
EN: I have been studying English for five years but I still cannot speak fluently. (78)
ME: :5Y studi inglish but i no can spiic fluuent. (45)
BT: For-five-years study English but I not can speak fluent.
```

> **Compression:** 42.3% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

### Complex Modifiers & Voice

#### Ex. 8

```text
EN: We are going to the extremely new restaurant tomorrow at seven in the evening. (78)
ME: \*i1d gou tu restaurant >>niu @ 19:00. (38)
BT: All-of-us in-one-day go to one-restaurant extremely-new at 19:00.
```
 51.3% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 9

```text
EN: Look out! The glass window was just broken by the angry man. (60)
ME: uac! uindou glas breic bai man angri. (39)
BT: Watch! One-window glass just-now break by one-man angry.
```

> **Compression:** 35.0% Δ
>
> **Observation:** Exclamatory prefixes (`!!`) enforce immediate semantic
> parsing, bypassing syntactic buildup.

#### Ex. 10

```text
EN: She must give her book to him before she can start working. (59)
ME: s1must giv s's buc tu h bifor s1can start tu uorc. (50)
BT: She-now-must give her book to he before she-now-can start [Object] one-work.
```
 15.3% Δ
>
> **Observation:** General lexical optimization and phonetic spelling reduction.

### Conditionals, Logic & Commands

#### Ex. 11

```text
EN: If you don't stop running, you will fall and break your legs. (61)
ME: if u1no stop tu run, u1fol an breic tu u's 2leg. (48)
BT: If you-now-not stop [Obj] run, you-now-fall and break [Obj] your two-leg.
```

> **Compression:** 21.3% Δ
>
> **Observation:** General lexical optimization and phonetic spelling reduction.

#### Ex. 12

```text
EN: Every morning I drink two cups of coffee and eat one piece of toast before work. (80)
ME: *morning i*drinc 2cup cofi an \*iit piis toust bifor uorc. (58)
BT: Any-morning I-habitually-drink two-cup coffee and habitually-eat one-piece toast before work.
```
 27.5% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

#### Ex. 13

```text
EN: Take three eggs, add two cups of flour, and mix everything together for ten minutes. (84)
ME: teic 3eg, ad 2cup flaur, an mics \*ting for 10m. (48)
BT: Take three-egg, add two-cup flour, and mix all-thing for ten-minutes.
```

> **Compression:** 42.9% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

#### Ex. 14

```text
EN: Please give me two glasses of water, I am very thirsty. (55)
ME: ~u giv i 2glas uoter, i bi >tersti. (35)
BT: Polite-you-give I two-glass water, I be very-thirsty.
```
 36.4% Δ
>
> **Observation:** Approximation operators (`~`) drastically reduce multi-word
> phrasings like "about" or "approximately".

### Dialogue & Description

#### Ex. 15

```text
EN: "How many children do you have?" "I have two boys and one girl." (64)
ME: "haum ciald u hav?" "i hav 2boi an gerl." (41)
BT: "How-many child you have?" "I have two-boy and one-girl."
```

> **Compression:** 35.9% Δ
>
> **Observation:** Interrogative prefixes condense investigative clauses into
> single tokens.

#### Ex. 16

```text
EN: Last year, she traveled to five different countries and learned three new languages because she wanted to understand the world better. (134)
ME: s-1Y travel tu 5cuntri diferent an lern 3languij niu cos s-1Y uant understand uerld mor gud. (92)
BT: She one-year-ago travel to five-country different and learn three-language new because she one-year-ago want understand one-world more good.
```
 31.3% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 17

```text
EN: I might go to the party, but she loves him and he does not love her. (68)
ME: i1d ~can gou tu parti, but s1luv h an h no luv s. (50)
BT: I in-future might go to one-party, but she-now-love he and he not love she.
```

> **Compression:** 26.5% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 18

```text
EN: My brother works at a hospital and my sister studies at the university. (71)
ME: i's bruder *uorc @ hospital an i's sister *studi @ iuniversiti. (63)
BT: My brother any-work at one-hospital and my sister any-study at one-university.
```

> _Low compression — long Latin words maintain their length._
 11.3% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

#### Ex. 19

```text
EN: The children were playing in the park when it started raining heavily. (70)
ME: \*ciald in parc uen t-0s start rein >hevi. (42)
BT: Any-child just-now in(verb) one-park when it-just-now start rain very-heavily.
```

> **Compression:** 40.0% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

#### Ex. 20

```text
EN: How much does this car cost? It is too expensive for me. (56)
ME: haum dis car cost? t bi >>ecspensiv for i. (43)
BT: How-much this car cost? It be extremely-expensive for I.
```
 23.2% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

### Advanced Domains (Sci-Fi, Philosophy, Business)

#### Ex. 21

```text
EN: The spaceship launched into orbit after the countdown reached zero. (67)
ME: speisship lonci in orbit after caunt-daun hic 0. (48)
BT: One-spaceship just-now launch in one-orbit after one-count-down hit zero.
```

> **Compression:** 28.4% Δ
>
> **Observation:** General lexical optimization and phonetic spelling reduction.

#### Ex. 22

```text
EN: To be or not to be, that is the question we must all answer eventually. (71)
ME: bi or no bi, dat bi cuesciun \*i must anser in taim. (52)
BT: Be or not be, that be one-question all-of-us must answer in future-time.
```
 26.8% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

#### Ex. 23

```text
EN: Our company needs to optimize its supply chain to maximize profit margins next year. (84)
ME: *i's compani niid optimaiz t's suplai-cein tu macsimaiz *marjin-profit 1Y. (74)
BT: All-of-us-possessive company need optimize its supply-chain to maximize any-margin-profit next-year.
```

> **Compression:** 11.9% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 24

```text
EN: The president announced a new tax policy that will affect middle class families. (80)
ME: prezident anauns tacs-polisi niu dat 1d apect \*pamili clas-midl. (65)
BT: One-president just-now announce one-tax-policy new that in-future affect any-family class-middle.
```
 18.8% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 25

```text
EN: The doctor prescribed antibiotics to treat the patient's severe bacterial infection. (84)
ME: doctor prescraib tu antibiotik tu triit bacteriel infecshun >siirius peishent's. (80)
BT: One-doctor just-now prescribe [Obj] one-antibiotic to treat one-bacterial-infection very-serious one-patient's.
```

> **Compression:** 4.8% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

#### Ex. 26

```text
EN: The three bedroom house with a large backyard is currently on the market for rent. (82)
ME: haus 3bedruum uid baciard big in marcet for rent nau. (53)
BT: One-house three-bedroom with one-backyard big now-in one-market for rent now.
```
 35.4% Δ
>
> **Observation:** General lexical optimization and phonetic spelling reduction.

#### Ex. 27

```text
EN: If the server crashes, the backup system will automatically restore the database. (81)
ME: if server craish, backup sistem 1d otoristor daatabeis. (55)
BT: If one-server crash, one-backup-system in-future auto-restore one-database.
```

> **Compression:** 32.1% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 28

```text
EN: Global warming is melting the polar ice caps faster than scientists predicted. (78)
ME: gloubal uorming melt *cap-ais poular >fast dan *saientist -1d pridiict. (71)
BT: Global-warming now-melt any-cap-ice polar more-fast than any-scientist past-predict.
```
 9.0% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 29

```text
EN: The wind whispered through the ancient trees as the silver moon rose in the sky. (80)
ME: uind uisper tru \*trii >ould az muun silver raiz in scai. (57)
BT: One-wind just-now whisper through any-tree very-old as one-moon silver just-now rise in one-sky.
```

> **Compression:** 28.7% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

#### Logistics

#### Ex. 30

```text
EN: The delivery truck will arrive with your package between noon and two o'clock. (78)
ME: diliveri truc 1d ariv uid u's pacij btuiin 12:00 an 14:00. (58)
BT: One-delivery-truck in-future arrive with your package between 12:00 and 14:00.
```
 25.6% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 31

```text
EN: The defendant formally pleaded not guilty to all charges presented by the court. (80)
ME: diipendant formal pliid no gilti tu \*carj prizent bai tu cort. (63)
BT: One-defendant just-now formal plead not guilty to any-charge present by [Obj] one-court.
```

> **Compression:** 21.3% Δ
>
> **Observation:** Universal deference operators (`*`) substitute complex plural
> or aggregate noun constraints.

#### Ex. 32

```text
EN: Boil the water, add a pinch of salt, and stir constantly until the sauce thickens. (82)
ME: boil tu uoter, ad tu pinci solt, an \*ster until sos >tic. (58)
BT: Boil [Obj] one-water, add [Obj] one-pinch salt, and any-stir until one-sauce very-thick.
```
 29.3% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

#### Ex. 33

```text
EN: I have never felt this way about anyone before, you changed my entire life. (75)
ME: -1d *no fiil dis ue abaut *person bifor, u -1d ceinj i's laif >hol. (67)
BT: I-just-now-yesterday any-not feel this way about any-person before, you yesterday change [Obj] my life very-whole.
```

> **Compression:** 10.7% Δ
>
> **Observation:** Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex
> tense architectures and prepositional phrases.

#### Ex. 34

```text
EN: Go straight for two miles, then turn left at the second traffic light you see. (78)
ME: gou streit for 2mail, den tern left @ trapic lait tuu u1sii. (60)
BT: Go straight for two-mile, then turn left at one-traffic-light two you-now-see.
```
 23.1% Δ
>
> **Observation:** General lexical optimization and phonetic spelling reduction.

#### Ex. 35

```text
EN: Hyperinflation destroys purchasing power and severely halts economic development. (81)
ME: >>haiperinflashun distroi tu pauer-bai an >siirius holt tu divelopment economik. (80)
BT: Extremely-hyperinflation now-destroy [Obj] power-buy and very-serious halt [Obj] development economic.
```

---

> **Compression:** 1.2% Δ **Observation:** Low compression due to retention of
> exact international academic vocabulary.

---
 1.2% Δ
>
> **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
> modifiers.

\newpage
## Appendix B: License

```
MIT License

Copyright (c) 2026 Dan Micsa, PhD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this language specification and associated documentation files (the
"Specification"), to deal in the Specification without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and-or sell copies of the Specification, and to
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
