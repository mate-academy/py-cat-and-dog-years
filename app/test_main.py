import pytest
from app.main import get_human_age


class TestCatDogYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (-1, -50, [0, 0]),
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
            "Negative age",
            "Zero age",
            "Same age",
            "Small age",
            "Medium age",
            "Medium age (next)",
            "Big age",
            "Big age (next)",
            "Very big age"
        ]
    )
    def test_human_age_is_correct(
            self, cat_age: int,
            dog_age: int,
            result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("one", "twenty", TypeError),
            ([1], [10], TypeError)
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
