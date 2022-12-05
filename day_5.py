with open('inputs/input_5_pure.txt', 'r') as input:
    all_lines = input.readlines()
    steps = [line.strip() for line in all_lines if 'from' in line]
    start = [line for line in all_lines if '[' in line]

def parse_start(start):  # Convert AoC's mess of formatting to lists with index zero at the bottom of the stack
    output = [[] for _ in range(9)]
    start_ = list(reversed(start))  # start_ used to preserve original start
    for line in start_:
        for i, index in enumerate(range(1, len(line), 4)):
            if line[index] != ' ':
                output[i].append(line[index])
    return output


def parse_steps(steps):  # Split each instruction line into its component number, start position, and end position
    ns, pos1s, pos2s = [], [] , []
    for step in steps:
        step_list = step.split(' ')
        ns.append(int(step_list[1]))
        pos1s.append(int(step_list[3]))
        pos2s.append(int(step_list[5]))

    return ns, pos1s, pos2s

def single_transfer(layout, pos1, pos2, n):
    layout[pos2 - 1] += reversed(layout[pos1 - 1][-n:])
    layout[pos1 - 1] = layout[pos1 - 1][:-n]

    
def multiple_transfer(layout, pos1, pos2, n):
    layout[pos2-1] += layout[pos1 - 1][-n:]
    layout[pos1 - 1] = layout[pos1 - 1][:-n]


layout1 = parse_start(start)
layout2 = [line.copy() for line in layout1]  # Need copy since operations are done in place

ns, pos1s, pos2s = parse_steps(steps)

for n, pos1, pos2 in zip(ns, pos1s, pos2s):
    single_transfer(layout1, pos1, pos2, n)
    multiple_transfer(layout2, pos1, pos2, n)

assert "".join([line[-1] for line in layout1]) == 'WHTLRMZRC', f'part 2: expected WHTLRMZRC but got {"".join([line[-1] for line in layout1])}'
print(f'part 1 : {"".join([line[-1] for line in layout1])}')
    
assert "".join([line[-1] for line in layout2]) == 'GMPMLWNMG', f'part 2: expected GMPMLWNMG but got {"".join([line[-1] for line in layout2])}'
print(f'part 2 : {"".join([line[-1] for line in layout2])}')
