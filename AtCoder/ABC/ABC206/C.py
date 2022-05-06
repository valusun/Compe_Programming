from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    element_counts = Counter()
    print(type(element_counts))
    print(isinstance(element_counts, dict))
    ans = 0
    for i, v in enumerate(A):
        ans += i - element_counts[v]
        element_counts[v] += 1
    print(ans)


if __name__ == "__main__":
    main()
