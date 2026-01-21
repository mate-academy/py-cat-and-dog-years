import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
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
            "Invalid data should return 0",
            "Zeros for both at age 0",
            "Zeros for both under 15",
            "Ones for both at age 15",
            "Ones for both under 24",
            "Twos for both at age 24",
            "Twos for both under 28",
            "Three for cat and two for dog at age 28",
            "21 for cat and 17 for dog at age 100",
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           human_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ([], 12),
            (21, "PYTHONez"),
        ],
        ids=[
            "TypeError for age list",
            "TypeError for age string",
        ]
    )
    def test_for_invalid_data(self,
                              cat_age: int,
                              dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
