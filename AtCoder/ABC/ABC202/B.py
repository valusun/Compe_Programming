def main():
    ans = ""
    for s in input():
        if s == "6":
            ans += "9"
        elif s == "9":
            ans += "6"
        else:
            ans += s
    print(ans[::-1])


if __name__ == "__main__":
    main()
