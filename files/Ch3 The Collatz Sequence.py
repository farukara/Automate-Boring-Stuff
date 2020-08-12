

def collatz(number):
    global entry
    if (number % 2) == 0:
        print(int(number / 2))
        entry = int(number /2)
    elif (number % 2) == 1:
        print(number * 3 + 1)
        entry = int(number * 3 + 1)
try:
    print('enter a number, please')
    entry = int(input())
    while entry != 1:
        collatz(entry)



except ValueError:
    print('that\'s not an integer')



