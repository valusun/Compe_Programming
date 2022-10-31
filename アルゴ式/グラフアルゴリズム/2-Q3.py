import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Graph = [[] for _ in range(N)]
    for i, p in enumerate(P):
        Graph[p].append(i + 1)

    depth = [-1] * N

    def dfs(v: int, d: int):
        depth[v] = d
        for nv in Graph[v]:
            if depth[nv] == -1:
                dfs(nv, d + 1)

    dfs(0, 0)
    print(*depth, sep="\n")


if __name__ == "__main__":
    main()
