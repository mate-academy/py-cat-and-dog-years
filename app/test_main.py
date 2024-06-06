from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-2, -5, [0, 0])
    ]
)
def test_human_age_in_cat_and_dog_age(cat_age: int, dog_age: int, result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ("1", 2, TypeError),
        (3, None, TypeError),
    ]
)
def test_func_wait_int(cat_age: int, dog_age: int, error: type(TypeError)) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
