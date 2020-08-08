
# 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
enterd_position = {'8h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
                   '3h': 'wking', '3f': 'bqueen',}

def checking_validity_of_table(enterd_position):
    # Checks if the table entered is a valid chess layout. If not returns appropriate message.
    # If everything is good returns TRUE.

    # Initial values
    validator = True
    bking_c=wking_c=bqueen_c=wqueen_c=bbishop_c=wbishop_c=brook_c=wrook_c=bknight_c=wknight_c=bpawn_c=wpawn_c = 0

    # validating square names (keys in dict) are correct. Should be 1a through 8h (excepts vapital letters ok)
    for key, value in enterd_position.items():
        if int(key[0]) in [1,2,3,4,5,6,7,8]:
            pass
        else:
            print('at least one of the square entered is not proper !!!')
            validator = False
        if key[1].lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            pass
        else:
            print('at least one of the square entered is not proper !!!')
            validator = False

    # validating the right number of pieces
    # TODO work on doing that with dictionary should be more graceful.
    for val in enterd_position.values():
        if val == 'bking':
            bking_c += 2
        elif val == 'wking':
            wking_c += 2
        elif val == 'bqueen':
            bqueen_c += 2
        elif val == 'wqueen':
            wqueen_c += 2
        elif val == 'bbishop':
            bbishop_c += 1
        elif val == 'wbishop':
            wbishop_c += 1
        elif val == 'brook':
            brook_c += 1
        elif val == 'wrook':
            wrook_c += 1
        elif val == 'bknight':
            bknight_c += 1
        elif val == 'wknight':
            wknight_c += 1
        elif val == 'bpawn':
            bpawn_c += 1
        elif val == 'wpawn':
            wpawn_c += 1
        else:
            print('One of the pieces you entered is wrong ')
            validator = False


    all_pieces=[bknight_c,wknight_c,bpawn_c,wpawn_c,bking_c,wking_c,
                brook_c,wrook_c,bbishop_c,wbishop_c,bqueen_c,wqueen_c]
    names_pieces = ('bknight_c,wknight_c,bpawn_c,wpawn_c,bking_c,wking_c,\
                brook_c,wrook_c,bbishop_c,wbishop_c,bqueen_c,wqueen_c').split(',')

    # checking for number of pieces to not be more than 1 or 2
    for piece, names in zip(all_pieces, names_pieces):
        if piece > 2:
            print(f'too many {names[:-2]} on the table')
            validator = False


    # validating correct names of values in dict
    for values in enterd_position.values():
        if values[0] not in ['b', 'w'] or values[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            print('at least one of the pieces name is wrong')
            validator = False

    # TODO not wanted but checking if at least 2 pieces are on the same square.
    #  If so return False and give a warning
    #print(len(enterd_position.values()))
    # checking if two pieces on the same square
    #if len(enterd_position.keys()) != len(enterd_position.values()):
        #print('at least two pieces are on the same square')

    return validator

# print(checking_validity_of_table(enterd_position))
# result = checking_validity_of_table(enterd_position)
# print(result)