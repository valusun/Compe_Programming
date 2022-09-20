def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    dist = [abs(X - a) for a in x]
    ans = dist[0]
    for x in dist:
        ans = gcd(ans, x)
    print(ans)


if __name__ == "__main__":
    main()
