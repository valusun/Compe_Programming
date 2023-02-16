from collections import Counter


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    S = sum(A)
    start = A[0]
    ans = 0
    res = A[0]
    memo = Counter()
    for i in range(1, N):
        if A[i - 1] <= A[i] <= A[i - 1] + 1:
            res += A[i]
        else:
            memo[start] = res
            ans = max(ans, res)
            start = A[i]
            res = A[i]
    if A[-1] == M - 1:
        res += memo[0]
    ans = max(ans, res)
    print(S - ans)


if __name__ == "__main__":
    main()
