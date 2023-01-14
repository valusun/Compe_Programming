from math import sqrt


def main():
    N = int(input())
    ans = []
    for i in range(2, int(sqrt(N)) + 1):
        while N % i == 0:
            N //= i
            ans.append(i)
    if N != 1:
        ans.append(N)
    print(*ans)


if __name__ == "__main__":
    main()
