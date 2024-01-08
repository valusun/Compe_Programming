def main():
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if a + 1 != b:
        print("No")
        exit()
    if a % 3 != 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
