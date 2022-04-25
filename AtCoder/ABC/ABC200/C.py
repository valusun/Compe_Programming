from math import comb


def main():
    _ = int(input())
    A = list(map(int, input().split()))

    A_mod200_counts = [0] * 200
    for a in A:
        A_mod200_counts[a % 200] += 1

    pairs_count = 0
    for n in A_mod200_counts:
        pairs_count += comb(n, 2)
    print(pairs_count)


if __name__ == "__main__":
    main()
