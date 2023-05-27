def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(-1, N - sum(A)))


if __name__ == "__main__":
    main()
