def main():
    N = int(input())
    if N % 10 in (2, 4, 5, 7, 9):
        print("hon")
    elif N % 10 == 3:
        print("bon")
    else:
        print("pon")


if __name__ == "__main__":
    main()
