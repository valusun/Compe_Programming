from itertools import accumulate


def main():
    p, q = input().split()
    dist = [3, 1, 4, 1, 5, 9]
    cusum = [0] + list(accumulate(dist))
    p_i = ord(p) - 65
    q_i = ord(q) - 65
    print(cusum[max(p_i, q_i)] - cusum[min(p_i, q_i)])


if __name__ == "__main__":
    main()
