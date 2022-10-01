def main():
    S = input()
    ans = 1000
    for i in range(3, len(S) + 1):
        ans = min(ans, abs(int(S[i - 3 : i]) - 753))
    print(ans)


if __name__ == "__main__":
    main()
