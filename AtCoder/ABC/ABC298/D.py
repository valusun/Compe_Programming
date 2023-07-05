from collections import deque


def Pow(x, n, mod):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * x % mod
        x = x * x % mod
        n >>= 1
    return ret


def main():
    Q = int(input())
    ans = 1
    s = deque()
    s.append(1)
    MOD = 998244353
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            ans = (ans * 10 + q[1]) % MOD
            s.append(q[1])
        elif q[0] == 2:
            t = s.popleft()
            ans = (ans - t * Pow(10, len(s), MOD)) % MOD
        else:
            print(ans)


if __name__ == "__main__":
    main()
