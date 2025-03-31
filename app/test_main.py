import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (20, 20, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_cat_and_dog_years_convert(
    cat_age: int,
    dog_age: int,
    result: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result
