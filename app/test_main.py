import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (100000, 100000, [24996, 19997]),

        (14, 10, [0, 0]),
        (15, 10, [1, 0]),
        (23, 10, [1, 0]),
        (24, 10, [2, 0]),
        (27, 10, [2, 0]),
        (28, 10, [3, 0]),

        (10, 14, [0, 0]),
        (10, 15, [0, 1]),
        (10, 23, [0, 1]),
        (10, 24, [0, 2]),
        (10, 28, [0, 2]),
        (10, 29, [0, 3]),
    ]
)
def test_get_human_age_calculations(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_get_human_age_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")


def test_get_human_age_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)
