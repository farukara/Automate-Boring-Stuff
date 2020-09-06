#! Python3
# finds and returns email addresses from a given text

import re

def email_finder(text):
    """returns emails found inside a given text"""
    
    email_finder = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
    mo = re.findall(email_finder, text)
    
    return mo

if __name__ == '__main__':
    text = """Copied to clipboard:
    800-420-7240
    415-863-9900
    415-863-9950
    info@nostarch.com
    media@nostarch.com
    academic@nostarch.com
    info@nostarch.com"""

    email_list = email_finder(text)

    for i in email_list:
        print(i)
