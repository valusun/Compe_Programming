def main():
    S = input()
    ans = 0
    for i, s in enumerate(S[::-1]):
        ans += (ord(s) - 64) * 26**i
    print(ans)


if __name__ == "__main__":
    main()
