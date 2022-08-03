def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    ans = [[0] * W for _ in range(H)]

    dh = [-1, -1, -1, 0, 0, 1, 1, 1]
    dw = [-1, 0, 1, -1, 1, -1, 0, 1]

    for h in range(H):
        for w in range(W):
            if Field[h][w] == "#":
                ans[h][w] = "#"
                continue
            res = 0
            for i in range(8):
                next_h = h + dh[i]
                next_w = w + dw[i]
                if 0 <= next_h < H and 0 <= next_w < W and Field[next_h][next_w] == "#":
                    res += 1
            ans[h][w] = res

    for a in ans:
        print(*a, sep="")


if __name__ == "__main__":
    main()
