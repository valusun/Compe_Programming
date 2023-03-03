def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        _ = int(input())
        S.append(set(map(int, input().split())))
    ans = 0
    for i in range(2**M):
        choices = set()
        for j in range(M):
            if i & (1 << j):
                choices |= S[j]
        if len(choices) == N:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
