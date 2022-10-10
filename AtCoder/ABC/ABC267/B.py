def main():
    n = input()
    column = ""
    column += "1" if n[6] == "1" else "0"
    column += "1" if n[3] == "1" else "0"
    column += "1" if n[1] == "1" or n[7] == "1" else "0"
    column += "1" if n[0] == "1" or n[4] == "1" else "0"
    column += "1" if n[2] == "1" or n[8] == "1" else "0"
    column += "1" if n[5] == "1" else "0"
    column += "1" if n[9] == "1" else "0"

    column = [c for c in column.split("0") if c != ""]
    print("Yes" if len(column) >= 2 and n[0] == "0" else "No")


if __name__ == "__main__":
    main()
