def main():
    mountain_count = int(input())
    mountains: list = []
    for _ in range(mountain_count):
        mountain, height = input().split()
        mountains.append([int(height), mountain])
    mountains.sort(reverse=True)
    print(mountains[1][1])


if __name__ == "__main__":
    main()
