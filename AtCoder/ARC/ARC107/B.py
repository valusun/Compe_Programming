def main():
    N, K = map(int, input().split())
    K = abs(K)
    num = [0] * (2 * N + 1)
    for i in range(2, 2 * N + 1):
        num[i] = min(i - 1, 2 * N + 1 - i)
    ans = 0
    for i in range(K, N * 2 + 1):
        ans += num[i] * num[i - K]
    print(ans)


if __name__ == "__main__":
    main()
