"""Unit tests for utils.py functions for ex05."""
__author__ = "730456646"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_odds_only_evens() -> None:
    """In a list of all odd numbers, function will return empty string."""
    start_list = [3, 7, 9, 13]
    assert only_evens(start_list) == []


def test_evens_and_odds_only_evens() -> None:
    """In a list with both even and odd numbers, function will return just even numbers."""
    start_list = [1, 4, 5, 13, 16, 18, 21]
    assert only_evens(start_list) == [4, 16, 18]


def test_empty_only_evens() -> None:
    """In an empty list, the function will return an empty list."""
    start_list = []
    assert only_evens(start_list) == []


def test_negative_start_sub() -> None:
    """If start index is negative, function will return list at start index 0."""
    start_list = [2, 4, 6, 8, 10, 12]
    assert sub(start_list, -2, 3) == [2, 4, 6]


def test_end_too_large_sub() -> None:
    """If end index is larger than end index than function will return list froms start index to the end of the list."""
    start_list = [2, 4, 6, 8, 10, 12]
    assert sub(start_list, 1, 8) == [4, 6, 8, 10, 12]


def test_list_empty_sub() -> None:
    """If list is empty, start is greater than length return empty list."""
    start_list = []
    assert sub(start_list, 1, 3) == []


def test_two_empty_list_concat() -> None:
    """If both lists are empty, return empty list."""
    first_list = []
    second_list = []
    assert concat(first_list, second_list) == []


def test_two_lists_concat() -> None:
    """If given two lists they concat consecutively."""
    first_list = [1, 2, 3]
    second_list = [4, 5, 6]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6]


def test_two_length_lists_concat() -> None:
    """If given two lists with two different lengths, concatenation list length will the total of both original lists indeces."""
    first_list = [1, 2]
    second_list = [3, 4, 5, 6]
    assert len(concat(first_list, second_list)) == (len(first_list) + len(second_list))
