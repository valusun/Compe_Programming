import sys

sys.setrecursionlimit(10**9)


def Calc(n):
    return n * (n - 1) // 2


def main():
    N, M = map(int, input().split())
    Graph = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        Graph[u - 1].add(v - 1)
        Graph[v - 1].add(u - 1)
    Colors = [-1] * N
    c0, c1 = 0, 0

    def dfs(v: int, c: int) -> None:
        nonlocal c0, c1
        Colors[v] = c
        if c == 0:
            c0 += 1
        else:
            c1 += 1
        for u in Graph[v]:
            if Colors[u] == Colors[v]:
                print("0")
                exit()
            if Colors[u] != -1:
                continue
            dfs(u, (c + 1) % 2)

    ng_edge_cnt = 0
    for i in range(N):
        if Colors[i] != -1:
            continue
        c0, c1 = 0, 0
        dfs(i, 0)
        # 木ごとに独立して考える必要がある
        ng_edge_cnt += Calc(c0) + Calc(c1)
    print(Calc(N) - M - ng_edge_cnt)


if __name__ == "__main__":
    main()
