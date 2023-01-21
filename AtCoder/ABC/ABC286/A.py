def main():
    n, p, q, r, s = map(int, input().split())
    A = list(map(int, input().split()))
    A[r - 1 : s], A[p - 1 : q] = A[p - 1 : q], A[r - 1 : s]
    print(*A)


if __name__ == "__main__":
    main()
