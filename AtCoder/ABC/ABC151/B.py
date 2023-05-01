def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    x = N * M - sum(A)
    if x < 0:
        print(0)
    elif x > K:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    main()
