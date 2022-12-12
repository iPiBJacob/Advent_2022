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


def add_edges(graph, grid):
    for node in graph.nodes():
        [graph.add_edge(node, partner) for partner in check_partners(grid, node) if partner in graph.nodes()]


grid = None  # Build grid into a numpy array
for line in lines:
    grid = np.vstack([grid, [char for char in line]]) if grid is not None else np.array([char for char in line])

start = (np.where(grid == 'S')[0][0], np.where(grid == 'S')[1][0])
end = (np.where(grid == 'E')[0][0], np.where(grid == 'E')[1][0])
grid[start] = 'a'
grid[end] = 'z'

graph = nx.DiGraph()
graph.add_nodes_from([(y, x) for x in range(grid.shape[1]) for y in range(grid.shape[0])])

print(graph)
add_edges(graph, grid)
short_path = nx.shortest_path(graph, start, end)
print(short_path)
