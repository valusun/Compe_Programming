def main():
    S = input()
    first_white, first_black = 0, 0
    for i, s in enumerate(S):
        if i % 2:
            if s == "1":
                first_black += 1
            else:
                first_white += 1
        else:
            if s == "1":
                first_white += 1
            else:
                first_black += 1
    print(min(first_black, first_white))


if __name__ == "__main__":
    main()
