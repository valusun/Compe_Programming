def main():
    N = input()
    if N[0] == N[1] == N[2] or N[1] == N[2] == N[3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
