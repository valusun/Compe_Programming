def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = []
    for i in range(M, -1, -1):
        B.append(C[i + N] // A[N])
        for j in range(N + 1):
            C[i + j] -= A[j] * B[-1]
    print(*B[::-1])


if __name__ == "__main__":
    main()
