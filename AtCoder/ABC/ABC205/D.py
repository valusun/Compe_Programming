from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    using_number_counts = [A[i] - (i + 1) for i in range(N)]
    for _ in range(Q):
        k = int(input())
        idx = bisect_left(using_number_counts, k)
        if idx == N:
            print((A[N - 1]) + (k - using_number_counts[N - 1]))
        else:
            print((A[idx] - 1) - (using_number_counts[idx] - k))


if __name__ == "__main__":
    main()
