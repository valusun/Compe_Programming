def main():
    A, B = input().split()
    if A == B:
        print("=")
    elif A < B:
        print("<")
    else:
        print(">")


if __name__ == "__main__":
    main()
