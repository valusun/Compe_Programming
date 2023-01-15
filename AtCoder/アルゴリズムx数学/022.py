def main():
    _ = int(input())
    A = list(map(int, input().split()))
    tgt = 100000
    cards = [0] * tgt
    for a in A:
        cards[a] += 1
    ans = 0
    for i in range(1, tgt // 2):
        ans += cards[i] * cards[tgt - i]
    print(ans + cards[tgt // 2] * (cards[tgt // 2] - 1) // 2)


if __name__ == "__main__":
    main()
