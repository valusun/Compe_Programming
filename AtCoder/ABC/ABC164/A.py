def main():
    S, W = map(int, input().split())
    print("unsafe" if S <= W else "safe")


if __name__ == "__main__":
    main()
