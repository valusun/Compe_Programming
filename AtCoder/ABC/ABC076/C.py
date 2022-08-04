def main():
    S = input()
    T = input()
    idx = -1
    for i in range(len(S) - len(T) + 1):
        for j in range(len(T)):
            if S[i + j] != "?" and S[i + j] != T[j]:
                break
        else:
            idx = i
    if idx == -1:
        print("UNRESTORABLE")
    else:
        S = S.replace("?", "a")
        print(f"{S[:idx]}{T}{S[idx+len(T):]}")


if __name__ == "__main__":
    main()
