def main():
    s = input()
    print("yes" if len(set(s)) == len(s) else "no")


if __name__ == "__main__":
    main()
