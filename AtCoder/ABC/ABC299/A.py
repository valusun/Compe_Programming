def main():
    N = int(input())
    S = input()
    s, e = S.index("|"), N - S[::-1].index("|")
    print("in" if "*" in S[s:e] else "out")


if __name__ == "__main__":
    main()
