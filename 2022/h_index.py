def h_index(papers: int, citations_quantities: map):
    h = 0
    y = ""

    citations = [0] * (papers + 1)

    new_citations = 0

    for citation_times in citations_quantities:

        if citation_times > h:
            try:
                citations[citation_times] += 1
            except IndexError:
                citations[papers] += 1

            if new_citations == citations[h]:
                h += 1
                new_citations = 0
            else:
                new_citations += 1

        y += f" {h}"

    return y


def main():
    cases = int(input())

    for case in range(1, cases + 1):
        papers = int(input())
        citations = map(int, input().split())

        print(f"Case #{case}: {h_index(papers, citations)}")


if __name__ == "__main__":
    main()
