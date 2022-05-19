from itertools import permutations


def main():
    S, K = input().split()
    p = sorted(list(set(permutations(S))))
    print("".join(p[int(K) - 1]))


if __name__ == "__main__":
    main()
