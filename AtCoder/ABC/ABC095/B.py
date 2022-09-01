def main():
    N, X = map(int, input().split())
    M = [int(input()) for _ in range(N)]
    X -= sum(M)
    print(N + X // min(M))


if __name__ == "__main__":
    main()
