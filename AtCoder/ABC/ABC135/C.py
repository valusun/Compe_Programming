def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if B[i] >= A[i] + A[i + 1]:
            ans += A[i] + A[i + 1]
            A[i + 1] = 0
            continue
        ans += B[i]
        if B[i] > A[i]:
            A[i + 1] -= B[i] - A[i]
    print(ans)


if __name__ == "__main__":
    main()
