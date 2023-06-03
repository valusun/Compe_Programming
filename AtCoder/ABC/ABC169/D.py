from math import sqrt


def get_factors(n):
    ret = []
    for p in range(2, int(sqrt(n)) + 1):
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt != 0:
            ret.append((p, cnt))
    if n > 1:
        ret.append((n, 1))
    return ret


def main():
    N = int(input())
    factors = get_factors(N)
    ans = 0
    for p, c in factors:
        cnt = 1
        while True:
            if cnt * (cnt + 1) > 2 * c:
                break
            cnt += 1
        ans += cnt - 1
    print(ans)


if __name__ == "__main__":
    main()
