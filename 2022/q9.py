from utils import utils

def parse_file(f):
    moves = []

    for line in f:
        movement, amount = line.strip().split(' ')
        moves.append((movement, int(amount)))

    return moves

def is_move_diagonal(head, tail):
    # if directly up, down, left, right by 2, then move step in direction;
    # otherwise if head and tail aren't touching and not in the same row or col -> diagonal
    if( (head[0] == tail[0]) and (abs(head[1] - tail[1]) <= 2)):
        # if x is same for head and tail (ie. same row) and at most two spaces away
        return False

    if( (head[1] == tail[1]) and (abs(head[0] - tail[0]) <= 2)):
        # if y is same for head and tail (ie. same col) and at most two spaces away
        return False

    if( abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1):
        # if both x and y is off by one - diagonally touching
        return False

    return True

def is_touching(head, tail):
    if(head[0] == tail[0] and (abs(head[1] - tail[1]) <= 1)):
        # if x is same for head and tail (ie. same row) and at most one spaces away
        return True
    if(head[1] == tail[1] and (abs(head[0] - tail[0]) <= 1)):
        # if y is same for head and tail (ie. same col) and at most two spaces away
        return True

    if( abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1):
        # if both x and y is off by one - diagonally touching
        return True

    return False

def move_diagonally(head_pos, tail_pos):
    if(head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]):
        # head is top right of tail
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif(head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]):
        # head is bottom left of tail
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    elif(head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]):
        # head is bottom right of tail
        tail_pos[0] += 1
        tail_pos[1] -= 1
    else:
         # head is top left of tail
         tail_pos[0] -= 1
         tail_pos[1] += 1

    return tail_pos

def simulate_helper(head_pos, tail_pos, dir, amount, pos_set):
    while(amount > 0):

        if(dir  == "R"):
            # +1 in x-axis
            head_pos[0] += 1
            move_diagonal = is_move_diagonal(head_pos, tail_pos)
            is_touch = is_touching(head_pos, tail_pos)

            if not move_diagonal and not is_touch:
                # tail should follow
                tail_pos[0] += 1
            elif not is_touch:
                tail_pos = move_diagonally(head_pos, tail_pos)

        elif(dir == "L"):
            # -1 in x-axis
            head_pos[0] -= 1
            move_diagonal = is_move_diagonal(head_pos, tail_pos)
            is_touch = is_touching(head_pos, tail_pos)

            if not move_diagonal and not is_touch:
                # tail should follow
                tail_pos[0] -= 1
            elif not is_touch:
                tail_pos = move_diagonally(head_pos, tail_pos)

        elif(dir == "U"):
            # +1 in y-axis
            head_pos[1] += 1
            move_diagonal = is_move_diagonal(head_pos, tail_pos)
            is_touch = is_touching(head_pos, tail_pos)

            if not move_diagonal and not is_touch:
                # tail should follow
                tail_pos[1] += 1
            elif not is_touch:
                tail_pos = move_diagonally(head_pos, tail_pos)
        else:
            # down: -1 in y-axis
            head_pos[1] -= 1
            move_diagonal = is_move_diagonal(head_pos, tail_pos)
            is_touch = is_touching(head_pos, tail_pos)

            if not move_diagonal and not is_touch:
                # tail should follow
                tail_pos[1] -= 1
            elif not is_touch:
                tail_pos = move_diagonally(head_pos, tail_pos)

        pos_set.add(tuple(tail_pos))
        return simulate_helper(head_pos, tail_pos, dir, amount - 1, pos_set)

    return head_pos, tail_pos, pos_set

def simulate(moves):
    head_pos = [0, 0]
    tail_pos = [0, 0]
    pos_set = set() # set for tail positions
    pos_set.add((0, 0))

    for move in moves:
        dir = move[0]
        amount = move[1]

        head_pos, tail_pos, pos_set = simulate_helper(head_pos, tail_pos, dir, amount, pos_set)

    return pos_set


def follow_knot(curr, prev):
    # if not diagonal / only up down left right
    if(prev[0] == curr[0] and prev[1] < curr[1]):
        # if same x but prev.y down of curr.y
        curr[1] -=1
    elif(prev[0] == curr[0] and prev[1] > curr[1]):
        curr[1] +=1

    elif(prev[1] == curr[1] and prev[0] > curr[0]):
        # if same y but prev.x right of curr.x
        curr[0] +=1
    else:
        curr[0] -=1

    return curr
