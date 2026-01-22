import pytest

from app.main import get_human_age


class TestCountHumanAge:

    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_years",
        [
            (-1, -1, [0, 0]),
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
            "Should return 0, 0 when years less than 0",
            "Should return 0, 0 when years 0",
            "Should return 0, 0 when years less than 15",
            "Should return 1, 1 when years equal 15",
            "Should return 1, 1 when years less than 24",
            "Should return 2, 2 when years equal 24",
            "Should return 2, 2 when years less than 28",
            "Should return 3, 2 when years equal 28",
            "Should return 21, 17 when years equal 100",
        ]
    )
    def test_return_counting_of_human_years(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_years: list[int]
    ) -> None:
        result = get_human_age(initial_cat_age, initial_dog_age)
        assert result == expected_years, (f"{initial_cat_age} cat years and "
                                          f"{initial_dog_age} dog years "
                                          f"should be "
                                          f"{expected_years} human years.")

    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_error",
        [
            (10, "10", TypeError),
            (15, [8], TypeError),

        ],
        ids=[
            "Should return TypeError when age is string",
            "Should return TypeError when age is array",
        ]
    )
    def test_should_raise_expected_error(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_error: type(Exception)
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
