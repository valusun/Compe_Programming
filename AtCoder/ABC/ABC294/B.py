def main():
    H, W = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        tmp = []
        for j in range(W):
            c = chr(f[i][j] + ord("A") - 1) if f[i][j] != 0 else "."
            tmp.append(c)
        print(*tmp, sep="")


if __name__ == "__main__":
    main()
