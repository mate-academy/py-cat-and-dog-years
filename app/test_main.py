from app.main import get_human_age


def test_returns_zeroes_with_zeroes_as_arguments() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_not_counts_with_pre_basic_boundary_conditions() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_counts_with_lowest_boundary_conditions() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_not_counts_with_pre_2nd_boundary_conditions() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_counts_with_2nd_boundary_conditions() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_not_counts_with_pre_3rd_boundary_conditions() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_counts_for_cat_and_not_dog_with_3rd_boundary_conditions() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_counts_for_cat_and_dog_with_3rd_boundary_conditions() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_with_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
