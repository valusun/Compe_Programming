def main():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    sum_a = 0
    for i in range(1, N + 2):
        sum_a += abs(A[i] - A[i - 1])
    for i in range(N):
        t = abs(A[i + 2] - A[i])
        t1 = abs(A[i + 1] - A[i]) + abs(A[i + 2] - A[i + 1])
        print(sum_a + t - t1)


if __name__ == "__main__":
    main()
