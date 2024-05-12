import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (16, 9, [1, 0]),
        (8, 17, [0, 1]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (30, 31, [3, 3]),
        (28, 28, [3, 2]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("14", 14),
        (16, "9"),
        ([8], 17),
        (15, (15,)),
        (24, {"age": 24}),
    ],
)
def test_get_human_age_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
