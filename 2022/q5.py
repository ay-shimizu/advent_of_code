from utils import utils
import copy

def find_stack(crates, line, stacks, ):
    CRATE_LENGTH = 3 + 1 # plus one for the space
    repeated_letter = {}

    for crate in crates:
        if(crate == ''):
            continue

        if(crate in repeated_letter):
            index = line.index(crate, repeated_letter[crate] + 1)
        else:
            index = line.index(crate)

        repeated_letter[crate] = index

        num = int(index/CRATE_LENGTH)

        if num + 1 in stacks:
            stacks[num + 1].insert(0, crate)
        else:
            stacks[num +1] = [crate]

def parse_file(f):
    stacks = {}
    # crate_num : stack_crate[] where the first entry is the bottom of the stack
    instructions = []
    at_instr = False

    for line in f:
        line = line.rstrip()

        if line == '':
            at_instr = True
            continue

        if line.strip()[0] == '1':
            continue

        if not at_instr:
            crates = line.split(' ')
            find_stack(crates, line, stacks)
        else:
            amount = line[line.index("move") + 4: line.index("from")].strip()
            from_crate = line[line.index("from") + 4: line.index("to")].strip()
            to_crate = line[line.index("to") + 2:].strip()

            instructions.append([int(amount), int(from_crate), int(to_crate)])

    return stacks, instructions

def pop_amount(list, num):
    removed = []
    for i in range(0, num):
        e = list.pop()
        removed.append(e)
    return removed

def rearrange(stacks, instructions):

    for instr in instructions:
        amount = instr[0]
        from_crate = instr[1]
        to_crate = instr[2]

        removed = pop_amount(stacks[from_crate], amount)
        stacks[to_crate] = stacks[to_crate] + removed

def remove_group(list, num):
    removed = list[len(list)- num: len(list)]
    del list[(num * -1):]

    return removed

def rearrange_9001(stacks, instructions):
    for instr in instructions:
        amount = instr[0]
        from_crate = instr[1]
        to_crate = instr[2]

        removed = remove_group(stacks[from_crate], amount)
        stacks[to_crate] = stacks[to_crate] + removed

def find_top(stacks):
    final = ""
    for i in range(0, len(stacks)):
        last = stacks[i + 1][-1]
        final += last[1]
    return final

def main():
    utils.print_header("5")
    input_file = "inputs/input5.txt"

    f = open(input_file, "r")
    stacks, instructions = parse_file(f)
    stacks2 = copy.deepcopy(stacks)

    utils.print_part("1")
    rearrange(stacks, instructions)
    ans = find_top(stacks)
    utils.print_answer(ans)

    utils.print_part("2")
    rearrange_9001(stacks2, instructions)
    ans = find_top(stacks2)
    utils.print_answer(ans)

main()
