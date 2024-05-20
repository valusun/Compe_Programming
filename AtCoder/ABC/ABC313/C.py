def main():
    N = int(input())
    A = list(map(int, input().split()))
    base = sum(A) // N
    bias_count = sum(A) % base
    sorted_A = sorted(A)
    diff = []
    for i in range(N):
        t = base + 1 if i >= N - bias_count else base
        diff.append(abs(sorted_A[i] - t))
    print(sum(diff) // 2)


if __name__ == "__main__":
    main()
