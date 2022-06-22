def main():
    A = sorted(list(map(int, input().split())))
    print("Yes" if A[0] + A[1] == A[2] else "No")


if __name__ == "__main__":
    main()
