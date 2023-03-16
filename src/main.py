"""example test"""
from typing import List


def total(iterable: List[float]) -> float:
    """total"""
    return sum(iterable)


def total_using_for_loop(iterable: List[float]) -> float:
    """total using for loop"""
    result: float = 0.0
    for items in iterable:
        result += items
    return result

# with skeleton function we should know our type of result
# and return that specific type ie: str, float


def list_with_delimiter(iterable: List[float], delimiter: str) -> str:
    """delimit list"""
    string: str = ""
    for items in iterable:
        if string == "":  # don't put delimiter before first item
            string = str(items)
        else:
            string += delimiter + str(items)
    return string


def percentage(num: float, percent: float):
    """percentage arithmetic"""
    combined = num * (percent/100)
    return round(combined, 1)


def square_root(num: int, square: int) -> float:
    """square of a number"""
    return num ** square

def list_creation(numbers: int) -> List[int]:
    """test list comprehension"""
    x = [x for x in range(numbers)]
    return x

def length_of_string(word:str ) -> int:
    """len"""
    return len(word)

def map_function(ints: List[int]) -> List[int]:
    """map func"""
    return list(map(lambda n: n * 2, ints))