from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cusum_A = [0] + list(accumulate(A))
    xor_A = [0]
    for i, x in enumerate(A):
        xor_A.append(xor_A[-1] ^ A[i])
    ans = 0
    for i in range(N):
        ok, ng = i, N + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            tgt_xor = xor_A[mid] ^ xor_A[i]
            tgt_sum = cusum_A[mid] - cusum_A[i]
            if tgt_xor == tgt_sum:
                ok = mid
            else:
                ng = mid
        ans += ok - i
    print(ans)


if __name__ == "__main__":
    main()
