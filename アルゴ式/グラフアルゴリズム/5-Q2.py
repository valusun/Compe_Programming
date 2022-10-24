import sys

sys.setrecursionlimit(10**9)


def main():
    N, M, S, G = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)

    prev = [-1] * N

    def dfs(v, visited):
        visited[v] = True
        for u in Graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            prev[u] = v
            dfs(u, visited)

    visited = [False] * N
    visited[S] = True
    dfs(S, visited)

    ans = [G]
    while ans[-1] != S:
        ans.append(prev[ans[-1]])
    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
