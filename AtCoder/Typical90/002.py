def GenerateCorrectParentheses(n, parentheses):
    """正しい括弧列を作成する

    Args:
        n (int): 作成する括弧列の長さ
        par (str): 現時点で作成した括弧
    """

    if len(parentheses) == n:
        print(parentheses)
        return
    left_cnt = parentheses.count("(")
    right_cnt = parentheses.count(")")
    if left_cnt < n // 2:
        GenerateCorrectParentheses(n, parentheses + "(")
    if left_cnt > right_cnt:
        GenerateCorrectParentheses(n, parentheses + ")")


def main():
    N = int(input())
    GenerateCorrectParentheses(N, "")


if __name__ == "__main__":
    main()
