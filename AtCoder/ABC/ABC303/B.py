def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    is_neighbor = [[False] * N for _ in range(N)]
    for i in range(N):
        is_neighbor[i][i] = True
    for i in range(M):
        for j in range(N - 1):
            x = A[i][j]
            y = A[i][j + 1]
            is_neighbor[x - 1][y - 1] = True
            is_neighbor[y - 1][x - 1] = True
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += 1 if not is_neighbor[i][j] else 0
    print(ans)


if __name__ == "__main__":
    main()
