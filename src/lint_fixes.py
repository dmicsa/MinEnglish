import re
import os

readme = 'd:/My/Work/Language/README.md'
with open(readme, 'r', encoding='utf-8') as f:
    text = f.read()
# Fix MD036 in README
text = text.replace('**"Uat u spic is uat u spel."**', '> *"Uat u spic is uat u spel."*')
with open(readme, 'w', encoding='utf-8') as f:
    f.write(text)

me = 'd:/My/Work/Language/MinEnglish.md'
with open(me, 'r', encoding='utf-8') as f:
    text = f.read()
# Fix MD036 in MinEnglish.md (line 399: **Subject...**)
text = text.replace('**Subject + Time-Verb + Number-Object + Modifiers**', '> **Subject + Time-Verb + Number-Object + Modifiers**')
# Fix MD001 in MinEnglish.md (line 854: #### Ex. 4 -> ### Ex. 4)
text = text.replace('#### Ex. 4', '### Ex. 4')
# Fix MD040 (Language tags on code fences)
text = re.sub(r'```\nNOUN:', r'```text\nNOUN:', text)
text = re.sub(r'```\nc = /k/', r'```text\nc = /k/', text)
text = re.sub(r'```\ni = I/me', r'```text\ni = I/me', text)
text = text.replace('```\nMIT License', '```text\nMIT License')

with open(me, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
