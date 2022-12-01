#===============================================================================
# with open('input_1-1.txt', 'r') as input_file:
#     lines = input_file.readlines()
#
# lines = [line.strip() for line in lines]
#
# elves = []
# index = 0
# for line in lines:
#     if len(elves) == index:
#         elves.append(0)
#     if line == '':
#         index += 1
#         continue
#     else:
#         elves[index] += int(line)
#
# print(max(elves))
# elves = sorted(elves)
# print(sum(elves[-3:]))
#===============================================================================

with open('input_1-1.txt', 'r') as input_file:
    lines = input_file.readlines()

lines = [line.strip() for line in lines]

elves = [0]
for line in lines:
    if line == '':
        elves.append(0)
    else:
        elves[-1] += int(line)

print(max(elves))
elves = sorted(elves)
print(sum(elves[-3:]))
