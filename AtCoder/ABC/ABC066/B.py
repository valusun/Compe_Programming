def main():
    S = input()

    while S := S[:-1]:
        one_sided = S[: len(S) // 2]
        if one_sided * 2 == S:
            print(len(S))
            break


if __name__ == "__main__":
    main()
