import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # test_when_cat_and_dog_years_are_zeros
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "0 cat/dog years.",
        "-1 cat/dog years.",
        "14 cat/dog years.",
        "15 cat/dog years.",
        "23 cat/dog years.",
        "24 cat/dog years.",
        "27 cat/dog years.",
        "28 cat/dog years.",
        "100 cat/dog years."
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_with_invalid_param_type() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("14", "14") == [0, 0]
