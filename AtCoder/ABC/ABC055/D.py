from typing import List


def GetAnimalsLine(S: str, animals: str) -> List[str]:
    """矛盾しない動物の並びを返す

    Args:
        S (str): "o"か"x"の文字列
        animals (str): 動物の並び

    Returns:
        List[str]: 矛盾しない動物の並び(矛盾するなら空リストを返す)
    """

    for i in range(1, len(S)):
        if S[i] == "o":
            if animals[i] == "S":
                animals += animals[i - 1]
            else:
                animals += "W" if animals[i - 1] == "S" else "S"
        else:
            if animals[i] == "S":
                animals += "W" if animals[i - 1] == "S" else "S"
            else:
                animals += animals[i - 1]
    if animals[:2] == animals[-2:]:
        return animals[:-2]
    return []


def main():
    _ = int(input())
    S = input()
    # 1番目と2番目の動物を仮定
    temp_animals = ["SS", "SW", "WS", "WW"]
    for animal in temp_animals:
        animals = GetAnimalsLine(S + S[0], animal)
        if animals:
            print("".join(animals))
            break
    else:
        print("-1")


if __name__ == "__main__":
    main()
