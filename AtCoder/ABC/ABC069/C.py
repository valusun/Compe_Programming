def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd, multiple_four = 0, 0
    for a in A:
        if a % 4 == 0:
            multiple_four += 1
        if a % 2:
            odd += 1

    if multiple_four + 1 == odd and N - multiple_four - odd == 0:
        print("Yes")
    elif multiple_four < odd:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
