def main():
    def rotate(a):
        res = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                n_i, n_j = N - j - 1, i
                res[n_i][n_j] = a[i][j]
        return res

    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    B_1 = set((i, j) for i in range(N) for j in range(N) if B[i][j] == 1)
    for _ in range(4):
        A_1 = [(i, j) for i in range(N) for j in range(N) if A[i][j] == 1]
        for i, j in A_1:
            if (i, j) not in B_1:
                break
        else:
            print("Yes")
            exit()
        A = rotate(A)
    print("No")


if __name__ == "__main__":
    main()
