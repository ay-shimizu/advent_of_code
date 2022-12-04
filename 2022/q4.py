from utils import utils

def parse_file(f):
    pairs = []

    for line in f:
        line = line.strip()
        one, two = line.split(',')
        one_min, one_max = one.split('-')
        two_min, two_max = two.split('-')

        pairs.append(((int(one_min), int(one_max)), (int(two_min), int(two_max))))

    return pairs

def find_full_overlap(pairs):
    overlap_pairs = []

    for pair in pairs:
        one_min = pair[0][0]
        one_max = pair[0][1]
        two_min = pair[1][0]
        two_max = pair[1][1]

        min_diff = one_min - two_min
        max_diff = one_max - two_max

        if not ((min_diff < 0 and max_diff < 0) or (min_diff > 0 and max_diff > 0)):
            # if the two diffs are both pos and neg then they completely overlap
            overlap_pairs.append(pair)

    return overlap_pairs

def find_overlap(pairs):
    overlap_pairs = []

    for pair in pairs:
        one_min = pair[0][0]
        one_max = pair[0][1]
        two_min = pair[1][0]
        two_max = pair[1][1]

        greater_min = max(one_min, two_min)
        if(greater_min == two_min):
            # check if two_min is bw one_min and one_max
            if(two_min >= one_min and two_min <= one_max):
                overlap_pairs.append(pair)
        else:
            if(one_min >= two_min and one_min <= two_max):
                overlap_pairs.append(pair)

    return overlap_pairs


def main():
    utils.print_header("4")
    input_file = "inputs/input4.txt"

    f = open(input_file, "r")
    pairs = parse_file(f)

    utils.print_part("1")
    overlaps = find_full_overlap(pairs)

    utils.print_answer(len(overlaps))

    utils.print_part("2")
    overlaps = find_overlap(pairs)
    utils.print_answer(len(overlaps))

main()
