import pytest

def unique_amount(string):
    unique_set = set(string.split())
    return len(unique_set)

@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("qqq qqw qqe qwq qww qwe qeq qew qee wqq wqw wqe wwq www wwe eqq eqw eqe ewq eww ewe eeq eew eee",24),

        ("hello hello world", 2),
        ("Hello hello HELLO", 3),

        ("single", 1),
        ("", 0),

        ("  multiple   spaces  between  words  ", 4),
        ("a b c a b c",3)

    ])
class TestUniqueWordCount:
    def test_unique_amount(self, string: str, expected:int) -> None:
        got = unique_amount(string)
        assert got == expected

    def test_positive_result(self, string: str, expected:int) -> None:
        got = unique_amount(string)
        assert got >= 0

    def test_consistency_result(self, string:str, expected:int) -> None:
        first_got = unique_amount(string)
        second_got = unique_amount(string)
        assert ((first_got == expected) and (second_got == expected))


def test_case_sensitive() -> None:
    assert unique_amount("Hello HELLO heLLo") == 3

def test_whitespace_variations():
    assert unique_amount("hello world") == 2
    assert unique_amount("hello  world") == 2
    assert unique_amount("hello\tworld") == 2

def test_empty_cases():
    assert unique_amount("") == 0
    assert unique_amount("   ") == 0

def test_duplicates_only():
    assert unique_amount("word word word") == 1
    assert unique_amount("a a a b b b") == 2
