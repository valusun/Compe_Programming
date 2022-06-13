def round(x):
    return (x * 2 + 1) // 2


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ave = round(sum(A) / N)
    ans = 0
    for a in A:
        ans += (a - ave) ** 2
    print(int(ans))


if __name__ == "__main__":
    main()
