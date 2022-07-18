from itertools import accumulate


def GetCusumFromWeightGroups(items):
    """重さごとのリストに分割し、それぞれの重さで価値の累積和を求める"""

    values = [[] for _ in range(4)]
    base_weight = items[0][0]
    for w, v in items:
        values[w - base_weight].append(v)
    cusum_values = []
    for i in range(4):
        # 価値の高いアイテムを優先的に鞄に入れるため
        values[i].sort(reverse=True)
        cusum_values.append([0] + list(accumulate(values[i])))
    return cusum_values


def GetWeights(items):
    """重さのリストを昇順で返す"""

    weights = set()
    for w, _ in items:
        weights.add(w)
    # 重さのパターン数を4に合わせる
    for i in range(4 - len(weights)):
        weights.add(10**10 + i)
    return sorted(list(weights))


def main():
    N, W = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    v = GetCusumFromWeightGroups(items)
    w = GetWeights(items)

    ans = 0
    for w1_cnt in range(len(v[0])):
        for w2_cnt in range(len(v[1])):
            for w3_cnt in range(len(v[2])):
                for w4_cnt in range(len(v[3])):
                    choice_w = (
                        w[0] * w1_cnt + w[1] * w2_cnt + w[2] * w3_cnt + w[3] * w4_cnt
                    )
                    if choice_w > W:
                        break
                    choice_v = v[0][w1_cnt] + v[1][w2_cnt] + v[2][w3_cnt] + v[3][w4_cnt]
                    ans = max(ans, choice_v)
    print(ans)


if __name__ == "__main__":
    main()
