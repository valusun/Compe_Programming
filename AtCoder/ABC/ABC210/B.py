def main():
    _ = int(input())
    target = list(input()).index("1")
    print("Aoki" if target % 2 else "Takahashi")


if __name__ == "__main__":
    main()
