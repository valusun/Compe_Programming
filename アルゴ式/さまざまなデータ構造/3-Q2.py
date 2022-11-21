def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    diff_cnt = 0
    for i in range(H):
        for j in range(W):
            diff_cnt += S[i][j] != T[i][j]
    print(diff_cnt)


if __name__ == "__main__":
    main()
