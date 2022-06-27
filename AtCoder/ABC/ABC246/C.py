def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    for i, a in enumerate(A):
        if a // X > K:
            A[i] -= X * K
            K = 0
            break
        else:
            A[i] %= X
            K -= a // X

    A.sort(reverse=True)
    print(sum(A[K:]))


if __name__ == "__main__":
    main()
