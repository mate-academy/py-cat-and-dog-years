import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
    ]
)
def test_age_below_15(cat_age: int,
                      dog_age: int,
                      expected: list
                      ) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
    ]
)
def test_boundary_age_between_15_and_23(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (28, 28, [3, 2]),
        (29, 28, [3, 2]),
        (29, 30, [3, 3]),
        (50, 50, [8, 7]),
        (100, 100, [21, 17])
    ]
)
def test_last_boundary_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_only_one_age_are_boundary() -> None:
    assert get_human_age(24, 14) == [2, 0]
    assert get_human_age(14, 24) == [0, 2]
