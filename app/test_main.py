import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
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
            "Should be zeros if years equal to 0",
            "Should be zeros if years less than 15",
            "Should be ones if years equal to 15",
            "Should be ones if years less than 24",
            "Should be twos if years equal to 24",
            "Should be twos if years less than 28",
            "Should be three for cat years and two for dog years "
            "if years equal to 28",
            "Should be 21 for cat years and 17 dog years "
            "if years equal to 100",
        ]
    )
    def test_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result, (
            f"For cat age {cat_age} and dog age {dog_age} "
            f"result should be {expected_result}"
        )
