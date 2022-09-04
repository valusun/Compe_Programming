from math import sqrt


def main():
    X = int(input())
    ans = 1
    for i in range(2, int(sqrt(X)) + 1):
        for j in range(X):
            if i**j <= X:
                ans = max(ans, i**j)
            else:
                break
    print(ans)


if __name__ == "__main__":
    main()
