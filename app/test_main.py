import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_with_various_inputs(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_increments_every_four_years_after_twenty_four() -> None:
    # 24 years = 2 human years. 24 + 4 = 28 (should be 3 human years)
    assert get_human_age(28, 0)[0] == 3
    # 28 + 3 = 31 (still 3 human years because we discard remainder)
    assert get_human_age(31, 0)[0] == 3


def test_dog_age_increments_every_five_years_after_twenty_four() -> None:
    assert get_human_age(29, 29)[1] == 3
    assert get_human_age(33, 33)[1] == 3
