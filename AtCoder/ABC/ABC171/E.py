from functools import reduce


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    all_xor = reduce(lambda x, y: x ^ y, A, 0)
    print(*[all_xor ^ a for a in A])


if __name__ == "__main__":
    main()
