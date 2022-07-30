def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def lcm(x, y):
    return x // gcd(x, y) * y


def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    if N == 1:
        print(T[0])
        exit()
    ans = lcm(T[0], T[1])
    for i in range(2, N):
        ans = lcm(ans, T[i])
    print(ans)


if __name__ == "__main__":
    main()
