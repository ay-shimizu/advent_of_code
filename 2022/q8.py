from utils import utils

def parse_file(f):
    grid = []

    for line in f:
        line = line.strip()
        values = [*line]
        ints = [int(value) for value in values]
        grid.append(ints)

    return grid

def get_max_values(grid):
    row_maxes = []
    col_maxes = []

    for row in range(0, len(grid)):
        for col in range(1, len(grid[row]) - 1):
            row_vals = grid[row]
            left_max = max(row_vals[: col])
            right_max = max(row_vals[col+1:])
            row_maxes.append((left_max, right_max))

    for col in range(0, len(grid[0])):
        col_vals = []

        for row in range(0, len(grid)):
            col_vals.append(grid[row][col])

        for row in range(1, len(grid) - 1):
            up_max = max(col_vals[:row])
            down_max = max(col_vals[row + 1:])
            col_maxes.append((up_max, down_max))

    return row_maxes, col_maxes

def find_visible(grid, num_interior_col = 3, num_interior_row = 3):
    row_maxes, col_maxes = get_max_values(grid)
    interior_visible = 0
    edges = (len(grid) * 2) + ( (len(grid[0]) - 2) * 2)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            value = grid[row][col]

            this_row_maxes = row_maxes[row * num_interior_col + col - 1]
            this_col_maxes = col_maxes[col * num_interior_row + row - 1]

            if(value > this_row_maxes[0] or value > this_row_maxes[1]):
                interior_visible += 1
            elif(value > this_col_maxes[0] or value > this_col_maxes[1]):
                interior_visible += 1

    return interior_visible + edges

def find_distance(vals, curr_index):
    dist_left = 0
    dist_right = 0

    for i in range(0, len(vals)):
        if(i < curr_index):
            # left side
            if vals[i] >= vals[curr_index]:
                dist_left = curr_index - i
        elif i == curr_index:
            # at index
            continue
        elif(i > curr_index and dist_right == 0):
            # right side
            if vals[i] >= vals[curr_index]:
                dist_right = i - curr_index


    # cannot find anything higher - this tree is the highest
    if(dist_left == 0):
        dist_left = curr_index
    if(dist_right == 0):
        dist_right = len(vals) - curr_index - 1

    return dist_left, dist_right

def find_scenic(grid, num_interior_col = 3, num_interior_row = 3):

    row_distances = []
    col_distances = []
    scores = []

    for row in range(0, len(grid)):
        for col in range(1, len(grid[row]) - 1):
            row_vals = grid[row]

            dist_left, dist_right = find_distance(row_vals, col) #returns an index
            row_distances.append((dist_left, dist_right))

    for col in range(0, len(grid[0])):
        col_vals = []

        for row in range(0, len(grid)):
            col_vals.append(grid[row][col])

        for row in range(1, len(grid) - 1):
            dist_up, dist_down = find_distance(col_vals, row) #returns an index
            col_distances.append((dist_up, dist_down))

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):

            this_row_dist = row_distances[row * num_interior_col + col - 1]
            this_col_dist= col_distances[col * num_interior_row + row - 1]

            scenic = this_row_dist[0] * this_row_dist[1] * this_col_dist[0] * this_col_dist[1]
            scores.append(scenic)

    return max(scores)


def main():
    utils.print_header("8")
    input_file = "inputs/input8.txt"
    # input_file = "inputs/input_example.txt"

    f = open(input_file, "r")
    grid = parse_file(f)


    utils.print_part("1")
    num_visible = find_visible(grid, len(grid[0]) - 2, len(grid) -2)
    utils.print_answer(num_visible)
    #
    utils.print_part("2")
    scenic_value = find_scenic(grid,  len(grid[0]) - 2, len(grid) -2)
    utils.print_answer(scenic_value)


main()
