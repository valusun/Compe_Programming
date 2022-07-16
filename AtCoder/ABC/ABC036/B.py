def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        tmp = ""
        for j in range(N - 1, -1, -1):
            tmp += A[j][i]
        print(tmp)


if __name__ == "__main__":
    main()
