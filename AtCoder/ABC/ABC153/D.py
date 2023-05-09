def main():
    H = int(input())
    depth = 1
    while H != 1:
        H //= 2
        depth += 1
    print(2**depth - 1)


if __name__ == "__main__":
    main()
