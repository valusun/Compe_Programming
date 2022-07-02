def main():
    N = int(input())
    MOD = 10**9 + 7
    now = 1
    for i in range(1, N + 1):
        now = now * i % MOD
    print(now)


if __name__ == "__main__":
    main()
