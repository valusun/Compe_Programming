def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        x = set(S[:i])
        y = set(S[i:])
        if (tmp := len(x & y)) > ans:
            ans = tmp
    print(ans)


if __name__ == "__main__":
    main()
