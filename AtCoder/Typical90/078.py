def main():
    N, M = map(int, input().split())
    memo = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        c = sorted([a, b])
        memo[c[1] - 1] += 1
    print(memo.count(1))


if __name__ == "__main__":
    main()
