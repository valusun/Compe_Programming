def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    B = [a[:] for a in A]

    for i in range(N):
        for j in range(N):
            if not (i == 0 or i == N - 1 or j == 0 or j == N - 1):
                continue
            if i == 0 and j < N - 1:
                B[i][j + 1] = A[i][j]
            if i < N - 1 and j == N - 1:
                B[i + 1][j] = A[i][j]
            if i == N - 1 and j > 0:
                B[i][j - 1] = A[i][j]
            if i > 0 and j == 0:
                B[i - 1][j] = A[i][j]

    for b in B:
        print(*b, sep="")


if __name__ == "__main__":
    main()
