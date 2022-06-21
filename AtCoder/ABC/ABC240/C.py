def main():
    N, X = map(int, input().split())
    jumps_points = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(X):
            if dp[i][j]:
                if j + jumps_points[i][0] <= X:
                    dp[i + 1][j + jumps_points[i][0]] = 1
                if j + jumps_points[i][1] <= X:
                    dp[i + 1][j + jumps_points[i][1]] = 1
    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
