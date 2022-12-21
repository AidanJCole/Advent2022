with open("day_1.txt", 'r') as f:
    txt = f.read()
    sums = [sum(l) for l in [[int(n) for n in s.split('\n')] for s in txt.split('\n\n')]]
    sums.sort()
    print(sum(sums[-3:]))