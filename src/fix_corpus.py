
import re

with open('d:/My/Work/Language/MinEnglish.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the Git URL and bare email URL
text = text.replace('dmicsa@gmail.com', '<dmicsa@gmail.com>')
text = text.replace(' | **Repository:** [GitHub](https://github.com/dmicsa/MinEnglish)', '')

# Fix Corpus Examples
text = text.replace('!!uac! uindou glas', 'uac! uindou glas')
text = text.replace('!!uac!', 'uac!') # just in case
text = text.replace('Watch-intensely! One-window', 'Watch! One-window')

text = text.replace('?haum ciald u hav?', 'haum ciald u hav?')
text = text.replace('Question-how-much child', 'How-much child')

text = text.replace('?haum dis car cost?', 'haum dis car cost?')
text = text.replace('Question-how-much this car', 'How-much this car')

text = text.replace('!h no luv s.', 'h no luv s.')
text = text.replace('focus-he not love', 'he not love')

text = text.replace('?huu (who?),', 'huu (who?),')

# Re-save
with open('d:/My/Work/Language/MinEnglish.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Corpus and Git address updated.')
