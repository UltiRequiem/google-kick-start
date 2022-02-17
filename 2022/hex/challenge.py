VALID_INPUTS = ["B", "R", "."]


def process(data: list[list[str]], size: int):

    if any(len(data) != size for data in data):
        return "Impossible"

    flatten = [char for row in data for char in row]

    if any(char not in VALID_INPUTS for char in set(flatten)):
        return "Impossible"

    b_apparitions, r_apparitions, dot_apparitions = [
        flatten.count(char) for char in VALID_INPUTS
    ]

    if size > 1 and (
        (b_apparitions + dot_apparitions < r_apparitions)
        or (r_apparitions + dot_apparitions < b_apparitions)
    ):
        return "Impossible"

    blue_wins = []
    red_wins = []

    for index, value in enumerate(data):

        column_data = (row[index] for row in data)

        blue_wins.append(all(char == "B" for char in value))

        red_wins.append(all(char == "R" for char in column_data))

    b_wins_count, r_wins_count = sum(blue_wins), sum(red_wins)

    if size > 1 and (b_wins_count > 1 and r_wins_count > 1):
        return "Impossible"

    if b_wins_count or r_wins_count:
        return "Blue wins" if b_wins_count else "Red wins"

    return "Nobody wins"


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        size = int(input())
        data = [list(input()) for _ in range(size)]

        result = process(data, size)

        print(f"Case #{case}: {result}")


if __name__ == "__main__":
    main()
