import pytest
from app.main import get_human_age


def test_human_age_for_zero_animal_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_human_age_for_14_animal_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_human_age_for_15_animal_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_human_age_for_23_animal_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_human_age_for_24_animal_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_human_age_for_27_animal_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_human_age_for_28_animal_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_human_age_for_100_animal_years() -> None:
    assert get_human_age(100, 100) == [21, 17]

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (50, 50, [8, 7]),
        (100, 100, [21, 17]),
    ]
)


def test_human_age_with_multiple_inputs(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
