import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17]),
        (-50, 500000000000000000000000000000000000000000,
         [0, 99999999999999999999999999999999999999997])
    ],
    ids=[
        "zero values",
        "round for first year",
        "second year",
        "extra year",
        "negative and big value"
    ]
)
def test_values_for_get_human_age_func(cat_age: int,
                                       dog_age: int,
                                       result: list) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        (f"Human age for cat_age {cat_age} = {result[0]}, "
         f"for dog age {dog_age} = {result[1]}")


def test_wrong_values_for_get_human_age_func() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat_age", [0])
