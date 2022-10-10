def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print("No")
        exit()
    print("Yes" if T[: len(S)] == S else "No")


if __name__ == "__main__":
    main()
