def main():
    H, _, x, y = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(fields[x + i - 1][y + j - 1])
        print(*tmp, sep="")


if __name__ == "__main__":
    main()
