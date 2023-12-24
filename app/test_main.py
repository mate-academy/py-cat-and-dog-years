import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (-10, -10, [0, 0]),
        (100000, 100000, [24996, 19997]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 27, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "(0, 0) zero should return [0, 0]",
        "(-10, -10) negative numbers should return [0, 0]",
        "(100000, 100000) big numbers return [24996, 19997]",
        "(14, 14) should return [0, 0]",
        "(15, 15) should return [1, 1]",
        "(23, 23) should return [1, 1]",
        "(24, 24) should return [2, 2]",
        "(28, 27) should return [3, 2]",
        "(100, 100) should return [21, 17]",
    ]
)
def test_different_data_range(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error_when_take_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("15.0", "15.0")
