import pytest

from app.main import get_human_age


def test_values_must_be_integers() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("15", "abcdefg")


def test_one_year_equals_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_less_than_fifteen_years_equal_zero() -> None:
    assert get_human_age(5, 5) == [0, 0]


def test_zero_equals_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_basic_set_of_integers(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, -17),
        (-28, -78)
    ]
)
def test_handles_negative_age(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (17, 14, [1, 0]),
        (1, 25, [0, 2])
    ]
)
def test_different_values_return_different_lists(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (9.162, 23.739, [0, 1]),
        (27.54, 30.44, [2, 2])
    ]
)
def test_func_rounds_floats_into_integers(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (56, 0, [8, 0]),
        (0, 73, [0, 10]),
        (42, 90, [5, 14]),
        (60, 30, [9, 2])
    ]
)
def test_counts_big_age_values_correctly(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (999999, -9999999, [249994, 0]),
        (9999999, 100000000000, [2499994, 19999999996])
    ]
)
def test_counts_large_age_values_correctly(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result
