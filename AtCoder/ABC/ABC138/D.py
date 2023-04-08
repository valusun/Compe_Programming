import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    memo = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        memo[p - 1] += x
    visited = [False] * N

    def dfs(v: int):
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            memo[u] += memo[v]
            dfs(u)

    visited[0] = True
    dfs(0)
    print(*memo)


if __name__ == "__main__":
    main()
