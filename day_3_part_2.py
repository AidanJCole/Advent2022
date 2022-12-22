with open('day_3.txt','r') as f:
    txt = f.read()
    sacks = txt.split('\n')
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    sum = 0;
    for group in groups:
        val = ord(set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop())
        sum += val - 96 if val > 96 else val-38
    print(sum)