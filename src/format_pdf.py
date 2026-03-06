
import re

with open('d:/My/Work/Language/MinEnglish.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add \newpage before every major heading (e.g. ## 1. , ## 2. , ## Appendix)
text = re.sub(r'\n(## (\d+\.|Appendix))', r'\n\\newpage\n\1', text)

# 2. Add an extended Bibliography
extended_bib = """- Shannon, C. E. (1948). A mathematical theory of communication. _Bell System
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
- Sapir, E. (1921). _Language: An Introduction to the Study of Speech_. Harcourt, Brace."""

# Find the existing references and replace
pattern_refs = re.compile(r'- Shannon, C\. E.*?Addison-Wesley\.', re.DOTALL)
text = re.sub(pattern_refs, extended_bib, text)


# 3. Reformat the Corpus Tables to Codeblocks
# We want to match:
# |                | Text                                           | Chars |
# | -------------- | ---------------------------------------------- | ----- |
# | **English**    | <en> | <en_len>  |
# | **MinEnglish** | <me> | <me_len>  |
# | **↩ Back**     | <bk> |       |
#
# Replace with:
# ```text
# EN: <en> (<en_len>)
# ME: <me> (<me_len>)
# BT: <bk>
# ```

def replace_table(match):
    lines = match.group(0).split('\n')
    en_parts = lines[2].split('|')
    me_parts = lines[3].split('|')
    bk_parts = lines[4].split('|')
    
    en_text = en_parts[2].strip()
    en_len  = en_parts[3].strip()
    me_text = me_parts[2].strip()
    me_len  = me_parts[3].strip()
    bk_text = bk_parts[2].strip()
    
    return f"```text\nEN: {en_text} ({en_len})\nME: {me_text} ({me_len})\nBT: {bk_text}\n```"

table_regex = re.compile(r'\|\s*\|\s*Text.*?\|\s*Chars\s*\|\n\|\s*-+.*?\n\|\s*\*\*English\*\*.*?\|\n\|\s*\*\*MinEnglish\*\*.*?\|\n\|\s*\*\*↩ Back\*\*.*?(?=\n)', re.DOTALL)
text = re.sub(table_regex, replace_table, text)

# Remove stray duplicate compression blocks if any
dup_comp_regex = re.compile(r'(> \*\*Compression:\*\*.*?\n)\n+> \*\*Compression:\*\*', re.DOTALL)
def clean_comp(match):
    return match.group(1)
text = re.sub(dup_comp_regex, clean_comp, text)

with open('d:/My/Work/Language/MinEnglish.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done reformatting.")
