def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = A[0]
    for a in A[1:]:
        ans = gcd(ans, a)
    print(ans)


if __name__ == "__main__":
    main()
