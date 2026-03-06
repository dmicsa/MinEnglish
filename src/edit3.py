import re

filepath = 'd:/My/Work/Language/MinEnglish.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the examples still using 'no'
text = text.replace('if u1no stop', 'if u1!stop')
text = text.replace('you-now-not stop', 'you-now-negation-stop')  # Fix BT for Ex 11
text = text.replace('h no luv s', 'h !luv s')
text = text.replace('he not love she', 'he negation-love she') # Fix BT for Ex 17
text = text.replace('*no fiil dis ue', '*!fiil dis ue')
text = text.replace('any-not feel', 'any-negation-feel') # Fix BT for Ex 33
text = text.replace('no gilti', '!gilti')

# Update Section 3.5 "Negation" text itself
text = text.replace(
'''### 3.5 Negation

Negation is expressed by prepending `no` immediately before the verb. The `no`
token is invariant and does not conjugate.

- `no laic cat` = I do not like the cat.
- `u1d no cum` = You will not come tomorrow.
- `*h no can spiic` = None of them can speak.
''',
'''### 3.5 Negation

Negation is uniquely expressed by attaching the `!` prefix directly to the target word (typically the verb or adjective) without a space.

- `!laic cat` = I do not like the cat.
- `u1d !cum` = You will not come tomorrow.
- `*h !can spiic` = None of them can speak.
- `bi !gud` = It is not good.
'''
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done')
