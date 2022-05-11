def main():
    print("Yes" if len(set(list(input() for _ in range(4)))) == 4 else "No")


if __name__ == "__main__":
    main()
