def main():
    H, W, K = map(int, input().split())
    f = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            res = 0
            for ii in range(H):
                for jj in range(W):
                    if i & (1 << ii) and j & (1 << jj) and f[ii][jj] == "#":
                        res += 1
            if res == K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
