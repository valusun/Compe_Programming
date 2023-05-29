from itertools import combinations_with_replacement


def main():
    N, M, Q = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(Q)]

    ans = 0
    for p in combinations_with_replacement(range(1, M + 1), N):
        res = 0
        for i in range(Q):
            a, b, c, d = S[i]
            if p[b - 1] - p[a - 1] == c:
                res += d
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
