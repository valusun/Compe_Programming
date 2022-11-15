def main():
    Q = int(input())
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    for _ in range(Q):
        n, k, *v = list(map(int, input().split()))
        if n == 0:
            print(A[k])
        else:
            A[k] = v[0]


if __name__ == "__main__":
    main()
