with open('inputs/input_6.txt', 'r') as input:
    line = input.read()
    
def find_packet(line, marker_length):
    for i in range(marker_length, len(line)):
        if len(set([line[i-j] for j in range(marker_length)])) == marker_length:
            return(i+1)
        
print(f'part 1 : {find_packet(line, 4)}')
print(f'part 2 : {find_packet(line, 14)}')