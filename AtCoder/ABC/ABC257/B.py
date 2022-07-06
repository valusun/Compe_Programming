def main():
    N, K, _ = map(int, input().split())
    A = list(map(int, input().split()))
    S = list(map(int, input().split()))
    for s in S:
        s -= 1
        if s + 1 == K:
            if A[s] != N:
                A[s] += 1
        else:
            if A[s] + 1 != A[s + 1]:
                A[s] += 1
    print(*A)


if __name__ == "__main__":
    main()
