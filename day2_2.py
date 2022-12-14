# https://adventofcode.com/2022/day/2


def convert(char):
    match char:
        case "A" | "X": return 0  # rock
        case "B" | "Y": return 1  # paper
        case "C" | "Z": return 2  # scissors


def main():
    f = open("input2.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    points = 0

    for round in lines:
        strategy = round.split(" ")[1]
        opponent, player = [convert(m) for m in round.split(" ")]

        if strategy == "X":
            # player must lose
            player = (opponent - 1) % 3
        elif strategy == "Z":
            # player must win
            player = (opponent + 1) % 3
        elif strategy == "Y":
            # player must draw
            player = opponent

        points += 6 if player - opponent == 1 or player - \
            opponent == -2 else 0  # win or lose
        points += 3 if player == opponent else 0  # draw
        points += player + 1  # points for match

    print("Day 2 - points: ", points)


if __name__ == "__main__":
    main()
