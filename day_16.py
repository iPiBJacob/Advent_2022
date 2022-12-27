from itertools import permutations

with open('inputs/input_16.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
class Valve:
    
    max_depth = 20
    
    def __init__(self, name='', flow_rate=None, tunnels=[], open=False):
        self.name, self.flow_rate, self.tunnels, self.open = name, flow_rate, tunnels, open
        self.released = 0
        self.paths = {}

    def __repr__(self):
        return f'\nname: {self.name}, flow_rate: {self.flow_rate}, tunnels: {self.tunnels}, open: {self.open}, released: {self.released}\n'
    
    def sort_tunnels(self, valves): self.tunnels.sort(key=lambda x: valves[x].flow_rate, reverse=True)

    def seek(self, target, valves, depth=0, blacklist=[]):
        blacklist = blacklist.copy()
        blacklist.append(self.name)
        if target in self.tunnels: return [self.name, target]
        if depth == 0: return None
        for tunnel in self.tunnels:
            if tunnel not in blacklist:
                path = valves[tunnel].seek(target, valves, depth=depth - 1, blacklist=blacklist)
                if path:
                    path.insert(0, self.name)
                    return path
        return None
    
    def calculate_paths(self, valves):
        for valve in valves.values():       
            for i in range(Valve.max_depth):
                path = self.seek(valve.name, valves, depth=i)
                if path: 
                    self.paths[valve.name] = path
                    break
                if i == Valve.max_depth-1: raise Exception(f'No route from {self.name} to {valve.name} found within max depth')

def _score(route, valves, minutes, start='AA'):
    for valve in valves.values():
        valve.open = False  # reset all valves
        valve.released = 0
    route = list(route)   
    route.insert(0, start)
    path = []
    for i in range(len(route)-1):
        path += valves[route[i]].paths[route[i+1]]
       
        if len(path) >= minutes:
            break
    for i in range(minutes):        
        #=======================================================================
        # print(f'minute {i+1}')
        # if i < len(path): print(f'location: {path[i]}')
        # print(f'open valves: {[valve.name for valve in valves.values() if valve.open]}')
        # print(f'released this round: {sum([valve.flow_rate for valve in valves.values() if valve.open])}')
        # print('\n')
        #=======================================================================
        for valve in valves.values():
            if valve.open:
                valve.released += valve.flow_rate
        if (i < len(path)-1 and path[i+1] == path[i]) or i == len(path)-1 and not valves[path[i]].open:
            valves[path[i]].open = True
    #===========================================================================
    # while i < minutes - 1:
    #     for valve in valves.values():
    #         if valve.open:
    #             valve.released += valve.flow_rate
    #     i += 1
    #===========================================================================
    return sum([valve.released for valve in valves.values()])
  

def highest_score(valves, start):
    nonzero = [valve.name for valve in valves.values() if valve.flow_rate > 0]
    options = permutations(nonzero)
    max_score = 0
    for perm in options:
        local_score = _score(perm, valves, 30)
        if local_score > max_score: 
            max_score = local_score
            print(local_score)
    return max_score
    


valves = {}
for line in lines:
    valve, tunnels = line.split(';')
    name, flow_rate = valve.split(' ')[1], int(valve.split('=')[-1].strip())
    try: tunnels = tunnels.split('valves')[1]
    except: tunnels = tunnels.split('valve')[1]
    tunnels = [tunnel.strip() for tunnel in tunnels.split(',')]
    valves[name] = Valve(name, flow_rate, tunnels)

for valve in valves.values():valve.sort_tunnels(valves)
for valve in valves.values():valve.calculate_paths(valves)

print(highest_score(valves, 'AA'))
#print(score(('DD', 'BB', 'JJ', 'HH', 'EE', 'CC'), valves, 30))
#print(score(('HH', 'DD', 'JJ', 'BB', 'CC', 'EE'), valves, 30))
