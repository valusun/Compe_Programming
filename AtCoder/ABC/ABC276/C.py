def main():
    N = int(input())
    P = list(map(int, input().split()))
    pos = N - 2
    while P[pos] < P[pos + 1]:
        pos -= 1
    i = pos + 1
    while i + 1 < N and P[i + 1] < P[pos]:
        i += 1
    P[pos], P[i] = P[i], P[pos]
    P[pos + 1 :] = sorted(P[pos + 1 :], reverse=True)
    print(*P)


if __name__ == "__main__":
    main()
