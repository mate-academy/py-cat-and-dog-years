import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cats_age, dogs_age, expected_result",
    [
        (0, 5, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (-1, -2, [0, 0]),
        ("one", "two", TypeError)

    ],

    ids=[
        "cats and dogs years less than 15",
        "cats and dogs years equal to 15 ",
        "cats and dogs years in range 16-23",
        "cats and dogs years equal to 23",
        "cats and dogs years in range 24-27",
        "cats and dogs have extra year",
        "cats and dogs age is negative number",
        "string ages should raise exception"
    ]
)
def test_cats_and_dogs_years(
        cats_age: int,
        dogs_age: int, expected_result: list
) -> None:
    if expected_result == TypeError:
        with pytest.raises(TypeError):
            get_human_age("one", "two")
    else:
        assert get_human_age(cats_age, dogs_age) == expected_result
