def main():
    x, a, b = map(int, input().split())
    print("A" if abs(x - a) < abs(x - b) else "B")


if __name__ == "__main__":
    main()
