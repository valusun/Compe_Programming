# REで落ちる謎を追う -> メモリ食い過ぎ
import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    depth = [-1] * N
    depth[0] = 0

    def dfs(v):
        for nv in Graph[v]:
            if depth[nv] != -1:
                continue
            depth[nv] = depth[v] + 1
            dfs(nv)

    dfs(0)
    print(max(depth))


if __name__ == "__main__":
    main()
