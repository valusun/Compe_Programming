def main():
    _, A, B = map(int, input().split())
    C = list(map(int, input().split()))
    print(C.index(A + B) + 1)


if __name__ == "__main__":
    main()
