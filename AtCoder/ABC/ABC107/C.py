def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = float("inf")

    for i in range(N - K + 1):
        left = A[i]
        right = A[i + K - 1]
        ans = min(
            ans, min(abs(left) + abs(left - right), abs(right) + abs(right - left))
        )
    print(ans)


if __name__ == "__main__":
    main()
