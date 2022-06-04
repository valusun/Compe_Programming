def main():
    S1 = input()
    S2 = input()
    if S1 + S2 == "#..#" or S1 + S2 == ".##.":
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
