
catlist = []

while True:
    print('Enter cat\'s name: ')
    catname = [input()]
    catlist = catlist + catname
    print('Do you have anymore cats? (Y) (N)')
    morecats = input().lower()
    if morecats == 'n':
        break

print('you completed the list.')
print('here are your cat\'s names:')

n=1
for i in catlist:
    print(str(n) + '.' + ' ', end='')
    print(i)
    n += 1