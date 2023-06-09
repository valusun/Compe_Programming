def main():
    X, Y = map(int, input().split())
    for t in range(X + 1):
        if t * 2 + (X - t) * 4 == Y:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
