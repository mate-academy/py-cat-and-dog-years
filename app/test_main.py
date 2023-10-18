import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_nums",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 29, [2, 3]),
    ]
)
def test_human_age(cat_age: int,
                   dog_age: int,
                   expected_nums: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_nums


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 2),
        ([3], 9),
        (1, {4: 1}),
    ]
)
def test_type_human_age(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
