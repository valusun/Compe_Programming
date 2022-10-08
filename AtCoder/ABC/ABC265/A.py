def main():
    X, Y, N = map(int, input().split())
    print(min(X * N, N // 3 * Y + N % 3 * X))


if __name__ == "__main__":
    main()
