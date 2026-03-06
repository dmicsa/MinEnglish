import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Capitalize first letter of all sentences in the corpus tables and inline examples
# We need a robust way to uppercase MinEnglish sentences.
# Let's uppercase the start of text blocks in tables specifically:
def cap_table(match):
    before = match.group(1)
    word = match.group(2)
    after = match.group(3)
    if word.startswith('*'):
        # Capitalize the letter after the star
        if len(word) > 1:
            word = '*' + word[1].upper() + word[2:]
    elif word.startswith('~'):
        pass # Approximate number, ignore
    elif word.startswith('-'):
        # Keep -1d, etc
        pass
    else:
        word = word[0].upper() + word[1:]
    return before + word + after

# Look for: | **MinEnglish** | <word>
text = re.sub(r'(\|\s*\*\*MinEnglish\*\*\s*\|\s*)([a-zA-Z\*\~\-\>!]+)(.*)', cap_table, text)

# For inline list examples like: - `laic cat`
def cap_inline(match):
    before = match.group(1)
    word = match.group(2)
    after = match.group(3)
    
    # Exclude EBNF rule definitions
    if "::=" in after or "<" in word:
        return match.group(0)

    if word.startswith('*'):
        if len(word) > 1:
            word = '*' + word[1].upper() + word[2:]
    elif word.startswith('~') or word.startswith('-') or word.startswith('!'):
        pass
    else:
        word = word[0].upper() + word[1:]
    return before + word + after

text = re.sub(r'(- `)([\w\*\~\-\>!]+)([^`]*` = )', cap_inline, text)


# 2. Fix the "Look out!" idiom example string to have !! at the end
# Currently: - "Look out!" → `!!uac` (Watch intensely!)
text = text.replace('`!!uac`', '`Uac!!`')

# 3. Document the <, <<, >, >> amplifiers. They should probably go under 3.5 Adjectives & Adverbs.
amp_text = """### 3.5.1 Scalable Amplification (`>`, `>>`, `<`, `<<`)

Adjectives and adverbs lack morphological escalation (no "-er" or "-est"). Instead, magnitude is modulated using absolute mathematical prefixes:

| Operator | Function        | Example                 | Meaning                  |
| :------- | :-------------- | :---------------------- | :----------------------- |
| `>`      | Amplification   | `>big`, `>cuic`         | Very big, very fast      |
| `>>`     | Maximization    | `>>big`, `>>cuic`       | Massive, intensely fast  |
| `<`      | Attenuation     | `<big`, `<cuic`         | Slightly big, slowish    |
| `<<`     | Minimization    | `<<big`, `<<cuic`       | Tiny, barely moving      |

These operators attach directly to the front of their nominal target, creating an unbreakable semantic unit.
"""
# Insert after 3.5 Adjectives & Adverbs
text = re.sub(r'(### 3\.5 Adjectives & Adverbs.*?)(?=\n### 3\.6)', r'\1\n' + amp_text + r'\n', text, flags=re.DOTALL)


# 4. Remove entirely "3.12 Derivational Morphology Engine (Suffixes)"
# Find the headers for 3.12 and everything until 3.13
text = re.sub(r'### 3\.12 Derivational Morphology Engine \(Suffixes\).*?(?=### 3\.13)', '', text, flags=re.DOTALL)


# 5. Remove 'v0.2.0', 'v1.0.0', 'v0.9.0', 'v1.8' references embedded in the text.
text = re.sub(r' \(v[0-9]\.[0-9]\.[0-9]\)', '', text)
text = re.sub(r' \(v[0-9]\.[0-9]\)', '', text)
text = text.replace('v1.0.0 ', '')
text = text.replace('v0.9.0 ', '')
text = text.replace('the v1.8 and preceding protocols', 'previous linguistic protocols')

# Adjust the remaining headers down by one to fill the gap of 3.12
text = text.replace('### 3.13', '### 3.12')
text = text.replace('### 3.14', '### 3.13')
text = text.replace('### 3.15', '### 3.14')

# Capitalize the ebnf examples in 3.1
text = text.replace('`1cat sit on 1mat`', '`1cat sit on 1mat`') # Numbers don't cap
text = text.replace('`cat sit on mat`', '`Cat sit on mat`')
text = text.replace('`dog run in parc`', '`Dog run in parc`')
text = text.replace('`3cat run, den 1cat stop.`', '`3cat run, den 1cat stop.`')
text = text.replace('`laic cat`', '`Laic cat`')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done with script 1.")
