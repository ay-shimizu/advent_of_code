# from utils import *
from utils import utils

def parse_file(f):
    # stores calories per elf
    calories = []

    accumulator = 0
    for line in f:
        if line.strip():
            # if line is not empty
            num = int(line)
            accumulator += num
        else:
            # link is blank
            calories.append(accumulator)
            accumulator = 0

    return calories

def main():
    utils.print_header("1")
    input_file = "inputs/input1.txt"

    f = open(input_file, "r")

    utils.print_part("1")
    calories = parse_file(f)
    utils.print_answer(max(calories))

    utils.print_part("2")
    calories.sort(reverse=True)
    print(calories[0:3])
    utils.print_answer(sum(calories[0:3]))

main()
