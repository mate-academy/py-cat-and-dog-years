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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-144, -144, [0, 0])



    ]
)
def test_different_mind_get_human_age(cat_age: int,
                                      dog_age: int,
                                      result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        ("15", 15, TypeError),
        (15, "15", TypeError),
        ("15", "15", TypeError),
        ([15], 15, TypeError),
        (15, [15], TypeError),
    ]
)
def test_error_get_human_age(cat_age: int,
                             dog_age: int,
                             exception: Exception) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
