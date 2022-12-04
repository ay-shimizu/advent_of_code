from utils import utils

def parse_file(f):
    rounds = []

    accumulator = 0
    for line in f:
        round = line.split()
        rounds.append(round)

    return rounds


def play(opponent, you):
    win_points = 6;
    draw_points = 3;
    lose_points = 0;
    rock_points = 1;
    paper_points = 2;
    scissor_points = 3;

    if(opponent == "A"):
        # Rock
        if(you == "X"):
            # Rock
            return rock_points + draw_points
        elif(you == "Y"):
            # Paper
            return paper_points + win_points
        else:
            # Scissors
            return scissor_points + lose_points

    elif(opponent == "B"):
        # Paper
        if(you == "X"):
            # Rock
            return rock_points + lose_points
        elif(you == "Y"):
            # Paper
            return paper_points + draw_points
        else:
            # Scissors
            return scissor_points + win_points

    else:
        #Scissors
        if(you == "X"):
            # Rock
            return rock_points + win_points
        elif(you == "Y"):
            # Paper
            return paper_points + lose_points
        else:
            # Scissors
            return scissor_points + draw_points


def play2(opponent, you):
    win_points = 6;
    draw_points = 3;
    lose_points = 0;
    rock_points = 1;
    paper_points = 2;
    scissor_points = 3;

    if(opponent == "A"):
        # Rock
        if(you == "X"):
            # Need to Lose
            return scissor_points + lose_points
        elif(you == "Y"):
            # Need to draw
            return rock_points + draw_points
        else:
            # Need to win
            return paper_points + win_points

    elif(opponent == "B"):
        # Paper
        if(you == "X"):
            # Need to Lose
            return rock_points + lose_points
        elif(you == "Y"):
            # Need to draw
            return paper_points + draw_points
        else:
            # Need to win
            return scissor_points + win_points

    else:
        #Scissors
        if(you == "X"):
            # Need to Lose
            return paper_points + lose_points
        elif(you == "Y"):
            # Need to draw
            return scissor_points + draw_points
        else:
            # Need to win
            return rock_points + win_points

def play_tournament(rounds):
    total_score = 0

    for round in rounds:
        res = play(round[0], round[1])
        total_score += res

    return total_score

def play_tournament2(rounds):
    total_score = 0

    for round in rounds:
        res = play2(round[0], round[1])
        total_score += res

    return total_score

def main():
    utils.print_header("2")
    input_file = "inputs/input2.txt"

    f = open(input_file, "r")
    rounds = parse_file(f)

    utils.print_part("1")
    res = play_tournament(rounds)
    utils.print_answer(res)

    utils.print_part("2")
    res = play_tournament2(rounds)
    utils.print_answer(res)

main()
