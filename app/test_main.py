import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-5, -5, [0, 0]),
        ]
    )
    def test_age_animal_to_human(self,
                                 cat_age: int,
                                 dog_age: int,
                                 expected_age: list[int]
                                 ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_exception",
        [
            ("2", 2, TypeError),
            (1, "1", TypeError),
        ]
    )
    def test_incorrect_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_exception: Exception
                           ) -> None:

        with pytest.raises(expected_exception):
            get_human_age(cat_age, dog_age)
