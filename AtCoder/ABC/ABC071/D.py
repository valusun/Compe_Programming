def main():
    N = int(input())
    Field = [list(input()) for _ in range(2)]
    MOD = 10**9 + 7
    ans = 1
    pre = None
    i = 0
    while i < N:
        if Field[0][i] == Field[1][i]:
            if pre == "Tate":
                ans *= 2
            elif pre == "Yoko":
                pass
            else:
                ans *= 3
            pre = "Tate"
            i += 1
        else:
            if pre == "Tate":
                ans *= 2
            elif pre == "Yoko":
                ans *= 3
            else:
                ans *= 6
            pre = "Yoko"
            i += 2
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
