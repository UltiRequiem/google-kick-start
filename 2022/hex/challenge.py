import numpy
from numpy.typing import NDArray

VALID_INPUTS = ["B", "R", "."]


def create_win_array(letter: str, data, size: int):
    wins = []

    for index, value in enumerate(data):
        for idx, char in enumerate(value):
            if char == letter:
                for win in find_path(letter, (index, idx), data, size):
                    wins.append(win)

    return wins


def find_path(
    letter: str, path: tuple[int, int], data: NDArray, size: int, tail=[]
) -> list[bool]:
    if size == 1:
        return [data[path] == letter]

    possible_paths = []

    can_go_right, can_go_left = path[0] + 1 <= size, path[0] - 1 >= 0
    can_go_up, can_go_down = path[1] + 1 <= size, path[1] - 1 >= 0
    can_go_left_down, can_go_righ_up = (
        can_go_left and can_go_down,
        can_go_right and can_go_up,
    )

    if can_go_right:
        possible_paths.append((path[0] + 1, path[1]))

    if can_go_left:
        possible_paths.append((path[0] - 1, path[1]))

    if can_go_up:
        possible_paths.append((path[0], path[0] + 1))

    if can_go_down:
        possible_paths.append((path[0], path[0] - 1))

    if can_go_left_down:
        possible_paths.append((path[0] - 1, path[1] - 1))

    paths = []

    try:
        for path in possible_paths:
            print(f"len of {path} =>", len(data[path]))
            print(f"adding => {data[path]}")

            current = {"value": data[path], "path": path}

            tail.append(current)
            paths.append(current)


    except IndexError:
        exit("Chales")
        return [False]

    print("final paths =>", paths)

    return paths


def process(data: NDArray, size: int):

    flatten = [char for row in data for char in row]

    b_apparitions, r_apparitions, _ = [flatten.count(char) for char in VALID_INPUTS]

    if (
        (any(len(data) != size for data in data))
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

    blue_wins, red_wins = create_win_array("B", data, size), create_win_array(
        "R", data.T, size
    )

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
