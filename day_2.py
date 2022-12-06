with open('inputs/input_2.txt', 'r') as input:
    guide = [line.strip().split() for line in input.readlines()]

inputs, outputs = ([match[0] for match in guide], [match[1] for match in guide])
winning_plays, ties, losing_plays = ({'A': 'Y', 'B': 'Z', 'C': 'X'}, {'A': 'X', 'B': 'Y', 'C': 'Z'}, {'A': 'Z', 'B': 'X', 'C': 'Y'})
win_loss_matrix = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}}


def score_attempt(inputs, outputs, strategy=None):
    if strategy:
        return sum(win_loss_matrix[input][strategy[output][input]] for input, output in zip(inputs, outputs))
    return sum([win_loss_matrix[input][output] for input, output in zip(inputs, outputs)])


print(f"part 1 : {score_attempt(inputs, outputs)}")
print(f"part 2 : {score_attempt(inputs, outputs, strategy={'X': losing_plays, 'Y': ties, 'Z': winning_plays})}")
