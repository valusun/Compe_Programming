def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for k in range(K, N + 2):
        mn = (k * (k - 1)) // 2
        mx = (k * (2 * N - k + 1)) // 2
        ans += mx - mn + 1
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
