def Choose(n, k, mod):
    a, b = 1, 1
    k = min(k, n - k)
    for i in range(k):
        a = a * (n - i) % mod
        b = b * (i + 1) % mod
    return a * Pow(b, mod - 2, mod) % mod


def Pow(x, n, mod):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * x % mod
        x = x * x % mod
        n >>= 1
    return ret


def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    print((Pow(2, n, MOD) - 1 - Choose(n, a, MOD) - Choose(n, b, MOD)) % MOD)


if __name__ == "__main__":
    main()
