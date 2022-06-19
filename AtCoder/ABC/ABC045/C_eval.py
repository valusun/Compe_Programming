def main():
    S = input()
    ans = 0
    for i in range(2 ** (len(S) - 1)):
        siki = S[0]
        for j in range(len(S) - 1):
            if i & (1 << j):
                siki += "+"
            siki += S[j + 1]
        ans += eval(siki)
    print(ans)


if __name__ == "__main__":
    main()
