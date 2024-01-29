import pytest
from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
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
            "Any invalid input should result in a return value of 0",
            "At age 0 both values should be to 0",
            "For ages under 15 both values should be to 0",
            "At age 15 both values should be to 1",
            "For ages under 24 both values should be to 1",
            "At age 24 both values should be to 2",
            "For ages under 28 both values should be to 2",
            "At age 28 the value should be 3 and 2",
            "At age 100 the value should be 21 and 17",
        ]
    )
    def test_results_of_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("!", 8),
            (5, {9}),
        ],
        ids=[
            "TypeError for age string",
            "TypeError for age set",
        ]
    )
    def test_should_raise_expected_error(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
