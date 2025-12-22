import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (1, 0, [0, 0]),
        (0, 1, [0, 0]),
        (14, 13, [0, 0]),
        (15, 15, [1, 1]),
        (23, 22, [1, 1]),
        (24, 24, [2, 2]),
        (26, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 6, [0, 0]),
        (6, -1, [0, 0])
    ]
)
def test_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        (1, "1", TypeError),
        ("14", 13, TypeError),
        (None, 15, TypeError),
        (23, None, TypeError)
    ]
)
def test_human_age_with_invalid_types(
        cat_age: int,
        dog_age: int,
        error: type(Exception)
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
