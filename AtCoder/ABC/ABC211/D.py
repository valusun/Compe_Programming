from collections import deque


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a - 1].append(b - 1)
        Graph[b - 1].append(a - 1)
    Q = deque()
    Q.append(0)
    MOD = 10**9 + 7
    dist = [MOD] * N
    dist[0] = 0
    dist_cnt = [0] * N
    dist_cnt[0] = 1
    while Q:
        v = Q.popleft()
        for u in Graph[v]:
            if dist[u] == MOD:
                dist[u] = dist[v] + 1
                Q.append((u))
                dist_cnt[u] = dist_cnt[v]
            elif dist[u] == dist[v] + 1:
                dist_cnt[u] += dist_cnt[v]
                dist_cnt[u] %= MOD
    print(dist_cnt[N - 1])


if __name__ == "__main__":
    main()
