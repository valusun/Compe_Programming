def main():
    number_memo = input()
    pattern = 0
    for number in range(10000):
        is_numbers = [0] * 10
        for i in range(4):
            is_numbers[number % 10] = 1
            number //= 10
        for i in range(10):
            if is_numbers[i] and number_memo[i] == "x":
                break
            if not is_numbers[i] and number_memo[i] == "o":
                break
        else:
            pattern += 1
    print(pattern)


if __name__ == "__main__":
    main()
