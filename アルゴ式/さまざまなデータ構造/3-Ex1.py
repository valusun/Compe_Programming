def main():
    H, W = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    row_cnts = [0] * H
    col_cnts = [0] * W
    for i in range(H):
        for j in range(W):
            if fields[i][j] == ".":
                continue
            row_cnts[i] += 1
            col_cnts[j] += 1

    Q = int(input())
    for _ in range(Q):
        p, q = map(int, input().split())
        duplicated_cnt = 1 if fields[p][q] == "#" else 0
        print(row_cnts[p] + col_cnts[q] - duplicated_cnt)


if __name__ == "__main__":
    main()
