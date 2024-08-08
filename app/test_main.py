import pytest
from app.main import get_human_age


# write your code here

class TestCatDogAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_cat_human,expected_dog_human",
        [
            (0, 0, 0, 0),
            (14, 14, 0, 0),
            (15, 15, 1, 1),
            (23, 23, 1, 1),
            (24, 24, 2, 2),
            (27, 27, 2, 2),
            (28, 28, 3, 2),
            (100, 100, 21, 17),
            (15.1, 15.5, 1, 1),
        ]
    )
    def test_correct(
            self,
            cat_age: int,
            dog_age: int,
            expected_cat_human: int,
            expected_dog_human: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [
            expected_cat_human,
            expected_dog_human
        ]
