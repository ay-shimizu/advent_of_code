from utils import utils

def parse_file(f):
    # assuming input is only one line
    for line in f:
        line = line.strip()
        return line

def has_repeat(list):
    to_set = set()
    for e in list:
        to_set.add(e)

    if len(list) == len(to_set):
        return False
    return True

def find_marker(input, req=4):
    tracker = []
    index = 0

    for e in input:
        index += 1
        if(len(tracker) < (req-1)):
            tracker.append(e)
        else:
            # e is 4th character or later
            if not e in tracker:
                if not has_repeat(tracker):
                    return index
            tracker.pop(0)
            tracker.append(e)

def main():
    utils.print_header("6")
    input_file = "inputs/input6.txt"
    # input_file = "inputs/input_example.txt"

    f = open(input_file, "r")
    input = parse_file(f)

    utils.print_part("1")
    marker = find_marker(input)
    utils.print_answer(marker)

    utils.print_part("2")
    marker = find_marker(input, 14)
    utils.print_answer(marker)

main()
