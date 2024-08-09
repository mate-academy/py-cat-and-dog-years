from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
    ]
)
def test_get_human_age_zero_years(
    cat_years: int, dog_years: int, expected: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected


class TestCatYearsToHumanYears:
    @pytest.mark.parametrize(
        "cat_years, expected_human_years",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (28, 3),
            (100, 21),
        ]
    )
    def test_cat_age(self, cat_years: int, expected_human_years: int) -> None:
        assert get_human_age(cat_years, 0)[0] == expected_human_years


class TestDogYearsToHumanYears:
    @pytest.mark.parametrize(
        "dog_years, expected_human_years",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (28, 2),
            (100, 17),
        ]
    )
    def test_dog_age(self, dog_years: int, expected_human_years: int) -> None:
        assert get_human_age(0, dog_years)[1] == expected_human_years
