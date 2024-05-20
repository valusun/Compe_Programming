def main():
    _ = int(input())
    A = list(map(int, input().split()))
    if max(A) == A[0] and A.count(max(A)) == 1:
        print(0)
    else:
        print(max(A) - A[0] + 1)


if __name__ == "__main__":
    main()
