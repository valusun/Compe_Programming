from collections import defaultdict
from itertools import combinations


def main():
    MARCH = "MARCH"
    N = int(input())
    dic = defaultdict(int)
    for _ in range(N):
        s = input()
        if s[0] in MARCH:
            dic[s[0]] += 1
    ans = 0
    for p1, p2, p3 in combinations(MARCH, 3):
        ans += dic[p1] * dic[p2] * dic[p3]
    print(ans)


if __name__ == "__main__":
    main()
