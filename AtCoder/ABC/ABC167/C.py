def main():
    N, M, X = map(int, input().split())
    book_info = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**18
    for bit in range(2**N):
        res = 0
        tmp = [0] * M
        for i in range(N):
            if bit & (1 << i):
                res += book_info[i][0]
                for bi, a in enumerate(book_info[i][1:]):
                    tmp[bi] += a
        if all([t >= X for t in tmp]):
            ans = min(ans, res)
    print(ans if ans != 10**18 else "-1")


if __name__ == "__main__":
    main()
