from collections import deque


def main():
    K = int(input())
    q = deque([str(i) for i in range(1, 10)])
    cnt = 0
    while q:
        n = q.popleft()
        cnt += 1
        if cnt == K:
            print(n)
            break
        nn = int(n[-1])
        if nn != 0:
            q.append(f"{n}{nn-1}")
        q.append(f"{n}{nn}")
        if nn != 9:
            q.append(f"{n}{nn+1}")


if __name__ == "__main__":
    main()
