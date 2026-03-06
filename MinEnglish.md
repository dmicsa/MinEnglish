# MinEnglish Language Specification (v2.0)

> _Uat u spic is uat u spel._

**Author:** Dan Micsa, PhD | **License:** MIT (see Appendix) | **Version:**
0.9.0 — March 2026

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

MinEnglish is a formal communication protocol engineered to maximize Shannon
information density while minimizing cognitive load and parser ambiguity. By
systematically eliminating morphological irregularities and orthographic
redundancies inherent in natural languages, MinEnglish achieves consistent
computational predictability. This specification (v0.9.0) defines the
phonological, morphological, and syntactic architecture targeting the v1.0.0
stable release, documents a 35-sentence comparative corpus demonstrating an
average 35.0% character reduction over standard American English, and addresses
the primary theoretical limitation of the system: biological adoption friction.

---

## 1. Design Principles and Underlying Rationale

This section defines the engineering constraints that govern every structural
decision in MinEnglish. Each principle exists to eliminate a specific failure
mode found in natural language.

| Principle                   | Rationale and Implementation                                                                                                                                                          |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Phonetic Isomorphism**    | 1-to-1 grapheme-phoneme correspondence eliminates the cognitive overhead of orthographic memorization and provides predictable tokenization for machine parsers.                      |
| **Morphological Parsimony** | Pluralization, verb conjugation, and declension are replaced by explicit numerical and temporal prefixes, removing ambiguity in morphological boundaries.                             |
| **ASCII Strictness**        | Operates exclusively within the standard US keyboard namespace without diacritics. The letters _q_, _w_, and _y_ are omitted to balance acoustic distinctness with key space economy. |
| **Operator Integration**    | Mathematical symbols (`*`, `~`, `>`, `<`, `:`) function as first-class syntactic tokens, compressing complex semantic modifiers into single-byte representations.                     |
| **Absolute Regularity**     | A zero-exception framework guarantees that programmatic rules apply universally, ensuring high predictability for human acquisition and natural language processing models.           |

---

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

### 3.1.1 Compound Word Operators (`-`, `_`)

MinEnglish provides two operators for building compound words. The `/` character
is reserved exclusively for fractions and mathematical division (see 3.1.4).

