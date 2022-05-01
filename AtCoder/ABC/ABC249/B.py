def main():
    S = input()
    is_char_check = [0, 0]
    for s in S:
        if s.isupper():
            is_char_check[0] = 1
        if s.islower():
            is_char_check[1] = 1
    if not is_char_check.count(0) and len(set(S)) == len(S):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
