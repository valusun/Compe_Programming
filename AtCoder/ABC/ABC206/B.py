def main():
    N = int(input())
    now_money = 0
    now_day = 0
    while now_money < N:
        now_day += 1
        now_money += now_day
    print(now_day)


if __name__ == "__main__":
    main()