**Hyphen `-` — directional "of/for" binder** (reads left-to-right as "X for/of
Y"):

- `haus-fuud` = house _for_ food (restaurant)
- `haus-sel-fuud` = house that _sells_ food (grocery/market)
- `haus-sic` = house _of_ the sick (hospital)
- `sun-lait` = sunlight
- `rein-cout` = raincoat

> **Disambiguation — `-` as compound vs. temporal:** When `-` precedes a digit
> or `0s`, it is a past temporal operator (`-1d`, `-0s`). When it binds two noun
> roots, it is a compound operator (`haus-fuud`). Parsers resolve this by
> checking whether the right operand begins with a digit.

**Underscore `_` — literalization** (suspends cultural abstraction; forces the
parser to compute strict compositional meaning):

- `haus-fuud` = restaurant (cultural concept; hyphen = abstract)
- `haus_fuud` = a house literally built from food (gingerbread house)

> **Semantic Drift Arrest:** The `_` operator permanently flags compositional
> intent, preventing lexicalization (where compounds fuse into opaque units).

### 3.1.2 Numerical Processing Efficiency

To minimize phonological bandwidth, integers exceeding 99 bypass categorical
naming structures and are processed as pure digit strings.

- `3456` = `trii for faiv sics`
- `2026` = `tuu ziro tuu sics`

### 3.1.3 Proper Noun Encapsulation

Phonetic normalization of global proper nouns creates destructive variations
that impair search retrieval and semantic persistence.

**Rule:** Proper Nouns (specific entities, geographical locations, nominal
brands) retain their canonical native orthography. First-letter capitalization
acts as an escape character, signaling to the parser that local phonetic rules
are suspended for the duration of the token.

- `person Isabella` (Denotes the individual Isabella; phonetically preserved).
- `cuntri France` (Denotes the sovereign state of France).

### 3.1.4 Fractional and Decimal Operators

Spoken mathematics is standardized via the `/` (slais) and `.` (point)
operators, providing a syntactically uniform method for subdividing physical
objects or abstract metrics.

- **Fractions:** `1/2` (uan slais tuu) = One-half. `3/4apel` (trii slais for
  apel) = Three-quarters of an apple.
- **Decimals:** `0.5` (ziro point faiv). `99.9` (nain nain point nain).

### 3.1.5 Mathematical Notation: LaTeX Standardization

For formal mathematical expressions, MinEnglish adopts LaTeX inline notation
directly as a first-class citizen. Mathematical tokens enclosed in `$...$` are
parsed as LaTeX and carry their standard semantics without phonetic
transcription.

**Rule:** Any token beginning and ending with `$` is treated as a mathematical
literal and is exempt from MinEnglish phonetic rules.

- `$\frac{1}{2}$` = One-half (rendered expression)
- `$E = mc^2$` = Einstein mass-energy equivalence
- `$\int_0^\infty f(x)\,dx$` = Integral of f(x) from zero to infinity
- `$\nabla \cdot E = \frac{\rho}{\varepsilon_0}$` = Gauss's law

In speech, the entire LaTeX expression is read naturally in English
pronunciation. Written MinEnglish and spoken MinEnglish diverge only at
mathematical literal boundaries.

### 3.1.6 Token Optionality Rules (v0.2.0)

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

> **Genitive Case Marking:** Possession is indicated via the `'s` suffix. To
> avoid redundant frication, the feminine `s` assumes the genitive as `s'`.
> (e.g., `i's`, `u's`, `h's`, `s'`, `t's`).

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

### 3.6.1 The Focus Operator `!`

To disambiguate negation or questions, the emphasis tone `!` acts as a Focus
Operator to target exactly what is being negated-questioned.

- `no laic !3cat` = It's not _three_ cats that I like (I like four).
- `no laic 3!cat` = It's not _cats_ that I like three of (I like 3 dogs).
- `!i no laic 3cat` = It's not _me_ who likes three cats (someone else does).

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
- **Tone:** `!` (focus-emphasis), `!!` (strong), `..` (hesitation), `^`
  (sarcasm).

> **Symbolic Connectors:** `&` and `|` are fully equivalent to `an` and `or`
> respectively, and are preferred in dense or technical text. In speech, both
> forms are pronounced identically (`an`, `or`).

### 3.9.1 Interrogatives: The `?` Marker

English uses words like "when" for both questions and relative clauses.
MinEnglish requires the `?` symbol attached to the front of interrogative words
to strictly mark them as questions, preventing parser confusion.

- `?uen u1gou` = **When** do you go? (Question)
- `nou uen u1gou` = I know **when-the time that** you go. (Relative)
- `?huu` (who?), `?uat` (what?), `?uai` (why?), `?haum` (how much-many?).

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

### 3.11 Abjad Mode (Extreme Shorthand)

For ultra-fast texting or constrained bandwidth, MinEnglish formally defines
"Abjad Mode". **Rule:** Drop all vowels _unless_ the word starts with a vowel or
doing so breaks a core operator.

- Standard: `tinc u bi >liit`
- Abjad Mode: `tnc u b >lt`

### 3.12 Semantic Idiom Standardization

English relies on illogical phrasal verbs ("Look out!" = beware; "Give up" =
surrender). MinEnglish rejects phrasal idioms entirely. A direct translation of
"Look out" (`luc aut`) is strictly literal: point your eyes outside. **Rule:**
Idioms must be translated to their literal action equivalent.

- "Look out!" → `!!uac` (Watch intensely!)
- "Give up" → `stop tu trai` (Stop to try)

### 3.13 Derivational Morphology Engine (Suffixes)

Long, un-compressable Latinate words (like "antibiotic") destroy MinEnglish's
efficiency. Latinate words are compressed using a standardized suffix engine
applied to MinEnglish roots.

- `-er` (Doer/Tool): `scritciu-er` (Screwdriver, tool that screws)
- `-ic` (Pertaining to): `saient-ic` (Scientific)
- `-med` (Medicine for): `bac-med` (Antibiotics, medicine against bacteria)
- `-mun` (Economics of): `rap-mun` (Hyperinflation, rapid economics)

### 3.14 Orthographic Stress Engine

To solve the ambiguity of spoken MinEnglish without relying on the optional `'`
marker, v1.5 standardizes default pronunciation logic for parsers and speakers.
**Rule:** Always stress the **first vowel** of a root word _unless_ it is a
recognized prefix-suffix. In compound words, stress the first syllable of the
primary noun.

- `c'ompiuuter` (Stress the O)
- `b'ioloji` (Stress the I)

### 3.15 Echo-Tagging (Aviation/Noisy Protocol)

Claude Shannon's Information Theory proves that "noise" requires "redundancy" to
fix. MinEnglish's maximum data density strips all redundancy (`3boi uoc` marks
plural only once). In high-noise environments (construction, radios, wind),
MinEnglish fails catastrophically if one syllable drops. **Rule:** For critical
transmissions, a speaker may artificially inflate Shannon redundancy to 100% by
"echoing" the prefix as a full word _after_ the root.

