import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
    for i in range(N):
        Graph[i] = sorted(Graph[i])
    visited = [False] * N
    ans = []

    def dfs(v):
        ans.append(v)
        for nv in Graph[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            dfs(nv)

    visited[0] = True
    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
