import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Downcase Corpus examples and inline rules again.
def downcase_table(match):
    before = match.group(1)
    word = match.group(2)
    after = match.group(3)
    # Don't lowercase known proper nouns from the table if they exist
    if 'Isabella' in word or 'Spain' in word or 'France' in word:
        return match.group(0)
    
    if word.startswith('*'):
        if len(word) > 1:
            word = '*' + word[1].lower() + word[2:]
    else:
        word = word[0].lower() + word[1:]
    return before + word + after

text = re.sub(r'(\|\s*\*\*MinEnglish\*\*\s*\|\s*)([A-Z\*\~\-\>!]+)(.*)', downcase_table, text)

# For inline list examples
def downcase_inline(match):
    before = match.group(1)
    word = match.group(2)
    after = match.group(3)
    if 'Isabella' in word or 'Spain' in word or 'France' in word:
        return match.group(0)
    if word.startswith('*'):
        if len(word) > 1:
            word = '*' + word[1].lower() + word[2:]
    elif word.startswith('!!'):
        if len(word) > 2:
            word = '!!' + word[2].lower() + word[3:]
    elif word.startswith('Uac'):
        word = 'u' + word[1:]
    else:
        word = word[0].lower() + word[1:]
    return before + word + after

text = re.sub(r'(- `)([\w\*\~\-\>!]+)([^`]*` = )', downcase_inline, text)

# Lowercase explicit blocks
def downcase_me(match):
    return match.group(1) + match.group(2).lower() + match.group(3)
text = re.sub(r'(ME: )([A-Z\*\~\>!]+)(.*)', downcase_me, text)

text = text.replace('`Cat sit on mat`', '`cat sit on mat`')
text = text.replace('`Dog run in parc`', '`dog run in parc`')

# 2. Add documentation enforcing lowercase in 3.1.2 
caps_doc = """**Rule:** Proper Nouns (specific entities, geographical locations, nominal brands) retain their canonical native orthography. First-letter capitalization acts as an escape character, signaling to the parser that local phonetic rules are suspended for the duration of the token.

> **Strict Lowercase Axiom:** Because capitalization is an active mathematical operator (the Escape key), MinEnglish strictly prohibits capitalizing the first letter of sentences. Capitalizing a sentence-starting word would force parsers to guess whether the word is an escaped proper noun or standard orthographic decoration, destroying mathematical purity. All standard MinEnglish text is strictly lowercase."""

text = re.sub(r'\*\*Rule:\*\* Proper Nouns.*?the duration of the token\.', caps_doc, text, flags=re.DOTALL)


# 3. Add XOR (^) 
text = text.replace(
"""| `&`      | Ampersand | Logical AND (≡ `an`)                       | `laic cat & dog`            |
| `        | `         | Pipe                                       | Logical OR (≡ `or`)         |""",
"""| `&`      | Ampersand | Logical AND (≡ `an`)                       | `laic cat & dog`            |
| `|`      | Pipe      | Logical OR (≡ `or`)                        | `cat | dog`                  |
| `^`      | Caret     | Logical XOR (Exclusive OR)                 | `iit cat ^ dog` (one only)  |"""
)

text = text.replace('`or` / `|` (or)', '`or` / `|` (or), `^` (xor)')

# 4. !! and ?? markers as obnoxious / warning
# Replace the Exclamation (Space/End) definition
text = text.replace(
"""- **Exclamation (Space/End):** When placed at the end of a sentence or separated
  by a space, it acts natively as an exclamation.""",
"""- **Exclamation (Space/End):** When placed at the end of a sentence or separated
  by a space, it acts natively as an exclamation. Doubling the terminal marks (`!!` or `??`) is supported and explicitly defined as an aggressive, warning, or obnoxious tone multiplier.""")

text = text.replace('`uac!` = Watch out! (Exclamation)', '`uac!!` = Watch out! (Aggressive Warning)')
text = text.replace('`uen u1gou?` = **When** do you go?', '`uen u1gou??` = **When** do you go?! (Obnoxious Interrogation)')

# 5. Abjad Mode with english translations
text = text.replace(
"""- Standard: `tinc u bi >liit`
- Abjad Mode: `tnc u b >lt`""",
"""- Standard / English: `tinc u bi >liit` (I think you are very late)
- Abjad Mode: `tnc u b >lt`""")

# 6. Ex 7 "i no can" to "i !can"
text = text.replace('ME: :5Y studi inglish but i no can spiic fluuent. (45)', 'ME: :5Y studi inglish but i !can spiic fluuent. (44)')
# Update the corpus character counts and BT translation if necessary. The diff is 1 char
text = text.replace('BT: For-five-years study English but I not can speak fluent.', 'BT: For-five-years study English but I negation-can speak fluent.')

# Fix Exclamation / Uac spacing in corpus
text = text.replace('uac! uindou glas', 'uac!! uindou glas')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done')
