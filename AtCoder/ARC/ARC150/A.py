from itertools import accumulate


def CheckRules(N, K, S):
    """引数が条件を満たしていればYes, 満たしていなければNoを返す"""

    one_cusum = list(accumulate([1 if s == "1" else 0 for s in S], initial=0))
    zero_cusum = list(accumulate([1 if s == "0" else 0 for s in S], initial=0))
    one_cnt = one_cusum[-1]
    exist = False
    for i in range(N - K + 1):
        not_exist_zero = not zero_cusum[i + K] - zero_cusum[i]
        if one_cusum[i + K] - one_cusum[i] == one_cnt and not_exist_zero:
            if exist:
                return "No"
            exist = True
    return "Yes" if exist else "No"


def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        S = input()
        print(CheckRules(n, k, S))


if __name__ == "__main__":
    main()
