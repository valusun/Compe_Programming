import sys

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]

    def dfs(h, w):
        Field[h][w] = "."
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            is_area = 0 <= nh < H and 0 <= nw < W
            if is_area and Field[nh][nw] == "#":
                dfs(nh, nw)

    ans = 0
    for i in range(H):
        for j in range(W):
            if Field[i][j] == "#":
                dfs(i, j)
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
