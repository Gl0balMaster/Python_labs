import pytest

def count_words(words):
    return len(words.split())


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("there is 4 words",4),
        ("there is     5 spaces and 7 words",7),
        ("tab   вместо    space",3),
        ("zeroSpaces",1),
        ("",0),

        ("sentence! with? signs,. ",3),

        ("123 456 789", 3),
        ("1 2 3 four five six", 6),

        ("first line\nsecond line", 4),


        ("a", 1),
        (" a ", 1),
        ("          ", 0)


    ])
class TestWordCount:
    def test_basic_functionality(self, string:str, expected:int) -> None:
        got = count_words(string)
        assert got == expected

    def test_non_negative_result(self, string:str, expected:int) -> None:
        got = count_words(string)
        assert got >= 0

    def test_consistency_result(self, string:str, expected:int) -> None:
        first_got = count_words(string)
        second_got = count_words(string)
        assert ((first_got == expected) and (second_got == expected))

def test_invalid_input() -> None:
    with pytest.raises(AttributeError):
        count_words(123)
    with pytest.raises(AttributeError):
        count_words(None)