def priority(char):
    if char.lower() == char:
        return ord(char)-96 # Lowercase letters start from 1 for puzzle but 97 in ord
    else:
        return ord(char)-38 # Capital letters start from 27 for puzzle but 65 in ord
    
def common_char(comp1, comp2):
    for char in comp1:
        if char in comp2:
            return char
        
def find_badge(elf1, elf2, elf3):
    for char in elf1:
        if char in elf2 and char in elf3:
            return char
        
def split_compartments(sack):
    comp1 = sack[0:len(sack)//2]
    comp2 = sack[len(sack)//2:]
    return(comp1, comp2)
    
with open('inputs/input_3.txt', 'r') as input:
    sacks = [line.strip() for line in input.readlines()]
    
sum = 0

for sack in sacks:
    comp1, comp2 = split_compartments(sack)
    common = common_char(comp1, comp2)
    sum += priority(common)

print(f'part 1 : {sum}')

groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]

sum = 0

for group in groups:
    sum += priority(find_badge(*group))
    
print(f'part 2 : {sum}')