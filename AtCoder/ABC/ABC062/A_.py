def main():
    group = [-1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    x, y = map(int, input().split())
    if group[x] == group[y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
