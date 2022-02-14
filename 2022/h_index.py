def h_index(citations):
    citations.sort()

    papers = len(citations)

    for index, cited in enumerate(citations):
        result = papers - index

        if result <= cited:
            return result

    return 0


def h_index_per_paper(papers: int, citations):
    return [h_index(citations[:paper]) for paper in range(1, papers + 1)]


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        papers = int(input())
        citations = list(map(int, input().split()))

        print(f"Case #{case}: {h_index_per_paper(papers, citations)}")


if __name__ == "__main__":
    main()
