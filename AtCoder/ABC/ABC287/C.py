import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if visited[u]:
                continue
            dfs(u)

    dfs(0)
    # 連結していない or 辺の数が正しいか
    if False in visited or M != N - 1:
        print("No")
        exit()
    for g in graph:
        if not (1 <= len(g) <= 2):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
