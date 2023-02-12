def main():
    S = input()
    a1, num, a2 = S[0], S[1:-1], S[-1]
    # "A0999999B"で死ぬため、len(num)==6は必要
    is_num_rules = num.isdecimal() and len(num) == 6 and 100000 <= int(num) <= 999999
    if a1.isupper() and a2.isupper() and is_num_rules:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
