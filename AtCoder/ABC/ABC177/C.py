def main():
    _ = int(input())
    A = list(map(int, input().split()))
    sum_ = sum(A)
    seen = 0
    ans = 0
    MOD = 10**9 + 7
    for a in A:
        seen += a
        ans += (sum_ - seen) * a
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
