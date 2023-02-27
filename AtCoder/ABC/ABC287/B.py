def main():
    N, M = map(int, input().split())
    S = [input()[-3:] for _ in range(N)]
    T = set(input() for _ in range(M))
    ans = 0
    for s in S:
        ans += s in T
    print(ans)


if __name__ == "__main__":
    main()
