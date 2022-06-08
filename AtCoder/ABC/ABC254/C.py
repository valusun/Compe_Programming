def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [[] for _ in range(K)]
    for i, v in enumerate(A):
        B[i % K].append(v)
    for j in range(K):
        B[j].sort()
    C = []
    for i in range(N):
        C.append(B[i % K][i // K])
    if sorted(A) == C:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
