def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    K = int(input())
    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            z = gcd(a, b)
            for c in range(1, K + 1):
                ans += gcd(z, c)
    print(ans)


if __name__ == "__main__":
    main()
