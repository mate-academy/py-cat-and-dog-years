import pytest
from app.main import get_human_age


# write your code here

class TestCatDogAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_years",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (15.5, 15.5, [1, 1]),
            (-1, 3, 0),
            (3, -1, 0),
            (-1, -1, 0),
        ],
        ids=[
            "both ages are zero must be 0/0",
            "both ages are 14 must be 0/0",
            "both ages are 15 must be 1/1",
            "both ages are 23 must be 1/1",
            "both ages are 24 must be 2/2",
            "both ages are 27 must be 2/2",
            "both ages are 28 must be 3/2",
            "both ages are 100 must be 21/17",
            "both ages are 15.5 must be 1/1",
            "cat age is negative value",
            "dog age is negative value",
            "both ages is negative value",
        ]
    )
    def test_correct(
            self,
            cat_age: int,
            dog_age: int,
            expected_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_years

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            (3, None, TypeError),
        ],
        ids=[
            "One of ages is None value",
        ]
    )
    def test_incorrect(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: BaseException
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
