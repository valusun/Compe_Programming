def main():
    N = int(input())
    A = []
    for _ in range(N):
        _ = int(input())
        A.append(list(map(int, input().split())))
    X = int(input())

    hit = sorted([(i + 1, a) for i, a in enumerate(A) if X in a], key=lambda x: len(x[1]))
    ans = [h[0] for h in hit if len(h[1]) == len(hit[0][1])]
    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
