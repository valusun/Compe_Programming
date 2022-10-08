from bisect import bisect_left
from itertools import accumulate


def main():
    def GetNextStartIndex(start_idx, tgt_sum):
        tgt = tgt_sum + A_cusum[start_idx]
        idx = bisect_left(A_cusum, tgt)
        if idx > N or A_cusum[idx] != tgt:
            return -1
        return idx

    N, P, Q, R = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    A_cusum = list(accumulate(A))

    for x in range(N):
        ans = [x]
        y = GetNextStartIndex(x, P)
        ans.append(y)
        z = GetNextStartIndex(y, Q)
        ans.append(z)
        w = GetNextStartIndex(z, R)
        ans.append(w)
        if x < y < z < w:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
