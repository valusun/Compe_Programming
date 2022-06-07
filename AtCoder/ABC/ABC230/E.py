from math import sqrt


def main():
    N = int(input())
    ans = 0
    for i in range(1, int(sqrt(N)) + 1):
        ans += (N // i - i) * 2
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
