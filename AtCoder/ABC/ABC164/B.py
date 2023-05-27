def main():
    a, b, c, d = map(int, input().split())
    t_atk_cnt = (c + b - 1) // b
    a_atk_cnt = (a + d - 1) // d
    print("Yes" if a_atk_cnt >= t_atk_cnt else "No")


if __name__ == "__main__":
    main()
