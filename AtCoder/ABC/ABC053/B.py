def main():
    S = input()
    print(len(S) - S[::-1].index("Z") - S.index("A"))


if __name__ == "__main__":
    main()