def simulate_helper2(head_pos, tail_positions, dir, amount, pos_set):
    while(amount > 0):

        if(dir  == "R"):
            # +1 in x-axis
            head_pos[0] += 1
            for i in range(0, len(tail_positions)):

                tail_pos = tail_positions[i]
                if i > 0:
                    kbefore = tail_positions[i-1]
                else:
                    kbefore = head_pos

                move_diagonal = is_move_diagonal(kbefore, tail_pos)
                is_touch = is_touching(kbefore, tail_pos)

                if not move_diagonal and not is_touch:
                    # tail should follow in direction of previous knot

                    tail_pos = follow_knot(tail_pos, kbefore)
                elif not is_touch:
                    tail_pos = move_diagonally(kbefore, tail_pos)

                if(i == len(tail_positions) - 1):
                    pos_set.add(tuple(tail_pos))

        elif(dir == "L"):
            # -1 in x-axis
            head_pos[0] -= 1
            for i in range(0, len(tail_positions)):
                if i > 0:
                    kbefore = tail_positions[i-1]
                else:
                    kbefore = head_pos
                tail_pos = tail_positions[i]

                move_diagonal = is_move_diagonal(kbefore, tail_pos)
                is_touch = is_touching(kbefore, tail_pos)


                if not move_diagonal and not is_touch:
                    # tail should follow
                    tail_pos = follow_knot(tail_pos, kbefore)
                elif not is_touch:
                    tail_pos = move_diagonally(kbefore, tail_pos)

                if(i == len(tail_positions) -1):
                    pos_set.add(tuple(tail_pos))
        elif(dir == "U"):
            # +1 in y-axis
            head_pos[1] += 1
            for i in range(0, len(tail_positions)):
                if i > 0:
                    kbefore = tail_positions[i-1]
                else:
                    kbefore = head_pos
                tail_pos = tail_positions[i]

                move_diagonal = is_move_diagonal(kbefore, tail_pos)
                is_touch = is_touching(kbefore, tail_pos)


                if not move_diagonal and not is_touch:
                    # tail should follow
                    tail_pos = follow_knot(tail_pos, kbefore)
                elif not is_touch:
                    tail_pos = move_diagonally(kbefore, tail_pos)
                if(i == len(tail_positions) -1):
                    pos_set.add(tuple(tail_pos))
        else:
            # down: -1 in y-axis
            head_pos[1] -= 1
            for i in range(0, len(tail_positions)):
                if i > 0:
                    kbefore = tail_positions[i-1]
                else:
                    kbefore = head_pos
                tail_pos = tail_positions[i]
                move_diagonal = is_move_diagonal(kbefore, tail_pos)
                is_touch = is_touching(kbefore, tail_pos)


                if not move_diagonal and not is_touch:
                    # tail should follow
                    tail_pos = follow_knot(tail_pos, kbefore)
                elif not is_touch:
                    tail_pos = move_diagonally(kbefore, tail_pos)

                if(i == len(tail_positions) - 1):
                    pos_set.add(tuple(tail_pos))

        return simulate_helper2(head_pos, tail_positions, dir, amount - 1, pos_set)

    return head_pos, tail_positions, pos_set

def simulate2(moves, knots=9):
    tail_positions = []
    head_pos = [0,0]
    pos_set = set()

    for k in range(0, knots):
        tail_positions.append([0,0])

    pos_set.add((0, 0))

    for move in moves:
        dir = move[0]
        amount = move[1]

        head_pos, tail_positions, pos_set = simulate_helper2(head_pos, tail_positions, dir, amount, pos_set)

    return pos_set

def main():
    utils.print_header("9")
    input_file = "inputs/input9.txt"
    # input_file = "inputs/input_example.txt"

    f = open(input_file, "r")
    moves = parse_file(f)

    utils.print_part("1")
    tail_positions = simulate(moves)
    utils.print_answer(len(tail_positions))

    utils.print_part("2")
    tail_positions = simulate2(moves)
    utils.print_answer(len(tail_positions))

main()
