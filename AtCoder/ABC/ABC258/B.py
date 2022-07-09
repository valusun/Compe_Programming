def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    ans = 0

    def UpdateAns(res):
        nonlocal ans
        for i in range(N):
            tmp = res[i:] + res[:i]
            ans = max(ans, int("".join(tmp)))
        for i in range(N):
            tmp = res[:i][::-1] + res[i:][::-1]
            ans = max(ans, int("".join(tmp)))

    # 縦移動
    for i in range(N):
        res = []
        for j in range(N):
            res.append(A[j][i])
        UpdateAns(res)

    # 横移動
    for i in range(N):
        res = []
        for j in range(N):
            res.append(A[i][j])
        UpdateAns(res)

    # 右斜め移動
    for i in range(N):
        res = []
        for j in range(N):
            res.append(A[j][(i + j) % N])
        UpdateAns(res)

    # 左斜めの移動
    for i in range(N):
        res = []
        for j in range(N):
            res.append(A[j][i - j])
        UpdateAns(res)

    print(ans)


if __name__ == "__main__":
    main()
