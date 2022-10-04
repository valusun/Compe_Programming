def main():
    A, B = map(int, input().split())
    print(A + B if B % A == 0 else B - A)


if __name__ == "__main__":
    main()
