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
     return list(map(lambda x, y: x+y, [int(i) for i in s.split() if i.isdigit()], [0, -1, -1]))

with open("day_5.txt", 'r') as f:
    str = f.read()
    (stacks, procedure) = str.split('\n\n')
    print(stacks)

    stacks = parse_stacks(stacks)

    procedure = procedure.split('\n')
    for step in procedure:
        step = parse_instruction(step)
        stacks[step[2]] += stacks[step[1]][-step[0]:]
        stacks[step[1]] = stacks[step[1]][:-step[0]]
    str = ''.join([stack[-1] for stack in stacks])
    print(str)

