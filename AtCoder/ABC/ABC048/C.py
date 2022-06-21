def main():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i - 1] + a[i] > x:
            ans += a[i - 1] + a[i] - x
            a[i] = max(0, -a[i - 1] + x)
    print(ans)


if __name__ == "__main__":
    main()
