from math import sqrt


def main():
    _ = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        if a == 1:
            continue
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
