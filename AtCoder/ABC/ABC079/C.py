def main():
    A = input()
    for i in range(8):
        siki = A[0]
        for j in range(3):
            if i & (1 << j):
                siki += "+"
            else:
                siki += "-"
            siki += A[j + 1]
        if eval(siki) == 7:
            print(f"{siki}=7")
            break


if __name__ == "__main__":
    main()
