def main():
    W, a, b = map(int, input().split())
    print(0 if abs(a - b) <= W else abs(a - b) - W)


if __name__ == "__main__":
    main()
