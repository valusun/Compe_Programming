import sys

sys.setrecursionlimit(10**9)


def main():
    N, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N
    ans = [X]
    visited[X - 1] = True

    def dfs(v):
        if v == Y - 1:
            print(*ans)
            exit()
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            ans.append(u + 1)
            dfs(u)
            ans.pop(-1)
            visited[u] = False

    dfs(X - 1)


if __name__ == "__main__":
    main()
