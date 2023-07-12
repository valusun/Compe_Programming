from math import sqrt
import sys

sys.setrecursionlimit(10**9)


def main():
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    seen = [False] * N

    def is_check(i, j):
        return sqrt((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2) <= D

    def dfs(v):
        seen[v] = True
        for u in range(N):
            if seen[u]:
                continue
            if is_check(v, u):
                dfs(u)

    dfs(0)
    for s in seen:
        print("Yes" if s else "No")


if __name__ == "__main__":
    main()
