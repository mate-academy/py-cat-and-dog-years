import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (24, 0, [2, 0]),
        (0, 24, [0, 2]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-15, 0, [0, 0]),
        (0, -15, [0, 0]),
    ]
)
def test_all_boundary_ages(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"{cat_age} cat years, should be {result[0]} human years, "
        f"{dog_age} dog years should be {result[1]} human years.")


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 0),
        (0, "15"),
        (None, 0),
        (0, None)
    ]
)
def test_invalid_data(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
