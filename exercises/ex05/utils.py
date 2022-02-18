"""A variety of functions for ex05 and unit test practice which will be found in utils_test.py."""
__author__ = "730456646"


def only_evens(start_list: list[int]) -> list[int]:
    """Receives a start_list of integers and runs through and returns a list with only even integers."""
    even_list: list[int] = []
    for items in start_list:
        if items % 2 == 0:
            even_list.append(items)
    return even_list


def sub(start_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Will create sub list from start_index to end_index of start_list."""
    sub_list: list[int] = []
    if start_index < 0:
        i: int = 0
    else:
        i = start_index

    if end_index >= len(start_list):
        end_index = len(start_list) 
    
    if len(start_list) == 0 or start_index > len(start_list) or end_index <= 0:
        return sub_list

    while i < end_index:
        sub_list.append(start_list[i])
        i += 1
    return sub_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Functions concats first_list and second_list to create a new list that has all items of the first followed by all items of the second."""
    new_list: list[int] = []
    for items in first_list:
        new_list.append(items)
    for items in second_list:
        new_list.append(items)
    return new_list