def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] == "L":
                continue
            if A[i][j] == "L" and A[j][i] == "W":
                continue
            if A[i][j] == A[j][i] == "D":
                continue
            print("incorrect")
            exit()

    print("correct")


if __name__ == "__main__":
    main()
