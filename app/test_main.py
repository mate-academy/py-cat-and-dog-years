from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),

        ],
        ids=[
            "both_zero",
            "both_14_years",
            "both_15_years",
            "both_23_years",
            "both_24_years",
            "both_27_years",
            "cat_28_years_dog_28_years",
            "both_100_years"
        ]
    )
    def test_correct_behavior(
        self,
        cat_years: int,
        dog_years: int,
        expected: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected

    @pytest.mark.parametrize(
        "cat_years, dog_years, expected",
        [
            (-1, 0, [0, 0]),
            (0, -1, [0, 0]),
            (-10, -10, [0, 0]),
            (15.5, 15, [1, 1]),
            (15, 15.5, [1, 1]),
        ],
        ids=[
            "negative_cat_years",
            "negative_dog_years",
            "both_negative_years",
            "float_cat_years",
            "float_dog_years",
        ]
    )
    def test_invalid_input(
        self,
        cat_years: int,
        dog_years: int,
        expected: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected

    @pytest.mark.parametrize(
        "cat_years, dog_years",
        [
            ("cat", 0),
            (0, "dog"),
        ],
        ids=[
            "non_integer_cat_years",
            "non_integer_dog_years",
        ]
    )
    def test_non_integer_input(
        self,
        cat_years: str | int,
        dog_years: str | int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_years, dog_years)
