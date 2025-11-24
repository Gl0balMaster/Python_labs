import pytest

def is_anagram(word1: str, word2: str):
    let1 = dict()
    let2 = dict()

    if not isinstance(word1,str):
        raise ValueError
    if not isinstance(word2, str):
        raise ValueError

    for ch in word1:
        if let1.get(ch) is None:
            let1[ch] = 1
        else:
            let1[ch]+=1

    for ch in word2:
        if let2.get(ch) is None:
            let2[ch] = 1
        else:
            let2[ch]+=1

    for key, value in let1.items():
        if let2.get(key) != value:
            return False

    for key, value in let2.items():
        if let1.get(key) != value:
            return False
    return True

@pytest.mark.parametrize(
    ("word1","word2","expected"),
    [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("a", "a", True),
        ("a", "b", False),

        ("Listen", "silent", False),
        ("A", "a", False),

        ("hello world", "world hello", True),
        ("hello", "hello ", False),
        ("  hello", "hello  ", True),

        ("", "", True),
        ("", "a", False),
        ("a", "", False),

        ("a1b2", "2b1a", True),
        ("a!b", "b!a", True),
        ("asdasfasdasfasdasdasfasgasfasfasf", "askjdilsaiufhewuoifewuifniewowemf", False),
        ("asdasfasdasfasdasdasfasgasfasfasf", "asdasfasdasfasdasdasfasgasfasfasf", True)

    ]
)
class TestAnagramCheck:
    def test_is_anagram(self, word1: str,word2: str, expected: bool) -> None:
        result = is_anagram(word1, word2)
        assert result == expected

    def test_symmetry_property(self, word1: str, word2: str, expected: bool) -> None:
        result1 = is_anagram(word1, word2)
        result2 = is_anagram(word2, word1)
        assert result1 == result2

    def test_same_strings_are_anagrams(self, word1: str, word2: str, expected: bool) -> None:
        assert is_anagram(word1, word1) == True
        assert is_anagram(word2, word2) == True
    def test_consistency_result(self, word1: str, word2: str, expected: bool) -> None:
        first_got = is_anagram(word1,word2)
        second_got = is_anagram(word1,word2)
        assert ((first_got == expected) and (second_got == expected))

def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        is_anagram("123",123)
    with pytest.raises(ValueError):
        is_anagram(None,"123")
    with pytest.raises(ValueError):
        is_anagram(123.45,None)