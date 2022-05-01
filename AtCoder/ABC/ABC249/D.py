from math import sqrt


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    appearances = [0] * (2 * 10**5 + 1)
    for i in A:
        appearances[i] += 1
    ans = 0
    for num in A:
        for i in range(1, int(sqrt(num)) + 1):
            if num % i != 0 and (appearances[i] or appearances[num // i]):
                continue
            if i == num // i:
                ans += appearances[i] * appearances[num // i]
            else:
                ans += appearances[i] * appearances[num // i] * 2
    print(ans)


if __name__ == "__main__":
    main()
