from math import sqrt


def main():
    K = int(input())
    ans = 0
    for i in range(2, int(sqrt(K)) + 1):
        cnt = 0
        while K % i == 0:
            K //= i
            cnt += 1
        now = 0
        while cnt > 0:
            now += i
            x = now
            while x % i == 0:
                x //= i
                cnt -= 1
        ans = max(ans, now)
    print(max(ans, K))


if __name__ == "__main__":
    main()
