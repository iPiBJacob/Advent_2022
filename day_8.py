import numpy as np
import matplotlib.pyplot as plt

with open('inputs/input_8.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
   
lines = [[int(char) for char in line] for line in lines]
grid = np.array(lines)

def count_edge_visible(grid):
    visible = grid*0
    
    for y in range(grid.shape[0]):
        left_max = 0
        for x in range(grid.shape[1]):
            if x == 0 or grid[y,x] > left_max:
                left_max = grid[y,x]
                visible[y, x] = 1
                
        right_max = 0
        for x in range(grid.shape[1]-1, 0, -1):
            if x == grid.shape[1]-1 or grid[y,x] > right_max:
                right_max = grid[y,x]
                visible[y,x] = 1
                
    for x in range(grid.shape[1]):
        top_max = 0
        for y in range(grid.shape[0]):
            if y == 0 or grid[y,x] > top_max:
                top_max = grid[y,x]
                visible[y,x] = 1
                
        bottom_max = 0
        for y in range(grid.shape[0]-1, 0, -1):
            if y == grid.shape[0]-1 or grid[y,x] > bottom_max:
                bottom_max = grid[y,x]
                visible[y,x] = 1
                

    return visible

def scenic_score(grid, source_x, source_y):
    
    left_score, right_score, top_score, bottom_score = None,None,None,None    
    source_height = grid[source_y, source_x]
      
    for x in range(source_x-1, -1, -1):  # Left Score
        if grid[source_y, x] >= source_height or x == 0:
            left_score = source_x - x
            break
        
    for x in range(source_x+1, grid.shape[1]):  # Right Score
        if grid[source_y, x] >= source_height or x == grid.shape[1]-1:
            right_score = x - source_x
            break
        
    for y in range(source_y-1, -1, -1):  # Top Score
        if grid[y, source_x] >= source_height or y == 0:
            top_score = source_y - y
            break
        
    for y in range(source_y+1, grid.shape[0]):
        if grid[y, source_x] >= source_height or y == grid.shape[0]-1:
            bottom_score = y - source_y
            break

    if source_x == 0:
        left_score=1
    if source_x == grid.shape[1]-1:
        right_score=1
    if source_y == 0:
        top_score=1
    if source_y == grid.shape[0]-1:
        bottom_score=1

    return top_score * bottom_score * left_score * right_score

def assess_scenic(grid):
    
    scenic_scores = grid*0
    
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            scenic_scores[y,x] = scenic_score(grid, x, y)
            
    return scenic_scores
 
 
visible = count_edge_visible(grid) 
scenic_scores = assess_scenic(grid)
max = np.unravel_index(scenic_scores.argmax(), scenic_scores.shape)
            
print(f'part 1 : {np.sum(visible)}')  # correct answer 1832
print(f'part 2 : {scenic_score(grid, max[1], max[0])}')  # correct answer 157320
