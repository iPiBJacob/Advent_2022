import numpy as np
import matplotlib.pyplot as plt

with open('inputs/input_17.txt') as input_file:
    line = input_file.read().strip()
    
class Rock:
    
    shapes = [np.array([1,1,1,1]).reshape(1,4),
              np.array([[0,1,0], [1,1,1], [0,1,0]]),
              np.array([[1,1,1], [0,0,1], [0,0,1]]),
              np.array([1,1,1,1]).reshape(4,1),
              np.array([[1,1],[1,1]])]
    
    def __init__(self, shape, board):
        self.shape = Rock.shapes[shape]
        self.board = board
        self.x_pos = 2
        if board.nonzero()[0].size > 0: self.y_pos = board.nonzero()[0][-1]+4
        else: self.y_pos = 3
        
    def __repr__(self):
        return str(self.shape) + f'\nx_pos={self.x_pos}, y_pos={self.y_pos}'
        
    def jet(self, direction):
        if direction == '>':
            if self.x_pos + self.shape.shape[1] >= 7 or self.check_collision(direction): return
            else: self.x_pos += 1    
        if direction == '<':
            if self.x_pos <= 0 or self.check_collision(direction): return            
            else: self.x_pos -= 1   
            
    def drop(self):
        if self.y_pos == 0 or self.check_collision('down'):
            sub_board = self.board[self.y_pos:self.y_pos+self.shape.shape[0],
                                   self.x_pos:self.x_pos+self.shape.shape[1]]
            sub_board += self.shape
            return False
        self.y_pos -= 1
        return True
    
    def check_collision(self, direction):
        y_pos, x_pos = self.y_pos, self.x_pos
        if direction == '>': x_pos += 1
        if direction == '<': x_pos -= 1
        if direction == 'down': y_pos -= 1

        
        sub_board = self.board[y_pos:y_pos+self.shape.shape[0],
                               x_pos:x_pos+self.shape.shape[1]]

        if 2 in sub_board + self.shape: return True
        return False
    
def sliding_window(iterations, window_size=50, starting_i=0):
    
    board = np.full((window_size,7), 0) 
    jet_counter = 0
    slide_adjust = 0
    for i in range(starting_i, iterations):
        rock = Rock(i%5, board)
        rock.jet(line[jet_counter%len(line)])
        jet_counter += 1
        while rock.drop(): 
            rock.jet(line[jet_counter%len(line)])
            jet_counter += 1
        if board.nonzero()[0][-1] > 40:
            board = np.pad(board[10:], ((0,10), (0,0)))
            slide_adjust += 10
    return board.nonzero()[0][-1] + 1 + slide_adjust

def run_to_repeat(n_repeats = 1, window_size=50):
    board = np.full((window_size,7), 0) 
    jet_counter = 0
    slide_adjust = 0
    i = 0
    while True:
        if slide_adjust > 0 and jet_counter % (n_repeats * len(line)) == 0: return [board.nonzero()[0][-1] + 1 + slide_adjust,i]
        rock = Rock(i%5, board)
        rock.jet(line[jet_counter%len(line)])
        jet_counter += 1
        while rock.drop(): 
            rock.jet(line[jet_counter%len(line)])
            jet_counter += 1
            if slide_adjust > 0 and jet_counter % (n_repeats * len(line)) == 0: return [board.nonzero()[0][-1] + 1 + slide_adjust,i]
        if board.nonzero()[0][-1] > 40:
            board = np.pad(board[10:], ((0,10), (0,0)))
            slide_adjust += 10
        i += 1
    return board.nonzero()[0][-1] + 1 + slide_adjust


print(f'part 1 : {sliding_window(2022)}')

print(len(line))

repeat_3 = run_to_repeat(3)
repeat_6 = run_to_repeat(6)
blocks = 1000000000000
height_repeat, block_repeat = int(repeat_6[0]-repeat_3[0]), int(repeat_6[1]-repeat_3[1])
cycles = blocks // block_repeat
spillover = blocks % block_repeat
print([height_repeat, block_repeat])
print(cycles)
print(spillover)
loop_height = (cycles-1) * height_repeat
print(f'part 2 : {loop_height + int(sliding_window(spillover + block_repeat))}')
