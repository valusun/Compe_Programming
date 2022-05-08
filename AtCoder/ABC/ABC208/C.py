def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    base = K // N
    K %= N
    if not K:
        for _ in range(N):
            print(base)
    else:
        give_point = sorted(A)[K - 1]
        for a in A:
            if a <= give_point:
                print(base + 1)
            else:
                print(base)


if __name__ == "__main__":
    main()
