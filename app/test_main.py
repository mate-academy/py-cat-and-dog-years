from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 0, [1, 0]),
            (0, 15, [0, 1]),
            (100, 100, [21, 17]),
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
        "cat_years, dog_years, expected_exception",
        [
            (-1, 0, ValueError),
            (0, -1, ValueError),
            (-10, -10, ValueError),
            ("cat", 0, TypeError),
            (0, "dog", TypeError),
        ]
    )
    def test_invalid_input(
        self,
        cat_years: int,
        dog_years: int,
        expected_exception: type[Exception]
    ) -> None:
        with pytest.raises(expected_exception):
            get_human_age(cat_years, dog_years)
