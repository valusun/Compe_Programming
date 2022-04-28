def main():
    sequence = sorted(list(map(int, input().split())))
    if sequence[2] - sequence[1] == sequence[1] - sequence[0]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
