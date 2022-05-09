import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a - 1].append(b - 1)
        Graph[b - 1].append(a - 1)

    dist = [10**9] * N

    def dfs(v, d):
        dist[v] = d
        for u in Graph[v]:
            if d + 1 < dist[u]:
                dfs(u, d + 1)

    dfs(0, 0)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] - dist[d - 1]) % 2:
            print("Road")
        else:
            print("Town")


if __name__ == "__main__":
    main()
