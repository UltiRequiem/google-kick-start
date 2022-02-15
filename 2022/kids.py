def main():
    cases = int(input())

    for case in range(1, cases + 1):
        _, num_kids = map(int, input().split())

        candies_quantity = map(int, input().split())

        print(f"Case #{case}: {sum(candies_quantity) % num_kids}")


if __name__ == "__main__":
    main()
