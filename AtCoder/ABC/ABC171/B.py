def main():
    N, K = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    print(sum(p[:K]))


if __name__ == "__main__":
    main()
