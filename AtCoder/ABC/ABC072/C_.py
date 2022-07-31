from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    c = Counter()
    for a in A:
        for i in range(-1, 2):
            c[a + i] += 1
    print(max(c.items(), key=lambda x: x[1])[1])


if __name__ == "__main__":
    main()
