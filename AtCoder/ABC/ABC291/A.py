def main():
    S = input()
    for i, s in enumerate(S):
        if s.isupper():
            print(i + 1)


if __name__ == "__main__":
    main()
