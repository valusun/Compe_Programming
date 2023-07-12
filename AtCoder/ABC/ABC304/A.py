def main():
    N = int(input())
    n, a = [], []
    for _ in range(N):
        nn, aa = input().split()
        n.append(nn)
        a.append(int(aa))
    idx = a.index(min(a))
    ans = n[idx:] + n[:idx]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
