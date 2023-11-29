import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (-1, -1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (35.5, 50.1, [4, 7])
        ],
        ids=[
            "Test if age is negative",
            "Test if 14 yo pet's have less than 1 human's year",
            "Test if 15 yo pet's are equal to 1 human's year",
            "Test if 23 yo pet's have less than 2 human's year",
            "Test if 24 yo pet's already have 2 human year's",
            "Test max age limit's for pets before condition changes",
            "Test min age limit's for pets after condition changes",
            "Test if function work with large number's correctly",
            "Test if function will work with float age"
        ],
    )
    def test_get_human_age(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestWrongData:
    def test_wrong_data_type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)
