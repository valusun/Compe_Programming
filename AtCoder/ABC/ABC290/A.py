def main():
    _, _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = sum(A[b - 1] for b in B)
    print(ans)


if __name__ == "__main__":
    main()
