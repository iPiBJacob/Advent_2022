with open('inputs/input_10.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
def addx(value, tracker):
    tracker.append(tracker[-1])
    tracker.append(tracker[-1] + value)
    
def noop(tracker):
    tracker.append(tracker[-1])
    
def draw(tracker):
    output = ''
    for i in range(6):
        for j in range(40):
            if abs(tracker[j+40*i] - j) < 2:
                output += '#'
            else: output += ' '
        output += '\n'
    return output
    
tracker = [1]
for line in lines:  # Build tracker
    if line.split()[0] == 'addx':
        addx(int(line.split()[1]), tracker)
    else:
        noop(tracker)

print(f'part 1 : {sum([tracker[i-1]*(i) for i in [20, 60, 100, 140, 180, 220]])}')  # Answer 12840
print(f'part 2 :\n{draw(tracker)}')  # Answer ZKJFBJFZ but in ASCII