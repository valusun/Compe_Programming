def main():
    N, S = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if (j := S - i) > 0:
            ans += min(j, S)
        else:
            break
    print(ans)


if __name__ == "__main__":
    main()
