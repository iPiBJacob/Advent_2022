with open('inputs/input_4.txt', 'r') as input:
    lines = [line.strip().split(',') for line in input.readlines()]
    
firsts = [line[0].split('-') for line in lines]
seconds = [line[1].split('-') for line in lines]

contained_count = 0

for first, second in zip(firsts, seconds):
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):  # second fully contained
        contained_count += 1
        continue
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):  # first fully contained
        contained_count += 1
        
print(f'part 1 : {contained_count}')

overlap_count = 0

for first, second in zip(firsts, seconds):
    first_range = list(range(int(first[0]), int(first[1])+1))
    second_range = list(range(int(second[0]), int(second[1])+1))
    
    if int(first[0]) in second_range or int(first[1]) in second_range:
        overlap_count += 1
        continue
    if int(second[0]) in first_range or int(second[1]) in first_range:
        overlap_count += 1
        
print(f'part 2 : {overlap_count}')