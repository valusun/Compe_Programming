from bisect import bisect_right
from collections import Counter


def main():
    W, H = map(int, input().split())
    N = int(input())
    p, q = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        p.append(a)
        q.append(b)
    p.append(W)
    q.append(H)
    A = int(input())
    a = list(map(int, input().split()))
    B = int(input())
    b = list(map(int, input().split()))

    m = Counter()
    for i in range(N):
        x = bisect_right(a, p[i])
        y = bisect_right(b, q[i])
        m[(x, y)] += 1
    c = m.most_common()
    mn = c[-1][1] if len(m) == (A + 1) * (B + 1) else 0
    mx = c[0][1]
    print(mn, mx)


if __name__ == "__main__":
    main()
