"""Unit tests for invert, count, and favorite_colors functions in dictionary.py."""
__author__ = "730456646"

from exercises.ex06.dictionary import invert, count, favorite_color
import pytest


def test_key_value_switch_invert() -> None:
    """In a one item dictionary the key and value switch."""
    start_dict = {'cat': 'apple'}
    assert invert(start_dict) == {'apple': 'cat'}


def test_if_empty_invert() -> None:
    """In empty dictionary, an empty dictionary is return."""
    start_dict = {}
    assert invert(start_dict) == {}


def test_key_error_invert() -> None:
    """If there are multiple values, this will result in non-unique keys which should raise a key error."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_correct_count() -> None:
    """Given multiple examples of repeated strings, the function can count these correctly."""
    start_list = ["blue", "blue", "blue", "orange", "orange", "yellow", "orange", "black"]
    assert count(start_list) == {'blue': 3, 'orange': 3, "yellow": 1, "black": 1}


def test_empty_count() -> None:
    """Given empty list returns empty dict."""
    start_list = []
    assert count(start_list) == {}


def test_new_items_only_count() -> None:
    """Given a list with only unique colors, dictionary works accordingly."""
    start_list = ["blue", "orange", "yellow", "black"]
    assert count(start_list) == {'blue': 1, 'orange': 1, "yellow": 1, "black": 1}


def test_tie_favorite_color() -> None:
    """Given a tie in favorite colors, first one mentioned gets returns."""
    start_dict = {"Marc": "yellow", "Sarah": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(start_dict) == "yellow"


def test_largest_count_favorite_color() -> None:
    """The largest frequency of color gets returned correctly."""
    start_dict = {"Marc": "yellow", "Sarah": "yellow", "Ezri": "yellow", "Kris": "blue"}
    assert favorite_color(start_dict) == "yellow"


def test_empty_favorite_color() -> None:
    """Given an empty dict, returns empty dictionary."""
    start_dict = {}
    assert favorite_color(start_dict) == ""