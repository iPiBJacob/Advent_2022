with open('input_2.txt', 'r') as input:
    lines = input.readlines()
    
lines = [line.strip() for line in lines]

guide = [line.split() for line in lines]

inputs = [match[0] for match in guide]
outputs = [match[1] for match in guide]

winning_plays = {'A': 'Y', 'B': 'Z', 'C': 'X'}
ties = {'A': 'X', 'B': 'Y', 'C': 'Z'}
losing_plays = {'A': 'Z', 'B': 'X', 'C': 'Y'}
strategy = {'X': losing_plays, 'Y': ties, 'Z': winning_plays}
choice_scores = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for input, output in zip(inputs, outputs):
    score += choice_scores[output]
    
    if winning_plays[input] == output:
        score += 6
    elif ties[input] == output:
        score += 3
        
print(f'part 1 : {score}')


counts = {'X': 0, 'Y': 0, 'Z': 0}

score = 0
for input, output in zip(inputs, outputs):
    counts[output] += 1
    choice = strategy[output][input]
    
    score += choice_scores[choice]
    
    if winning_plays[input] == choice:
        score += 6
    elif ties[input] == choice:
        score += 3

print(f'part 2 : {score}')