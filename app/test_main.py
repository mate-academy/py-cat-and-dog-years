import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10, 31, [0, 3]),
        (31, 10, [3, 0]),
        (-10, -5, [0, 0]),
        (-10, 15, [0, 1]),
        (15, -10, [1, 0]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_result: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("6", 7),
        (6, "7"),
        (None, 7),
        (6, None),
    ],
)
def test_invalid_input_type(
    cat_age: int | str | None,
    dog_age: int | str | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
