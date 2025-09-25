import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,in_human_years",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, in_human_years: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == in_human_years
    ), f"Expected {in_human_years} and got {get_human_age(cat_age, dog_age)}"


def test_get_human_age_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "b")