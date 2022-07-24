def main():
    a, b = map(int, input().split())
    if (c := a + b) > 9:
        print("error")
    else:
        print(c)


if __name__ == "__main__":
    main()
