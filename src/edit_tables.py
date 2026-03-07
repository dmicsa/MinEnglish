import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 2.1 Vowels
table_2_1_4col = '''| Grapheme | Phoneme | English Equivalent | Example |
| :------- | :------ | :----------------- | :------ |
| **a**    | /æ/     | c**a**t            | cat     |
| **e**    | /ɛ/     | b**e**d            | bed     |
| **i**    | /ɪ/     | b**i**t            | bit     |
| **o**    | /ɒ/     | h**o**t            | hot     |
| **u**    | /ʌ/     | b**u**t            | but     |'''

table_2_1_2col = '''| MinEnglish | English Equivalent |
| :--------- | :----------------- |
| **a** (/æ/) | c**a**t (cat) |
| **e** (/ɛ/) | b**e**d (bed) |
| **i** (/ɪ/) | b**i**t (bit) |
| **o** (/ɒ/) | h**o**t (hot) |
| **u** (/ʌ/) | b**u**t (but) |'''
text = text.replace(table_2_1_4col, table_2_1_2col)

# 2.2 Diphthongs
table_2_2_4col = '''| Grapheme | Phoneme | English Equivalent | Example   |
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
| **er**   | /ɜːr/   | h**er**, b**ir**d  | her, berd |'''

table_2_2_2col = '''| MinEnglish | English Equivalent |
| :--------- | :----------------- |
| **ei** (/eɪ/) | d**ay**, m**a**ke (dei, meic) |
| **ii** (/iː/) | s**ee**, **ea**t (sii, iit) |
| **ai** (/aɪ/) | l**i**ke, m**y** (laic, mai) |
| **ou** (/oʊ/) | g**o**, n**o** (gou, nou) |
| **uu** (/uː/) | f**oo**d, t**oo** (fuud, tuu) |
| **au** (/aʊ/) | h**ow**, h**ou**se (hau, haus) |
| **oi** (/ɔɪ/) | b**oy** (boi) |
| **ar** (/ɑːr/) | c**ar** (car) |
| **or** (/ɔːr/) | f**or** (for) |
| **er** (/ɜːr/) | h**er**, b**ir**d (her, berd) |'''
text = text.replace(table_2_2_4col, table_2_2_2col)

# 2.3 Consonants
table_2_3_4col = '''| Grapheme | Phoneme    | Application Rule                                                                   | Example            |
| :------- | :--------- | :--------------------------------------------------------------------------------- | :----------------- |
| **c**    | /k/        | Soft, unaspirated velar plosive.                                                   | cat, cum, cup, bac |
| **k**    | /kʰ/       | Hard, aspirated velar plosive.                                                     | king, kiip, kic    |
| **ce** / **ci** | /tʃ/ | Voiceless palato-alveolar affricate. The _e_ or _i_ functions as an orthographic trigger. | ceic, ciald, cier |
| **u**    | /w/        | Semivowel substitution for _w_.                                                    | uoter, uid         |
| **i**    | /j/        | Semivowel substitution for _y_.                                                    | ies, iir           |
| **t**    | /t/ or /θ/ | Alveolar plosive; assumes the voiceless dental fricative locally.                  | tinc, trii         |
| **d**    | /d/ or /ð/ | Alveolar plosive; assumes the voiced dental fricative locally.                     | de, dat            |'''

table_2_3_2col = '''| MinEnglish | Rule / English Example |
| :--------- | :--------------------- |
| **c** (/k/) | Soft velar plosive (cat, cum) |
| **k** (/kʰ/) | Hard aspirated velar plosive (king, kic) |
| **ce / ci** (/tʃ/) | Palato-alveolar affricate (ceic, ciald) |
| **u** (/w/) | Semivowel _w_ (uoter, uid) |
| **i** (/j/) | Semivowel _y_ (ies, iir) |
| **t** (/t/ or /θ/) | Alveolar plosive / dental (tinc) |
| **d** (/d/ or /ð/) | Alveolar plosive / dental (de, dat) |'''
text = text.replace(table_2_3_4col, table_2_3_2col)

# 3.4 Pronouns
table_3_4_4col = '''| Singular | Referent               | Plural Array | Array Referent              |
| :------- | :--------------------- | :----------- | :-------------------------- |
| **i**    | First-person singular  | `5i`         | First-person group (n=5)    |
| **u**    | Second-person singular | `3u`         | Second-person group (n=3)   |
| **h**    | Third-person masculine | `4h`         | Masculine demographic (n=4) |
| **s**    | Third-person feminine  | `21s`        | Feminine demographic (n=21) |
| **t**    | Third-person inanimate | `*t`         | Inanimate collective        |'''

table_3_4_2col = '''| MinEnglish Singular | MinEnglish Plural |
| :------------------ | :---------------- |
| **i** (I) | `5i` (We five) |
| **u** (You) | `3u` (You three) |
| **h** (He) | `4h` (They four males) |
| **s** (She) | `21s` (They 21 females) |
| **t** (It) | `*t` (They things) |'''
text = text.replace(table_3_4_4col, table_3_4_2col)

# 3.9.3 Logic Operators
table_3_9_4col = '''| Operator | Name      | Primary Role                               | Example                     |
| :------- | :-------- | :----------------------------------------- | :-------------------------- |
| `+`      | Plus      | Future offset (optional; bare N = default) | `1d gou` = will go tomorrow |
| `-`      | Minus     | Past offset (required)                     | `-1d iit` = ate yesterday   |
| `*`      | Star      | Universal / generic quantifier             | `*cat` = all cats           |
| `&`      | Ampersand | Logical AND (≡ `an`)                       | `laic cat & dog`            |
| `|`      | Pipe      | Logical OR (≡ `or`)                        | `cat | dog`                  |
| `^`      | Caret     | Logical XOR (Exclusive OR)                 | `iit cat ^ dog` (one only)  |'''

table_3_9_2col = '''| Operator | Role & Example |
| :------- | :------------- |
| `+` | Future offset (`1d gou` = will go tomorrow) |
| `-` | Past offset (`-1d iit` = ate yesterday) |
| `*` | Universal quantifier (`*cat` = all cats) |
| `&` | Logical AND (`laic cat & dog`) |
| `|` | Logical OR (`cat | dog`) |
| `^` | Logical XOR (`iit cat ^ dog`) |'''
text = text.replace(table_3_9_4col, table_3_9_2col)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done')
