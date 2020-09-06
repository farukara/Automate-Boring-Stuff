import re

phone_number_regex = re.compile(r'(\(?\d{3}\)?-)?(\d{3}-\d{4})')
text = 'My home number is 831-555-4242 and work number (831)-455-4545.'

mo = phone_number_regex.search(text)
print ('found a number: ', mo.group())
print(mo.group(1))
print(mo.group(2))
print('serch method: ', mo.group())

mo = phone_number_regex.findall(text)
print('findall method: ', mo)

for i in range(len(mo)):
    print('Number ', i+1, ' from findall: ', mo[i][0], mo[i][1])
