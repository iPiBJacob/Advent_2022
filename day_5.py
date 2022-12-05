with open('inputs/input_5_steps.txt', 'r') as input:
    steps = [line.strip() for line in input.readlines()]
    
with open('inputs/input_5_start.txt', 'r') as input:
    start = input.readlines()
    
    
def parse_start(start):
    output = [[] for _ in range(9)]
    start_ = list(reversed(start[:-1]))  # start_ used to preserve original start
    for line in start_:
        for i, index in enumerate(range(1, 36, 4)):
            if line[index] != ' ':
                output[i].append(line[index])
    return output

def single_transfer(layout, pos1, pos2, n):
    pos1 -= 1  # Unit index to zero index
    pos2 -= 1  # Unit index to zero index
    
    list1 = layout[pos1]
    list2 = layout[pos2]
    
    for _ in range(n):
        list2.append(list1.pop())
        
def multiple_transfer(layout, pos1, pos2, n):
    pos1 -= 1  # Unit index to zero index
    pos2 -= 1  # Unit index to zero index
    
    list1 = layout[pos1]
    list2 = layout[pos2]
    
    helper = []
    
    for _ in range(n):
        helper.insert(0, list1.pop())
        
    list2 += helper
    
layout = parse_start(start)

for step in steps:
    step_list = step.split(' ')
    n = int(step_list[1])
    pos1 = int(step_list[3])
    pos2 = int(step_list[5])
    single_transfer(layout, pos1, pos2, n)
    
print(f'part 1 : {"".join([line[-1] for line in layout])}')

layout = parse_start(start)

for step in steps:
    step_list = step.split(' ')
    n = int(step_list[1])
    pos1 = int(step_list[3])
    pos2 = int(step_list[5])
    multiple_transfer(layout, pos1, pos2, n)
    
print(f'part 2 : {"".join([line[-1] for line in layout])}')