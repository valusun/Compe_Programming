def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([1 for i in range(1, N) if A[i] > A[i - 1]]))


if __name__ == "__main__":
    main()
