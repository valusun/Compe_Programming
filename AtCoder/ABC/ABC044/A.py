def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    print(min(N, K) * X + max(0, N - K) * Y)


if __name__ == "__main__":
    main()
