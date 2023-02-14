from math import sqrt


def main():
    def f(n):
        return A / sqrt(n + 1) + B * n

    A, B = map(int, input().split())
    left, right = 0, 10**18
    while right - left > 2:
        p1 = (left * 2 + right) // 3
        p2 = (left + right * 2) // 3
        if f(p1) > f(p2):
            left = p1
        else:
            right = p2
    ans = 10**18
    for i in range(left, right + 1):
        ans = min(ans, f(i))
    print(ans)


if __name__ == "__main__":
    main()
