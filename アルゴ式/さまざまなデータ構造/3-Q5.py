def main():
    def GetBomberCount():
        ret = 0
        for xd, yd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + xd < H and 0 <= y + yd < W:
                ret += 1 if fields[x + xd][y + yd] == "#" else 0
        return ret

    H, W = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    Q = int(input())
    for _ in range(Q):
        x, y = map(int, input().split())
        print(GetBomberCount())


if __name__ == "__main__":
    main()
