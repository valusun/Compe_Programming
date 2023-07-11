MOVING = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]


def main():
    def is_check(h, w):
        for dh, dw in MOVING:
            tmp = []
            idx = []
            for i in range(5):
                nh, nw = h - dh * i, w - dw * i
                is_area = 0 <= nh < H and 0 <= nw < W
                if not is_area:
                    break
                tmp.append(S[nh][nw])
                idx.append((nh + 1, nw + 1))
            else:
                if tmp == ["s", "n", "u", "k", "e"]:
                    for i in idx:
                        print(*i)
                    exit()

    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "s":
                is_check(i, j)


if __name__ == "__main__":
    main()
