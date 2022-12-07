from collections import namedtuple

with open('inputs/input_7.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]


class Directory:
    
    def __init__(self, parent, name):
        self.parent = parent
        self.files = {}
        self.directories = {}
        self.name = name

    def size(self):
        file_sizes = [file.size for file in self.files.values()]
        directory_sizes = [directory.size() for directory in self.directories.values()]

        return sum(file_sizes) + sum(directory_sizes)


File = namedtuple('File', ['name', 'size'])

def dir(current_dir, name):
    current_dir.directories[name] = Directory(current_dir, name)

    
def cd(current_dir, target):
    if target == '/':
        if current_dir.name == '/':
            return current_dir
        while current_dir.parent:
            current_dir = current_dir.parent
    elif target == '..':
        current_dir = current_dir.parent
    else:
        current_dir = current_dir.directories[target]
    return current_dir

def sum_small_folders(top_dir, cutoff):
    sum = 0
    if top_dir.size() <= cutoff:
        sum = top_dir.size()
    for dir in top_dir.directories.values():
        sum += sum_small_folders(dir, cutoff)
    return sum

def find_smallest_deletable(top_dir, total_space, needed_space):
    min_size = needed_space - (total_space - root.size())
    if top_dir.size() < min_size:
        return None
    best_dir = top_dir
    for dir in top_dir.directories.values():
        print(f'best_dir: {best_dir.size()}, dir: {dir.size()}, needed: {min_size}')
        if dir.size() >= min_size:
            sub_dir = find_smallest_deletable(dir, total_space, needed_space)
            if sub_dir.size() < best_dir.size():
                best_dir = sub_dir
    return best_dir


root = Directory(None, '/')
current_dir = root

for line in lines:  # Build directory
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            current_dir = cd(current_dir, line[2])
        elif line[1] == 'ls':
            continue
    elif line[0] == 'dir':
        dir(current_dir, line[1])
    else:
        current_dir.files[line[1]] = File(name=line[1], size=int(line[0]))

print(f'part 1 : {sum_small_folders(root, 100000)}')
print(f'part 2 : {find_smallest_deletable(root, 70000000, 30000000).size()}')
