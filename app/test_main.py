import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            (-2, -4, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "should check if the ages is negative",
            "should check if the ages is zero",
            "should check ages less then 15",
            "should check ages consists of 15 and 9",
            "should check ages, which include extra years",
            "should check few extra ages"
        ]
    )
    def test_interpetend_cat_and_dog_ages_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_list: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list

    def test_should_check_correct_type_arguments(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 2)
