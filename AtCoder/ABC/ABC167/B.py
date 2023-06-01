def main():
    A, B, C, K = map(int, input().split())
    ans = 0
    for s, n in ((A, 1), (B, 0), (C, -1)):
        ans += min(s, K) * n
        K = max(0, K - s)
    print(ans)


if __name__ == "__main__":
    main()
