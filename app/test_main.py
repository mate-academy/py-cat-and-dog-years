import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (-15, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (29, 28, [3, 2]),
        (32, 28, [4, 2]),
        (28, 30, [3, 3]),
        (28, 34, [3, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_result: list,
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("28", 29),
        (28, "29"),
        (None, 29),
        (28, None),
    ],
)
def test_get_human_age_raises_error_for_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
