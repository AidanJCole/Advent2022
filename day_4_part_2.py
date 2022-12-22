with open('day_4.txt', 'r') as f:
    txt = f.read()
    ranges = [[list(map(lambda x: int(x), r.split('-'))) for r in p.split(',')] for p in txt.split('\n')]
    count = 0
    for pair in ranges:
        if not ((pair[0][1] < pair[1][0]) or (pair[0][0] > pair[1][1])):
            count += 1
    print(count)