def main():
    N = list(input())
    n = len(N)
    ans = 10**19
    for i in range(1, 2**n):
        sum_, k = 0, 0
        for j in range(n):
            if i & (1 << j):
                sum_ = sum_ * 10 + int(N[j])
            else:
                k += 1
        if sum_ % 3 == 0:
            ans = min(ans, k)
    print(-1 if ans == 10**19 else ans)


if __name__ == "__main__":
    main()
