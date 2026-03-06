import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix broken compression blocks that look like this:
# 23.2% Δ
# 
# > **Observation:** ...
# 
# We want to change it to:
# > **Compression:** 23.2% Δ
# >
# > **Observation:** ...

text = re.sub(r'\n([0-9\.]+%\s*Δ)\n+\>\s*\*\*Observation:\*\*', r'\n> **Compression:** \1\n>\n> **Observation:**', text)

# Clean up Ex 35 duplicate block:
# ---
# 
# > **Compression:** 1.2% Δ **Observation:** Low compression due to retention of
# > exact international academic vocabulary.
# 
# ---
# 
# > **Compression:** 1.2% Δ
# >
# > **Observation:** Intensity operators (`>`, `>>`) eliminate lengthy adverbial
# > modifiers.

bad_ex35 = r"""---

> \*\*Compression:\*\* 1\.2% Δ \*\*Observation:\*\* Low compression due to retention of
> exact international academic vocabulary\.

---

> \*\*Compression:\*\* 1\.2% Δ
>
> \*\*Observation:\*\* Intensity operators \(`>`\, `>>`\) eliminate lengthy adverbial
> modifiers\."""

good_ex35 = r"""> **Compression:** 1.2% Δ
>
> **Observation:** Low compression due to retention of exact international academic vocabulary."""

text = re.sub(bad_ex35, good_ex35, text)

# Ensure Ex 2 doesn't have stray data.
# Replace: > **Compression:** *h's ouner. (42) (oops, that didn't happen)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done formatting compression block")
