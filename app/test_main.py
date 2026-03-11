import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 12, [2, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (44, 58, [7, 8]),
        (100, 100, [21, 17])
    ], ids=[
        "should return zeros when negative ages",
        "should return zeros when ages is zero",
        "should return zeros when ages less than 15",
        "should return ones when ages exactly 15",
        "should return two and zero when different ages in this scenario",
        "should return ones when ages greater-equal than 15 and less than 24",
        "should return two in equal ages when below 28",
        "should return two in equal ages when right before 28",
        "should return proper year in different species rules",
        "should return proper year when different ages",
        "should return proper human age when cat and dogs ages is very high"
    ]
)
def test_should_calculate_proper_human_age(
        cat_age: int,
        dog_age: int,
        expected_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


def test_should_raise_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "3")
