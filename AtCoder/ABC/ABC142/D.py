from math import sqrt


def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def get_divisors(a, b):
    c = gcd(a, b)
    ret = []
    for i in range(1, int(sqrt(c) + 1)):
        if c % i:
            continue
        ret.append(i)
        if i * i != c:
            ret.append(c // i)
    return ret


def get_prime_cnt(divisors):
    cnt = 0
    for d in divisors:
        for i in range(2, int(sqrt(d) + 1)):
            if d % i == 0:
                break
        else:
            cnt += 1
    return cnt


def main():
    A, B = map(int, input().split())
    divisors = get_divisors(A, B)
    print(get_prime_cnt(divisors))


if __name__ == "__main__":
    main()
