def main():
    A = list(map(int, input().split()))
    K = int(input())
    print(sum(A) + max(A) * 2**K - max(A))


if __name__ == "__main__":
    main()
