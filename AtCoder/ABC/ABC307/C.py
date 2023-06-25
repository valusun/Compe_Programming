def main():
    Ha, Wa = map(int, input().split())
    A = [list(input()) for _ in range(Ha)]
    Hb, Wb = map(int, input().split())
    B = [list(input()) for _ in range(Hb)]
    Hx, Wx = map(int, input().split())
    X = [list(input()) for _ in range(Hx)]

    # "#"の座標だけを取る
    a_b = [(h, w) for h in range(Ha) for w in range(Wa) if A[h][w] == "#"]
    b_b = [(h, w) for h in range(Hb) for w in range(Wb) if B[h][w] == "#"]
    x_b = [(h, w) for h in range(Hx) for w in range(Wx) if X[h][w] == "#"]

    # Xシートを固定した時に、Aシートが重ねられる座標を求める
    # 重ねられる: "#"の位置が同じ
    a_pattern = list()
    for hx, wx in x_b:
        used_a = set()
        bias_h, bias_w = hx - a_b[0][0], wx - a_b[0][1]
        for ha, wa in a_b:
            nha, nwa = ha + bias_h, wa + bias_w
            is_area = 0 <= nha < Hx and 0 <= nwa < Wx
            if is_area and X[nha][nwa] == "#":
                used_a.add((nha, nwa))
            else:
                break
        else:
            a_pattern.append(used_a)

    # 同様の操作を、Bシートでも行う
    b_pattern = list()
    for hx, wx in x_b:
        used_b = set()
        bias_h, bias_w = hx - b_b[0][0], wx - b_b[0][1]
        for hb, wb in b_b:
            nhb, nwb = hb + bias_h, wb + bias_w
            is_area = 0 <= nhb < Hx and 0 <= nwb < Wx
            if is_area and X[nhb][nwb] == "#":
                used_b.add((nhb, nwb))
            else:
                break
        else:
            b_pattern.append(used_b)

    # シートAで一致する座標パターンと、シートBで一致する座標パターンを重ね合わせて、Xを構成できるかを調べる
    size_x = len(x_b)
    for a_p in a_pattern:
        for b_p in b_pattern:
            if len(a_p | b_p) == size_x:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
