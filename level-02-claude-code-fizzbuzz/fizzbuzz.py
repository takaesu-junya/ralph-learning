"""
FizzBuzz実装モジュール

1から指定された数までの数を処理し、以下のルールに従って出力する:
- 3の倍数の場合は "Fizz"
- 5の倍数の場合は "Buzz"
- 3と5両方の倍数の場合は "FizzBuzz"
- それ以外の場合は数字そのもの
"""


def fizzbuzz(n):
    """
    FizzBuzzのロジックを実装する関数

    Args:
        n (int): 処理する数値（1以上の整数）

    Returns:
        list: FizzBuzzの結果のリスト

    Raises:
        TypeError: nが整数でない場合
        ValueError: nが1未満の場合
    """
    # 型チェック
    if not isinstance(n, int):
        raise TypeError(f"引数は整数である必要があります。与えられた型: {type(n).__name__}")

    # 値の範囲チェック
    if n < 1:
        raise ValueError(f"引数は1以上である必要があります。与えられた値: {n}")

    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


def print_fizzbuzz(n):
    """
    FizzBuzzの結果を標準出力に表示する関数

    Args:
        n (int): 処理する数値（1以上の整数）

    Raises:
        TypeError: nが整数でない場合
        ValueError: nが1未満の場合
    """
    results = fizzbuzz(n)
    for result in results:
        print(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("使用方法: python fizzbuzz.py <数値>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print_fizzbuzz(n)
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)
    except TypeError as e:
        print(f"エラー: {e}")
        sys.exit(1)
