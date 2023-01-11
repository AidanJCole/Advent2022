def parse_stacks(s):
    rows = s.split('\n')
    parsed = []
    for row in rows:
        parsed.append(row[1::4])
    parsed = [i.ljust(len(parsed[-1]), ' ') for i in parsed]
    parsed = parsed[:-1]
    parsed = list(zip(*parsed[::-1]))
    return [[el for el in i if el != ' '] for i in parsed]

def parse_instruction(s):
    return [int(i) for i in s.split() if i.isdigit()]

with open("day_5.txt", 'r') as f:
    str = f.read()
    (stacks, procedure) = str.split('\n\n')
    print(stacks)

    stacks = parse_stacks(stacks)

    procedure = procedure.split('\n')
    for step in procedure:
        step = parse_instruction(step)
        for i in range(step[0]):
            stacks[step[2]-1].append(stacks[step[1]-1].pop())
    str = ''
    for s in stacks:
        str+=s[-1]
    print(str)

