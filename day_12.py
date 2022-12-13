import networkx as nx
import numpy as np

with open('inputs/input_12.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

UDLR = [np.array([-1, 0]), np.array([1, 0]), np.array([0, -1]), np.array([0, 1])]

def check_partners(grid, yx_tup):
    accessible = []
    for dir in UDLR:
        try:
            partner = grid[(np.array(yx_tup) + dir)[0], (np.array(yx_tup) + dir)[1]]
            if ord(partner) <= ord(grid[yx_tup]) + 1:  # partner is no more than one step up
                accessible.append(tuple(np.array(yx_tup) + dir))
        except:  pass  # If trying to go off the grid
    return accessible

grid = None  # Build grid into a numpy array
for line in lines:
    grid = np.vstack([grid, [char for char in line]]) if grid is not None else np.array([char for char in line])

start = (np.where(grid == 'S')[0][0], np.where(grid == 'S')[1][0])
end = (np.where(grid == 'E')[0][0], np.where(grid == 'E')[1][0])
grid[start] = 'a'
grid[end] = 'z'

graph = nx.DiGraph()
graph.add_nodes_from([(y, x) for x in range(grid.shape[1]) for y in range(grid.shape[0])])
for node in graph.nodes():
    [graph.add_edge(node, partner) for partner in check_partners(grid, node) if partner in graph.nodes()]
    
all_paths = {}
for node in graph.nodes():
    if grid[node] == 'a':
        try:
            all_paths[node] = nx.shortest_path(graph, node, end)
        except: pass  # Some paths are not possible

print(f'part 1 : {len(nx.shortest_path(graph, start, end))-1}')
print(f'part 2 : {min([len(path)-1 for path in all_paths.values()])}')