import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            (-1, -2, [0, 0]),
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
            "Numbers should be positive",
            "All zero",
            "Age < 15",
            "First human age",
            "First human age",
            "Second human age",
            "Second human age",
            "Third human age",
            "Very old age",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ([], "age"),
            (25, {}),
        ],
        ids=[
            "TypeError for age list and string",
            "TypeError for age dict",
        ]
    )
    def test_incorrect_data(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
