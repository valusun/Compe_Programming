from collections import Counter
from heapq import heappop, heappush


def main():
    Q = int(input())
    S_min, S_max = [], []
    S_in_numbers = Counter()
    for _ in range(Q):
        t, *a = map(int, input().split())
        if t == 1:
            heappush(S_min, a[0])
            heappush(S_max, -a[0])
            S_in_numbers[a[0]] += 1
        elif t == 2:
            S_in_numbers[a[0]] -= min(a[1], S_in_numbers[a[0]])
        else:
            while True:
                x = heappop(S_min)
                if S_in_numbers[x]:
                    S_minimum = x
                    heappush(S_min, x)
                    break
            while True:
                x = heappop(S_max) * (-1)
                if S_in_numbers[x]:
                    S_maximum = x
                    heappush(S_max, -x)
                    break
            print(S_maximum - S_minimum)


if __name__ == "__main__":
    main()
