def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    BC = list(B[C[j] - 1] for j in range(N))

    BC_appearances_counts = [0] * (N + 1)
    for i in BC:
        BC_appearances_counts[i - 1] += 1

    ans = 0
    for i in A:
        ans += BC_appearances_counts[i - 1]
    print(ans)


if __name__ == "__main__":
    main()
