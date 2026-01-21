import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-3, -5, [0, 0])
    ],
    ids=[
        "cat and dog age as zeros",
        "cat and dog age as 14",
        "cat and dog age as 15",
        "cat and dog age as 23",
        "cat and dog age as 24",
        "cat and dog age as 27",
        "cat and dog age as 28",
        "cat and dog age as 100",
        "cat and dog age as -3 and -5 respectively"
    ]
)
def test_can_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Convert of cat_age={cat_age} and "
        f"dog_age={dog_age} should equal to {result}")


def test_cannot_use_cat_age_as_str() -> None:
    with pytest.raises(TypeError):
        get_human_age("-3", 3)


def test_cannot_use_dog_age_as_str() -> None:
    with pytest.raises(TypeError):
        get_human_age(5, "5")
