import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i, p in enumerate(P):
        graph[p].append(i + 1)

    ans = []

    def dfs(v: int):
        ans.append(v)
        for u in graph[v]:
            dfs(u)

    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
