import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        Graph[a - 1].append((b - 1, i))
        Graph[b - 1].append((a - 1, i))
    Colors = [0] * (N - 1)

    def dfs(v, pre_v, pre_col):
        col = 1
        for nv, edge in Graph[v]:
            if nv == pre_v:
                continue
            if col == pre_col:
                col += 1
            Colors[edge] = col
            dfs(nv, v, col)
            col += 1

    dfs(0, -1, -1)
    print(max(Colors), *Colors, sep="\n")


if __name__ == "__main__":
    main()
