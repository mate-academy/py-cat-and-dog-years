import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (15, 46, [1, 6]),
        ]
    )
    def test_calculating_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == result
        ), (f"List of {cat_age} years old cat "
            f"and {dog_age} years old dog should be equal to {result}")

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            (-1, -5, ValueError),
            (35, 200, ValueError),
            ("sdfsd", -5, TypeError),
            (True, 15, TypeError)
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)