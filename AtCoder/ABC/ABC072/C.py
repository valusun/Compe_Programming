def main():
    _ = int(input())
    A = list(map(int, input().split()))
    memo = [0] * (10**5 + 5)
    for a in A:
        for i in range(-1, 2):
            memo[a + i] += 1
    print(max(memo))


if __name__ == "__main__":
    main()
