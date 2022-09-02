def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]

    def IsNeighborBlack(h, w):
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and Field[nh][nw] == "#":
                return True
        return False

    for i in range(H):
        for j in range(W):
            if Field[i][j] == "#":
                if not IsNeighborBlack(i, j):
                    print("No")
                    exit()
    print("Yes")


if __name__ == "__main__":
    main()
