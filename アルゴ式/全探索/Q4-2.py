from math import sqrt


def get_divisor_cnt(n):
    cnt = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if i * i != n:
                cnt += 1
    return cnt


def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if get_divisor_cnt(i) == K:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
