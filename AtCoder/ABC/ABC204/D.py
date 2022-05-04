def main():
    N = int(input())
    T = list(map(int, input().split()))
    sum_T = sum(T)
    selections_minutes = [[False] * (sum_T + 1) for _ in range(N + 1)]
    selections_minutes[0][0] = True
    for i in range(N):
        for j in range(sum_T):
            if selections_minutes[i][j]:
                selections_minutes[i + 1][j] = True
            if j - T[i] >= 0 and selections_minutes[i][j - T[i]]:
                selections_minutes[i + 1][j] = True
    ans = 10**9
    for i in range(sum_T + 1):
        if selections_minutes[N][i]:
            ans = min(ans, max(i, sum_T - i))
    print(ans)


if __name__ == "__main__":
    main()
