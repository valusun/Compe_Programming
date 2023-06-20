def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    n_mx = A[0]
    for i in range(1, N):
        if n_mx <= A[i]:
            n_mx = max(n_mx, A[i])
            continue
        ans += n_mx - A[i]
    print(ans)


if __name__ == "__main__":
    main()
