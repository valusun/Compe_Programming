def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    dist = [A[0]]
    for i in range(1, N):
        dist.append(A[i] - A[i - 1])
    dist.append(K - A[-1] + A[0])
    print(K - max(dist))


if __name__ == "__main__":
    main()
