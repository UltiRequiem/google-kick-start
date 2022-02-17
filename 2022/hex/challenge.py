import numpy
from numpy.typing import NDArray

VALID_INPUTS = ["B", "R", "."]
R_DIRECTION = "VERTICAL"
B_DIRECTION = "HORIZONTAL"


def find_path(path: tuple, data: NDArray, tail=[]):
    pass


def process(data: NDArray, size: int):

    parse_data = numpy.array(data)

    flatten = [char for row in parse_data for char in row]

    b_apparitions, r_apparitions, _ = [flatten.count(char) for char in VALID_INPUTS]

    if (
        (any(len(data) != size for data in parse_data))
        or (any(char not in VALID_INPUTS for char in set(flatten)))
        or (
            size > 1
            and (
                (b_apparitions - 1 > r_apparitions)
                or (r_apparitions - 1 > b_apparitions)
            )
        )
    ):
        return "Impossible"

    blue_wins = []
    red_wins = []

    for index, value in enumerate(data):
        blue_wins.append(all(char == "B" for char in value))
        red_wins.append(all(char == "R" for char in data.T[index]))

    b_wins_count, r_wins_count = sum(blue_wins), sum(red_wins)

    if size > 1 and (b_wins_count > 1 or r_wins_count > 1):
        return "Impossible"

    if b_wins_count or r_wins_count:
        return "Blue wins" if b_wins_count else "Red wins"

    return "Nobody wins"


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        size = int(input())
        data = numpy.array([numpy.array(list(input())) for _ in range(size)])

        result = process(data, size)

        print(f"Case #{case}: {result}")


if __name__ == "__main__":
    main()
