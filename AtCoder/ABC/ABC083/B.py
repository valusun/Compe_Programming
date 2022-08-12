def SumDigit(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res


def main():
    N, A, B = map(int, input().split())
    ans = 0
    for num in range(1, N + 1):
        if A <= SumDigit(num) <= B:
            ans += num
    print(ans)


if __name__ == "__main__":
    main()
