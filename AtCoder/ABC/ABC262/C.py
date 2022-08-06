def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i, v in enumerate(A):
        if v == i + 1:
            ans += 1
    ans = ans * (ans - 1) // 2
    for i in range(N):
        if A[i] > i + 1 and A[A[i] - 1] == i + 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
