from math import sqrt


def main():
    N, M = map(int, input().split())
    ans = 1
    for i in range(1, int(sqrt(M)) + 1):
        if M % i == 0 and N * i <= M:
            ans = max(ans, i)
            if M // i * N <= M:
                ans = max(ans, M // i)
    print(ans)


if __name__ == "__main__":
    main()
