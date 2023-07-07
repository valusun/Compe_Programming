def main():
    N = int(input())
    S = input()
    if "o" not in S or "-" not in S:
        print(-1)
        exit()
    h = [0]
    for i, s in enumerate(S, start=1):
        if s == "-":
            h.append(i)
    h.append(N + 1)
    ans = -1
    for i in range(1, len(h)):
        ans = max(ans, h[i] - h[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
