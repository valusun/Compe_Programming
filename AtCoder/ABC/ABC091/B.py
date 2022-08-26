from collections import Counter


def main():
    N = int(input())
    dic = Counter()
    for _ in range(N):
        dic[input()] += 1
    M = int(input())
    for _ in range(M):
        dic[input()] -= 1
    print(max(0, dic.most_common()[0][1]))


if __name__ == "__main__":
    main()
