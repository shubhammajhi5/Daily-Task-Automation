#! python3

import pyperclip as pc

text = pc.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pc.copy(text)
print('Bullet Points added to your text and copied to clipboard')