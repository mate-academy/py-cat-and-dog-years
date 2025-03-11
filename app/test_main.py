import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (40, 40, [6, 5]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat_0_and_dog_0_years",
        "cat_14_and_dog_14_years",
        "cat_15_and_dog_15_years",
        "cat_24_and_dog_24_years",
        "cat_28_and_dog_29_years",
        "cat_40_and_dog_40_years",
        "cat_100_and_dog_100_years",
    ],
)
def test_correct_result(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_result, (
        f"Incorrect result, must be {expected_result}"
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (0, 0),
        (14, 14),
        (15, 15),
    ],
    ids=[
        "cat_0_and_dog_0_years",
        "cat_14_and_dog_14_years",
        "cat_15_and_dog_15_years",
    ],
)
def test_correct_result_data_type(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list), "Result must be list"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15, 15),
        (28, 29),
        (40, 40),
    ],
    ids=[
        "cat_15_and_dog_15_years",
        "cat_28_and_dog_29_years",
        "cat_40_and_dog_40_years",
    ],
)
def test_data_types(cat_age: int, dog_age: int) -> None:
    assert isinstance(cat_age, int) and isinstance(dog_age, int), (
        "Animal age must be int"
    )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (10, 15),
        (28, 29),
        (12, 10),
    ],
)
def test_values_within_range(cat_age: int, dog_age: int) -> None:
    assert 0 <= cat_age <= 100 and 0 <= dog_age <= 100, (
        "Animal age must be in range from 1 to 100(including)"
    )
