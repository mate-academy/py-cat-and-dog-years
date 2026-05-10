from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (19, 19, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_basic_parametrized_structure(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        (-1, 0, ValueError),
        (0, -1, ValueError),
        ("cat", "dog", TypeError),
    ]
)
def test_edged_situations(
        cat_age: int | str,
        dog_age: int | str,
        error: type[Exception]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
