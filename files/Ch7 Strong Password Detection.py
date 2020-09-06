#! Python3
# Regex to detect strong password


import re
def strong_password(pw):
    """Checks if password(pw) is a strong one and returns True. Otherwise returns False """

    strong_aggr = []
    # minimum lengt of 8 characters
    if len(pw)<8:
        print("password should be at least 8 characters")
        strong_aggr.append(False)
    else:
        strong_aggr.append(True)

    #includes at least one uppercase letter
    UpperRegex = re.compile(r'[A-Z]+')
    mo = UpperRegex.search(pw)
    if not mo:
        print("password should include at least one uppercase letter")
        strong_aggr.append(False)
    else:
        strong_aggr.append(True)
        
    #includes at least one lowercase letter
    LowerRegex = re.compile(r'[a-z]+')
    mo = LowerRegex.search(pw)
    if not mo:
        print("password should include at least one lowercase letter")
        strong_aggr.append(False)
    else:
        strong_aggr.append(True)
        
    #includes at least one number
    NumberRegex = re.compile(r'\d+')
    mo = NumberRegex.search(pw)
    if not mo:
        print("password should include at least one number")
        strong_aggr.append(False)
    else:
        strong_aggr.append(True)

    #inform if the password is a strong one
    if all(strong_aggr):
        print('Congratulations, that\'s a strong password!!!!')
        print("")  # Empty line for testing more than one pw
        return True
    else:
        print("")
        return False


if __name__ == '__main__':
    pw_tests = ['Chicago81!', 'short2', 'longbutnonumbers', 'longwithUPPERCASE', 'ALLUPPERCASE12']
    for pw in pw_tests:
        print(pw, end=' -->  \n')
        strong_password(pw)
