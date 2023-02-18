def main():
    N, M = map(int, input().split())
    matched = [[False] * N for _ in range(N)]
    for _ in range(M):
        k, *a = map(int, input().split())
        for i in range(k):
            for _, j in enumerate(a[i + 1 :]):
                matched[a[i] - 1][j - 1] = True
    for i in range(N):
        for j in range(i + 1, N):
            if not matched[i][j]:
                print("No")
                exit()
    print("Yes")


if __name__ == "__main__":
    main()
