def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(2 ** (N - 1)):
        res, tmp = 0, int(S[0])
        for j in range(N - 1):
            if i & (1 << j):
                res += tmp
                tmp = 0
            tmp = tmp * 10 + int(S[j + 1])
        res += tmp
        ans += res
    print(ans)


if __name__ == "__main__":
    main()
