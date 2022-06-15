from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    C = Counter()
    for a in A:
        C[a] += 1
    print(C.most_common()[-1][0])


if __name__ == "__main__":
    main()
