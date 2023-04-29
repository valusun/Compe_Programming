from itertools import permutations


def main():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    i = 0
    for p in permutations(range(1, N + 1)):
        if p == P:
            p_i = i
        if p == Q:
            q_i = i
        i += 1
    print(abs(p_i - q_i))


if __name__ == "__main__":
    main()
