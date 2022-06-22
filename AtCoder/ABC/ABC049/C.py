def main():
    S = input()[::-1]
    now = 0
    while now != len(S):
        if len(S) - now >= 5 and (
            S[now : now + 5] == "maerd" or S[now : now + 5] == "esare"
        ):
            now += 5
        elif len(S) - now >= 6 and S[now : now + 6] == "resare":
            now += 6
        elif len(S) - now >= 7 and S[now : now + 7] == "remaerd":
            now += 7
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
