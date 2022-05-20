from collections import deque


def main():
    N, M = map(int, input().split())
    cylinders = []
    top_ball_indexes = [[] for _ in range(N)]
    query = deque()

    def AppendTopBallIdx(ball_number: int, cylinder_idx: int):
        """筒の先頭にあるボールごとに、筒の番号を書き込む

        Args:
            ball_number (int): ボールに書かれた番号
            cylinder_idx (int): 筒番号
        """

        top_ball_indexes[ball_number].append(cylinder_idx)
        if len(top_ball_indexes[ball_number]) == 2:
            query.append(top_ball_indexes[ball_number])

    for i in range(M):
        _ = int(input())
        cylinders.append(deque(map(int, input().split())))
        AppendTopBallIdx(cylinders[i][0] - 1, i)
    action_count = 0
    while query:
        top_idx1, top_idx2 = query.popleft()
        cylinders[top_idx1].popleft()
        if cylinders[top_idx1]:
            AppendTopBallIdx(cylinders[top_idx1][0] - 1, top_idx1)
        cylinders[top_idx2].popleft()
        if cylinders[top_idx2]:
            AppendTopBallIdx(cylinders[top_idx2][0] - 1, top_idx2)
        action_count += 1

    if action_count == N:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
