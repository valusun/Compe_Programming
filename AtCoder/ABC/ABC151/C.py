def main():
    N, M = map(int, input().split())
    A = [list(input().split()) for _ in range(M)]
    ac = [False] * (N + 1)
    wa = [0] * (N + 1)
    for a, s in A:
        a = int(a)
        if ac[a]:
            continue
        if s == "WA":
            wa[a] += 1
        else:
            ac[a] = True
    w = sum([w for i, w in enumerate(wa) if ac[i]])
    print(sum(ac), w)


if __name__ == "__main__":
    main()
