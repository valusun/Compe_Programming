def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    Alice = sum(A[::2])
    Bob = sum(A[1::2])
    print(Alice - Bob)


if __name__ == "__main__":
    main()
