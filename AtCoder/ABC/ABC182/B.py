from math import sqrt


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    gcd_cnts = [0] * (max(A) + 1)
    for a in A:
        for p in range(1, int(sqrt(a)) + 1):
            if a % p == 0:
                gcd_cnts[p] += 1
                if p * p != a:
                    gcd_cnts[a // p] += 1
    gcd_cnts[1] = 0  # "2"以上が答えの対象なので、0にして辻褄を合わせておく
    print(gcd_cnts.index(max(gcd_cnts)))


if __name__ == "__main__":
    main()
