def main():
    S = input()
    if "a" not in S:
        print(-1)
    else:
        c = S[::-1].index("a")
        print(len(S) - c)


if __name__ == "__main__":
    main()
