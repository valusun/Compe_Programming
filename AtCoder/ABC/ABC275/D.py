def main():
    N = int(input())
    memo = dict()
    memo[0] = 1

    def f(n):
        if n in memo:
            return memo[n]
        memo[n] = f(n // 2) + f(n // 3)
        return memo[n]

    print(f(N))


if __name__ == "__main__":
    main()
