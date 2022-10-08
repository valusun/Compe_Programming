def main():
    def IsBlack(x, y):
        x = min(abs(16 - x), x)
        y = min(abs(16 - y), y)
        if x % 2 and x <= y <= (16 - x):
            return True
        return False

    R, C = map(int, input().split())
    print("black" if IsBlack(R, C) or IsBlack(C, R) else "white")


if __name__ == "__main__":
    main()
