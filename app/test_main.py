import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age_err, dog_age_err",
    [
        (14, "14"),
        ("15", 15),
        ([23], 23),
        (24, [24]),
    ]
)
def test_incorrect_data(
        cat_age_err: int | str | list,
        dog_age_err: int | str | list) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age_err, dog_age_err)
