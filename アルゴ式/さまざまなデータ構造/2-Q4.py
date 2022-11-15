def main():
    _ = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        n, m, *v = map(int, input().split())
        if n == 0:
            A.insert(m, v[0])
        elif n == 1:
            del A[m]
        else:
            print(A.count(m))


if __name__ == "__main__":
    main()
