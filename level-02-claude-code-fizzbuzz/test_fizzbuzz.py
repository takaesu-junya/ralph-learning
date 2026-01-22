"""
FizzBuzzの単体テスト

PyTestを使用してfizzbuzz関数の動作を検証する
"""

import pytest
from fizzbuzz import fizzbuzz, print_fizzbuzz


class TestFizzBuzz:
    """FizzBuzz関数のテストクラス"""

    def test_fizzbuzz_basic_numbers(self):
        """基本的な数値のテスト"""
        result = fizzbuzz(2)
        assert result == ["1", "2"]

    def test_fizzbuzz_with_fizz(self):
        """3の倍数でFizzが返されることをテスト"""
        result = fizzbuzz(3)
        assert result == ["1", "2", "Fizz"]

    def test_fizzbuzz_with_buzz(self):
        """5の倍数でBuzzが返されることをテスト"""
        result = fizzbuzz(5)
        assert result == ["1", "2", "Fizz", "4", "Buzz"]

    def test_fizzbuzz_with_fizzbuzz(self):
        """15の倍数でFizzBuzzが返されることをテスト"""
        result = fizzbuzz(15)
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        assert result == expected

    def test_fizzbuzz_comprehensive(self):
        """包括的なテスト（1から30まで）"""
        result = fizzbuzz(30)
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
            "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"
        ]
        assert result == expected

    def test_fizzbuzz_single_element(self):
        """n=1のテスト"""
        result = fizzbuzz(1)
        assert result == ["1"]

    def test_fizzbuzz_large_number(self):
        """大きな数値のテスト"""
        result = fizzbuzz(100)
        assert len(result) == 100
        assert result[0] == "1"
        assert result[2] == "Fizz"
        assert result[4] == "Buzz"
        assert result[14] == "FizzBuzz"
        assert result[99] == "Buzz"


class TestFizzBuzzValidation:
    """FizzBuzzのバリデーションテストクラス"""

    def test_fizzbuzz_with_zero(self):
        """n=0でValueErrorが発生することをテスト"""
        with pytest.raises(ValueError) as exc_info:
            fizzbuzz(0)
        assert "1以上である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_negative(self):
        """負の数でValueErrorが発生することをテスト"""
        with pytest.raises(ValueError) as exc_info:
            fizzbuzz(-5)
        assert "1以上である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_float(self):
        """浮動小数点数でTypeErrorが発生することをテスト"""
        with pytest.raises(TypeError) as exc_info:
            fizzbuzz(3.5)
        assert "整数である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_string(self):
        """文字列でTypeErrorが発生することをテスト"""
        with pytest.raises(TypeError) as exc_info:
            fizzbuzz("10")
        assert "整数である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_none(self):
        """NoneでTypeErrorが発生することをテスト"""
        with pytest.raises(TypeError) as exc_info:
            fizzbuzz(None)
        assert "整数である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_list(self):
        """リストでTypeErrorが発生することをテスト"""
        with pytest.raises(TypeError) as exc_info:
            fizzbuzz([1, 2, 3])
        assert "整数である必要があります" in str(exc_info.value)

    def test_fizzbuzz_with_dict(self):
        """辞書でTypeErrorが発生することをテスト"""
        with pytest.raises(TypeError) as exc_info:
            fizzbuzz({"n": 10})
        assert "整数である必要があります" in str(exc_info.value)


class TestPrintFizzBuzz:
    """print_fizzbuzz関数のテストクラス"""

    def test_print_fizzbuzz_output(self, capsys):
        """標準出力のテスト"""
        print_fizzbuzz(5)
        captured = capsys.readouterr()
        expected_output = "1\n2\nFizz\n4\nBuzz\n"
        assert captured.out == expected_output

    def test_print_fizzbuzz_validation(self):
        """print_fizzbuzzのバリデーションテスト"""
        with pytest.raises(ValueError):
            print_fizzbuzz(0)

        with pytest.raises(TypeError):
            print_fizzbuzz("invalid")
