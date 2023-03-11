from math import sqrt


def get_pattern(n):
    ret = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ret += 1
            if i * i != n:
                ret += 1
    return ret


def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        x, y = i, N - i
        x_p = get_pattern(x)
        y_p = get_pattern(y)
        ans += x_p * y_p
    print(ans)


if __name__ == "__main__":
    main()
