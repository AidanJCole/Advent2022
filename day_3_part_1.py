with open('day_3.txt','r') as f:
    txt = f.read()
    sacks = txt.split('\n')
    sum = 0
    for sack in sacks:
        char = set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])).pop()
        val = ord(char)
        diff = val - 96 if val > 96 else val-38
        sum += diff
    print(sum)

