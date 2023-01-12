from math import sqrt


def main():
    N, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            tmp = 0
            for y, z in zip(A[i], A[j]):
                tmp += (y - z) ** 2
            if sqrt(tmp) % 1 == 0:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
