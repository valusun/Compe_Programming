def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 1):
        for j in range(M):
            if B[i][j] + 7 != B[i + 1][j]:
                print("No")
                exit()
    for j in range(M - 1):
        if B[0][j] + 1 != B[0][j + 1] or B[0][j] % 7 == 0:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
