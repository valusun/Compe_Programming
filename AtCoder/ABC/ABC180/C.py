from math import sqrt


def main():
    N = int(input())
    ans = []
    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
            ans.append(i)
            if i * i != N:
                ans.append(N // i)
    print(*list(sorted(ans)), sep="\n")


if __name__ == "__main__":
    main()
