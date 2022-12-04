from utils import utils

def parse_file(f):
    rucksacks = []

    for line in f:
        line = line.strip()
        half_index = int(len(line)/2)
        one = line[:half_index]
        two = line[half_index:]

        rucksacks.append((one, two))

    return rucksacks

def convert_to_set(list):
    to_set = set()
    for e in list:
        to_set.add(e)

    return to_set

def find_match(one, two, three = None):
    one_set = convert_to_set(one)
    if three:
        three_set = convert_to_set(three)

    for e in two:
        if(e in one_set):
            # print("duplicate")
            if not three:
                return e
            else:
                if(e in three_set):
                    return e

    return None

def convert_to_num(letter):
    letter_as_num = ord(letter)

    # 97 is 'a' and 65 is 'A'
    if(letter_as_num < 97):
        # is a capital
        # convert to one_based: 'A' == 1 PLUS 26
        letter_as_num = (letter_as_num - 64) + 26
    else:
        # is lowercase
        letter_as_num = (letter_as_num - 96)

    return letter_as_num

def find_priority(sacks):
    matches = []
    for sack in sacks:
        match = find_match(sack[0], sack[1])
        if(match):
            matches.append(match)
        else:
            print("uh oh, error...")
            return

    sum_priorities = 0
    for match in matches:
        sum_priorities += convert_to_num(match)
    return sum_priorities

def find_group_priority(sacks):
    matches = []

    for i in range(0, len(sacks), 3):
        group_list = sacks[i:i+3]
        group = []
        for g in group_list:
            merge = g[0] + g[1]
            group.append(merge)

        match = find_match(group[0], group[1], group[2])
        matches.append(match)

    sum_priorities = 0
    for match in matches:
        sum_priorities += convert_to_num(match)
    return sum_priorities


def main():
    utils.print_header("3")
    input_file = "inputs/input3.txt"

    f = open(input_file, "r")
    sacks = parse_file(f)

    utils.print_part("1")
    ret = find_priority(sacks)
    utils.print_answer(ret)

    utils.print_part("2")
    ret = find_group_priority(sacks)
    utils.print_answer(ret)

main()
