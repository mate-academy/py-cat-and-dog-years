import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (35, 23, [4, 1]),
        (15, 14, [1, 0]),
        (24, 28, [2, 2]),
        (28, 41, [3, 5]),
        (0, 0, [0, 0]),
        (-10, -20, [0, 0]),
        (123, 456, [26, 88])
    ]
)
def test_can_calculate_age_correctly(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_should_raise_error_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", [20])
