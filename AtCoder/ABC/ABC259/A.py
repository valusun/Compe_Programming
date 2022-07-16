def main():
    A = list(map(int, input().split()))
    if A[1] <= A[2]:
        first = A[3] - (A[2] * A[4])
        print(first + A[1] * A[4])
    else:
        print(A[3])


if __name__ == "__main__":
    main()
