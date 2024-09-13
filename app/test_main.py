import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (-1, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (14, 15, [0, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (20452371, 11, [5113088, 0]),
    ]
)
def test_convert_dog_or_cat_age(
        cat_age: int,
        dog_age: int,
        result: list | str
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Cat age on human should equal: {result[0]}, "
        f"dog age on human should equal: {result[1]}")


def test_should_raise_error_if_argument_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("131", 12)
