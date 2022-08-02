from itertools import permutations


def main():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    INF = 10**18
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = c
        dist[b - 1][a - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = INF
    for p in permutations(r):
        res = 0
        for i in range(R - 1):
            res += dist[p[i] - 1][p[i + 1] - 1]
        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
