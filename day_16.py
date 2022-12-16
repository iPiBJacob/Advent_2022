import time

with open('inputs/input_16_test.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
class Valve:
    
    def __init__(self, name='', flow_rate=None, tunnels=[], open=False):
        self.name, self.flow_rate, self.tunnels, self.open = name, flow_rate, tunnels, open
        self.released = 0

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

def bfs(valves, start, target):

def highest_first(valves, steps, start='AA'):
    valves_sorted = sorted(list(valves.values()), key=lambda x: x.flow_rate, reverse=True)
    for target_valve in valves_sorted:
        path, depth = None, 0
        while path is None:
            for source_valve in valves_sorted:
                path = source_valve.seek(valve, valves, depth, blacklist=[source_valve.name])
                if path: break
            depth += 1
                
        print(path)


valves = {}
for line in lines:
    valve, tunnels = line.split(';')
    name, flow_rate = valve.split(' ')[1], int(valve.split('=')[-1].strip())
    try: tunnels = tunnels.split('valves')[1]
    except: tunnels = tunnels.split('valve')[1]
    tunnels = [tunnel.strip() for tunnel in tunnels.split(',')]
    valves[name] = Valve(name, flow_rate, tunnels)

[valve.sort_tunnels(valves) for valve in valves.values()]

# print(f"path : {valves['AA'].seek('DD', valves, depth=1, blacklist=[])}")
# print(f'seeking CC')
# print(f"path : {valves['AA'].seek('GG', valves, depth=2, blacklist=[])}")
# highest_first(valves, 10)
