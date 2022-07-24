def main():
    a = "".join(input().split())
    print("YES" if int(a) % 4 == 0 else "NO")


if __name__ == "__main__":
    main()
