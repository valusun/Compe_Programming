def main():
    S = input()
    shift_words = []
    for i in range(len(S)):
        shift_words.append(S[i:] + S[:i])
    shift_words.sort()
    print(shift_words[0], shift_words[-1], sep="\n")


if __name__ == "__main__":
    main()
