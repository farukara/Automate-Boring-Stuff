#! Python3
# Finds dates  in the DD/MM/YYYY format and checks if dates are entered correctly.

import re

text = " 31/04/2021, 31/04/2021, 31,04,2012, 34/05/2020, 31/24/2021, 31/11/3021, 31/02/2030, 29/02/2024, 29/02/2100, 29/02/2000, 23/13/2011"

finder = re.compile(r'[0-3][0-9]/[0-1][0-9]/[1-2][0-9]{3}')
mo = re.findall(finder, text)

print(mo)

for date in mo:
    if 0< int(date[0:2]) >31 or 0< int(date[3:5]) >12:
        print(date, 'date is not correct - this day does not exist')

    if int(date[3:5]) == 2 and int(date[6:10])%400 and  0< int(date[0:2]) >29:
        print(date, 'date is not correct - this day does not exist')
    elif int(date[6:10])%100 != 0 and int(date[6:10])%4 == 0 and 0< int(date[0:2]) >29:
        print(date, 'date is not correct - this day does not exist')
    elif int(date[6:10])%100 == 0 and int(date[6:10])%400 != 0 and 0< int(date[0:2]) >28:
        print(date, 'date is not correct - this day does not exist')
    elif int(date[3:5]) == 2 and int(date[6:10])%4 !=0 and 0< int(date[0:2]) >28:  
        print(date, 'date is not correct - this day does not exist')
