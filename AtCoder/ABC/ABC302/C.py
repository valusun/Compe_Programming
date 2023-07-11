from itertools import permutations


def main():
    def is_check(s1, s2):
        d_c = 0
        for i in range(M):
            if s1[i] != s2[i]:
                d_c += 1
        return d_c != 1

    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    for p in permutations(S):
        for i in range(1, N):
            if is_check(p[i - 1], p[i]):
                break
        else:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
