def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if max(A[i], A[j], A[k]) == A[j]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
