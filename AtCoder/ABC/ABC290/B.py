def main():
    _, K = map(int, input().split())
    S = input()
    ans = ""
    for s in S:
        if s == "o" and K:
            ans += "o"
            K -= 1
        else:
            ans += "x"
    print(ans)


if __name__ == "__main__":
    main()
