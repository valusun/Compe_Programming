def main():
    S = input()
    ans = ""
    for i in range(0, len(S), 2):
        ans += S[i + 1] + S[i]
    print(ans)


if __name__ == "__main__":
    main()
