def main():
    def update(i, j):
        rng = int(fields[i][j])
        for ii in range(R):
            for jj in range(C):
                if fields[ii][jj] != "#":
                    continue
                t = abs(ii - i) + abs(jj - j)
                if t <= rng:
                    fields[ii][jj] = "."

    R, C = map(int, input().split())
    fields = [list(input()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if fields[i][j] != "." and fields[i][j] != "#":
                update(i, j)
                fields[i][j] = "."
    for f in fields:
        print(*f, sep="")


if __name__ == "__main__":
    main()