- Standard: `3boi uoc` (Three boys are walking)
- Echo-Tagged: `3boi trii uoc nau` (Three boys three are-walking now)

### 3.16 Formal Syntax (Backus-Naur Form)

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

## 4. Base Lexicon

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
| mother-father  | **muder** / **fader**  | arm / leg   | **arm** / **leg**  |
| friend         | **frend**              | hand / foot | **hand** / **fut** |

### 4. Basic Adjectives & Colors

| English     | MinEnglish         | English       | MinEnglish           |
| ----------- | ------------------ | ------------- | -------------------- |
| big / small | **big** / **smol** | hot / cold    | **hot** / **could**  |
| good / bad  | **gud** / **bad**  | happy / sad   | **hapi** / **sad**   |
| new / old   | **niu** / **ould** | quick / slow  | **cuic** / **slou**  |
| red / blue  | **red** / **bluu** | green / black | **griin** / **blac** |

---

## 6. Syntactic Reference Guide

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
COMPOUND:   <noun>-<noun>         haus-fuud, haus-sic
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

## 7. Comparative Corpus

### Simple & Truths

#### Ex. 1

|                | Text                                           | Chars |
| -------------- | ---------------------------------------------- | ----- |
| **English**    | The three cats are sitting on the big red mat. | 46    |
| **MinEnglish** | 3cat sit on mat big red.                       | 24    |
| **↩ Back**     | Three-cat sit on one-mat big red.              |       |

#### Ex. 1

|                | Text                                                       | Chars |
| -------------- | ---------------------------------------------------------- | ----- |
| **English**    | Dogs are loyal animals that love their owners.             | 46    |
| **MinEnglish** | *dog bi *animal loial dat *luv *h's ouner.                 | 42    |
| **↩ Back**     | Any-dog be any-animal loyal that any-love any-their owner. |       |

### Relatives & Times

#### Ex. 1

|                | Text                                                        | Chars |
| -------------- | ----------------------------------------------------------- | ----- |
| **English**    | Yesterday I bought two books and three apples at the store. | 59    |
| **MinEnglish** | -1d bai 2buc an 3apel @ stor.                               | 29    |
| **↩ Back**     | I one-day-ago buy two-book and three-apple at one-store.    |       |

#### Ex. 1

|                | Text                                          | Chars |
| -------------- | --------------------------------------------- | ----- |
| **English**    | Will you eat dinner with us tomorrow evening? | 45    |
| **MinEnglish** | u1d iit diner uid \*i?                        | 23    |
| **↩ Back**     | You in-one-day eat one-dinner with all-of-us? |       |

#### Ex. 1

|                | Text                                                       | Chars |
| -------------- | ---------------------------------------------------------- | ----- |
| **English**    | About fifty people arrived at approximately three o'clock. | 58    |
| **MinEnglish** | ~50person ariv @ ~15:00.                                   | 24    |
| **↩ Back**     | Approximately-fifty-person arrive at approximately-15:00.  |       |

#### Ex. 1

