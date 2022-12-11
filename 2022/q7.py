from utils import utils

class File:
    def __init__(self, name, size):
        self.name = name,
        self.size = size

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = {} # filename -> Directory obj
        self.prev_dir = None
        self.files = []
        self.total_size = 0

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def add_size(self, size):
        self.total_size += size

    def set_directories(self, directories):
        self.directories = directories
    def set_files(self, files):
        self.files = files
    def set_prev_dir(self, dir):
        self.prev_dir = dir

class Command:
    def __init__(self, command):
        self.command = command
        self.results = []

    def add_results(self, result):
        self.results.append(result)


def print_commands(commands):
    for command in commands:
        print(command.command)
        print(command.results)

def print_directory(directory):
    print(directory)

def parse_file(f):
    terminal_commands = []

    for line in f:
        line = line.strip()
        if line[0] == "$":
            # command
            new_command = Command(line[2:])
            terminal_commands.append(new_command)
        else:
            # output line
            # add result into previous command
            terminal_commands[-1].add_results(line)

    return terminal_commands

def get_items(results):
    directories = {}
    files = []
    for result in results:
        size_or_dir, filename = result.split(' ')
        if size_or_dir == "dir":
            # create new directory
            directories[filename] = (Directory(filename))
        else:
            # must be a file
            files.append(File(filename, int(size_or_dir)))

    return directories, files


def create_directory(commands):
    main_directory = None

    curr_dir = None
    for command in commands:
        keys = command.command.split(' ')
        name = keys[0]

        if(name == "cd" and keys[1] == '/'):
            # root
            main_directory = Directory('/')
            curr_dir = main_directory
        elif(name == "cd"):
            target = keys[1]
            if(target == ".."):
                curr_dir = curr_dir.prev_dir
            else:
                prev_dir_hold = curr_dir
                curr_dir = curr_dir.directories[target]
                if not curr_dir:
                    print("ERROR UH OH")

                if not curr_dir.prev_dir:
                    curr_dir.set_prev_dir(prev_dir_hold)
        elif(name == "ls"):
            results = command.results
            directories, files = get_items(results)
            curr_dir.set_directories(directories)
            curr_dir.set_files(files)
        else:
            print("COMMAND NOT FOUND")

    print(main_directory)
    return main_directory

def calculate_directory_size(directory):
    for file in directory.files:
        directory.add_size(file.size)

    sub_dir_total = 0
    for dir_key, dir_value in directory.directories.items():
        print(dir)
        sub_dir_total += calculate_directory_size(dir_value)

    directory.add_size(sub_dir_total)
    return directory.total_size

def print_dir(directory):
    print(directory.name, ": ", directory.total_size)

    for dir_key, dir_value in directory.directories.items():
        print_dir(dir_value)

def find_dir_with_size(directory, max, list):

    if(directory.total_size <= max):
        list.append(directory)

    for dir_key, dir_value in directory.directories.items():
        find_dir_with_size(dir_value, max, list)

    return list

def get_sum(dir_list):
    sum = 0
    for dir in dir_list:
        sum += dir.total_size
    return sum

def del_helper(directory, size, smallest):
    this_size = directory.total_size
    print(this_size)
    if(this_size >= size and this_size < smallest.total_size):
        smallest = directory

    for dir_key, dir_value in directory.directories.items():
        smallest = del_helper(dir_value, size, smallest)

    return smallest

def find_dir_to_delete(directory):
    unused_space = 70000000 - directory.total_size
    space_needed = 30000000 - unused_space
    print(space_needed)

    smallest = del_helper(directory, space_needed, directory)
    return smallest

def main():
    utils.print_header("7")
    input_file = "inputs/input7.txt"
    # input_file = "inputs/input_example.txt"

    f = open(input_file, "r")
    commands = parse_file(f)
    main_directory = create_directory(commands)
    calculate_directory_size(main_directory)
    print_dir(main_directory)

    utils.print_part("1")
    list = find_dir_with_size(main_directory, 100000, [])
    utils.print_answer(get_sum(list))
    #
    utils.print_part("2")
    smallest = find_dir_to_delete(main_directory)
    print()
    # marker = find_marker(input, 14)
    utils.print_answer(smallest.total_size)

main()
