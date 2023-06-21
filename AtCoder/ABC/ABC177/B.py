def main():
    S = input()
    T = input()
    S_n, T_n = len(S), len(T)
    ans = S_n
    for i in range(S_n - T_n + 1):
        tmp_S = S[i : i + T_n]
        res = 0
        for j in range(T_n):
            if tmp_S[j] != T[j]:
                res += 1
        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
