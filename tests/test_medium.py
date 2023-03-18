"""pytest for medium difficulty python code"""
from src.medium import (
    sort,
    while_loop,
    zip_it_up,
    flatten,
    common_elements,
    second_largest_element,
    pythonic_common_characters,
    common_two,
    even_nums_list,
    my_reverse
)


def test_sort() -> None:
    assert sort([4, 2, 1, 3]) == [1, 2, 3, 4]


def test_sort_empty_array() -> None:
    assert sort([]) == []


def test_while_loop() -> None:
    assert while_loop(range(0, 99)) == False
    assert while_loop(range(100, 200)) == True


def test_zip_it_up_with_one() -> None:
    assert zip_it_up(["Cameron", "Kaily"], [1, 22]) == [("Cameron", 1), ("Kaily", 22)]


def test_flatten() -> None:
    assert flatten([[1, 2], [3, [4, 5]], 6, [7, 8, [9, 10, [11]]]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
    ]


def test_common_elements() -> None:
    assert common_elements(one=[1, 2, 3, 4], two=[3, 4, 5, 6]) == [3, 4]


def test_common_elements_with_nothing_in_common() -> None:
    assert common_elements([1, 2, 3, 4], [5, 6, 7, 8]) == []


def test_common_elements_with_empty_args() -> None:
    assert common_elements([], []) == []


def test_pythonic_common_characters() -> None:
    assert pythonic_common_characters("hello") == "l"


def test_second_largest_element() -> None:
    assert second_largest_element([0.5, 2, 4, 634, 35, 16, 124]) == 124


def test_second_largest_element_of_list_with_one_int() -> None:
    assert second_largest_element([1]) == None


def test_common_two() -> None:
    assert common_two([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_even_nums_list() -> None:
    assert even_nums_list([1,2,3,4,5,6]) == [2,4,6]

def test_even_nums_list_empty() -> None:
    assert even_nums_list([]) == []

def test_even_nums_list_empty() -> None:
    assert even_nums_list([1,3,5,7,9]) == []

def test_reversed() -> None:
    assert my_reverse([1, 2, 3, 4, 5]) == [5,4,3,2,1]