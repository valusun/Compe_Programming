import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a - 1].append(b - 1)
        Graph[b - 1].append(a - 1)
    for i in range(N):
        Graph[i].sort()
    visited = [False] * N
    ans = []

    def dfs(v):
        ans.append(v + 1)
        visited[v] = True
        for u in Graph[v]:
            if visited[u]:
                continue
            dfs(u)
            ans.append(v + 1)

    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
