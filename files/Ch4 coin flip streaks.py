import random

def making_list():
    """making 100 flip coins into a list """
    coin_flips = []
    flips = ['H', 'T']

    for i in range(100):
        coin_flips += random.choice(flips)

    return coin_flips

def checking_streak(coin_flips):
    """checking number of streaks of 6 in the random list"""
    streaks = 0
    j = 0

    for i, flip in enumerate(coin_flips):
        if j <= len(coin_flips) - 6:
            j += 1
            #if opposite not in coin_flips[i : i+6]:
            if coin_flips[i : i+6].count('H') == 6 or coin_flips[i : i+6].count('T') == 6:
                streaks += 1

    return streaks

total_streaks = 0

# main loop for 10,000 tries.
for i in range(10_000):
    a = making_list()
    total_streaks += checking_streak(a)

print(total_streaks)