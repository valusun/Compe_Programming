def main():
    N, _, W = map(int, input().split())
    A = list(map(int, input().split()))
    if N >= 2:
        ans = max(abs(A[-1] - W), abs(A[-2] - A[-1]))
    else:
        ans = abs(A[0] - W)

    print(ans)


if __name__ == "__main__":
    main()
