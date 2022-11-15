def main():
    N, k = map(int, input().split())
    A = list(map(int, input().split()))
    print(A[k], A[-k - 1], sep="\n")


if __name__ == "__main__":
    main()
