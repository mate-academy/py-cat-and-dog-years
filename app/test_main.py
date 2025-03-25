import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,human_age",
    [
        (
            0, 0, [0, 0]
        ),
        (
            14, 14, [0, 0]
        ),
        (
            15, 15, [1, 1]
        ),
        (
            23, 23, [1, 1]
        ),
        (
            24, 24, [2, 2]
        ),
        (
            27, 27, [2, 2]
        ),
        (
            28, 28, [3, 2]
        ),
        (
            100, 100, [21, 17]
        )
    ]
)
def test_convert_correctly(cat_years: int,
                           dog_years: int,
                           human_age: list) -> None:

    assert get_human_age(cat_years, dog_years) == human_age, \
        f"Should return {human_age}, when cat age is " \
        f"{cat_years} and dog age is {dog_years}"
