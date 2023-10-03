def main():
    N = int(input())
    counter = [-1] * (N + 1)
    counter[N] = 100
    for _ in range(3):
        t = int(input())
        if t <= N:
            counter[t] = None
    for i in range(N, 0, -1):
        if counter[i] is None or counter[i] <= 0:
            continue
        for t in (1, 2, 3):
            if i - t < 0 or counter[i - t] is None:
                continue
            counter[i - t] = max(counter[i] - 1, counter[i - t])
    print("YES" if counter[0] >= 0 else "NO")


if __name__ == "__main__":
    main()
