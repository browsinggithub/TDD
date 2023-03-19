"medium difficulty python code"
from typing import List


def sort(numbers: List[int]) -> List[int]:
    """sort"""
    return sorted(numbers)


def while_loop(numbers: List[int]) -> bool:
    """while loop"""
    for x in numbers:
        if x < 100:
            return False
        if x > 100:
            return True


def zip_it_up(x: List[str], y: List[int]) -> List[tuple]:
    """zip it up function"""
    zipped = zip(x, y)
    new_list = list(zipped)
    return new_list


def flatten(first: List[List[int]]) -> List[int]:
    """takes list of nested lists of integers and flattens it out to a single list"""
    result = []
    for nested in first:
        if isinstance(nested, list):
            result.extend(flatten(nested))
        else:
            result.append(nested)
    return result


def common_elements(one: List[int], two: List[int]) -> List[int]:
    """ "take two lists as arguments, iterate through them and find 
        the common numbers in both of them"""
    new = []
    for num in one:
        if num in two and num not in new:
            new.append(num)
    return new


def pythonic_common_characters(word: str) -> str:
    """pythonic common characters"""
    return max(word, key=word.count)


def common_characters(word: str) -> str:
    """"common characters"""
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_count = max(char_count.values())
    max_chars = [char for char, count in char_count.items() if count == max_count]
    return max_chars[0]


def find_common_substring(word: str, consec: int) -> str:
    """find common substring"""
    substr_count = {}
    for i in range(len(word) - consec + 1):
        substr = word[i : i + consec]
        if substr in substr_count:
            substr_count[substr] += 1
        else:
            substr_count[substr] == 1

    max_count = max(substr_count.values())
    max_substr = [
        substr for substr, count in substr_count.items() if count == max_count
    ]
    return max_substr[0]


def second_largest_element(nums: List[int]) -> int or None:
    """second largest elements"""
    sorted_list = list(sort(nums))
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]


def common_two(one: List[int], two: List[int]) -> List[int]:
    """common two"""
    new = []
    for nums in one:
        if nums in two and nums not in new:
            new.append(nums)

    return new


def pythonic_common_two(one: List[int], two: List[int]) -> List[int]:
    """pythonic common two"""
    new = []
    return [num for num in one if num in two and num not in new]


def even_nums_list(nums: List[int]) -> List[int]:
    """even nums func"""
    return [x for x in nums if x % 2 == 0]


def my_reverse(nums: List[int]) -> List[int]:
    """reverse function"""
    left, right = (
        0,
        len(nums) - 1,
    )  # left and right vars are the first and last indices of the list nums
    while left < right:  # while 0 is less than len(nums)
        nums[left], nums[right] = (
            nums[right],
            nums[left],
        )  # swaps values at the left and right of the list nums
        left += (
            1  ## updates the values of left and right to move towards center of list
        )
        right -= 1
    return nums
