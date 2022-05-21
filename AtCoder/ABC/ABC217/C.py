def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i, v in enumerate(P):
        Q[v - 1] = i + 1
    print(*Q)


if __name__ == "__main__":
    main()
