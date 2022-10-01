def main():
    N = int(input())
    A = list(int(input()) for _ in range(N))
    print(sum(A) - max(A) + max(A) // 2)


if __name__ == "__main__":
    main()
