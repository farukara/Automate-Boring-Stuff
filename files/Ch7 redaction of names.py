import re

text = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'

name_reg = re.compile(r'Agent ([A-Z])\w*')
reded_text = name_reg.sub(r'Agent \1****', text)

print(reded_text)

