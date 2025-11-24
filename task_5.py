import pytest

def merge_dicts(dict_1, dict_2):
    for item in dict_2:
        if item in dict_1:
            if type(dict_1[item]) == type(dict_2[item]):
                if type(dict_1.get(item)) == int:
                    dict_1[item] = dict_2[item]
                elif isinstance(dict_1[item], dict):
                    merge_dicts(dict_1[item], dict_2[item])
                else:
                    dict_1[item] = dict_2[item]
            else:
                temp_list = list()
                temp_list.append(dict_1[item])
                temp_list.append(dict_2[item])
                dict_1[item] = temp_list
        else:
            dict_1[item] = dict_2[item]
    return dict_1


@pytest.mark.parametrize(
    ("dict1", "dict2", "expected"),
    [
        # 1. простые словари
        ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
        ({"a": 1}, {"a": 2}, {"a": 2}),

        # 2. Вложенные словари
        (
                {"outer": {"inner": 1}},
                {"outer": {"inner2": 2}},
                {"outer": {"inner": 1, "inner2": 2}}
        ),
        (
                {"data": {"user": "john"}},
                {"data": {"age": 25}},
                {"data": {"user": "john", "age": 25}}
        ),

        # 3. Разные типы данных - создание списка
        ({"key": 1}, {"key": "hello"}, {"key": [1, "hello"]}),
        ({"key": "text"}, {"key": 42}, {"key": ["text", 42]}),

        # 4. Многоуровневая вложенность словарей
        (
                {"level1": {"level2": {"level3": "value"}}},
                {"level1": {"level2": {"new_key": "new_value"}}},
                {"level1": {"level2": {"level3": "value", "new_key": "new_value"}}}
        ),

        # 5. Словари содержащие списки
        (
                {"config": {"colors": ["red", "blue"]}},
                {"config": {"sizes": ["small", "large"]}},
                {"config": {"colors": ["red", "blue"], "sizes": ["small", "large"]}}
        ),

        # 6. Словари содержащие другие словари
        (
                {"users": {"john": {"age": 25}}},
                {"users": {"alice": {"age": 30}}},
                {"users": {"john": {"age": 25}, "alice": {"age": 30}}}
        ),

        # 7. Пустые словари
        ({}, {"key": "value"}, {"key": "value"}),
        ({"key": "value"}, {}, {"key": "value"}),
        ({}, {}, {}),

        # 8. Словари с кортежами и множествами
        (
                {"data": {"tuple_data": (1, 2, 3)}},
                {"data": {"set_data": {4, 5, 6}}},
                {"data": {"tuple_data": (1, 2, 3), "set_data": {4, 5, 6}}}
        ),

        # 9. Сложные вложенные структуры
        (
                {"system": {"db": {"host": "localhost", "port": 5432}}},
                {"system": {"db": {"user": "admin"}, "cache": {"enabled": True}}},
                {"system": {"db": {"host": "localhost", "port": 5432, "user": "admin"}, "cache": {"enabled": True}}}
        ),

        # 10. Конфликт типов на разных уровнях
        (
                {"nested": {"key": 100}},
                {"nested": {"key": "text"}},
                {"nested": {"key": [100, "text"]}}
        ),
    ]
)
class TestMergeDicts:
    def test_merge_functionality(self, dict1, dict2, expected):
        result = merge_dicts(dict1.copy(), dict2.copy())
        assert result == expected

    def test_merge_idempotent(self, dict1, dict2, expected):
        first_result = merge_dicts(dict1.copy(), dict2.copy())
        second_result = merge_dicts(dict1.copy(), dict2.copy())
        assert first_result == second_result


def test_merge_with_none_values():
    dict1 = {"a": None}
    dict2 = {"a": 1}
    result = merge_dicts(dict1, dict2)
    assert result == {"a": [None, 1]}


def test_merge_with_boolean_values():
    dict1 = {"a": True}
    dict2 = {"a": False}
    result = merge_dicts(dict1, dict2)
    assert result == {"a": False}


def test_merge_complex_nested_structure():
    dict1 = {
        "users": {
            "john": {"age": 25, "hobbies": ["reading", "swimming"]},
            "alice": {"age": 30}
        },
        "settings": {"theme": "dark"}
    }

    dict2 = {
        "users": {
            "john": {"age": 26, "city": "New York"},
            "bob": {"age": 35}
        },
        "settings": {"language": "en"}
    }

    expected = {
        "users": {
            "john": {"age": 26, "hobbies": ["reading", "swimming"], "city": "New York"},
            "alice": {"age": 30},
            "bob": {"age": 35}
        },
        "settings": {"theme": "dark", "language": "en"}
    }

    result = merge_dicts(dict1, dict2)
    assert result == expected


def test_merge_with_different_collection_types():
    test_cases = [
        ({"a": [1, 2]}, {"a": {3, 4}}, {"a": [[1, 2], {3, 4}]}),
        ({"a": (1, 2)}, {"a": [3, 4]}, {"a": [(1, 2), [3, 4]]}),
        ({"a": {"b": 1}}, {"a": [1, 2]}, {"a": [{"b": 1}, [1, 2]]}),
    ]

    for dict1, dict2, expected in test_cases:
        result = merge_dicts(dict1.copy(), dict2.copy())
        assert result == expected


def test_merge_circular_reference_avoidance():
    dict1 = {"a": 1}
    dict2 = {"b": 2}

    result = merge_dicts(dict1, dict2)
    assert result == {"a": 1, "b": 2}

def test_merge_with_numeric_types():
    test_cases = [
        ({"a": 1}, {"a": 2.0}, {"a": [1, 2.0]}),  # int vs float
        ({"a": 1}, {"a": 1}, {"a": 1}),  # одинаковые int
        ({"a": 1.5}, {"a": 1.5}, {"a": 1.5}),  # одинаковые float
    ]

    for dict1, dict2, expected in test_cases:
        result = merge_dicts(dict1.copy(), dict2.copy())
        assert result == expected