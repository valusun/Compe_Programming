from bisect import bisect_right


def main():
    N = int(input())
    A = list(map(int, input().split()))
    active = [0]
    for idx, a in enumerate(A[1:], start=1):
        res = active[-1] + (a - A[idx - 1]) if idx % 2 else active[-1]
        active.append(res)
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        l_i = bisect_right(A, l) - 1
        r_i = bisect_right(A, r)
        if r_i == N:
            r_i -= 1
        diff1 = l - A[l_i] if l_i % 2 == 1 else 0
        diff2 = A[r_i] - r if r_i % 2 == 0 else 0
        diff3 = active[r_i] - active[l_i]
        print(A[r_i] - A[l_i] - diff1 - diff2 - diff3)


if __name__ == "__main__":
    main()