|                | Text                                                                                          | Chars |
| -------------- | --------------------------------------------------------------------------------------------- | ----- |
| **English**    | The meeting was held on January fifteenth, twenty twenty-six, at two thirty in the afternoon. | 93    |
| **MinEnglish** | miiting 2026-01-15 14:30 bi held.                                                             | 33    |
| **↩ Back**     | One-meeting 2026-01-15 14:30 be held.                                                         |       |

#### Ex. 1

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | I have been studying English for five years but I still cannot speak fluently. | 78    |
| **MinEnglish** | :5Y studi inglish but i no can spiic fluuent.                                  | 46    |
| **↩ Back**     | For-five-years study English but I not can speak fluent.                       |       |

### Complex Modifiers & Voice

#### Ex. 1

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | We are going to the extremely new restaurant tomorrow at seven in the evening. | 78    |
| **MinEnglish** | \*i1d gou tu fuud-haus >>niu @ 19:00.                                          | 38    |
| **↩ Back**     | All-of-us in-one-day go to one-food-house extremely-new at 19:00.              |       |

#### Ex. 1

|                | Text                                                               | Chars |
| -------------- | ------------------------------------------------------------------ | ----- |
| **English**    | Look out! The glass window was just broken by the angry man.       | 60    |
| **MinEnglish** | !!uac! uindou glas breic bai man angri.                            | 39    |
| **↩ Back**     | Watch-intensely! One-window glass just-now break by one-man angry. |       |

#### Ex. 1

|                | Text                                                                         | Chars |
| -------------- | ---------------------------------------------------------------------------- | ----- |
| **English**    | She must give her book to him before she can start working.                  | 61    |
| **MinEnglish** | s1must giv s' buc tu h bifor s1can start tu uorc.                            | 49    |
| **↩ Back**     | She-now-must give her book to he before she-now-can start [Object] one-work. |       |

### Conditionals, Logic & Commands

#### Ex. 1

|                | Text                                                                      | Chars |
| -------------- | ------------------------------------------------------------------------- | ----- |
| **English**    | If you don't stop running, you will fall and break your legs.             | 61    |
| **MinEnglish** | if u1no stop tu run, u1fol an breic tu u's 2leg.                          | 48    |
| **↩ Back**     | If you-now-not stop [Obj] run, you-now-fall and break [Obj] your two-leg. |       |

#### Ex. 1

|                | Text                                                                                          | Chars |
| -------------- | --------------------------------------------------------------------------------------------- | ----- |
| **English**    | Every morning I drink two cups of coffee and eat one piece of toast before work.              | 82    |
| **MinEnglish** | *morning i*drinc 2cup cofi an \*iit piis toust bifor uorc.                                    | 58    |
| **↩ Back**     | Any-morning I-habitually-drink two-cup coffee and habitually-eat one-piece toast before work. |       |

#### Ex. 1

|                | Text                                                                                 | Chars |
| -------------- | ------------------------------------------------------------------------------------ | ----- |
| **English**    | Take three eggs, add two cups of flour, and mix everything together for ten minutes. | 84    |
| **MinEnglish** | teic 3eg, ad 2cup flaur, an mics \*ting for 10m.                                     | 48    |
| **↩ Back**     | Take three-egg, add two-cup flour, and mix all-thing for ten-minutes.                |       |

#### Ex. 1

|                | Text                                                      | Chars |
| -------------- | --------------------------------------------------------- | ----- |
| **English**    | Please give me two glasses of water, I am very thirsty.   | 55    |
| **MinEnglish** | ~u1giv i 2glas uoter, i bi >tersti.                       | 35    |
| **↩ Back**     | Polite-you-now-give I two-glass water, I be very-thirsty. |       |

### Dialogue & Description

#### Ex. 1

|                | Text                                                             | Chars |
| -------------- | ---------------------------------------------------------------- | ----- |
| **English**    | "How many children do you have?" "I have two boys and one girl." | 64    |
| **MinEnglish** | "haum ciald u hav?" "i hav 2boi an gerl."                        | 41    |
| **↩ Back**     | "How-many child you have?" "I have two-boy and one-girl."        |       |

