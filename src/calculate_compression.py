import sys
import re

with open('d:/My/Work/Language/MinEnglish.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('#### Ex.'):
        new_lines.append(line)
        i += 1
        ex_block = []
        # collect block
        while i < len(lines) and not lines[i].startswith('#### ') and not lines[i].startswith('### ') and not lines[i].startswith('## '):
            ex_block.append(lines[i])
            i += 1
            
        # Parse table to find English and MinEnglish Chars
        eng_len = 0
        min_len = 0
        eng_text = ''
        min_text = ''
        for l in ex_block:
            if l.startswith('| **English**'):
                parts = [p.strip() for p in l.split('|')]
                if len(parts) > 2:
                    eng_text = parts[2]
                    eng_len = len(eng_text)
            elif l.startswith('| **MinEnglish**'):
                parts = [p.strip() for p in l.split('|')]
                if len(parts) > 2:
                    min_text = parts[2]
                    min_len = len(min_text)
        
        if eng_len > 0 and min_len > 0:
            compression = round((1 - (min_len / eng_len)) * 100, 1)
            
            # Default analysis based on regex patterns or length
            observation = 'General lexical optimization and phonetic spelling reduction.'
            
            text_lower = min_text.lower()
            if '-1d' in text_lower or '1d' in text_lower or '-1y' in text_lower or '1y' in text_lower or ':' in text_lower:
                observation = 'Temporal operators (`-1d`, `1d`, `:5Y`) collapse complex tense architectures and prepositional phrases.'
            elif '~' in text_lower:
                observation = 'Approximation operators (`~`) drastically reduce multi-word phrasings like "about" or "approximately".'
            elif '>' in text_lower or '>>' in text_lower:
                observation = 'Intensity operators (`>`, `>>`) eliminate lengthy adverbial modifiers.'
            elif '?' in text_lower:
                observation = 'Interrogative prefixes condense investigative clauses into single tokens.'
            elif '!!' in text_lower:
                observation = 'Exclamatory prefixes (`!!`) enforce immediate semantic parsing, bypassing syntactic buildup.'
            elif '*' in text_lower:
                observation = 'Universal deference operators (`*`) substitute complex plural or aggregate noun constraints.'
            elif compression > 40:
                observation = 'High compression achieved via removal of definite articles, auxiliary verbs, and strict phonetic normalization.'
            elif compression < 15:
                observation = 'Low compression—Domain instances with heavily Latinate base nouns maintain phonetic parity with Standard English.'
            
            # recreate block
            new_block = []
            for l in ex_block:
                if l.startswith('| **English**') or l.startswith('| **MinEnglish**'):
                    # recalculate length to be safe
                    parts = l.split('|')
                    if len(parts) > 2:
                        text_part = parts[2].strip()
                        parts[3] = f' {len(text_part):<3} '
                        new_block.append('|'.join(parts))
                else:
                    new_block.append(l)
            
            ex_block = new_block
            
            # Inject the analysis below the table
            ex_block.append('\n')
            ex_block.append(f'> **Compression:** {compression}% Δ\n')
            ex_block.append(f'>\n')
            ex_block.append(f'> **Observation:** {observation}\n')
            ex_block.append('\n')
            
        new_lines.extend(ex_block)
    else:
        new_lines.append(line)
        i += 1

with open('d:/My/Work/Language/MinEnglish.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Updated with compressions.')
