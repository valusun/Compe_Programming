def main():
    X = list(input())
    if len(set(X)) == 1:
        print("Weak")
        return
    for i in range(3):
        if (int(X[i]) + 1) % 10 != int(X[i + 1]):
            print("Strong")
            break
    else:
        print("Weak")


if __name__ == "__main__":
    main()
