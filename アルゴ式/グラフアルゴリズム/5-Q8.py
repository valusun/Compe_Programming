import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
    visited = [False] * N
    finished = [False] * N

    def dfs(v):
        visited[v] = True
        for u in Graph[v]:
            if visited[u]:
                if not finished[u]:
                    print("Yes")
                    exit()
                continue
            dfs(u)
        finished[v] = True

    for v in range(N):
        if visited[v]:
            continue
        dfs(v)
    print("No")


if __name__ == "__main__":
    main()
