from itertools import groupby


def main():
    _ = int(input())
    S = input()
    ans = 0
    for i, k in groupby(S):
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
