def main():
    N, M = map(int, input().split())
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    Edges = []
    for _ in range(M):
        v, u, c = map(int, input().split())
        dist[v - 1][u - 1] = c
        dist[u - 1][v - 1] = c
        Edges.append([v - 1, u - 1, c])
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for v, u, c in Edges:
        if c > dist[v][u]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
