import numpy as np

with open('inputs/input_8.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
   
lines = [[int(char) for char in line] for line in lines]
grid = np.array(lines)

def count_visible_left_edge(grid, output_matrix):
    for y in range(grid.shape[0]):
        left_max = 0
        for x in range(grid.shape[1]):
            if x == 0 or grid[y, x] > left_max:
                left_max = grid[y, x]
                output_matrix[y, x] = 1

                
def count_edge_visible(grid):
    visible = grid * 0
    left = count_visible_left_edge(grid, visible)
    right = count_visible_left_edge(np.flip(grid, 1), np.flip(visible, 1))
    top = count_visible_left_edge(np.flip(grid.T, 1), np.flip(visible.T, 1))
    bottom = count_visible_left_edge(grid.T, visible.T)
    return visible


def scenic_score_right(grid, source_x, source_y):
    for x in range(source_x+1, grid.shape[1]):  # Right Score
        if grid[source_y, x] >= grid[source_y, source_x] or x == grid.shape[1]-1:
            return x - source_x          
    return 1
    
 
def assess_scenic(grid):
    scenic_scores = grid*0
    
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            right = scenic_score_right(grid, x, y)
            left = scenic_score_right(np.flip(grid, 1), grid.shape[1]-x-1, y)
            top = scenic_score_right(np.flip(grid.T, 1), grid.shape[0]-y-1, x)
            bottom = scenic_score_right(grid.T, y, x)
            scenic_scores[y, x] = right * left * top * bottom
    return scenic_scores
 
visible = count_edge_visible(grid) 
scenic_scores = assess_scenic(grid)
max = np.unravel_index(scenic_scores.argmax(), scenic_scores.shape)
            
print(f'part 1 : {np.sum(visible)}')  # correct answer 1832
print(f'part 2 : {scenic_scores[max]}')  # correct answer 157320
