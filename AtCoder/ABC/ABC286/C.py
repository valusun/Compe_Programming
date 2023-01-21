def main():
    def Check(S):
        res = 0
        for i in range(N // 2):
            if S[i] != S[-1 - i]:
                res += B
        return res

    N, A, B = map(int, input().split())
    S = list(input())
    ans = 10**18
    for i in range(N):
        ans = min(ans, Check(S) + A * i)
        S = S[1:] + [S[0]]
    print(ans)


if __name__ == "__main__":
    main()
