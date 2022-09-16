from math import sqrt


def main():
    N = int(input())
    ans = 0
    for n in range(1, N + 1, 2):
        res = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                res += 1
                if n // i != i:
                    res += 1
        if res == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
