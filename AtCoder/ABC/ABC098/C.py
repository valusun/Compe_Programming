from itertools import accumulate


def main():
    N = int(input())
    S = input()
    west = [1 if s == "W" else 0 for s in S]
    east = [1 if s == "E" else 0 for s in S]
    cusum_west = [0] + list(accumulate(west))
    cusum_east = [0] + list(accumulate(east))
    ans = 10**6
    for i in range(N + 1):
        ans = min(ans, cusum_west[i] + (cusum_east[-1] - cusum_east[i]))
    print(ans)


if __name__ == "__main__":
    main()
