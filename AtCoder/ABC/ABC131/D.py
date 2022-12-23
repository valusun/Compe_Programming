def main():
    N = int(input())
    tasks = [list(map(int, input().split())) for _ in range(N)]
    tasks.sort(key=lambda x: x[1])
    now = 0
    for a, b in tasks:
        if (now := now + a) > b:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
