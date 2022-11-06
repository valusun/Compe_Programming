def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    g = A[0]
    for a in A[1:]:
        g = gcd(g, a)
    ans = 0
    for a in A:
        a //= g
        while a % 2 == 0:
            a //= 2
            ans += 1
        while a % 3 == 0:
            a //= 3
            ans += 1
        if a != 1:
            print(-1)
            break
    else:
        print(ans)


if __name__ == "__main__":
    main()