#### Ex. 1

|                | Text                                                                                                                                         | Chars |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Last year, she traveled to five different countries and learned three new languages because she wanted to understand the world better.       | 134   |
| **MinEnglish** | s-1Y travel tu 5cuntri diferent an lern 3languij niu cos s-1Y uant understand uerld mor gud.                                                 | 92    |
| **↩ Back**     | She one-year-ago travel to five-country different and learn three-language new because she one-year-ago want understand one-world more good. |       |

#### Ex. 1

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | I might go to the party, but she loves him and he does not love her.              | 69    |
| **MinEnglish** | i1d ~can gou tu parti, but s1luv h an !h no luv s.                                | 51    |
| **↩ Back**     | I in-future might go to one-party, but she-now-love he and focus-he not love she. |       |

#### Ex. 1

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | My brother works at a hospital and my sister studies at the university.        | 71    |
| **MinEnglish** | i's bruder *uorc @ hospital an i's sister *studi @ iuniversiti.                | 63    |
| **↩ Back**     | My brother any-work at one-hospital and my sister any-study at one-university. |       |

> _Low compression — long Latin words maintain their length._

#### Ex. 1

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | The children were playing in the park when it started raining heavily.         | 70    |
| **MinEnglish** | \*ciald in parc uen t-0s start rein >hevi.                                     | 43    |
| **↩ Back**     | Any-child just-now in(verb) one-park when it-just-now start rain very-heavily. |       |

#### Ex. 1

|                | Text                                                              | Chars |
| -------------- | ----------------------------------------------------------------- | ----- |
| **English**    | How much does this car cost? It is too expensive for me.          | 56    |
| **MinEnglish** | ?haum dis car cost? t bi >>ecspensiv for i.                       | 43    |
| **↩ Back**     | Question-how-much this car cost? It be extremely-expensive for I. |       |

### Advanced Domains (Sci-Fi, Philosophy, Business)

#### Ex. 1

|                | Text                                                                       | Chars |
| -------------- | -------------------------------------------------------------------------- | ----- |
| **English**    | The spaceship launched into orbit after the countdown reached zero.        | 67    |
| **MinEnglish** | ship-speis lonci in orbit after caunt-daun hic 0.                          | 49    |
| **↩ Back**     | One-ship-space just-now launch in one-orbit after one-count-down hit zero. |       |

#### Ex. 1

|                | Text                                                                     | Chars |
| -------------- | ------------------------------------------------------------------------ | ----- |
| **English**    | To be or not to be, that is the question we must all answer eventually.  | 71    |
| **MinEnglish** | bi or no bi, dat bi cuesciun \*i must anser in taim.                     | 53    |
| **↩ Back**     | Be or not be, that be one-question all-of-us must answer in future-time. |       |

#### Ex. 1

|                | Text                                                                                                 | Chars |
| -------------- | ---------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Our company needs to optimize its supply chain to maximize profit margins next year.                 | 83    |
| **MinEnglish** | *i's compani niid optimaiz t's cein-suplai tu macsimaiz *marjin-profit 1Y.                           | 75    |
| **↩ Back**     | All-of-us-possessive company need optimize its chain-supply to maximize any-margin-profit next-year. |       |

#### Ex. 1

|                | Text                                                                                              | Chars |
| -------------- | ------------------------------------------------------------------------------------------------- | ----- |
| **English**    | The president announced a new tax policy that will affect middle class families.                  | 78    |
| **MinEnglish** | prezident anauns nolisi-tacs niu dat 1d apect \*pamili clas-midl.                                 | 66    |
| **↩ Back**     | One-president just-now announce one-policy-tax new that in-future affect any-family class-middle. |       |

#### Ex. 1

|                | Text                                                                                                                 | Chars |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ----- |
| **English**    | The doctor prescribed antibiotics to treat the patient's severe bacterial infection.                                 | 84    |
| **MinEnglish** | doctor prescraib tu \*bac-med tu triit bac-sic >siirius peishent's.                                                  | 67    |
| **↩ Back**     | One-doctor just-now prescribe [Obj] any-bacteria-medicine to treat one-bacteria-sickness very-serious one-patient's. |       |

