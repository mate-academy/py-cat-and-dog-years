import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 29, [3, 3]),
            (50, 50, [8, 7]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "checking ages with zeroes parameters",
            "checking ages closest to one year parameters",
            "checking ages equal first year life",
            "checking ages before second year life",
            "checking ages equal second year life",
            "checking ages equal third year life",
            "checking ages with big parameters",
            "checking ages hundred parameters"
        ]
    )
    def test_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_value: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_error",
        [
            pytest.param("five", "ten", TypeError, id="cat & dog age == int")
        ]
    )
    def test_raising_errors_correctly(
            self,
            initial_cat_age: str,
            initial_dog_age: str,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
