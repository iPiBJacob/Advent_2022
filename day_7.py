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
        print(self.files)
        print(self.files.items())
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


root = Directory(None, '/')
current_dir = root

for line in lines:
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

print(root.size())

