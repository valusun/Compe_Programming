def main():
    def get(arr):
        for a, i in arr:
            if a == 0:
                continue
            else:
                return i

    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    memo_r = [[0, i + 1] for i in range(H)]
    memo_c = [[0, j + 1] for j in range(W)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                memo_r[i][0] += 1
                memo_c[j][0] += 1
    memo_r.sort()
    memo_c.sort()
    print(get(memo_r), get(memo_c))


if __name__ == "__main__":
    main()
