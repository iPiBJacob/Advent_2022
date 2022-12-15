with open('inputs/input_15.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
def manhattan_distance(tup_1, tup_2): return abs(tup_1[0] - tup_2[0]) + abs(tup_1[1] - tup_2[1])

def merge_slices(slice_1, slice_2):
    if slice_2[0] > slice_1[1] + 1: return [slice_1, slice_2]  # slices do not overlap or meet
    if slice_2[1] < slice_1[1]: return [slice_1]  # slice 2 fully contained
    return [(slice_1[0], slice_2[1])]  # slices overlap, take lowest bottom and highest top

def reduce_slices(slice_list):
    working = []
    big_slice = slice_list[0]
    for slice in slice_list:
        if len(merge_slices(big_slice, slice)) == 2:
            working.append(big_slice)
            big_slice = slice
        else:
            big_slice = merge_slices(big_slice, slice)[0]
    working.append(big_slice)
    return working
        

def x_slice(sensor, beacon, y):
    distance = manhattan_distance(sensor, beacon)
    if abs(sensor[0] - y) > distance: return None
    distance -= abs(sensor[0] - y)
    return (sensor[1] - distance, sensor[1] + distance)


def read_x_line(y, pings, x_floor=None, x_ceil=None):
    long_distance = max([manhattan_distance(sensor, pings[sensor]) for sensor in pings])
    if x_floor is None: min_x = min([min([coord[1] for coord in pings.keys()]), min([coord[1] for coord in pings.values()])]) - long_distance
    else: min_x = x_floor
    if x_ceil is None: max_x = max([max([coord[1] for coord in pings.keys()]), max([coord[1] for coord in pings.values()])]) + long_distance
    else: max_x = x_ceil

    slices = sorted([x_slice(sensor, pings[sensor], y)  for sensor in pings if x_slice(sensor, pings[sensor], y)])
    slices = [(max([slice[0], min_x]), min([slice[1], max_x])) for slice in slices]
    if len(slices) > 0: slices = reduce_slices(slices)
    blocked_sum = sum([slice[1] - slice[0] + 1 for slice in slices])
    for beacon in set(pings.values()):
        if beacon[0] == y and any([beacon[1] > slice[0] and beacon[1] < slice[1] for slice in slices]):
            blocked_sum -= 1

    return blocked_sum

def find_unblocked(x_range, y_range, pings):
    for y in range(y_range[0], y_range[1]+1):
        if y % 100 == 0 : print(f'progress: y={y}')
        slices = sorted([x_slice(sensor, pings[sensor], y)  for sensor in pings if x_slice(sensor, pings[sensor], y)])
        slices = [(max([slice[0], x_range[0]]), min([slice[1], x_range[1]])) for slice in slices]
        if len(slices) > 0: slices = reduce_slices(slices)
        if slices[0] != (x_range[0], x_range[1]):
            return (slices[1][0] - 1) * x_range[1] + y


pings = {}
for line in lines:
    sensor, beacon = line.split(':')
    sensor_x, sensor_y = [int(coord.split('=')[1]) for coord in sensor.split(',')]
    beacon_x, beacon_y = [int(coord.split('=')[1]) for coord in beacon.split(',')]
    pings[(sensor_y, sensor_x)] = (beacon_y, beacon_x)

print(f'part 1 : {read_x_line(2000000, pings)}')  # Answer is 6275922
print(f'part 2 : {find_unblocked((0, 4000000), (0, 4000000), pings)}')  # Answer 11747175442119
