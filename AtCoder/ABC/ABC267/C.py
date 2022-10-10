from itertools import accumulate


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_cusum = [0] + list(accumulate(A))
    B = [0] * (N - M + 1)
    B[0] = sum([a * i for i, a in enumerate(A[:M], 1)])
    for i in range(1, N - M + 1):
        B[i] = B[i - 1] + A[M + i - 1] * M - (A_cusum[M + i - 1] - A_cusum[i - 1])
    print(max(B))


if __name__ == "__main__":
    main()
