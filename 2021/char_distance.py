def process(text: str, letter: str):
    def get_distances(char: str, special_letter: str):
        def get_distance(c: str, c2: str):
            p_uni, f_uni = ord(c), ord(c2)
            start, end = min(p_uni, f_uni), max(p_uni, f_uni)

            return min(start + 26 - end, end - start)

        return [get_distance(char, second_char) for second_char in special_letter]

    count = 0

    for char in text:
        count += min(get_distances(char, letter))

    return count


def main():
    times = int(input())

    for time in range(times):
        text, letter = input(), input()

        print(f"Case #{time+1}: {process(text, letter)}")


if __name__ == "__main__":
    main()
