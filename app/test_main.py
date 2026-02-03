import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("cat", "dog", TypeError),
        ("dog", "cat", TypeError),
    ],
)
def test_get_human_age_raises_type_error(cat_age: object, dog_age: object, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

@pytest.mark.parametrize("cat_age, dog_age", [(-1, 0), (0, -1), (-1, -1)])
def test_get_human_age_raises_value_error(cat_age, dog_age) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
