def main():
    Contests = set(["ABC", "ARC", "AGC", "AHC"])
    S = set([input() for _ in range(3)])
    print(*Contests - S)


if __name__ == "__main__":
    main()