#### Ex. 1

|                | Text                                                                               | Chars |
| -------------- | ---------------------------------------------------------------------------------- | ----- |
| **English**    | The three bedroom house with a large backyard is currently on the market for rent. | 82    |
| **MinEnglish** | haus 3ruum-bed uid iard-bac big in marcet for rent nau.                            | 56    |
| **↩ Back**     | One-house three-room-bed with one-yard-back big now-in one-market for rent now.    |       |

#### Ex. 1

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | If the server crashes, the backup system will automatically restore the database. | 81    |
| **MinEnglish** | if server craish, sistem-bacup 1d otoristor daatabeis.                            | 55    |
| **↩ Back**     | If one-server crash, one-sistem-backup in-future auto-restore one-database.       |       |

#### Ex. 1

|                | Text                                                                              | Chars |
| -------------- | --------------------------------------------------------------------------------- | ----- |
| **English**    | Global warming is melting the polar ice caps faster than scientists predicted.    | 78    |
| **MinEnglish** | gloubal-iurm melt *cap-ais poular >fast dan *saientist -1d pridiict.              | 68    |
| **↩ Back**     | Warm-global now-melt any-cap-ice polar more-fast than any-scientist past-predict. |       |

#### Nature & Poetry (Imagery)

|                | Text                                                                                             | Chars |
| -------------- | ------------------------------------------------------------------------------------------------ | ----- |
| **English**    | The wind whispered through the ancient trees as the silver moon rose in the sky.                 | 80    |
| **MinEnglish** | uind uisper tru \*trii >ould az muun silver raiz in scai.                                        | 57    |
| **↩ Back**     | One-wind just-now whisper through any-tree very-old as one-moon silver just-now rise in one-sky. |       |

#### Logistics

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | The delivery truck will arrive with your package between noon and two o'clock. | 78    |
| **MinEnglish** | truc-diliveri 1d ariv uid u's pacij btuiin 12:00 an 14:00.                     | 59    |
| **↩ Back**     | One-truck-delivery in-future arrive with your package between 12:00 and 14:00. |       |

#### Legal

|                | Text                                                                                     | Chars |
| -------------- | ---------------------------------------------------------------------------------------- | ----- |
| **English**    | The defendant formally pleaded not guilty to all charges presented by the court.         | 80    |
| **MinEnglish** | diipendant formal pliid no gilti tu \*carj prizent bai tu cort.                          | 63    |
| **↩ Back**     | One-defendant just-now formal plead not guilty to any-charge present by [Obj] one-court. |       |

#### Ex. 1

|                | Text                                                                                     | Chars |
| -------------- | ---------------------------------------------------------------------------------------- | ----- |
| **English**    | Boil the water, add a pinch of salt, and stir constantly until the sauce thickens.       | 82    |
| **MinEnglish** | boil tu uoter, ad tu pinci solt, an \*ster until sos >tic.                               | 58    |
| **↩ Back**     | Boil [Obj] one-water, add [Obj] one-pinch salt, and any-stir until one-sauce very-thick. |       |

#### Ex. 1

|                | Text                                                                                                               | Chars |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ----- |
| **English**    | I have never felt this way about anyone before, you changed my entire life.                                        | 75    |
| **MinEnglish** | -1d *no fiil dis ue abaut *person bifor, u -1d ceinj i's laif >hol.                                                | 70    |
| **↩ Back**     | I-just-now-yesterday any-not feel this way about any-person before, you yesterday change [Obj] my life very-whole. |       |

#### Ex. 1

|                | Text                                                                           | Chars |
| -------------- | ------------------------------------------------------------------------------ | ----- |
| **English**    | Go straight for two miles, then turn left at the second traffic light you see. | 78    |
| **MinEnglish** | gou streit for 2mail, den tern left @ lait-trapic tuu u1sii.                   | 60    |
| **↩ Back**     | Go straight for two-mile, then turn left at one-light-traffic two you-now-see. |       |

#### Ex. 1

