from utils import utils

def parse_file(f):
    instr = []

    for line in f:
        instr.append(line.strip())

    return instr

def process(instrs):
    x = 1
    cycle = 1
    signal_strengths = {}
    addx_latency = 2
    noop_latency = 1

    for instr in instrs:
        if instr == "noop":
            cycle += noop_latency
        else:
            instr, value = instr.split(' ')
            for mid_cycle in range(1, addx_latency):
                signal_strengths[cycle + mid_cycle] = (cycle + mid_cycle) * x
            x += int(value)
            cycle += addx_latency

        signal_strengths[cycle] = cycle * x

    return signal_strengths, cycle

def find_sum_interesting_signals(signal_strengths, max_cycles):
    first_cycle = 20
    every = 40
    sum = 0

    for i in range(first_cycle, max_cycles+1, every):
        sum += signal_strengths[i]

    return sum

def draw_pixel(grid, cycle, x):
    # x is the middle position of the sprite
    # CRT draws a pixel in each cycle
    # is curr position of CRT (in each cycle) is where the sprite loc is, draw # otherwise a .

    screen_width = 40
    screen_height = 6

    if(cycle > screen_width * screen_height):
        return

    row = int((cycle -1) / screen_width)
    col = (cycle -1) % screen_width

    sprite_row = int(x / screen_width)
    sprite_col = x % screen_width

    if(col in range(sprite_col-1, sprite_col+2)):
        grid[row][col] = '#'
    else:
        grid[row][col] = "."

    return grid

def print_grid(grid):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            print(grid[row][col], end='')
        print()

def draw(instrs):
    screen_width = 40
    screen_height = 6
    grid = [[0 for col in range(screen_width)] for row in range(screen_height)]

    # print_grid(grid)
    x = 1
    cycle = 1
    addx_latency = 2
    noop_latency = 1
    draw_pixel(grid, cycle, x)

    for instr in instrs:
        if instr == "noop":
            cycle += noop_latency
        else:
            instr, value = instr.split(' ')
            for mid_cycle in range(1, addx_latency):
                draw_pixel(grid, (cycle + mid_cycle), x)
            x += int(value)
            cycle += addx_latency

        draw_pixel(grid, cycle, x)

    return grid


def main():
    utils.print_header("10")
    input_file = "inputs/input10.txt"
    # input_file = "inputs/input_example.txt"

    f = open(input_file, "r")
    instrs = parse_file(f)

    utils.print_part("1")
    signal_strengths, total_cycles = process(instrs)
    sum = find_sum_interesting_signals(signal_strengths, 220)
    utils.print_answer(sum)
    #
    utils.print_part("2")
    grid = draw(instrs)
    print("Answer:")
    print("---------")
    print_grid(grid)
    print("---------")

main()
