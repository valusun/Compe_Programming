def main():
    N, K = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort()
    now = sum([b for _, b in ab])
    day = 1
    for a, b in ab:
        if now <= K:
            break
        now -= b
        day = a + 1
    print(day)


if __name__ == "__main__":
    main()
