def main():
    S = input()
    l_s = len(S)
    N = int(input())
    mn = S.replace("?", "0")
    if int(mn, 2) > N:
        print(-1)
        exit()
    ans = int(mn, 2)
    for i, s in enumerate(S):
        if s != "?":
            continue
        if ans + 2 ** (l_s - i - 1) <= N:
            ans += 2 ** (l_s - i - 1)
    print(ans)


if __name__ == "__main__":
    main()
