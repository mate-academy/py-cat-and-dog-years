import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0, 0, [0, 0], id="should not return values when out normal range"
        ),
        pytest.param(
            -1, -10, [0, 0], id="should not return values when out normal range"
        ),
        pytest.param(
            14, 14, [0, 0], id="should return the correct value at the range boundaries"
        ),
        pytest.param(
            23, 23, [1, 1], id="should return the correct value at the range boundaries"
        ),
        pytest.param(
            24, 24, [2, 2], id="should return the correct value at the range boundaries"
        ),
        pytest.param(
            27, 29, [2, 3], id="should return the correct value at the range boundaries"
        ),
        pytest.param(
            500, 500, [121, 97], id="should not return values when out normal range"
        )

    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "10", 5, TypeError, id="should raise TypeError when value not int"
        ),
        pytest.param(
            None, 5, TypeError, id="should raise TypeError when value is None"
        ),
    ]
)
def test_get_human_age_invalid_input(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
