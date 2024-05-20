# --- 楽な解法 ---
# 「一度も負けたことがない人が1人しかいない」: 最強
# 「一度も負けたことがない人が複数人いる」：最強が決まらない -> -1


def main():
    N, M = map(int, input().split())
    is_lose = [False] * N
    for _ in range(M):
        _, b = map(int, input().split())
        is_lose[b - 1] = True
    print(is_lose.index(False) + 1 if is_lose.count(False) == 1 else -1)


if __name__ == "__main__":
    main()
