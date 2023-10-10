from bisect import bisect_left
from itertools import accumulate


def main():
    _, M, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cusum = [0] + list(accumulate(B))
    ans = 0
    for a in A:
        if a >= P:
            ans += P * M
            continue
        idx = bisect_left(B, P - a)
        if idx == 0:
            ans += P * M
        else:
            ans += P * (M - idx)
            ans += cusum[idx] + a * idx
    print(ans)


if __name__ == "__main__":
    main()
