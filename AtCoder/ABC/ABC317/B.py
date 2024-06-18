def main():
    _ = int(input())
    A = list(map(int, input().split()))
    mn, mx = min(A), max(A)
    s = (mx - mn + 1) * (mx + mn) // 2
    print(s - sum(A))


if __name__ == "__main__":
    main()
