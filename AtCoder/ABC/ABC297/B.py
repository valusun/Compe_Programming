def main():
    s = input()
    fb, sb = s.index("B"), len(s) - s[::-1].index("B") - 1
    fr, sr = s.index("R"), len(s) - s[::-1].index("R") - 1
    k = s.index("K")
    if fb % 2 != sb % 2 and fr < k < sr:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
