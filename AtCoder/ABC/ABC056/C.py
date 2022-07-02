def main():
    X = int(input())
    max_going_point = 0
    time = 0
    while max_going_point < X:
        time += 1
        max_going_point += time
    print(time)


if __name__ == "__main__":
    main()
