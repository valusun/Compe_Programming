def main():
    _ = int(input())
    S = input()
    left_cnt, right_cnt = 0, 0
    for s in S:
        if s == "(":
            right_cnt += 1
        else:
            if right_cnt:
                right_cnt -= 1
            else:
                left_cnt += 1
    print(f"{'('*left_cnt}{S}{')'*right_cnt}")


if __name__ == "__main__":
    main()
