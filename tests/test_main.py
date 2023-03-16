"""Test"""
from bank.main import total, total_using_for_loop, list_with_delimiter, percentage, square_root


def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    "Total of a single item list should be the first items value"
    assert total([110.0]) == 110.0


def test_total_double_item() -> None:
    """Test"""
    assert total([1, 2, 3]) == 6.0


def test_total_using_for_loop_one_item() -> None:
    """Test"""
    assert total_using_for_loop([1.0]) == 1.0


def test_total_using_for_loop_two_items() -> None:
    """Test"""
    assert total_using_for_loop([100.0, 123.00]) == 223.00


def test_list_with_delimiter_use_case() -> None:
    """Test"""
    assert list_with_delimiter([1, 2, 3], ", ") == "1, 2, 3"


def test_list_with_delimiter_edge_case() -> None:
    """Test"""
    assert list_with_delimiter([1, 2, 3], "") == "123"


def test_list_with_delimiter_use_two() -> None:
    """Test"""
    assert list_with_delimiter([1, 2, 3], "-") == "1-2-3"


def test_percentage() -> None:
    """Test"""
    assert percentage(100, 10.0) == 10.0


def test_percentage_with_zero() -> None:
    """Test"""
    assert percentage(100, 0.0) == 0.0


def test_percentage_with_above_100_percent() -> None:
    """Test"""
    assert percentage(100, 110.0) == 110.0


def test_square() -> None:
    """Test"""
    assert square_root(5,2) == 25


def test_square_of_zero() -> None:
    """Test"""
    assert square_root(5,0) == 1


def test_square_of_one() -> None:
    """Test"""
    assert square_root(5,1) == 5

def test_square_by_three() -> None:
    """Test"""
    assert square_root(5,3) == 125
    