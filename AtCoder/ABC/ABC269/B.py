def main():
    S = [list(input()) for _ in range(10)]
    sr, sc, er, ec = 10, 10, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == ".":
                continue
            sr = min(sr, i + 1)
            sc = min(sc, j + 1)
            er = max(er, i + 1)
            ec = max(ec, j + 1)
    print(sr, er)
    print(sc, ec)


if __name__ == "__main__":
    main()
