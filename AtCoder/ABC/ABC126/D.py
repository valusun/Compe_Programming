import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        Graph[u - 1].append((v - 1, w))
        Graph[v - 1].append((u - 1, w))
    vertices_color = [-1] * N

    def dfs(v: int):
        for u, w in Graph[v]:
            if vertices_color[u] != -1:
                continue
            coloring = vertices_color[v] if w % 2 == 0 else (vertices_color[v] + 1) % 2
            vertices_color[u] = coloring
            dfs(u)

    vertices_color[0] = 0
    dfs(0)
    print(*vertices_color, sep="\n")


if __name__ == "__main__":
    main()
