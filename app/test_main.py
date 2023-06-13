import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ([2], 8, TypeError),
        (10, [1], TypeError),
        ("hello", "13", TypeError)
    ]
)
def test_raise_error_if_value_types_are_incorrect(
        cat_age: int | list | str,
        dog_age: int | list | str,
        error: type[Exception]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (2, 8, [0, 0]),
        (10, 12, [0, 0]),
        (14, 13, [0, 0])
    ]
)
def test_human_age_should_be_zero_when_ages_below_15(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (16, 19, [1, 1]),
        (21, 22, [1, 1]),
        (17, 18, [1, 1])
    ]
)
def test_human_age_should_be_one_when_ages_below_23_and_above_15(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (24, 26, [2, 2]),
        (26, 24, [2, 2]),
        (25, 25, [2, 2])
    ]
)
def test_human_age_when_ages_above_23_and_below_28(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (14, 35, [0, 4])
    ]
)
def test_human_age_in_another_cases(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
