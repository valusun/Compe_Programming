from math import sqrt


def main():
    def get_divisor(n):
        ret = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                ret.append(i)
                if i * i != n:
                    ret.append(n // i)
        return ret

    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    cnt = [0] * N
    for i in range(N - 1, -1, -1):
        if cnt[i] == A[i]:
            continue
        ans.append(i + 1)
        divisor = get_divisor(i + 1)
        for d in divisor:
            cnt[d - 1] = (cnt[d - 1] + 1) % 2
    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
