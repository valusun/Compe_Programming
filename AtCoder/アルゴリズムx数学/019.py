def main():
    _ = int(input())
    A = list(map(int, input().split()))
    cards = [0, 0, 0]
    for a in A:
        cards[a - 1] += 1
    ans = 0
    for c in cards:
        ans += c * (c - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
