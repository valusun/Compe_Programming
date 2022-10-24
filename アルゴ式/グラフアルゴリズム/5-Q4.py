import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    Color = ["."] * N

    def dfs(v, c):
        Color[v] = c
        nc = "W" if c == "B" else "B"
        for u in Graph[v]:
            if Color[u] == ".":
                dfs(u, nc)
            elif Color[u] == nc:
                continue
            else:
                print("No")
                exit()

    for v in range(N):
        if Color[v] == ".":
            dfs(v, "B")
    print("Yes")


if __name__ == "__main__":
    main()
