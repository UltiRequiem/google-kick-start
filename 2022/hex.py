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

    if size > 1:
        if b_apparitions + dot_apparitions < r_apparitions:
            return "Impossible"
    
        if r_apparitions + dot_apparitions < b_apparitions:
            return "Impossible"
    
    blue_wins = []
    red_wins = []

    for row in data:
        blue_wins.append(all(char == "B" for char in row))
        red_wins.append(all(char == "R" for char in row))

    for column in range(len(data)):
        column_data = [row[column] for row in data]

        blue_wins.append(all(char == "B" for char in column_data))
        red_wins.append(all(char == "R" for char in column_data))

    if size > 2 and (sum(blue_wins) > 1 or sum(red_wins) > 1):
        return "Impossible"

    if sum(blue_wins):
        return "Blue wins"

    if sum(red_wins):
        return "Red wins"

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
