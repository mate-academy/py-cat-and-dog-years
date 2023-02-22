import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (-1, -1, [0, 0]),
            (14, 1, [0, 0]),
            (23, 15, [1, 1]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (35.5, 50.1, [4, 7]),
        ],
        ids=[
            "Test if age is negative.",
            "Test if pets from 1 to 14 have less than 1 human's year",
            "Test if pets age from 15 to 23 are equal to 1 human's year",
            "Test if pet's age after 24 calculating correctly",
            "Test if function work with large number's correctly",
            "Test if function will work with float age",
        ],
    )
    def test_get_human_age(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestIncomingDataType:
    def test_wrong_data_type_str(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)

