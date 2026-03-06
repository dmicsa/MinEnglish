import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace escaped asterisks in corpus code blocks
text = text.replace('\*ciald', '*ciald')
text = text.replace('\*iit', '*iit')
text = text.replace('\*ting', '*ting')
text = text.replace('\*trii', '*trii')
text = text.replace('\*carj', '*carj')
text = text.replace('\*ster', '*ster')
text = text.replace('\*i1d', '*i1d')
text = text.replace('\*i', '*i')
text = text.replace('\*h', '*h')
text = text.replace('\*person', '*person')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done removing escaped asterisks')
