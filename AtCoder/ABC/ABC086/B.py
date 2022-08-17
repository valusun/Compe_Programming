def main():
    a, b = input().split()
    tgt = int(f"{a}{b}")
    i = 1
    while i * i <= tgt:
        if i * i == tgt:
            print("Yes")
            exit()
        i += 1
    print("No")


if __name__ == "__main__":
    main()
