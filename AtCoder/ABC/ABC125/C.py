def gcd(x, y):
    return gcd(y, x % y) if y else x


def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        left[i + 1] = gcd(left[i], A[i])
    for i in range(N - 1, -1, -1):
        right[i] = gcd(right[i + 1], A[i])
    ans = 0
    for i in range(N):
        res = gcd(left[i], right[i + 1])
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
