def main():
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        X += D // A[i]
        X += 1 if D % A[i] else 0
    print(X)


if __name__ == "__main__":
    main()
