from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    bias = 0
    reset_cnt = 0
    c = Counter()
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            bias = q[1]
            reset_cnt += 1
        if q[0] == 2:
            c[(reset_cnt, q[1])] += q[2]
        if q[0] == 3:
            if reset_cnt:
                print(c[(reset_cnt, q[1])] + bias)
            else:
                print(A[q[1] - 1] + c[(reset_cnt, q[1])])


if __name__ == "__main__":
    main()
