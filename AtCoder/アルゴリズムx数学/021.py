def combination(n: int, r: int) -> int:
    r = min(n, n - r)
    ans = 1
    for i in range(r):
        ans = ans * (n - i) // (i + 1)
    return ans


def main():
    n, r = map(int, input().split())
    print(combination(n, r))  # math.comb(n,r)


if __name__ == "__main__":
    main()
