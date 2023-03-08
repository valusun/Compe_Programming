def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    print(sum(A[N:-N]) / (N * 5 - N * 2))


if __name__ == "__main__":
    main()
