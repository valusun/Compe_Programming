def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    a, b, c, d = map(int, input().split())
    a -= 1
    lcm = c // gcd(c, d) * d
    e = a - a // c - a // d + a // lcm
    f = b - b // c - b // d + b // lcm
    print(f - e)


if __name__ == "__main__":
    main()
