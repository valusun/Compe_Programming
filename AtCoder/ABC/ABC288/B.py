def main():
    N, K = map(int, input().split())
    S = list(input() for _ in range(N))
    print(*sorted(S[:K]), sep="\n")


if __name__ == "__main__":
    main()
