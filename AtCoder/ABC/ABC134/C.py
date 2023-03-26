def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    sorted_a = sorted(A, reverse=True)
    for a in A:
        print(sorted_a[1] if a == sorted_a[0] else sorted_a[0])


if __name__ == "__main__":
    main()
