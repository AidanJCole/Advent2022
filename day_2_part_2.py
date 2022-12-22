score = {'X': 0, 'Y': 3, 'Z': 6}
score_play = {
    'X': {'A': 3, 'B': 1, 'C': 2},
    'Y': {'A': 1, 'B': 2, 'C': 3},
    'Z': {'A': 2, 'B': 3, 'C': 1}}

with open("day_2.txt", 'r') as f:
    txt = f.read().strip()
    pairs = [s.split(' ') for s in txt.split('\n')]
    sum = 0
    for pair in pairs:
        sum += score[pair[1]]
        sum += score_play[pair[1]][pair[0]]
    print(sum)