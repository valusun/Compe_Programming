from bisect import bisect_right
from itertools import accumulate


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Aa = [0] + list(accumulate(A))
    Bb = list(accumulate(B))
    ans = 0
    for i, a in enumerate(Aa):
        remaining = K - a
        if remaining < 0:
            break
        idx = bisect_right(Bb, remaining)
        ans = max(ans, i + idx)
    print(ans)


if __name__ == "__main__":
    main()
