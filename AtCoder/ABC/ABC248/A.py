def main():
    S = set(input())
    print(list(set(str(i) for i in range(10)) - S)[0])


if __name__ == "__main__":
    main()
