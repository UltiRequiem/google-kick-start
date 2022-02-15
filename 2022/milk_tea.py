def generate_change_set(distance: list, choice: float):
    change_set = set()
    add_distance = 0

    i = 0

    while choice > 0:
        if choice % 2 == 1:
            change_set.add(distance[i][1])
            add_distance += distance[i][0]
        i += 1
        choice /= 2

    return change_set, add_distance


def generate_new_optimal(optimal: str, change_set: set):
    opt = ""

    for index, char in enumerate(optimal):
        if index not in change_set:
            opt += char
        else:
            if char == "1":
                opt += "0"
            else:
                opt += "1"

    return opt


def main():
    t = int(input())
    for t in range(t):
        n, m, p = map(int, input().split())
        friends = []
        for i in range(n):
            s = input()
            friends.append(list(map(int, s)))
        forbidden = set()
        for i in range(m):
            s = input()
            forbidden.add(s)

        optimal = ""
        distance = []
        optimal_distance = 0

        for i in range(p):
            ones = sum([friends[j][i] for j in range(n)])

            if ones > n - ones:
                optimal += "1"
                distance.append([ones - n + ones, i])
                optimal_distance += n - ones
            else:
                optimal += "0"
                distance.append([n - ones - ones, i])
                optimal_distance += ones

        distance = sorted(distance, key=lambda s: s[0])

        min_complicates = 99999999999999

        for choice in range(min(120, pow(2, len(distance)))):

            change_set, add_distance = generate_change_set(distance, choice)

            if (
                optimal_distance + add_distance >= min_complicates
                or generate_new_optimal(optimal, change_set) in forbidden
            ):
                continue

            min_complicates = optimal_distance + add_distance

        print(f"Case #{t+1}: {min_complicates}")


if __name__ == "__main__":
    main()
