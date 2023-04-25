def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans, now = 0, 1
    for a in A:
        if a == now:
            now += 1
        else:
            ans += 1
    print(-1 if ans == N else ans)


if __name__ == "__main__":
    main()
