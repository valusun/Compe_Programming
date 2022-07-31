import string


def main():
    S = set(input())
    alphabets = string.ascii_lowercase
    for a in alphabets:
        if a not in S:
            print(a)
            break
    else:
        print(None)


if __name__ == "__main__":
    main()
