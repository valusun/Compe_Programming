def pow_(x, n, MOD):
    ret = 1
    while n > 0:
        if n & 1:
            ret *= x % MOD
        x *= x
        n >>= 1
    return ret


def main():
    N = int(input())
    MOD = 10**9 + 7
    all_ = pow_(10, N, MOD)
    not_zero = pow_(9, N, MOD)
    not_nine = not_zero
    not_zero_and_nine = pow_(8, N, MOD)
    print((all_ - not_zero - not_nine + not_zero_and_nine) % MOD)


if __name__ == "__main__":
    main()
