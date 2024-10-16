import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "Age of the cat/dog == 0/0 should convert into 0.",
            "Age of the cat/dog == 14/14 should convert into 0.",
            "Age of the cat/dog == 15/15 should convert into 1.",
            "Age of the cat/dog == 23/23 should convert into 1.",
            "Age of the cat/dog == 24/24 should convert into 2.",
            "Age of the cat/dog == 27/27 should convert into 2.",
            "Age of the cat/dog == 28/28 should convert into 3/2.",
            "Age of the cat/dog == 100/100 should convert into 21/17."
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected, (
            f"Age of cat {cat_age} and age of dog "
            f"{dog_age} should return {expected}"
        )

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (-2, 5, [0, 0]),
            (10, -1, [0, 0]),
            (-15, -6, [0, 0]),
            (550, 550, [133, 107]),
            (1200, 1500, [296, 297])
        ],
        ids=[
            "Age of cat can't be less than 0",
            "Age of dog can't be less than 0",
            "Age of cat and dog can't be less than 0",
            "Age of cat and dog can't be more than 100",
            "Age of cat and dog can't be more than 100",
        ]
    )
    def test_get_negative_or_very_high_value(self,
                                             cat_age: int,
                                             dog_age: int,
                                             expected: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("one", 5, TypeError),
            (10, (1,), TypeError),
            ([15], 6, TypeError),
            ("eleven", "eight", TypeError),
            ({}, 17, TypeError)
        ],
        ids=[
            "Age of cat == string, not int",
            "Age of dog == tuple, not int",
            "Age of cat == list, not int",
            "Age of cat and dog == string, not int",
            "Age of cat == dict, not int",
        ]
    )
    def test_incorrect_value(self,
                             cat_age: any,
                             dog_age: any,
                             expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
