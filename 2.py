# %% Part 1
with open("2.txt", 'r') as f:
    text = f.readlines()

o_d = {"A": 'r', "B": 'p', "C": 's'}
y_d = {"X": 'r', "Y": 'p', "Z": 's'}

beats = {"p": 'r', "s": 'p', "r": 's'}
score_dict = {"p": 2, "s": 3, "r": 1}

score = 0
for round in text:
    o, y = round.split()
    opponent, your = o_d[o],  y_d[y]

    score += score_dict[your]
    if your == opponent:  # tie
        score += 3
    if beats[your] == opponent:  # you win
        score += 6

score
# %% Part 2
score2 = 0
loses_to = {"r": 'p', "p": 's', "s": 'r'}
for round in text:
    o, y = round.split()
    opponent = o_d[o]

    if y == "X":  # lose
        score2 += score_dict[beats[opponent]]
    elif y == "Y":  # draw
        score2 += 3
        score2 += score_dict[opponent]
    elif y == "Z":  # win
        score2 += 6
        score2 += score_dict[loses_to[opponent]]

score2
