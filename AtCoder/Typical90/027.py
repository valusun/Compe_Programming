def main():
    N = int(input())
    recorded = set()
    for day in range(N):
        user_name = input()
        if user_name not in recorded:
            print(day + 1)
            recorded.add(user_name)


if __name__ == "__main__":
    main()
