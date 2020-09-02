#!Python3
#Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.



def print_table(table):
    print('')  # for asthetics
    max_width = []
    indice = -1
    for i in table:
        indice += 1 
        max_width.append(0)
        for j in i:
            if len(j) > max_width[indice]:
                max_width[indice] = len(j)
    #print(max_width)

    for i in range(len(table[1])):
        for j in range(len(table)):
            print(table[j][i].rjust(max_width[j]), end=' ')
        print('')


if __name__ == '__main__':
    
    tableData = [['apples', 'oranges', 'cherries', 'banana'],                                                         ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)
