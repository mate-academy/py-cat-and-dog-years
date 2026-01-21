import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_age",
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
            "should return correct value for 0 years old",
            "should return correct value for 14 years old",
            "should return correct value for 15 years old",
            "should return correct value for 23 years old",
            "should return correct value for 24 years old",
            "should return correct value for 27 years old",
            "should return correct value for 28 years old",
            "should return correct value for 100 years old"
        ]
    )
    def test_convert_to_human_age_correctly(
            self, cat_age: int, dog_age: int, expected_human_age: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            ("", "", TypeError),
            ([], [], TypeError)
        ],
        ids=[
            "should raise an error if parameters are strings",
            "should raise an error if parameters are lists"
        ]
    )
    def test_should_rise_a_value_error(
            self, cat_age: int, dog_age: int, expected_error: Exception
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
