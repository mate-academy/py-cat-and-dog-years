import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-3, -3, [0, 0]),
        (150, 150, [33, 27])
    ],
    ids=[
        "0 cat and dog years",
        "14 cat and dog years",
        "15 cat and dog years",
        "23 cat and dog years",
        "24 cat and dog years",
        "27 cat and dog years",
        "28 cat and dog years",
        "100 cat and dog years",
        "-3 cat and dog years",
        "150 cat and dog years"
    ]
)
def test_can_convert(cat_years: int, dog_years: int, result: list) -> None:
    assert (
        get_human_age(cat_years, dog_years) == result
    ), f"Convert {cat_years} cat and {dog_years} dog "
    "years should be equal {result}"


def test_cannot_convert_str_and_str() -> None:
    with pytest.raises(TypeError):
        get_human_age("dog", "cat")


def test_cannot_convert_list_and_list() -> None:
    with pytest.raises(TypeError):
        get_human_age([10], [10])
