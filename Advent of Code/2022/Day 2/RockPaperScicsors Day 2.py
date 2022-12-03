from enum import IntEnum


class RPS(IntEnum):
    Rock = A = X = 1
    Paper = B = Y = 2
    Scissors = C = Z = 3


rules = {RPS.Rock: RPS.Scissors, RPS.Scissors: RPS.Paper, RPS.Paper: RPS.Rock}
strategy = {'X': (lambda elf: rules[elf]),
            'Y': (lambda elf: elf),
            'Z': (lambda elf: {v: k for k, v in rules.items()}[elf])}


def rps_round(player: RPS, elf: RPS) -> int:
    points = player
    if rules[player] == elf:
        points += 6
    elif player == elf:
        points += 3

    return points


def day2():
    with open("input.txt", 'r') as f:
        rounds = [tuple(x.split(" ")) for x in f.read().splitlines()]

    points1, points2 = 0, 0
    for e, p in rounds:
        elf, player, selected_strategy = RPS[e], RPS[p], p
        points1 += rps_round(player, elf)
        points2 += rps_round(strategy[selected_strategy](elf), elf)

    print(points1)
    print(points2)


if __name__ == "__main__":
    day2()
