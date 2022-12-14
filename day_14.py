import numpy as np
import matplotlib.pyplot as plt

with open('inputs/input_14.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
def fill_between(xy_1, xy_2, grid):
    yx_1, yx_2 = np.array(list(reversed(xy_1))), np.array(list(reversed(xy_2)))
    vector = np.clip(yx_2 - yx_1, -1, 1)
    while not np.array_equal(yx_1, yx_2):
        grid[yx_1[0], yx_1[1]] = 5
        yx_1 += vector
    grid[yx_1[0], yx_1[1]] = 5

    
def sand_fall(grid, sand):  # Return True if sand rests, False if it falls out
    vectors = [np.array([1, 0]), np.array([1, -1]), np.array([1, 1]), 'End']
    if grid[tuple(sand)] == 20:
        return False
    while sand[0] < grid.shape[0] - 1:
        for vec in vectors:
            if vec == 'End':
                grid[tuple(sand)] = 20
                return True
            if grid[tuple(sand + vec)] < 1:
                sand = sand + vec
                break
    return False
            
    
grid = np.full((500, 1000), 0)
for wall in [line.split('->') for line in lines]:
    nodes = [seg.strip().split(',') for seg in wall]
    nodes = [[int(val) for val in pair] for pair in nodes]
    for i in range(len(nodes)-1):
        fill_between(nodes[i], nodes[i + 1], grid)

origin = np.array([0, 500])
nonzero = grid.nonzero()
smaller_grid = np.copy(grid[0:max(nonzero[0] + 2), min(nonzero[1]) - 2:max(nonzero[1]) + 2])
smaller_origin = origin - np.array([0, min(nonzero[1]) - 2])
grid[origin[0], origin[1]] = 10

plt.figure()
plt.title('empty')
plt.imshow(grid)

while(sand_fall(smaller_grid, smaller_origin)): pass

print(f'part 1 : {np.count_nonzero(smaller_grid == 20)}')  # Answer 715

plt.figure()
plt.title('part 1')
plt.imshow(smaller_grid)

grid[smaller_grid.shape[0]] += 5
while(sand_fall(grid, origin)): pass

print(f'part 2 : {np.count_nonzero(grid == 20)}')  # Answer 25248

plt.figure()
plt.title('part 2')
plt.imshow(grid)

plt.show()
