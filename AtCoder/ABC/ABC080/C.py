def main():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    ans = -(10**10)
    for bit in range(1, 2**10):
        res = 0
        for i in range(N):
            c = 0
            for j in range(10):
                if bit & (1 << j) and F[i][j]:
                    c += 1
            res += P[i][c]
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
