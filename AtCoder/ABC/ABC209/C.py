def main():
    _ = int(input())
    C = sorted(list(map(int, input().split())))
    ans = 1
    MOD = 10**9 + 7
    for i, v in enumerate(C):
        ans *= v - i
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
