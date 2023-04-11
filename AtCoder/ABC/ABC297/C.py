def main():
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(1, W):
            if field[i][j - 1] == field[i][j] == "T":
                field[i][j - 1] = "P"
                field[i][j] = "C"
    for f in field:
        print(*f, sep="")


if __name__ == "__main__":
    main()
