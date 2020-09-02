
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#### text inserted for initial test purposes. Actual script copies from clipboad
# text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author\
# abbreviation\nLists of cultivars'

text = text.split('\n')
newlist = []
for line in text:
    line = '* ' + line
    newlist.append(line)
newtext = '\n'.join(newlist)
print(newtext)

pyperclip.copy(text)
