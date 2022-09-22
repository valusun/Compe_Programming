def main():
    A = sorted(list(map(int, input().split())), reverse=True)
    print(A[0] * 10 + A[1] + A[2])


if __name__ == "__main__":
    main()
