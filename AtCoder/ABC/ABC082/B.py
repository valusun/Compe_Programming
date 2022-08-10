def main():
    s = "".join(sorted(input()))
    t = "".join(sorted(input(), reverse=True))
    print("Yes" if s < t else "No")


if __name__ == "__main__":
    main()
