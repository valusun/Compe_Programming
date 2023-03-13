def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        s = input()
        ans += s == s[::-1]
    print(ans)


if __name__ == "__main__":
    main()
