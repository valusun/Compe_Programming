def main():
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        now = 1
        while now <= D:
            X += 1
            now += A[i]
    print(X)


if __name__ == "__main__":
    main()
