def main():
    A, B = map(int, input().split())
    print("Yes" if A <= B <= A * 6 else "No")


if __name__ == "__main__":
    main()
