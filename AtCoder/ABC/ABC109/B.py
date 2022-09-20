# TODO:読みやすく
def main():
    N = int(input())
    words = [input() for _ in range(N)]
    for i, w in enumerate(words[1:], 1):
        if words[i - 1][-1] != w[0]:
            print("No")
            break
    else:
        print("Yes" if len(set(words)) == N else "No")


if __name__ == "__main__":
    main()
