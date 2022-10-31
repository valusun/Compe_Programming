import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    visited = [False] * N

    def dfs(v):
        visited[v] = True
        for nv in Graph[v]:
            if visited[nv]:
                continue
            dfs(nv)

    dfs(0)
    print("No" if visited.count(False) else "Yes")


if __name__ == "__main__":
    main()
