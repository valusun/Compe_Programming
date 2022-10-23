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
        for u in Graph[v]:
            if visited[u]:
                continue
            dfs(u)

    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        dfs(i)
    print(ans)


if __name__ == "__main__":
    main()
