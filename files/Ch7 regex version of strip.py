#! Python3
# Regex version of strip.

import re

def regex_ver_strip(text, remove=''):
    """ strips optional remove (defaults space)from text using regex"""
    if remove:
        extras = re.compile(r'^(%s*)'%remove)
        mo = extras.sub('', text)
        mo = mo[::-1]
        mo = extras.sub('', mo)
        mo = mo[::-1]
        return mo
    else:
        spaces = re.compile(r'^(?: *)(.+)')
        mo = spaces.findall(text)
        mo = mo[0][::-1]
        mo = spaces.findall(mo)
        mo = mo[0][::-1]
        return mo


if __name__ == '__main__':
    text = '      $ Hello World  12       '
    print(regex_ver_strip(text))  # strip spaces
    text = 'tt$ Hello World  12tt'
    print(regex_ver_strip(text, remove='tt'))  # strip tt
