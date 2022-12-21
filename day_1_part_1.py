with open("day_1.txt", 'r') as f:
    txt = f.read()
    print(max([sum(l) for l in [[int(n) for n in s.split('\n')] for s in txt.split('\n\n')]]))