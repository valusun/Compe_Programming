def main():
    X, K, D = map(int, input().split())
    m_cnt = abs(X) // D
    if m_cnt > K:
        print(abs(X) - (D * K))
    else:
        mn = abs(X) % D
        if (K - m_cnt) % 2 == 0:
            print(mn)
        else:
            print(min(abs(mn - D), abs(mn + D)))


if __name__ == "__main__":
    main()
