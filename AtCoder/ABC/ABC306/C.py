from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    memo = [(0, 0)] * N
    cnt = Counter()
    for i, a in enumerate(A):
        if cnt[a] == 1:
            memo[a - 1] = (i, a)
        cnt[a] += 1
    memo.sort()
    ans = []
    for _, i in memo:
        ans.append(i)
    print(*ans)


if __name__ == "__main__":
    main()
