def main():
    S = input()
    N = len(S)
    ans, i = 0, 0
    while i < N:
        if S[i] != "0":
            i += 1
        else:
            if i + 1 == N or S[i + 1] != "0":
                i += 1
            else:
                i += 2
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
