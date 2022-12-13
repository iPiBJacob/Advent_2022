import ast

with open('inputs/input_13.txt', 'r') as input_file:
    lines = [ast.literal_eval(line.strip()) for line in input_file.readlines() if line != '\n' ]


def parse_pairs(lines, pairs=[]):
    for i, line in enumerate(lines):
        if i % 2 == 0: pairs.append([line])
        elif i % 2 == 1: pairs[-1].append(line)
    return pairs


def check_right_order(list_a, list_b):
    if not type(list_a) == list: list_a = [list_a]  # Convert lone numbers to list
    if not type(list_b) == list: list_b = [list_b]
    for i in range(max(len(list_a), len(list_b))):
        try: val_a, val_b = list_a[i], list_b[i]
        except: return True if len(list_b) > len(list_a) else False
        if val_a == val_b: continue
        if type(val_a) == int and type(val_b) == int and val_b > val_a: return True
        elif type(val_a) == int and type(val_b) == int: return False
        else:
            if check_right_order(val_a, val_b) != None: return check_right_order(val_a, val_b)


def shitty_bubble_sort(sortable):  # Because I can't be bothered to even check if this is right
    while not all([check_right_order(sortable[i], sortable[i+1]) for i in range(len(sortable)-1)]):
        for i in range(len(sortable)-1):
            if not check_right_order(sortable[i], sortable[i+1]):
                sortable.insert(i, sortable.pop(i + 1))
    return sortable

sum_1 = 0
for i, pair in enumerate(parse_pairs(lines)):
    if check_right_order(*pair): sum_1 += i + 1

lines.append([[6]])
lines.append([[2]])
sorted_lines = shitty_bubble_sort(lines)

print(f'part 1 : {sum_1}')  # Answer 5659
print(f'part 2 : {(sorted_lines.index([[2]])+1) * (sorted_lines.index([[6]])+1)}')

