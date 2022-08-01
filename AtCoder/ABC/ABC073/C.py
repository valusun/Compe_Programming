from collections import Counter


def main():
    N = int(input())
    ans = 0
    dic = Counter()
    for _ in range(N):
        a = int(input())
        dic[a] += 1
        ans += 1 if dic[a] % 2 else -1
    print(ans)


if __name__ == "__main__":
    main()
