from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 0, [1, 0]),
            (0, 15, [0, 1]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (100, 100, [21, 17])
        ],
        ids=[
            "should return zero if age is zero",
            "should return zero if age lower than 15",
            "should return zero only for dog if dog age lower than 15",
            "should return zero only for cat if cat age lower than 15",
            "should return ones",
            "should return ones if age lower than 24",
            "should return twos",
            "should return twos if cat age lower than 28 and if dog age lower than 29",
            "should return 3 for cat if age are equal 28",
            "should return 3 for dog if age are equal 29",
            "should return correct age"

        ]
    )
    def test_calculation_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age
