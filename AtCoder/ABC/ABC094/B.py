def main():
    N, M, X = map(int, input().split())
    A = [0] * N
    cost_place = list(map(int, input().split()))
    for cp in cost_place:
        A[cp - 1] += 1
    print(min(sum(A[: X - 1]), sum(A[X:])))


if __name__ == "__main__":
    main()
