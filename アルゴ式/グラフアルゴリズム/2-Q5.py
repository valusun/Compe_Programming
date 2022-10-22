import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Graph = [[] for _ in range(N)]
    for i, p in enumerate(P):
        Graph[p].append(i + 1)

    descendants = [-1] * N

    def dfs(v: int):
        res = 0
        for u in Graph[v]:
            if descendants[u] == -1:
                res += dfs(u)
        descendants[v] = res
        return res + 1

    dfs(0)
    print(*descendants, sep="\n")


if __name__ == "__main__":
    main()
