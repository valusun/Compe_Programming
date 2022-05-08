def main():
    P = int(input())
    factorial = [1]
    for i in range(2, 11):
        factorial.append(factorial[-1] * i)
    ans = 0
    for f in factorial[::-1]:
        if f > P:
            continue
        ans += P // f
        P -= f * (P // f)
    print(ans)


if __name__ == "__main__":
    main()
