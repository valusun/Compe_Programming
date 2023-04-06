def main():
    N, M = map(int, input().split())
    ans = 10**12 + 1
    for a in range(1, N + 1):
        b = (M + a - 1) // a
        if b <= N:
            ans = min(ans, a * b)
        if a > b:
            break
    print(-1 if ans > 10**12 else ans)


if __name__ == "__main__":
    main()
