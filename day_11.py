from copy import deepcopy

with open('inputs/input_11.txt', 'r') as input_file:
    lines = [line.strip('\n') for line in input_file.readlines()]
    
class Monkey:
    
    def __init__(self):
        self.items, self.operation, self.test, self.throw_to, self.interact_count, self.parent_list = None,None,None,None,0, None
        
    def play_round(self, worry_divisor):
        operate = lambda old: eval(self.operation)
        while self.items:          
            self.interact_count += 1
            self.items[0] = operate(self.items[0]) // worry_divisor
            self.parent_list[self.throw_to[self.items[0] % self.test == 0]].items.append(self.items.pop(0))
     
    def join_list(self, list):
        self.parent_list = list        
        
def monkey_business(rounds, worry_divisor):   
    business_monkeys = deepcopy(monkeys)
    [monkey.join_list(business_monkeys) for monkey in business_monkeys]
    for i in range(rounds):
        if worry_divisor == 1:  # Division incompatible with shrinking
            shrink_numbers(business_monkeys)
        for monkey in business_monkeys:
            monkey.play_round(worry_divisor)
    return list_mult(sorted([monkey.interact_count for monkey in business_monkeys])[-2:])

def list_mult(target):
    product = 1
    for val in target: product *= val
    return product

def shrink_numbers(monkey_list):
    LCM = list_mult([monkey.test for monkey in monkey_list])
    for monkey in monkey_list:
        monkey.items = [item % LCM if item > LCM else item for item in monkey.items]
        
monkeys = []
for line in lines:
    if 'Monkey' in line:
        monkeys.append(Monkey())
    elif 'Starting' in line:
        items = line.split(':')[1].strip()
        monkeys[-1].items = [int(item) for item in items.split(',')]
    elif 'Operation' in line:
        monkeys[-1].operation = line.split('=')[1].strip()
    elif 'Test' in line:
        monkeys[-1].test = int(line.split()[-1])
    elif 'true' in line:
        monkeys[-1].throw_to = {True: int(line.split()[-1])}
    elif 'false' in line:
        monkeys[-1].throw_to[False] = int(line.split()[-1])

LCM = list_mult([monkey.test for monkey in monkeys])

print(f'part 1: {monkey_business(20, 3)}') # Answer 151312
print(f'part 2: {monkey_business(10000, 1)}') # Answer 51382025916
