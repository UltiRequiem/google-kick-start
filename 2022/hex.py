def process(dashboard_data: list, size: int):
    if any(len(row) != size for row in dashboard_data):
        return "Impossible"

    flatten = [char for row in dashboard_data for char in row]

    b_apparitions, r_apparitions, dot_apparitions = (
        flatten.count("B"),
        flatten.count("R"),
        flatten.count("."),
    )

    if b_apparitions - 1 > r_apparitions or r_apparitions - 1 > b_apparitions:
        return "Impossible"

    if any(char not in "BR." for char in set(flatten)):
        return "Impossible"

    blue_wins = []
    red_wins = []

    for line in dashboard_data:
        blue_wins.append(all(char == "B" for char in line))
        red_wins.append(all(char == "R" for char in line))

    if sum(blue_wins) > 1 or sum(red_wins) > 1:
        return "Impossible"

    if sum(blue_wins) == 1:
        return "Blue wins"

    if sum(red_wins) == 1:
        return "Red wins"

    return "Nobody wins"


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        size = int(input())
        data = [input() for _ in range(size)]

        result = process(data, size)

        print(f"Case #{case}: {result}")


if __name__ == "__main__":
    main()
