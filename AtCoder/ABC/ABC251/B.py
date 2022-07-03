def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    possible_numbers = set()

    def Check(n):
        if n <= W:
            possible_numbers.add(n)

    for i in range(N):
        Check(A[i])
        for j in range(i + 1, N):
            Check(A[i] + A[j])
            for k in range(j + 1, N):
                Check(A[i] + A[j] + A[k])
    print(len(possible_numbers))


if __name__ == "__main__":
    main()
