import pytest

def palindrome_check(number : int):
    if not isinstance(number, int):
        raise ValueError
    num_as_str = str(number)
    for i in range(0, len(num_as_str)):
        if num_as_str[i] != num_as_str[len(num_as_str) - i - 1]:
            return False
    return True

@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (121, True),
        (12321, True),
        (123421, False),
        (1, True),
        (11, True),
        (12, False),
        (1234321, True),
        (123456, False),

        (1111111, True),

        (-121, False),
        (-12321, False),
        (-1, False),

    ]
)
class TestPalindromeCheck:
    def test_is_palindrome(self, number: int, expected: bool) -> None:
        assert palindrome_check(number) == expected

    def test_consistency_result(self, number: int, expected: bool) -> None:
        first_got = palindrome_check(number)
        second_got = palindrome_check(number)
        assert ((first_got == expected) and (second_got == expected))

    def test_result_boolean(self, number: int, expected: bool):
        result = palindrome_check(number)
        assert isinstance(result, bool)

def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        palindrome_check("123")
    with pytest.raises(ValueError):
        palindrome_check(None)
    with pytest.raises(ValueError):
        palindrome_check(123.45)