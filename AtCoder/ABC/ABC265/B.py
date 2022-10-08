from collections import defaultdict


def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    dic = defaultdict(int)
    for _ in range(M):
        x, y = map(int, input().split())
        dic[x - 1] = y

    now = T
    for i in range(N - 1):
        now += dic[i]
        if now <= A[i]:
            print("No")
            break
        now -= A[i]
    else:
        print("Yes")


if __name__ == "__main__":
    main()
