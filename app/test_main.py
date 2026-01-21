import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_result",
    [
        (-20, -50, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (25, 27, [2, 2]),
        (44, 51, [7, 7]),
        (521, 1077, [126, 212])
    ],
    ids=[
        "-20 cats and -50 dogs years must convert to 0, 0 humans years",
        "0 cats and 0 dogs years must convert to 0, 0 humans years",
        "14 cats and 14 dogs years must convert to 0, 0 humans years",
        "23 cats and 23 dogs years must convert to 1, 1 humans years",
        "25 cats and 27 dogs years must convert to 2, 2 humans years",
        "44 cats and 51 dogs years must convert to 7, 7 humans years",
        "521 cats and 1077 dogs years must convert to 126, 212 humans years"
    ]
)
def test_should_correct_convert_animals_ages_to_humans(
    cat_years: int | float,
    dog_years: int | float,
    expected_result: list[int]
) -> None:
    assert (
        get_human_age(cat_years, dog_years) == expected_result
    )
