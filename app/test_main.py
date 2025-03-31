import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0], id="Should return 0 when animals age equals 0"
        ),
        pytest.param(
            14, 14, [0, 0], id="Should return 0 when animals age < 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="Should return 1 when animals age between 15 and 23",
        ),
        pytest.param(
            24, 24, [2, 2], id="Should return 2 when animals age > 23"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="Should count age differently when cat and dog age 28",
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Should return [cat, dog] age as [21, 17] human age",
        ),
        pytest.param(-4, -4, [0, 0], id="Returns 0 if the value is negative"),
    ],
)
def test_conversion_to_human_years(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            [23], 23, TypeError, id="Age parameter should be integer, not list"
        ),
        pytest.param(
            27,
            "27",
            TypeError,
            id="Age parameter should be integer, not string",
        ),
    ],
)
def test_validates_the_the_right_data_entered(
    cat_age: int, dog_age: int, expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
