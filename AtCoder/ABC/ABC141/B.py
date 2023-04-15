def main():
    S = input()
    for i, s in enumerate(S, start=1):
        if (i % 2 and s == "L") or (i % 2 == 0 and s == "R"):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
