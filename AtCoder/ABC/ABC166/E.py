from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    indexes = []
    memo = Counter()
    for i, x in enumerate(A):
        indexes.append(i + x)
        memo[i - x] += 1
    ans = 0
    for i in indexes:
        ans += memo[i]
    print(ans)


if __name__ == "__main__":
    main()
