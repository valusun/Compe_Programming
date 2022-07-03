from math import sqrt


def GetPrimeFactorization(n):
    res = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n != 1:
        res.append(n)
    return res


def main():
    N = int(input())
    divisor_counts = [0] * (N + 1)
    for i in range(2, N + 1):
        divisor_nums = GetPrimeFactorization(i)
        for num in divisor_nums:
            divisor_counts[num] += 1
    ans = 1
    MOD = 10**9 + 7
    for c in divisor_counts:
        if c:
            ans = ans * (c + 1) % MOD
    print(ans)


if __name__ == "__main__":
    main()
