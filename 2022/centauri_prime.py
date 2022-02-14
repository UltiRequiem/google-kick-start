def ruler(kingdom: str):
    last_letter = kingdom[-1].lower()

    if "y" == last_letter:
        return "nobody"

    if last_letter in "aeiou":
        return "Alice"

    return "Bob"


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        kingdom = input()

        print(f"Case #{case}: {kingdom} is ruled by {ruler(kingdom)}.")


if __name__ == "__main__":
    main()
