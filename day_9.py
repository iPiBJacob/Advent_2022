import numpy as np

with open('inputs/input_9.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
directions = {'U': np.array([-1,0]), 'D': np.array([1,0]), 'L': np.array([0,-1]), 'R': np.array([0,1])}

def move(head_pos, tails, direction, number, visit_tracker):
    for i in range(number):
        head_pos += directions[direction]
        knot_ahead = head_pos
        for j, tail_pos in enumerate(tails):
            follow(knot_ahead, tail_pos)
            knot_ahead = tail_pos
        visit_tracker.add((tail_pos[0], tail_pos[1]))

        
def follow(leader, follower):
    if abs(leader - follower)[0] < 2 and abs(leader - follower)[1] < 2:
        return
    follower += np.clip((leader - follower), -1, 1)


head_pos_1, head_pos_2 = np.array([0, 0]), np.array([0, 0])
tails_1, tails_2 = [np.array([0, 0])], [np.array([0, 0]) for _ in range(9)]
visit_tracker_1, visit_tracker_2 = {(0, 0)}, {(0, 0)}

for line in lines:
    direction, number = line.split()
    move(head_pos_1, tails_1, direction, int(number), visit_tracker_1)
    move(head_pos_2, tails_2, direction, int(number), visit_tracker_2)
    
print(f'part 1 : {len(visit_tracker_1)}')  # Answer 6087
print(f'part 2 : {len(visit_tracker_2)}')  # Answer 2493
