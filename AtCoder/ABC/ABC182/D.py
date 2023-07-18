def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = now = 0
    bef_mx = 0
    mp = 0
    for i in range(N):
        ans = max(ans, now + bef_mx)
        mp += A[i]
        now += mp
        bef_mx = max(bef_mx, mp)
    print(max(ans, now))


if __name__ == "__main__":
    main()
