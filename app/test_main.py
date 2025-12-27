import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (18259, 5128, [4560, 1022]),
    ],
    ids=[
        "test negative value",
        "test zero value",
        "test result is zero",
        "test first year",
        "test second year",
        "test each year",
        "test large value",
        "test very large value",
    ]
)
def test_should_return_right_values(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("", ""),
        ([], []),
    ],
    ids=[
        "if inputs are strings",
        "if inputs are list",
    ]
)
def test_should_raise_error(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