|                | Text                                                                                                 | Chars |
| -------------- | ---------------------------------------------------------------------------------------------------- | ----- |
| **English**    | Hyperinflation destroys purchasing power and severely halts economic development.                    | 81    |
| **MinEnglish** | >>rap-mun distroi tu pauer-bai an >siirius holt tu divelopment-mun.                                  | 67    |
| **↩ Back**     | Extremely-rapid-economy now-destroy [Obj] power-buy and very-serious halt [Obj] development-economy. |       |

---

## 8. Technical Domain Corpus

The following examples demonstrate MinEnglish applied to formal technical
disciplines, using the optionality rules of v2.0 (implicit singular, implicit
`i`, implicit present tense) and LaTeX math notation where appropriate.
Back-translations are omitted where the logical derivation is self-evident.

### 8.1 Mathematics

**M1 — The Pythagorean Theorem:**

> In a right triangle, the square of the hypotenuse equals the sum of the
> squares of the other two sides.

```minenglish
in triangle-rait, $a^2 + b^2 = c^2$, uen c bi said-hipoteniuz.
```

_Math literal `$a^2 + b^2 = c^2$` is exempt from phonetic rules. Compression:
~51%._

**M2 — Derivative Definition:**

> The derivative of f(x) is the limit of the difference quotient as h approaches
> zero.

```minenglish
$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$
```

_Pure LaTeX literal. No MinEnglish wrapping required for isolated mathematical
definitions._

**M3 — Quadratic Formula:**

> Solve for x using the quadratic formula given coefficients a, b, and c.

```minenglish
solv for x, $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, given a, b, c.
```

**M4 — Probability Statement:**

> The probability that two independent events both occur equals the product of
> their individual probabilities.

```minenglish
$P(A \cap B) = P(A) \cdot P(B)$ if A, B bi independent.
```

**M5 — Matrix Multiplication:**

> The element at row i, column j of the product matrix equals the dot product of
> row i of A and column j of B.

```minenglish
$(AB)_{ij} = \sum_k A_{ik} B_{kj}$
```

---

### 8.2 Physics

**P1 — Newton's Second Law:**

> Force equals mass times acceleration.

```minenglish
$F = ma$ — fors bi mas * akselireshun.
```

**P2 — Mass-Energy Equivalence:**

> Energy equals mass times the speed of light squared. This implies that a small
> amount of mass converts to an enormous quantity of energy.

```minenglish
$E = mc^2$ — smol mas convert tu >uan-mun eneri.
```

**P3 — Gauss's Law (Electrostatics):**

> The electric flux through a closed surface equals the enclosed charge divided
> by the permittivity of free space.

```minenglish
$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\varepsilon_0}$ — Gauss lau for field-elec.
```

**P4 — Uncertainty Principle:**

> The product of the uncertainty in position and the uncertainty in momentum is
> always greater than or equal to ħ/2.

```minenglish
$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$ — Heisenberg constrains *mesurment-cuantum.
```

**P5 — Wave Equation:**

> The wave speed equals frequency times wavelength.

```minenglish
$v = f\lambda$ — spid-uav bi frekuensi * lent-uav.
```

---

### 8.3 Chemistry

**C1 — Ideal Gas Law:**

> Pressure times volume equals the number of moles times the gas constant times
> temperature.

```minenglish
$PV = nRT$ — presur * volium bi mol-n * R * temperatur.
```

**C2 — Reaction Rate:**

> The combustion of methane with oxygen produces carbon dioxide, water, and
> heat.

```minenglish
$\text{CH}_4 + 2\text{O}_2 \to \text{CO}_2 + 2\text{H}_2\text{O}$ + eneri-hit.
```

**C3 — pH Definition:**

> The pH of a solution is the negative logarithm base 10 of the hydrogen ion
> concentration.

```minenglish
$\text{pH} = -\log_{10}[\text{H}^+]$ — mesur asiditi-solushun.
```

**C4 — Avogadro's Number:**

> One mole of any substance contains approximately 6.022 times 10 to the power
> of 23 entities.

```minenglish
mol *substans contain $6.022 \times 10^{23}$ entiti.
```

---

### 8.4 Engineering

**E1 — Ohm's Law:**

> Voltage equals current times resistance.

