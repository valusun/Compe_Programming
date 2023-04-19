from math import sqrt


def main():
    N = int(input())
    ans = N
    for i in range(1, int(sqrt(N)) + 1):
        if N % i:
            continue
        j = N // i
        ans = min(ans, i + j - 2)
    print(ans)


if __name__ == "__main__":
    main()
