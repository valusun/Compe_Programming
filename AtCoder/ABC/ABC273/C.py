from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    c = sorted(c.items(), reverse=True)
    for i in range(N):
        if len(c) > i:
            print(c[i][1])
        else:
            print(0)


if __name__ == "__main__":
    main()
