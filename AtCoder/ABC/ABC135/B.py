def main():
    N = int(input())
    p = list(map(int, input().split()))
    tgt = list(sorted(p))
    print("Yes" if sum([1 for i in range(N) if p[i] != tgt[i]]) <= 2 else "No")


if __name__ == "__main__":
    main()
