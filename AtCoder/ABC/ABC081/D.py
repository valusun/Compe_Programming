def main():
    N = int(input())
    A = list(map(int, input().split()))
    idx = A.index(max(A, key=abs))
    actions = []
    for i in range(N):
        actions.append([idx + 1, i + 1])
    if A[idx] > 0:
        for i in range(1, N):
            actions.append([i, i + 1])
    else:
        for i in range(N, 1, -1):
            actions.append([i, i - 1])
    print(len(actions))
    for act in actions:
        print(*act)


if __name__ == "__main__":
    main()
