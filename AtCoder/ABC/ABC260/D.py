from bisect import bisect_right


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    eating_turns = [-1] * N
    top_cards = []
    table_cards = []
    if K == 1:
        for turn, p in enumerate(P, 1):
            eating_turns[p - 1] = turn
    else:
        for turn, p in enumerate(P, 1):
            x = bisect_right(top_cards, p)
            if len(top_cards) == x:
                top_cards.append(p)
                table_cards.append([p])
            else:
                top_cards[x] = p
                table_cards[x].append(p)
                if len(table_cards[x]) % K == 0:
                    for p in table_cards[x]:
                        eating_turns[p - 1] = turn
                    table_cards.pop(x)
                    top_cards.pop(x)
    print(*eating_turns, sep="\n")


if __name__ == "__main__":
    main()
