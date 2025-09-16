import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# capitalize ================
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("тЕСТирование", "Тестирование"),
    ("a", "A")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("SkyPro", "Skypro"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# trim ==================
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" skypro", "skypro"),
    ("skypro", "skypro"),
    ("\tskypro", "\tskypro"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("skypro   ", "skypro   "),
    ("  sky  pro  ", "sky  pro  "),
])
def test_trim_negative(input_str, expected):
     assert string_utils.trim(input_str) == expected

# contains ================
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "o", True),
    ("SkyPro", "y", True),
    ("Hello World", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("SkyPro", "sky", False),
   ])
def test_contains_negative(string, symbol, expected):
     assert string_utils.contains(string, symbol) == expected

# delete_symbol =================
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("aaa", "a", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("SkyPro", "", "SkyPro"),
    ("SkyPro", "sky", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