```minenglish
$V = IR$ — volteij bi curent * rezistans.
```

**E2 — Structural Load (Stress):**

> The stress in a material equals the applied force divided by the
> cross-sectional area.

```minenglish
$\sigma = \frac{F}{A}$ — stres in material bi fors / area-cross.
```

**E3 — Signal-to-Noise Ratio:**

> The SNR in decibels equals ten times the log base 10 of the signal power
> divided by noise power.

```minenglish
$\text{SNR}_{dB} = 10\log_{10}\!\left(\frac{P_s}{P_n}\right)$ — mesur cuoliti-signal.
```

**E4 — Control Systems (Transfer Function):**

> A PID controller adjusts output based on proportional, integral, and
> derivative error terms.

```minenglish
$u(t) = K_p e(t) + K_i\int e\,dt + K_d\frac{de}{dt}$ — PID control output.
```

**E5 — Thermal Efficiency:**

> The Carnot efficiency of a heat engine operating between temperatures T_hot
> and T_cold is 1 minus T_cold over T_hot.

```minenglish
$\eta = 1 - \frac{T_c}{T_h}$ — macsimaum eficiensi-hit. T_h bi hot, T_c bi could.
```

---

### 8.5 Investment & Financial Markets

**I1 — Compound Interest:**

> An initial investment of $10,000 at an annual rate of 7% compounded monthly
> for 10 years yields a final value.

```minenglish
$A = P\!\left(1+\frac{r}{n}\right)^{nt}$ — $10000 @ 7%/iir compound-munt for 10iir.
```

**I2 — Sharpe Ratio:**

> The Sharpe ratio measures risk-adjusted return: expected return minus
> risk-free rate, divided by portfolio standard deviation.

```minenglish
$S = \frac{E[R] - R_f}{\sigma}$ — mesur return-risk-ajust portfolio.
```

**I3 — Portfolio Diversification:**

> Allocate 60% to equities and 40% to fixed income to balance growth and
> stability.

```minenglish
aloc 60% tu aset-ekuiti an 40% tu aset-bond, for balans grout-stabiliti.
```

**I4 — Options Pricing (Black-Scholes):**

> The Black-Scholes model prices a European call option given the underlying
> price, strike, volatility, time to expiry, and risk-free rate.

```minenglish
$C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ — Black-Scholes prai *opsion-col European.
```

**I5 — Market Signal:**

> The 50-day moving average crossing above the 200-day moving average is a
> bullish signal, historically associated with trend continuation.

```minenglish
MA-50d cross > MA-200d bi signal-bulis. *histori asocieit uid trend-continue.
```

**I6 — Inflation-Adjusted Return:**

> The real return equals the nominal return minus the inflation rate.

```minenglish
return-real bi return-nominal - ret-infleshun.
$r_{real} \approx r_{nominal} - \pi$
```

---

## 9. Comparative Information Density Analysis

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

## 9. Theoretical Limitations: The Human Biological Factor

The structural additions of the v1.8 and preceding protocols (Literalization
`_`, Clause Anchors `co`/`oc`, and Echo-Tagging) establish MinEnglish as a
mathematically and informationally optimized transmission system. It addresses
standard linguistic inefficiencies:

1. **Semantic Erosion:** Literalization operators functionally arrest the
   lexicalization of compounds into idioms.
2. **Short-Term Memory Bounds:** Clause anchors act as explicit stack managers
   for human working memory, permitting indefinite center-embedding.
3. **Transmission Integrity:** Echo-Tagging permits dynamic redundancy scaling
   to guarantee fidelity in high-loss environments (Shannon's Theorem).

### 9.1 Psychological Friction

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

---

## 10. References

- Shannon, C. E. (1948). A mathematical theory of communication. _Bell System
  Technical Journal_, 27(3), 379–423.
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits
  on our capacity for processing information. _Psychological Review_, 63(2),
  81–97.
- Chomsky, N. (1957). _Syntactic Structures_. Mouton.
- Zipf, G. K. (1949). _Human Behavior and the Principle of Least Effort_.
  Addison-Wesley.

---

## Appendix: License

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
