def main():
    N, K = map(int, input().split())
    if K == 0:
        print(N**2)
        exit()
    ans = 0
    for b in range(1, N + 1):
        ans += max(0, b - K) * (N // b) + max(0, N % b - K + 1)
    print(ans)


if __name__ == "__main__":
    main()
