def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    now, ans = 0, 0
    right = 0
    for left in range(N):
        while right < N and now < K:
            now += A[right]
            right += 1
        if now < K:
            break
        ans += N - right + 1
        now -= A[left]
    print(ans)


if __name__ == "__main__":
    main()
