from math import comb


def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        a_combination = comb(A + B - 1, A - 1)
        if K <= a_combination and A:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= a_combination
    ans += "a" * A
    ans += "b" * B
    print(ans)


if __name__ == "__main__":
    main()
