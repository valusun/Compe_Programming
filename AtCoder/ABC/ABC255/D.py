from bisect import bisect_right
from itertools import accumulate


def main():
    N, Q = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    Cusum = list(accumulate(A))
    for _ in range(Q):
        x = int(input())
        y = bisect_right(A, x)
        if not y:
            print(Cusum[-1] - (x * N))
        elif y == N:
            print(x * y - Cusum[-1])
        else:
            print((x * y - Cusum[y - 1]) + (Cusum[-1] - Cusum[y - 1] - (x * (N - y))))


if __name__ == "__main__":
    main()
