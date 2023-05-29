import sys

sys.setrecursionlimit(10**9)


def main():
    N, M, Q = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(Q)]

    ans = 0

    def rec(seq, num):
        nonlocal ans
        if len(seq) == N:
            res = 0
            for i in range(Q):
                a, b, c, d = S[i]
                if seq[b - 1] - seq[a - 1] == c:
                    res += d
            ans = max(ans, res)
            return
        for n in range(num, M + 1):
            seq.append(n)
            rec(seq, n)
            seq.pop()

    rec([], 1)
    print(ans)


if __name__ == "__main__":
    main()
