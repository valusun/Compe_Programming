def lcm(n, m):
    def gcd(x, y):
        if x % y == 0:
            return y
        return gcd(y, x % y)

    return n // gcd(n, m) * m


def Sum(n):
    return n * (n + 1) // 2


def main():
    N, A, B = map(int, input().split())
    a_cnt = N // A
    b_cnt = N // B
    ab_lcm = lcm(A, B)
    ab_lcm_cnt = N // ab_lcm
    print(Sum(N) - Sum(a_cnt) * A - Sum(b_cnt) * B + Sum(ab_lcm_cnt) * ab_lcm)


if __name__ == "__main__":
    main()
