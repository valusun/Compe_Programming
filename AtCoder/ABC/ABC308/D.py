import sys

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    if S[0][0] != "s":
        print("No")
        exit()

    words = list("snuke")
    dh = (0, 1, 0, -1)
    dw = (1, 0, -1, 0)
    visited = [[False] * W for _ in range(H)]
    visited[0][0] = True

    def dfs(h, w, memo):
        if h == H - 1 and w == W - 1:
            print("Yes")
            exit()
        tgt = memo % 5
        for i in range(4):
            nxt_h = h + dh[i]
            nxt_w = w + dw[i]
            if not (0 <= nxt_h < H and 0 <= nxt_w < W):
                continue
            if visited[nxt_h][nxt_w]:
                continue
            if S[nxt_h][nxt_w] != words[tgt]:
                continue
            visited[nxt_h][nxt_w] = True
            dfs(nxt_h, nxt_w, memo + 1)

    dfs(0, 0, 1)
    print("No")


if __name__ == "__main__":
    main()
