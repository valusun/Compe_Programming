def SumUp(n):
    return (n + 1) * n // 2


def main():
    N = int(input())
    MOD = 998244353
    length_max_num = [0]
    for i in range(1, 20):
        length_max_num.append(int("9" * i))
    ans = 0
    for i in range(1, 20):
        if N >= length_max_num[i]:
            ans += SumUp(length_max_num[i] - length_max_num[i - 1])
        else:
            ans += SumUp(N - length_max_num[i - 1])
            break
        ans %= MOD
    print(ans % MOD)


if __name__ == "__main__":
    main()
