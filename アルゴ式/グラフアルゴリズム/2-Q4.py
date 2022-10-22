import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Graph = [[] for _ in range(N)]
    for i, p in enumerate(P):
        Graph[p].append(i + 1)

    height = 0
    visited = set()

    def dfs(v: int, h: int):
        nonlocal height
        height = max(height, h)
        for u in Graph[v]:
            if u not in visited:
                visited.add(u)
                dfs(u, h + 1)

    dfs(0, 0)
    print(height)


if __name__ == "__main__":
    main()
