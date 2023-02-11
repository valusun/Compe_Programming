def main():
    def Check(s1, s2):
        for k in range(M):
            if s1[k] == s2[k] == "x":
                return False
        return True

    N, M = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    ans = 0
    for i, s1 in enumerate(S):
        for s2 in S[i + 1 :]:
            ans += Check(s1, s2)
    print(ans)


if __name__ == "__main__":
    main()
