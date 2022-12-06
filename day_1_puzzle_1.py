with open('inputs/input_1-1.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

elves = [0]
for line in lines:
    if line == '':
        elves.append(0)
    else:
        elves[-1] += int(line)

print(f'part 1 : {max(elves)}')
print(f'part 2 : {sum(sorted(elves)[-3:])}')
