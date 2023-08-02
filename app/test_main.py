import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="both_zero_age"),
    pytest.param(14, 14, [0, 0], id="both_under_15_years"),
    pytest.param(15, 15, [1, 1], id="both_15_years"),
    pytest.param(23, 23, [1, 1], id="both_just_over_15_years"),
    pytest.param(24, 24, [2, 2], id="both_exactly_1_more_year"),
    pytest.param(27, 27, [2, 2], id="both_just_over_1_more_year"),
    pytest.param(28, 28, [3, 2], id="cat_1_more_year_than_dog"),
    pytest.param(100, 100, [21, 17], id="both_just_over_2_more_years"),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_values() -> None:
    with pytest.raises(ValueError):
        get_human_age(-5, 10)


def test_zero_values() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_large_values() -> None:
    assert get_human_age(2 ** 31 - 1, 2 ** 31 - 1) == [1073741858, 858993062]


def test_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", 14)
