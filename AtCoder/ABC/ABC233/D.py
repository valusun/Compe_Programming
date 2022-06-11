from itertools import accumulate
from typing import Counter


def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    cusum_A = list(accumulate(A))
    element_counts = Counter()
    element_counts[0] += 1
    ans = 0
    for x in cusum_A:
        y = x - K
        ans += element_counts[y]
        element_counts[x] += 1
    print(ans)


if __name__ == "__main__":
    main()
