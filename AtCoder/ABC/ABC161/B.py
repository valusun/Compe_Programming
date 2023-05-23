def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    th = sum(A) / (4 * M)
    print("Yes" if A[M - 1] >= th else "No")


if __name__ == "__main__":
    main()
