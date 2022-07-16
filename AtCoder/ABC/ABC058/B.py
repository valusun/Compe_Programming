def main():
    O = input()
    E = input()
    ans = ""
    for i in range(len(E)):
        ans += O[i] + E[i]
    print(ans + O[-1] if len(O) > len(E) else ans)


if __name__ == "__main__":
    main()
