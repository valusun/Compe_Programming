def main():
    N, M = map(int, input().split())
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = c
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        for i in range(N):
            for j in range(N):
                if dist[i][j] < INF:
                    ans += dist[i][j]
    print(ans)


if __name__ == "__main__":
    main()
