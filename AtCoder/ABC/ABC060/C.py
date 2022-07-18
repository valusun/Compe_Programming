def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    prev_diff = []
    for i in range(1, N):
        prev_diff.append(t[i] - t[i - 1])
    total = 0
    for pd in prev_diff:
        total += min(T, pd)
    print(total + T)


if __name__ == "__main__":
    main()
