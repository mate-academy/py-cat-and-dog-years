import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 30, [3, 3]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (-5, -5, [0, 0]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_get_human_age_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
