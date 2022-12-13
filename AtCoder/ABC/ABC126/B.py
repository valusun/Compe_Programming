def main():
    def IsMonthFormat(num: str):
        return 1 <= int(num) <= 12

    S = input()
    results = [IsMonthFormat(S[:2]), IsMonthFormat(S[2:])]
    if False not in results:
        print("AMBIGUOUS")
    elif True not in results:
        print("NA")
    elif results[0]:
        print("MMYY")
    else:
        print("YYMM")


if __name__ == "__main__":
    main()
